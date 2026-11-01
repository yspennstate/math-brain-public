# B18 FEI proof integration — physical flag square-to-linear Radon bank

**Date:** 21 September 2026  
**Scope:** `fleet03 / B18`, full-FEI proof integration  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status of unrestricted FEI:** **OPEN / NOT PROVED**  
**Claim level:** exact universal source theorem, exact Hardy collision identity, and a sharper compiler-facing sufficient interface. No novelty or publication-priority claim.

## 0. Exact next implication attacked

This run followed the current FEI owner order, read `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md`, and continued from the newest compatible signed-transport state rather than auditing the read-once certificate.

The freshest inputs are:

1. **fleet03/B18 arbitrary-q-flip three-local theorem** (`20260921T165709Z-qflip-three-local-lift`): arbitrary q-flip spectral parity and physical sensitivity triples have the sharp local transport bound; for the dependent triple `(u,v,u+v)` the exact transport distance is the derivative-disagreement kernel `p_u(v)` after the later fleet02 dictionary;
2. **fleet02/B18 dependent-triple/Radon theorem** (`20260921T170605Z-qflip-dependent-triple-radon-frame`): `W1(u,v,u+v)=p_u(v)` and every arbitrary pivot has a positive central Radon square;
3. **fleet03/B16 ordered physical flag theorem** (`20260921T175324Z-ordered-flag-physical-resolvent`): ordered-min q-flips with physical pivot `i` are exactly uniform subsets of the later-coordinate flag, and the random-order average is the Hardy multiplier `(I+D)^{-1}`. It proved the coarse source estimate `sum_i E p_i(W)^2 <= 2 J(f)`;
4. **fleet04/B16 correlated-noise double-resolvent theorem** (`20260921T181233Z-correlated-noise-double-resolvent`): the newest compiler object is already a **positive quadratic bank**
   \[
   \frac18\int\!\int\!\int\frac{1-y^2}{xy}
   \sum_j\langle D_j\Phi,N_xC_{y,\lambda}^{(j)}D_j\Phi\rangle,
   \]
   with signed R32 aggregation before squaring, both inverse numbers retained, singleton syndrome killed, and the terminal subtraction kept inside `Phi`. Its stated next obligation is to push this already-squared bank through the dependent-q-flip Radon/original-cut map.

The exact statement attempted here is therefore:

> **PHYSICAL FLAG SQUARE PAYMENT.** Can the physical q-flip source itself absorb a quadratic compiler bank without an `L^infinity` Radon--Nikodym domination or a generic endpoint `L2` estimate?

The answer is **yes on the source side, with constant one**. More strongly, every squared q-flip disagreement is reducible to its *linear* Radon first moment by the folded physical influence of the pivot. The remaining gap is no longer a source-square estimate; it is the specific positive contraction from the B16 clone-pair curvature bank into these physical dependent-face discrepancies.

The three deliberate `FLEET_RULES` moves are:

- **#11 DUALIZE:** diagonalize the ordered physical flag on the Fourier spectrum of the physical derivative indicator;
- **#25 COUNT THE SAME THING TWICE:** compute the flag second moment both directly as a symmetric-difference probability and by grouped Walsh energies, then average the coordinate order;
- **#20 FIND WHY THE ALGORITHM FAILS:** test and refute the tempting stronger estimate with no collision term, while replacing the already-refuted *generic* endpoint `L2` route by an exact Boolean-derivative `L2` theorem.

---

## 1. Physical q-flip source

Let
\[
f:\mathbb F_2^n\to\{-1,+1\}.
\]
For a physical coordinate `i`, define
\[
\eta_i(x):=\mathbf 1\{f(x)\ne f(x+e_i)\},
\qquad
\alpha_i:=\mathbb E\eta_i=\operatorname{Inf}_i(f),
\]
and its folded density
\[
\beta_i:=\min\{\alpha_i,1-\alpha_i\}.
\]
Write
\[
J(f):=\sum_i\beta_i\le I(f):=\sum_i\alpha_i.
\]

For a translation `w` with `w_i=0`, let
\[
p_i(w):=\Pr_x\{\eta_i(x)\ne\eta_i(x+w)\}.
\tag{1.1}
\]
This is exactly the dependent-triple spectral/physical transport distance for `(e_i,w,e_i+w)` from the compatible q-flip theorem.

Because replacing `eta_i` by its complement leaves every symmetric difference unchanged, and the smaller of the set and its complement has density `beta_i`,
\[
\boxed{0\le p_i(w)\le 2\beta_i\quad\text{for every }w.}
\tag{1.2}
\]
This elementary pointwise fact becomes powerful when combined with the exact Radon first moment.

---

## 2. PROVED — square-to-linear Radon principle

### Theorem 2.1 — `P03-B18-SQUARE-TO-LINEAR-RADON`

For **any** probability law `mu` on translations `w` with `w_i=0`,
\[
\boxed{
\mathbb E_{W\sim\mu}p_i(W)^2
\le
2\beta_i\,\mathbb E_{W\sim\mu}p_i(W).
}
\tag{2.1}
\]
The constant `2 beta_i` is pointwise sharp.

### Proof

Equation (1.2) gives pointwise
\[
p_i(w)^2\le2\beta_i p_i(w).
\]
Average under `mu`. `square`

### Sharpness

Take `f(x)=(-1)^{x_i x_j}` and `w=e_j`. Then `eta_i(x)=x_j`, so `beta_i=1/2` and `p_i(e_j)=1`. Equality holds in (2.1).

### Why this matters for the newest compiler

The fleet04/B16 object is already quadratic and positive after the authentic signed aggregation. Once one of its positive terms is pushed to a nonnegative mixture of **squared** physical dependent-face discrepancies, (2.1) converts that square back to the *linear* q-flip Radon profile. Thus the physical source does not require a generic endpoint `L2` norm bound.

---

## 3. PROVED — exact ordered-flag Plancherel identity

Fix a coordinate order `pi`. Let
\[
L_i^\pi=\{j:\pi(j)>\pi(i)\}
\]
and let `nu_i^pi` be the uniform law on all subsets of `L_i^pi`, identified with their translation vectors.

Since `eta_i(x+e_i)=eta_i(x)`, write its normalized nonconstant Walsh energies on the `i`-free quotient as
\[
a_i(U):=\widehat\eta_i(U)^2,
\qquad
E_i:=\sum_{U\ne\varnothing}a_i(U)
=\alpha_i(1-\alpha_i)
=\beta_i(1-\beta_i).
\tag{3.1}
\]

Group those energies by their trace on the later flag:
\[
A_{i,\pi}(V)
:=\sum_{U:\,U\cap L_i^\pi=V}a_i(U),
\qquad V\subseteq L_i^\pi,
\tag{3.2}
\]
and put
\[
T_{i,\pi}:=\sum_{V\ne\varnothing}A_{i,\pi}(V)
=\sum_{U:\,U\cap L_i^\pi\ne\varnothing}a_i(U).
\tag{3.3}
\]

For `W subseteq L_i^pi`, Fourier inversion gives
\[
\boxed{
p_i(W)
=2T_{i,\pi}
-2\sum_{V\ne\varnothing}A_{i,\pi}(V)(-1)^{V\cdot W}.}
\tag{3.4}
\]

Uniform flag characters are orthonormal. Hence:

### Theorem 3.1 — `P03-B18-ORDERED-FLAG-PLANCHEREL`

For every Boolean `f`, every order `pi` and every physical pivot `i`,
\[
\boxed{
\mathbb E_{W\sim\nu_i^\pi}p_i(W)=2T_{i,\pi},
}
\tag{3.5}
\]
\[
\boxed{
\mathbb E_{W\sim\nu_i^\pi}p_i(W)^2
=4T_{i,\pi}^2
+4\sum_{V\ne\varnothing}A_{i,\pi}(V)^2.
}
\tag{3.6}
\]

The second term is an exact **trace-collision energy**. It cannot in general be deleted.

### Proof

Average (3.4). Every nonconstant flag character has mean zero, giving (3.5). Square (3.4), average again, and use orthogonality of distinct flag characters. `square`

---

## 4. PROVED — constant-one physical flag square bank

Combining the general square-to-linear theorem (2.1) with the exact first moment (3.5),
\[
\mathbb E_{\nu_i^\pi}p_i(W)^2
\le4\beta_iT_{i,\pi}.
\tag{4.1}
\]
Since `T_{i,pi}<=E_i=beta_i(1-beta_i)`, and `0<=beta_i<=1/2`,
\[
4\beta_iT_{i,\pi}
\le4\beta_i^2(1-\beta_i)
\le\beta_i,
\tag{4.2}
\]
because `4 beta(1-beta)<=1` on `[0,1/2]`.

### Theorem 4.1 — `P03-B18-PHYSICAL-FLAG-SQUARE-BANK`

For **every fixed coordinate order**,
\[
\boxed{
\sum_i\mathbb E_{W\sim\nu_i^\pi}p_i(W)^2
\le J(f)
\le I(f).
}
\tag{4.3}
\]

This improves the previous ordered-flag source estimate `<=2J(f)` by a factor of two and, more importantly, identifies the correct mechanism: a quadratic physical q-flip bank is already paid directly by original-coordinate influence.

The coordinatewise constant in
\[
\mathbb E_{\nu_i^\pi}p_i(W)^2\le\beta_i
\tag{4.4}
\]
is sharp. Again take `f(x)=(-1)^{x_i x_j}` with `j` later than `i`. Then `eta_i=x_j`, `beta_i=1/2`, and `p_i(W)=1_{\{j\in W\}}`; therefore
\[
\mathbb E p_i(W)^2=\frac12=\beta_i.
\]
No constant below one can replace the right side of (4.4) universally.

A harmless finite-order refinement is also immediate: the last pivot in the order has empty later flag and contributes zero, so choosing the last coordinate to have maximal `beta_i` gives
\[
\sum_i\mathbb E p_i(W)^2
\le J(f)-\max_i\beta_i
\le\left(1-\frac1n\right)J(f).
\tag{4.5}
\]
This is not needed for dimension-free closure but explains the small-dimensional extremal numerics below.

---

## 5. PROVED — exact random-order Hardy collision kernel

The ordered flag already has the exact Hardy resolvent in first moment. Its **second moment** also has an exact inverse-number formula.

Let `Pi` be a uniform random coordinate order and then `W~nu_i^Pi`. For two nonempty `i`-free Walsh frequencies `U,V`, put
\[
u=|U|,\qquad v=|V|.
\]
There are two contributions in (3.6).

First,
\[
\Pr_\Pi(U\cap L_i^\Pi\ne\varnothing,
          V\cap L_i^\Pi\ne\varnothing)
=1-\frac1{u+1}-\frac1{v+1}
 +\frac1{|U\cup V|+1}.
\tag{5.1}
\]
This is inclusion--exclusion: `U` misses the later flag exactly when `i` is last among `{i} union U`.

Second, the two nonzero flag traces agree exactly when every coordinate of `U triangle V` lies before `i`, while at least one coordinate of `U cap V` lies after `i`. Hence
\[
\begin{aligned}
&\Pr_\Pi(U\cap L_i^\Pi=V\cap L_i^\Pi\ne\varnothing)\\
&\qquad=
\frac1{|U\triangle V|+1}
-\frac1{|U\cup V|+1}.
\end{aligned}
\tag{5.2}
\]

The `|U union V|` terms cancel between (5.1) and (5.2). Therefore:

### Theorem 5.1 — `P03-B18-RANDOM-FLAG-HARDY-COLLISION`

\[
\boxed{
\mathbb E_{\Pi,W}p_i(W)^2
=4\sum_{U,V\ne\varnothing}a_i(U)a_i(V)
\left[
1-\frac1{|U|+1}-\frac1{|V|+1}
+\frac1{|U\triangle V|+1}
\right].
}
\tag{5.3}
\]

The pair kernel is nonnegative and has the exact integral form
\[
\boxed{
K(U,V)=\int_0^1
\left(1-t^{|U|}-t^{|V|}+t^{|U\triangle V|}\right)dt\ge0.
}
\tag{5.4}
\]
Indeed, writing
\[
a=|U\setminus V|,\quad b=|V\setminus U|,\quad c=|U\cap V|,
\]
the integrand is
\[
1-t^{a+c}-t^{b+c}+t^{a+b}
\ge(1-t^a)(1-t^b)\ge0,
\]
since `t^c<=1`.

This is the quadratic analogue of the B16 Hardy resolvent: the physical flag square is itself a positive inverse-number **collision** form indexed by symmetric differences. It has the same structural language as the newest compiler-side positive correlation-flow/double-resolvent bank, instead of the exponential generic endpoint `L2` geometry that was previously refuted.

The square-to-linear form gives a simpler upper envelope. Since
\[
\mathbb E_\Pi T_{i,\Pi}
=\sum_{U\ne\varnothing}a_i(U)\frac{|U|}{|U|+1},
\tag{5.5}
\]
we have
\[
\boxed{
\mathbb E_{\Pi,W}p_i(W)^2
\le
4\beta_i\sum_{U\ne\varnothing}a_i(U)\frac{|U|}{|U|+1}
\le\beta_i.
}
\tag{5.6}
\]
Thus the exact Hardy high-pass multiplier survives the quadratic payment.

---

## 6. PROVED conditional compiler implication matching the newest B16 object

The newest fleet04/B16 bank is already a positive quadratic form after all required signed aggregation. The preceding theorem shows that the appropriate compiler interface is a **quadratic contraction**, not pointwise density domination.

### Theorem 6.1 — `P03-B18-DEPENDENT-FACE-L2-COMPILER-CRITERION`

Fix an ordered-min physical q-flip flag. Suppose a nonnegative post-refund compiler bank `Q` admits a representation or PSD domination
\[
\boxed{
\mathcal Q
\le A\sum_i
\mathbb E_{W\sim\nu_i^\pi}|z_i(W)|^2
}
\tag{6.1}
\]
with one dimension-free `A`, where for every `(i,W)`, `z_i(W)` is the expectation discrepancy of a **1-Lipschitz** observable between the spectral-parity and physical-sensitivity laws on the dependent q-flip triple
\[
(e_i,W,e_i+W).
\]
Then
\[
\boxed{
\mathcal Q\le A J(f)\le A I(f).
}
\tag{6.2}
\]

### Proof

For the dependent triple, the compatible q-flip theorem gives exact Hamming transport distance
\[
W_1=p_i(W).
\]
Kantorovich--Rubinstein duality therefore gives
\[
|z_i(W)|\le p_i(W).
\]
Insert this into (6.1) and then apply (4.3). `square`

For an `L`-Lipschitz observable, the right side is `A L^2 I(f)`.

### What this changes

The previous ordered-flag handoff asked for an absolute Radon--Nikodym density bound of the compiler source relative to the flag law. The latest compiler has since become a PSD curvature **square**. Theorem 6.1 shows that an `L2`/PSD contraction is enough; no `L^infinity` density estimate is needed.

This is a materially weaker and better-matched target. It also avoids the generic endpoint-`L2` counterexample: the physical dependent-face source is far from a generic selector function and obeys the sharp source inequality (4.4).

What remains **OPEN** is to prove (6.1) for the authentic B16 central curvature bank
\[
\frac18\int_{x,y\le1/2}\int_0^1
\frac{1-y^2}{xy}
\sum_j\langle D_j\Phi,
N_xC_{y,\lambda}^{(j)}D_j\Phi\rangle
\,d\lambda\,dy\,dx,
\]
with its actual Borel/MacWilliams coefficients, dual-code multiplicity, negative R32 credits, R16/moment refunds and terminal subtraction retained. No such compiler contraction is asserted here.

---

## 7. REFUTED stronger shortcut: delete the trace-collision term

One might hope that (3.6) can be strengthened to
\[
\mathbb E_{\nu_i^\pi}p_i(W)^2\le4T_{i,\pi}^2.
\tag{7.1}
\]
This is **false**.

For `f(x)=(-1)^{x_i x_j}` with `j` later than `i`, the derivative indicator is `eta_i=x_j`. Its only nonconstant Walsh energy is
\[
a_i(\{j\})=\frac14,
\qquad T_{i,\pi}=\frac14.
\]
But
\[
\mathbb E p_i(W)^2=\frac12,
\qquad
4T_{i,\pi}^2=\frac14.
\]
The ratio is exactly two. Equivalently, the collision term in (3.6) is as large as the square-of-mean term.

So the positive collision kernel (5.3) is genuine and cannot be discarded. The viable route is the square-to-linear inequality (2.1), not a fictitious cancellation of physical trace collisions.

---

## 8. Exact falsification computation

`check_flag_l2_source.py` uses only the Python standard library and exact `Fraction` arithmetic.

It verifies the exact fixed-order Plancherel identity, the strengthened source payment, and the random-order Hardy first-moment identity on all Boolean functions through dimension three. It then exhausts **every Boolean function and every coordinate order through dimension four** for the global source bound (4.3).

Counts:

- exact fixed-order flag identity cases: `4 + 64 + 4,608 = 4,676`;
- exact random-order Hardy identity cases: `4 + 32 + 768 = 804`;
- exhaustive Boolean-function/order source-bound cases through `n=4`: **1,574,436**.

The observed maxima of
\[
\frac{\sum_i\mathbb E p_i(W)^2}{I(f)}
\]
over all tested functions/orders are
\[
0,\quad \frac12,\quad \frac23,\quad \frac34
\]
for `n=1,2,3,4`, respectively. These finite maxima are not used as a theorem; they are consistent with the trivial last-coordinate refinement (4.5).

The checker also verifies the sharp coordinate example
\[
\beta_i=\frac12,
\quad T_i=\frac14,
\quad \mathbb E p_i^2=\frac12,
\]
and the factor-two refutation of (7.1).

Executed checker SHA-256:
`a0881bba4635519bec14a300c35e8347d2510e204f714a62a22bbb22f8d9b0c6`.

Archived stdout SHA-256:
`59d49aeacaf8eb96bd8c38aed1ee5a45ca040ced8b75916c032c672571beee3a`.

These computations are self-check/falsification evidence. The all-dimensional results above are proved algebraically.

---

## 9. Classification and next attack

### PROVED in this run

- universal square-to-linear q-flip Radon inequality `E p_i^2 <= 2 beta_i E p_i` for every translation law;
- exact fixed-order flag Plancherel identity (3.6), including the unavoidable trace-collision term;
- **constant-one physical flag square bank** `sum_i E p_i^2 <= J(f) <= I(f)` for every coordinate order;
- exact random-order Hardy collision kernel (5.3), a positive symmetric-difference inverse-number form;
- Hardy-preserving upper envelope (5.6);
- conditional dependent-face `L2` compiler criterion: a dimension-free PSD contraction of the authentic central compiler into dependent-face observable squares immediately pays by physical influence.

### REFUTED in this run

- the stronger collision-free bound `E p_i^2 <= 4 T_i^2`; the two-variable monomial phase misses it by factor two;
- consequently one cannot remove the physical trace-collision term and pretend the square is just the square of the linear Radon first moment.

### OPEN

- prove the actual PSD contraction (6.1) from fleet04/B16's retained Borel/MacWilliams clone-pair curvature bank to the ordered physical dependent-face bank, preserving signed equal-syndrome aggregation, the terminal subtraction, dual-code multiplicity, R16/moment refunds and the central `x,y<=1/2` cutoff;
- pay the high/endpoint complement using its already-reserved R16/moment and terminal mechanisms;
- unrestricted FEI.

### Next attack

Start from one authentic central integrand
\[
\langle D_j\Phi,N_xC_{y,\lambda}^{(j)}D_j\Phi\rangle
\]
with `x,y<=1/2`. Expand **only its marked clone pair `j`** through the retained MacWilliams/Borel representation and keep the other noise operators as Markov contractions. The target is not a pointwise density. The target is to show that the resulting quadratic form is a positive contraction of the dependent-face discrepancy squares indexed by the ordered physical flag. If successful, Theorem 6.1 pays that whole central term by `J(f)` with no ambient-dimension loss. If this contraction fails on an authentic R32 packet, preserve the packet and switch to the exact Hardy collision kernel (5.3), comparing the compiler multiplier directly against
\[
1-\frac1{|U|+1}-\frac1{|V|+1}+\frac1{|U\triangle V|+1}.
\]

**Full FEI remains OPEN / NOT PROVED.**
