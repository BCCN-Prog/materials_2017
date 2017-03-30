def genfromtxt(fname, dtype=float, comments='#', delimiter=None,
               skip_header=0, skip_footer=0, converters=None,
               missing_values=None, filling_values=None, usecols=None,
               names=None, excludelist=None, deletechars=None,
               replace_space='_', autostrip=False, case_sensitive=True,
               defaultfmt="f%i", unpack=None, ndmin=0, usemask=False, loose=True,
               invalid_raise=True, max_rows=None):
    """
    Load data from a text file, with missing values handled as specified.

    Each line past the first `skip_header` lines is split at the `delimiter`
    character, and characters following the `comments` character are discarded.

    Parameters
    ----------
    fname : file, str, pathlib.Path, list of str, generator
        File, filename, list, or generator to read.  If the filename
        extension is `.gz` or `.bz2`, the file is first decompressed. Note
        that generators must return byte strings in Python 3k.  The strings
        in a list or produced by a generator are treated as lines.
    dtype : dtype, optional
        Data type of the resulting array.
        If None, the dtypes will be determined by the contents of each
        column, individually.
    comments : str, optional
        The character used to indicate the start of a comment.
        All the characters occurring on a line after a comment are discarded
    delimiter : str, int, or sequence, optional
        The string used to separate values.  By default, any consecutive
        whitespaces act as delimiter.  An integer or sequence of integers
        can also be provided as width(s) of each field.
    skiprows : int, optional
        `skiprows` was removed in numpy 1.10. Please use `skip_header` instead.
    skip_header : int, optional
        The number of lines to skip at the beginning of the file.
    skip_footer : int, optional
        The number of lines to skip at the end of the file.
    converters : variable, optional
        The set of functions that convert the data of a column to a value.
        The converters can also be used to provide a default value
        for missing data: ``converters = {3: lambda s: float(s or 0)}``.
    missing : variable, optional
        `missing` was removed in numpy 1.10. Please use `missing_values`
        instead.
    missing_values : variable, optional
        The set of strings corresponding to missing data.
    filling_values : variable, optional
        The set of values to be used as default when the data are missing.
    usecols : sequence, optional
        Which columns to read, with 0 being the first.  For example,
        ``usecols = (1, 4, 5)`` will extract the 2nd, 5th and 6th columns.
    names : {None, True, str, sequence}, optional
        If `names` is True, the field names are read from the first valid line
        after the first `skip_header` lines.
        If `names` is a sequence or a single-string of comma-separated names,
        the names will be used to define the field names in a structured dtype.
        If `names` is None, the names of the dtype fields will be used, if any.
    excludelist : sequence, optional
        A list of names to exclude. This list is appended to the default list
        ['return','file','print']. Excluded names are appended an underscore:
        for example, `file` would become `file_`.
    deletechars : str, optional
        A string combining invalid characters that must be deleted from the
        names.
    defaultfmt : str, optional
        A format used to define default field names, such as "f%i" or "f_%02i".
    autostrip : bool, optional
        Whether to automatically strip white spaces from the variables.
    replace_space : char, optional
        Character(s) used in replacement of white spaces in the variables
        names. By default, use a '_'.
    case_sensitive : {True, False, 'upper', 'lower'}, optional
        If True, field names are case sensitive.
        If False or 'upper', field names are converted to upper case.
        If 'lower', field names are converted to lower case.
    unpack : bool, optional
        If True, the returned array is transposed, so that arguments may be
        unpacked using ``x, y, z = loadtxt(...)``
    usemask : bool, optional
        If True, return a masked array.
        If False, return a regular array.
    loose : bool, optional
        If True, do not raise errors for invalid values.
    invalid_raise : bool, optional
        If True, an exception is raised if an inconsistency is detected in the
        number of columns.
        If False, a warning is emitted and the offending lines are skipped.
    max_rows : int,  optional
        The maximum number of rows to read. Must not be used with skip_footer
        at the same time.  If given, the value must be at least 1. Default is
        to read the entire file.

        .. versionadded:: 1.10.0

    Returns
    -------
    out : ndarray
        Data read from the text file. If `usemask` is True, this is a
        masked array.

    See Also
    --------
    numpy.loadtxt : equivalent function when no data is missing.

    Notes
    -----
    * When spaces are used as delimiters, or when no delimiter has been given
      as input, there should not be any missing data between two fields.
    * When the variables are named (either by a flexible dtype or with `names`,
      there must not be any header in the file (else a ValueError
      exception is raised).
    * Individual values are not stripped of spaces by default.
      When using a custom converter, make sure the function does remove spaces.

    References
    ----------
    .. [1] NumPy User Guide, section `I/O with NumPy
           <http://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html>`_.

    Examples
    ---------
    >>> from io import StringIO
    >>> import numpy as np

    Comma delimited file with mixed dtype

    >>> s = StringIO("1,1.3,abcde")
    >>> data = np.genfromtxt(s, dtype=[('myint','i8'),('myfloat','f8'),
    ... ('mystring','S5')], delimiter=",")
    >>> data
    array((1, 1.3, 'abcde'),
          dtype=[('myint', '<i8'), ('myfloat', '<f8'), ('mystring', '|S5')])

    Using dtype = None

    >>> s.seek(0) # needed for StringIO example only
    >>> data = np.genfromtxt(s, dtype=None,
    ... names = ['myint','myfloat','mystring'], delimiter=",")
    >>> data
    array((1, 1.3, 'abcde'),
          dtype=[('myint', '<i8'), ('myfloat', '<f8'), ('mystring', '|S5')])

    Specifying dtype and names

    >>> s.seek(0)
    >>> data = np.genfromtxt(s, dtype="i8,f8,S5",
    ... names=['myint','myfloat','mystring'], delimiter=",")
    >>> data
    array((1, 1.3, 'abcde'),
          dtype=[('myint', '<i8'), ('myfloat', '<f8'), ('mystring', '|S5')])

    An example with fixed-width columns

    >>> s = StringIO("11.3abcde")
    >>> data = np.genfromtxt(s, dtype=None, names=['intvar','fltvar','strvar'],
    ...     delimiter=[1,3,5])
    >>> data
    array((1, 1.3, 'abcde'),
          dtype=[('intvar', '<i8'), ('fltvar', '<f8'), ('strvar', '|S5')])

    """
    if max_rows is not None:
        if skip_footer:
            raise ValueError(
                    "The keywords 'skip_footer' and 'max_rows' can not be "
                    "specified at the same time.")
        if max_rows < 1:
            raise ValueError("'max_rows' must be at least 1.")

    # Py3 data conversions to bytes, for convenience
    if comments is not None:
        comments = asbytes(comments)
    if isinstance(delimiter, unicode):
        delimiter = asbytes(delimiter)
    if isinstance(missing_values, (unicode, list, tuple)):
        missing_values = asbytes_nested(missing_values)

    #
    if usemask:
        from numpy.ma import MaskedArray, make_mask_descr
    # Check the input dictionary of converters
    user_converters = converters or {}
    if not isinstance(user_converters, dict):
        raise TypeError(
            "The input argument 'converter' should be a valid dictionary "
            "(got '%s' instead)" % type(user_converters))

    # Initialize the filehandle, the LineSplitter and the NameValidator
    own_fhd = False
    try:
        if is_pathlib_path(fname):
            fname = str(fname)
        if isinstance(fname, basestring):
            if sys.version_info[0] == 2:
                fhd = iter(np.lib._datasource.open(fname, 'rbU'))
            else:
                fhd = iter(np.lib._datasource.open(fname, 'rb'))
            own_fhd = True
        else:
            fhd = iter(fname)
    except TypeError:
        raise TypeError(
            "fname must be a string, filehandle, list of strings, "
            "or generator. Got %s instead." % type(fname))

    split_line = LineSplitter(delimiter=delimiter, comments=comments,
                              autostrip=autostrip)._handyman
    validate_names = NameValidator(excludelist=excludelist,
                                   deletechars=deletechars,
                                   case_sensitive=case_sensitive,
                                   replace_space=replace_space)

    # Skip the first `skip_header` rows
    for i in range(skip_header):
        next(fhd)

    # Keep on until we find the first valid values
    first_values = None
    try:
        while not first_values:
            first_line = next(fhd)
            if names is True:
                if comments in first_line:
                    first_line = (
                        b''.join(first_line.split(comments)[1:]))
            first_values = split_line(first_line)
    except StopIteration:
        # return an empty array if the datafile is empty
        first_line = b''
        first_values = []
        warnings.warn('genfromtxt: Empty input file: "%s"' % fname, stacklevel=2)

    # Should we take the first values as names ?
    if names is True:
        fval = first_values[0].strip()
        if fval in comments:
            del first_values[0]

    # Check the columns to use: make sure `usecols` is a list
    if usecols is not None:
        try:
            usecols = [_.strip() for _ in usecols.split(",")]
        except AttributeError:
            try:
                usecols = list(usecols)
            except TypeError:
                usecols = [usecols, ]
    nbcols = len(usecols or first_values)

    # Check the names and overwrite the dtype.names if needed
    if names is True:
        names = validate_names([_bytes_to_name(_.strip())
                                for _ in first_values])
        first_line = b''
    elif _is_string_like(names):
        names = validate_names([_.strip() for _ in names.split(',')])
    elif names:
        names = validate_names(names)
    # Get the dtype
    if dtype is not None:
        dtype = easy_dtype(dtype, defaultfmt=defaultfmt, names=names,
                           excludelist=excludelist,
                           deletechars=deletechars,
                           case_sensitive=case_sensitive,
                           replace_space=replace_space)
    # Make sure the names is a list (for 2.5)
    if names is not None:
        names = list(names)

    if usecols:
        for (i, current) in enumerate(usecols):
            # if usecols is a list of names, convert to a list of indices
            if _is_string_like(current):
                usecols[i] = names.index(current)
            elif current < 0:
                usecols[i] = current + len(first_values)
        # If the dtype is not None, make sure we update it
        if (dtype is not None) and (len(dtype) > nbcols):
            descr = dtype.descr
            dtype = np.dtype([descr[_] for _ in usecols])
            names = list(dtype.names)
        # If `names` is not None, update the names
        elif (names is not None) and (len(names) > nbcols):
            names = [names[_] for _ in usecols]
    elif (names is not None) and (dtype is not None):
        names = list(dtype.names)

    # Process the missing values ...............................
    # Rename missing_values for convenience
    user_missing_values = missing_values or ()

    # Define the list of missing_values (one column: one list)
    missing_values = [list([b'']) for _ in range(nbcols)]

    # We have a dictionary: process it field by field
    if isinstance(user_missing_values, dict):
        # Loop on the items
        for (key, val) in user_missing_values.items():
            # Is the key a string ?
            if _is_string_like(key):
                try:
                    # Transform it into an integer
                    key = names.index(key)
                except ValueError:
                    # We couldn't find it: the name must have been dropped
                    continue
            # Redefine the key as needed if it's a column number
            if usecols:
                try:
                    key = usecols.index(key)
                except ValueError:
                    pass
            # Transform the value as a list of string
            if isinstance(val, (list, tuple)):
                val = [str(_) for _ in val]
            else:
                val = [str(val), ]
            # Add the value(s) to the current list of missing
            if key is None:
                # None acts as default
                for miss in missing_values:
                    miss.extend(val)
            else:
                missing_values[key].extend(val)
    # We have a sequence : each item matches a column
    elif isinstance(user_missing_values, (list, tuple)):
        for (value, entry) in zip(user_missing_values, missing_values):
            value = str(value)
            if value not in entry:
                entry.append(value)
    # We have a string : apply it to all entries
    elif isinstance(user_missing_values, bytes):
        user_value = user_missing_values.split(b",")
        for entry in missing_values:
            entry.extend(user_value)
    # We have something else: apply it to all entries
    else:
        for entry in missing_values:
            entry.extend([str(user_missing_values)])

    # Process the filling_values ...............................
    # Rename the input for convenience
    user_filling_values = filling_values
    if user_filling_values is None:
        user_filling_values = []
    # Define the default
    filling_values = [None] * nbcols
    # We have a dictionary : update each entry individually
    if isinstance(user_filling_values, dict):
        for (key, val) in user_filling_values.items():
            if _is_string_like(key):
                try:
                    # Transform it into an integer
                    key = names.index(key)
                except ValueError:
                    # We couldn't find it: the name must have been dropped,
                    continue
            # Redefine the key if it's a column number and usecols is defined
            if usecols:
                try:
                    key = usecols.index(key)
                except ValueError:
                    pass
            # Add the value to the list
            filling_values[key] = val
    # We have a sequence : update on a one-to-one basis
    elif isinstance(user_filling_values, (list, tuple)):
        n = len(user_filling_values)
        if (n <= nbcols):
            filling_values[:n] = user_filling_values
        else:
            filling_values = user_filling_values[:nbcols]
    # We have something else : use it for all entries
    else:
        filling_values = [user_filling_values] * nbcols

    # Initialize the converters ................................
    if dtype is None:
        # Note: we can't use a [...]*nbcols, as we would have 3 times the same
        # ... converter, instead of 3 different converters.
        converters = [StringConverter(None, missing_values=miss, default=fill)
                      for (miss, fill) in zip(missing_values, filling_values)]
    else:
        dtype_flat = flatten_dtype(dtype, flatten_base=True)
        # Initialize the converters
        if len(dtype_flat) > 1:
            # Flexible type : get a converter from each dtype
            zipit = zip(dtype_flat, missing_values, filling_values)
            converters = [StringConverter(dt, locked=True,
                                          missing_values=miss, default=fill)
                          for (dt, miss, fill) in zipit]
        else:
            # Set to a default converter (but w/ different missing values)
            zipit = zip(missing_values, filling_values)
            converters = [StringConverter(dtype, locked=True,
                                          missing_values=miss, default=fill)
                          for (miss, fill) in zipit]
    # Update the converters to use the user-defined ones
    uc_update = []
    for (j, conv) in user_converters.items():
        # If the converter is specified by column names, use the index instead
        if _is_string_like(j):
            try:
                j = names.index(j)
                i = j
            except ValueError:
                continue
        elif usecols:
            try:
                i = usecols.index(j)
            except ValueError:
                # Unused converter specified
                continue
        else:
            i = j
        # Find the value to test - first_line is not filtered by usecols:
        if len(first_line):
            testing_value = first_values[j]
        else:
            testing_value = None
        converters[i].update(conv, locked=True,
                             testing_value=testing_value,
                             default=filling_values[i],
                             missing_values=missing_values[i],)
        uc_update.append((i, conv))
    # Make sure we have the corrected keys in user_converters...
    user_converters.update(uc_update)

    # Fixme: possible error as following variable never used.
    #miss_chars = [_.missing_values for _ in converters]

    # Initialize the output lists ...
    # ... rows
    rows = []
    append_to_rows = rows.append
    # ... masks
    if usemask:
        masks = []
        append_to_masks = masks.append
    # ... invalid
    invalid = []
    append_to_invalid = invalid.append

    # Parse each line
    for (i, line) in enumerate(itertools.chain([first_line, ], fhd)):
        values = split_line(line)
        nbvalues = len(values)
        # Skip an empty line
        if nbvalues == 0:
            continue
        if usecols:
            # Select only the columns we need
            try:
                values = [values[_] for _ in usecols]
            except IndexError:
                append_to_invalid((i + skip_header + 1, nbvalues))
                continue
        elif nbvalues != nbcols:
            append_to_invalid((i + skip_header + 1, nbvalues))
            continue
        # Store the values
        append_to_rows(tuple(values))
        if usemask:
            append_to_masks(tuple([v.strip() in m
                                   for (v, m) in zip(values,
                                                     missing_values)]))
        if len(rows) == max_rows:
            break

    if own_fhd:
        fhd.close()

    # Upgrade the converters (if needed)
    if dtype is None:
        for (i, converter) in enumerate(converters):
            current_column = [itemgetter(i)(_m) for _m in rows]
            try:
                converter.iterupgrade(current_column)
            except ConverterLockError:
                errmsg = "Converter #%i is locked and cannot be upgraded: " % i
                current_column = map(itemgetter(i), rows)
                for (j, value) in enumerate(current_column):
                    try:
                        converter.upgrade(value)
                    except (ConverterError, ValueError):
                        errmsg += "(occurred line #%i for value '%s')"
                        errmsg %= (j + 1 + skip_header, value)
                        raise ConverterError(errmsg)

    # Check that we don't have invalid values
    nbinvalid = len(invalid)
    if nbinvalid > 0:
        nbrows = len(rows) + nbinvalid - skip_footer
        # Construct the error message
        template = "    Line #%%i (got %%i columns instead of %i)" % nbcols
        if skip_footer > 0:
            nbinvalid_skipped = len([_ for _ in invalid
                                     if _[0] > nbrows + skip_header])
            invalid = invalid[:nbinvalid - nbinvalid_skipped]
            skip_footer -= nbinvalid_skipped
#
#            nbrows -= skip_footer
#            errmsg = [template % (i, nb)
#                      for (i, nb) in invalid if i < nbrows]
#        else:
        errmsg = [template % (i, nb)
                  for (i, nb) in invalid]
        if len(errmsg):
            errmsg.insert(0, "Some errors were detected !")
            errmsg = "\n".join(errmsg)
            # Raise an exception ?
            if invalid_raise:
                raise ValueError(errmsg)
            # Issue a warning ?
            else:
                warnings.warn(errmsg, ConversionWarning, stacklevel=2)

    # Strip the last skip_footer data
    if skip_footer > 0:
        rows = rows[:-skip_footer]
        if usemask:
            masks = masks[:-skip_footer]

    # Convert each value according to the converter:
    # We want to modify the list in place to avoid creating a new one...
    if loose:
        rows = list(
            zip(*[[conv._loose_call(_r) for _r in map(itemgetter(i), rows)]
                  for (i, conv) in enumerate(converters)]))
    else:
        rows = list(
            zip(*[[conv._strict_call(_r) for _r in map(itemgetter(i), rows)]
                  for (i, conv) in enumerate(converters)]))

    # Reset the dtype
    data = rows
    if dtype is None:
        # Get the dtypes from the types of the converters
        column_types = [conv.type for conv in converters]
        # Find the columns with strings...
        strcolidx = [i for (i, v) in enumerate(column_types)
                     if v in (type('S'), np.string_)]
        # ... and take the largest number of chars.
        for i in strcolidx:
            column_types[i] = "|S%i" % max(len(row[i]) for row in data)
        #
        if names is None:
            # If the dtype is uniform, don't define names, else use ''
            base = set([c.type for c in converters if c._checked])
            if len(base) == 1:
                (ddtype, mdtype) = (list(base)[0], np.bool)
            else:
                ddtype = [(defaultfmt % i, dt)
                          for (i, dt) in enumerate(column_types)]
                if usemask:
                    mdtype = [(defaultfmt % i, np.bool)
                              for (i, dt) in enumerate(column_types)]
        else:
            ddtype = list(zip(names, column_types))
            mdtype = list(zip(names, [np.bool] * len(column_types)))
        output = np.array(data, dtype=ddtype)
        if usemask:
            outputmask = np.array(masks, dtype=mdtype)
    else:
        # Overwrite the initial dtype names if needed
        if names and dtype.names:
            dtype.names = names
        # Case 1. We have a structured type
        if len(dtype_flat) > 1:
            # Nested dtype, eg [('a', int), ('b', [('b0', int), ('b1', 'f4')])]
            # First, create the array using a flattened dtype:
            # [('a', int), ('b1', int), ('b2', float)]
            # Then, view the array using the specified dtype.
            if 'O' in (_.char for _ in dtype_flat):
                if has_nested_fields(dtype):
                    raise NotImplementedError(
                        "Nested fields involving objects are not supported...")
                else:
                    output = np.array(data, dtype=dtype)
            else:
                rows = np.array(data, dtype=[('', _) for _ in dtype_flat])
                output = rows.view(dtype)
            # Now, process the rowmasks the same way
            if usemask:
                rowmasks = np.array(
                    masks, dtype=np.dtype([('', np.bool) for t in dtype_flat]))
                # Construct the new dtype
                mdtype = make_mask_descr(dtype)
                outputmask = rowmasks.view(mdtype)
        # Case #2. We have a basic dtype
        else:
            # We used some user-defined converters
            if user_converters:
                ishomogeneous = True
                descr = []
                for i, ttype in enumerate([conv.type for conv in converters]):
                    # Keep the dtype of the current converter
                    if i in user_converters:
                        ishomogeneous &= (ttype == dtype.type)
                        if ttype == np.string_:
                            ttype = "|S%i" % max(len(row[i]) for row in data)
                        descr.append(('', ttype))
                    else:
                        descr.append(('', dtype))
                # So we changed the dtype ?
                if not ishomogeneous:
                    # We have more than one field
                    if len(descr) > 1:
                        dtype = np.dtype(descr)
                    # We have only one field: drop the name if not needed.
                    else:
                        dtype = np.dtype(ttype)
            #
            output = np.array(data, dtype)
            if usemask:
                if dtype.names:
                    mdtype = [(_, np.bool) for _ in dtype.names]
                else:
                    mdtype = np.bool
                outputmask = np.array(masks, dtype=mdtype)
    # Try to take care of the missing data we missed
    names = output.dtype.names
    if usemask and names:
        for (name, conv) in zip(names or (), converters):
            missing_values = [conv(_) for _ in conv.missing_values
                              if _ != b'']
            for mval in missing_values:
                outputmask[name] |= (output[name] == mval)
    # Construct the final array
    if usemask:
        output = output.view(MaskedArray)
        output._mask = outputmask
    # Verify that the array has at least dimensions `ndmin`.
    # Check correctness of the values of `ndmin`
    if ndmin not in [0, 1, 2]:
        raise ValueError('Illegal value of ndmin keyword: %s' % ndmin)
    # Tweak the size and shape of the arrays - remove extraneous dimensions
    if output.ndim > ndmin:
        output = np.squeeze(output)
    # and ensure we have the minimum number of dimensions asked for
    # - has to be in this order for the odd case ndmin=1, X.squeeze().ndim=0
    if output.ndim < ndmin:
        if ndmin == 1:
            output = np.atleast_1d(output)
        elif ndmin == 2:
            output = np.atleast_2d(output).T
    if unpack:
        return output.T
    return output
