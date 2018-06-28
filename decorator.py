

def new_decorator(func):

    def wrap_func():
        print("in new_decorator before executing the func")

        func()                              # call the func_needs_decorator() function

        print("in new_decorator after the func()")

    return wrap_func                        # this will call the wrap_func() function and return a pointor on the wrap_func

#def func_needs_decorator():
#    print ("1 - This function is in need of a Decorator")
    

@new_decorator                              #by calling the func_needs_decorator, the new_decorator will be call
def func_needs_decorator():
    print ("2 - in func_needs_decorator")
    
func_needs_decorator()
