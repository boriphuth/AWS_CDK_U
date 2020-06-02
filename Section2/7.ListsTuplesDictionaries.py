list1 = ["a", "b", "c"]
print(list1)    #['a', 'b', 'c']
print(list1[0]) #a
print(list1[-1]) #c
list1.append("d")
print(list1)    #['a', 'b', 'c', 'd']
print(list1.pop()) #d
print(list1)    #['a', 'b', 'c']
print(list1.pop(0)) #a
print(list1)  #['b', 'c']
print(list1.remove('c')) #None
print(list1)  #['b']
list1.append('e')
print(list1) #['b', 'e']
list1.remove('e')
print(list1)  #['b']
l1=[1,2,3,4]
l2=l1.copy() 
print(l2)   #[1, 2, 3, 4]
l3=['a','b', 'c','d']
l4=l2+l3
print(l4)   #[1, 2, 3, 4, 'a', 'b', 'c', 'd']
print(l3)   #['a', 'b', 'c', 'd']
l3.insert(2,'z')
print(l3)   #['a', 'b', 'z', 'c', 'd']
t1=('a','b', 'c', 'd')
print(t1)   #('a', 'b', 'c', 'd')
