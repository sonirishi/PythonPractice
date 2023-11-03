from mypytest_protocol import support_complex
from typing import runtime_checkable, Protocol
from abc import abstractmethod

@runtime_checkable
class test_again(support_complex,Protocol):
    @abstractmethod
    def __len__(self):
        pass

c = [1,2,3]
print(isinstance(c,test_again))
import numpy as np
d = np.complex64(3+4j)
print(isinstance(d,support_complex)) 
print(isinstance(d,test_again)) 
print(test_again.__dict__)
