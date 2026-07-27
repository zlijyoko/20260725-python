# 輸入一個整數，先只印出 n % 2 的值，觀察它與奇偶的關係。

integer = int(input( 'integer = '))
print('remainder = ' ,integer % 2)

""" 如果是偶數 = 0 ，是奇數的話 = 1 """

# 輸入秒數 (例如 3725)，輸出 [ 一小時兩分五秒 ]。
second = int(input( 'second = ' ))

if second / 60 > 60 :
    minute = second / 60
    print ( '0 小時 ', minute, '分 ', second,' 秒 ')
    if minute / 60 > 60 :
        hour = minute / 60
        print ( hour,' 小時 ', minute, '分 ', second,' 秒 ')
    else :
        print ( '0 小時 ', minute, '分 ', second,' 秒 ')
else :
    print ( '0 小時 0 分 ', second,' 秒 ')

# 先不要執行，猜出下列四式的結果與型別，再驗證 :
# 10 / 3 ， 10 // 3 ， 10 % 3 ， 10 ** 3

"""
猜
10 / 3 : 3.333333...
10 // 3 : 3
10 % 3 : 1
10 ** 3 : 不知道
"""
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

"""
10 / 3 : 3.333333...
10 // 3 : 3
10 % 3 : 1
10 ** 3 : 1000
"""
