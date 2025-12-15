def sub(a,d):
    return d - a

class Car: 
    def __init__(self,brand,name,year):
        self.brand = brand
        self.name = name
        self.year = year 
        
    def __str__(self):
        return(f"Hoho Yes {self.brand},{self.name},{self.year}" )
        
Car1 = Car("Honda","City",1997)
print(Car1)

testing3 = sub(10,80)
print(testing3)