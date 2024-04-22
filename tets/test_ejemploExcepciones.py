import pytest

from ejemploExcepciones import EjemploExcepciones

def test_ZeroDivisionError():
    ejemplo = EjemploExcepciones()
    with pytest.raises(ZeroDivisionError):
        ejemplo.zeroDivisionError(num = 2, den = 0)

    assert ejemplo.zeroDivisionError(num = 4, den = 2) == 2

#ValueError
def test_valueError():
    ejemplo = EjemploExcepciones()
    with pytest.raises(ValueError):
        ejemplo.valueError()

#FileNotFoundError
def test_fileNotFoundError():
    ejemplo = EjemploExcepciones()
    with pytest.raises(FileNotFoundError):
        ejemplo.fileNotFoundError()

#TypeError
def test_typeError():
    ejemplo = EjemploExcepciones()
    with pytest.raises(TypeError):
        ejemplo.typeError()

#PermissionError
def test_permissionError():
    ejemplo = EjemploExcepciones()
    with pytest.raises(PermissionError):
        ejemplo.permissionError()

#IndexError
def test_indexError():
    ejemplo = EjemploExcepciones()
    with pytest.raises(IndexError):
        ejemplo.indexError()

#KeyboardInterrupt
def test_keyboardInterrupt():
    ejemplo = EjemploExcepciones()
    with pytest.raises(KeyboardInterrupt):
        ejemplo.keyboardInterrupt()

#UnicodeDecodeError
def test_unicodeDecodeError():
    ejemplo = EjemploExcepciones()
    with pytest.raises(UnicodeDecodeError):
        ejemplo.unicodeDecodeError()

#AttributeError
def test_attributeError():
    ejemplo = EjemploExcepciones()
    with pytest.raises(AttributeError):
        ejemplo.attributeError()