"""card_number=input()
x=len(card_number)-1
extra_num=""
reiz_num = ""
if x %2 == 0:
    while x >= 0:
        n=str(int(card_number[x-1])*2)
        reiz_num+=(n)
        extra_num+=(card_number[x])
        x-=2
else:
    while x >= 0:
        n=str(int(card_number[x-1])*2)
        reiz_num+=(n)
        extra_num+=(card_number[x])
        x-=2
print(reiz_num)
print(extra_num)
"""
#for l in reiz_num:
