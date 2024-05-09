N = int(input('Enter N: '))
K = int(input('Enter K: '))

for i in range(1, N+1):
    if i % K == 0:
        print(i)