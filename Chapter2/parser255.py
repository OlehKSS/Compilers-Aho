class Parser:
    def __init__(self, input_str: str) -> None:
        self._input_str: str = input_str
        self._output_chars: list = []
        self._curr_pos: int = 0
        self._lookahead: str = input_str[self._curr_pos]

    def expr(self):
        self.term()
        while True:
            if self._lookahead == '+':
                self.match('+')
                self.term()
                self.print('+')
            elif self._lookahead == '-':
                self.match('-')
                self.term()
                self.print('-')
            else:
                return "".join(self._output_chars)
    
    def term(self):
        if self._lookahead.isdigit():
            self.print(self._lookahead)
            self.match(self._lookahead)
        else:
            raise ValueError("Syntax error.")
    
    def match(self, t: str):
        if self._lookahead == t:
            self._curr_pos = self._curr_pos + 1

            if self._curr_pos  < len(self._input_str):
                self._lookahead = self._input_str[self._curr_pos]
        else:
            raise ValueError("Syntax error.")
    
    def print(self, t: str):
        self._output_chars.append(t)


if __name__ == "__main__":
    print("Translate infix expressions into postfix form:")
    input_str = input()
    p = Parser(input_str)
    print(p.expr())
        