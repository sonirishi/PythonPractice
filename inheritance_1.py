from collections import UserDict

class doppledict(UserDict):
    def __setitem__(self, key, value):
        return super().__setitem__(key, [value]*2)
    
if __name__ == '__main__':
    dd = doppledict(one=1)
    print(dd)
    dd['two'] = 2
    print(dd)
    dd.update(three=3)
    print(dd)