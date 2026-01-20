n = int(input())

def hollow(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('* ' * n)
        else:
            print('*' + ' ' * (2*n-3) + '*')

hollow(n)