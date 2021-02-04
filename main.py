# Compile dictionary matching English Alphabet to Morse Alphabet

letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0'.split()
morses = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- ' \
         '.-- -..- -.-- --.. .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----'.split()

to_morse = dict(zip(letters, morses))
from_morse = {v: k for k, v in to_morse.items()}

# Write function to change English into Morse


def morsify():
    string = input('What would you like to morsify?\n')
    new_string = []
    for word in string.lower().split():
        word = ' '.join([to_morse[letter] for letter in word if letter in letters])
        new_string.append(word)
    print(' / '.join(new_string))
    cont()


# Write function to convert morse to english

def demorsify():
    morse = input('What would you like to de-morsify?\n'
                  '(Seperate letters with a space and words with a slash, '
                  'ex: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."\n')
    new_string = ''
    for letter in morse.split():
        if letter == '/':
            letter = ' '
            new_string += letter
        else:
            letter = from_morse[letter]
            new_string += letter
    print(new_string)
    cont()


# Write overarching function as interface


def translator():
    choice = input('Would you like to:\n1) Convert text into morse code\n'
                   '2) Convert morse code into readable text\n(Type 1 or 2)\n')
    if choice == '1':
        morsify()
    elif choice == '2':
        demorsify()
    else:
        print('Please type 1 or 2.')
        translator()


def cont():
    choice = input('Would you like to translate something else? (y/n)\n')
    if choice == 'y':
        translator()
    elif choice == 'n':
        print('Thanks for using the Morse Translator! .... .- ...- . / .- / --. --- --- -.. / -.. .- -.--')
        pass
    else:
        print('Please type y or n')
        cont()


if __name__ == '__main__':
    translator()
