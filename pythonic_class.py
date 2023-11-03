class pixel:
    def __init__(self,x,y,p):
       self.x = x
       self.y = y
       self.__private = p

p = pixel(2,3,8)
print(p.__dict__) ##_pixel__private = 8
#print(p.__private) ## doesnt work