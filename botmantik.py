import random

def sifre_olusturucu(parola_uzunlugu ):
    karakterler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    parola = ""
    for _ in range(parola_uzunlugu):
        rastgele_karakter = random.choice(karakterler)
        parola += rastgele_karakter

    return parola

def double_letter (str):
    result = ''
    for letter in str:
        result += letter * 2
    return result

def yazitura ():
    random_number = random.randint(1,2)
    if random_number == 1:
        return 'Yazı'
    else:
        return 'Tura'
