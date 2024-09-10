import random, bcrypt
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_+'

all_characters = lowercase + uppercase + numbers + symbols
a = int(input('Podaj długość hasła:'))


haslo = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(numbers),
    random.choice(symbols)
]

while len(haslo) <a:
    next_char = random.choice(all_characters)
    if next_char not in haslo:
        haslo.append(next_char)

random.shuffle(haslo)
haslo = ''.join(haslo)

hashed = bcrypt.hashpw(haslo.encode(), bcrypt.gensalt())
print(f'Hasło:{haslo}, zahaszowane:{hashed}')






