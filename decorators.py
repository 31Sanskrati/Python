def announce(f):
    def wrapper():
        print("Going to run the function...")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()