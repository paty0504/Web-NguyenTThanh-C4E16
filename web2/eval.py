from random import choice
# x = 3
# op = choice(['+', '-', '*', '/'])
# y = 7
# if op == "+":
#     result = x + y
# elif op == "-":
#     result = x - y
# elif op == "*":
#     result = x*y
# elif op == "/":
#     result = x/y
# print(result)
op = choice(['+', '-', '*', '/'])
def calc(x, y, op):



    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x*y
    elif op == "/":
        result = x/y
    return result  #đưa ra ngoài scope
# res = calc(3, 7, '+') #hứng kết quả bằng biến
# print(res)
# r = calc(1, 2, '-')
# print(r)

#argument, parameter: tham số đầu vào


#scope: phạm vi làm việc
