# P0072 — exact `n/log n` bridge asymptotic for the loop-erased five-edge losange

Status: **new restricted theorem / PROVED CANDIDATE conditional only on the already-established losange convergence theorem in this own root; full canonical P0072 remains OPEN; publication novelty UNVERIFIED.**

This note continues `research7_2026-09-17/R7-02/artifacts/2026-09-18/2026-09-18T053600Z__P0072_loop_erased_losange_harmonic_martingale.md`.  That note proves for the loop-erased ant process on the five-edge losange that, with unit initial weights, there is an a.s. random `chi in (0,1)` such that

\[
 w_1,w_2\to\chi,\qquad w_4,w_5\to1-\chi,\qquad w_3\to0.
\tag{A}
\]

Here `t_n=n+2`, `W_i=W_i(n)`, `w_i=W_i/t_n`,

\[
d_n=w_1-w_2,
\qquad
Q_n=w_3+w_1w_4+w_2w_5,
\]

and the exact bridge-selection probability already derived from the published loop-erased path formula is

\[
p_n:=\mathbb P(3\text{ reinforced at }n+1\mid\mathcal F_n)
 =\frac{w_3(w_1w_5+w_2w_4)}{Q_n}
 =w_3 r_n,
\tag{1}
\]

where

\[
r_n=1-\frac{w_3-d_n^2}{Q_n}.
\tag{2}
\]

The source state space gives `|d_n|<=w_3`, so `0<=d_n^2<=w_3^2<=w_3`.

The 2022 Kious–Mailler–Schapira paper explicitly says that its uniform-geodesic proof uses a polynomial decay estimate for the normalized middle-edge weight, that obtaining such a rate for the loop-erased rule is much harder, and that the polynomial rate “could in fact be wrong.”  The theorem below proves that it is indeed wrong: the middle edge has raw weight asymptotic to `n/log n`, so its normalized weight is asymptotic to a random positive constant divided by `log n`.

## Theorem

For the loop-erased ant process on the five-edge losange with unit initial weights, let `chi` be the random limit in (A). Then almost surely

\[
\boxed{
  w_3(n)\,\log n\longrightarrow 2\chi(1-\chi)
}
\tag{3}
\]

and hence

\[
\boxed{
  W_3(n)\sim \frac{2\chi(1-\chi)\,n}{\log n}.
}
\tag{4}
\]

In particular, for every fixed `alpha>0`,

\[
 n^\alpha w_3(n)\longrightarrow\infty,
\]

so no almost-sure polynomial upper bound `w_3(n)=O(n^{-alpha})` can hold.

The proof uses a fresh nonrepeating Section-B triple relative to the preceding B2/B16/B19 losange run:

- **B7 (take the limit):** identify the asymptotic bridge selection ratio from the already-proved outer-edge limit;
- **B18 (translate the statement):** replace the quadratic normalized drift by the reciprocal variable `Y_n=t_n/W_3(n)`;
- **B3 (prove something stronger):** prove the exact `n/log n` equivalent, not merely subpolynomial decay.

## 1. B7 — asymptotic selection ratio and raw exponent one

From (A),

\[
Q_n\longrightarrow q:=2\chi(1-\chi)>0.
\tag{5}
\]

Moreover `w_3->0` and `d_n^2<=w_3^2`, so (2) yields

\[
r_n\longrightarrow1.
\tag{6}
\]

Write `X_n=W_3(n)` and let `I_{n+1}` be the indicator that edge 3 is reinforced by ant `n+1`; then

\[
X_{n+1}=X_n+I_{n+1},
\qquad
\mathbb E[I_{n+1}\mid\mathcal F_n]=p_n=\frac{X_n}{t_n}r_n.
\tag{7}
\]

### Lemma 1 — the bridge raw weight diverges

Almost surely `X_n -> infinity`.

### Proof

By (6), a.s. there is a finite random `N` such that `r_n>=1/2` for all `n>=N`. Since `X_n>=1`,

\[
p_n\ge \frac1{2t_n}\qquad(n\ge N).
\]

Thus `sum_n p_n=infinity` pathwise. The conditional Borel–Cantelli lemma gives infinitely many bridge reinforcements, and because `X_n` is nondecreasing integer-valued, `X_n->infinity`. ∎

### Lemma 2 — exponent one

Almost surely

\[
\boxed{\frac{\log X_n}{\log n}\longrightarrow1.}
\tag{8}
\]

### Proof

Set `L_n=log X_n`. By (7),

\[
\Delta L_n=I_{n+1}\log\left(1+\frac1{X_n}\right).
\]

Its predictable drift is

\[
a_n:=\mathbb E[\Delta L_n\mid\mathcal F_n]
 =\frac{r_n}{t_n}
 X_n\log\left(1+\frac1{X_n}\right).
\tag{9}
\]

Lemma 1, (6), and `x log(1+1/x)->1` imply

\[
t_n a_n\longrightarrow1.
\tag{10}
\]

Therefore

\[
\sum_{k<n}a_k\sim\log n.
\tag{11}
\]

Let

\[
M_n=L_n-L_0-\sum_{k<n}a_k.
\]

This is a martingale. Since `log(1+1/X)<=1/X` and `p_n<=X_n/t_n` (because `r_n<=1`),

\[
\mathbb E[(\Delta M_n)^2\mid\mathcal F_n]
\le p_n\log^2\left(1+\frac1{X_n}\right)
\le\frac1{t_nX_n}
\le\frac1{t_n}.
\tag{12}
\]

Hence the predictable quadratic variation is `O(log n)`, while the martingale increments are bounded by `log 2`. Freedman’s inequality on dyadic times, followed by Borel–Cantelli (and its maximal version on the intervening dyadic blocks), gives

\[
M_n=o(\log n)\quad\text{a.s.}
\tag{13}
\]

Combining (11) and (13) proves (8). ∎

Thus the source authors’ possible failure of polynomial normalized decay is already forced: `X_n=n^{1+o(1)}` and `w_3=X_n/t_n=n^{o(1)}` on the logarithmic exponent scale.  B18 now identifies the exact slowly varying factor.

## 2. B18 — reciprocal translation

Define

\[
Y_n:=\frac{t_n}{X_n}=\frac1{w_3(n)}.
\tag{14}
\]

The point of this translation is that the normalized bridge drift in the preceding artifact is quadratic,

\[
F_3=p_n-w_3=-\frac{w_3(w_3-d_n^2)}{Q_n},
\]

whereas the reciprocal has asymptotically constant drift on logarithmic time.

Conditionally on `F_n`, if `I_{n+1}=0`, then

\[
Y_{n+1}-Y_n=\frac1{X_n};
\tag{15}
\]

if `I_{n+1}=1`, then

\[
Y_{n+1}-Y_n
=\frac{t_n+1}{X_n+1}-\frac{t_n}{X_n}
=-\frac{t_n-X_n}{X_n(X_n+1)}.
\tag{16}
\]

Consequently, writing

\[
b_n:=\mathbb E[Y_{n+1}-Y_n\mid\mathcal F_n],
\]

we obtain exactly

\[
\begin{aligned}
b_n
&=\frac1{X_n}
  \left(1-p_n\frac{t_n+1}{X_n+1}\right)\\
&=\frac1{X_n}
  \left(1-r_n\frac{(t_n+1)X_n}{t_n(X_n+1)}\right)\\
&=\frac{1-r_n}{X_n}
  +\frac{r_n(1-w_3)}{X_n(X_n+1)}.
\end{aligned}
\tag{17}
\]

Using (2) and `X_n=t_n w_3`, this becomes the exact decomposition

\[
\boxed{
 b_n=
 \frac{1-d_n^2/w_3}{t_nQ_n}
 +\frac{r_n(1-w_3)}{X_n(X_n+1)}.
}
\tag{18}
\]

Because `d_n^2/w_3<=w_3->0` and `Q_n->q`, the first term satisfies

\[
\frac{1-d_n^2/w_3}{t_nQ_n}
=\frac{1+o(1)}{qt_n}.
\tag{19}
\]

By Lemma 2, for any fixed `epsilon>0`, eventually `X_n>=n^{1-epsilon}`. Choosing, say, `epsilon=1/4`,

\[
\sum_n\frac1{X_n(X_n+1)}<\infty
\quad\text{a.s.}
\tag{20}
\]

Therefore

\[
\sum_{k<n}b_k
=\frac1q\log n+o(\log n)
\quad\text{a.s.}
\tag{21}
\]

## 3. B3 — the martingale error converges, giving the exact constant

Let

\[
Z_n:=Y_n-Y_0-\sum_{k<n}b_k.
\]

This is a martingale. From (15)–(16),

\[
\begin{aligned}
\mathbb E[(Y_{n+1}-Y_n)^2\mid\mathcal F_n]
&=(1-p_n)\frac1{X_n^2}
+p_n\frac{(t_n-X_n)^2}{X_n^2(X_n+1)^2}\\
&\le \frac1{X_n^2}
+\frac{t_n}{X_n(X_n+1)^2},
\end{aligned}
\tag{22}
\]

where the last line uses `p_n<=X_n/t_n`.

Lemma 2 lets us choose, for example, an almost-sure random time after which `X_n>=n^{5/6}`. Then the right-hand side of (22) is bounded by

\[
n^{-5/3}+O(n^{-3/2}),
\]

which is summable. Localizing before that random time if necessary, the martingale convergence theorem gives

\[
Z_n\longrightarrow Z_\infty\in\mathbb R
\quad\text{a.s.}
\tag{23}
\]

Combining (21) and (23),

\[
\frac{Y_n}{\log n}\longrightarrow\frac1q.
\tag{24}
\]

Since `Y_n=1/w_3(n)` and `q=2chi(1-chi)>0`, inversion yields

\[
w_3(n)\log n\longrightarrow q=2\chi(1-\chi),
\]

which is (3). Since `t_n/n->1`, (4) follows. ∎

## 4. Consequences and source interpretation

1. **The parent paper’s suspected obstruction is real.**  The published discussion says that its uniform-geodesic losange proof relies on polynomial decay of the normalized middle edge and that this rate could fail for loop erasure.  Here
   \[
   w_3(n)\sim\frac{2\chi(1-\chi)}{\log n},
   \]
   so polynomial decay does fail.

2. **The bridge is asymptotically negligible but almost linear in raw weight.**
   \[
   W_3(n)=o(n),\qquad W_3(n)=n^{1+o(1)}.
   \]
   Thus “non-geodesic has zero linear normalized mass” and “non-geodesic reinforcement is sparse” are very different statements.

3. **This does not close canonical P0072.**  The 2025 source is universal over finite graphs and covers both reinforcement rules. The frozen metric remains
   `C_P0072: 0 -> 0 (NO MOVEMENT)`.

4. **The restricted five-edge loop-erased milestone is strengthened, not merely rechecked.**  The preceding artifact established convergence/support; the present theorem identifies the exact first-order slowly varying asymptotic of the unique non-geodesic edge.

## 5. Dated prior-art check (2026-09-18)

Primary source/status checks used in this continuation:

- Kious–Mailler–Schapira, *Finding geodesics on graphs using reinforcement learning*, arXiv:2010.04820 / *Annals of Applied Probability* 32 (2022).  Its discussion explicitly leaves the loop-erased five-edge losange open and says polynomial decay of the middle edge could be false.
- Aletti et al., *Open Problems in Stochastic Reinforcement Models* (2025), DOI `10.1007/978-3-031-76738-8_29`, Section 2.  The author/MATRIX PDF still states the general finite-graph geodesic-support conjecture.
- Mailler–Varin, *The two-nest ants process on triangle-series-parallel graphs*, arXiv:2601.22855 (submitted 2026-01-30).  This changes the model to two nests and a restricted graph class; it does not state the present one-nest losange theorem.

A bounded fresh search on 2026-09-18 for the exact phrases `loop-erased ant process`, `losange`, and `n/log n` did not surface this convergence/rate theorem. That is negative evidence only. **Publication novelty remains UNVERIFIED.**

## 6. Next mathematical attack

The exact `n/log n` law suggests a general local principle: once the geodesic-edge normalized weights converge to an interior limit and a non-geodesic edge has selection ratio

\[
\frac{p_e}{w_e}=1-c_e w_e+o(w_e)
\]

with `c_e>0`, the reciprocal transform should give `w_e log n -> 1/c_e`.  The next source-relevant task is to derive such an expansion from the transfer-current/loop-erasure formula on the smallest graph obtained by adding a second non-geodesic chord to the losange, and then determine whether coupled chords preserve logarithmic decay or create a positive-mass obstruction.