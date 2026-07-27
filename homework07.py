# 先猜再驗證下列各式的結果 ( Ture 或 False )

"""
猜
5 == 5 #True
5 != 3 #False
3 >= 5 #False
(10 > 5) and (2 > 8) #False
(10 > 5) or (2 > 8) #False
not (3 == 3) #True
"""

print(5 == 5) #True 
print(5 != 3) #True
print(3 >= 5) #False
print((10 > 5) and (2 > 8)) #False
print((10 > 5) or (2 > 8)) #True
print(not (3 == 3)) #False

# 有一個分數 score，請用一行條件式判斷它是否落在 60 到 89 (含) 之間，善用 Python 的連續比較寫法。

score = int(input('score: '))

if 60<= score <= 89:
    if score < 60:
        print("sorry...")
    else:
        print("good job!")
else:
    print("input out of range (0~100)")

# 說明 = 與 == 的差別，並指出下列哪一行是語法錯誤 :

"""
if x = 5:
if x == 5:
"""
# 第一行，應該用 == 或 . 代替。
# == 是邏輯判斷，= 是給東西它的身分。

