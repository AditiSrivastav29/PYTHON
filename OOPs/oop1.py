class Dog:
    def __init__(self,name):
        self.name = name
        #print(name)

    def add_one(self,x):
        print (x + 1)
    def bark(self):
        print("bark")
d = Dog("duke")
print(d.name)
d1 = Dog("jacky")
print(d1.name)

#d.bark()
#d.add_one(10)
#print(d)

 
