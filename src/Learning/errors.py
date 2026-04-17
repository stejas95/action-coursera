

def check_n(n):
    if n%2 != 0:
        print("Weird")
    elif n<5 and n%2 == 0:
        print("Not Weird")
    elif n>=6 and n<=20 and n%2 == 0:
        print("Weird")
    elif n>20 and n%2 == 0:
        print("Not Weird")


n = int(input().strip())
result = check_n(n)
