from datetime import datetime
birth_year = input('Birth year: ')
age = datetime.now().year - int(birth_year)
print(age)