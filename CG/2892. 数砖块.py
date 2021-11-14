while True:
    n = int(input())
    if n == 0:  # 程序终止条件
        break
    # 利用递推解题
    a, b = 1, 0
    for i in range(2, n + 1):
        a, b = 2 * a - b + i, a
    print(a)
