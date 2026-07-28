# 入場判斷 : 輸入年齡與是否有票(y/n)。

years_old = int(input('years_old : '))
ticket = input('ticket( yes / no ) : ')

if years_old <= 18 and ticket == 'yes' :
    print ( '禁止入場' )
elif years_old <= 18 and ticket == 'no' :
    print ( '禁止入場' )
elif years_old >= 18 and ticket == 'yes' :
    print ( '可以入場' )
elif years_old >= 18 and ticket == 'no' :
    print ( '請先購票' )
else :
    print ( '禁止入場' )

# 除錯題 : 以下程式為什麼所有人都印出 [不及格] ? 請找出原因並修正。

"""
score = input('分數')
if score >= 60:
    print('及格')
else:
    print('不及格')
"""
score = int(input('分數'))
if score >= 60:
    print('及格')
else:
    print('不及格')

# 需要先將 input 中得到，轉為整數 int。