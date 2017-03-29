def deprecated(planet):
  print("Hello world!")
  def wrap(f):
      #print("Inside the wrap()")
      def destroy_world(*names):
        print("We are going to destroy the",planet)
        f(*names)
        print("Bye bye world")
      return destroy_world
      #print("Out of the wrap()")
  return wrap

@deprecated("Earth")
def King_name(arg1, arg2):
    print ("We are", arg1,"and", arg2)


King_name("Noam","Jiyun")
