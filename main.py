from mathoperation.div import divValue
from mathoperation.mult import mulValue

if __name__ == '__main__':
    val1 = int(input('enter first number:  '))
    val2 = int(input('enter second number:  '))
    op = input('which math op you want to do ?')

    if op.lower() == 'div':
        a1 = divValue(val1,val2)
        print(f'division = {a1}')
    elif op.lower() == 'mul':
        a2 = multiplication(val1,val2)
        print(f'multiplication = {a2}')
    else:
        print('please choose correct operation, div,mul')