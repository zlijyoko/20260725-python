# 輸入一個分數，判斷及格 (>=60) 或不及格，印出對應文字。

score = int(input('score: '))

if 0<= score <= 100:
    if score < 60:
        print("sorry...")
    else:
        print("good job!")
else:
    print("input out of range")

# 輸入一個分數，依下列規則印出等第:

score = int(input('score: '))

if score >= 90:
        print( "A" )
elif score >= 80:
        print( "B" )
elif score >= 70:
        print( "C" )
elif score >= 60:
        print( "D" )
else:
    print( "F" )

# 輸入一個整數，判斷它是正數/負數還是零。

number = int(input('number: '))

if number > 0:
    print('正數')
elif number == 0:
    print('零')
else:
    print('負數')




