import test_class as tc

print(tc.rishabh())
print(tc.rish)

def test_func():
    tc.rish.dict = {'python':'Karletabc'}
    return None

print(tc.rish.dict)
test_func()
print('***'*50)
print(tc.rish.dict) ## variable changed for whole module as 
## it was imported for the entire module. This change doesnt impact the variable in original code
## test_class