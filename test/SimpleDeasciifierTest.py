import unittest

from Corpus.Sentence import Sentence
from Dictionary.Word import Word
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer

from Deasciifier.SimpleAsciifier import SimpleAsciifier
from Deasciifier.SimpleDeasciifier import SimpleDeasciifier


class SimpleDeasciifierTest(unittest.TestCase):

    def test_Deasciify(self):
        fsm = FsmMorphologicalAnalyzer()
        simpleDeasciifier = SimpleDeasciifier(fsm)
        simpleAsciifier = SimpleAsciifier()
        for i in range(fsm.getDictionary().size()):
            word = fsm.getDictionary().getWordWithIndex(i)
            count = 0
            for j in range(len(word.getName())):
                if word.getName()[j] == 'ç' or word.getName()[j] == 'ö' or word.getName()[j] == 'ğ' or \
                        word.getName()[j] == 'ü' or word.getName()[j] == 'ş' or word.getName()[j] == 'ı':
                    count = count + 1
            if (count > 0 and not word.getName().endswith("fulü") and (word.isNominal() or word.isAdjective() or
                                                                       word.isAdverb() or word.isVerb())):
                asciified = simpleAsciifier.asciifyWord(word)
                if len(simpleDeasciifier.candidateList(Word(asciified))) == 1:
                    deasciified = simpleDeasciifier.deasciify(Sentence(asciified)).toString()
                    self.assertEqual(word.getName(), deasciified)

    def test_Deasciify2(self):
        fsm = FsmMorphologicalAnalyzer()
        simpleDeasciifier = SimpleDeasciifier(fsm)
        self.assertEqual(simpleDeasciifier.deasciify(Sentence("hakkinda")).toString(), "hakkında")
        self.assertEqual(simpleDeasciifier.deasciify(Sentence("kucuk")).toString(), "küçük")
        self.assertEqual(simpleDeasciifier.deasciify(Sentence("karsilikli")).toString(), "karşılıklı")


if __name__ == '__main__':
    unittest.main()
