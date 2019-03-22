###################################
# クラス
###################################

class Human():
  # コンストラクタ
  def __init__(self, name):
    self.name = name

  # 自己紹介
  def introduce_oneself(self):
    print("私は" + self.name + "です")

taro = Human("太郎")
taro.introduce_oneself() # 私は太郎です


