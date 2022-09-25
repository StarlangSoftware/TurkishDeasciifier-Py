from Corpus.Sentence import Sentence
from Dictionary.Word import Word

from Deasciifier.Asciifier import Asciifier


class SimpleAsciifier(Asciifier):

    def asciifyWord(self, word: Word) -> str:
        """
        The asciifyWord method takes a Word as an input. Then,
        loops i times where i ranges from 0 to length of the word and substitutes Turkish
        characters with their corresponding Latin versions and returns it as a new str.

        PARAMETERS
        ----------
        word : Word
            Word type input to asciify.

        RETURNS
        -------
        str
            String output which is asciified.
        """
        modified = ""
        for i in range(len(word.getName())):
            if word.getName()[i] == "ç":
                modified = modified + 'c'
            elif word.getName()[i] == "ö":
                modified = modified + 'o'
            elif word.getName()[i] == "ğ":
                modified = modified + 'g'
            elif word.getName()[i] == "ü":
                modified = modified + 'u'
            elif word.getName()[i] == "ş":
                modified = modified + 's'
            elif word.getName()[i] == "ı":
                modified = modified + 'i'
            elif word.getName()[i] == "Ç":
                modified = modified + 'C'
            elif word.getName()[i] == "Ö":
                modified = modified + 'O'
            elif word.getName()[i] == "Ğ":
                modified = modified + 'G'
            elif word.getName()[i] == "Ü":
                modified = modified + 'U'
            elif word.getName()[i] == "Ş":
                modified = modified + 'S'
            elif word.getName()[i] == "İ":
                modified = modified + 'I'
            else:
                modified = modified + word.getName()[i]
        return modified

    def asciify(self, sentence: Sentence) -> Sentence:
        """
        Another asciify method which takes a Sentence as an input. It loops i times where i ranges form 0 to
        number of words in the given sentence. First it gets each word and calls asciify with current word and creates
        Word with returned String. At the and, adds each newly created ascified words to the result Sentence.

        PARAMETERS
        ----------
        sentence : Sentence
            Sentence type input.

        RETURNS
        -------
        Sentence
            Sentence output which is asciified.
        """
        result = Sentence()
        for i in range(sentence.wordCount()):
            word = sentence.getWord(i)
            new_word = Word(self.asciifyWord(word))
            result.addWord(new_word)
        return result
