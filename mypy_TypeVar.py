from typing import TypeVar, Generic, Iterable, Iterator

List_co = TypeVar('List_co', covariant=True)
class ImmutableList(Generic[List_co]):
    def __init__(self, items: Iterable[List_co]) -> None:
        pass
        
    def __iter__(self) -> Iterator[List_co]:
        pass
        

class Employee():
    pass
    
class Manager(Employee):
    pass

def list_employees(employees: ImmutableList[Employee]) -> None:
    for employee in employees:
        print(employee)

managers = ImmutableList(Manager())
list_employees(managers)
