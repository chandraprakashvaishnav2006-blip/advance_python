class point:
    def __init__ (self,x,y):
        self.x=x
        self.y=y
    def __add__ (self,p):
        return (self.x+p.x),(self.y+p.y)
    def print(self):
        print(f"x is {self.x}yis {self.y}")


p1=point(3,5)
p2=point(6,7)

p=p1+p2
print(p)



# Other useful magic methods: (You don't need to memorize them all, but be aware they exist!)

# __sub__ (-), __mul__ (*), __truediv__ (/), __eq__ (==), __ne__ (!=), __lt__ (<), __gt__ (>), __len__ (len()), __getitem__, __setitem__, __delitem__ (for list/dictionary-like behavior – allowing you to use [] with your objects).
# Getters and Setters: Controlling Access to Attributes
# Getters and setters are methods that you create to control how attributes of your class are accessed and modified. They are a key part of the principle of encapsulation. Instead of directly accessing an attribute (like my_object.attribute), you use methods to get and set its value. This might seem like extra work, but it provides significant advantages.

# Why use them?

# Validation: You can add checks within the setter to make sure the attribute is set to a valid value. For example, you could prevent an age from being negative.
# Read-Only Attributes: You can create a getter without a setter, making the attribute effectively read-only from outside the class. This protects the attribute from being changed accidentally.
# Side Effects: You can perform other actions when an attribute is accessed or modified. For instance, you could update a display or log a change whenever a value is set.
# Maintainability and Flexibility: If you decide to change how an attribute is stored internally (maybe you switch from storing degrees Celsius to Fahrenheit), you only need to update the getter and setter methods. You don't need to change every other part of your code that uses the attribute. This makes your code much easier to maintain and modify in the future.
# class Person: