# B18 FEI synthesis: character-invariant folded cooling and an activation-refunded crossing compiler

**Status:** **PARTIAL / new proved universal auxiliary potential + proved conditional compiler.** Full uniform-cube Friedgut--Kalai Fourier entropy--influence (FEI) remains **OPEN / NOT PROVED**.

**Route:** APPROACH 11/12 synthesis: physical restriction / decision-tree entropy payment + restricted-potential dual.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. No authenticated brain retrieval/context was available or claimed. No novelty or publication-priority claim is made.

## 1. Fresh compatible inputs actually consumed

This run changes mechanism because the preceding B18 target was killed by a newer peer result.

1. **account03/B12**, `proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260921T211211Z-ordered-parent-flag-nonreuse/REPORT.md`, blob `a76cd2ab5c03546c421c9c004cfeae3f12b1e7a9`, gives an explicit Boolean bent family for which the preceding B18 unconditional remainder
   \[
   R_{\rm pref}=I\,\mathrm{TC}(P)-\mathbb E\log_2(K!)
   \]
   is not `O(I)`. It repairs the prefix code by conditioning on the stopping level `T=|P|` and proves the exact stop-conditioned tensorization. Therefore the old B18 target `R_pref=O(I)` is **REFUTED** and is not pursued here.

2. **account04/B14**, `proofnet24/P03-fei/fleet-2026-09-21/account04/B14/20260921T201002Z-dimension-cooling-activation/REPORT.md`, blob `8923525f8e010e372837cdfc44fd629ba3510f8a`, proves the fixed-gauge activation potential
   \[
   P_z(f)=\sum_S\widehat f(S)^2\Phi_z(|S|),\qquad
   \Phi_z(k)=1+z+\cdots+z^{k-1},
   \]
   its exact physical block drop, and the monotone-scale telescope. Its important limitation for the present F/J critical-core programme is explicit: the telescope is stated after choosing one root character gauge and then not re-gauging descendants.

3. **account02/B14**, `proofnet24/P03-fei/fleet-2026-09-21/account02/B14/20260921T210915Z-crossing-information-selector/REPORT.md`, blob `673dbf5d2bc162fc43b7931e88a5449fce2a219a`, proves the physical crossing inequality
   \[
   I_A\ge \frac12\log_2\frac{1-p_j}{p_j}\,c_j(A)
   \]
   and, for `p_j<=1/4`, the Shannon payment
   \[
   c_j(A)\ge\gamma p_j
   \Longrightarrow
   h_2(p_j)\le\frac{9}{2\gamma}I_A.
   \]
   It also proves the `(gamma,K)` certificate compiler with unrefunded corrected erasure.

The present result resolves the gauge-compatibility issue in item 2 and then inserts the resulting **globally paid folded activation reserve** into item 3's certificate compiler.

## 2. Normalization

Let
\[
f:\{0,1\}^n\to\{-1,+1\},\qquad
p_S=\widehat f(S)^2,
\]
and let `X` denote the Fourier spectral sample with `Pr(X=S)=p_S`. Put
\[
p_i=\Pr(i\in X),\qquad
j_i=\min(p_i,1-p_i),\qquad
\mathcal J(f)=\sum_i j_i.
\]
Multiplication by a character `chi_T` shifts the spectral law by symmetric difference `S -> S triangle T`; hence `H(f)` and `J(f)` are character invariant.

For `0<=z<=1` define
\[
\Phi_z(0)=0,\qquad
\Phi_z(k)=\sum_{r=0}^{k-1}z^r\quad(k>=1),
\]
with `Phi_1(k)=k`.

For a character gauge `T subseteq[n]` set
\[
P_z^T(f):=
\sum_S p_S\,\Phi_z(|S\triangle T|).
\tag{2.1}
\]
The new folded activation potential is
\[
\boxed{
\mathcal A_z(f):=\min_{T\subseteq[n]}P_z^T(f).
}
\tag{2.2}
\]

## 3. PROVED: the folded activation potential is character invariant and costs at most J

### Theorem 3.1
For every Boolean `f` and `0<=z<=1`:

\[
\boxed{
0\le\mathcal A_z(f)\le\mathcal J(f),
\qquad
\mathcal A_1(f)=\mathcal J(f).
}
\tag{3.1}
\]
Moreover `A_z(f)` is nondecreasing in `z` and invariant under multiplication by an arbitrary character.

### Proof

Character multiplication by `chi_R` replaces `p_S` by `p_{S triangle R}`. In (2.2), changing variables and replacing `T` by `T triangle R` leaves the minimum unchanged.

For every `k`, `Phi_z(k)` is nonnegative, nondecreasing in `z`, and at most `k`. Therefore the minimum in (2.2) is nondecreasing in `z` and nonnegative.

At `z=1`,
\[
P_1^T(f)=\mathbb E|X\triangle T|
=\sum_i \Pr(1_{i\in X}\ne1_{i\in T}).
\]
The minimization separates coordinatewise: include `i` in `T` exactly when `p_i>1/2` (ties arbitrary). Thus
\[
\mathcal A_1(f)=\sum_i\min(p_i,1-p_i)=\mathcal J(f).
\]
Since `Phi_z(k)<=k`, evaluating (2.2) at an `A_1`-minimizing median character gives `A_z<=J`. QED.

This is the first useful point: unlike the fixed-gauge potential, `A_z` can be re-centered independently at every physical descendant without changing its meaning.

## 4. PROVED: physical block drop survives arbitrary re-gauging

Fix a physical block `A subseteq[n]`, a scale `z`, and choose **any** minimizer `T_*` of (2.2). Define
\[
\Lambda_{A,z}^{T_*}(f)
:=
\sum_S p_S\,
 z^{|(S\triangle T_*)\setminus A|}
 \Phi_z(|(S\triangle T_*)\cap A|).
\tag{4.1}
\]
(At `z=0` use the continuous/polynomial convention coming from the displayed finite sum.)

### Theorem 4.1 — folded block activation
For uniform physical restriction `f_{A=a}`,
\[
\boxed{
\mathcal A_z(f)-\mathbb E_a\mathcal A_z(f_{A=a})
\ge
\Lambda_{A,z}^{T_*}(f)
\ge0.
}
\tag{4.2}
\]

### Proof

Apply the exact fixed-gauge block identity from account04/B14 to `g=f chi_{T_*}`. Restricting the coordinates in `A` turns the queried part of `chi_{T_*}` into a sign depending on `a`; on the surviving coordinates the inherited character is `T_*\setminus A`. Hence
\[
P_z^{T_*}(f)
-
\mathbb E_a P_z^{T_*\setminus A}(f_{A=a})
=
\Lambda_{A,z}^{T_*}(f).
\tag{4.3}
\]
By definition of the folded child potential,
\[
\mathcal A_z(f_{A=a})
\le P_z^{T_*\setminus A}(f_{A=a}).
\]
Also `P_z^{T_*}(f)=A_z(f)` because `T_*` is a parent minimizer. Substitute these two facts into (4.3). QED.

The inequality direction is crucial: allowing each child to choose a **better** character center can only make the parent-to-child activation drop larger. Thus re-centering is not a leakage term; it is a refund.

## 5. PROVED: adaptive cooling telescope with free descendant re-centering

Consider any finite physical block-restriction tree. At node `u` let the current function be `f_u`, its reach probability be `w_u`, its queried block be `A_u`, and choose a scale `z_u`. Suppose every child `v` obeys
\[
z_v\le z_u.
\tag{5.1}
\]
Choose an arbitrary minimizer `T_u` for `A_{z_u}(f_u)` and put
\[
\Lambda_u:=\Lambda_{A_u,z_u}^{T_u}(f_u).
\]

### Theorem 5.1 — folded adaptive activation budget
\[
\boxed{
\sum_{u\ {m internal}}w_u\Lambda_u
\le
\mathcal A_{z_{\rm root}}(f)
\le
\mathcal J(f).
}
\tag{5.2}
\]

### Proof

By monotonicity in `z`, for every child `v`,
\[
\mathcal A_{z_v}(f_v)\le\mathcal A_{z_u}(f_v).
\]
Therefore Theorem 4.1 gives
\[
\mathcal A_{z_u}(f_u)-\mathbb E_{v\mid u}\mathcal A_{z_v}(f_v)
\ge
\Lambda_u.
\tag{5.3}
\]
Multiply by `w_u` and sum over internal nodes. The left side telescopes to the root potential minus a nonnegative leaf average. Apply (3.1). QED.

This is a strict compatibility improvement over the consumed fixed-gauge cooling theorem: **each descendant may now choose its own optimal character gauge**, yet the entire activation bank is still charged only once, to the root folded influence `J`.

## 6. PROVED: dimension cooling retains a pointwise folded reserve

Let `d` be the number of still-unqueried physical coordinates and choose
\[
z_d=1-\frac1d\quad(d>=1).
\tag{6.1}
\]
For any parent minimizer `T_*` and any surviving coordinate `i`, let
\[
q_i^{T_*}:=\Pr(i\in X\triangle T_*).
\]
Then `q_i^{T_*}` is either `p_i` or `1-p_i`, so `q_i^{T_*}>=j_i`.

For a singleton block,
\[
\Lambda_{\{i\},z_d}^{T_*}
=
\sum_{S:\ i\in S\triangle T_*}
 p_S z_d^{|S\triangle T_*|-1}.
\]
Since `|S triangle T_*|<=d`,
\[
\boxed{
\Lambda_{\{i\},z_d}^{T_*}
\ge
\left(1-\frac1d\right)^{d-1}q_i^{T_*}
\ge e^{-1}j_i.
}
\tag{6.2}
\]
The `d=1` case is interpreted directly and is stronger.

More generally, whenever `(S triangle T_*) cap A` is nonempty, the factor in (4.1) is at least `z_d^{d-1}`. Therefore
\[
\boxed{
\Lambda_{A,z_d}^{T_*}
\ge
e^{-1}\Pr\big((X\triangle T_*)\cap A\ne\varnothing\big).
}
\tag{6.3}
\]

Thus the tensor-padding advantage of dimension cooling survives **even after optimal per-state character re-centering**. The one-use total budget is `J`, not the ordinary influence in a frozen gauge.

## 7. Integrating the folded bank with the crossing compiler

Use the established corrected entropy potential
\[
\mathcal C(f)=\sum_i\mathfrak j(j_i),
\qquad
\mathcal F(f)=H(f)-\mathcal C(f),
\]
where the inherited scalar bound is
\[
0\le\mathcal C(f)\le\frac2{\ln2}\mathcal J(f).
\tag{7.1}
\]
For a physical block `A`, write the exact corrected decrement and folded drift as
\[
E_A:=\mathcal F(f)-\mathbb E_a\mathcal F(f_{A=a})=B_A-Q_A,
\qquad Q_A\ge0,
\tag{7.2}
\]
\[
D_A:=\mathcal J(f)-\mathbb E_a\mathcal J(f_{A=a})=J_A+C_A,
\qquad J_A=\sum_{i\in A}j_i.
\tag{7.3}
\]

For a fixed `lambda>=0`, at a state with `d` unqueried physical coordinates define the **activation-refunded potential**
\[
\boxed{
\mathcal G_\lambda(f)
:=
\mathcal F(f)-\lambda\mathcal A_{z_d}(f).
}
\tag{7.4}
\]
This quantity is character invariant.

When block `A` is restricted and children use their smaller dimension-cooling scales, define the true adaptive folded activation drop
\[
T_A
:=
\mathcal A_{z_d}(f)
-
\mathbb E_a\mathcal A_{z_{d_a}}(f_{A=a}),
\tag{7.5}
\]
where `d_a<=d-|A|`. By Theorem 5.1,
\[
T_A\ge\Lambda_{A,z_d}^{T_*}\ge0.
\tag{7.6}
\]
Hence
\[
\Delta_A\mathcal G_\lambda
=E_A-\lambda T_A
\le E_A-\lambda\Lambda_{A,z_d}^{T_*}.
\tag{7.7}
\]

## 8. PROVED conditional theorem: activation-refunded Shannon crossing certificates imply full FEI

Let
\[
\rho_*:=4h_2(1/4)=3.245112497836531\ldots.
\]

### Definition 8.1 — `(gamma,K,lambda)` folded cooling certificate
At a centered physical state, a block/survivor pair `(A,j)`, `j notin A`, is a certificate if
\[
\boxed{c_j(A)\ge\gamma j_j}
\tag{8.1}
\]
and, for a minimizer `T_*` of the folded activation potential at the current dimension-cooling scale,
\[
\boxed{
E_A-\lambda\Lambda_{A,z_d}^{T_*}
\le K h_2(j_j).
}
\tag{8.2}
\]
Only one pair is required. This is strictly weaker than the unrefunded account02/B14 condition when `lambda>0`.

### Theorem 8.2 — folded activation-refunded compiler
Fix universal constants `gamma>0`, `K<infinity`, `lambda>=0`. Suppose every nonconstant physical-restriction core maximizing `G_lambda/J` with ratio larger than `rho_*` admits a certificate (8.1)--(8.2). Then for every Boolean function
\[
\boxed{
H(f)
\le
\left[
\max\left\{\rho_*,\frac{9K}{2\gamma}\right\}
+\lambda+rac2{\ln2}
\right] I(f).
}
\tag{8.3}
\]
In particular full FEI follows.

### Proof

Take a physical restriction descendant maximizing the positive ratio
\[
\rho=\frac{\mathcal G_\lambda}{\mathcal J};
\]
characters may be re-centered freely because both numerator and denominator are character invariant. If no descendant has positive numerator, the final bound is immediate.

Ratio maximality implies for every physical block
\[
\Delta_A\mathcal G_\lambda\ge\rho D_A.
\tag{8.4}
\]
For a singleton `i`, (7.7) and `Q_i>=0` give
\[
\rho D_i
\le\Delta_i\mathcal G_\lambda
\le E_i
\le B_i
\le h_2(j_i).
\]
Since `D_i>=j_i`,
\[
h_2(j_i)\ge\rho j_i.
\tag{8.5}
\]
Thus if `rho>rho_*`, monotonicity of `h_2(x)/x` on `(0,1/2]` forces every active `j_i<1/4`.

Choose the assumed certificate `(A,j)`. The consumed account02/B14 crossing-to-Shannon theorem, applied in the centered character gauge, yields
\[
h_2(j_j)
\le\frac9{2\gamma}J_A
\le\frac9{2\gamma}D_A.
\tag{8.6}
\]
On the other hand, (7.7), (8.2), and criticality (8.4) give
\[
\rho D_A
\le\Delta_A\mathcal G_\lambda
\le K h_2(j_j)
\le\frac{9K}{2\gamma}D_A.
\]
Positive crossing implies `D_A>0`, so
\[
\rho\le\frac{9K}{2\gamma}.
\]
Therefore every descendant ratio, and in particular the root ratio, is at most
\[
C_0=\max\left\{\rho_*,\frac{9K}{2\gamma}\right\}.
\]
Using `A_{z_d}<=J` and (7.1),
\[
H
=\mathcal G_\lambda+\lambda\mathcal A_{z_d}+\mathcal C
\le
\left(C_0+\lambda+\frac2{\ln2}\right)\mathcal J
\le
\left(C_0+\lambda+\frac2{\ln2}\right)I.
\]
QED.

## 9. What changed, and the exact remaining arrow

### PROVED this run

- The folded activation potential `A_z=min_T P_z(f chi_T)` is character invariant, satisfies `A_1=J` and `A_z<=J`.
- Its physical block decrement dominates the exact fixed-gauge activation computed in **any parent minimizing gauge**.
- Arbitrary descendant re-centering is compatible with the nonincreasing-scale telescope; the whole bank is paid once by root `J`.
- Dimension cooling still gives the local reserve `Lambda_i>=e^{-1}j_i` after this minimization.
- The activation-refunded crossing certificate compiler (8.3) is valid.

### REFUTED / retired input

The preceding B18 target `R_pref=O(I)` is refuted by the consumed account03/B12 bent family. The stop-conditioned replacement remains compatible but is not needed to prove Theorem 8.2.

### OPEN

The new universal obligation is now strictly weaker than account02/B14's unrefunded certificate existence problem:

> On every high-`G_lambda/J` primitive core, find one physical `(A,j)` with
> \[
> c_j(A)\ge\gamma j_j,
> \qquad
> E_A\le K h_2(j_j)+\lambda\Lambda_{A,z_d}^{T_*}
> \]
> for fixed universal `gamma,K,lambda`, or force a complementary already-paid branch.

The extra term is not bookkeeping: by Theorem 5.1 it is a genuine nonreused resource whose total tree expenditure is at most root `J`, and unlike the consumed fixed-gauge version it is compatible with the per-descendant character centering required by the crossing/critical-core argument.

A natural next attack is a **minimal posterior-crossing block**: try to prove that the part of `E_A` unrelated to the target survivor is bounded by a universal multiple of the folded activation drop `Lambda_A`; the survivor's logarithmic rarity is then paid by the crossing theorem. If false, an exact Boolean counterexample to this refunded certificate would identify the next missing resource.

**Full FEI remains OPEN / NOT PROVED.**
