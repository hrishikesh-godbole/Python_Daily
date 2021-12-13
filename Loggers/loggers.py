import logging

logging.basicConfig(filename='test,log',level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

num1 = 50
num2 = 8

add_result = add(num1, num2)
logging.debug('Add: {} + {} = {}'.format(num1,num2,add_result))

sub_result = sub(num1, num2)
logging.debug('Sub: {} - {} = {}'.format(num1,num2,sub_result))

mul_result = mul(num1, num2)
logging.debug('Mul: {} * {} = {}'.format(num1,num2,mul_result))

div_result = div(num1, num2)
logging.debug('Sub: {} / {} = {}'.format(num1,num2,div_result))