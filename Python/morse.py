import unicodedata

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}  # todos os caracteres disponíveis no obj morse_code

frase = input('Digite a frase a ser convertida: ')
frase_filter = unicodedata.normalize('NFD', frase)

convert_to_morse = []
for x in frase_filter:
    char = x.upper()
    if char in morse_code:
        convert_to_morse.append(morse_code[char])
    elif char == ' ':  # caso o caractere seja um espaço, ele adiciona uma barra no lugar para separar
        convert_to_morse.append('/')

print(' '.join(convert_to_morse))
