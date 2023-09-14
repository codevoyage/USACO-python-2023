"""
ID: shikha11
LANG: PYTHON3
TASK: zerosum
"""

fin = open('zerosum.in', 'r')
fout = open('zerosum.out', 'w')

n = int(fin.readline().strip())

operators = [' ', '+', '-']


def compute_expression(expression):
    sign = '+'
    result = 0
    num = 0
    for i in range(0, len(expression), 2):
        digit = int(expression[i])
        if i+1 < len(expression):
            operator = expression[i + 1]
        else:
            operator = sign
        num = num * 10 + digit
        if digit == n or operator in ['+', '-']:
            if num == 0:
                num = digit
            if sign == '+':
                result += num
            elif sign == '-':
                result -= num
            sign = operator
            num = 0
    return result


def generate_expressions(expression, next_num):
    if next_num > n:
        if compute_expression(expression) == 0:
            fout.write(expression + '\n')
            return
    else:
        for op in operators:
            new_expression = expression + op + str(next_num)
            generate_expressions(new_expression, next_num + 1)


generate_expressions('1', 2)
