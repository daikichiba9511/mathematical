<!-- markdownlint-capture -->

# 測度論ゼミ

## notation

- $\mathbb{R}$　:　実数
- $\mathbb{R} ^ {N}$　：　N次元ユークリッド空間
- $I = (a _ {1}, b _{1}] \times \cdots \times ( a _ {N}, b _{N} ]$　：　$\mathbb{R} ^ {n}$の区間
- $(a _ {1}, b _{1}) \times \cdots \times (a _ {N}, b _{N})$　：　$\mathbb{R} ^ {n}$の開区間
- $E = \underbrace{I _ {1}} _ {\text{区間１}} + \cdots + \underbrace{I _ {N}} _ {\text{区間N}}$ ：　$\mathbb{R} ^ {N}$の区間塊（互いに素なものの和）

- $F _ {N}$ : $\mathbb{R} ^ {N}$の区間塊全体

---

## 導入

- 有限加法族

  ↓

- 外測度

  ↓

- 可測性

  ↓

- 可測集合族　$\Leftrightarrow \sigma$-加法族

測度が**完備**という条件が欲しい

---

#### Def(有限加法族)

$X:\text{set}$

空間Xの部分集合族$F \sub P(\lambda)$が

(1) $\phi \in F$

(2) $\mathbb{A} \in F$　ならば　$A ^ {c}\space(=X-A) \in F$

(3) $A, B \in F$ ならば $\underbrace{A \cup B \in F} _ {\cup _ {n} A _ {n} \in F \text{ で帰納法より}}$

---

##### e.g.) イメージ

![有限加法族イメージ](./finite_algebla.png)

---

#### 定理(4.1)

$Z = X \times Y$として$\mathbb{E} \sub P(X), \mathbb{F} \sub P(Y)$を有限加法族とする。

この時、$K = E \times F$　($E \in \mathbb{E}, F \in \mathbb{F}$)　なる形の集合の有限個の直和として表されるものの全体$\mathbb{A}$は有限加法族

---

(4.1) 証明

まず、$\phi \times \phi = \{(x, y) | x \in \phi, y \in \phi \}$でどちらも満たす元はないので

任意の$Z$に対して, $Z \in \phi \times \phi$ 従って、

「$Z \in \phi \Leftrightarrow Z \in \phi \times \phi$」が真のため$\phi = \phi \times \phi$　　（外延性定理のため）

$K = E \times F \space \space (E \in \mathbb{E} , F \in \mathbb{F})$ ならば

$K ^ {c} \in \mathbb{A}$　($K ^ {c} = Z - K \in \mathbb{A}$)で、また

$
\begin{cases}
    E ^ {c} = X - E \\\\
    F ^ {c} = Y - F
\end{cases}
$

であることから

$$
\begin{aligned}
    Z &= \underbrace{(E + E ^ {c})} _ {X} \times \underbrace{(F + F ^ {c})} _ {Y} \\\\
      &= (E \times F) + (E ^ {c} \times F) + (E \times F ^ {c}) + (E ^ {c}\times F ^ {c})
\end{aligned}
$$

だから、$K ^ {c} = Z - K$より

$$
\begin{aligned}
    K ^ {c} &= (E \times F) ^ {c}\\\\
    &= (E ^ {c} \times F) + (E \times F ^ {c}) + (E ^ {c}\times F ^ {c}) \in \mathbb{A}
\end{aligned}
$$

また$A = A _ {1} + A _ {2}$ で $(A _ {1} , A _ {2} \in \mathbb{A})$ならば $A \in \mathbb{A
}$


## 参考

- 「ルベーグ積分入門」: 伊藤清三
