import os
import logging

def main():
    while True:
        question_2 = input('\nPlease enter a directory path in which you would like to save the log file: ')
        if os.path.isdir('{}'.format(question_2)):
            os.chdir(question_2)
            question_1 = input('\nWhat would you like to name the file? ')
            logging.basicConfig(filename='{}.txt'.format(question_1), level=logging.INFO)
            print('\nThis directory is valid...\nThe file "{}" has been created.'.format(question_1))
            question_3 = input('\nWhat is your name? ')
            question_4 = input('What is your address? ')
            question_5 = input('Whats is your phone number? ')
            logging.info(question_3 + ', ' + question_4 + ', ' + question_5)
            print('\n'+ question_3 + ", " + question_4 + ", " + question_5)
        else:
            print("\nDirectory does not exist.")
            main()

main()