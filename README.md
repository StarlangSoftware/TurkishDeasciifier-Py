Turkish Deasciifier
============

This tool is used to turn Turkish text written in ASCII characters, which do not include some letters of the Turkish alphabet, into correctly written text with the appropriate Turkish characters (such as ı, ş, and so forth). It can also do the opposite, turning Turkish input into ASCII text, for the purpose of processing.

Video Lectures
============

[<img src="https://github.com/StarlangSoftware/TurkishDeasciifier/blob/master/video.jpg" width="50%">](https://youtu.be/b18-k8SKQ6U)

For Developers
============

You can also see [Cython](https://github.com/starlangsoftware/TurkishDeasciifier-Cy), [Java](https://github.com/starlangsoftware/TurkishDeasciifier), [C++](https://github.com/starlangsoftware/TurkishDeasciifier-CPP), [Swift](https://github.com/starlangsoftware/TurkishDeasciifier-Swift), [Js](https://github.com/starlangsoftware/TurkishDeasciifier-Js), or [C#](https://github.com/starlangsoftware/TurkishDeasciifier-CS) repository.

## Requirements

* [Python 3.7 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Pip Install

	pip3 install NlpToolkit-Deasciifier

## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called Deasciifier will be created. Or you can use below link for exploring the code:

	git clone https://github.com/starlangsoftware/TurkishDeasciifier-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `TurkishDeasciifier-PY` file
* Select open as project option
* Couple of seconds, dependencies will be downloaded. 

Detailed Description
============

+ [Asciifier](#using-asciifier)
+ [Deasciifier](#using-deasciifier)

## Using Asciifier

Asciifier converts text to a format containing only ASCII letters. This can be instantiated and used as follows:

      asciifier = SimpleAsciifier()
      sentence = Sentence("çocuk")
      asciified = asciifier.asciify(sentence)
      print(asciified)

Output:
    
    cocuk      

## Using Deasciifier

Deasciifier converts text written with only ASCII letters to its correct form using corresponding letters in Turkish alphabet. There are two types of `Deasciifier`:


* `SimpleDeasciifier`

    The instantiation can be done as follows:  
    
        fsm = FsmMorphologicalAnalyzer()
        deasciifier = SimpleDeasciifier(fsm)
     
* `NGramDeasciifier`
    
    * To create an instance of this, both a `FsmMorphologicalAnalyzer` and a `NGram` is required. 
    
    * `FsmMorphologicalAnalyzer` can be instantiated as follows:
        
            fsm = FsmMorphologicalAnalyzer()
    
    * `NGram` can be either trained from scratch or loaded from an existing model.
        
        * Training from scratch:
                
                corpus = Corpus("corpus.txt")
                ngram = NGram(corpus.getAllWordsAsArrayList(), 1)
                ngram.calculateNGramProbabilities(LaplaceSmoothing())
                
        *There are many smoothing methods available. For other smoothing methods, check [here](https://github.com/olcaytaner/NGram).*       
        * Loading from an existing model:
     
                    ngram = NGram("ngram.txt")

	*For further details, please check [here](https://github.com/starlangsoftware/NGram).*        
            
    * Afterwards, `NGramDeasciifier` can be created as below:
        
            deasciifier = NGramDeasciifier(fsm, ngram)
     
A text can be deasciified as follows:
     
    sentence = Sentence("cocuk")
    deasciified = deasciifier.deasciify(sentence)
    print(deasciified)
    
Output:

    çocuk
