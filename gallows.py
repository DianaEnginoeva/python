# выбор соперника
def choose_opponent():
    opponent = input('Choose an opponent (computer or person): ')
    if opponent == 'computer':
        word = 'cat'
    elif opponent == 'person':
        word = input('Enter a word: ')
    else:
        print('Incorrect choice')
    word_handler(word)

        

#обработчик слов
def word_handler(word):
	underlines_count = len(word)
	underlines = ''
	i = 1
	for i in range(underlines_count):
		underlines = underlines + '_'
		i += 1
	print('Guess the word', underlines)
	draw_startgallows(word, underlines)


# функции входящие в состав функции play
# печатать начальную виселицу
def draw_startgallows(word, underlines):
	start_gallows = "----------------------\n|          |\n|          |\n|\n|\n|\n|\n|\n|\n|\n"
	print(start_gallows)
	draw_startgallows(word, underlines)

# поиск угаданных букв
def right_letters(probably_letter, word):
	underlines = ''
	j = 0
	for i in range(0, len(word)):
		if probably_letter in word:
			index_letter = word.index(probably_letter)
			if i == index_letter:
				underlines = underlines + word[index_letter]
				i += 1
			else:
				underlines = underlines + '_'
				i += 1
			print(underlines)
			gap = '_'
			if gap in underlines:
				process_of_game(word, underlines)
			else:
				check_win(False, True)
				

# проверка выигрыша после каждого хода
def check_win(player1_win, player2_win):
    if player1_win == True:
        print("You didn't guess the word. Player1 is win!")
    elif player2_win == True:
        print("Congratulations! You guessed the word. Player2 is win!")

#
def process_of_game(word, underlines):
    probably_letter = input('Write letter: ')
    right_letters(probably_letter, word)


# главная функция
def main():
    choose_opponent()
    
        
        

def play(word, underlines):
    player1_win = False
    player2_win = False
    process_of_game(word, underlines)
    
    
        
        
    
    

      
