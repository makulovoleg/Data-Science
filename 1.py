file = open('test.txt', 'w')
text = input('Введите текст \n')
while text:
    file.writelines(f'{text} \n')
    text = input('Введите текст \n')
    if not text:
        break
file.close()
