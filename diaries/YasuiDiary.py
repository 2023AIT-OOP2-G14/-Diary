from diaries.AbstractDiary import AbstractDiary

class YasuiDiary(AbstractDiary):
    def get_date(self):
        return "2023-12-14"
    
    def get_summary(self):
        return "今日はオブジェクト指向プログラミング演習2のグループワーク演習だった。リーダーになっちゃった。"
    
    def get_author(self):
        return "K22137安井"