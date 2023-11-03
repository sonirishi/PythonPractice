class bus:
    def __init__(self, passengers = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers  ## exact same passed

    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)

    def __repr__(self):
        return f"{self.passengers}"
    
from copy import copy, deepcopy

passlist = ['rishabh','yashi','shivangi','minto']
bus11 = bus(passlist)
bus31 = copy(bus11)
bus41 = deepcopy(bus11)

print('*'*50)

print(id(passlist)); print(id(bus11.passengers)); print(id(bus31.passengers));
print(id(bus41.passengers))

print(bus11)
passlist.append('chips')
print(passlist)
print(bus11)

