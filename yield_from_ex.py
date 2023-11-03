def tree(cls):
    yield cls.__name__,0
    yield from sub_tree(cls,1)

def sub_tree(cls,level):
    for subcls in cls.__subclasses__():
        yield subcls.__name__,level
        yield from sub_tree(subcls,level+1)

def disp(cls):
    for cls_name, level in tree(cls):
        print('**'*10)
        print(f'Class Name {cls_name},{level}')

if __name__ == '__main__':
    disp(BaseException)  ## this implements DFS, very cool solution