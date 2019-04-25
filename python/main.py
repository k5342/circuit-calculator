# !/path/to/bin/of/python
#↑Fill in as appropriate

from abc import ABCMeta, abstractmethod #抽象クラス用

class PartsBehavior(metaclass=ABCMeta):
    @abstractmethod
    def getResistance(self):
        pass

class Cable(PartsBehavior):
    pass

class Parts(Cable):
    pass

class Resistance(Parts):
    def __init__(self, ohm):
        self.ohm = ohm

    def getResistance(self):
        return self.ohm

class SerialCable(Cable):
    def __init__(self, c):
        self.c = c

    def getResistance(self):
        sum = 0.0
        for p in self.c:
            sum += p.getResistance()
        return sum

class ParalleCable(Cable):
    def __init__(self, left, right):
        self.left  = left
        self.right = right

    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right

    def getResistance(self):
        l = self.left.getResistance()
        r = self.right.getResistance()
        return 1.0/(1.0/l + 1.0/r)

# entry point
pc2 = ParalleCable(Resistance(30.0), SerialCable([Resistance(15.0), 
                                                  Resistance(15.0)]))
pc1_right = SerialCable([Resistance(15.0), pc2])
pc1 = ParalleCable(Resistance(30.0), pc1_right)
c = SerialCable([Resistance(15.0), pc1])

print("gousei teikou: %s [ohm]" % c.getResistance())
