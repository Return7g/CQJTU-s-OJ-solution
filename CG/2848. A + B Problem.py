# 该题无法确定输入数据长度
# 因此使用while循环加try-except的结构处理输入
while True:
    try:
        print(sum([int(x) for x in input().split(" ")]))
    except:
        break
