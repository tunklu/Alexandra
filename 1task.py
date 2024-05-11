def compare_number(in_string):
    result_string = ''
    index = 0
    while index < 50:
        if (in_string[index] == '2') and (in_string[index+1] == '2'):
            result_string += '*'
            index += 2
        else:
            result_string += in_string[index]
    return (result_string)


string_ = '22222222222222222222222222222222222222222222222222'
print(compare_number(string_))
