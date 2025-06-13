def func(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

func(1, 2, 3, a=4, b=5)

# And now this:
args = (10, 20)
kwargs = {'x': 30, 'y': 40}
func(args, kwargs)
func(*args, **kwargs)
