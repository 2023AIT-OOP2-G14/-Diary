from diaries.AbstractDiary import AbstractDiary

class aihacharDiary(AbstractDiary):
    
    def get_date(self):
        return "2023-12-14"
    
    def get_summary(self):
        return """今日はオブジェクト指向プログラミング演習2のグループワーク演習だった。
        この資料を作成するのは、正直しんどかった。 資料に書かれてないことも勝手に伝われば良いのに。と思った。"""
    
    def get_author(self):
        return "aihachar"