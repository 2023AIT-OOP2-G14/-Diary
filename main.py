from diaries.DiarySample import DiarySample
from diaries.NiwaDiary import NiwaDiary
from diaries.aihacharDiary import aihacharDiary
from diaries.YuutaDiary import YuutaDiary
from diaries.YokoyamaDiary import YokoyamaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), 
           NiwaDiary(),
           aihacharDiary(),
           YuutaDiary(),
           YokoyamaDiary(),
           ]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()