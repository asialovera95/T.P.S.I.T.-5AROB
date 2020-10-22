'''lista = [
    a = 0,
    b = 1,
    c = 2,
    d = 3,
    e = 4,
    f = 5,
    g = 6,
    h = 7,
    i = 8,
    j = 9,
    k = 10,
    l = 11,
    m = 12,
    n = 13,
    o = 14,
    p = 15,
    q = 16,
    r = 17,
    s = 18,
    t = 19,
    u = 20,
    v = 21,
    w = 22,
    x = 23,
    y = 24,
    z = 25,
]
'''
chiave = 'itisdelpozzo'
messaggio = input(f'Scrivi qui il tuo messaggio: ')
print('Il messaggio da cifrare è: ', messaggio)

messaggio = messaggio.lower()

output = ['Il messaggio cifrato è: '] 

for character in messaggio:
    #messaggio1 = messaggio.split()
    numero = ord(character) - 96
    output.append(numero) 

print(output)

output1 = ['La chiave cifrata è: '] 
for character in chiave:
    numero = ord(character) - 96
    output1.append(numero) 

print(output1)

somma = output + output1
print(somma)

risultato = somma % 96
print(risultato)



