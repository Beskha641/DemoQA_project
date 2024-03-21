import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(2000, 20000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        phone_number=random.randint(1000000000, 9999999999)
    )


def generated_file():
    file_path = rf'C:\Users\User\PycharmProjects\DemoQA_project\new_file{random.randint(0, 100)}.txt'
    file = open(file_path, 'w+')
    file.write(f'Hello world{random.randint(0, 100)}!')
    file.close()
    return file.name, file_path
