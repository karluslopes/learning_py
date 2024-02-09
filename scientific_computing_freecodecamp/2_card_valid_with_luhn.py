def verify_card_number(card_number): #Card-number validation function by Luhn Algorithm
    card_number_reversed = card_number[::-1] #Reversing the card-number, because the number is processed backwards

    odd_digits = card_number_reversed[::2] #Separating the odd digtis
    sum_of_odd_digits = 0
    for digit in odd_digits:
        sum_of_odd_digits += int(digit) #Obtaining the sum of the odd digits

    even_digits = card_number_reversed[1::2] #Separating the even digits
    sum_of_even_digits = 0
    for digit in even_digits:
        number = int(digit) * 2 #The even digits must be doubled
        if number >= 10:
            number = (number // 10) + (number % 10) #numbers greater than 9 must be added together to convert them into a single digit
        sum_of_even_digits += number #Obtaining the sum of the even digits

    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0 #As a rule, the total sum must be divisible by 10 to return True

def main(): #Main function to be used by the user
    card_number = input('Digite o número do cartão: ') #Ex.: 4111-1111-4555-1142
    card_translation = str.maketrans({'-': '', ' ': ''}) #Defining the translation method
    translated_card_number = card_number.translate(card_translation) #Applying the translation method to the variable

    if verify_card_number(translated_card_number):
        print('\nValid!')
    else:
        print('\nInvalid!')

main()
