from lib.diary_entry import *
'''
given a title  and contents returns a formatted string,
e.g:
"My Title: These are the contents"
'''
def test_format_takes_title_and_contents_returns_formatted_text():
    diary_entry = DiaryEntry("My Title", "These are the contents")
    result = diary_entry.format()
    assert result == "My Title: These are the contents"

'''
It returns the number of words in the diary entry,
e.g:
6
'''

def test_count_words_returns_the_number_words():
    diary_entry = DiaryEntry("My Title", "These are the contents")
    result = diary_entry.count_words()
    assert result == 6

'''
It takes  words per minute that can be read by user, 
and it returns an estimate reading time for a given content
(based on the words per minute the user can read)
e.g:
2 wpm
"My Title", "These are the contents" -> 6/2 = 3
'''

def test_reading_time_takes_2_wpm_returns_reading_time_for_given_text():
    diary_entry = DiaryEntry("My Title", "These are the contents")
    result = diary_entry.reading_time(2)
    assert result == 3

'''
if the user can read 200 wpm,
and the user has to read for 20 minutes
reading_chunk will return the content that the user could read in those 20 minutes;
N.B: 
If called again, `reading_chunk` should return the next chunk,
skipping what has already been read, until the contents is fully read.
The next call after that should restart from the beginning.
'''

def test_reading_chunk_takes_2wpm_and_3_minutes_returns_piece_of_text():
    diary_entry = DiaryEntry("My Title", "These are the contents")
    result = diary_entry.reading_chunk(2, 3)
    assert result == "My Title: These are the contents"

