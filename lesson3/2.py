def person(name, lastname, year_of_birth, city, email, phone):
    return f'{name} {lastname} {year_of_birth} {city} {email} {phone}'

name = input('Имя ')
lastname = input('Фамилия ')
year_of_birth = input('Дата рождения ')
city = input('Город ')
email = input('Почта ')
phone = input('Телефон ')

print(person(name, lastname, year_of_birth, city, email, phone))



