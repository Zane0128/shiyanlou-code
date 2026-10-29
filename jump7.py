# jump7.py
# 逢7跳过：打印1-100，包含7或者是7的倍数的数字跳过

for i in range(1, 101):
    # 判断是否包含7（个位是7或十位是7）或者是7的倍数
    if i % 7 == 0 or '7' in str(i):
        continue
    print(i)
