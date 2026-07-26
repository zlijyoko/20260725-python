# 輸入一個商品價格(整數)，用千分位格式印出，例如輸入 1234567 > 印出 總金額 1,234,567 元。

price = input( 'price = ')
price = int(price)
print(f"{price:,}")

# 輸入三科成績，計算平均後用 f-string 印出 [平均: xx.x 分] ( 小數點後第一位 )

English = int(input('English = '))
Math = int(input('Math = '))
Chinese = int(input('Chinese = '))
total = English + Math + Chinese
average = (f'{total}/{3} = {total / 3:.1f}')

print('average = ',average )

# 輸入你的身高(公尺) 與體重(公斤)，印出一張版面整齊的個人資料卡。

name = input( 'Name = ')
height = input( 'Height (m) = ')
weight = input( 'Weight (kg) = ')