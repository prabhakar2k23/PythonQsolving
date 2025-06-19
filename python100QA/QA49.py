class A:
    @property
    def val(self):
        return 42

class B(A):
    val = 99

print(B().val)
