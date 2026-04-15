def cesar(text, k):
    """Chiffre ou déchiffre un texte avec un décalage k"""
    result = ""
    for char in text:
        if char.isalpha():
            # Décalage de base selon la casse
            base = ord('A') if char.isupper() else ord('a')
            # Application du décalage (modulo 26)
            result += chr((ord(char) - base + k) % 26 + base)
        else:
            result += char  # Conserve espaces, ponctuation, chiffres
    return result

# Paramètres
k = 4
mots = ["BONJOUR", "HELLO", "MPSSIR"]

print("=" * 40)
print(f"CHIFFREMENT DE CÉSAR (k={k})")
print("=" * 40)

# Traitement automatique des 3 mots
for mot in mots:
    chiffre = cesar(mot, k)
    dechiffre = cesar(chiffre, -k)
    
    print(f"\nMot : {mot}")
    print(f"  → Chiffré : {chiffre}")
    print(f"  → Déchiffré : {dechiffre}")

# Option : traiter une saisie utilisateur
print("\n" + "=" * 40)
print("TESTEZ VOS PROPRES MOTS")
print("=" * 40)

while True:
    choix = input("\nVoulez-vous (1) Chiffrer, (2) Déchiffrer ou (3) Quitter ? ")
    
    if choix == '1':
        texte = input("Entrez le texte à chiffrer : ").upper()
        print(f"Résultat : {cesar(texte, k)}")
    
    elif choix == '2':
        texte = input("Entrez le texte à déchiffrer : ").upper()
        print(f"Résultat : {cesar(texte, -k)}")
    
    elif choix == '3':
        print("Au revoir !")
        break
    
    else:
        print("Choix invalide")