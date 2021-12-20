file = open('test.txt', 'w')
text = input('Введите текст \n')
while text:
    file.writelines(text)
    text = input('Введите текст \n')
    if not text:
        break

file.close()
file = open('test.txt', 'r')
content = file.readlines()
print(content)
file.close()