class animal:
    location="aus"
    def __int__(self,name):
        self.name=name
    def speak(self):
        print("genric animal sound") 

class dog(animal):
    def speak(self): #method override
        super().speak()
    
        print("bhow bhow")

        
d=dog()
d.speak()
print(d.location)          








# inheritance ex
# super(): Inside a child class, super() lets you call methods from the parent class. 
# This is useful when you want to extend the parent's behavior instead of completely replacing it.
# It's especially important when initializing the parent class's part of a child object.



