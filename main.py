converted_code = {
    'A': '.- ',
    'B': '-... ',
    'C': '-.-. ',
    'D': '-.. ',
    'E': '. ',
    'F': '..-. ',
    'G': '--. ',
    'H': '.... ',
    'I': '.. ',
    'J': '.---- ',
    'K': '-.- ',
    'L': '.-.. ',
    'M': '-- ',
    'N': '-. ',
    'O': '--- ',
    'P': '.--. ',
    'Q': '--.- ',
    'R': '.-. ',
    'S': '... ',
    'T': '- ',
    'U': '..- ',
    'V': '...- ',
    'W': '.-- ',
    'X': '-..- ',
    'Y': '-.-- ',
    'Z': '--.. ',
    '1': '.---- ',
    '2': '..--- ',
    '3': '...-- ',
    '4': '....-- ',
    '5': '..... ',
    '6': '-.... ',
    '7': '--... ',
    '8': '---.. ',
    '9': '----. ',
    '0': '---- ',
    ' ': '/ '
}


def text_to_morseCode(text):
    converted_text = ''
    for i in text:
        if converted_code.get(i) == None:
            return 'Special characters not allowed'
        converted_text += converted_code.get(i)
    return converted_text


print('MORSE CODE CONVERTER\n')
more_to_do = True
while more_to_do:
    text_entered = (input('Enter text : ')).upper()
    conversion = text_to_morseCode(text_entered)
    print(f"Text : {text_entered}\nMorse Code : {conversion}")
    more_to_do = bool(input('Press 0 to exit else anything to continue\n'))
