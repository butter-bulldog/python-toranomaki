###################################
# ファイル
###################################

# 書込
file = open("file.txt","w")
file.write("line1\n")
file.write("line2\n")
file.close()


# 読込
filename = "file.txt"
file = open(filename, "r")
for line in file:
  print(line) # line1 line2
file.close()


# 存在確認
import os.path
if os.path.exists("file.txt"):
    print("存在する")
else:
    print("存在しない")

# 削除
import os
os.remove("file.txt")
