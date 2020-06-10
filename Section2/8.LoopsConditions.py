l1=['a', 'b', 'c', 'd']
print(l1) #['a', 'b', 'c', 'd']
for item in l1:
    print(item) #a b c d

for item in l1:
    if item == 'a':
        print('we got {}'.format(item)) #we got a
d1={'color':'orange','count': 2, 'fruit': 'orange'}
print(d1) #{'color': 'orange', 'count': 2, 'fruit': 'orange'}
for k,v in d1.items():
    print(k,v)  # color orange
                # count 2
                # fruit orange
for k,v in d1.items():
    print(k is 'color') #True
                        # False
                        # False
for x in range(10):
    print(x)# 0
            # 1
            # 2
            # 3
            # 4
            # 5
            # 6
            # 7
            # 8
            # 9
l2=[]
for x in range(10):
    l2.append(x)
print(l2) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

import time
count=1
while True:
    count+=1
    print(count)
    if count >=5:
        break
    time.sleep(1)
        # 2
        # 3
        # 4
        # 5