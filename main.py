from diaries.DiarySample import DiarySample
from diaries.masaDiary import masaDiary
from diaries.YuutaDiary import YuutaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), YuutaDiary(),masaDiary(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()