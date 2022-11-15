import random, os, sys

pic=['''

   +---+
   |   |
       |
       |
       |
       |
=========''','''

   +---+
   |   |
   O   |
       |
       |
       |
=========''','''

   +---+
   |   |
   O   |
   |   |
       |
       |
=========''','''

   +---+
   |   |
   O   |
  /|   |
       |
       |
=========''','''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========''','''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========''','''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''']

words = 'муравей бабуин барсук медведь бобр верблюд кошка моллюск кобра пума койот ворона олень собака осел утка орел хорек лиса лягушка коза гусь ястреб ящерица лама моль обезьяна лось мышь мул тритон выдра сова панда попугай голубь питон кролик баран крыса носорог лосось акула змея паук аист лебедь тигр жаба форель индейка черепаха ласка кит волк вомбат зебра'.split()

secretWord=words[random.randint(0, len(words) - 1)]

clear = lambda: os.system('cls')

word=['*' for i in range(len(secretWord))]
usedLetters=''
k=0

print(pic[0])

while k<=len(pic):
    if ''.join(word).find('*')==-1:
        print('Вы победили')
        sys.exit()

    print(''.join(word))
    print(f'Использованные буквы: {usedLetters} ')
    print('Введите букву:')
    letter=input().lower()

    e=[]
    for i in range(len(secretWord)):
        if secretWord[i]==letter:
            e.append(i)
    if str(e)=='[]':
        if letter not in usedLetters:
            usedLetters=usedLetters+letter
            k=k+1
            print(clear())
            print(pic[k])
        else:
            print(clear())
            print(pic[k])
        if k==6:
            print('Вы проиграли')
            print(f'Загаданное слово: {secretWord}')
            sys.exit()
    else:
        for i in e:
            word[i]=letter
            print(clear())
            print(pic[k])

