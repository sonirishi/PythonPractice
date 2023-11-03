def test_func():
    import test_class as tc
    tc.rish.dict = {'python':'Karletabc'}
    print(tc.rish.dict)
    return None

test_func()
print(tc.rish.dict)
print('***'*50)
print(tc.rish.dict) ## variable changed for whole module as 
## it was imported for the entire module. This change doesnt impact the variable in original code
## test_class