# this function will count backwards from 10 and ends with blastoff

def backwards(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        backwards(n - 1)

backwards(10)
