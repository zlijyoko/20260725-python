# 輸入三個數字，找出最大值 (不使用 max())。

a = int(input( 'number1 = '))
b = int(input( 'number2 = '))
c = int(input( 'number3 = '))

if a>b>c or a>c>b or a>b==c or a>c==b :
    print('max = a')
elif b>a>c or b>c>a or b>a==c or b>c==a :
    print('max = b')
elif c>b>a or c>a>b or c>a==b or c>b==a :
    print('max = c')
elif a<b==c or a<c==b :
     print('max = b and c')
elif b<a==c or b<c==a :
     print('max = a and c')
elif c<b==a or c<a==b :
     print('max = a and b')
else :
    print('same')

# 輸入年分，判斷是否為閏年。

year = int(input('year = '))

if year % 400 == 0 :
    print('閏年')
elif year % 4 == 0 :
        if year % 100 != 0 :
             print('閏年')
        else :
             print('平年')
else :
     print('平年')

# BMI 計算機 : 輸入身高(公分) 與體重(公斤)，計算 BMI 並分級 :
# 過輕 <18.5 / 正常 18.5 - 24 / 過重 24 - 27 / 肥胖 >= 27。

Height = float(input('Height(cm) : '))
Weight = float(input('Weight(kg) : '))

miles = Height / 100
miles = float(miles)
m2 = miles * miles
m2 = float(m2)
BMI = Weight / m2
print( f'BMI = {BMI:.1f}')

if BMI < 18.5 :
     print ('過輕')
elif 18.5 <= BMI < 24 :
     print ('正常')
elif 24 <= BMI < 27 :
     print ('過重')
else :
     print ('肥胖')