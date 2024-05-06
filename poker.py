from __future__ import annotations


def load_card_glyphs(path: str = 'cards.dat') -> dict[str, str]:
    '''Retorna un diccionario donde las claves serán los palos
    y los valores serán cadenas de texto con los glifos de las
    cartas sin ningún separador'''

    return {'♣' : "🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞",'◆' : "🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎",'❤' : "🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾",'♠' : "🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮" }


class Card:
    CLUBS = '♣'
    DIAMONDS = '◆'
    HEARTS = '❤'
    SPADES = '♠'
    #           1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13
    SYMBOLS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    A_VALUE = 1
    K_VALUE = 13
    GLYPHS = load_card_glyphs()

    def __init__(self, value: int | str, suit: str):
        '''Notas:
        - Si el suit(palo) no es válido hay que elevar una excepción de tipo
        InvalidCardError() con el mensaje: 🃏 Invalid card: {repr(suit)} is not a supported suit
        - Si el value(como entero) no es válido (es menor que 1 o mayor que 13) hay que
        elevar una excepción de tipo InvalidCardError() con el mensaje:
        🃏 Invalid card: {repr(value)} is not a supported value
        - Si el value(como string) no es válido hay que elevar una excepción de tipo
        🃏 Invalid card: {repr(value)} is not a supported symbol

        - self.suit deberá almacenar el palo de la carta '♣◆❤♠'.
        - self.value deberá almacenar el valor de la carta (1-13)'''
        self.value = value
        self.suit = suit

        if isinstance(self.value,str):
            if self.value != self.SYMBOLS:
                raise InvalidCardError(f'🃏 Invalid card: {repr(value)} is not a supported symbol')
        if self.value < 1 or self.value > 13:
            raise InvalidCardError(f'🃏 Invalid card: {repr(value)} is not a supported value')
        if self.suit != self.CLUBS and self.suit != self.DIAMONDS and self.suit != self.HEARTS and self.suit != self.SPADES:
            raise InvalidCardError(f'🃏 Invalid card: {repr(suit)} is not a supported suit')

    @property
    def cmp_value(self) -> int:
        '''Devuelve el valor (numérico) de la carta para comparar con otras.
        Tener en cuenta el AS.'''
        return self.value

    def __repr__(self):
        '''Devuelve el glifo de la carta'''
        return self.GLYPHS[self.suit][self.value - 1]

    def __eq__(self, other: Card | object):
        '''Indica si dos cartas son iguales'''
        return self.value == other.value and self.suit == other.suit

    def __lt__(self, other: Card):
        '''Indica si una carta vale menos que otra'''
        return self.value > other.value

    def __gt__(self, other: Card):
        '''Indica si una carta vale más que otra'''
        return self.value < other.value

    def __add__(self, other: Card) -> Card:
        '''Suma de dos cartas:
        1. El nuevo palo será el de la carta más alta.
        2. El nuevo valor será la suma de los valores de las cartas. Si valor pasa
        de 13 se convertirá en un AS.'''
           
        
        card = self.value + other.value
        if self.value == self.A_VALUE:
            card = self.A_VALUE
        elif card > self.K_VALUE:
            card = self.value
        elif card > other.K_VALUE:
            card = other.value
        elif (self.value or other.value) < self.K_VALUE or other.K_VALUE:
            card = self.value + other.value
        newpalo = ""
        if self.value > other.value:
            newpalo = self.suit 
        elif self.value < other.value:
            newpalo = other.suit 
        elif self.value == self.A_VALUE:
            newpalo = self.suit
        elif other.value == other.A_VALUE:
            newpalo = other.suit    
        
        return Card(card,newpalo)

    def is_ace(self) -> bool:
        '''Indica si una carta es un AS'''
        if self.value == self.A_VALUE:
            return False

    @classmethod
    def get_available_suits(cls) -> str:
        '''Devuelve todos los palos como una cadena de texto'''
        return cls.CLUBS + cls.DIAMONDS + cls.HEARTS + cls.SPADES

    @classmethod
    def get_cards_by_suit(cls, suit: str):
        '''Función generadora que devuelve los glifos de las cartas por su palo'''

        return cls.GLYPHS[suit]


class InvalidCardError(Exception):
    '''Clase que representa un error de carta inválida.
    - El mensaje por defecto de esta excepción debe ser: 🃏 Invalid card
    - Si se añaden otros mensajes aparecerán como: 🃏 Invalid card: El mensaje que sea'''

