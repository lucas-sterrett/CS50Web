def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the funciton.")
    return wrapper

@announce
def hello(): 
    print("Hello, world!")

hello()