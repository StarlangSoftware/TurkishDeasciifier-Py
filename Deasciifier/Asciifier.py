from abc import abstractmethod

from Corpus.Sentence import Sentence


class Asciifier:

    @abstractmethod
    def asciify(self, sentence: Sentence) -> Sentence:
        """
        The asciify method which takes a Sentence as an input and also returns a Sentence as the output.

        PARAMETERS
        ----------
        sentence : Sentence
            Sentence type input.

        RETURNS
        -------
        Sentence
            Sentence result.
        """
        pass
