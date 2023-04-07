from words_Data import words_List
from random import choice
from string import ascii_uppercase
import click

def valid_Word_selection():
    return (choice(words_List)).upper()

def hangman_Logic():
    word = valid_Word_selection()
    # print(word)
    word_Alphabets = (set(word)) # set of all alphabets of the word to be guessed
    alphabets = set(ascii_uppercase)  # All the alphabets are stored here
    used_Alphabets = set()
    
    while len(word_Alphabets) != 0:
        print()
        user_Alphabet = ""
        print("Word to Guessed :- ", end=" ")
        word_list = [user_Alphabet if user_Alphabet in used_Alphabets else "_ " for user_Alphabet in word]
        print(" ".join(word_list))
        print("Alphabets Used:- "," ".join(used_Alphabets))


        # Taking the input
        user_Alphabet = (input("Enter the Alphabet to be Guessed:- ")).upper() # user put anything, It will consider the first alphabet only

        if user_Alphabet in used_Alphabets:
            click.secho("Guess Again!!! This Alphabet is already being Used", bold=True, fg="red")

        elif user_Alphabet not in alphabets:
            click.secho("Guess Again!!! This Input is not an Alphabet", bold=True, fg="red")

        else: #This is a Valid input case
            used_Alphabets.add(user_Alphabet)
            if user_Alphabet in word_Alphabets:
                word_Alphabets.remove(user_Alphabet)
    
    click.secho("\nHurray!!!! You gussed the correct Word", bold=True, fg="green")
    print(word)
