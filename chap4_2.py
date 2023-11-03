from dataclasses import dataclass, field

# @dataclass
# class ClubMember:
#     name: str
#     guests: list = []  ## mutable attributes not allowed 

# @dataclass
# class ClubMember1:
#     name: str
#     guests: list = field(default_factory=list)
#     obese: bool = False
#     athlete: bool = field(default=False)

#     def __init__(self,teamname: str):
#         self.team = teamname

# print(ClubMember1.__annotations__)
# print(ClubMember1.__doc__)  ## only teamname comes here

# from typing import NamedTuple
# class testing(NamedTuple):  ## cant overwrite inits
#     a:int
#     b:int
#     def increment(self):
#         self.a+=1  
#         self.b+=1
#     def __repr__(self):
#         return f"val1 {self.a},val2 {self.b}"

# obj = testing(2,3)
# print(obj)
# print(obj.increment()) ##when i have defined using namedtuple i can change the value at all

# from dataclasses import dataclass
# @dataclass
# class testing:  ## cant overwrite inits
#     a:int
#     b:int
#     def increment(self):
#         self.a+=1  
#         self.b+=1
#     def __repr__(self):
#         return f"val1 {self.a},val2 {self.b}"

# obj = testing(2,3)
# print(obj)
# obj.increment()  ## this works
# print(obj)

from dataclasses import dataclass
@dataclass(frozen=True)
class testing:  ## cant overwrite inits
    a:int
    b:int
    def increment(self):
        self.a+=1  
        self.b+=1
    def __repr__(self):
        return f"val1 {self.a},val2 {self.b}"

obj = testing(2,3)
print(obj)
obj.increment()  ## this wont work again is hashable due to frozen
print(obj)