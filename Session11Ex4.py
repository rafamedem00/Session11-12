#test if a given number is prime

num = int(input('write a number'))
if (num>1):
    isprime = True
    for i in range (2, num//2):
        if (num % i==0):
            print(num, "not prime")
        isprime = False
        break
    if isprime:
        print(num, 'is prime')