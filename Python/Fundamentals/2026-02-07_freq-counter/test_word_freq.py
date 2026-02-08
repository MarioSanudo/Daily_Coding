from solution import word_freq, word_freq_2
import pytest

@pytest.mark.parametrize("texto, esperado",
                         [("Hi hi, bye!", {"hi": 2, "bye": 1}), (" A a, a. ", {"a": 3}),
                         ("one\ntwo\t two   ONE", {"one": 2, "two": 2}),("can't cant cant", {"can": 1, "t": 1, "cant": 2}),
                        (("... ,,, !!!", {}))])
def test_word_freq(texto, esperado):
   assert word_freq(texto) == esperado

