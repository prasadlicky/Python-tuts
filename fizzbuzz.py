sum=0
upto=int(input("enter the number: "))
for i in range(1,upto+1):
    
    if i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    elif i%3==0 and i%5==0:
        print("fizzbuzz")
    else:
        print(i)
