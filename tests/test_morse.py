from src.entities import Morse
import pytest

def test_to_morse():
    morse = Morse()
    assert morse.text_to_morse("A") == ".-"

def test_to_text():
    morse = Morse()
    assert morse.morse_to_text(".-") == "A"

def test_to_text_con_espacios():
    morse = Morse()
    assert morse.morse_to_text(". ... - ---  . ...  ..- -.  - .-. .- -.. ..- -.-. - --- .-.  -.. .  -.-. --- -.. .. --. ---  -- --- .-. ... .") == "ESTO ES UN TRADUCTOR DE CODIGO MORSE"