MORSE_CODE = {'A': '.-', 'B': '-...', 'C': '−·−·', 'D': '−··', 'E': '·', 'F': '··−·',
              'G': '−−·', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..', '.': '.-.-.-',
              '?': '..--..', '.': '·−·−·−'}

SPACE_MORSE = {' ': '.......'}


def change_to_morse():
    #一文字ずつ、空白あける
    user_input = input("Enter a string: ").upper()
    user_input = ' '.join(user_input)
    morse_code = user_input.translate(str.maketrans(MORSE_CODE))
    moser_code_space = morse_code.translate(str.maketrans(SPACE_MORSE))
    return morse_code

print(change_to_morse())


