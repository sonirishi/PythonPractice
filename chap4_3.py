from dataclasses import dataclass, field, fields
from typing import Optional, ClassVar
from enum import Enum, auto
from datetime import date

class ResourceType(Enum):
    Book = auto()
    Ebook = auto()
    Video = auto()

@dataclass
class resource:
    identifier: str
    title: str = '<Untitled>'
    creators: list[str] = field(default_factory=list)
    date:Optional[date] = None
    type:ResourceType = ResourceType.Book
    description: str = ''
    language:str = ''
    subjects: list[str] = field(default_factory=list)

    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        indent = '*'*4
        res = [f'{cls_name}(']
        for f in fields(cls):
            value = getattr(self,f.name)
            res.append(f'{indent}{f.name} = {value!r},')
        res.append(')')
        return '\n'.join(res)

description = 'newbook'
book = resource('abcd','refactoring',['Rishi','Minto'],date(2020,12,12),ResourceType.Book,description,'EN',['coding','programming'])
print(book)
print(fields(book)) ## all fields in the class

