# class newbus:
#     def __init__(self,passengers=[]):
#         self.passengers = passengers
#     def pick(self,name):
#         self.passengers.append(name)
#     def drop(self,name):
#         self.passengers.remove(name)
#     def __repr__(self):
#         return (f'Bus has {self.passengers}')

# bus1 = newbus(['a','b'])
# print(bus1) 
# bus1.pick('c')
# print(bus1)
# bus1.drop('a')
# print(bus1)
# bus2 = newbus() ## blank list is mutable hence shared among objects
# ### This is wrong things
# bus2.pick('d')
# print(bus2)
# bus3 = newbus()
# print(bus3)
# print(newbus.__init__.__defaults__)
# print(newbus.__init__.__defaults__[0] is bus3.passengers) ## alias for defaults
# ## not a separate list

class newbus:
    def __init__(self,passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    def pick(self,name):
        self.passengers.append(name)
    def drop(self,name):
        self.passengers.remove(name)
    def __repr__(self):
        return (f'Bus has {self.passengers}')

bus1 = newbus(['a','b'])
print(bus1) 
bus1.pick('c')
print(bus1)
bus1.drop('a')
print(bus1)
bus2 = newbus() 
bus2.pick('d')
print(bus2)
bus3 = newbus()
print(bus3)
print(newbus.__init__.__defaults__) ## use list which shallow copies the argument
print(newbus.__init__.__defaults__[0] is bus3.passengers) 