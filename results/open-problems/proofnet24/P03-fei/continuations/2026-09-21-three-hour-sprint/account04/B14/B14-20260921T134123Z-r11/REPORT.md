# B14 — exact erasure payment for arbitrary disjoint-clause DNFs

**Run:** `B14-20260921T134123Z-r11`  
**Role:** FEI erasure and selector proof  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** **PARTIAL / proved a larger hereditary selector theorem. Full uniform-cube FEI remains OPEN / NOT PROVED.**  
**Publication priority:** **UNVERIFIED**; no novelty claim is made.

This run follows `FEI-SEVEN-TASKS-2026-09-21` and the active sprint assignment for account04/B14. It starts from the exact restriction-fibre identity already present in the P03 state,
\[
\Delta_iH=B_i+JS_i,
\]
with fibre profile
\[
\Psi(t)=h_2(t)+j(t),\qquad
j(t)=1-h_2\!\left(\frac12+\sqrt{t(1-t)}\right),
\]
and the proved tangent bound
\[
j(t)\le \frac{2}{\ln2}\min(t,1-t).
\]
The preceding B14 run proved hereditary payment for the complete restriction closure of **width-two** tribes. The new step removes the equal-width assumption entirely: every monotone read-once DNF with arbitrary disjoint clause widths has an exact one-coordinate payment depending only on the width of the chosen clause and that coordinate's influence. A one-dimensional concavity certificate then gives a uniform **every-coordinate** restriction payment with constant `6.096` inside this structured hereditary class.

This does **not** revive a universal every-coordinate conjecture. Known obstructions to prescribed/every-coordinate payment in general Boolean functions remain untouched. The theorem here is only for disjoint-clause DNFs and their physical restrictions.

## 1. Hereditary class

Let
\[
F(x)=\bigvee_{r=1}^m\ \bigwedge_{j\in C_r} x_j,
\]
where the clauses `C_r` are pairwise disjoint and may have arbitrary positive sizes `k_r=|C_r|`.

This class is hereditary under physical restrictions: fixing a variable to `0` kills its clause; fixing it to `1` shortens its clause by one; satisfying a singleton makes the whole function constant. Thus every nonconstant descendant is again a disjoint-clause DNF.

Write
\[
d_r=1-2^{-k_r},\qquad q=\prod_r d_r.
\]
For the usual `±1` encoding, the nonempty Fourier coefficients factor blockwise. If a nonempty Fourier label `S` meets exactly the clause set `R`, then
\[
\boxed{
|\widehat f(S)|=2q\prod_{r\in R}\frac1{2^{k_r}-1}.
}
\tag{1}
\]
Indeed `1-F=\prod_r(1-A_r)` with `A_r` the clause indicator; the constant Fourier coefficient of `1-A_r` is `d_r`, while every nonempty local coefficient has magnitude `2^{-k_r}`.

## 2. Exact coordinate law

Fix a relevant coordinate `i` lying in a clause of width `k`. Define
\[
a_k=2^{1-k},\qquad m_k=2^k-1,\qquad D_k=m_k^2+1,
\]
and let
\[
p=\operatorname{Inf}_i(f).
\]
If `q_-` is the probability that every *other* clause fails, then
\[
p=2^{-(k-1)}q_-=a_kq_-,
\]
so in particular
\[
0<p\le a_k.
\tag{2}
\]
Also
\[
q=\frac{m_k}{2}p.
\tag{3}
\]

Erase the coordinate `i` from the Fourier label and pair the two masses in each fibre. There are exactly three types.

1. **The residual label contains another variable from the same clause.** Both Fourier labels activate the clause and their squared masses are equal. The total `i`-present mass in these fibres is `(1-a_k)p`, hence their total fibre mass is `2(1-a_k)p`.

2. **The residual label avoids the chosen clause but activates another clause.** Adding `i` activates the chosen clause, so the squared-mass ratio is `m_k^2:1`. The total smaller (`i`-present) mass of these fibres is
\[
a_kp-p^2.
\]
Thus their total fibre mass is `D_k(a_kp-p^2)` and their minor fraction is `1/D_k`.

3. **The empty fibre.** By (3), its two squared masses are
\[
(1-m_kp)^2\qquad\text{and}\qquad p^2.
\tag{4}
\]

Let
\[
F_\phi(x,y)=(x+y)\phi\!\left(\frac{y}{x+y}\right)
\]
for any symmetric profile `\phi`. The exact erasure term is therefore
\[
\boxed{
B_{k}(p)
=2(1-a_k)p
+D_kh_2(1/D_k)(a_kp-p^2)
+F_{h_2}((1-m_kp)^2,p^2).
}
\tag{5}
\]
The exact recombination term is
\[
\boxed{
JS_{k}(p)
=2(1-a_k)p
+D_kj(1/D_k)(a_kp-p^2)
+F_{j}((1-m_kp)^2,p^2).
}
\tag{6}
\]
Hence the full restriction-entropy decrement is
\[
\boxed{
\Delta_iH
=4(1-a_k)p
+K_k(a_kp-p^2)
+F_{\Psi}((1-m_kp)^2,p^2),
}
\tag{7}
\]
where
\[
K_k:=D_k\Psi(1/D_k).
\]
Equation (7) is exact and depends on the rest of the DNF only through the single scalar `p`.

For `k=2`, (5) specializes to the width-two tribes formula from the preceding B14 run. Thus the earlier theorem was one slice of (7), not a special accident of equal clause sizes.

## 3. A universal scalar envelope for this class

Set
\[
x=(1-m_kp)^2,\qquad y=p^2.
\]
The binary entropy part of the exceptional fibre obeys
\[
(x+y)h_2\!\left(\frac{y}{x+y}\right)
=y\log_2(1+x/y)+x\log_2(1+y/x)
\le p^2\log_2(1+p^{-2})+\frac{p^2}{\ln2},
\tag{8}
\]
because `x<=1` and `x log_2(1+y/x)<=y/ln 2`.

The inherited tangent bound gives
\[
(x+y)j\!\left(\frac{y}{x+y}\right)
\le \frac{2}{\ln2}\min(x,y)
\le \frac{2p^2}{\ln2}.
\tag{9}
\]
Combining (7)--(9),
\[
\frac{\Delta_iH}{p}\le U_k(p),
\tag{10}
\]
where
\[
\boxed{
U_k(p)=4(1-a_k)+K_k(a_k-p)
+p\log_2(1+p^{-2})+\frac{3p}{\ln2}.
}
\tag{11}
\]

The important fact is that every `U_k` is strictly concave on `(0,1)`:
\[
\boxed{
U_k''(p)=\frac{2(p^2-1)}{\ln2\,p(1+p^2)^2}<0.
}
\tag{12}
\]
The clause width enters only through the affine part of (11).

## 4. Scalar certificate: `sup U_k < 6.096`

The attached script `disjoint_dnf_selector_cert.py` evaluates `k=1,...,7` with outward interval arithmetic (`mpmath.iv`, 60 decimal digits). For each `k` it chooses a decimal point `p_0` near the unique stationary point. By concavity, the tangent at `p_0` is a global upper bound on the full interval `0<p<=a_k`; the code encloses both `U_k(p_0)` and `U'_k(p_0)` and then takes the worst endpoint of that tangent.

The certified tangent upper bounds are:

| `k` | upper bound on `sup_{0<p<=a_k} U_k(p)` |
|---:|---:|
| 1 | 5.352788869320870 |
| 2 | **6.095344045232610** |
| 3 | 5.636576985640779 |
| 4 | 5.088412199359908 |
| 5 | 4.674010751320553 |
| 6 | 4.400680223586702 |
| 7 | 4.231880648121361 |

For the infinite tail `k>=8` no numerical interval search is needed. For `0<t<=1/2`,
\[
h_2(t)\le t\log_2(1/t)+\frac{t}{\ln2},\qquad
j(t)\le\frac{2t}{\ln2},
\]
so
\[
K_k\le\log_2D_k+\frac3{\ln2}.
\]
Since `p<=a_k<=1/128`, the function `p log_2(1+p^{-2})` is increasing on this range. Also
\[
\log_2D_k<2k,
\qquad
\log_2(1+a_k^{-2})<2k-1.
\]
Therefore
\[
U_k(p)
<4+a_k\left(4k+\frac3{\ln2}-5\right).
\tag{13}
\]
The right side decreases for `k>=8`; at `k=8` it is
\[
4.244750665020835.
\]
Thus (11)--(13) give the uniform statement
\[
\boxed{
\frac{\Delta_iH}{\operatorname{Inf}_i(f)}<6.096
}
\tag{14}
\]
for **every relevant coordinate of every disjoint-clause DNF**.

The certificate output is saved verbatim in `disjoint_dnf_selector_cert.out`; its finite-`k` maximum is `6.095344045232610` at the `k=2` envelope.

## 5. Hereditary selector theorem

### Theorem

Let `f` be any monotone Boolean DNF whose clauses are pairwise disjoint and nonempty. For every relevant coordinate `i`,
\[
\boxed{
\Delta_iH(f)<6.096\,\operatorname{Inf}_i(f).
}
\tag{15}
\]
Every nonconstant physical restriction descendant remains in the same class, so ordinary restriction induction yields
\[
\boxed{
H(f)<6.096\,I(f).
}
\tag{16}
\]
for the entire hereditary class.

**Proof.** Equation (15) is (14). Under restriction the class is closed. The standard identities
\[
H(f)=\Delta_iH(f)+\frac{H(f_0)+H(f_1)}2,
\qquad
I(f)=p_i+\frac{I(f_0)+I(f_1)}2
\]
then induct on the number of relevant variables. QED.

This is stronger than the sprint's requested *existential* selector inside this class: every coordinate pays. It does **not** assert an every-coordinate inequality outside this class, and therefore does not conflict with the known general counterexamples that motivated the existential formulation.

## 6. Direct Walsh support and separate `H/I`

The attached checker also evaluates five nonuniform clause patterns directly from truth tables,

`[1,3]`, `[2,3]`, `[4]`, `[1,2,3]`, `[2,2,3]`,

and compares the actual restriction decrement with (7) at every coordinate. The maximum absolute discrepancy is
\[
6.661\times10^{-16}.
\]
This is only a check of the algebra; the proof of (7) is the blockwise Fourier calculation above.

As required by the sprint, the global entropy ratio is kept separate from the local induction ratio. For those five examples, respectively, `H/I` is approximately
\[
1.36099,\ 2.46423,\ 3.40248,\ 2.47064,\ 2.62371,
\]
whereas the largest local `\Delta_iH/p_i` in the same examples is approximately
\[
4.74223,\ 4.69141,\ 4.74223,\ 5.30984,\ 4.10547.
\]
Neither list is used in the proof of the universal class bound.

## 7. Why this matters for the full selector route

The exact formula (7) isolates a useful structural principle that is weaker than the previous width-two `9:1` fibre law:

> **If the nonempty Fourier fibres decompose into block-activation classes with a clause-width-dependent fixed odds ratio, then the entire restriction payment collapses to a scalar function of the influence.**

The full FEI route does not have such exact block factorization, but the mass-weighted calculation suggests a next universal target. Instead of trying to bound every fibre individually, seek a coordinate for which the distribution of fibre log-odds is dominated, in the `w_T`-weighted sense, by a mixture of the disjoint-clause templates. The exceptional fibre can already be paid by the universal quadratic estimate (8)--(9). What remains is to control the nonempty-fibre odds dispersion.

A precise next lemma to try is therefore an **existential mass-weighted odds selector**: find `i` such that
\[
\sum_{T\ne\varnothing}w_T\Psi(s_T)
\]
is bounded by the same influence budget as a convex mixture of fixed-odds clause fibres, with no claim for a prescribed coordinate. The all-shift Boolean orthogonality identities from the earlier critical-core work are a plausible source of the required average control.

## Claim ledger

**PROVED here**
- exact formulas (5)--(7) for arbitrary disjoint clause widths;
- strict concavity (12) of the scalar envelope;
- analytic tail bound (13);
- with the attached interval certificate for `k<=7`, the every-coordinate bound (15) with constant `6.096`;
- hereditary restriction-induction consequence (16).

**COMPUTATIONAL SUPPORT**
- outward interval tangent certificate: global envelope upper bound `6.095344045232610`;
- direct Walsh checks on five nonuniform families, maximum absolute formula discrepancy `6.661e-16`.

**NOT CLAIMED**
- a universal every-coordinate selector;
- a proof of full FEI;
- an improved universal FEI constant;
- publication priority or novelty.

Full uniform-cube FEI remains **OPEN / NOT PROVED**.
