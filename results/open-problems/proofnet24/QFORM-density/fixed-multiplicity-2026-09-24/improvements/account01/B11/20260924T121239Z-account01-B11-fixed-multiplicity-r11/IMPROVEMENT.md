# account01/B11 improvement note — constants, nonsymmetric Schur count, terminal r=4 saturation

Run: `20260924T121239Z-account01-B11-fixed-multiplicity-r11`  
Baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

This note records only rigorously proved improvements/obstructions. It does **not** claim a 16-eigenvalue theorem or the unrestricted three-eigenvalue conjecture.

## 1. Same-proof constant improvement at multiplicity 17

Let `L0=4+4 log 16`, as in the manuscript. In the scalar-pivot proof of the truncated half potential,

\[
H(Q)\le \eta^{-1/2}(8+3L_0)
=10(20+12\log16)
=200+120\log16.
\]

This dominates all other branches used to establish the nine-direction remainder estimate: no pivot gives `<200`; a definite two-coordinate pivot gives `<40 pi`; the indefinite-pair bound is smaller. Therefore the full half potential satisfies

\[
\sup_a E|Q-a|^{-1/2}\le 201+120\log16.
\]

At the main scalar pivot, `|A_ii|>=eta=1/100`, so

\[
\|p_Q\|_\infty
\le 10(201+120\log16)
=2010+1200\log16
=5337.106466687737\ldots .
\]

The no-pivot branch is at most `800e`, the definite-pair branch is `<40`, and the indefinite-pair branch is `<251`. Hence the entire proof gives the replacement theorem

> If the hypotheses of the manuscript hold with `s_17(A)>=s>0`, then
> \[
> \boxed{\|p_Q\|_\infty\le (2010+1200\log16)K^2/s<5610K^2/s.}
> \]

No hypothesis changes. This is a complete numerical strengthening of the stated `10000 K^2/s` bound.

## 2. Nonsymmetric singular-value Schur count

### Lemma

Let a real square matrix (symmetry not assumed) be partitioned as

\[
N=\begin{pmatrix}B&C\\D&E\end{pmatrix},\qquad B\in\mathbb R^{k\times k},\quad \det B\ne0,
\]

and let

\[
S=E-DB^{-1}C.
\]

Then for every `t>0`,

\[
\boxed{\#\{j:s_j(S)\ge t\}\ge \#\{j:s_j(N)\ge t\}-k.}
\]

Equivalently,

\[
\boxed{s_j(S)\ge s_{j+k}(N),\qquad 1\le j\le n-k.}
\]

### Proof for invertible N

Block inversion gives `S^{-1}` as the complementary row/column compression of `N^{-1}`. For orthogonal coordinate projections `P,Q`, singular values satisfy

\[
s_j(PN^{-1}Q)\le s_j(N^{-1}).
\]

Thus

\[
\#\{j:s_j(S^{-1})>t^{-1}\}
\le
\#\{j:s_j(N^{-1})>t^{-1}\}.
\]

For an invertible `m x m` matrix `T`, the singular values of `T^{-1}` are the reciprocals of those of `T` in reverse order. Therefore

\[
\#\{s_j(T^{-1})>t^{-1}\}=m-\#\{s_j(T)\ge t\}.
\]

Apply this to `S` and `N` and rearrange.

### Singular N

Take real `epsilon_l->0` avoiding the finitely many values for which either `N+epsilon_l I` or `B+epsilon_l I_k` is singular. The corresponding Schur complements converge to `S`, because `B` is invertible. Singular values are 1-Lipschitz under operator-norm perturbation, so for `|epsilon_l|<t`,

\[
\#\{s_j(N+\epsilon_l I)\ge t-|\epsilon_l|\}
\ge \#\{s_j(N)\ge t\}.
\]

Apply the invertible result at threshold `t-|epsilon_l|` and pass to the limit by continuity of ordered singular values. This proves the lemma.

This lemma is strictly more general than the manuscript's symmetric eigenvalue-modulus Schur count, but it does not by itself lower the theorem's multiplicity.

## 3. Attempted 17 -> 16 reduction: exact terminal Schur saturation

The existing no-pivot order-five proof can fail only at terminal ratio index `r=4`. Write its completion as

\[
M=A-E=D+R,
\]

with

\[
\operatorname{rank}R\le12,\qquad R_{L,L}=P_{L,L},\qquad \operatorname{rank}P\le4.
\]

Assume the attempted lower hypothesis `s_16(A)>=1`, let `epsilon=||E||<=1/16`, and put `tau=1-epsilon`. Then `s_16(M)>=tau`. Rank perturbation forces at least four diagonal entries of `D` of modulus `>=tau`. If there are five, the manuscript's original `5x5` diagonal-dominance contradiction closes the branch. Thus the only new chamber is exact saturation: precisely four such indices. Call them `H subset L`, `|H|=4`.

The same no-pivot estimates imply that

\[
R_{H,H}=P_{H,H}
\]

is strictly diagonally dominant and hence invertible. Put

\[
D_H=\operatorname{diag}(D_{ii}\mathbf 1_{i\in H}),
\qquad N=M-D_H.
\]

Because `rank D_H<=4`,

\[
s_{12}(N)\ge s_{16}(M)\ge tau.
\]

Use `H` as a 4-dimensional pivot in `N`. By the nonsymmetric Schur lemma above, the Schur complement `S_H(N)` has at least eight singular values `>=tau`.

Now decompose the completion correction in the support form used by the manuscript:

\[
R=P+U+V,
\]

where `U` is supported on the four seed rows `T`, and `V` is supported on the four seed columns `S_0` (here `S_0` denotes the sampled seed, to distinguish it from the Schur complement). Because `H subset L`, neither `U` has rows in `H` nor `V` columns in `H`. Since `P` has rank at most four and `P_{H,H}` is invertible, `rank P=4` and its Schur complement across `H` vanishes:

\[
P_{K,K}-P_{K,H}P_{H,H}^{-1}P_{H,K}=0.
\]

A direct expansion gives

\[
S_H(N)=D_K+W_T+W_{S_0},
\]

where

\[
W_T=
U_{K,K}-U_{K,H}P_{H,H}^{-1}P_{H,K}
-U_{K,H}P_{H,H}^{-1}V_{H,K},
\]

and

\[
W_{S_0}=
V_{K,K}-P_{K,H}P_{H,H}^{-1}V_{H,K}.
\]

Every row of `W_T` outside `T` is zero, so `rank W_T<=4`. Every column of `W_{S_0}` outside `S_0` is zero, so `rank W_{S_0}<=4`. Hence

\[
\operatorname{rank}(W_T+W_{S_0})\le8.
\]

In the exact-saturation chamber, every diagonal entry in `D_K` has modulus `<tau`, so `||D_K||<tau`. The rank perturbation inequality then gives

\[
s_9(S_H(N))<tau,
\]

i.e. **at most eight** singular values can reach `tau`.

Combining lower and upper bounds:

\[
\boxed{\#\{j:s_j(S_H(N))\ge tau\}=8.}
\]

Thus the pure Schur-compression mechanism reaches an exact **8-versus-8 saturation**. It does not contradict `s_16(A)>=1`.

### Consequences of the saturation identity

Any one of the following additional facts would close the terminal chamber and therefore prove the 16-direction no-pivot step:

- a fifth diagonal entry of `D` with modulus `>=tau`;
- `rank(W_T+W_{S_0})<=7` (or any strict rank slack);
- a ninth Schur singular value `>=tau` forced by another invariant;
- a quantitative reason the eight rank directions cannot all simultaneously sit at/above `tau` under the sampling identities.

None follows from the current manuscript hypotheses by the above argument alone.

## 4. Fresh compatible terminal information from another worker

After the derivation above, a source refresh found the independent account02/B14 terminal lemma in

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account02/B14/20260924T120303Z-account02-B14-QFORM-audit11/AUDIT.md`

(commit observed as `a4f1eeb0645b2dc47feff28df821eba369f914a4` when read).

In the same terminal `r=4`, `s_16` chamber, it proves that the four large directions make `P[H,H]` quantitatively invertible and, if

\[
b=|\det A[S_0,T]|,
\quad c=|\det A[H,T]|,
\quad e=|\det A[S_0,H]|,
\]

then

\[
\frac{ce}{b}=|\det P[H,H]|,
\]

and the no-pivot entry cap implies individually

\[
\boxed{c\ge (109/100)^4 b,\qquad e\ge(109/100)^4 b.}
\]

So every sampled-good terminal seed has two strictly heavier neighboring disjoint four-minors. This is a genuine strengthening of the terminal structure and is compatible with the `8 versus 8` Schur saturation above. It still does **not** prove multiplicity 16, because the heavier neighboring seeds are not known to satisfy the same small residual ratio needed to rerun the good-seed argument.

## 5. Current rigorous threshold

The current unconditional theorem remains at **17** spectral directions. This run does not supply a complete replacement proof at 16 or below. The sharpened next obligation is:

> **Terminal transfer problem.** In the no-pivot `k=5,r=4,s_16` chamber, show that the sampled-good seed's forced heavier neighbors can be transferred to another good seed (or otherwise force fifth-order crossing volume), or prove that the exact `8 versus 8` Schur saturation is incompatible with the volume-sampling optimality identities.

Until that is closed, any statement replacing `s_17` by `s_16` is a GAP.
