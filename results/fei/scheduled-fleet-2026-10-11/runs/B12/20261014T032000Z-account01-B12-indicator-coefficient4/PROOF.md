# Exact indicator coefficient obstructions

## 1. Normalized remainder and tensor law

Let `q:{-1,1}^n->{0,1}` be nonzero and put

\[
p=\mathbb E q=\sum_S\widehat q(S)^2,
\qquad
P_q(S)=\frac{\widehat q(S)^2}{p}.
\]

Write

\[
\mathcal E(q)=\sum_S\widehat q(S)^2
 \log_2\frac1{\widehat q(S)^2},
\qquad
\Phi(q)=\mathcal E(q)-p\log_2\frac1p.
\]

Substitution gives the exact identities

\[
\Phi(q)=pH(P_q),\qquad
\mathcal I(q)=\sum_S|S|\widehat q(S)^2
             =p\,\mathbb E_{P_q}|S|.                 \tag{1}
\]

If `q=product_j q_j` and the factors use disjoint physical variable blocks,
then Fourier coefficients multiply and `P_q=otimes_j P_{q_j}`.  Entropy and
degree add under this product law, hence

\[
\frac{\Phi(q)}{\prod_jp_j}
 =\sum_j\frac{\Phi(q_j)}{p_j},\qquad
\frac{\mathcal I(q)}{\prod_jp_j}
 =\sum_j\frac{\mathcal I(q_j)}{p_j}.                 \tag{2}
\]

In particular, every tensor power of one seed has exactly the seed's ratio
`Phi/I`.  This is a disjoint-product identity, not an overlapping-input
closure theorem.

## 2. Co-singleton family

Fix `r>=1`, let `N=2^r`, and let `q_r` be one except at one point.  In integer
Walsh normalization its empty coefficient is `N-1`; every nonempty
coefficient has magnitude one.  Since the sum of their squares is
`N(N-1)`, the normalized spectral law is

\[
P_{q_r}(\varnothing)=\frac{N-1}{N},\qquad
P_{q_r}(S)=\frac1{N(N-1)}\quad(S\ne\varnothing).
\]

Therefore

\[
h_r:=H(P_{q_r})
=r-\frac{N-2}{N}\log_2(N-1),                         \tag{3}
\]

while

\[
m_r:=\mathbb E_{P_{q_r}}|S|
=\frac{1}{N(N-1)}\sum_{S\ne\varnothing}|S|
=\frac{r}{2(N-1)}.                                   \tag{4}
\]

Combining (1), (3), and (4),

\[
K_r:=\frac{\Phi(q_r)}{\mathcal I(q_r)}
=\frac{2(N-1)}r
 \left(r-\frac{N-2}{N}\log_2(N-1)\right).           \tag{5}
\]

At `r=3`,

\[
K_3=14-\frac72\log_2 7
=4.174257772798386\ldots>4.
\]

The strict inequality is equivalent to `7^7<2^20`, an exact integer
certificate.  At `r=5`,

\[
K_5=62-\frac{93}{8}\log_2 31
=4.407467891752582\ldots>4.4,
\]

with exact certificate `31^155<2^768`.

In fact `K_r>4` for every `r>=3`.  Since

\[
\log_2(N-1)=r+\log_2(1-1/N)
 \le r-\frac1{N\ln2},
\]

(3) is strictly larger than `2r/(N-1)` whenever

\[
(N-1)(N-2)>2rN\ln2,
\quad\text{equivalently}\quad
N-3+2/N>2r\ln2.                                      \tag{6}
\]

Inequality (6) holds at `r=3`.  Its left side increases by
`N-1/N>2 ln 2` when `r` is incremented, proving it for all larger `r`.
Finally expansion of `log(1-1/N)` in (5) yields

\[
K_r=4+\frac{2}{r\ln2}+O(r2^{-r}),                    \tag{7}
\]

so this clean family approaches four from above.  By (2),
`q_{r,k}=q_r^{tensor k}` has `Phi/I=K_r` in dimension `rk` for every
`k>=1`.

## 3. A stronger six-bit exact seed

The deterministic search produced the indicator with 64-bit truth-table
mask

`18446708751093190623`,

whose zero locations are `[5,12,13,28,29,37,45]`.  It has 57 ones.  Its
integer Walsh-square multiplicities are

| Walsh square | multiplicity |
|---:|---:|
| 3249 = 57^2 | 1 |
| 49 | 3 |
| 9 | 24 |
| 1 | 36 |

Their sum is `3648=64*57`, as required by Parseval.  The degree-weighted
sum of integer Walsh squares is 832, so

\[
p=\frac{57}{64},\qquad
\mathcal I=\frac{832}{64^2}=\frac{13}{64},\qquad
m=\frac{\mathcal I}{p}=\frac{13}{57}.                \tag{8}
\]

The normalized spectral entropy is

\[
h_6=\log_2 3648-
\frac{3249\log_2 3249+3\cdot49\log_2 49
 +24\cdot9\log_2 9}{3648}.                           \tag{9}
\]

Consequently

\[
K_*=\frac{\Phi}{\mathcal I}=\frac{h_6}{m}
=\frac{57}{13}h_6
=4.512256384896659\ldots.                             \tag{10}
\]

After collecting prime factors, `K_*>9/2` is equivalent to

\[
2^{3024}>3^{547}19^{475}7^{49},                       \tag{11}
\]

which `CHECK.py` verifies by exact integer arithmetic.  Thus every universal
inequality `Phi(q)<=K I(q)` for Boolean indicators requires

\[
\boxed{K\ge K_*>9/2}.
\]

More precisely, it requires `K>=K_*`; the displayed strict inequality only
certifies the convenient rational lower bound `K_*>9/2`.  Tensor powers of
this seed preserve equality `Phi=K_* I` at every depth by (2).

## 4. Genuine Boolean companion control

For any indicator product `Q_k=q^{tensor k}`, put `f_k=2Q_k-1`.  The
nonempty Fourier coefficients of `f_k` are twice those of `Q_k`, while the
empty coefficient is `2p^k-1`.  Direct substitution gives a bounded
genuine-Boolean FEI ratio.  In particular, for the co-singleton `r=3` seed,

\[
\lim_{k\to\infty}\frac{H(f_k)}{I(f_k)}
=\frac{h_3+\log_2(8/7)}{m_3}
=5.073268136529566\ldots,                             \tag{12}
\]

and for the six-bit seed,

\[
\lim_{k\to\infty}\frac{H(f_k)}{I(f_k)}
=\frac{h_6+\log_2(64/57)}{13/57}
=5.244969399712791\ldots.                             \tag{13}
\]

Thus these growing families are exact activation obstructions but are not
counterexamples to FEI.

## 5. Consequence for the B12 coherent-remainder route

The preceding signed-ensemble reduction could have closed with constant
four if its agreement and disagreement activation indicators were each
payable by the unsigned estimate `Phi<=4I`.  Sections 2 and 3 disprove that
estimate: the clean co-singleton family exceeds four at every depth, and the
six-bit seed forces a coefficient above 4.5.  The failure is multiplicative
and cannot be removed by a depth-independent additive correction.

This does not refute a joint signed payment.  The remaining route must retain
the companion sign, posterior activation information, or terminal reserve
inside the near/separated coherent kernel.  Any unsigned component isolated
from that joint ledger must allow coefficient at least `K_*`.

