for i in range(1,1001):
    if (i%7==0 or i%10==7 or i//10==7 or i//100==7):
        continue
    print(i)
print("================Game over!=====================")
