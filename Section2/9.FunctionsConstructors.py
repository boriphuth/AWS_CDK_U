# def my_function(name):
#     print('Hello'+name)

# my_function('DevOps') #HelloDevOps

# def my_function(*args):
#     print('First fruit name is {}'.format(args[0]))

# my_function('apple','orange','banana') #First fruit name is apple

# def my_function(**fruits):
#     print('First fruit name is {} and count is {}'.format(fruits["fruit"],fruits["count"]))

# my_function(fruit="apple", count=2) #First fruit name is apple and count is 2

class Fruits:
    def __init__(self,name,count):
        self.name = name
        self.count = count
    def showfruits(self):
            print('Fruit name is {} and count is {}'.format(self.name,self.count))


apple=Fruits("Apple",2)
orange=Fruits("Orange",3)

apple.showfruits() #Fruit name is Apple and count is 2
orange.showfruits() #Fruit name is Orange and count is 3