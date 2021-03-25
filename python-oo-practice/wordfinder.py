import random


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> word_finder = WordFinder('words_test.txt')
    4 words read

    >>> word_finder.random() in ['yellow', 'green', 'orange', 'blue']
    True
    
    """

    def __init__(self, file_path):
        """Read file and print number of words read."""
        file = open(file_path)
        self.words = self.read_file(file)
        print(f'{len(self.words)} words read')


    def read_file(self, file):
        """Parse file and return a list of words."""
        return [word.strip() for word in file]


    def random(self):
        """Return random word from the file."""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
        """Special Word Finder: finds random words from a dictionary 
        and excludes comments and blank lines.
        """

        def read_file(self, file):
            """Parse file and return a list of words without comments or blank lines."""
            return [word.strip() for word in file
                if word.strip() and not word.startswith("#")]





