class A:
    def __del__(self):
        print("Deleted!")

a = A()
del a
print("Done")
