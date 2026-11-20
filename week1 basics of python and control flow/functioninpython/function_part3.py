def listops(nos):
    s = 0 
    count = 0 
    evencount =0 
    oddcount = 0 
    for n in nos:
        s=s+n
        count = count+1
        if(n%2==0):
            evencount=evencount+1
        else:
            oddcount=oddcount+1
            
    return f"""total count {count} \n sum of all the items :{s}
\n even count {evencount} odd count {oddcount}"""
print(listops([34,5,23,66,23]))