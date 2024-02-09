# CREATE A FUNCTION THAT TAKES A STRING AS INPUT AND CHECKS IF IT IS A PALINDROME (A WORD, PHRASE, OR SEQUENCE THAT READS THE SAME BACKWARD AS FORWARD)

import unicodedata

def process_text(text):
    processing = unicodedata.normalize("NFD", text) #Using the function from the module in Python. The function converts a string to one of the Unicode normalization forms.
    processing = processing.encode("ascii", "ignore") #Encoding the normalized Unicode string into ASCII format. The argument tells Python to ignore errors and drop any characters that are not representable in ASCII
    processing = processing.decode("utf-8") #Decoding the ASCII encoded bytes back into a string using UTF-8 encoding
    processed_text = processing

    for char in processed_text:
        if not char.isalpha():
            processed_text = processed_text.replace(char, "") #Remove characters not aplhabetics
    return processed_text.upper()

def is_palindrome():
    text = process_text(input('Digite uma palavra, frase ou sequência qualquer de caracteres:\n\n>> '))

    if text == text[-1::-1]: #Compares whith its own inverse
        print('A sequência de caracteres inserida forma um palíndromo!')
    else:
        print('A sequência de caracteres inserida não forma um palíndromo. Tente outra sequência cuja qual seu inverso seja um espelho! Ex.: Arara\n')
        print(f'Sequência original  > {text}')
        print(f'Sequência invertida > {text[-1::-1]}')

if __name__ == '__main__':
    is_palindrome()
