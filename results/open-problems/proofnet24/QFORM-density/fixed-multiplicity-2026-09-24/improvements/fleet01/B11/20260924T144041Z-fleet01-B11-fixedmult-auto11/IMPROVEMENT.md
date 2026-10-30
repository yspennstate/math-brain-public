# fleet01/B11 auto11 — complete nine-direction replacement with constant <2547

Run: `20260924T144041Z-fleet01-B11-fixedmult-auto11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **complete B11 replacement proof at multiplicity nine; new constant candidate `<2547 K^2/s`; multiplicity eight remains open.** The threshold-nine mechanism already has separate complete reviews in the repository. The new `<2547` constant derived here still needs a genuinely separate end-to-end constant review before being promoted to an independently validated/release constant.

## Theorem

Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by `K<infinity`. Let `A=A^T` be arbitrary real symmetric, `b in R^n`, `c in R`, and assume

` s_9(A) >= s > 0. `

Then

` Q=X^T A X+b^T X+c `

has an essentially bounded density and

` boxed: ||p_Q||_infinity < 2547 K^2/s. `

No Gaussianity, log-concavity, moment, support, iid, sign, exact-rank, leverage, diagonal-basis, smoothness, or post-rotation-independence hypothesis is added. Global continuity is not asserted. The no-pivot order-three Fourier branch has a continuous `C_0` density; the pivot branches below are measure-domination arguments.

The proof is self-contained relative to the fully audited baseline lemmas. Normalize `K=s=1` until the final scaling, and retain

` eta=1/100,   kappa=1/80^2=1/6400. `

---

## 1. Product-Fourier compiler retained from the threshold-nine mechanism

This section records the complete analytic replacement for the baseline order-five endpoint.

Let `H,I,J` be disjoint sets of original coordinates. Let `W` be a `k`-dimensional orthogonal projection of `X_H` with density cap `M_H`. After collecting all same-bank terms into complex phases, write

`Q=F(X_H)+2<W,M_I X_I+M_J X_J+beta>+R(X_I,X_J),`

where `F` is arbitrary measurable and finite a.s., `R` is an arbitrary quadratic/affine polynomial, and `M_J` has row rank `k`. Let `S` be the product of the `k` nonzero singular values of `M_J` (`S=1` when `k=0`).

For each literal `I`-row `a_i` of the `I-J` crossing in `R`, decompose

`a_i=c_i+lambda_i M_J`,  with `c_i perpendicular row(M_J)`,

and let `C` be the matrix with physical rows `c_i`. For `ell>=1` put

`Z_ell=sum_{|T|=ell} det(C_T C_T^T)>0`,
`w_T=det(C_T C_T^T)/Z_ell`,
`alpha_i=sum_{T contains i} w_T`.

Assume each positive `alpha_i<=1/2` and put `d=k+ell`. Then for `t!=0`,

`|phi_Q(t)| <= min(1,K_(k,ell)|t|^(-d/2)),`                    (1.1)

where

`K_(k,ell)=M_H^(1/2) pi^(d/2) 2^(ell/4) e^((k+2ell)/4)
            (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4).`       (1.2)

If `d>2`, Fourier inversion gives

`||p_Q||_infinity
 <= [d/(d-2)] M_H^(1/d) 2^(ell/(2d)) e^((k+2ell)/(2d))
    (ell^ell/ell!)^(1/(2d)) S^(-1/d) Z_ell^(-1/(2d)).`        (1.3)

If `d=2`, the audited half-Riesz identity gives the corresponding half-potential endpoint obtained by integrating `|t|^-1/2 min(1,K/|t|)`.

### Proof

Push the complex measure `exp(itF)dP_H` through `W`. Its complex density `a_t` obeys `|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`. Plancherel at scale `2t` gives

`int |hat a_t(2t(y+beta))|^2 dy <= M_H (pi/|t|)^k.`           (1.4)

Push `exp(itR)dP_(I,J)` through the `k`-dimensional map `M_I X_I+M_J X_J` and call its complex density `mu_t`. For rough laws, insert a compact approximate identity first. Full row rank of `M_J`, conditioning on literal `X_I`, and the audited product-projection theorem give absolute continuity. Cauchy--Schwarz gives

`|phi_Q(t)|^2 <= M_H(pi/|t|)^k ||mu_t||_2^2.`                 (1.5)

To bound `||mu_t||_2`, condition on literal `X_I=x`; translation in the projected output preserves `L^2`. Expanding the mollified squared norm uses one independent copy `X'_J` only. Put `D=X_J-X'_J`; its coordinates remain independent and each difference density is bounded by one. The pure same-bank `J` phase has modulus one, while averaging each original independent `X_i`, `i in I`, produces the scalar factors

`prod_i |psi_i(2t<a_i,D>)|`.

All bounds are uniform in the mollifier, so weak compactness/lower semicontinuity removes it without assuming a conditional density cap.

For one positive-weight `ell`-set `T`, the map

`D -> (M_JD,(<c_i,D>)_(i in T))`

has row-Gram determinant

`S^2 det(C_T C_T^T)`.                                         (1.6)

Normalize its row Gram matrix and apply the audited `d`-dimensional product-projection theorem. Its image density is at most

`e^(d/2)/[S sqrt(det(C_T C_T^T))].`                            (1.7)

Weighted Holder with the subset weights `w_T` raises the scalar Fourier factors to exponents `1/alpha_i`. Because `alpha_i<=1/2`, the audited integrated Fourier-power lemma applies at `p=1/alpha_i>=2` and, after the scale `2t`, gives

`int |psi_i(2t(y+u))|^(1/alpha_i) dy
 <= pi sqrt(2e alpha_i)/|t|.`                                  (1.8)

The determinant geometric mean contributes

`Z_ell^(-1/2) exp(H(w)/2)`,

while the marginal factors contribute

`exp[(1/2)sum_i alpha_i log alpha_i]`.

Choose `T` with law `w` and uniformly order its `ell` elements. Entropy subadditivity for the ordered tuple gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!).`     (1.9)

Substituting (1.7)--(1.9) into (1.5) and taking a square root proves (1.1)--(1.2). For `d>2`,

`int_R min(1,K|t|^(-d/2))dt=2d/(d-2) K^(2/d)`,

and the `pi` from `K^(2/d)` cancels the Fourier factor `1/(2pi)`, proving (1.3). Every random independence statement in this proof is on disjoint literal original-coordinate product banks.

---

## 2. Marginal-free physical `E_3` and `E_2` receivers

For a literal physical crossing matrix `M`, write `E_r(M)=e_r(MM^T)`.

### Third volume

Let `Z=E_3(M)>0`. If `J_i` is the incident third-volume mass at physical row `i`, then `sum_i J_i=3Z`.

If every `J_i/Z<=1/2`, apply (1.3) at `(k,ell,d)=(0,3,3)`. If some row is heavy, promote that literal row `w` and project the remaining rows orthogonally off it. Exact Gram--Schmidt gives

`J_i=||w||^2 E_2(C).`

If the residual order-two marginals are light, use `(1,2,3)`. If a residual row is heavy, promote it; with promoted two-row matrix `P` and remaining residual rows `C_2`,

`det(PP^T)||C_2||_F^2 > J_i/2 > Z/4.`

If the last one-volume packet is light, use `(2,1,3)`. Otherwise one more promoted literal row gives a three-row Gram determinant `>Z/8`, and the exact three-row Plancherel receiver applies. The worst constant is the diffuse branch:

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6),`

`C_3=3 sqrt(2)e(9/2)^(1/6)=14.818337...<15.`                  (2.1)

All four branches have an integrable characteristic-function majorant, so this fixed-crossing receiver is `C_0`.

### Second volume

Repeat the same promotion tree one dimension lower. If `Z=E_2(M)>0`, then

`sup_a E|Q-a|^(-1/2) <= C_2 E_2(M)^(-1/8),`

`C_2=8 sqrt(e)2^(-1/8)=12.095073...<13.`                      (2.2)

In the diffuse branch this follows from `(k,ell,d)=(0,2,2)` and

`int_R |t|^(-1/2) min(1,L/|t|)dt=8 sqrt(L)`;

one heavy row is paid by `(1,1,2)`, and a second heavy row by the exact two-row half-potential receiver. This is a half-potential theorem only, not a rank-two bounded-density assertion.

---

## 3. New exact quarter-power coefficient certificate

The baseline quarter-power proof actually gives the coefficient

`C_q=2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8)`                    (3.1)

in

`P{|R-a|<rho} <= min(1,C_q rho^(1/4))`                         (3.2)

whenever the quadratic part of `R` has operator norm at least one.

We prove the fully elementary bound

` boxed: C_q < 418613/100000 = 4.18613. `                      (3.3)

First, on `[0,1]`, the alternating Taylor polynomial through degree six is an upper bound for `e^{-x}`. Hence

`int_0^1 x^(-5/8)e^(-x)dx
 <= sum_(k=0)^6 (-1)^k/[k!(k+3/8)]
 =1826700959/866256930.`                                       (3.4)

On `[1,infinity)`, `x^(-5/8)<=1`, while

`e > sum_(k=0)^6 1/k! =1957/720 >125/46`,

so `e^{-1}<46/125`. Consequently

`Gamma(3/8)<1826700959/866256930+46/125<2477/1000`;            (3.5)

the final rational margin is `23490637/86625693000>0`.

For the remaining prefactor:

- `2^(5/8)<1543/1000`, since `(1543/1000)^8>32`;
- `pi^(-1/4)<94/125`. Indeed the classical Archimedean lower bound `pi>223/71>313/100`, and `(94/125)^4(313/100)>1`;
- `e^(3/8)<291/200`. The degree-four exponential sum plus its geometric tail gives
  `e^(3/8)<1191929/819200<291/200`.

Therefore

`2^(5/8) pi^(-1/4)e^(3/8)
 <(1543/1000)(94/125)(291/200)
 =21103611/12500000 <169/100.`                                (3.6)

Combining (3.5)--(3.6) proves (3.3).

Layer cake applied to (3.2) now gives the improved logarithmic potential

`sup_a E log_+(1/|R-a|)
 <=4+4 log C_q
 <4+4 log(418613/100000).`                                    (3.7)

---

## 4. Exact singular convolution and sharpened pivot half-potential

For

`J(d)=int_(-1)^1 |x|^(-1/2)|x-d|^(-1/2)dx`,

one has for every `d!=0`

` boxed: J(d) <= pi+4 log2+2 log_+(1/|d|). `                   (4.1)

Proof: `J(-d)=J(d)`. If `0<d<=1` and `x=d^(-1/2)>=1`, exact integration gives

`J(d)=2 asinh(x)+pi+2 acosh(x)`.

The function

`2 asinh x+2 acosh x-4 log x`

is increasing on `[1,infinity)` because

`1/sqrt(x^2+1)+1/sqrt(x^2-1)>=2/x`,

and its limit is `4 log2`. This gives (4.1) for `d<=1`. If `d>=1`, exact integration gives

`J(d)=2 asinh(d^(-1/2))+2 asin(d^(-1/2))`,

which is maximal at `d=1` and is below `pi+4log2`.

Now suppose a quadratic polynomial has at least two unit-magnitude spectral directions and has a scalar `eta`-pivot. The audited Schur count leaves one unit spectral direction in its remainder `R`, so (3.7), (4.1), Tonelli and the scalar-square profile give

`H <=10[pi+4 log2+8+8 log(418613/100000)].`                    (4.2)

We record exact rational log certificates. The positive exponential Taylor sums give

`log2<1733/2500`

(the degree-six sum of `exp(1733/2500)` exceeds `2`), and

`log(418613/100000)<143179/100000`

(the degree-nine positive Taylor sum exceeds `418613/100000` by the positive rational
`16079788264619658996888890097664246707351070219 /
 362880000000000000000000000000000000000000000000000`).

Using also `pi<22/7`, the bracket in (4.2) is strictly less than

`22/7 +4(1733/2500)+8+8(143179/100000)
 =2219873/87500
 =25.369977142857... .`                                        (4.3)

Thus the scalar-pivot truncated half potential is

`H <2219873/8750 =253.699771428...`,                            (4.4)

and the full half potential, adding at most one outside `|Q-a|<=1`, is

`sup_a E|Q-a|^(-1/2) <2228623/8750=254.699771428... .`          (4.5)

### Indefinite pair subcase is smaller

For completeness, the scalar branch is indeed the worst pivot. Re-run the original hyperbolic-tail proof with cancellation ratio `q=2/9`. On a positive level branch `w(t)=u e^t+v e^{-t}`, choose an original coordinate with `|u_i|>=|u|/sqrt2`. Once

`t>=T_0=(1/2)log(sqrt2/q)=log3-(1/4)log2`,

we have `|v_i|e^{-t}<=q|u_i|e^t`, so

`|w_i'| >=[(1-q)/(1+q)]|w_i|=(7/11)|w_i|`.

Choose the tail cutoff also so that `|w_i|>=1`. A change of variable in that original coordinate costs at most `(11/7)log2` on each tail. The same argument on the negative tail and the middle interval yields, on either level sign,

`p(z)<=D^(-1/2)[C_0+log_+(B sqrt(D)/|z-v|)]`,                  (4.6)

where

`C_0=2log3+(37/14)log2`,   `B=36sqrt2/49`.

The baseline logarithmic-kernel integral then gives

`H_ind(D)<=D^(-1/2)[4C_0+8+4log_+(B sqrt D)].`                 (4.7)

For `D>=eta=1/100`, the right side is decreasing in `sqrt D`; also `B/10<1`. Since `log3<11/10` and `log2<7/10`,

`C_0<81/20`,

hence

`H_ind<10(8+4C_0)<242.`                                       (4.8)

A definite pair has truncated half potential `<4pi/sqrt(eta)<126`. Therefore (4.4) controls every pivot under the two-direction hypothesis.

---

## 5. Assemble the nine-direction theorem

Assume `s_9(A)>=1`.

### No pivot

The audited spectral-to-volume proposition at order `k=3` gives

`V_3(A)>=kappa^3`.

A fair literal coordinate cut produces a cross block `M` with

`E_3(M)>=4^(-3)kappa^3`,

so

`E_3(M)^(-1/6)<=2 kappa^(-1/2)=160`.

By (2.1),

`||p_Q||_infinity <15*160=2400.`                              (5.1)

This branch has a continuous `C_0` density.

### Scalar pivot

Suppose `|A_hh|>=eta`. Complete the square in the literal coordinate `X_h`. The Schur complement `S` retains at least eight unit spectral directions by the audited sign-independent Schur lemma.

If `S` has a pivot, Section 4 applies (it needs only two surviving directions), and its full half potential is bounded by (4.5).

If `S` has no pivot, then in particular `s_5(S)>=1`. The audited spectral-to-volume proposition at order `k=2`, followed by a fair cut, gives

`E_2(M_S)>=4^(-2)kappa^2`,

so by (2.2)

`sup_a E|R-a|^(-1/2)
 <13 E_2(M_S)^(-1/8)
 =13 sqrt(160)<165`,                                           (5.2)

strictly smaller than (4.5).

The outer scalar-square profile costs `eta^(-1/2)=10`. Therefore

`||p_Q||_infinity
 <10*(2228623/8750)
 =2228623/875
 =2546.997714285...
 <2547.`                                                        (5.3)

The final strict margin is exactly

`2547-2228623/875 =2/875>0.`

### Definite pair pivot

A definite physical two-coordinate pivot with determinant modulus at least `eta` has conditional density

`<=pi/sqrt(eta)=10pi<32.`                                      (5.4)

### Indefinite pair pivot

A physical indefinite pair removes at most two spectral directions, so its Schur complement retains at least seven unit directions, in particular operator norm at least one. The fully audited baseline hyperbolic/log-potential averaging therefore gives

`||p_Q||_infinity<251.`                                        (5.5)

The no-pivot, scalar, definite-pair and indefinite-pair cases exhaust the normalized theorem. The maximum is (5.3).

---

## 6. Scaling

For general `K,s`, set `Y=KX`. Its coordinates have densities at most one, and define

`Qtilde=Y^T(A/s)Y+(K/s)b^T Y+(K^2/s)c`.

Then `s_9(A/s)>=1` and

`Q=(s/K^2)Qtilde`.

Scalar density scaling applied to the normalized result gives

`boxed: ||p_Q||_infinity <2547 K^2/s.`                          (6.1)

This proves the theorem.

---

## 7. How far the multiplicity lowers in this run

The complete rigorous threshold remains **9**. Current `s_8` work has sharply narrowed the no-pivot obstruction but has not closed it:

- if the ordinary third crossing volume is large, the `E_3` receiver above pays it;
- otherwise current three-bank aggregation produces a literal crossing with a dimension-free `E_2` lower bound and a shared-middle compound overlap;
- if its normalized `E_3/E_2^(3/2)` is not too small, the `E_3` receiver again pays it;
- the unpaid state is therefore an `E_2`-rich / `E_3`-poor shared-middle collar with arbitrary same-bank curvature;
- a separate explicit rank-two construction in the repository shows that `E_2`/`Xi_2` positivity alone cannot be a bounded-density receiver while arbitrary same-bank phases are retained.

Thus no `s_8` theorem is claimed here. The missing ingredient must consume the shared-middle/overlap-one spectral currency, not merely the two-sided second crossing volume.

## 8. Review status

- Baseline `s_17` theorem: **PASS** in the companion full audit for this run.
- Threshold `s_9` theorem: complete replacement proof above; the threshold mechanism has multiple separate prior full reconstructions.
- New constant `<2547 K^2/s`: **proved in this B11 run, but not yet independently reviewed at this exact constant**.
- Threshold `s_8`: **OPEN**.
- Unrestricted three-eigenvalue conjecture: **OPEN**.
- Global continuity at threshold nine: **not proved**; no-pivot branch is `C_0`.

Model: GPT-5.6 Sol. Configured reasoning effort/provider reasoning counters: `UNKNOWN / NOT_EXPOSED`.