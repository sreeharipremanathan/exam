from modules.add import*
from modules.sub import*
from modules.mul import*
from modules.div import*
from modules.mod import*
num1=int(input('enter a number: '))
num2=int(input('enter a number: '))
while True:
    print('''
        1.add
        2.sub
        3.multi
        4.div
        5.mod
''')
    ch=int(input('select op: '))
    if ch==1:
        add(num1,num2)
    elif ch==2:
        sub(num1,num2)
    elif ch==3:
        multi(num1,num2)
    elif ch==4:
        div(num1,num2)
    elif ch==5:
        mod(num1,num2)