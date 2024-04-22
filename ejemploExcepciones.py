class EjemploExcepciones:
    #ZeroDivisionError
    def zeroDivisionError(self, *, num:int, den:int)->int:
        if (den == 0):
            raise ZeroDivisionError
        
        return num // den

    #ValueError
    def valueError(self):
        raise ValueError
    #FileNotFoundError
    def fileNotFoundError(self):
        raise FileNotFoundError

    #TypeError
    def typeError(self):
        raise TypeError

    #PermissionError
    def permissionError(self):
        raise PermissionError

    #IndexError
    def indexError(self):
        raise IndexError

    #KeyboardInterrupt
    def keyboardInterrupt(self):
        raise KeyboardInterrupt

    #UnicodeDecodeError
    def unicodeDecodeError(self):
        raise UnicodeDecodeError

    #AttributeError
    def attributeError(self):
        raise AttributeError