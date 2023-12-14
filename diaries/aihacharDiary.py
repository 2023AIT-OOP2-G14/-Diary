from diaries.AbstractDiary import AbstractDiary

class aihacharDiary(AbstractDiary):
    
    def get_date(self):
        return "2023-12-14"
    
    def get_summary(self):
        return """今日はオブジェクト指向プログラミング演習2のグループワーク演習だった。
        いまいち授業内容を理解することができなかった。もう一度資料に目を通してみようと思う。"""
    
    def get_author(self):
        return "aihachar"