# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_playground.ipynb.

# %% auto 0
__all__ = ['foo', 'HelloSayer']

# %% ../00_playground.ipynb 3
def foo(): pass

# %% ../00_playground.ipynb 4
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    #show_doc(HelloSayer.say)
    def __init__(self, to): self.to = to
        
    def say(self):
        "Do the saying"
        return say_hello(self.to)
        
# shows method of class
show_doc(HelloSayer.say)
