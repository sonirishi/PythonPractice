class bus:
    def __init__(self, passengers = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)  ## copy here creates same value not id

    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)

    def __repr__(self):
        return f"{self.passengers}"

from copy import copy, deepcopy

bus1 = bus(['rishabh','yashi','shivangi','minto'])
bus2 = bus1  ##same id
bus3 = copy(bus1)
bus4 = deepcopy(bus1)

print(id(bus1),id(bus2),id(bus3),id(bus4))
## bus1 and 2 have same id, 3 and 4 are different

print(bus1==bus2)  ##True
print(bus1 == bus3) ##False

bus1.pick('piggychops')
print(bus1, bus2, bus3, bus4) ## except bus4 all are same

print(id(bus1.passengers),id(bus2.passengers),id(bus3.passengers),id(bus4.passengers))

## bus1-3 share list and hence have same id, not 4

passlist = ['rishabh','yashi','shivangi','minto']
bus11 = bus(passlist)
bus31 = copy(bus11)
bus41 = deepcopy(bus11)

print('*'*50)

print(id(passlist)); print(id(bus11.passengers))
print(id(bus31.passengers));print(id(bus41.passengers))
print(bus11)
passlist.append('chips')
print(passlist)
print(bus11)

