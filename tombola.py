import abc

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self,iterable):
        pass

    @abc.abstractmethod
    def pick(self):
        pass

    def loaded(self):
        return bool(self.inspect())
    
    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(items)