# 輸入一個商品價格(整數)，用千分位格式印出，例如輸入 1234567 > 印出 總金額 1,234,567 元。

price = input( 'price = ')
price = int(price)
print(f"{price:,}")
