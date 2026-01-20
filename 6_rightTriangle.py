n = int(input())

def left(n):
    for i in range(n):
        print('*'*(i+1))

def downRight(n):
    for i in range(n):
        print(' '*(i)+'* '*(n-i))

# downRight(n)

def right(n):
    for i in range(n):
        print(' '*(n-i-1)+'*'*(i+1))
right(n)