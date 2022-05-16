import random
def passwort(laenge = 16):
    buchstaben = "abcdefghijklmnopqrstuvwxyz"
    ziffern = "0123456789"
    sonderzeichen = "!$%&#ß[]{}"
    zeichen = buchstaben + buchstaben.upper() +\
              ziffern + sonderzeichen
    passwort = ""
    for i in range(laenge):
        passwort += random.choice(zeichen) 
    return passwort
print("Passwort: ", passwort())
