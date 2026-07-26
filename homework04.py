# 輸入姓名與年齡，輸出 [ XXX 明年 XX 歲 ]。

name = input('name = ')
age = input('age = ')
x = int(age)

print("My name is ", name, ", I will be  ", (x + 1), " years old next year.")

# 輸入圓半徑，輸出圓面積(取小數點後兩位，π 用 3.14159)。
# 面積 = π * r²

π = float( 3.14159 )
r = input(" r : ")
r = float( r )
r2 = r*r
r2 = float( r2 )
area = (f"{3.14159} * {r2} = {3.14159*r2:.2f}")
print('area = ',area)

# 輸入攝氏溫度，輸出華氏溫度( 公式 : F = C * 9 / 5 + 32 )

C = input('C: ')
C = float( C )
F = C * 9 / 5 + 32
print( F )
