def chiffrement_cesar(mot, k):
    """Chiffre un mot avec un décalage k (César)."""
    resultat = ""
    for lettre in mot:
        if lettre.isalpha():
            # Garder la casse (majuscule/minuscule)
            if lettre.isupper():
                resultat += chr((ord(lettre) - 65 + k) % 26 + 65)
            else:
                resultat += chr((ord(lettre) - 97 + k) % 26 + 97)
        else:
            resultat += lettre  # Garder les caractères non alphabétiques
    return resultat

def dechiffrement_cesar(mot_chiffre, k):
    """Déchiffre un mot chiffré avec César (décalage inverse)."""
    return chiffrement_cesar(mot_chiffre, -k)

# Mots à traiter
mots = ["BONJOUR", "HELLO", "MPSSIR"]
k = 4

print("=== CHIFFREMENT DE CÉSAR ===")
print(f"Clé utilisée : k = {k}\n")

for mot in mots:
    mot_chiffre = chiffrement_cesar(mot, k)
    mot_dechiffre = dechiffrement_cesar(mot_chiffre, k)
    
    print(f"Mot original   : {mot}")
    print(f"Mot chiffré    : {mot_chiffre}")
    print(f"Mot déchiffré  : {mot_dechiffre}")
    print("-" * 30)