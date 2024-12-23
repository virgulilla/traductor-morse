class Morse:
    def __init__(self):
        self.dictionary = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'Ñ': '--.--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
            '0': '-----', ' ': ' '
        }

    def text_to_morse(self, text: str) -> str:
        morse_code = []
        for char in text:
            if char == ' ':
                morse_code.append('')
            else:
                morse_code.append(self.dictionary[char.upper()])
        return ' '.join(morse_code)
    
    def morse_to_text(self, morse: str) -> str:
        morse_words = morse.split("  ") # 2 espacios para separar palabras
        decoded_text = []

        for word in morse_words:
            letters = word.split(" ") # 1 espacio para separar letras
            decoded_word = ''.join(
                next((key for key, value in self.dictionary.items() if value == letter), '')
                for letter in letters
            )
            decoded_text.append(decoded_word)

        return ' '.join(decoded_text)