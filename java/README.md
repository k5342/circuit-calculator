## circuit-calculator
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

インスタンスメソッド `append()` を持ち，引数として受け取った素子を直列に追加する．

インターフェイス `PartsBehavior` を実装し，各素子の抵抗値の和を合成抵抗の値として返却する関数 `getResistance()` をもつ．

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
これは `Main.java` と同じ内容である．

```java
ParallelCable pc2 = new ParallelCable(new SerialCable(), new SerialCable());
((SerialCable) pc2.getLeft()).append(new Resistance(30));
((SerialCable) pc2.getRight()).append(new Resistance(15));
((SerialCable) pc2.getRight()).append(new Resistance(15));

SerialCable pc1_right = new SerialCable();
pc1_right.append(new Resistance(15));
pc1_right.append(pc2);

ParallelCable pc1 = new ParallelCable(new SerialCable(), pc1_right);
((SerialCable) pc1.getLeft()).append(new Resistance(30));

SerialCable c = new SerialCable();
c.append(new Resistance(15));
c.append(pc1);

System.out.printf("gousei teikou: %f [ohm]\n", c.getResistance());
```

変数 `pc2` は c-e 間，変数 `pc1` は b-f 間を表す `ParallelCable` クラスのオブジェクトであり，
並列接続された素子を表現するためのデータ構造である．

#### 実行方法
全ての .java ファイルをコンパイルした上で，`Main` クラスを実行する．
```
% javac *.java
% java Main
```

#### 結果
```
% java Main
gousei teikou: 30.000000 [ohm]
```
