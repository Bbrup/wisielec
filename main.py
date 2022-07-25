# Step 1
import random
import os

word_list = ["banan", "truskawka", "gruszka"]
pusta = []



stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

randomek_letters = random.randint(0, len(word_list) - 1)
#print(word_list[randomek_letters]) #- wylosowane slowo z tablicy

for i in range(len(word_list[randomek_letters])):
    pusta += "_"

End_of_game = False
zycie = 6

while not End_of_game:

    print(stages[zycie])
    print(pusta)

    if zycie == 0:
        print("Przegrales")
        break



    litera = input("Podaj litere ").lower()


    if litera==word_list[randomek_letters]:
            End_of_game = True;
            print("Wygrales")
            print("Hasło to:"+word_list[randomek_letters])
    else:

        odgadniete = False

        for i in range(len(word_list[randomek_letters])):
            if word_list[randomek_letters][i] == litera:
                pusta[i] = litera
                odgadniete = True

        if odgadniete == False:
            print("Pudło!")
            zycie -= 1

        #print(pusta)


        if "_" not in pusta:

            End_of_game = True;
            print("Wygrales")
            print("Hasło to:"+word_list[randomek_letters])




