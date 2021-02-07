import difflib
from typing import Union
import sqlite3

conn = sqlite3.connect('Database.db')
cursor = conn.cursor()

all_words = cursor.execute('SELECT word FROM definitions').fetchall()
all_words = list(zip(*all_words))[0]


def search_db(key: str) -> list:
    """Queries the database for the key

    :argument:
        key (str): The word to search for

    :rtype:
        list: A list of all the definitions for the word
    """
    query = cursor.execute(f'''SELECT definition 
                                 FROM definitions
                                WHERE word = '{key}';''')
    return cursor.fetchall()


def get_definition(key: str) -> Union[list, str]:
    """Returns the definition of the key if it exists in the dictionary

    :argument:
        key (str): The word that is to be defined

    :rtype:
        Union[list, str]: The definition/s of the key
    """

    possible_words = difflib.get_close_matches(key, all_words, n=5, cutoff=0.8)

    if key.lower() in all_words:
        return search_db(key.lower())
    elif key.title() in all_words:
        return search_db(key.title())
    elif key.upper() in all_words:
        return search_db(key.upper())
    elif len(possible_words) > 0:
        print("Word doesn't exist. Did you mean any of the words below?")
        print(possible_words, '\n')
        new_key = input('Enter the new word or -1 to EXIT: ')

        if new_key != '-1':
            return get_definition(new_key)
        else:
            exit()
    else:
        return "The word doesn't exist. Please double check it."


word = input('Enter a word: ')
word_definition = get_definition(word)

if isinstance(word_definition, list):
    for number, definition in enumerate(word_definition, start=1):
        print(number, ': ', definition[0])
else:
    print(word_definition)
