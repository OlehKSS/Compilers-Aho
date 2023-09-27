from enum import Enum


class Tag(Enum):
    NUM = 256
    ID = 257
    TRUE = 258
    FALSE = 259


class Token:
    def __init__(self, t : int):
        self._tag = t
    
    @property
    def tag(self):
        return self._tag


class Num(Token):
    def __init__(self, v: int):
        super().__init__(Tag.NUM)
        self.value  = v


class Word(Token):
    def __init__(self, t: int, s: str):
        super().__init__(t)
        self.lexeme = s