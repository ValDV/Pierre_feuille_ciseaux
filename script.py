from random import choice

liste_signes = ["pierre","feuille", "ciseaux"]
signe_ordi = choice(liste_signes)
signe_joueur = input("Choisissez pierre, feuille ou ciseaux :")
signe_joueur = signe_joueur.lower()

print("Vous avez choisi", signe_joueur)
print("L'Ordinateur a choisi", signe_ordi)

if signe_ordi == signe_joueur :
  print("Egalite")
  
elif signe_joueur == "pierre" and signe_ordi == "ciseaux" :
  print("Victoire Utilisateur")
  
elif signe_joueur == "feuille" and signe_ordi == "pierre" :
  print("Victoire Utilisateur")
  
elif signe_joueur == "ciseaux" and signe_ordi == "feuille" :
  print("Victoire Utilisateur")
  
else :
  print("Victoire Ordinateur")