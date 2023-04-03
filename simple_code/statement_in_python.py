mylist = [1,2,3,4,5,6,7,8,9,10]

for i in mylist:
    #check fot even 
    if i % 2 == 0: 
        print(i)
    else:
        print(f'Odd number :{i}')
        

list_sum =0 

for j in mylist:
    list_sum = list_sum+j
    
    print(list_sum)
    
    
mystring = "Ahmed Abdelkareem"

#iterate for string 
for letter in mystring:
    print(letter)
    

tup = (1,2,3)

for item in tup:
    print(item)
    


#unpacking tuple from list     
myList2 = [(1,2,3),(5,6,7),(8,9,10)]

for a,b,c in myList2:
    print(a)
    print(b)
    print(c)
    
    
dic = {'k1':1,'k2':2,'k3':3}

for ite in dic.items():
    print(ite)
    
    
