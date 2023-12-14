from diaries.DiarySample import DiarySample
from diaries.NakashimaDiary import NakashimaDiary
from diaries.NiwaDiary import NiwaDiary
from diaries.aihacharDiary import aihacharDiary
from diaries.YuutaDiary import YuutaDiary
from diaries.YasuiDiary import YasuiDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), 
           NiwaDiary(),
           aihacharDiary(),
           YuutaDiary(),
           NakashimaDiary(),
           YasuiDiary(),
           ]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()