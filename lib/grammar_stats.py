class GrammarStats:
    def __init__(self):
        self._total_tests = 0
        self._passed_tests = 0
  
    def check(self, text):
        self.text = text
        condition = text[0] in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ") and text[-1] in (".?!")
        if condition:
            self._passed_tests += 1
        self._total_tests += 1
        return condition
  
    def percentage_good(self):
        if self._total_tests != 0:
            return (self._passed_tests/self._total_tests)*100
        else:
            return 0