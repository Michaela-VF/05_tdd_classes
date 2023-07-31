class GrammarStats:
    def __init__(self):
        pass
  
    def check(self, text):
        self.text = text
        #for char in text:
        print(f"text[0] is: {text[0]} while text[-1] is: {text[-1]}")
        return text[0] in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ") and text[-1] in (".?!")

grammar_stats = GrammarStats()
grammar_stats.check("This is correct!")
print(grammar_stats.check("This is correct!"))

'''
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass
        '''