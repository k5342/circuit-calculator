from abc import ABCMeta, abstractmethod #抽象クラス用

# 素子に関するインターフェース
class PartsBehavior(metaclass=ABCMeta):
    @abstractmethod
    def getResistance(self):
        raise NotImplementedError

# 電流が流れる素子, 導線を表現するクラス
class Cable(PartsBehavior):
    pass

# 具体的な素子を表す抽象クラス
class Parts(Cable):
    pass

# 抵抗素子を表現するクラス
class Resistance(Parts):
    def __init__(self, ohm):
        self.ohm = ohm

    # 素子の抵抗値を返す
    def getResistance(self):
        return self.ohm

# 直列に接続した素子を表現するクラス
class SerialCable(Cable):
    def __init__(self):
        self.cables = []

    def append(self, c):
        self.cables.append(c)

    # 直列に接続した素子の抵抗値を計算して返す
    def getResistance(self):
        sum = 0.0
        for p in self.cables:
            sum += p.getResistance()
        return sum

# 並列に接続した素子を表現するクラス
class ParallelCable(Cable):
    def __init__(self, left, right):
        self.left  = left
        self.right = right

    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right

    # 並列に接続した素子の抵抗値を計算して返す
    def getResistance(self):
        l = self.left.getResistance()
        r = self.right.getResistance()
        return 1.0/(1.0/l + 1.0/r)

# entry point
pc2 = ParallelCable(SerialCable(), SerialCable())
pc2.getLeft().append(Resistance(30.0))
pc2.getRight().append(Resistance(15.0))
pc2.getRight().append(Resistance(15.0))

pc1_right = SerialCable()
pc1_right.append(Resistance(15.0))
pc1_right.append(pc2)

pc1 = ParallelCable(SerialCable(), pc1_right)
pc1.getLeft().append(Resistance(30.0))

c = SerialCable()
c.append(Resistance(15.0))
c.append(pc1)

print("gousei teikou: %s [ohm]" % c.getResistance())
