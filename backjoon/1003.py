n = input()
for _ in range(int(n)):
    T = input()
    zero, one = 1, 0
    for _ in range(int(T)):
        zero, one = one, zero+one
    print(zero, one)




