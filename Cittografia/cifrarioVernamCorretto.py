
message = input(f"inserisci: ")
print('messaggio cifrato', message)

key = "itisdelpozzo"

def vernam(key,message):
    message = str(message)
    m = message.upper().replace(" ","") # Convert to upper case, remove whitespace
    encrypt = ""
    try:
        key = int(key)           # if the key value is not a number, then run with key = 0
    except ValueError:
        key = 0
    for i in range(len(m)):
        letter = ord(m[i])-65      # Letters now range 0-25
        letter = (letter + key)%25 # Alphanumeric + key mod 25 = 0-25
        letter +=65
        

        encrypt = encrypt + chr(letter) # Concatenate message
        
    return encrypt
    
