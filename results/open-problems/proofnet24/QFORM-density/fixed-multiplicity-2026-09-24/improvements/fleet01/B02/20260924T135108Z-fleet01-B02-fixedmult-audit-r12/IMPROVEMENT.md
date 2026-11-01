# fleet01/B02 r12 improvement — nine directions with constant 549

Run: `20260924T135108Z-fleet01-B02-fixedmult-audit-r12`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Status: **PROVED CANDIDATE IMPROVEMENT / NEW CONSTANT NOT YET TWO-REVIEW VALIDATED.**

The threshold-nine mechanism used below is the completed `QFORM-FIXED-MULTIPLICITY-9-v1` proof of fleet03/B04, independently reconstructed and PASSed by fleet01/B16 and fleet03/B10 (with fleet03/B08 also recorded as an independent reconstruction). I independently reconstructed its grouped product-Fourier compiler, the physical-row promotion tree, the marginal-free `E_3` density receiver and the marginal-free `E_2` half-potential receiver during this run. The new contribution here is a retuning of the physical pivot/volume parameters together with a self-contained sharpening of the pivot half-potential constants.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K<infinity`. Let `A=A^T` be arbitrary, and let `b,c` be arbitrary. If

\[
s_9(A)\ge s>0,
\]

then

\[
Q=X^TAX+b^TX+c
\]

has an essentially bounded density satisfying

\[
\boxed{\ \|p_Q\|_\infty<549\,K^2/s.\ }
\]

No moment, support, log-concavity, sign, exact-rank, diagonal-basis, smoothness, leverage, or post-rotation-independence hypothesis is added. Global continuity is not claimed. The no-pivot branch is `C_0`; the pivot branches are used through measure domination.

The proof is normalized to `K=s=1` and then rescaled.

## 1. Retuned structural parameters

Set

\[
\eta=\frac1{21},\qquad \sqrt\kappa=\frac1{18},\qquad \kappa=\frac1{324}.
\tag{1.1}
\]

Call a scalar entry with `|a_ii|>=eta` or a principal `2x2` block with determinant modulus at least `eta` a pivot, exactly as in the baseline manuscript but with the new value of `eta`.

If there is no pivot, then

\[
|a_{ii}|<\frac1{21},\qquad
|a_{ij}|<\sqrt{\eta^2+\eta}=\frac{\sqrt{22}}{21}.
\tag{1.2}
\]

### Retuned spectral-to-volume proposition for orders at most three

For `1<=k<=3`, if `A` has no pivot and `s_{4k-3}(A)>=1`, then

\[
V_k(A)\ge\kappa^k.
\tag{1.3}
\]

#### Proof

Repeat the manuscript's telescoping-volume argument. If `V_k<kappa^k`, there is `0<=r<=k-1<=2` with `V_r>0` and `V_{r+1}<kappa V_r`.

If `r=0`, then

\[
\|A\|\le\|\operatorname{diag}A\|+\|\operatorname{off}A\|_F
<\frac1{21}+\frac1{18}=\frac{13}{126}<1,
\]

contrary to the spectral hypothesis.

For `r=1,2`, the manuscript's volume-sampled completion gives

\[
A=D+R+E,
\qquad \operatorname{rank}R\le3r,
\qquad \operatorname{rank}R_{L,L}\le r,
\]

with zero diagonal `E`, `D=0` on the seed, and

\[
\varepsilon:=\|E\|_F<(r+1)\sqrt\kappa=\frac{r+1}{18}.
\]

Writing `m=4k-3`, rank subtraction and perturbation force at least `r+1` diagonal entries of `D` on `L` to have modulus at least `1-epsilon`. Choose `H` of cardinality `r+1` among them.

For `r=2`, `epsilon<1/6`, hence for `i in H`

\[
|R_{ii}|>1-\frac16-\frac1{21}=\frac{11}{14},
\]

while

\[
\sum_{j\in H\setminus\{i\}}|R_{ij}|
<2\left(\frac{\sqrt{22}}{21}+\frac16\right)
=\frac{2\sqrt{22}}{21}+\frac13.
\]

The latter is strictly smaller than `11/14`, because this is equivalent to

\[
4\sqrt{22}<19,
\]

and `352<361` after squaring.

For `r=1`, `epsilon<1/9`; using `sqrt(22)<5`,

\[
|R_{ii}|>1-\frac19-\frac1{21}=\frac{53}{63},
\]

whereas the single off-diagonal entry is smaller than

\[
\frac{\sqrt{22}}{21}+\frac19
<\frac5{21}+\frac19=\frac{22}{63}.
\]

Thus `R[H,H]` is strictly diagonally dominant and has rank `r+1`, contradicting `rank R[L,L]<=r`. This proves (1.3). QED.

The fair physical cut therefore gives, for `k<=3`,

\[
Z_k^{-1/(2k)}\le2\kappa^{-1/2}=36.
\tag{1.4}
\]

For the order-two half-potential branch the exact consequence is

\[
(4^{-2}\kappa^2)^{-1/8}=6.
\tag{1.5}
\]

## 2. Two reviewed Fourier receivers

The independently reconstructed threshold-nine compiler proves, for every literal original-coordinate crossing block `M` and arbitrary remaining same-bank/affine phases,

\[
\|p_Q\|_\infty
\le C_3 E_3(M)^{-1/6},
\qquad
C_3=3\sqrt2\,e(9/2)^{1/6}<15,
\tag{2.1}
\]

and

\[
\sup_a\mathbb E|Q-a|^{-1/2}
\le C_2 E_2(M)^{-1/8},
\qquad
C_2=8\sqrt e\,2^{-1/8}<13.
\tag{2.2}
\]

For completeness, the simple rational checks are as follows. We have `sqrt(2)<99/70`, `e<87/32`, and `(9/2)^(1/6)<9/7`; hence

\[
C_3<3\frac{99}{70}\frac{87}{32}\frac97
=\frac{232551}{15680}<15.
\]

Also `2^{-1/4}<6/7` and `e<11/4`, so after squaring,

\[
C_2^2<64\frac{11}{4}\frac67=\frac{1056}{7}<169.
\]

The grouped compiler proof itself remains product-safe: all conditioning/copies are on disjoint original-coordinate banks, deterministic projections are used only in Jacobians/density bounds, and arbitrary same-bank phases stay inside complex pushforwards.

## 3. Sharpened pivot half-potential at eta=1/21

Two elementary improvements are useful.

### 3.1 Singular convolution kernel

For

\[
J(d)=\int_{-1}^1|x|^{-1/2}|x-d|^{-1/2}\,dx,
\]

one has

\[
\boxed{J(d)<6+2\log_+(1/|d|).}
\tag{3.1}
\]

By symmetry take `d>0`. If `0<d<=1`, direct substitutions give

\[
J(d)=2\operatorname{arsinh}(d^{-1/2})+\pi
+2\operatorname{arcosh}(d^{-1/2}).
\]

Putting `r=d^{-1/2}>=1`,

\[
\operatorname{arsinh}r+\operatorname{arcosh}r-2\log r
=\log[(1+\sqrt{1+r^{-2}})(1+\sqrt{1-r^{-2}})]\le\log4.
\]

Hence `J(d)<=pi+4log2+2log(1/d)<6+2log(1/d)`. If `d>=1`,

\[
J(d)=2\operatorname{arsinh}(d^{-1/2})+2\arcsin(d^{-1/2})<6.
\]

### 3.2 Quarter-power coefficient and logarithmic potential

The exact Gaussian-smoothing coefficient in the manuscript's quarter-power small-ball proof is

\[
C_q=2^{5/8}\pi^{-1/4}e^{3/8}\Gamma(3/8).
\]

A fully rational certificate is

\[
C_q<\frac{35}{8}.
\tag{3.2}
\]

Indeed,

- `2^(5/8)<31/20`;
- `pi^(-1/4)<19/25` from `pi>3`;
- `e^(3/8)<22/15` using `e<87/32<11/4` and the eighth-power comparison;
- `Gamma(3/8)<12665/5016<81/32`: on `[0,1]`, `e^{-x}<=1-x+x^2/2` gives `1348/627`, while the tail is at most `e^{-1}<3/8`.

Their product is `174933/40000<35/8`. Also

\[
\log(35/8)<119/80
\]

by the positive exponential series through order five. Therefore every quadratic polynomial whose quadratic matrix has operator norm at least one satisfies

\[
\sup_a\mathbb E\log_+\frac1{|R-a|}
<4+4\frac{119}{80}=\frac{199}{20}.
\tag{3.3}
\]

### 3.3 Indefinite two-coordinate pivot

For completeness we retain the dependence-safe original-coordinate hyperbolic argument with the improved tail split `q=2/9`. On one branch write

\[
w(t)=ue^t+ve^{-t},\qquad |u|=|v|.
\]

Choose an original coordinate with `|u_i|>=|u|/sqrt2`. Once the backward exponential is at most `q` times the forward one, the change of variables in that physical coordinate costs `(1+q)/(1-q)=11/7`. Choosing the cutoff at

\[
T_1=\log3-\frac14\log2
\]

and treating both tails gives the conditional density envelope

\[
p(z)\le D^{-1/2}\left(C_0+
\log_+\frac{B\sqrt D}{|z-v|}\right),
\tag{3.4}
\]

where

\[
C_0=2\log3+\frac{37}{14}\log2,
\qquad B=\frac{36\sqrt2}{49}.
\]

The manuscript's logarithmic-kernel integral therefore gives

\[
H_{\rm ind}(D)
\le D^{-1/2}\left(4C_0+8+4\log_+(B\sqrt D)\right).
\tag{3.5}
\]

For `D>=eta=1/21` this is maximal at `D=1/21`: below the activation point it is a constant times `D^{-1/2}`, and above it the derivative numerator is `4-(8+4C_0)-4log(Bsqrt D)<0`. Also `B/sqrt(21)<1`. Since `log2<7/10` and `log3<11/10`,

\[
C_0<\frac{81}{20},
\]

and hence

\[
H_{\rm ind}<\sqrt{21}\left(8+4\frac{81}{20}\right)
=\frac{121}{5}\sqrt{21}.
\tag{3.6}
\]

(The elementary exponential-series checks are `e^(7/10)>12013/6000>2` and the order-five lower Taylor sum for `e^(11/10)` is greater than three.)

### 3.4 Pivot synthesis

Suppose a quadratic matrix has at least two eigenvalues of modulus at least one and has an `eta=1/21` pivot.

For a scalar pivot, its Schur remainder retains one unit spectral direction. By (3.1) and (3.3), the truncated half potential is

\[
H<\sqrt{21}\left(6+2\frac{199}{20}\right)
=\frac{259}{10}\sqrt{21}.
\tag{3.7}
\]

A definite pair gives `H<=4pi sqrt(21)`, which is smaller than (3.7). The indefinite pair satisfies (3.6), also smaller than (3.7). Thus every pivot under the two-direction hypothesis has

\[
\boxed{H(Q)<\frac{259}{10}\sqrt{21}.}
\tag{3.8}
\]

Consequently the full half potential is smaller than

\[
\frac{259}{10}\sqrt{21}+1.
\tag{3.9}
\]

## 4. Nine directions: all branches

Assume `K=s=1` and `s_9(A)>=1`.

### 4.1 No pivot

The retuned proposition (1.3) at `k=3` gives `V_3>=kappa^3`. A fair original-coordinate cut gives

\[
E_3(M)\ge4^{-3}\kappa^3,
\qquad E_3(M)^{-1/6}\le36.
\]

By (2.1),

\[
\boxed{\|p_Q\|_\infty<15\cdot36=540.}
\tag{4.1}
\]

This branch has a continuous `C_0` density.

### 4.2 Scalar pivot

A scalar pivot leaves at least eight unit Schur directions. If its Schur complement has a pivot, (3.9) applies. If it has no pivot, then `s_5>=1`; the retuned proposition at `k=2`, a fair cut, and (1.5),(2.2) give the full half potential bound

\[
<13\cdot6=78.
\]

Hence in all cases the Schur remainder has full half potential below `(259/10)sqrt(21)+1`. The outer scalar square profile yields

\[
\|p_Q\|_\infty
<\sqrt{21}\left(\frac{259}{10}\sqrt{21}+1\right)
=\frac{5439}{10}+\sqrt{21}
<549,
\tag{4.2}
\]

where `sqrt(21)<5`.

### 4.3 Definite pair

The direct conditional density bound is

\[
\|p_Q\|_\infty\le\pi\sqrt{21}<16.
\tag{4.3}
\]

### 4.4 Indefinite pair

The pair Schur complement retains at least seven unit spectral directions, so its operator norm is at least one. Averaging the baseline hyperbolic density envelope and using (3.3),

\[
p_Q(z)
\le\sqrt{21}\left(6+\log16+\frac{199}{20}\right)+\frac1e.
\]

Since `log16<14/5` and `sqrt21<5`, this is smaller than `95`.

The maximum of the four branches is therefore strictly below `549`.

## 5. Scaling

For general `K,s`, put `Y=KX` and

\[
\widetilde Q=Y^T(A/s)Y+(K/s)b^TY+(K^2/s)c.
\]

The coordinates of `Y` have density cap one, `s_9(A/s)>=1`, and

\[
Q=(s/K^2)\widetilde Q.
\]

Density scaling gives

\[
\boxed{\|p_Q\|_\infty<549K^2/s.}
\]

## 6. Lowest multiplicity reached

The threshold **9** is rigorously closed by the product-Fourier/volume mechanism and already has at least two genuinely separate full PASS reconstructions in the repository. I found no valid theorem at threshold 8. Current threshold-eight work forces a quantitative overlap-one/two-sided physical collar in the no-pivot endpoint, but the required dependence-safe analytic receiver for that collar remains unproved. Therefore I do not claim `s_8`, and a fortiori do not claim the full three-eigenvalue conjecture.

The new `<549` constant/retuning in this file has not yet received the owner's required two separate complete reviews. It must remain **PROVED_CANDIDATE / NOT YET VALIDATED** until that happens.

Model: `GPT-5.6 Sol`. Provider effort/reasoning telemetry: `UNKNOWN / not exposed`.