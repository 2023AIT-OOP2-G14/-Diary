from diaries.DiarySample import DiarySample
from diaries.aihacharDiary import aihacharDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    aihacharDiary(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()