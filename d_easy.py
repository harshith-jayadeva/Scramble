import pygame
import pygame as pg
import sys
import random

from words import *


# Constants
pg.init()
WIDTH, HEIGHT = 1275, 695

display = pg.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
main_font = pg.font.SysFont("cambria", 50)

GREEN = "#6aaa64"
YELLOW = "#ff2d00"
GREY = "#787c7e"
nardo_grey = "686A6C"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"
midnight = (70, 70, 70)
black = (50, 50, 50)
cream = (255, 255, 250)


home_button = 'd_home_button.png'
home_hover = 'd_home_hover.png'
next_button = 'd_next_button.png'
next_hover = 'd_next_hover.png'



list = ''

ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

GUESSED_LETTER_FONT = pg.font.Font("FreeSansBold.otf", 40)
AVAILABLE_LETTER_FONT = pg.font.Font("FreeSansBold.otf", 20)

display.fill(cream)

pg.display.update()

LETTER_X_SPACING = 70
LETTER_Y_SPACING = 70
LETTER_SIZE = 60

title = pg.image.load('dark_play_bg.png')

title_align = title.get_rect(center=((WIDTH/2), HEIGHT/2))
display.blit(title, title_align)


a = easy_words[random.randint(0, (len(easy_words) - 1))]
CORRECT_WORD = a
unknown_word = str(''.join(random.sample(a, len(a))))
scrambled_word_font = pg.font.Font("FreeSansBold.otf", 40)
scrambled_word_text = scrambled_word_font.render(unknown_word, True, cream)
scrambled_rect = scrambled_word_text.get_rect(center=(WIDTH/2, 50))
display.blit(scrambled_word_text, scrambled_rect)
pg.display.update()


class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.img = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.img.get_rect(center=(self.x_pos, self.y_pos))
        self.txt_input = text_input
        self.txt = main_font.render(self.txt_input, True, black)
        self.txt_rect = self.txt.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        display.blit(self.img, self.rect)
        display.blit(self.txt, self.txt_rect)



    def checkInput1(self, position):
        global counter
        counter = 0
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):

            from testing_space import dark_background

    def checkInput2(self, position):
        global counter
        counter = 0
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            import dark_medium

    def home_button(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            button1 = pg.image.load(home_hover)
            button_align = button1.get_rect(center=(500, 500))
            display.blit(button1, button_align)
        else:
            button2 = pg.image.load(home_button)
            button2_align = button2.get_rect(center=(500, 500))
            display.blit(button2, button2_align)

    def next_button(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            button1 = pg.image.load(next_hover)
            button_align = button1.get_rect(center=(775, 500))
            display.blit(button1, button_align)
        else:
            button2 = pg.image.load(next_button)
            button2_align = button2.get_rect(center=(775, 500))
            display.blit(button2, button2_align)

button_surface = pg.image.load(home_button)
button = Button(button_surface, 500, 500, '')

button_surface1 = pg.image.load(next_button)
button1 = Button(button_surface1, 775, 500, '')



def scrambled_word():
    a = easy_words[random.randint(0, (len(easy_words)-1))]
    CORRECT_WORD = a
    unknown_word = str(''.join(random.sample(a, len(a))))
    scrambled_word_font = pg.font.Font("FreeSansBold.otf", 40)
    scrambled_word_text = scrambled_word_font.render(unknown_word, True, "black")
    scrambled_rect = scrambled_word_text.get_rect(center=(WIDTH/2, 45))
    display.blit(scrambled_word_text, scrambled_rect)
    pg.display.update()


# Global variables

guesses_count = 0
score_board = guesses_count

if score_board == 1:
    score = 25
    score_display = pg.font.Font("FreeSansBold.otf", 40)
    score_text = score_display.render(score, True, "black")


# guesses is a 2D list that will store guesses. A guess will be a list of letters.
# The list will be iterated through and each letter in each guess will be drawn on the screen.
guesses = [[]] * 4

current_guess = []
current_guess_string = ""
current_letter_bg_x = 470

# Indicators is a list storing all the Indicator object. An indicator is that button thing with all the letters you see.
indicators = []

game_result = ""


class Letter:
    def __init__(self, text, bg_position):

        global GREY, black, cream
        # Initializes all the variables, including text, color, position, size, etc.
        self.bg_color = GREY
        self.text_color = cream
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1] + 55
        self.bg_rect = (bg_position[0], self.bg_y, LETTER_SIZE, LETTER_SIZE)
        self.text = text
        self.text_position = (self.bg_x + 30, self.bg_position[1] + 85)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self):
        # Puts the letter and text on the screen at the desired positions.
        pg.draw.rect(display, self.bg_color, self.bg_rect)
        if self.bg_color == cream:
            pg.draw.rect(display, FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        display.blit(self.text_surface, self.text_rect)
        pg.display.update()

    def delete(self):
        global GREY, OUTLINE
        # Fills the letter's spot with the default square, emptying it.
        pg.draw.rect(display, GREY , self.bg_rect)
        pg.draw.rect(display, OUTLINE, self.bg_rect, 3)
        pg.display.update()


class Indicator:
    def __init__(self, x, y, letter):
        global GREY
        # Initializes variables such as color, size, position, and letter.
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 50, 50)
        self.bg_color = GREY

    def draw(self):
        # Puts the indicator and its text on the screen at the desired position.
        pg.draw.rect(display, self.bg_color, self.rect)
        self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x + 20, self.y + 15))
        display.blit(self.text_surface, self.text_rect)
        pg.display.update()


# Drawing the indicators on the screen.

indicator_x, indicator_y = 380, 475

for i in range(3):
    for letter in ALPHABET[i]:
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 51
    indicator_y += 55
    if i == 0:
        indicator_x = 400
    elif i == 1:
        indicator_x = 450


def check_guess(guess_to_check):
    # Goes through each letter and checks if it should be green, yellow, or grey.
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result
    game_decided = False
    for i in range(5):
        lowercase_letter = guess_to_check[i].text.lower()
        if lowercase_letter in CORRECT_WORD:
            if lowercase_letter == CORRECT_WORD[i]:
                guess_to_check[i].bg_color = GREEN
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = GREEN
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                if not game_decided:
                    game_result = "W"
            else:
                guess_to_check[i].bg_color = YELLOW
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = YELLOW
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_decided = True
        else:
            guess_to_check[i].bg_color = FILLED_OUTLINE
            for indicator in indicators:
                if indicator.text == lowercase_letter.upper():
                    indicator.bg_color = FILLED_OUTLINE
                    indicator.draw()
            guess_to_check[i].text_color = "white"
            game_result = ""
            game_decided = True
        guess_to_check[i].draw()
        pg.display.update()

    guesses_count += 1
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 470

    if guesses_count == 4 and game_result == "":
        game_result = "L"


def play_again():
    # Puts the play again text on the screen.
    global score
    global guesses_count
    score = (6 - int(guesses_count)) * 15

    # Puts the play again text on the screen.
    pg.draw.rect(display, cream, (342.5, 210, 590, 360))
    pg.draw.rect(display, FILLED_OUTLINE, (347.5, 215, 580, 350))
    play_again_font = pg.font.Font("FreeSansBold.otf", 40)
    if game_result == "L":
        play_again_text = play_again_font.render("You can do it next time!", True, "black")
        scoring_text = play_again_font.render("Score: 0", True, "black")
    if game_result == "W":
        play_again_text = play_again_font.render("Wow! You are so good at this!", True, "black")
        scoring_text = play_again_font.render("Score: " + str(score), True, "black")

    play_again_rect = play_again_text.get_rect(center=(WIDTH / 2, 350))
    scoring_rect = scoring_text.get_rect(center=((WIDTH/2), 250))
    word_was_text = play_again_font.render("The word was " + CORRECT_WORD + "!", True, "black")
    word_was_rect = word_was_text.get_rect(center=(WIDTH / 2, 400))
    display.blit(word_was_text, word_was_rect)
    display.blit(play_again_text, play_again_rect)
    display.blit(scoring_text, scoring_rect)
    # Scoring stuff here
    if event.type == pg.MOUSEBUTTONDOWN:
        button1.checkInput2(pg.mouse.get_pos())

    if event.type == pg.MOUSEBUTTONDOWN:
        button.checkInput1(pg.mouse.get_pos())

    button1.next_button(pg.mouse.get_pos())
    button.home_button(pg.mouse.get_pos())
    pg.display.update()


def reset():
    # Resets all global variables to their default states.
    global guesses_count, CORRECT_WORD, guesses, current_guess, current_guess_string, game_result

    guesses_count = 0
    CORRECT_WORD = random.choice()
    guesses = [[]] * 4
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pg.display.update()
    for indicator in indicators:
        indicator.bg_color = OUTLINE
        indicator.draw()


def create_new_letter():
    # Creates a new letter and adds it to the guess.
    global current_guess_string, current_letter_bg_x
    key_pressed = event.unicode.upper()
    current_guess_string += key_pressed
    new_letter = Letter(key_pressed, (current_letter_bg_x, guesses_count * 75 + LETTER_Y_SPACING))

    current_letter_bg_x += LETTER_X_SPACING
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for guess in guesses:
        for letter in guess:
            letter.draw()


def delete_letter():
    # Deletes the last letter from the guess.
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= LETTER_X_SPACING


while True:
    if game_result != "":
        print(CORRECT_WORD)
        play_again()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                print('works')
                if game_result != "":
                    reset()
                    scrambled_word()
                else:
                    if len(current_guess_string) == 5:
                        check_guess(current_guess)
            elif event.key == pg.K_BACKSPACE:
                if len(current_guess_string) > 0:
                    delete_letter()
            else:
                key_pressed = event.unicode.upper()
                if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                    if len(current_guess_string) < 5:
                        create_new_letter()
