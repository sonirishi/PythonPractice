from collections.abc import MutableSequence

class temp(MutableSequence): ## mutable sequence needs methods implemented post __init__

    def __init__(self):
        pass
    def __delitem__(self,position):
        pass
    def __getitem__(self,position):
        pass
    def __len__(self):
        pass
    def __setitem__(self):
        pass
    def insert(self,position,value):
        pass

d = temp()
print(d)
