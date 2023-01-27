import hashlib
import json

try:
    with open("Passwords.json", "r") as f:
        hash_password = json.load(f)

except:
    hash_password = {}

#Afficher les conditions pour créer un mot de passe

menu = """
Votre mot de passe requiert au minimum  :
- 8 caractères
- une lettre minuscule 
- un lettre majuscule
-un caractère spécial : !@#$%^&*
"""
print(menu)

#Créer une fonction pour vérifier si les conditions sont bien remplies

def checkPassword():
    
    while True:
        password = input("Entrez un mot de passe: ")
        if len(password) < 8:
            print("Votre Mot de passe doit contenir au moins 8 caractères")
        elif not any(c in "0123456789" for c in password):
            print("Votre mot de passe doit contenir au moins un chiffre")
        elif not any(c in "abcdefghijklmnopqrstuvwxyz" for c in password):
            print("Votre mot de passse doit contenir au moins une Lettre minuscule")
        elif not any(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in password):
            print("Votre mot de passe doit contenir au moins une lettre majuscule")
        elif not any(c in "!@#$%^&*" for c in password):
            print ("Votre mot de passe doit contenir au moins un caractère spécial parmis !@#$%^&*")
        else:
            print("Mot de passe Validé")
            return password

#Fonction pour hacher le mot de passe

def hashpasswrd(password):
    passwordhashed = hashlib.sha256(password.encode()).hexdigest()
    return passwordhashed

#Fonction pour afficher le mot de passe haché (pas obligatoire mais plus facile pour les vérifications)

def print_password(password):
    print("Le mot de passe haché est :", hashpasswrd(password))

# demander le nom d'utilisateur
user = input("Entrez votre nom d'utilisateur : ")
# demande d'affichage des mots de passes deja enregistrés si l'utilisateur existe déja
if user in hash_password :
    printPassword = input("voulez vou afficher vos mots de passes existants ? (o/n) ")
    if printPassword == "o":
        print(hash_password[user])
    elif printPassword == "n":
        quit
# execution de la fonction de vérification du mdp
password=checkPassword()

# Enregistrement de l'utilisateur avec son mdp dans un fichier json 
# si le mot de passe existe déja envoyer un message 
if user not in hash_password :
    hash_password[user]= [hashpasswrd(password)] 
elif user in hash_password:
    if hashpasswrd(password) in hash_password[user]:
        print ("Mot de passe déja utilisé!")
        pass
    elif hashpasswrd(password) not in hash_password[user]: 
        hash_password[user] += [hashpasswrd(password)] 
        print("Mot de passe ajouté avec succes!")

# Ecriture des données avec les séparateurs dans le fichier json
with open("Passwords.json", "w") as f:
    json.dump(hash_password, f, separators=(",",": "), indent=4)