# class Bird:
#     pass

# class Duck(Bird):
#     def quack(self):
#         print('quack')
    
# def alert(birdie):
#     birdie.quack()

# def alert_duck(birdie: Duck) -> None:
#     birdie.quack()

# def alert_bird(birdie: Bird) -> None:
#     birdie.quack()

# daffy = Duck()
# alert(daffy)
# alert_duck(daffy)
# alert_bird(daffy)

class temp:
    def __init__(self,n):
        self.n = n
    def __lt__(self,other):
        return self.n < other.n
    def __repr__(self):
        return f'temp({self.n})'
    
l = [temp(n) for n in range(10)]
print(l)
print(sorted(l,reverse=True))