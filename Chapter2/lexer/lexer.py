from tokens import Token


class Lexer:
    """Lexical analysis on input."""
    def __init__(self, text: str):
        self.line: int = 1 # counts input lines
        self._peek: str = " " # holds the next input char
        self._words = {}
        self._text = text

        # reserve( new Word(Tag.TRUE, "true") );
        # reserve( new Word(Tag.FALSE, "false") );

    def reserve(self, t):
        self._words[t.lexeme] = t
    
    def scan(self) -> Token:
        # find a non-white-space character
        pos = 0
        for i, peek in enumerate(self._text):
            pos = i
            if peek == " " or peek == "\t":
                continue
            elif peek == "\n":
                line = line + 1
            else:
                self._peek = peek
        
        if self._peek.isdigit():
            v = 0
            while (self._peek.isdigit()):
                v = 10 * v + int(self._peek)
                pos = pos + 1
                peek = self._text
