from lib.grammar_stats import *


'''
It takes a text and returns true if the text begins with a capital letter and ends with a
sentence-ending punctuation mark, false otherwise.
'''

'''
If text starts with capital and ends with a punctuarion mark.
e.g:
it takes   : "This is correct!" ,
it returns : True
'''
def test_check_cap_start_punc_mark_end():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("This is correct!")
    assert result == True

'''
If text does NOT starts with capital and ends with a punctuarion mark.
e.g:
it takes   : "this is NOT correct!" ,
it returns : True
'''

def test_check_non_cap_start_yes_punc_mark_end():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("this is correct!")
    assert result == False

'''
If text does NOT starts with capital NOR ends with a punctuarion mark.
e.g:
it takes   : "this is NOT correct" ,
it returns : FALSE
'''
def test_check_non_cap_start_no_punc_mark_end():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("this is NOT correct")
    assert result == False