# 輸入姓名與年齡，輸出 [ XXX 明年 XX 歲 ]。

name = input('name = ')
age = input('age = ')
x = int(age)

print("My name is ", name, ", I will be  ", (x + 1), " years old next year.")

# 輸入圓半徑，輸出圓面積(取小數點後兩位，π 用 3.14159)。
# 面積 = π * r²

π = int(3.14159)
r = input(" r = ")
r2 = (f"{r} ^ {2} = {r**2}")
area = (f"{π} * {r2} = {π*r2}")

print('area = ',area)