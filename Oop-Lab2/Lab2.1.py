n = int(input("input : "))

for i in range(1, n+1):
    print('*' * i)

print("--------------------------------")

for i in range(n, 0, -1):
    print('*' * i)

print("--------------------------------")

for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    for j in range(1, i + 1):
        if j < i:
            print('* ', end='')
        else:
            print('*')

print("--------------------------------")

for i in range(n, 0, -1):
    print(' ' * (n - i), end='')
    for j in range(1, i + 1):
        if j < i:
            print('* ', end='')
        else:
            print('*')

print("--------------------------------")

for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print('*' * i)

