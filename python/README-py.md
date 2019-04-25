# ## circuit-calculator
回路計算機

オブジェクト指向を初めて勉強する人のための，直感的に理解しやすい例を考えてみた．

### class
```
+---------------------------------------------------------+
|                                                         |
|                          Cable                          |
|                                                         |
+-----+---------------------+---------------------+-------+
      ^                     ^                     ^
      |                     |                     |
      |                     |                     |
+-----+-------+     +-------+-------+     +-------+-------+
|             |     |               |     |               |
| SerialCable |     | ParallelCable |     |     Parts     |
|             |     |               |     |               |
+-------------+     +---------------+     +-------+-------+
                                                  ^
                                                  |
                                                  |
                                          +-------+-------+
                                          |               |
                                          |   Resistance  |
                                          |               |
                                          +---------------+

```

#### class Cable
電流が流れる素子，導線を表現するクラス．

#### class SerialCable
素子を直列に接続した場合を表すクラス．内部で ArrayList をもっていて可変長配列で素子を記憶している．

直列に接続された素子の表現として、Cableの配列を内部に持つ

インスタンスメソッド append() を持ち，引数として受け取った素子を直列に追加する．

インターフェース `PartsBehavior` を実装し，各素子の抵抗値の和を合成抵抗の値として返却する関数 `getResistance()` をもつ．

#### class ParallelCable
素子を並列に接続した場合を表すクラス．変数 `left` と変数 `right` はそれぞれ，左・右に接続された導線を記憶する．

インターフェイス `PartsBehavior` を実装し，各素子の抵抗値の逆数和の逆数を合成抵抗の値として返却する関数 `getResistance()` をもつ．

#### class Parts
具体的な素子を表現する抽象クラス．

#### class Resistance
抵抗素子を表現するクラス．抵抗値 R をインスタンス変数として持つ．

関数 `getResistance()` の返り値として抵抗値 R を返却する．

### 例題
http://www.asahi-net.or.jp/~jk2m-mrt/reidai_1.htm の例題 3 を解くプログラムを以下に示す．

```python
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
```

変数 `pc2` は c-e 間，変数 `pc1` は b-f 間を表す `ParallelCable` クラスのオブジェクトであり，
並列接続された素子を表現するためのデータ構造である．

#### 実行方法
```
% python3 main.py
```

#### 結果
```
% python3 main.py
gousei teikou: 30.0 [ohm]
```
