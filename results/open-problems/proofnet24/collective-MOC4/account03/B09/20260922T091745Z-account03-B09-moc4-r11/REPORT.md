# account03/B09 MOC4 report — a single complementary-minor cofactor closes an entire nontrivial support slice

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Assignment:** exploit the special complementary `2 x 2` minors in dimension four and apply the resulting genuine-unitary inequality to determinant support  
**Named partner:** `account04/B07`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Fresh source-bound state and peer consumption

The target is the exact complex-normal `4 x 4` Marcus-de Oliveira inclusion

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\},
\]

including singular and repeated spectra.

The current campaign lead `account03/B07` (`20260922T074824Z-account03-B07-MOC4-r13`) proves that a mixed-Schur pair kernel at a hypothetical positive-gap global support maximizer is a full-Hessian kernel and introduces the exact cross-split reserve

\[
q+3R_{\rm pair}+3R_{\rm cross}\le0.
\]

The newer account03/B20 synthesis (`20260922T084401Z-account03-B20-MOC4-r11`) converts part of `R_cross` into explicit adjacent-root residual budget inequalities and leaves `MOC4-MSQR-STRUCTURED-RESIDUAL-BUDGET-v1` open.

The required named OTHER-account partner consumed here is `account04/B07`, run `20260922T071214Z-account04-B07-MOC4-r14`, theorem `MOC4-MIXED-SCHUR-SVD-PAYMENT-v1`.  On a genuine mixed-Schur Spin(4) block it obtains

\[
\sqrt A\,r_1+\sqrt B\,s_1=0
\]

and

\[
\delta\ge \frac{r_1^2}{B}
+\frac{A r_2^2+2\sigma_2r_2s_2+B s_2^2}{AB-\sigma_2^2},
\]

with the corresponding double-singular alignment limit.  This confirms that the live obstruction is a same-unitary compatibility problem, not an arbitrary bistochastic one.

The preceding B09 run closed all two-vertex outer mixtures involving a non-Weyl external Saxl atom.  Rather than perform a third local face enumeration, this run changes mechanism: it polarizes one genuine cofactor-annulus polynomial over the **entire support-positive slice** of the 72-vertex normalized-Saxl outer polytope.

## 2. The fixed genuine-unitary cofactor

Use the even-even spinor gauge `r=c=000` from `MOC4-SPINOR-COFACTOR-IDENTITY-v1`.  In this gauge the relevant `3 x 3` squared-modulus block is `B=q^-`.  Put

\[
t^2=1-P_{00},
\qquad
a=t^2-\sum_j B_{0j},
\qquad b=t^2-\sum_i B_{i0},
\]

and abbreviate

\[
c=B_{11},\quad d=B_{22},\quad e=B_{12},\quad f=B_{21}.
\]

For every true `4 x 4` unitary, the special dimension-four spinor cofactor identity gives

\[
ab=\left|N_{11}N_{22}-N_{12}N_{21}\right|^2.
\]

Consequently the phase-free annulus condition is exactly

\[
\boxed{
F:=(ab-cd-ef)^2-4cdef\le0.
}\tag{2.1}
\]

This is a necessary condition on one genuine unitary.  No independently selected stochastic or compound-minor array appears.

## 3. A structured support direction on which the outer Saxl bound genuinely fails

Retain the earlier exact B09 stress spectra, written as Gaussian pairs,

\[
a=(4+2i,-2+3i,-2i,-3-2i),
\]

\[
b=(-4-4i,-2i,1+2i,-3+3i),
\]

and the real support functional

\[
L(z)=\operatorname{Re}((1-i)z).
\]

For the 24 permutation products

\[
f_\sigma=L\!\left(\prod_i(a_i+b_{\sigma(i)})\right),
\]

exact enumeration gives

\[
M:=\max_{\sigma\in S_4}f_\sigma=240.
\tag{3.1}
\]

In the complete 72-vertex normalized-Saxl outer representation, however, one non-Weyl external atom has the strictly larger value

\[
E=\frac{740}{3}>240,
\tag{3.2}
\]

and every other outer vertex has value at most `240`.  Thus the plain outer-polytope relaxation is insufficient in this direction: it predicts a false external excess of `20/3`.

The unique dangerous external atom is

\[
e_*=e_{\tau,\rho'},\qquad
\tau=(2,3,0,1),\quad \rho'=(1,2,0)
\]

in the zero-based conventions of the exact verifier.

## 4. Exact support-slice reduction

Let `V=conv{e_*,v_1,...,v_71}` be the 72-vertex outer polytope and write

\[
L(v_j)=M-d_j,\qquad d_j\ge0,
\qquad E-M=\Delta=\frac{20}{3}.
\]

On the segment from `e_*` to `v_j`, let

\[
s_j=\lambda_j e_*+(1-\lambda_j)v_j,
\qquad
\lambda_j=\frac{d_j}{\Delta+d_j}.
\tag{4.1}
\]

Then `L(s_j)=M`.

### Lemma — exact perspective description of the positive support slice

\[
\boxed{
V\cap\{L\ge M\}=\operatorname{conv}\{e_*,s_1,\ldots,s_{71}\}.
}
\tag{4.2}
\]

Moreover, if

\[
x=\alpha_0 e_*+\sum_j\alpha_jv_j,
\qquad \alpha_j\ge0,\quad \sum_j\alpha_j=1,
\]

and `L(x)>=M`, then

\[
x=\beta_0 e_*+\sum_j\beta_js_j
\]

with

\[
\beta_j=\alpha_j\frac{\Delta+d_j}{\Delta},
\qquad
\beta_0=\alpha_0-\frac1\Delta\sum_j\alpha_jd_j
       =\frac{L(x)-M}{\Delta}.
\tag{4.3}
\]

All `beta` are nonnegative and sum to one.  Hence `L(x)>M` if and only if `beta_0>0`.

### Proof

Matching the `v_j` coefficients in `sum beta_j s_j` gives the displayed `beta_j`.  The required remaining coefficient at `e_*` is exactly the expression in (4.3), which is nonnegative precisely because `L(x)>=M`.  Direct summation gives total weight one.  The reverse inclusion is immediate because all generators have support at least `M`. `QED`

## 5. Quartic blossom certificate

The six quantities `a,b,c,d,e,f` in (2.1) are affine-linear functions of the outer coordinates.  On barycentric coordinates they may therefore be treated as linear forms, and

\[
F=(ab-cd-ef)^2-4(cd)(ef)
\]

is a homogeneous quartic.

For two points `z,w`, define the symmetric bilinear forms

\[
h(z,w)=\frac12\{a(z)b(w)+a(w)b(z)-c(z)d(w)-c(w)d(z)-e(z)f(w)-e(w)f(z)\},
\]

\[
q(z,w)=\frac12\{c(z)d(w)+c(w)d(z)\},
\qquad
r(z,w)=\frac12\{e(z)f(w)+e(w)f(z)\}.
\]

The symmetric four-linear polarization of `F` is

\[
\begin{aligned}
\mathcal F(z_1,z_2,z_3,z_4)
={}&\frac13\bigl(
 h_{12}h_{34}+h_{13}h_{24}+h_{14}h_{23}
\bigr)\\
&-\frac23\bigl(
q_{12}r_{34}+q_{13}r_{24}+q_{14}r_{23}
+q_{23}r_{14}+q_{24}r_{13}+q_{34}r_{12}
\bigr).
\end{aligned}
\tag{5.1}
\]

Thus `F(z)=mathcal F(z,z,z,z)`.

### Theorem — `MOC4-STRUCTURED-ONE-COFACTOR-BLOSSOM-CERTIFICATE-v1`

For the 72 support-slice generators in (4.2),

\[
\boxed{
\mathcal F(w_i,w_j,w_k,w_l)\ge0
\quad\text{for every multiset }\{i,j,k,l\}.
}
\tag{5.2}
\]

Here `w_0=e_*` and `w_1,...,w_71=s_1,...,s_71`.  In addition,

\[
\mathcal F(e_*,e_*,e_*,e_*)=F(e_*)=\frac1{81}.
\tag{5.3}
\]

The finite statement (5.2) contains

\[
\binom{72+4-1}{4}=1,215,450
\]

rational inequalities.  The exact standard-library verifier checks every one using `Fraction` arithmetic.  There are `64,895` zeros; every remaining coefficient is positive, with minimum positive value

\[
\frac{81}{38416}.
\tag{5.4}
\]

No floating-point sign decision is used.

### Consequence — quantitative support/cofactor incompatibility

If `x` belongs to the outer polytope and `L(x)>=240`, write it as in (4.3).  Expanding the homogeneous quartic in Bernstein form gives

\[
F(x)=\sum_{|\nu|=4}\binom4\nu\,
\mathcal F(w^\nu)\,\beta^\nu.
\]

Every coefficient is nonnegative by (5.2).  The pure `e_*^4` term therefore yields

\[
F(x)\ge \frac{\beta_0^4}{81}.
\]

Since `Delta=20/3` and `beta_0=(L(x)-240)/Delta`, this simplifies exactly to

\[
\boxed{
F(x)\ge \frac{(L(x)-240)^4}{160000}
\qquad (L(x)\ge240).
}
\tag{5.5}
\]

A genuine unitary must simultaneously satisfy the cofactor annulus `F<=0`.  Hence

\[
\boxed{L(x)\le240}
\tag{5.6}
\]

for every genuine unitary in this structured spectral/support direction.

This closes the **entire** false support-positive region of the 72-vertex outer relaxation with one complementary-minor cofactor; it is not merely an edge or three-atom exclusion.

## 6. Direct implication for MOC4 research

The stress direction was deliberately nontrivial: the normalized-Saxl outer relaxation itself has value `740/3`, strictly above the true permutation endpoint bound `240`.  Equation (5.5) shows exactly how same-unitary dimension-four compatibility removes that false excess.

Therefore this specific generic structured support direction cannot host a MOC4 counterexample, regardless of which mixed-Schur/negative-definite differential branch a putative maximizing unitary would occupy.  In particular, any hypothetical positive-gap unitary would have `L>240`, whence (5.5) forces `F>0`, contradicting the genuine cofactor identity before the lead's remaining cross-residual budget is even reached.

This does **not** prove MOC4 for arbitrary spectra/support directions.  The live universal first missing implication remains the lead/B20 structured residual-budget closure.  What is new is a fully target-facing model certificate: a single fixed cofactor plus quartic polarization can dominate an entire support-positive Saxl slice, including all mixtures with arbitrarily many outer atoms.

The natural next B09 task is `MOC4-COFACTOR-BLOSSOM-CHAMBER-COVER-v1`: characterize the structured spectral/support chambers in which one of the 144 genuine cofactor polynomials has nonnegative degree-four blossom on the corresponding support-positive outer slice.  A finite chamber cover would close support directly; any uncovered chamber should then be handed to the mixed-Schur residual-budget machinery rather than repeating local edge enumeration.

## 7. Verification and status

Exact verifier: `verify_one_cofactor_blossom.py`.  It reconstructs all 24 Weyl and 48 external outer vertices, independently checks `M=240`, the unique external maximum `740/3`, builds the 72 exact support-slice generators, evaluates all `1,215,450` degree-four blossom coefficients in rational arithmetic, and verifies (5.3)-(5.5).

Captured exact output is stored in `VERIFICATION.txt`.

**Status:** `ESSENTIAL_STEP_APPLIED`.  Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  No arbitrary bistochastic data, paid model/API/Codex, cross-account native action, or public workflow was used.
