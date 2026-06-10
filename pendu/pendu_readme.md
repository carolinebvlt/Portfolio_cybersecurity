# Création d'un jeu du pendu

[Code du jeu](https://github.com/carolinebvlt/Portfolio_cybersecurity/blob/main/pendu/pendu.py)

## Algorithme 
- l'ordinateur choisi un mot parmi une liste (fichier séparé), et indique à l'utilisateur le nombre de caractères
- le nombre de tentatives ratées est limité à 6, la 7ème = Game over (corde, tête, corps, bras, jambes)
- l'ordinateur demande à l'utilisateur d'entrer une lettre
- si la lettre fait partie du mot, elle s'affiche (toutes les occurences) à la bonne place
- si la lettre ne fait pas partie du mot, cela compte comme une tentative ratée et affichée dans la liste des lettres incorrectes déjà tentées
- Si le joueur trouve le mot avant d'avoir fait 7 mauvaises tentatives, c'est gagné
- Si le joueur atteint les 7 tentatives ratées, il a perdu

## Compétences Python
- Utilisation de `input()`
- Manipulation de `list` et de `str`
- Utilisation de conditions `if`, `else`
- Boucles `while` et `for`