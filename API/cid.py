from faker import Faker
import random

fake = Faker()
cities = set()

while len(cities) < 1000:
    city = fake.city()
    cities.add(city)

ciudades_lista = list(cities)
print(ciudades_lista)