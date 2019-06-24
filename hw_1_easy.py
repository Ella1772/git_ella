input_string = input('Введите число\n')
i=0

while i <= len(input_string):
    print(input_string[i])
    i = i+1
    if i == len(input_string):
        break