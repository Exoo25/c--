@staticmethod
def let(name, value):
    globals()[name] = value  # Correct usage of `globals()`
def print():
    pass