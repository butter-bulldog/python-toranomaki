###################################
# 文字列
###################################

# 代入
str1 = "文字列"
print(str1) # 文字列

# 結合
print(str1 + "です") # 文字列です
print(str1 * 3) # 文字列 文字列 文字列

# 分割
phrase = "If you can dream it you can do it"
print(phrase.split(" ")) ## => ["If","you","can","dream","it","you","can","do","it"]

# 切り出し
word = "ABCDE"
print(word[1:3]) # BC

# 置換
print(word.replace("ABC", "X")) # XDE

# 検索
print("ABC" in word) # True

# 大文字⇔小文字
print(word.lower()) # abcde
print(word.upper()) # ABCDE


# チェック

# 英数字？
print(word.isalnum()) # True
# 英字？
print(word.isalpha()) # True
# 数字？
print(word.isdigit()) # False


