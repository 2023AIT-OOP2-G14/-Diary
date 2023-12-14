from diaries.AbstractDiary import AbstractDiary

class DiarySample(AbstractDiary):
    def get_date(self):
        return "2023-12-14"
    
    def get_summary(self):
        return "すごくねむかった"
    
    def get_author(self):
        return "K22095中島瑞希"