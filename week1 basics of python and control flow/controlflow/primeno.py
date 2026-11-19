number = int(input("Enter any no "))
isprime = True
i=2
while(i<number):
    if(number%i ==0):
        isprime=False
        break
    i=i+1
if(isprime):
    print(f"{number} is prime ")    
else:
    print(f"{number} is not prime")