def logger(func):
    #This is the code that will execute when the decorator is called
    def wrapper():
        print('Logging execution')
        func() #Run the function where our decorator is on top of
        print('Done logging')
    return wrapper

@logger
def sample():
    print('-- Inside sample function')

sample()