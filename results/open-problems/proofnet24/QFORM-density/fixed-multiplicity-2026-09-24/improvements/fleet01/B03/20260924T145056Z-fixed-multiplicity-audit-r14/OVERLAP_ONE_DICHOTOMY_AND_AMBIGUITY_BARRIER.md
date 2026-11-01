# B03 improvement r14 — an overlap-one structural dichotomy at thirteen directions, and a sharp copy-sum energy barrier

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T145056Z-fixed-multiplicity-audit-r14`  
Pinned baseline: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **new exact structural reduction proved; a tempting retained-copy endpoint compiler is disproved in the arbitrary-density class; no unconditional reduction of the bounded-density threshold below 17 is claimed.**

The baseline audit is sound. At thirteen spectral directions, all pivot branches already have bounded densities, while the no-pivot branch produces order-four crossing volume and the critical `1/|t|` Fourier endpoint. This note sharpens the remaining no-pivot obstruction into a concrete overlap-one minor energy and records why the most direct copy-sum `L^2` attempt to pay that overlap is invalid for fragmented supports.

## 1. A full-residual interpolation identity

Use the manuscript notation

\[
V_r(A)=\sum_{\substack{S,T\subset[n],\ |S|=|T|=r\\S\cap T=\varnothing}}
\det(A_{S,T})^2.
\]

For a nonsingular disjoint `r`-seed `(S,T)`, write

\[
B=A_{S,T},\qquad L=[n]\setminus(S\cup T),\qquad
P=A_{\cdot,T}B^{-1}A_{S,\cdot}.
\]

The manuscript separates only the off-diagonal part of `A_{L,L}-P_{L,L}`. Here keep the **entire** residual

\[
C=A_{L,L}-P_{L,L}.
\tag{1}
\]

Let `E` be the matrix supported on `L x L` with `E_{L,L}=C`, and put `R=A-E`. Then

\[
R_{L,L}=P_{L,L},
\tag{2}
\]

and, exactly as in the manuscript's completion lemma, `R-P` vanishes on rows `S`, columns `T`, and the full `L x L` block. Every possible remaining entry therefore lies in rows `T` or columns `S`. Hence

\[
\boxed{\operatorname{rank}R\le3r.}
\tag{3}
\]

This version uses no diagonal matrix `D`; it is designed to retain the diagonal residual as an overlap-one minor currency.

## 2. Overlap-one bordered-minor energy

Define

\[
U_r(A)=
\sum_{\substack{S,T\subset[n],\ |S|=|T|=r,\ S\cap T=\varnothing\\
                  \det A_{S,T}\ne0}}
\ \sum_{i\notin S\cup T}
\det\bigl(A_{S\cup\{i\},\,T\cup\{i\}}\bigr)^2.
\tag{4}
\]

The row and column `(r+1)`-sets in (4) overlap in the single physical coordinate `i`; this is why `U_r` is not a sub-sum of the disjoint volume `V_{r+1}`.

For every nonsingular seed, the same bordered determinant calculation as in the manuscript gives, now also on the diagonal,

\[
\det\bigl(A_{S\cup\{i\},T\cup\{i\}}\bigr)^2
=\det(B)^2\,|A_{ii}-P_{ii}|^2.
\tag{5}
\]

The sign from sorting indices disappears after squaring.

## 3. Main structural theorem

### Theorem — disjoint-next-order or overlap-one energy

Let `A=A^T` and let `r>=1`. Assume

\[
V_r(A)>0,
\qquad
s_{3r+1}(A)\ge1.
\]

Then

\[
\boxed{
U_r(A)+(r+1)^2V_{r+1}(A)\ge V_r(A).
}
\tag{6}
\]

#### Proof

Fix any nonsingular disjoint `r`-seed and construct `R,E` above. Since `A=R+E` and `rank R<=3r`, the nonsymmetric rank perturbation inequality from the manuscript gives

\[
1\le s_{3r+1}(A)\le s_1(E)=\|E\|=\|C\|.
\]

Thus every nonsingular seed satisfies

\[
\|C\|_F^2\ge1.
\tag{7}
\]

Now sample nonsingular seeds with probability `det(B)^2/V_r(A)`, exactly as in the manuscript. Decompose the Frobenius norm into diagonal and off-diagonal parts. By (5), the weighted expected diagonal contribution is exactly

\[
\frac{U_r(A)}{V_r(A)}.
\tag{8}
\]

For the off-diagonal contribution, the manuscript's volume-sampling proof applies verbatim: every disjoint `(r+1,r+1)` minor is counted at most `(r+1)^2` times, while singular seeds carry zero sampling weight. Hence

\[
\mathbb E\|\operatorname{offdiag}C\|_F^2
\le
(r+1)^2\frac{V_{r+1}(A)}{V_r(A)}.
\tag{9}
\]

Averaging (7) and using (8)–(9) yields

\[
1\le
\frac{U_r}{V_r}+(r+1)^2\frac{V_{r+1}}{V_r},
\]

which is (6). QED.

### Remarks on hypotheses

- No no-pivot hypothesis is needed for (6).
- No symmetry of the auxiliary `R` or `P` is needed; the manuscript's singular-value rank inequality is exactly the correct tool.
- The result is deterministic. It does not invoke probability laws, density regularity, or rotated-coordinate independence.

## 4. Exact thirteen-direction consequence

Return to the normalized manuscript regime `K=s=1`, with

\[
\eta=1/100,
\qquad
\kappa=80^{-2}.
\]

Assume `A` has **no** `eta`-pivot and

\[
s_{13}(A)\ge1.
\tag{10}
\]

The audited baseline proposition with `k=4` gives

\[
V_4(A)\ge\kappa^4.
\tag{11}
\]

Apply (6) with `r=4`; its spectral hypothesis is exactly `s_{13}>=1`. Then

\[
\boxed{
U_4(A)+25V_5(A)\ge V_4(A)\ge\kappa^4.
}
\tag{12}
\]

Therefore there is a clean dichotomy:

\[
\boxed{
V_5(A)\ge V_4(A)/50
}
\tag{13a}
\]

or

\[
\boxed{
U_4(A)\ge V_4(A)/2\ge\kappa^4/2.
}
\tag{13b}
\]

The first branch already has a bounded continuous density using only the manuscript's existing order-five receiver. Indeed a fair coordinate cut yields

\[
Z_5\ge4^{-5}V_5
\ge 4^{-5}\kappa^4/50,
\]

and hence

\[
\boxed{
\|p_Q\|_\infty
\le 5e\,(4^5\,50\,\kappa^{-4})^{1/10}
=10e\,50^{1/10}80^{4/5}
<1339.
}
\tag{14}
\]

Thus, after the already-paid pivot branches are included, the **only new structural debt for an unconditional thirteen-eigenvalue bounded-density theorem is the no-pivot overlap-heavy branch (13b)**. This is strictly sharper than saying merely that order four is a critical Fourier endpoint.

For clarity: this does **not** prove the thirteen-eigenvalue theorem. `U_4` can be distributed over many overlap-one packets, and a dimension-free analytic receiver for the aggregate energy is still missing.

## 5. The retained copy-sum transform and the tempting endpoint step

The preceding B03 run retained the true dependence between a copied coordinate's difference and sum. For one original cap-one density `f`, put

\[
D=X-X',\qquad S=X+X',
\]

with joint density

\[
h(d,s)=\frac12
f\!\left(\frac{s+d}{2}\right)
 f\!\left(\frac{s-d}{2}\right).
\tag{15}
\]

Let

\[
g(d)=\int h(d,s)\,ds
\]

be the difference density and

\[
H(d,\xi)=\int e^{i\xi s}h(d,s)\,ds.
\tag{16}
\]

Then

\[
\int|H(d,\xi)|^2d\xi\le\pi g(d),
\tag{17}
\]

which is a valid unnormalized ambiguity-energy estimate.

It is tempting to normalize by the difference law,

\[
A(d,\xi)=H(d,\xi)/g(d)
\quad(g(d)>0),
\tag{18}
\]

observe `|A|<=1`, and hope for a universal averaged conditional energy

\[
\int g(d)\int|A(d,\xi)|^2d\xi\,dd\le C.
\tag{19?}
\]

If (19?) were true, one could combine one same-bank overlap frequency with the order-four crossing determinant by Cauchy–Schwarz and apparently manufacture the missing endpoint power. **This step is false under the manuscript's hypotheses.**

## 6. Fragmented-support counterexample to normalized ambiguity energy

### Proposition — no universal bound in (19?)

For every `N>=2`, there is a probability density `0<=f_N<=1` such that

\[
\int g_N(d)\int|A_N(d,\xi)|^2d\xi\,dd
\ge 2\pi(N-1).
\tag{20}
\]

Hence the left side of (19?) is unbounded over cap-one probability densities.

#### Construction and proof

Let `ell=1/N` and choose intervals

\[
I_j=[3^j,3^j+\ell],
\qquad j=1,\ldots,N,
\]

and set

\[
f_N=\sum_{j=1}^N\mathbf1_{I_j}.
\tag{21}
\]

The intervals are disjoint, each has length `ell`, so `f_N` is a probability density bounded by one.

For distinct ordered pairs `(j,k)`, the center differences `3^j-3^k` are distinct: equality of two such differences forces equality of the smaller exponent by the 3-adic valuation, and then equality of the larger exponent. They are separated by at least one integer unit, while each difference cluster below has radius `ell<=1/2`. Thus the off-diagonal difference clusters are disjoint up to endpoints.

Fix `j!=k` and write

\[
d=(3^j-3^k)+\delta,
\qquad |\delta|<\ell.
\]

On this cluster exactly the pair `I_j x I_k` contributes. A direct change from `(x,x')` to `(d,s)` gives

\[
g_N(d)=\ell-|\delta|=:q>0,
\tag{22}
\]

while, conditional on this `d`, the sum coordinate `S` is uniform on an interval of length `2q`. Hence its conditional density is `1/(2q)`, and by Plancherel

\[
\int|A_N(d,\xi)|^2d\xi
=2\pi\int\left(\frac1{2q}\right)^2\mathbf1_{\text{interval length }2q}\,ds
=\frac\pi q.
\tag{23}
\]

Multiplying by `g_N(d)=q` gives exactly `pi` for every interior point of this cluster. The cluster has length `2ell`, so each ordered pair `j!=k` contributes `2pi ell`. Summing the `N(N-1)` disjoint off-diagonal clusters yields

\[
N(N-1)\,2\pi\ell=2\pi(N-1),
\]

proving (20). The diagonal-difference cluster contributes a further nonnegative amount and is irrelevant. QED.

## 7. Consequence for the B03 endpoint programme

The counterexample is not a counterexample to the fixed-multiplicity density theorem. It invalidates a **specific intermediate shortcut**:

> after copying a coordinate, one may not normalize the retained sum transform by the difference density and then assume a law-uniform `L^2` energy in the sum frequency averaged over the difference.

Equivalently, the true pair `(D,S)` must remain coupled. The valid bound (17) is unnormalized; dividing by `g(d)` costs precisely the fragmented-support geometry that can grow without bound.

This explains why the seemingly natural Cauchy–Schwarz splice

- order-four crossing determinant from the difference variables, plus
- one normalized retained same-bank ambiguity factor

cannot by itself prove the thirteen-eigenvalue `L^infinity` theorem under arbitrary cap-one densities.

The structural dichotomy (12)–(13) remains valid and useful. It says that a successful unconditional `17 -> 13` proof can now focus on one of two genuinely new mechanisms:

1. an **aggregate overlap-one receiver** for `U_4` that never divides by the difference density, or
2. a stronger algebraic reduction converting large `U_4` into an already-paid pivot/grouped-coordinate configuration while preserving original-coordinate product provenance.

A support-length, connected-support, smoothness, moment, or log-concavity hypothesis would repair some normalized-energy bounds, but such an assumption is forbidden for the owner target and is not introduced here.

## 8. Multiplicity ledger after this run

- Baseline arbitrary-law bounded-density candidate: **17 directions, unchanged and audited PASS by this worker**.
- Thirteen directions, pivot branch: **bounded density already paid by the baseline pivot arguments**.
- Thirteen directions, no pivot, `V_5>=V_4/50`: **bounded continuous density <1339**, proved above.
- Thirteen directions, complementary no-pivot branch: **large overlap-one energy `U_4>=kappa^4/2`**, unresolved.
- Normalized copy-sum conditional-energy shortcut: **FALSE**, with explicit cap-one fragmented-support counterexample.
- Full unrestricted three-eigenvalue conjecture: **OPEN**.

No Gaussian, compact-support requirement (the counterexample happens to be compactly supported only because it is an obstruction example), connected-support, moment, log-concavity, diagonal-basis, or post-rotation independence assumption is used in the positive results.
