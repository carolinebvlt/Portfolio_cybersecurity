# Jeu du pendu
import os
from random import randint

# Importe la liste de mots en parsant un fichier .txt
base_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(base_dir, "pendu_liste_de_mots.txt")

with open(path, "r") as file :
    words_list_txt = file.read()
    words_list = words_list_txt.split("\n")

# L'ordinateur choisi un mot au hasard et indique le nombre de caractères
word_to_guess = words_list[randint(0, len(words_list))-1].strip()
word_to_guess = list(word_to_guess)
# print(word_to_guess)
printed_word = []
for letter in word_to_guess :
    printed_word.append("_")
print(f"Devine ce mot de {len(word_to_guess)} caractères : ")
print(printed_word)

# Initialisation du compteur de tentatives ratées, du nombre d'échecs max et de la liste des mauvaises lettres
failed_attempts = 0
max_failed_attempts = 6
failed_attempts_list = []

while failed_attempts <= max_failed_attempts and '_' in printed_word :
    
    # Demander à l'utilisateur d'entrer une lettre
    letter_attempt = ""
    while len(letter_attempt) != 1 :
        letter_attempt = input("Choisissez une lettre (a-z) : " )
        letter_attempt = letter_attempt.lower()
    
    # Si la lettre fait partie du mot, on en remplace toutes les occurences à la bonne place
    if letter_attempt in word_to_guess :
        for i in range(0, len(word_to_guess)) :
            if letter_attempt == word_to_guess[i] :
                printed_word[i] = letter_attempt
    
    # Sinon, on ajoute la tentative ratée à la liste
    else :
        failed_attempts += 1
        failed_attempts_list.append(letter_attempt)
        print(f"Cette lettre n'est pas dans le mot : {letter_attempt}")
    
    print(printed_word)
    print(f"Tentatives ratées : {failed_attempts} ({failed_attempts_list}) ")

if failed_attempts > max_failed_attempts :
    print(f"Perdu, vous voilà pendu ! Le mot était : {str(word_to_guess)}")
elif printed_word == word_to_guess :
    print(f"Félicitations ! Vous avez deviné le mot !")