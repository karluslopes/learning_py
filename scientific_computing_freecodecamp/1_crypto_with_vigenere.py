text = 'This is the start of my programming journey!'
custom_key = 'password'

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            # Next, the exemple of the firist iteration of the loop
            offset = alphabet.index(key_char) #15 (p)
            index = alphabet.find(char) #19 (t)
            new_index = (index + offset*direction) % len(alphabet) #(15 + 19) % 26 = 8 (i)
            final_message += alphabet[new_index] #add 'i' to final_message
    
    return final_message #invokes the result of the function

def encrypt(message, key): #simplify the original funcion call
    return vigenere(message, key) 
    
def decrypt(message, key): #simplify the original funcion call too
    return vigenere(message, key, -1) #however, in the opposite direction

encryption = encrypt(text, custom_key)
print(f'Encrypted text: {encryption}')
password = input('\nPassword: ')
decryption = decrypt(encryption, password)
print(f'\nDecrypted text: {decryption.capitalize()}')