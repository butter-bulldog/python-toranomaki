###################################
# ループ
###################################

for i in range(5):
   print(i) # 1 2 3 4


for i in range(1,10):
   print(i) # 1 2 3 4 5 6 7 8 9


word = ["a","b","c","d","e"]
for idx, elem in enumerate(word):
   print(str(idx) + ":" + elem) # 0:1 1:b…


# break
for i in range(1,10):
  print(i) # 1 2 3
  if i == 3:
    break


# continue
for i in range(1,10):
  if i <= 5:
    continue;
  print(i) # 6 7 8 9


# ループ終了時の処理が書ける
for i in range(1,10):
  print(i)
else:
  print("ループが終わりました")


cnt = 0
while cnt < 5:
  print(cnt)
  cnt+=1
# 0 1 2 3 4
