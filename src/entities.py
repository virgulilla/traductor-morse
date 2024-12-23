class Morse:
    def __init__(self):
        self.dictionary = {
            'A': '.–', 'B': '–...', 'C': '–.–.', 'D': '–..', 'E': '.',
            'F': '..–.', 'G': '––.', 'H': '....', 'I': '..', 'J': '.–––',
            'K': '–.–', 'L': '.–..', 'M': '––', 'Ñ': '--.--', 'N': '–.', 'O': '–––',
            'P': '.––.', 'Q': '––.–', 'R': '.–.', 'S': '...', 'T': '–',
            'U': '..–', 'V': '...–', 'W': '.––', 'X': '–..–', 'Y': '–.––',
            'Z': '––..', '1': '.––––', '2': '..–––', '3': '...––', '4': '....–',
            '5': '.....', '6': '–....', '7': '––...', '8': '–––..', '9': '––––.',
            '0': '–––––', ' ': ' '
        }

    def text_to_morse(self, text: str) -> str:
        return ' '.join([self.dictionary[char.upper()] for char in text])
    
    def morse_to_text(self, morse: str) -> str:
        return ''.join([key for key, value in self.dictionary.items() if value == morse])