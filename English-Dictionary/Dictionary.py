import json
import difflib
from typing import Union

data = json.load(open('data.json'))


def get_definition(key: str) -> Union[list, str]:
    """Returns the definition of the key if it exists in the dictionary

    :argument:
        key (str): The word that is to be defined

    :rtype: Union[list, str
        The definition/s of the key
    """
    possible_words = difflib.get_close_matches(key, data.keys(), n=5, cutoff=0.8)

    if key.lower() in data:
        return data[key.lower()]
    elif key.title() in data:
        return data[key.title()]
    elif key.upper() in data:
        return data[key.upper()]
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
        print(number, ': ', definition)
else:
    print(word_definition)
