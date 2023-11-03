class rishabh:
    def __init__(self,luck):
        self.luck = luck

class masti:
    def __init__(self,temp):
        self.temp = temp

    def __repr__(self) -> str:
        return (f'{self.temp} is done')
    
    @classmethod
    def initialize_rish(cls,rish_ob):
        obj1 = cls(rish_ob.luck) ## initialize an object within
        print('enter the dragon')
        print(obj1)
    

if __name__ == '__main__':
    rish = rishabh('hoga bhai hoga')
    masti.initialize_rish(rish)
    ##print(obj1.temp)  obj1 is local object hence not callable from main