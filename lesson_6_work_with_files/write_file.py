with open('resources/example.txt', 'w') as file:
    file.write('Hello world')

with open('resources/example.txt') as file:
    file.readlines()
