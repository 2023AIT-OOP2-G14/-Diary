from diaries.AbstractDiary import AbstractDiary

class YokoyamaDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-14"
    
    def get_summary(self):
        return "ちゃんと授業に行けた"
    
    def get_author(self):
        return "Yokoyama"