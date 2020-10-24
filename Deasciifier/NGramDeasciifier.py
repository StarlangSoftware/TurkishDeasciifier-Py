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

    def checkAnalysisAndSetRoot(self, sentence: Sentence, index: int) -> Word:
        """
        Checks the morphological analysis of the given word in the given index. If there is no misspelling, it returns
        the longest root word of the possible analyses.
        @param sentence Sentence to be analyzed.
        @param index Index of the word
        @return If the word is misspelled, null; otherwise the longest root word of the possible analyses.
        """
        if index < sentence.wordCount():
            fsmParses = self.fsm.morphologicalAnalysis(sentence.getWord(index).getName())
            if fsmParses.size() != 0:
                return fsmParses.getParseWithLongestRootWord().getWord()
        return None

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
        root = self.checkAnalysisAndSetRoot(sentence, 0)
        nextRoot = self.checkAnalysisAndSetRoot(sentence, 1)
        for i in range(sentence.wordCount()):
            word = sentence.getWord(i)
            if root is None:
                candidates = self.candidateList(word)
                bestCandidate = word.getName()
                bestRoot = word
                bestProbability = 0
                for candidate in candidates:
                    fsmParses = self.fsm.morphologicalAnalysis(candidate)
                    root = fsmParses.getParseWithLongestRootWord().getWord()
                    if previousRoot is not None:
                        previousProbability = self.__nGram.getProbability(previousRoot.getName(), root.getName())
                    else:
                        previousProbability = 0.0
                    if nextRoot is not None:
                        nextProbability = self.__nGram.getProbability(root.getName(), nextRoot.getName())
                    else:
                        nextProbability = 0.0
                    if max(previousProbability, nextProbability) > bestProbability:
                        bestCandidate = candidate
                        bestRoot = root
                        bestProbability = max(previousProbability, nextProbability)
                root = bestRoot
                result.addWord(Word(bestCandidate))
            else:
                result.addWord(word)
            previousRoot = root
            root = nextRoot
            nextRoot = self.checkAnalysisAndSetRoot(sentence, i + 2)
        return result
