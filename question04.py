#this code will count from 1-100, and replace multiples of 3 with 'Fizz'
for i in range(1, 101):
    if i % 3 == 0:
        print("Fizz!")
    else:
        print(i)
