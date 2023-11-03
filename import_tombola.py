import random

from tombola import Tombola

@Tombola.register
class temp_class(Tombola):

    def __init__(self,iterable):
        self._balls = list(iterable)  ## not a reference to iterable copy the thing

    def load(self,iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError("Test")
        return self._balls.pop(position)
    
    def loaded(self):
        return bool(self._balls)
    
    def inspect(self):
        return tuple(self._balls)
    
print(issubclass(temp_class,Tombola))  ## True
print(temp_class.__mro__) ## method resolution order