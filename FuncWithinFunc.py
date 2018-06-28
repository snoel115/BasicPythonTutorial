def hello(name='Jose'):
    
    def greet():
        return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    if name == 'Jose':
        return greet
    else:
        return welcome      #without () will return the function itself


x = hello('Jose') # assign the great() function to the variable x

print(x) #print the definition of the greet function

print(x())  #print the return value of the greet() function