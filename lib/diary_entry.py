class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        return f"{self.title}: {self.contents}"


    def count_words(self):
        diary_words = self.format().split()
        return len(diary_words)


    def reading_time(self, wpm):
        self.wpm = wpm
        return self.count_words()/wpm

    def reading_chunk(self, wpm, minutes):
        previous_read = int(0)
        self.wpm = wpm #2
        self.minutes = minutes #3
        words_user_can_read = int(wpm * minutes) #6
        #refactor this: diary_words = self.format().split()
        read_by_user_words = self.format().split()[previous_read:words_user_can_read] #[My, Title:, These, are, the, contents]
        previous_read += words_user_can_read
        return " ".join(read_by_user_words)
    
    '''
    add read_so_far variable
    '''