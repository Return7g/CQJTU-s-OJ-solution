while True:
    try:
        # 获取输入
        n = int(input())
        nums = [int(i) for i in input().split()]
        # 此时不需要考虑算法，直接计算结果即可
        ans = sum(nums) / n
        print(f"{ans:.1f}")
    except:
        break
