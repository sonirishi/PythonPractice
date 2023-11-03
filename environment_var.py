import os
def set_var():
    os.environ['rishabh'] = 'mast'
    #print(os.environ)
    #os.environ.pop('rishabh')
    return None

def rishabh():
    print('not set env var')

set_var()
print('import')
# print('****')
# print(os.environ)

if __name__ == '__main__':
    rishabh()