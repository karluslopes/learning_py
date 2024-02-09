# Develop a program that counts the number of words in a user-provided sentence

def count_words(pharse):

    for char in pharse:
        if not char.isalnum() and char != " ":
            print(char)
            pharse = pharse.replace(char, "")

    words = pharse.split()

    if len(words) == 0:
        print('Nenhuma palavra foi digitada.')
    elif len(words) == 1:
        print('A frase contém apenas uma palavra.')
    elif len(words) > 1:
        print(f'A frase contém {len(words)} palavras.')

if __name__ == '__main__':
    count_words(input('Digite uma frase!\n')) #Ex.: "1) two, three, FOUR-WORDS @@@" 

