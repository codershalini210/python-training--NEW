# no = int(input("Enter any no "))
# if(no%2==0):
#     print(f"{no} is even")
# else:
#     print(f"{no} is odd")
#question print all the even nos from 1-40
# for i in range(1,41):
#     if(i%2==0):
#         print(i)

# question print all  nos from 1-40 and stop loop at the no which is 
# divisible by both 5 and 2
# for i in range(1,41):
#     if(i%2==0 and i%5 ==0):
#         break
#     else:
#         print(i)

# print all the nos between 1-40 except no which are divisible by 5
for i in range(1,41):
    if(i%5==0):
        continue
    print(i,end=" ")