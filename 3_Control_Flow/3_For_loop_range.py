"""
    Syntax: For loop:
    ----------------
    for index in range(n):
        statement
    
    * range(n) Start from 0 to n-1
    * range(start,stop) start from start index and end with stop index (stop index -1)
    * range(start,stop,step) increment order 
"""
# you often want to execute a block of code multiple times. To do so, you use a for loop.

# For loop
# range start from 0 t0 n-1

for index in range(5):
    print(index,"\n") # 0 1 2 3 4 

for index in range(1,10):
    print(index)  # 1 2 3 4 5 6 7 8 9 

for index in range(0,11,2):
    print(index,"\n") # 0 2 4 6 8 10


# Example:1 Sum of the sequence (0 to 100):
sum=0
print("Before sum value is:",sum)
for i in range(101):
    sum=sum+i
print("Sum of the sequence is:",sum)

# without loop:
sum=0
n=100
print("Before sum value is:",sum)
sum = n * (n+1)/2
print("Sum of the sequence is:",sum)

