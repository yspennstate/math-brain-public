# QFORM fixed-multiplicity improvement: pivot-local thresholds and the exact 17 -> 16 obstruction

Run: `20260924T121745Z-fleet01-B12-FIXMULT-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Baseline manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **proved structural reduction and lower local multiplicities; no unconditional replacement of 17 by 16 is claimed.** All statements retain arbitrary independent rough coordinate laws, arbitrary affine terms, arbitrary dimension and arbitrary signs.

## 1. Pivot-local multiplicity theorem

Work first in the normalized cap-one, spectral-scale-one setting of the manuscript, with `eta=1/100`.

### Theorem 1

Let `Q=X^TAX+b^TX+c`, where the coordinates of `X` are independent and have densities bounded by one.

1. If some scalar pivot satisfies `|A_ii|>=eta` and `s_10(A)>=1`, then

\[
\boxed{\|p_Q\|_\infty\le 6010.}
\tag{1}
\]

2. If some principal `2 x 2` block `B` is definite and `|det B|>=eta`, then

\[
\boxed{\|p_Q\|_\infty\le 10\pi<40,}
\tag{2}
\]

with no spectral multiplicity assumption beyond the stated pivot.

3. If some principal `2 x 2` block is indefinite with `det B=-D`, `D>=eta`, and `s_3(A)>=1`, then

\[
\boxed{\|p_Q\|_\infty<251.}
\tag{3}
\]

Consequently, if `s_10(A)>=1` and an `eta`-pivot exists, then the full density conclusion holds with constant 6010. Thus the 17-direction requirement of the baseline theorem is used only in the **no-pivot** branch.

### Proof

For (1), condition on every coordinate except `X_i` and complete the square. The manuscript's scalar profile gives

\[
p_Q(z)\le |A_{ii}|^{-1/2}\,\mathbb E|z-R|^{-1/2}.
\tag{4}
\]

The one-coordinate Schur complement `S` is the quadratic matrix of `R`. The manuscript Schur-count lemma gives

\[
N_S(1)\ge N_A(1)-1\ge9.
\tag{5}
\]

The already proved nine-eigenvalue proposition therefore gives

\[
\sup_a\mathbb E|R-a|^{-1/2}\le601.
\tag{6}
\]

Since `|A_ii|>=1/100`, (4)--(6) give (1).

For (2), condition on the complement of the two pivot coordinates. The conditional joint density of the pair is bounded by one, and the manuscript's definite-pair lemma gives conditional density at most

\[
\pi/\sqrt{|\det B|}\le10\pi.
\]

Averaging the conditional law proves (2).

For (3), the two-coordinate Schur complement `S` satisfies

\[
N_S(1)\ge N_A(1)-2\ge1.
\tag{7}
\]

Hence its quadratic polynomial critical value `R` has nonzero quadratic matrix of operator norm at least one. The manuscript's quarter-power lemma gives

\[
\sup_a \mathbb E\log_+\frac1{|R-a|}\le L_0=4+4\log16.
\tag{8}
\]

Conditioning on the complement, the hyperbolic-pair envelope is

\[
p_{Q\mid X_{B^c}}(z)
\le D^{-1/2}\left(6+\log_+\frac{16\sqrt D}{|z-R|}\right).
\tag{9}
\]

Use

\[
\log_+\frac{16\sqrt D}{|z-R|}
\le \log_+(16\sqrt D)+\log_+\frac1{|z-R|},
\]

average, and use `D>=1/100` together with

\[
\sup_{D>0}D^{-1/2}\log_+D=2/e.
\]

Exactly as in the baseline main proof,

\[
\|p_Q\|_\infty
\le10(10+5\log16)+1/e<251.
\]

This proves (3) and the theorem. No branch uses independence after a rotation.

### Unnormalized form

Restoring arbitrary density cap `K` and spectral scale `s>0` by the manuscript's scaling gives:

- if `s_10(A)>=s` and some `|A_ii|>=s/100`, then `||p_Q||_infty<=6010 K^2/s`;
- if a definite principal pair has `|det B|>=s^2/100`, then `||p_Q||_infty<=10 pi K^2/s`;
- if `s_3(A)>=s` and an indefinite principal pair has `|det B|>=s^2/100`, then `||p_Q||_infty<251 K^2/s`.

Thus lowering the global multiplicity is purely a no-pivot problem within this architecture.

## 2. Exact reduction of the 17 -> 16 no-pivot problem

The next theorem identifies exactly where the baseline interpolation proof stops at sixteen directions.

### Theorem 2 (terminal `r=4` saturation)

Assume `A=A^T` has no `eta`-pivot and

\[
s_{16}(A)\ge1.
\tag{10}
\]

If the baseline order-five conclusion

\[
V_5(A)\ge\kappa^5,
\qquad \kappa=80^{-2},
\tag{11}
\]

fails, then all of the following hold:

1. `V_1,V_2,V_3,V_4` are positive and

\[
\frac{V_{r+1}}{V_r}\ge\kappa,
\qquad r=0,1,2,3,
\tag{12}
\]

so in particular

\[
\boxed{V_4(A)\ge\kappa^4.}
\tag{13}
\]

2. Necessarily

\[
\boxed{V_5(A)<\kappa V_4(A).}
\tag{14}
\]

Thus the only bad volume ratio is the terminal order `r=4` ratio.

3. Applying the manuscript's volume-sampled interpolation at `r=4` produces disjoint four-sets `S,T`, `L=[n]\setminus(S\cup T)`, and

\[
A=D+R+E
\tag{15}
\]

such that

\[
\|E\|_F\le5\sqrt\kappa=\frac1{16},
\qquad
\operatorname{rank}R\le12,
\qquad
R_{L,L}=P_{L,L},
\qquad
\operatorname{rank}R_{L,L}\le4,
\tag{16}
\]

with `D` diagonal and zero on `S union T`.

4. There are at least four indices `H subset L` such that

\[
|D_{ii}|\ge\frac{15}{16}\quad(i\in H).
\tag{17}
\]

For every such four-set `H`, the block `R_{H,H}` is strictly diagonally dominant and hence invertible. Therefore

\[
\boxed{\operatorname{rank}R_{H,H}=4,}
\tag{18}
\]

which **saturates** rather than contradicts the available restricted rank bound `rank R_{L,L}<=4`.

Hence the baseline `4k-3` proof fails at `m=16` for one reason only: the terminal `r=4` restricted-rank inequality becomes equality. Any proof that excludes/pays this saturation chamber yields a 16-eigenvalue theorem without changing the other branches.

### Proof

Suppose `V_5<kappa^5`. If all successive volumes are positive, telescoping gives

\[
V_5=\prod_{r=0}^4\frac{V_{r+1}}{V_r},
\qquad V_0=1,
\]

so some ratio is `<kappa`. If a volume first vanishes, take the preceding ratio. Thus there exists `r in {0,1,2,3,4}` with `V_r>0` and

\[
V_{r+1}<\kappa V_r.
\tag{19}
\]

We show `r<=3` is impossible under (10).

For `r=0`, (19) says

\[
\|\operatorname{off}A\|_F^2=V_1<\kappa,
\]

while no pivot gives `||diag A||<1/100`. Hence

\[
\|A\|\le\|\operatorname{diag}A\|+\|\operatorname{off}A\|_F
<\frac1{100}+\frac1{80}<1,
\]

contradicting `s_16(A)>=1`.

Now let `1<=r<=3`. The manuscript completion lemma gives (15) with

\[
\operatorname{rank}R\le3r,\qquad
\operatorname{rank}R_{L,L}\le r,\qquad
\varepsilon:=\|E\|\le\|E\|_F\le(r+1)\sqrt\kappa\le\frac1{20}<\frac1{16}.
\tag{20}
\]

Perturbation gives

\[
s_{16}(D+R)=s_{16}(A-E)\ge1-\varepsilon.
\tag{21}
\]

The rank shift then yields

\[
s_{16-3r}(D)\ge1-\varepsilon.
\tag{22}
\]

Because `16>=4r+1` for `r<=3`, one has `16-3r>=r+1`. Therefore `D` has at least `r+1` entries of modulus at least `1-epsilon`, all lying in `L`. Choose `H subset L`, `|H|=r+1`, among them.

Since `E` has zero diagonal and no pivot gives `|A_ii|<eta`,

\[
|R_{ii}|\ge1-\varepsilon-\eta
\ge1-\frac1{16}-\frac1{100}
=\frac{371}{400}.
\tag{23}
\]

For `i!=j` in `H`, no pivot gives `|A_ij|<1/7` and

\[
|R_{ij}|\le |A_{ij}|+|E_{ij}|<\frac17+\frac1{16}.
\tag{24}
\]

There are at most three off-diagonal entries in a row because `r<=3`, so

\[
\sum_{j\in H\setminus\{i\}}|R_{ij}|
<3\left(\frac17+\frac1{16}\right)
=\frac{69}{112}
<\frac{371}{400}.
\tag{25}
\]

Thus `R_{H,H}` is invertible, giving rank at least `r+1`, contradicting `rank R_{L,L}<=r`. Hence every bad ratio with `r<=3` is impossible. This proves (12)--(14).

At `r=4`, the same completion gives

\[
\varepsilon\le5\sqrt\kappa=\frac1{16},
\]

and (21) with `rank R<=12` gives

\[
s_4(D)\ge s_{16}(D+R)\ge\frac{15}{16}.
\]

Thus (17) holds for a four-set `H subset L`. For this four-set, (23) remains true and now each row has only three off-diagonal entries, so the stronger bound (25) still applies. Hence `R_{H,H}` is invertible and has rank four. But the restricted rank statement is only `rank R_{L,L}<=4`, so there is no contradiction. This proves the exact saturation statement.

## 3. Thirteen directions: the analytic endpoint is also exact for the present receiver

For completeness, the same baseline algebra at `k=4` gives a no-pivot order-four crossing under `s_13(A)>=1`. The determinant theorem then gives

\[
|\phi_Q(t)|\le\min\{1,u/|t|\},
\qquad u\le160\pi e.
\tag{26}
\]

This is square-integrable but not integrable. Gaussian regularization plus Plancherel therefore proves an `L^2` density with

\[
\boxed{\|p_Q\|_2\le\sqrt{2u/\pi}\le\sqrt{320e},}
\tag{27}
\]

but (26) alone cannot yield an `L^infinity` bound by absolute Fourier inversion. Thus, within the current proof architecture, the two sharp bottlenecks are:

- algebraically, the `r=4` saturation chamber for `17 -> 16`;
- analytically, the order-four `1/|t|` endpoint for the broader route toward 13.

The pivot branches do not cause either bottleneck.

## 4. Dependency map and next proof obligation

A rigorous `17 -> 16` theorem now needs only one new no-pivot implication:

> In the terminal `r=4` saturation state (13)--(18), prove a dimension-free bounded-density receiver for the original quadratic form, or derive a quantitative order-five crossing-volume lower bound despite the saturated restricted rank.

Useful information still unused by the rank-only contradiction includes the exact interpolation factorization

\[
P=A_{\cdot,T}A_{S,T}^{-1}A_{S,\cdot},
\]

its exact agreement with `A` on rows `S` and columns `T`, the invertibility/diagonal dominance of `R_{H,H}`, and the already-large order-four disjoint volume `V_4>=kappa^4`. A successful argument must exploit such quantitative structure; merely improving the global rank estimate from `3r` is not justified by the current proof.

No claim is made that sixteen is sufficient, and no Gaussianity, support, moment, diagonal, exact-rank, leverage, or rotated-independence assumption has been introduced.
