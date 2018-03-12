
## circuit-calculator
回路計算機

Rustによる実装

### data Structure

#### HasResist trait
抵抗値を持つ素子, 導線を表現するトレイト

#### Resistance
抵抗素子を表現する構造体. 抵抗値をインスタンス変数に持つ.

関数 `get_resistance()` の返り値として抵抗値を返却する.

#### Parallel
素子を並列に接続した場合を表す構造体. 変数 `l` と変数 `r` はそれぞれ, 左・右に接続された導線を記憶する.

関数 `get_resistance()` の返り値として抵抗値を返却する.

#### Serial
素子を直列に接続した場合を表す構造体. 内部でVec<T>をもっていて動的な配列で素子を記憶する.
ただし, １つのVec<T>内での型Tは全て一致している必要がある. この実装ではすべてResistance型として束縛することで解決している.

関数 `get_resistance()` の返り値として抵抗値を返却する.

### 例題
http://www.asahi-net.or.jp/~jk2m-mrt/reidai_1.htm の例題 3 を解くプログラムを以下に示す.

```rust
let pc2 = Parallel{
  l: Resistance{v:30.0},
  r: Serial{v:vec![ Resistance{v:15.0}, Resistance{v:15.0} ]},
};

let pc1_right = Serial{v:vec![ Resistance{v:15.0}, Resistance{v:pc2.get_resistance()}]};

let pc1 = Parallel{
  l: Resistance{v: 30.0},
  r: Resistance{v: pc1_right.get_resistance()}
};

let c = Serial{v:vec![ Resistance{v:15.0}, Resistance{v:pc1.get_resistance()} ]};

println!("gousei teikou: {} [ohm]", c.get_resistance());

```

#### 実行方法
Rustをインストールしていることを前提とする.
```
% cd rust
% cargo run
```

#### 結果
```
gousei teikou: 30 [ohm]
```
