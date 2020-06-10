import unittest

from Corpus.Sentence import Sentence
from Dictionary.Word import Word

from Deasciifier.SimpleAsciifier import SimpleAsciifier


class SimpleAsciifierTest(unittest.TestCase):

    simpleAsciifier: SimpleAsciifier

    def setUp(self) -> None:
        self.simpleAsciifier = SimpleAsciifier()

    def test_WordAsciify(self):
        self.assertEqual("cogusiCOGUSI", self.simpleAsciifier.asciifyWord(Word("çöğüşıÇÖĞÜŞİ")))
        self.assertEqual("sogus", self.simpleAsciifier.asciifyWord(Word("söğüş")))
        self.assertEqual("uckagitcilik", self.simpleAsciifier.asciifyWord(Word("üçkağıtçılık")))
        self.assertEqual("akiskanlistiricilik", self.simpleAsciifier.asciifyWord(Word("akışkanlıştırıcılık")))
        self.assertEqual("citcitcilik", self.simpleAsciifier.asciifyWord(Word("çıtçıtçılık")))
        self.assertEqual("duskirikligi", self.simpleAsciifier.asciifyWord(Word("düşkırıklığı")))
        self.assertEqual("yuzgorumlugu", self.simpleAsciifier.asciifyWord(Word("yüzgörümlüğü")))

    def test_SentenceAsciify(self):
        self.assertEqual(Sentence("cogus iii COGUSI").toString(), self.simpleAsciifier.asciify(Sentence("çöğüş ııı ÇÖĞÜŞİ")).toString())
        self.assertEqual(Sentence("uckagitcilik akiskanlistiricilik").toString(), self.simpleAsciifier.asciify(Sentence("üçkağıtçılık akışkanlıştırıcılık")).toString())
        self.assertEqual(Sentence("citcitcilik duskirikligi yuzgorumlugu").toString(), self.simpleAsciifier.asciify(Sentence("çıtçıtçılık düşkırıklığı yüzgörümlüğü")).toString())


if __name__ == '__main__':
    unittest.main()
