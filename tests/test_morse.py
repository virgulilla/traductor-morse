from src.entities import Morse
import pytest

def test_to_morse():
    morse = Morse()
    assert morse.text_to_morse("A") == ".–"

def test_to_text():
    morse = Morse()
    assert morse.morse_to_text(".–") == "A"