# Using "+" Operator:
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L3 = L1+L2
print ("Joined list:", L3)


# Using "extend" Keyword":
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
L1.extend(L2)
print ("Joined list:", L1)

# Using "append" method:
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']

for x in L2:
   L1.append(x)
   
print ("Joined list:", L1)