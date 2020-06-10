from Corpus.Sentence import Sentence
from Dictionary.Word import Word
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer
from NGram.NGram import NGram

from Deasciifier.SimpleDeasciifier import SimpleDeasciifier


class NGramDeasciifier(SimpleDeasciifier):

    __nGram: NGram

    def __init__(self, fsm: FsmMorphologicalAnalyzer, nGram: NGram):
        """
        A constructor of NGramDeasciifier class which takes an FsmMorphologicalAnalyzer and an NGram
        as inputs. It first calls it super class SimpleDeasciifier with given FsmMorphologicalAnalyzer input
        then initializes nGram variable with given NGram input.

        PARAMETERS
        ----------
        fsm : FsmMorphologicalAnalyzer
            FsmMorphologicalAnalyzer type input.
        nGram : NGram
            NGram type input.
        """
        super().__init__(fsm)
        self.__nGram = nGram

    def deasciify(self, sentence: Sentence) -> Sentence:
        """
        The deasciify method takes a Sentence as an input. First it creates a String list as candidates,
        and a Sentence result. Then, loops i times where i ranges from 0 to words size of given sentence. It gets the
        current word and generates a candidateList with this current word then, it loops through the candidateList.
        First it calls morphologicalAnalysis method with current candidate and gets the first item as root word. If it
        is the first root, it gets its N-gram probability, if there are also other roots, it gets probability of these
        roots and finds out the best candidate, best root and the best probability. At the nd, it adds the bestCandidate
        to the bestCandidate list.

        PARAMETERS
        ----------
        sentence : Sentence
            Sentence type input.

        RETURNS
        -------
        Sentence
            Sentence result as output.
        """
        previousRoot = None
        result = Sentence()
        for i in range(sentence.wordCount()):
            word = sentence.getWord(i)
            fsmParses = self.fsm.morphologicalAnalysis(word.getName())
            if fsmParses.size() == 0:
                candidates = self.candidateList(word)
                bestCandidate = word.getName()
                bestRoot = word
                bestProbability = 0
                for candidate in candidates:
                    fsmParseList = self.fsm.morphologicalAnalysis(candidate)
                    root = fsmParseList.getFsmParse(0).getWord()
                    if previousRoot is not None:
                        probability = self.__nGram.getProbability(previousRoot.getName(), root.getName())
                    else:
                        probability = self.__nGram.getProbability(root.getName())
                    if probability > bestProbability:
                        bestCandidate = candidate
                        bestRoot = root
                        bestProbability = probability
                previousRoot = bestRoot
                result.addWord(Word(bestCandidate))
            else:
                result.addWord(word)
                previousRoot = fsmParses.getParseWithLongestRootWord().getWord()
        return result
