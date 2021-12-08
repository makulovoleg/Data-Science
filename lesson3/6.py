def int_func(text):
    return text.title()

out_text = []
for word in input('Введите строку чисел, разделенных пробелом').split(' '):
    out_text.append(int_func(word))
print(" ".join(out_text))