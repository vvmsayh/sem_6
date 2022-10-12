# - Добавьте возможность использования скобок, меняющих приоритет операций.
        
#         *Пример:* 
        
#         1+2*3 => 7; 
        
#         (1+2)*3 => 9;
def my_action(op, digit_1, digit_2):

    if op == '+':
        return digit_1 + digit_2
    elif op == '-':
        return digit_1 - digit_2
    elif op == '/':
        return digit_1 // digit_2
    elif op == '*':
        return digit_1 * digit_2


my_string = '1+2+3*5-6/3+7-9*0-4'
my_list_symbols = [i for i in my_string if not i.isdigit()]

my_list_digits = [int(i) for i in my_string if i.isdigit()]
while"*" in my_list_symbols or  '/' in my_list_symbols:
    for i, e in enumerate(my_list_symbols):
        if e in ('*', '/'):
            my_list_digits[i] = my_action(
                e, my_list_digits[i], my_list_digits[i+1])
            del my_list_digits[i+1]
            del my_list_symbols[i]
while my_list_symbols: 
    for i, e in enumerate(my_list_symbols):
        my_list_digits[i] = my_action(
        e, my_list_digits[i], my_list_digits[i+1])
        del my_list_digits[i+1]
        del my_list_symbols[i]
print(my_list_digits)
