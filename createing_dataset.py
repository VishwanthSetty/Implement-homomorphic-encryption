import random


n = 99

with open("data1","w+") as file:
    # file.writelines('1\n')
    
    for i in range(n):
        file.write(str(random.randint(0,1000))+"\n")
    
    file.write(str(random.randint(0,1000)))

with open("data2","w+") as file:
    # file.writelines('1\n')
    
    for i in range(n):
        file.write(str(random.randint(0,1000))+"\n")
    
    file.write(str(random.randint(0,1000)))

with open("data1","r") as file1:
    value1 = file1.read().split("\n")
    value1 = [int(x) for x in (value1)]
print(value1)