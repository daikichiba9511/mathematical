# ガウス過程〜２

## はじめに

お久しぶりです。

この前の記事を書いてからかなりの時間がたち、色々な経験をし、前よりは理解が深まってはいると思いますが、まだまだ若輩者なので頑張ってアウトプットすることで勉強していきたいなと思います。。

最近はある企業様で研究開発的な業務に携わっており、論文調査や機械学習のモデリング、レポート作成とプレゼンなどを行ってます。（最近はMCMCの論文を読んだり、制御工学をかじったいりしました）

世の中が新型コロナウィルスで大変なことになってますが、僕自身今一度これから自分に何ができるのだろうと悩んでいる時期で、転職も視野に入れたカジュアル面談のご連絡お待ちしております。

TwitterのDMが早いかなと思います。よろしくお願いします。

さて、ガウス過程について見ていきますが、前回書いた内容を見てもほとんど思い出せないくらい月日がたってしまいましたがガウス過程について色々書いていきたいと思います。

追記：
書き終えてから、前書いた内容とかぶるとこあるな？と思ったり、内容がとっ散らかってるなと思います。。
このブログは自身のアウトプットとしてやってるので自己満スタンスなので。。
間違えてることもあると思います。。

## ガウス過程

前回は、観測データ${\bf y}$がガウス分布に従い以下のように表せました。
$${\bf y} \sim N( {\bf 0} , \lambda ^ {2} {\bf \Phi \Phi} ^ {T})\tag{1}$$

共分散行列を、${\bf K} =  \lambda ^ {2}\Phi \Phi ^ {T}$とおくと
この時、$(n,  n ^ {\prime})$要素はxの特徴ベクトルを${\bf \Phi}(x)=(\phi _ {0}(x), \cdots, \phi _ {H}(x) )) ^ {T}$とすると
$$
K _ {nn ^ {\prime}} = \lambda ^ {2} \phi(x _ {n}) ^ {T}\phi(x _ {n} ^ {\prime})
\tag{2}$$
とかけます。

つまり、(2)の式が計算できれば(1)の式から目的変数${\bf y}$が従っているガウス分布の形状が決定され、それを元に予測のような汎化タスクを行うことができる。

(2)の$x_n$を変換するような関数をカーネル関数といい、この内積の値を計算することでガウス過程は学習することができます。

このカーネル関数を使った方法はカーネルトリックと言われ、例えばサポートベクターマシーンでも利用することができ、線形分離ができないようなデータであっても、無限次元の内積が完備な空間への写像（これがカーネル関数）を考え内積を計算すると, 標本空間にデータ点を分離するような識別超平面が引けるというものが有ります。

この空間を扱うには関数解析と呼ばれる無限次元を扱う数学の理論が必要で、再生核ヒルベルト空間などの性質が必要だとか。。絶賛勉強中ですが、この分野は微分方程式や量子力学、真相学習などにも関わりがあるので機械学習の理論に興味があったりする人は勉強してみるといいと思います。


ガウス過程は目的変数がガウス分布に従う時、その分散共分散行列をカーネル関数によって無限次元で内積が完備な空間に飛ばし、そこで内積を計算することによって学習し、予測を行うアルゴリズムという訳でした。

## ガウス過程とカーネル

ガウス過程はというようにカーネル関数を使うことに特色があることがわかったと思います。カーネルトリックは、このカーネル関数によってより高次元の空間での内積を計算することで学習する（最適なパラメータを決める）方法でした。

では、どのような関数なのでしょうか。

性質の良いカーネル関数というのがいくつか見つかっているそうです

基本的なもので、動径基底関数(RBF)あるいはガウスカーネルと呼ばれるものが有ります。以下の式でデータ点同士の類似度を測ることができます

$$
k(x,x ^ {\prime}) = a \exp \left(- \frac{|x - x ^ {\prime}| ^ 2}{b} \right)\tag{3}
$$

a,b はこのカーネル関数の性質を決めるパラメータ。aは関数の平均からのどれくらいばらつくかをきめ、bは関数の乱雑な動き具合を決める

他には

- 線形カーネル

$$
k(x,x ^ {\prime}) = {\bf x} ^ T{\bf x}\tag{4}
$$

- 指数カーネル

$$
k(x,x ^ {\prime}) =  \exp \left(- \frac{|x - x ^ {\prime}|}{b} \right)\tag{5}
$$

- 周期カーネル

$$
k(x,x ^ {\prime}) =  \text{exp} \left(a\ \text{cos}\left( \frac{|x - x ^ {\prime}|}{b}\right) \right)\tag{6}
$$

- Matternカーネル

$$
k _ {\nu}(x , x^{\prime}) = \frac{2 ^ {1 - \nu}}{\Gamma(\nu)}\left(\frac{\sqrt{2\nu r}}{\theta}\right) ^ {\nu}\ K _ {\nu}\left(\frac{\sqrt{2\nu r}}{\theta}\right)\tag{7}
$$

$K _ {\nu}$は第二種の変形ベッセル関数、$\theta$はスケールを決めるパラメータで$\nu$が関数の滑らかさを決めるパラメータ

などが知られており、このカーネル関数を組み合わせて学習することも可能となっています。

ガウス過程ではこのカーネル関数によってサンプルの類似度を解析的に求めることで学習します。

(7)は特に　$\nu=\displaystyle{\frac{3}{2}}$や、$\nu=\displaystyle{\frac{5}{2}}$の時はMattern3やMattern5などと呼ばれています。
指数カーネルとRBFカーネルの中間程度の滑らかさを持った関数でデータ解析では初手にこのカーネルを使うという人もいます。

他にも色々なカーネル関数があるので興味がある人はググってみるといいと思います。
基本的によく使われるのはMatternカーネルやRBFカーネルのようです。

リンク先はカーネル関数についてまとめられています。

- [The Kernel Cookbook](https://www.cs.toronto.edu/~duvenaud/cookbook/)

## ガウス過程と観測ノイズ

ここからは観測されたデータには誤差$\epsilon$があるものとして考えていく。

ガウス過程によって生成される関数を$f$として、

$$
f \sim \mathcal{N}({\bf \mu}, {\bf K})\tag{8}
$$

としてデータセットを$D = \{({\bf x}_{i}, y_{i})\} _ {i = 1} ^ {N}$とすると

$$
{\bf y} = f({\bf x}) + \epsilon _ {}\tag{9}
$$

と表せる。この時、誤差が標準分布に従うとすると

$$
\epsilon  \sim \mathcal{N}( {\bf 0}, s ^ {2} {\bf I}) \tag{10}
$$

と表せる。これは平均が０で分散が$s ^ {2}$のばらつきを持つことを言っているので、(8)は(9)
を$f(x)$だけ並行移動したものが${\bf y}$と考えることができるので

$$
{\bf y} = \mathcal{N}\left(f({\bf x}), s ^ {2} {\bf I} \right)\tag{11}
$$

と表せることができるので、$f$がガウス過程から生成された時の${\bf y}$の確率分布は

$$
p( {\bf y} | {\bf f}) = \mathcal{N}\left({\bf f}, s ^ {2} {\bf I} \right) \tag{12}
$$

となる。ここで${\bf f} = \left(f({\bf x}_{1}), \cdots, f({\bf x}_{N}) \right)$とおいた。

一般的な汎化タスクのような機械学習で見たい関係は説明変数${\bf x}$が得られた時の目的変数${\bf y}$がどう予測できるかなので$p({\bf y} | {\bf x})$をみる。

この時、${\bf y}$はガウス過程によって生成された関数$f$によって関係付けられるので、
得られた$f$について期待値をとることで周辺化したものとみなせるので

$$
\begin{aligned}
p({\bf y} | {\bf x}) &= \int p({\bf y} , {\bf f} | {\bf x})d{\bf f}\\\\
&= \int p({\bf y} | {\bf f}) p({\bf f}|{\bf x}) d{\bf f}\\\\
&= \int \mathcal{N}({\bf y} | {\bf f, s ^ {2} {\bf I}}) \mathcal{N}({\bf f}| {\bf \mu}, {\bf K})d{\bf f}
\end{aligned}\tag{13}
$$

このとき(8)に戻ってみるとr.v. としての${\bf y}$ は二つのr.v.としての $f$と$\epsilon$の和の形になっているので、正規分布の再生性を用いることができる。証明はここでは略するが積率母関数を使うと容易にできる。（Twitterで教えていただきました。おもちさんありがとうございました）
そうすると(11)はそれぞれの確率変数が従うガウス分布の平均の行列の和と分散共分散行列の和を使って以下のように表すことができる。

$$
\begin{aligned}
p({\bf y} | {\bf x}) &= \mathcal{N}({\bf 0} + {\bf \mu}, {\bf K} + s ^ {2} {\bf I})\\\\
&= \mathcal{N}({\bf \mu}, {\bf K} + s ^ {2} {\bf I})
\end{aligned}\tag{14}
$$

このとき、新しい分散共分散行列を${\bf K} ^ {\prime} = {\bf K} + s ^ {2} {\bf I}$と置くと

$$
p({\bf y} | {\bf x}) = \mathcal{N}({\bf \mu}, {\bf K} ^ {\prime})\tag{15}
$$

と表すことができる。カーネル関数は組み合わせて使うことができるので観測ノイズを考える時はカーネル関数に足し合わせればいいことが分かる。また今後は簡単の為、${\bf y}$ について中心化を行い平均を０にすると(15)式は以下のようにかける。

$$
p({\bf y} | {\bf x}) = \mathcal{N}({\bf 0}, {\bf K} ^ {\prime})\tag{16}
$$

やはり、分散共分散行列を解析的に求めれば予測が行えることがわかります。

## 予測分布

さて、ベイズ推定など確率モデルを用いて予測を行うようなモデルは予測分布と呼ばれるものを考えます。

渡辺純生先生の「ベイズ統計の理論と方法」などでは１章で定義されてますが、学習するパラメータをwとして確率モデルを$p(x | w)$, サンプルを${\bf x} _ {n} = (x _ {1}, \cdots, x _ {N})$とすると学習するパラメータの事後分布は

$$
p(w | x) = \displaystyle{\frac{\Pi _ {n=1} ^ {N} p(x _ {n} | w) p(w)}{\int \Pi _ {n=1} ^ {N} p(x _ {n} | w) p(w) dw }}\tag{17}
$$

で表せて、これを用いて確率モデル$p(x)$を平均した以下の式で予測を行うと定義され,その分布を予測分布と呼び$p(x|{\bf x} _ {n})$とする。

$$
\begin{aligned}
p(x|{\bf x} _ {n}) &= E _ {w} \left[p(x|w)\right]\\\\
&= \int p(x | w) p(w|{\bf x} _ {n})dw
\end{aligned}\tag{18}
$$

これは(13)式と同じ形でガウス過程もベイズ推定としてみることができる。
(17)の式は最尤法などで求めたりするが、それは正則理論と呼ばれる３つの条件が成立するときに正しく機能するが、極値が複数あったりする（つまり非凸の時）と学習がうまくいってる保証はない。
（ベイズ推定らへんの話は好きなのでいつか他の記事で書きたい。）

ガウス過程の場合はガウス分布の(18)がガウス分布になるので予測分布は解析的に求めることができる。
ちなみにガウス過程では外れ値に対してロバスト性を持たせるのに確率分布モデル$p({\bf y} | {\bf f})$にコーシー分布やt分布を使ったりもするが予測分布が解析的に求めることはできないので、(17)の分子をハミルトニアンとしてMCMCで求めたり、変分推論して求め学習を行う。

ではデータセットDで学習済みのガウス過程において、あるデータ$D _ {test} = \{({\bf x} _ {j} ^ {test}, y _ {j} ^ {test})\} _ {j=1} ^ {M}$ で${\bf x} _ {j} ^ {test}$に対して$y _ {j} ^ {test}$の予測をしたいとする。

予測分布$p({\bf y} ^ {test} | {\bf x} ^ {test}, D)$を求める。

この時,

$$
\begin{pmatrix}
y _ {1}\\\\
\vdots\\\\
y _ {N}\\\\
y _ {1} ^ {test}\\\\
\vdots\\\\
y _ {M} ^ {test}
\end{pmatrix} = \mathcal{N}\left(
\begin{pmatrix}
0\\\\
\vdots\\\\
0\\\\
0\\\\
\vdots\\\\
0
\end{pmatrix},
\begin{pmatrix}
k(x _ {1}, x _ {1}) & k(x _ {1}, x _ {2}) & \cdots & k(x _ {1}, x _ {N}) & k(x _ {1}, x _ {1} ^ {test}) & k(x _ {1}, x _ {2} ^ {test}) & \cdots  & k(x _ {1}, x _ {M} ^ {test})\\\\
k(x _ {2}, x _ {1}) & k(x _ {2}, x _ {2})& \cdots & k(x _ {2}, x _ {N}) & k(x _ {2},  x _ {1} ^ {test}) & k(x _ {2}, x _ {2} ^ {test}) & \cdots  & k(x _ {2}, x _ {M} ^ {test})\\\\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\\\
k(x _ {N}, x _ {1}) & k(x _ {N}, x _ {2})& \cdots & k(x _ {N}, x _ {N}) & k(x _ {N}, x _ {1} ^ {test}) & k(x _ {N}, x _ {2} ^ {test}) & \cdots  & k(x _ {N}, x _ {M} ^ {test})\\\\
k(x _ {1} ^ {test}, x _ {1}) & k(x _ {1} ^ {test}, x _ {2})& \cdots & k(x _ {1} ^ {test}, x _ {N}) & k(x _ {1} ^ {test}, x _ {1} ^ {test}) & k(x _ {1} ^ {test}, x _ {2} ^ {test}) & \cdots  & k(x _ {1} ^ {test}, x _ {M} ^ {test})\\\\
\vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\\\
k(x _ {M} ^ {test}, x _ {1}) & k(x _ {M} ^ {test}, x _ {2})& \cdots & k(x _ {M} ^ {test}, x _ {N}) & k(x _ {M} ^ {test}, x _ {1} ^ {test}) & k(x _ {M} ^ {test}, x _ {2} ^ {test}) & \cdots  & k(x _ {1} ^ {test}, x _ {M} ^ {test})\\\\
\end{pmatrix}
\right)
$$


とかけて、各共分散行列を部分的に以下のように分ける

![gp_predict](gp_predict.png)

そうすると、予測分布は

$$
p({\bf y} ^ {test} | {\bf x} ^ {test}, D) = \mathcal{N}({\bf k} ^ {T}{\bf K} ^ {-1}{\bf y} , {\bf K} ^ {test} - {\bf k} ^ {T}{\bf K} ^ {-1}{\bf k})\tag{19}
$$
同時分布の一部のベクトルが得られた時、残りのベクトルをどう表すかの証明は
別記事か、追記する形にします。

(19)式のパラメータを解析的に計算して求めることでガウス過程回帰は予測を行うことができる。

## コード（おまけ）

(19)を計算することでガウス過程の予測分布求めることができる。

コード全体は以下のようになる。

まずカーネル関数をclassを用いて以下のように定義する

```python
import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

class RBFkernel(object):
    def __init__(self, a, b):
        self._a = a
        self._b = b
    def __call__(self,x, x_prime):
        return self._a * np.exp( - (x - x_prime)**2 / self._b )

class LinearKernel(object):
    def __init__(self):
        pass
    def __call__(self,x : np.ndarray, x_prime : np.ndarray):
        return x.T * x_prime

class ExpKernel(object):
    def __init__(self, b):
        self._b = b
    def __call__(self, x : np.ndarray, x_prime : np.ndarray, b):
        return np.exp( - np.abs(x - x_prime) / self._b)

class PeriodicKernel(object):
    def __init__(self,a, b):
        self._a = a
        self._b = b

    def __call__(self,x : np.ndarray, x_prime : np.ndarray):
        return np.exp(self._a * np.cos( np.abs(x - x_prime) / self._b))

```

Kernelは＿call__メソッドを使うことで、インスタンス化した時はパラメータを与えて定義した上でGaussianProcessないで同じように使えるようにした。
ガウス過程回帰の計算の基本アルゴリズムは

```python
import numpy as np


class GaussianProcess(object):
    def __init__(self, kernel):
        self.__kernel = kernel
        self.mu = None
        self.var = None

    def __size_check(self,x, y):
        if len(x) == len(y):
            pass
        else:
            raise ValueError("data size is not same!")

    def naive_gpr(self, xtrain, ytrain, xtest):
        self.__size_check(xtrain, ytrain)

        N = len(ytrain)
        M = len(xtest)
        K = [[0.]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                K[i][j] = self.__kernel(x=xtrain[i], x_prime=xtrain[j])
        K_inv = np.linalg.pinv(K)
        yy = K_inv * ytrain
        k = [0.]*N
        mu = [0.]*M
        var = [0.]*M
        for m in range(M):
            for n in range(N):
                k[n] = self.__kernel(xtrain[n], xtest[m])
            s = self.__kernel(xtest[m], xtest[m])
            mu[m] = k * yy
            var[m] = s - np.array(k) * K_inv * np.array(k).T
        self.mu = np.array(mu)
        self.var = np.array(var)
        return self

```

### example

```python
    xtrain = np.random.rand(100)
    xtest  = np.random.rand(10)
    ytrain  = np.random.rand(100)
    k = kernel.LinearKernel()
    gpr = GaussianProcess(kernel=k)
    model = gpr.naive_gpr(xtrain, ytrain, xtest)
    print("variance : ", model.var)
    print("mean : ", model.mu)
```

## 最後に

久しぶりに書いたけど、実際書いてる時はこうだ！って書いててもあとで見返すととっ散らかってたり、何が言いたいんだろうなぁって文章でした。。リハビリしながら少しずつ書くようにしたいなと思います。
実際に実装してみるとどう設計するのかが難しいと感じた。今回はとりあえず実装してみた感じなので今後改良していきたいです。次は、GPyとかも使って何かガウス過程について書いていきたいと思います。久々に２、３日でこんなにTex書いて疲れた。。

## 参考

- 「ガウス過程と機械学習」, 持橋大地. 大羽成征. , 講談社, (2019)

- 「[Gaussian Process for Machine Learning](http://www.gaussianprocess.org/gpml/chapters/RW.pdf)」C.E.Ramussen. C.K.I.Williams. the MIT press (2006)
