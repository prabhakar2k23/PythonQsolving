x = 'global'

def outer():
    x = 'outer'
    def inner():
        print(x)
    inner()

outer()
