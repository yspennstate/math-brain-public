# B16 FEI — two-scale first-hit covariance and signed curvature-square reduction

**Date:** 21 September 2026  
**Scope:** `fleet04 / B16`, FEI signed transport proof  
**Execution label:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact finite-dimensional probability/algebra plus a universal Poincare reduction for the current signed q-flip selector. No novelty or publication-priority claim.

## 0. Route and entering state

This run continues the newest compatible B16 handoffs rather than reviving a killed shortcut.

* The fleet03 common-order construction gives an exact signed first-hit disintegration of the R32 q-flip load. Its centered covariance kernel is
  \[
  K(A,B)=\frac{|R_A\cap R_B|}{|R_A\cup R_B|}
  -\frac{|R_A\cap R_B|}{q_Aq_B},
  \]
  with `q_A=|R_A|`, and opposite R32 signs create real covariance refunds.
* The fleet04 dummy-tower result removes arbitrary harmless-coordinate inflation by exact signed plaquette refunds; the remaining target must be dummy-stable.
* The fleet01 one-sided multiplier theorem shows that large positive nonconstant multipliers are credits, so the live burden is the fully refunded constant/radial mode plus genuinely negative nonconstant modes.
* The older Ward-energy result shows that absolute selector turnover loses `log q`, whereas quadratic variation is dimension-free relationwise.

The unresolved issue in the latest common-order report is the aggregate centered-Jaccard quadratic form. The calculation below resolves its probability structure exactly. It does **not** yet identify the resulting two square banks with all of the inherited R16/terminal payment, so full FEI remains open.

Throughout, `M` is the actual active q-flip set and every selected q-flip retains the inherited map to a genuine original-coordinate disagreement edge. Coefficients `c_A` are signed. No absolute value is inserted into the R32 ledger; `2 mod 4` negative entropy credits remain negative inside every aggregate polynomial below.

---

## 1. A single multilinear object for the first-hit selector

For each nonempty frustrated support `R_A subset M`, write its signed coefficient as `c_A` and put
\[
q_A=|R_A|.
\]
Define the multilinear signed relation polynomial
\[
\boxed{
C(z)=\sum_A c_A\prod_{u\in R_A}z_u.
}
\tag{1.1}
\]

Give the active q-flips independent priorities `U_u ~ Unif[0,1]`. For a fixed `v`, the common-order first-hit load is
\[
W_v
=\sum_{A:v\in R_A}
 c_A\,1_{\{U_v=\min_{u\in R_A}U_u\}}.
\tag{1.2}
\]
This is exactly the load of the inherited first-hit selector at `v`; ties have probability zero. Its mean is the inherited Aumann--Shapley load
\[
\mathbb EW_v=\sum_{A:v\in R_A}\frac{c_A}{q_A}.
\tag{1.3}
\]
Hence the aggregate centered selector energy is
\[
\mathcal K(C):=\sum_{v\in M}\operatorname{Var}(W_v),
\tag{1.4}
\]
which is exactly the fleet03 centered-Jaccard quadratic form.

Condition on `U_v=t` and write `s=1-t`. For `u ne v`, set
\[
Y_u=1_{\{U_u>t\}}.
\]
Conditioned on `s`, the `Y_u` are independent `Bernoulli(s)` variables, and
\[
\boxed{
W_v=\partial_v C(Y)
}
\tag{1.5}
\]
in conditional distribution. Indeed a relation contributes to `W_v` iff every other coordinate of that relation survives the threshold `t`.

Define
\[
P_v(Y):=\partial_vC(Y),
\qquad
m_v(s):=\mathbb E_sP_v(Y)=\partial_vC(s\mathbf1).
\tag{1.6}
\]
The second expression is a one-dimensional signed moment polynomial:
\[
\boxed{
m_v(s)=\sum_{A:v\in R_A}c_A s^{q_A-1}.}
\tag{1.7}
\]
Because every frustrated `q_A` is odd, only even powers occur in (1.7).

---

## 2. `P03-B16-FIRST-HIT-TWO-SCALE-VARIANCE` — PROVED

### Theorem 2.1

For every finite signed relation family,
\[
\boxed{
\mathcal K(C)
=\mathcal K_{\mathrm{int}}(C)+\mathcal K_{\mathrm{rad}}(C),
}
\tag{2.1}
\]
where
\[
\boxed{
\mathcal K_{\mathrm{int}}(C)
=\sum_v\int_0^1
\operatorname{Var}_{Y\sim\mathrm{Ber}(s)}(\partial_vC(Y))\,ds
}
\tag{2.2}
\]
and
\[
\boxed{
\mathcal K_{\mathrm{rad}}(C)
=\sum_v\operatorname{Var}_{s\sim\mathrm{Unif}[0,1]}
\bigl(\partial_vC(s\mathbf1)\bigr).
}
\tag{2.3}
\]
Both are positive-semidefinite **signed aggregate** quadratic forms in the coefficients `c_A`.

#### Proof

For each `v`, (1.5) and the law of total variance give
\[
\operatorname{Var}(W_v)
=
\mathbb E_s\operatorname{Var}(P_v(Y)\mid s)
+
\operatorname{Var}_s(\mathbb E[P_v(Y)\mid s]).
\]
Insert (1.6), integrate `s` uniformly, and sum over `v`. `square`

This is not an unsigned decomposition. The signs of different R32 relations combine inside `partial_v C` before either variance is taken. Thus negative entropy credits can cancel positive debits in both banks.

---

## 3. Exact pair kernel split

Let
\[
r=q_A,\qquad s=q_B,\qquad
h=|R_A\cap R_B|,\qquad
u=|R_A\cup R_B|.
\]
For one common coordinate `v in R_A cap R_B`, the two conditional monomials have product expectation
\[
\mathbb E_t[Y^{R_A\setminus\{v\}}Y^{R_B\setminus\{v\}}]
=t^{\nu-1},
\]
while their separate means have product `t^{r+s-2}`. Therefore
\[
\int_0^1\operatorname{Cov}_t(\cdot,\cdot)\,dt
=\frac1\nu-\frac1{r+s-1}.
\tag{3.1}
\]
The radial covariance is
\[
\operatorname{Cov}_{t\in[0,1]}(t^{r-1},t^{s-1})
=\frac1{r+s-1}-\frac1{rs}.
\tag{3.2}
\]
Summing over the `h` common coordinates proves the exact split
\[
\boxed{
K(A,B)=K_{\mathrm{int}}(A,B)+K_{\mathrm{rad}}(A,B)
}
\tag{3.3}
\]
with
\[
\boxed{
K_{\mathrm{int}}(A,B)
=h\left(\frac1\nu-\frac1{r+s-1}\right),
}
\tag{3.4}
\]
\[
\boxed{
K_{\mathrm{rad}}(A,B)
=h\left(\frac1{r+s-1}-\frac1{rs}\right).
}
\tag{3.5}
\]
Adding (3.4)--(3.5) gives exactly
\[
h\left(\frac1\nu-\frac1{rs}\right),
\]
the inherited centered-Jaccard kernel.

Although the entries in (3.4)--(3.5) are nonnegative, the useful statement is stronger: each whole matrix is PSD because it is a covariance Gram form. The R32 quadratic forms remain signed through `c_Ac_B`.

### The inherited `q=3`, overlap-two negative-credit example

For `r=s=3`, `h=2`, `nu=4`,
\[
K=\frac5{18},\qquad
K_{\mathrm{int}}=\frac1{10},\qquad
K_{\mathrm{rad}}=\frac8{45}.
\tag{3.6}
\]
In the genuine fleet03 example with coefficients `+1/8` and `-1/8`, the negative cross covariance refunds
\[
\frac5{576}
=\frac1{320}+\frac1{180}.
\tag{3.7}
\]
Thus the same real negative-credit refund previously seen in the undivided kernel splits into an internal Bernoulli refund `1/320` and a larger radial/moment refund `1/180`. Neither survives an absolute-value replacement.

---

## 4. `P03-B16-FIRST-HIT-CURVATURE-SQUARE-PAYMENT` — PROVED

The exact split can be dominated by two second-difference square banks with constants independent of `|M|`.

### Theorem 4.1

For every signed multilinear `C`,
\[
\boxed{
\begin{aligned}
\mathcal K(C)
\le &\int_0^1 t(1-t)
\sum_{v}\sum_{u\ne v}
\mathbb E_t\left[(\partial_{uv}C(Y))^2\right]dt\\
&+\frac12\int_0^1 t(1-t)
\sum_v\left(\sum_{u\ne v}
\partial_{uv}C(t\mathbf1)\right)^2dt.
\end{aligned}}
\tag{4.1}
\]
The first line is the **internal curvature-square bank**. The second is the **radial moment bank**. All signed relation cancellation occurs inside `partial_uv C` or the radial sum before squaring.

#### Proof of the internal term

For fixed `t`, the product Bernoulli Poincare inequality gives
\[
\operatorname{Var}_t(P_v)
\le t(1-t)\sum_{u\ne v}
\mathbb E_t[(D_uP_v)^2].
\tag{4.2}
\]
For multilinear `C`,
\[
D_uP_v=\partial_{uv}C.
\tag{4.3}
\]
Integrating (4.2) and summing `v` proves the first line.

#### Proof of the radial term

For a polynomial `F` on `[0,1]`, the sharp weighted uniform Poincare inequality is
\[
\operatorname{Var}_{[0,1]}F
\le\frac12\int_0^1t(1-t)F'(t)^2dt.
\tag{4.4}
\]
For completeness, expand `F` in shifted Legendre polynomials. The Sturm--Liouville operator
\[
-\frac d{dt}\left(t(1-t)\frac d{dt}\right)
\]
has eigenvalues `k(k+1)`; the first nonconstant eigenvalue is `2`. Integration by parts gives (4.4), and our `F` is a finite polynomial so no limiting issue occurs.

Now
\[
\frac d{dt}\partial_vC(t\mathbf1)
=\sum_{u\ne v}\partial_{uv}C(t\mathbf1).
\tag{4.5}
\]
Apply (4.4) to every `m_v(t)` and sum over `v`. `square`

### Explicit pairwise form of the upper banks

The internal upper bank has pair kernel
\[
\boxed{
D_{\mathrm{int}}(A,B)
=\frac{h(h-1)}{\nu(\nu+1)}.
}
\tag{4.6}
\]
Indeed there are `h(h-1)` ordered common pairs `(v,u)`, and
\[
\int_0^1t(1-t)t^{\nu-2}dt
=\frac1{\nu(\nu+1)}.
\]
The radial upper bank has pair kernel
\[
\boxed{
D_{\mathrm{rad}}(A,B)
=\frac{h(r-1)(s-1)}
{2(r+s-2)(r+s-1)},
}
\tag{4.7}
\]
with the term interpreted as zero when a derivative vanishes. Equations (4.6)--(4.7) are not asserted entrywise payments for arbitrary signs; (4.1) is the PSD quadratic-form statement.

The key structural gain is that the previously opaque aggregate cross-relation term has become a **second-difference square problem plus a one-dimensional signed moment problem**. This is exactly the division the inherited proof languages suggest: plaquette/q-flip curvature acts on mixed differences, while R16 is a signed moment/refund language. I do not identify either bank with an already-reserved R16 quantity without a separate proof.

---

## 5. A decisive obstruction: the radial bank cannot be discarded

A tempting continuation would be to prove that the radial moment variance is always bounded by a universal multiple of the internal Bernoulli variance and then use only local curvature/noisy-square payment. This is false even for an odd-support relation family.

Fix one distinguished q-flip `0` and `d` further coordinates. Take every triple
\[
R_{ij}=\{0,i,j\},\qquad 1\le i<j\le d,
\tag{5.1}
\]
with coefficient `+1`. All supports have odd size three. For the distinguished coordinate,
\[
P_0(Y)=\sum_{i<j}Y_iY_j=\binom{K}{2},
\qquad K\sim\operatorname{Bin}(d,t).
\tag{5.2}
\]
Its radial and internal pieces are
\[
\mathcal K_{\mathrm{rad},0}
=\frac4{45}\binom d2^2,
\tag{5.3}
\]
\[
\mathcal K_{\mathrm{int},0}
=\frac2{15}\binom d2+\frac3{10}\binom d3,
\tag{5.4}
\]
so their ratio is
\[
\boxed{
\frac{\mathcal K_{\mathrm{rad},0}}
{\mathcal K_{\mathrm{int},0}}
=\frac{4d(d-1)}{3(3d-2)}
\sim\frac49d.
}
\tag{5.5}
\]

More strongly, summing over **all** first-hit coordinates of this same triple-star family gives the exact aggregate formulas
\[
\boxed{
\mathcal K_{\mathrm{int}}
=\frac{d^2(d-1)}{10},
}
\tag{5.6}
\]
\[
\boxed{
\mathcal K_{\mathrm{rad}}
=\frac{d(d-1)^2(d+4)}{45},
}
\tag{5.7}
\]
and therefore
\[
\boxed{
\frac{\mathcal K_{\mathrm{rad}}}
{\mathcal K_{\mathrm{int}}}
=\frac{2(d-1)(d+4)}{9d}
\sim\frac29d.
}
\tag{5.8}
\]
At `d=64` the ratio is exactly `119/8=14.875`.

Thus there is no dimension-free generic inequality that absorbs the radial moment bank into the internal curvature bank. This is a **route obstruction**, not an FEI counterexample: the all-positive triple-star coefficient family is not claimed to be the complete R32 coefficient family of an admissible Boolean phase. It proves only that a proof based on selector algebra alone must retain the radial/moment channel rather than silently charge it to local plaquettes.

This obstruction is consistent with the inherited warning that a bounded terminal endpoint does not control earlier positive variation. Here the correct object is variance of the signed moment polynomial (1.7), not its absolute turnover.

---

## 6. Consequence for the live FEI compiler target

The common-order covariance gap is now separated into two sharply different obligations.

### 6.1 Internal / local obligation

Prove that the actual signed q-flip second-difference square bank
\[
\int_0^1t(1-t)
\sum_{u\ne v}\mathbb E_t[(\partial_{uv}C)^2]dt
\tag{6.1}
\]
is contained in, or paid by, the already retained fractional noisy-square / plaquette-curvature reservoir with the correct normalization and without spending a negative R32 credit twice.

This is now a genuine second-difference object. It no longer contains the arbitrary cross-relation covariance kernel as a black box.

### 6.2 Radial / moment obligation

For each actual q-flip,
\[
m_v(t)=\sum_{A:v\in R_A}c_A t^{q_A-1}
\tag{6.2}
\]
is an even signed moment polynomial. Prove a dimension-free payment for
\[
\sum_v\operatorname{Var}_{t\in[0,1]}m_v(t)
\tag{6.3}
\]
using the inherited alternating R16 first-separation deposits and the separate terminal-band endpoint, while retaining the negative `2 mod 4` credits.

This is materially narrower than paying arbitrary cross-relations: every dependence on relation overlap has disappeared from (6.3). Only the signed relation-size moments through each actual q-flip remain.

The weighted derivative bound in the second line of (4.1) is available, but the triple-star obstruction shows that it cannot be replaced by the internal bank. Any successful closure must use the actual R16/terminal structure or a new source-admissible identity.

---

## 7. Exact checker

`check_first_hit_two_scale.py` uses only the Python standard library and `Fraction`. It verified:

* `68` exact signed coefficient families on active sets through size five by full permutation enumeration;
* equality of the direct common-order first-hit variance, the centered-Jaccard kernel, and the internal-plus-radial split;
* `68` exact instances of both Poincare quadratic-form bounds;
* the exact `q=3`, overlap-two split `5/18 = 1/10 + 8/45`;
* the inherited `+1/8,-1/8` negative-credit refund split `5/576 = 1/320 + 1/180`;
* the single-coordinate triple-star growth.

`check_radial_star_obstruction.py` independently expands the full pair kernels for the aggregate triple-star family for `d=2,...,12` and matches (5.6)--(5.8) exactly. The displayed `d=64` value is then an exact evaluation of the proved closed forms.

Both checkers returned `PASS`. They are falsification evidence for the algebra, not finite-case proofs of FEI.

---

## 8. Status ledger

**PROVED**

* `P03-B16-FIRST-HIT-TWO-SCALE-VARIANCE`: the exact centered-Jaccard/Ward covariance is the sum of an internal Bernoulli variance and a radial signed-moment variance.
* Exact pair kernels (3.4)--(3.5), each PSD as a covariance Gram matrix.
* `P03-B16-FIRST-HIT-CURVATURE-SQUARE-PAYMENT`: the full aggregate covariance is bounded by the two explicit second-difference square banks in (4.1), with constants `1` and `1/2` independent of ambient active-set size.
* The inherited negative-credit covariance refund survives and can be located separately in the internal and radial channels.
* The aggregate triple-star family proves that radial variance cannot generically be swallowed by the internal curvature variance with a dimension-free constant.

**DEAD / DO NOT REPEAT**

* diagonal-only relationwise Ward summation;
* generic endpoint selector-space `L2` control;
* absolute selector turnover;
* replacing the radial/moment channel by the internal plaquette channel through a generic dimension-free comparison;
* discarding negative R32 credits or taking absolute values of the signed relation ledger.

**PRESERVED**

* original-coordinate q-flip to disagreement-edge geometry;
* exact dual-code multiplicity;
* alternating `0 mod 4` debit / `2 mod 4` credit signs;
* dummy-stable coupled selector and exact plaquette refund;
* R16 moment/high-resolvent refunds and their non-reuse constraint;
* separate terminal-band endpoint payment.

**OPEN**

The universal FEI gap is now to identify the actual internal bank (6.1) with available noisy-square/plaquette capacity and to pay the radial signed moment variance (6.3) from the authentic R16/terminal ledger. No equality or domination with those historical reservoirs is assumed here.

**FULL FEI:** **OPEN / NOT PROVED**.

---

## 9. Next exact attack

Work on the radial channel first, because the obstruction proves it cannot be delegated to local curvature. Substitute the exact Borel R32 coefficients into
\[
m_v(t)=\sum_A c_A(t)\,1_{\{v\in R_A\}}\,r^{q_A-1}
\]
with separate notation for Borel time and first-hit threshold, then group by relation weight before integrating either variable. The target is an exact identity or one-sided inequality expressing the radial variance through the same alternating collision-order moments that define the R16 common reservoir, with the terminal response used only as its authorized signed endpoint and never as a bound on cumulative positive variation.

If that identity fails on a genuine Boolean/q-flip family, preserve the witness and switch mechanism. Do not fall back to the now-refuted generic radial-to-internal comparison.
