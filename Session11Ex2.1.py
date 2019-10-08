#input 4 numbers and determine the average
i = 0
b = []
while(i<4):
    try:
        n = input('give me a number')
        n = int(n)
        b.append(n)
        i = i+1
    except ValueError:
        print('please enter a number')
        