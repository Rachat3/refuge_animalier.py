# Identification du Composantes du script
#1. Les entrees
# ce que l'utilisatuer doit saissir au clavier.
nb_chiens=int(input("Entrez le nombre de chien:"))
nb_chats=int(input("Entrez le nombre de chats:"))
nb_lapins=int(input("Entrez le nombre de lapins:"))
#2.Les Traitements
#les Calculs (sommes) et les structures logiques (recherche du maximum).
# A. Calcul du total des animaux
total_animaux = nb_chiens+ nb_chats+ nb_lapins
# B. Recherche de l'espece dominante
if nb_chiens > nb_chats and nb_chiens > nb_lapins:
    dominant= "chiens"
elif nb_chats > nb_chiens > nb_lapins:
    dominant= "chats"
else:
    dominant= "lapins"
#3. Les Sorties
#Ce que le script va afficher a l'ecran pour l'utilisateur.
print("Total=",total_animaux)
print("Espece dominante:",dominant)