# An explicit degree cutoff for the planted-clique likelihood ratio

Let Q be G(n,1/2). Let P be obtained by choosing a uniformly random k-subset C of [n] and forcing every edge inside C to be present. Here n≥2 and 0≤k≤n are integers. For each edge e write X_e=2A_e−1. Under Q the variables X_e are independent uniform signs.

Let L=dP/dQ, and let L_{≤D} be its orthogonal projection in L²(Q) onto polynomials of total degree at most the nonnegative integer D in the edge variables. Define

\[
S_D=\|L_{\le D}\|_{L^2(Q)}^2-1.
\]

All logarithms with subscript 2 are in base 2. Write

\[
H(p)=-p\log_2p-(1-p)\log_2(1-p),\qquad
A=\max_{0<p\le1/2}\frac{H(p)}{\sqrt{2p}},\qquad C_*=\frac4{A^2}.
\]

The maximum exists: the displayed function extends continuously to p=0 with value zero and is positive at p=1/2. In particular A≥1 and 0<C_*≤4.

## Theorem

For every n,k,D as above, put

\[
q=\frac{k^2}{n}\,2^{A\sqrt D}.
\]

Then

\[
0\le S_D\le e^q-1-q\le\frac{q^2e^q}{2}.                 \tag{1}
\]

Fix ε∈(0,1/2), let k=⌊n^{1/2−ε}⌋, and write ℓ=log₂n. For every fixed δ∈(0,1):

\[
D_n\le(1-\delta)C_*\varepsilon^2\ell^2
\quad\Longrightarrow\quad S_{D_n}\longrightarrow0.\tag{2}
\]

\[
D_n\ge(1+\delta)C_*\varepsilon^2\ell^2
\quad\Longrightarrow\quad S_{D_n}\longrightarrow\infty.\tag{3}
\]

The integer degrees D_n may otherwise vary arbitrarily. These are statements about the likelihood-ratio projection and normalized polynomial mean separation. They do not assert hardness for arbitrary thresholded polynomial statistics, arbitrary polynomial-time algorithms, or recovery.

## 1. Exact Fourier coefficients

For an edge set F let X_F=∏_{e∈F}X_e, with X_∅=1. The functions X_F are an orthonormal basis under Q: the product X_F X_{F'} has mean zero if F≠F', since some independent uniform sign appears exactly once, and has mean one if F=F'. Every polynomial on the sign cube can be made multilinear using X_e²=1, without increasing degree.

Conditional on C, the density relative to Q is

\[
L_C(X)=\prod_{e\in\binom C2}(1+X_e).
\]

Indeed each forced coordinate has density 2 at X_e=1 and zero at X_e=−1; all other coordinates retain density one. Averaging over C and expanding the product gives

\[
L(X)=\mathbb E_C L_C(X)=\sum_F p_{v(F)}X_F,             \tag{4}
\]

where v(F) is the number of vertices incident to F, p₀=1, and

\[
p_v=\Pr[V(F)\subseteq C]=\frac{(k)_v}{(n)_v}\quad(0\le v\le k),
\qquad p_v=0\quad(k<v\le n).
\]

The falling factorial is (a)_v=a(a−1)⋯(a−v+1). The probability formula follows by counting k-subsets containing a prescribed v-set. Consequently,

\[
S_D=\sum_{1\le |F|\le D}p_{v(F)}^2.                  \tag{5}
\]

There is no edge set with exactly one incident vertex.

## 2. An entropy bound for counting edge sets

For nonnegative integers M,D put B(M,D)=∑_{j=0}^{min(M,D)} binom(M,j). We claim

\[
B(M,D)\le2^{A\sqrt{2MD}}.                            \tag{6}
\]

If M=0 or D=0 the assertion is immediate. If 0<D<M/2, put p=D/M and z=p/(1−p), so 0<z<1. Since z^j≥z^D for j≤D,

\[
B(M,D)\le z^{-D}\sum_{j=0}^{M}\binom Mj z^j
=z^{-D}(1+z)^M=2^{MH(p)}.
\]

By the definition of A, H(p)≤A√(2p), which proves (6) in this case. If D≥M/2, then B(M,D)≤2^M; also √(2MD)≥M and A≥1. This proves (6) in every case, including D=M/2.

There are at most B(binom(v,2),D) graphs on a fixed labelled v-set with at most D edges and no isolated vertices; allowing isolated vertices only increases the count. For v≤k,

\[
p_v=\prod_{i=0}^{v-1}\frac{k-i}{n-i}\le(k/n)^v,
\]

because (k−i)/(n−i)≤k/n for each factor. Grouping (5) by its incident vertex set and using binom(n,v)≤n^v/v! gives

\[
\begin{split}
S_D
&\le\sum_{v=2}^{n}\binom nv (k/n)^{2v}
        B\left(\binom v2,D\right)\\
&\le\sum_{v=2}^{n}\frac{(k^2/n)^v}{v!}
        2^{A\sqrt{v(v-1)D}}\\
&\le\sum_{v=2}^{\infty}\frac{q^v}{v!}=e^q-1-q.
\end{split}
\]

In the first line terms v>k can be included because their true Fourier coefficients are zero. If k=0 the sum vanishes directly. Finally,

\[
\sum_{v=2}^\infty\frac{q^v}{v!}
\le\frac{q^2}{2}\sum_{j=0}^\infty\frac{q^j}{j!}
\]

since (j+2)!≥2j!. This proves (1).

For (2), k²/n≤n^{−2ε}, and the degree assumption implies

\[
q\le n^{-2\varepsilon}\,
2^{2\varepsilon\sqrt{1-\delta}\,\ell}
=n^{-2\varepsilon(1-\sqrt{1-\delta})}\longrightarrow0.
\]

Equation (1) proves (2), including D_n=0.

## 3. Matching lower bound

Choose a maximizer p of H(p)/√(2p). It has p>0 and satisfies

\[
C_*=\frac{8p}{H(p)^2}.                              \tag{7}
\]

Assume the degree condition in (3). Since S_D is nondecreasing in D, it suffices to use the smaller integer degree

\[
d_n=\left\lfloor(1+\delta)C_*\varepsilon^2\ell^2\right\rfloor.
\]

Put

\[
v=\left\lfloor\sqrt{2d_n/p}\right\rfloor,\qquad
M=\binom v2,\qquad m=\lfloor pM\rfloor.
\]

Then m≤pM≤pv²/2≤d_n≤D_n. Moreover v is of order ℓ, so eventually 2≤v≤k and 1≤m<M. Equation (7) gives

\[
\frac v\ell\longrightarrow
\beta:=\frac{4\varepsilon\sqrt{1+\delta}}{H(p)}>0.     \tag{8}
\]

We first count m-edge graphs on a fixed labelled v-set that have no isolated vertices. Choose m edges uniformly among the M possible edges. A fixed vertex is isolated with probability

\[
\frac{\binom{M-(v-1)}m}{\binom Mm}
\le\left(1-\frac{v-1}{M}\right)^m
\le\exp\left(-\frac{m(v-1)}M\right).
\]

For the first inequality, expose the m chosen edges successively without replacement. Conditional on avoiding the v−1 incident edges so far, their proportion among the remaining edges is at least (v−1)/M. If avoidance becomes impossible, the probability is zero and the bound still holds. A union bound over vertices shows that the fraction having an isolated vertex is at most

\[
v\exp\left(-\frac{m(v-1)}M\right)=o(1),
\]

because m/M→p>0 and v→∞. Thus the number b_{v,m} of such graphs without isolated vertices satisfies

\[
b_{v,m}\ge(1-o(1))\binom Mm.                         \tag{9}
\]

Next we bound the binomial coefficient from below without a graph-counting asymptotic. Put r=m/M. For a Binomial(M,r) variable, its probability mass is largest at m: the ratio of successive masses decreases with the index, exceeds one from m−1 to m, and is less than one from m to m+1. The largest of M+1 probabilities is at least 1/(M+1). Hence

\[
\binom Mm\ge\frac{2^{MH(r)}}{M+1}.                  \tag{10}
\]

Since |r−p|≤1/M and p∈(0,1), the derivative of H is bounded on a fixed neighborhood of p. The mean value theorem gives MH(r)=MH(p)+O(1). Consequently,

\[
\log_2\binom Mm\ge MH(p)-O(\log M).                 \tag{11}
\]

There are binom(n,v) choices of the incident vertex set. By (5), the m-edge graphs counted in (9) alone therefore contribute

\[
S_{D_n}\ge\binom nv\left(\frac{(k)_v}{(n)_v}\right)^2b_{v,m}.
                                                               \tag{12}
\]

To evaluate its coefficient, note that v²/k→0 and v²/n→0. For a=k or a=n, the product ∏_{i=0}^{v-1}(1−i/a) is at most one and at least 1−∑_{i=0}^{v-1}i/a. The lower bound follows by induction from (1−x)(1−y)≥1−x−y for x,y∈[0,1]. These products thus tend to one. In particular,

\[
\binom nv\left(\frac{(k)_v}{(n)_v}\right)^2
=\frac{(k)_v^2}{v!(n)_v}
=(1+o(1))\frac{(k^2/n)^v}{v!}.                       \tag{13}
\]

Also k/n^{1/2−ε}→1, so log₂(k²/n)=−2εℓ+o(1). Combining (9), (11), (12), and (13), and using log₂(v!)≤v log₂v, yields

\[
\begin{split}
\log_2 S_{D_n}
&\ge -2\varepsilon v\ell+\frac{H(p)}2v^2
            -O(\ell\log\ell)\\
&=\left(-2\varepsilon\beta+
            \frac{H(p)}2\beta^2+o(1)\right)\ell^2\\
&=\left(2\varepsilon\beta(\sqrt{1+\delta}-1)+o(1)\right)\ell^2.
\end{split}
\]

The leading coefficient is positive. Therefore S_{D_n}→∞, proving (3). All rounding errors are included above: d_n changes by less than one, v differs from √(2d_n/p) by less than one, and m differs from pM by less than one.

## 4. Exact characterization of the constant

The maximizing p is the unique solution p_*∈(0,1/2) of

\[
(1+p_*)\ln(1-p_*)-p_*\ln p_*=0.                    \tag{14}
\]

To see this, put h(p)=−p ln p−(1−p)ln(1−p). The derivative of h(p)/√p has the sign of

\[
F(p)=2p h'(p)-h(p)=(1+p)\ln(1-p)-p\ln p.
\]

The function F(p)/p is strictly decreasing: differentiation gives

\[
\left(\frac{F(p)}p\right)'
=\frac{-\ln(1-p)-2p/(1-p)}{p^2}<0.
\]

The last inequality follows from

\[
-\ln(1-p)=\int_0^p\frac{dt}{1-t}<\frac p{1-p}.
\]

As p↓0, F(p)/p→∞, while F(1/2)=−ln 2<0. Thus there is exactly one zero, with the derivative of h(p)/√p positive before it and negative after it. This proves the maximizer claim. Its location has an exact rational bracket:

\[
5F(1/5)=\ln(4096/3125)>0,\qquad
4F(1/4)=\ln(243/256)<0.
\]

Hence

\[
\frac15<p_*<\frac14,\qquad
C_*=\frac{8p_*}{H(p_*)^2}.                          \tag{15}
\]

There is a second way to derive the coefficient in (15). Restrict the Fourier sum to graphs on v∼aℓ vertices with m∼p binom(v,2) edges. The argument of Section 3 gives the leading logarithm

\[
\ell^2\left(-2\varepsilon a+\frac{a^2H(p)}2\right),
\]

while m/ℓ²→pa²/2. The logarithm is positive exactly when a>4ε/H(p). The infimum of the corresponding degree coefficient for this density is therefore 8ε²p/H(p)². Minimizing over p gives C_*ε² by (7). Densities p>1/2 cannot improve this infimum, because H(1−p)=H(p) and 1−p<p. This agrees with the upper-bound constant obtained from (6).

## 5. A separate overlap identity

Let C,C' be independent uniform k-subsets, and let R=|C∩C'|. For a fixed C the degree-D projection of L_C is

\[
(L_C)_{\le D}=\sum_{F\subseteq\binom C2,\ |F|\le D}X_F.
\]

For fixed C,C', orthogonality of the sign monomials gives

\[
\left\langle(L_C)_{\le D},(L_{C'})_{\le D}\right\rangle_Q
=\sum_{j=0}^{D}\binom{\binom R2}{j},
\]

since the surviving edge sets must be contained in both complete graphs, hence in the complete graph on C∩C'. Averaging over C,C' proves the exact identity

\[
1+S_D=\mathbb E_R\sum_{j=0}^{D}\binom{\binom R2}{j},
\qquad
\Pr[R=r]=\frac{\binom kr\binom{n-k}{k-r}}{\binom nk}. \tag{16}
\]

Binomial coefficients outside their usual nonnegative range are zero. The distribution formula counts C' after fixing C: choose r of its vertices inside C and k−r outside. This identity groups by the overlap of planted sets, rather than by the incident vertices of Fourier monomials.

It also verifies the asymptotic lower bound without counting graphs with no isolated vertices. In the setting of Section 3, for v=O(ℓ), the exact overlap mass can be written

\[
\Pr[R=v]=\frac{(k)_v^2}{v!(n)_v}
\frac{(n-k)_{k-v}}{(n-v)_{k-v}}.                     \tag{18}
\]

For the second factor, each of its k−v factors is 1−(k−v)/(n−v−i), with 0≤i<k−v. The product is at most one and at least

\[
1-\frac{(k-v)^2}{n-k+1}=1-o(1),
\]

using k²/n→0 and the product inequality used for (13). Equations (13) and (18) give Pr[R=v]=(1+o(1))(k²/n)^v/v!. Keeping only the R=v event and the j=m term in (16) therefore yields

\[
1+S_{D_n}\ge(1+o(1))\frac{(k^2/n)^v}{v!}\binom Mm.
\]

Equations (8) and (11) give the same positive leading exponent as in Section 3. Its right side tends to infinity, so this independently proves S_{D_n}→∞. The Fourier-support count in (12) and the exact-overlap count in (18) thus agree at the required exponential scale.

## 6. What the bound implies for polynomial statistics

If f is any real polynomial of degree at most D, then

\[
\begin{split}
\mathbb E_Pf-\mathbb E_Qf
&=\langle f-\mathbb E_Qf,L-1\rangle_Q\\
&=\langle f-\mathbb E_Qf,L_{\le D}-1\rangle_Q.
\end{split}
\]

The second equality is the defining orthogonality of the projection. Cauchy–Schwarz gives

\[
|\mathbb E_Pf-\mathbb E_Qf|
\le\sqrt{S_D}\,\sqrt{\operatorname{Var}_Q f}.         \tag{17}
\]

If S_D>0, equality is attained by f=L_{≤D}−1 after normalization. If S_D=0, every such mean difference is zero. Thus the supremum normalized mean gap is exactly √S_D whenever the degree-D space contains a nonconstant function.

In particular, a polynomial acceptance function f taking values in [0,1] on every graph has Var_Q f≤1/4, since E_Q f²≤E_Q f. Its distinguishing advantage is therefore at most √S_D/2, which vanishes in (2). A test that thresholds a degree-D polynomial need not itself have degree D as a function on the sign cube, so (17) alone does not cover that larger class. Divergence in (3) also does not by itself supply a test with vanishing error: it controls a mean gap relative to variance under Q only.
