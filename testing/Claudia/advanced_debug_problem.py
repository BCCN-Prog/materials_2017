import numpy as np
import pdb

def inner_rk(run_time, state, f_max, dt, rko):
    dtype = np.float64
    #pdb.set_trace()
    n_steps = int(run_time // dt)
    print('RK{}: {} seconds in {} steps'.format(rko, run_time, n_steps))
    if rko == 4:
        kc = np.array([0., 1./2. * dt, 1./2. * dt, dt], dtype=dtype)
        update = '{post} + dt * (k1 + 2*k2 + 2*k3 + k4)'
    else:
        kc = np.array([0., 2./3. * dt], dtype=dtype)
        update = '{post} + dt * (k1 + 3*k2)'

    results = {pn: np.empty((r.size, n_steps), dtype=dtype) for pn, r in state['rate'].items()}
    dy = {post: ('tau_inv*(' + ('in_{post} + ' if post in state['input'] else '')
                 + ' + '.join('h_'+pre for pre in all_pre.keys())+' - {post})').format(post=post)
          for post, all_pre in state['conn'].items()}
    hd = {post: {pre: np.zeros_like(state['rate'][post]) for pre in all_pre}
          for post, all_pre in state['conn'].items()}
    rates = state['rate']

    def make_partial(c, post, pre):
        from scipy.sparse import csr_matrix
        from functools import partial
        if isinstance(c, csr_matrix):
            
            #return partial(csr_matvec, c.shape[0], c.shape[1], c.indptr, c.indices, c.data, rates[pre], hd[post][pre])
            return partial(csr_matrix, c.shape[0], c.shape[1], c.indptr, c.indices, c.data, rates[pre], hd[post][pre])
        else:
            return partial(np.dot, c, rates[pre], hd[post][pre])
    dots = {post: {pre: make_partial(conn, post, pre) for pre, conn in all_pre.items()}
            for post, all_pre in state['conn'].items()}
    ud = {}
    for post, pd in hd.items():
        ud[post] = {'h_'+pre: h for pre, h in pd.items()}
        ud[post]['dt'] = dtype(dt/6.) if rko == 4 else dtype(dt/4.)
        ud[post][post] = state['rate'][post]
        ud[post]['tau_inv'] = dtype(1 / 10e-3)
        ka = np.zeros((rko + 1, state['rate'][post].size), dtype=dtype)
        ud[post]['k'] = ka
        ud[post].update({'k{}'.format(i): ka[i, :] for i in range(ka.shape[0])})
        if post in state['input']:
            ud[post]['in_'+post] = state['input'][post]
    for n in range(n_steps):
        for k in range(1, rko+1):
            def get_r(pn):
                return rates[pn] + kc[k - 1] * ud[pn]['k'][k - 1, :]
            [h.fill(0.) for post, all_pre in hd.items() for h in all_pre.values()]
            [dot() for post, all_pre in dots.items() for dot in all_pre.values()]
            for post, rule in dy.items():
                ld = dict(ud[post])
                ld[post] = get_r(post)
                ne.evaluate(rule, local_dict=ld, out=ud[post]['k'][k, :])
        for post, rule in dy.items():
            ne.evaluate(update.format(post=post), local_dict=ud[post], out=rates[post])
            np.clip(rates[post], 0.0, f_max, rates[post])
            results[post][:, n] = rates[post]

    return results




def make_state():
    #from snep.library.rates.utils import compute_connections, dtype
    dtype = np.float64()
    from scipy.sparse import csr_matrix
    check_sanity = 0
    single_array = 1
    if check_sanity:
        n_pc = n_pv = n_som = n_vip = 5
    else:
        n_pc = 317
        n_pv = 15
        n_som = 12
        n_vip = 16
    pops = ['pc', 'pv', 'som', 'vip']
    pop_n = {'pc': n_pc, 'pv': n_pv, 'som': n_som, 'vip': n_vip}
    r_pc = np.zeros(n_pc, dtype=dtype)
    r_pv = np.zeros(n_pv, dtype=dtype)
    r_som = np.zeros(n_som, dtype=dtype)
    r_vip = np.zeros(n_vip, dtype=dtype)
    conn_d = dict(sparse=False, scale=np.infty, f_global=0., d_pre=1., d_post=1., scalar_data=False, fixed_in=True,
                  j_scale=False)
    state = {'pops': pops,
             'n': pop_n,
             'rate': {'pc':  r_pc,
                      'pv':  r_pv,
                      'som': r_som,
                      'vip': r_vip},
             'input': {'pc':  10*np.ones_like(r_pc),
                       # 'pv':  np.zeros_like(r_pv),
                       # 'som': np.zeros_like(r_som),
                       'vip': 1.2*np.ones_like(r_vip)},
             'conn': {'pc': {'pc': dict(conn_d, p=.1, J=.5),
                             'pv': dict(conn_d, p=.6, J=-1.),
                             # 'som': dict(conn_d, p=.55, J=-1.)
                             },
                      'pv': {'pc': dict(conn_d, p=.45, J=1.),
                             'pv': dict(conn_d, p=.5, J=-1.),
                             'som': dict(conn_d, p=.6, J=-1.)},
                      'som': {'pc': dict(conn_d, p=.35, J=.9),
                              'vip': dict(conn_d, p=.5, J=-1.)},
                      'vip': {'pc': dict(conn_d, p=.1, J=.8),
                              # 'pv': dict(conn_d, p=.1, J=0.),
                              'som': dict(conn_d, p=.45, J=-1.)}
                      }
             }
    for post, all_pre in state['conn'].items():
        for pre in all_pre:
            cd = all_pre[pre]
            if check_sanity:
                cd['p'] = 1.
            cd['zero_diagonal'] = pre == post
            cd['N_pre'] = state['n'][pre]
            cd['N_post'] = state['n'][post]
            cd['J'] /= cd['p'] * (state['n'][pre] - 1 if pre == post else state['n'][pre])
            #all_pre[pre] = compute_connections(**cd)[0]
            my_c = np.zeros((cd['N_post'], cd['N_pre']))
            my_ps= np.random.uniform(size= cd['N_pre'] *cd['N_post']).reshape((cd['N_post'], cd['N_pre'])) 
            my_probablilty_of_connectivity = 1.1
            my_c[my_ps<my_probablilty_of_connectivity] = cd['J']
            print(cd['J'])
            all_pre[pre] = my_c
            
            
    if single_array:
        p_i = {pn: i for i, pn in enumerate(pops)}
        ns = np.array([0] + [state['n'][pn] for pn in pops])
        n = ns.sum()
        idx = np.cumsum(ns)
        c = np.zeros((n, n), dtype=dtype)
        for post in state['conn']:
            i = p_i[post]
            for pre in state['conn'][post]:
                #pdb.set_trace()
                j = p_i[pre]
                cpp = state['conn'][post][pre]
                c[idx[i]:idx[i+1], idx[j]:idx[j+1]] = cpp
        c = csr_matrix(c)
        r_in = np.zeros(n, dtype=dtype)
        for pn in state['input']:
            i = p_i[pn]
            r_in[idx[i]: idx[i+1]] = state['input'][pn]
        state['pops'] = ['all']
        state['n'] = {'all': n}
        state['conn'] = {'all': {'all': c}}
        state['input'] = {'all': r_in}
        state['rate'] = {'all': np.zeros(n, dtype=dtype)}
        state['sub'] = {'all': idx}
        state['spn'] = {'all': pops}
    else:
        state['sub'] = {pn: np.array([0, n]) for pn, n in state['n'].items()}
        state['spn'] = {pn: [pn] for pn, n in state['n'].items()}
    return state


st = make_state()
ans = inner_rk(10., st, 10., 0.1, 2)
