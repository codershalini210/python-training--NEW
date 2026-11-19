# i = 1
# while(i<=10):
#     print(i,end=" ")
#     i=i+1
# print("Loop end")    
# question take start no and end no from user and print all the no's between them
sno = int(input("Enter start no "))
eno = int(input("Enter end no "))
sum =0
evencount = 0 
oddcount =0
if(sno >= eno ):
    print("Start no should be less than end no ")
else:
    i=sno
    while(i<=eno):
        print(i,end=" ")
        if(i%2==0):
            evencount=evencount+1
        else:
            oddcount= oddcount+1
        sum = sum + i 
        i=i+1
    print(f"Total nos {evencount+oddcount}")
    print(f"Total even nos {evencount}")
    print(f"Total odd nos {oddcount}")
    print(f"sum of all the nos between {sno} and {eno} is {sum}")        
    
# print sum of all then nos betwenn sno and eno 
# print count of  eve nos between sno and eno         
#print count of odd nos between sno and eno