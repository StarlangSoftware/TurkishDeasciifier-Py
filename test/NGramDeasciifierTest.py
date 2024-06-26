import unittest

from Corpus.Corpus import Corpus
from Corpus.Sentence import Sentence
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from NGram.NGram import NGram
from NGram.NoSmoothing import NoSmoothing

from Deasciifier.NGramDeasciifier import NGramDeasciifier
from Deasciifier.SimpleAsciifier import SimpleAsciifier


class NGramDeasciifierTest(unittest.TestCase):

    def test_Deasciify(self):
        fsm = FsmMorphologicalAnalyzer("../turkish_dictionary.txt", "../turkish_misspellings.txt",
                                       "../turkish_finite_state_machine.xml")
        nGram = NGram("../ngram.txt")
        nGram.calculateNGramProbabilitiesSimple(NoSmoothing())
        nGramDeasciifier = NGramDeasciifier(fsm, nGram, True)
        simpleAsciifier = SimpleAsciifier()
        corpus = Corpus("../corpus.txt")
        for i in range(corpus.sentenceCount()):
            sentence = corpus.getSentence(i)
            for j in range(1, sentence.wordCount()):
                if fsm.morphologicalAnalysis(sentence.getWord(j).getName()).size() > 0:
                    asciified = simpleAsciifier.asciifyWord(sentence.getWord(j))
                    if asciified != sentence.getWord(j).getName():
                        deasciified = nGramDeasciifier.deasciify(Sentence(sentence.getWord(j - 1).getName() + " " + sentence.getWord(j).getName()))
                        self.assertEqual(sentence.getWord(j).getName(), deasciified.getWord(1).getName())

    def test_Deasciify2(self):
        fsm = FsmMorphologicalAnalyzer("../turkish_dictionary.txt", "../turkish_misspellings.txt",
                                       "../turkish_finite_state_machine.xml")
        nGram = NGram("../ngram.txt")
        nGram.calculateNGramProbabilitiesSimple(NoSmoothing())
        nGramDeasciifier = NGramDeasciifier(fsm, nGram, False)
        self.assertEqual("noter hakkında", nGramDeasciifier.deasciify(Sentence("noter hakkinda")).__str__())
        self.assertEqual("sandık medrese", nGramDeasciifier.deasciify(Sentence("sandik medrese")).__str__())
        self.assertEqual("kuran'ı karşılıklı", nGramDeasciifier.deasciify(Sentence("kuran'ı karsilikli")).__str__())


if __name__ == '__main__':
    unittest.main()
