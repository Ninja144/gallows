import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  0   |
  |   |
      |
     ===''', '''
  +---+
  0   |
 /|   |
      |
     ===''', '''
  +---+
  0   |
 /|\  |
      |
     ===''', '''
  +---+
  0   |
 /|\  |
 /    |
     ===''', '''
  +---+
  0   |
 /|\  |
 / \  |
     ===''']
38. words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея
индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон
попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()
39.
40. def getRandomWord(wordList):
41. # Эта функция возвращает случайную строку из переданного списка.
42. wordIndex = random.randint(0, len(wordList) - 1)
43. return wordList[wordIndex]
44.
45. def displayBoard(missedLetters, correctLetters, secretWord):
46. print(HANGMAN_PICS[len(missedLetters)])
47. print()
48.
49. print('Ошибочные буквы:', end=' ')
50. for letter in missedLetters:
51. print(letter, end=' ')
52. print()
53.
54. blanks = '_' * len(secretWord)
55.
56. for i in range(len(secretWord)): # заменяет пропуски отгаданными буквами
57. if secretWord[i] in correctLetters:
58. blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
59.
60. for letter in blanks: # Показывает секретное слово с пробелами между буквами
61. print(letter, end=' ')
62. print()
63.
64. def getGuess(alreadyGuessed):
65. # Возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввел только одну букву и ничего больше.
66. while True:
67. print('Введите букву.')
68. guess = input()
69. guess = guess.lower()
70. if len(guess) != 1:
71. print('Пожалуйста, введите одну букву.')
72. elif guess in alreadyGuessed:
73. print('Вы уже называли эту букву. Назовите другую.')
74. elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
75. print('Пожалуйста, введите БУКВУ.')122 Глава 8
76. else:
77. return guess
78.
79. def playAgain():
80. # Эта функция возвращает значение True, если игрок хочет сыграть заново; в противном случае возвращает False.
81. print('Хотите сыграть еще? (да или нет)')
82. return input().lower().startswith('д')
83.
84.
85. print('В И С Е Л И Ц А')
86. missedLetters = ''
87. correctLetters = ''
88. secretWord = getRandomWord(words)
89. gameIsDone = False
90.
91. while True:
92. displayBoard(missedLetters, correctLetters, secretWord)
93.
94. # Позволяет игроку ввести букву.
95. guess = getGuess(missedLetters + correctLetters)
96.
97. if guess in secretWord:
98. correctLetters = correctLetters + guess
99.
100. # Проверяет, выиграл ли игрок.
101. foundAllLetters = True
102. for i in range(len(secretWord)):
103. if secretWord[i] not in correctLetters:
104. foundAllLetters = False
105. break
106. if foundAllLetters:
107. print('ДА! Секретное слово - "' + secretWord + '"! Вы угадали!')
108. gameIsDone = True
109. else:
110. missedLetters = missedLetters + guess
111.
112. # Проверяет, превысил ли игрок лимит попыток и проиграл.
113. if len(missedLetters) == len(HANGMAN_PICS) - 1:
114. displayBoard(missedLetters, correctLetters, secretWord)
115. print('Вы исчерпали все попытки!\nНе угадано букв: ' + str(len(missedLetters)) + ' и угадано букв: ' + str(len(correctLetters)) + '. Было загадано слово "' + secretWord + '".')
116. gameIsDone = True
117. Написание кода игры «Виселица» 123
118. # Запрашивает, хочет ли игрок сыграть заново (только если игра завершена).
119. if gameIsDone:
120. if playAgain():
121. missedLetters = ''
122. correctLetters = ''
123. gameIsDone = False
124. secretWord = getRandomWord(words)
125. else:
126. break