import requests
from api_key import KEY
import sys

def get_word(w, type = '-s'):
    # handle error?

    url = f'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{w}?key={KEY}'
    response = requests.get(url).json()

    synonyms = response[0]['meta']['syns']
    antonyms = response[0]['meta']['ants']
    definitions = response[0]['def'][0]['sseq']

    print('Which definiton matches what you are looking for?')
    indexer = 0

    for definiton in definitions:
        print(indexer)
        print(f'Definition: {definiton[0][1]['dt'][0][1]}')
        print(f'Used in a sentence: {definiton[0][1]['dt'][1][1][0]['t']}')
        indexer += 1

    put = input('Make a selection: ')
    if type == '-a':
        return antonyms[int(put)]
    else: 
        return synonyms[int(put)]


def main():
    args = sys.argv
    if len(args) == 2:
        res = get_word(args[1])
    else:
        res = get_word(args[2], args[1])
    
    for word in res:
        print(word)


if __name__ == '__main__':
    main()
