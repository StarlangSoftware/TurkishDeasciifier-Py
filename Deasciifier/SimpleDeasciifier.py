from random import randrange

from Corpus.Sentence import Sentence
from Dictionary.Word import Word
from MorphologicalAnalysis.FsmMorphologicalAnalyzer import FsmMorphologicalAnalyzer

from Deasciifier.Deasciifier import Deasciifier


class SimpleDeasciifier(Deasciifier):

    fsm: FsmMorphologicalAnalyzer

    def __init__(self, fsm: FsmMorphologicalAnalyzer):
        """
        A constructor of SimpleDeasciifier class which takes a FsmMorphologicalAnalyzer as an input and
        initializes fsm variable with given FsmMorphologicalAnalyzer input.

        PARAMETERS
        ----------
        fsm : FsmMorphologicalAnalyzer
            FsmMorphologicalAnalyzer type input.
        """
        self.fsm = fsm

    def __generateCandidateList(self, candidates: list, word: str, index: int):
        """
        The generateCandidateList method takes a list candidates, a str, and an integer index as inputs.
        First, it creates a str which consists of corresponding Latin versions of special Turkish characters. If given
        index is less than the length of given word and if the item of word's at given index is one of the chars of str,
        it loops given candidates list's size times and substitutes Latin characters with their corresponding Turkish
        versions and put them to newly created str modified. At the end, it adds each modified item to the candidates
        list as a str and recursively calls generateCandidateList with next index.

        PARAMETERS
        ----------
        candidates : list
            list type input.
        word : str
            String input.
        index : int
            Integer input.
        """
        s = "ıiougcsİIOUGCS"
        if index < len(word):
            if s.index(word[index:index]) != -1:
                size = len(candidates)
                for i in range(size):
                    if word[index] == "ı":
                        newChar = "i"
                    elif word[index] == "i":
                        newChar = "ı"
                    elif word[index] == "o":
                        newChar = "ö"
                    elif word[index] == "u":
                        newChar = "ü"
                    elif word[index] == "g":
                        newChar = "ğ"
                    elif word[index] == "c":
                        newChar = "ç"
                    elif word[index] == "s":
                        newChar = "ş"
                    elif word[index] == "I":
                        newChar = "İ"
                    elif word[index] == "İ":
                        newChar = "I"
                    elif word[index] == "O":
                        newChar = "Ö"
                    elif word[index] == "U":
                        newChar = "Ü"
                    elif word[index] == "G":
                        newChar = "Ğ"
                    elif word[index] == "C":
                        newChar = "Ç"
                    elif word[index] == "S":
                        newChar = "Ş"
                    else:
                        newChar = word[index]
                    modified = candidates[i][0:index] + newChar + candidates[i][index + 1:]
                    candidates.append(modified)
            if len(candidates) < 10000:
                self.__generateCandidateList(candidates, word, index + 1)

    def candidateList(self, word: Word) -> list:
        """
        The candidateList method takes a Word as an input and creates new candidates list. First it
        adds given word to this list and calls generateCandidateList method with candidates, given word and
        index 0. Then, loops i times where i ranges from 0 to size of candidates list and calls
        morphologicalAnalysis method with ith item of candidates list. If it does not return any analysis for
        given item, it removes the item from candidates list.

        PARAMETERS
        ----------
        word : Word
            Word type input.

        RETURNS
        -------
        list
            List candidates.
        """
        candidates = [word.getName()]
        self.__generateCandidateList(candidates, word.getName(), 0)
        i = 0
        while i < len(candidates):
            fsmParseList = self.fsm.morphologicalAnalysis(candidates[i])
            if fsmParseList.size() == 0:
                candidates.pop(i)
                i = i - 1
            i = i + 1
        return candidates

    def deasciify(self, sentence: Sentence) -> Sentence:
        """
        The deasciify method takes a Sentence as an input and loops i times where i ranges from 0 to number of
        words in the given Sentence. First it gets ith word from given Sentence and calls candidateList with
        ith word and assigns the returned list to the newly created candidates list. And if the size of
        candidates list is greater than 0, it generates a random number and gets the item of candidates list
        at the index of random number and assigns it as a newWord. If the size of candidates list is 0, it then
        directly assigns ith word as the newWord. At the end, it adds newWord to the result Sentence.

        PARAMETERS
        ----------
        sentence : Sentence
            Sentence type input.

        RETURNS
        -------
        Sentence
            result Sentence.
        """
        result = Sentence()
        for i in range(sentence.wordCount()):
            word = sentence.getWord(i)
            fsmParseList = self.fsm.morphologicalAnalysis(word.getName())
            if fsmParseList.size() == 0:
                candidates = self.candidateList(word)
                if len(candidates) > 0:
                    randomCandidate = randrange(len(candidates))
                    newWord = Word(candidates[randomCandidate])
                else:
                    newWord = word
            else:
                newWord = word
            result.addWord(newWord)
        return result
