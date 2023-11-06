morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}


def convert():
    play = True
    while play == True:
        word_to_decipher = input("What string would you like to convert to Morse code?\n").upper()
        print(f"{word_to_decipher} is: ")

        string_split = list(word_to_decipher)

        morse_output = []
        for letter in string_split:
            if letter == " ":
                morse_output.append(letter)
            else:
                morse_output.append(morse_dict[letter])

        morse_string = '   '.join(morse_output)
        print(morse_string)

        more = input("Would you like to convert another string? Yes or No ('No' will exit)\n").upper()
        if more == "NO":
            play = False


convert()
