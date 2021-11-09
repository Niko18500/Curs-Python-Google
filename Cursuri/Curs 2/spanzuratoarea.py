# word = "a _ _ a _ _ t"
word = "alfabet"

# Formam lista de litere
word_list = []
for item in word:
    # Verificam daca avem prima sau ultima litera in interiorul cuvantului
    if item != word[0] and item != word[-1]:
        # Adaugam '_'
        word_list.append('_')
    else:
        # Adaugam litera
        word_list.append(item.lower())

# Ca sa facem lista ca string -> cu join (primul caracter -> delimiteaza elementele listei)
print(" ".join(word_list))

# Incercari pana la spanzurare (= 7)
count_nr = 1
# Lista literelor deja incercate
list_aready_checked = []

while count_nr <= 7:
    # Pt input (il facem lowercase)
    user_letter = input("Alege o litera: ").lower()

    # Daca nu s-a introdus nimic
    if user_letter == "":
        print("Introdu o litera")
        continue

    # Daca litera a fost deja ghicita
    if user_letter in word_list:
        print("Litera deja afisata")
    # Daca litera a fost deja aleasa de utilizator
    elif user_letter in list_aready_checked:
        print(f"Litera deja a fost incercata, literele deja incercate sunt: {' '.join(list_aready_checked)}")
    else:
        # Facem o lista cu literele deja incercate (ca sa nu incerce de mai multe ori aceeasi litera)
        if user_letter in word:
            # Litera exista in cuvant
            for i, value in enumerate(word):
                if user_letter == value:
                    word_list[i] = user_letter
            print(" ".join(word_list))
        else:
            count_nr += 1
        list_aready_checked.append(user_letter)
    if "".join(word_list) == word:
        print("Ai castigat")
        break
    elif count_nr > 7:
        print(f"Ai pierdut! Cuvantul era '{word}'")



# print(word_list.count(' ')) -> pt a numara chestii dintr-o lista

# Set -> elementele unice
print(set(word))

# Ca sa avem acces la variabile din alte fisiere
import random
from random_word import list_of_random_word
a_word = random.choice(list_of_random_word)