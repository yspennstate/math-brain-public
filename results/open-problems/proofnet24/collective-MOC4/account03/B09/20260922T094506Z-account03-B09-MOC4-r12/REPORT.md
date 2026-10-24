# account03/B09 MOC4 report — one genuine complementary cofactor certifies a full support-direction chamber

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T094506Z-account03-B09-MOC4-r12`  
**Assignment:** derive an inequality exploiting the special complementary `2 x 2` minors in dimension four and apply it to the determinant-support expression  
**Named partner:** `account04/B07`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Source-bound state and exact peer use

The target is the exact complex-normal `4 x 4` Marcus-de Oliveira inclusion
\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\},
\]
including singular and repeated spectra.

The current campaign lead, account03/B07 run
`20260922T074824Z-account03-B07-MOC4-r13`, proves that a mixed-Schur pair
kernel at a hypothetical positive-gap support maximizer is a full-Hessian
kernel and derives
\[
q+3R_{\rm pair}+3R_{\rm cross}\le 0.
\]
The current account03/B20 synthesis
`20260922T084401Z-account03-B20-MOC4-r11` turns this into explicit adjacent-root
budget gates
\[
3N_\epsilon(R)\le 2\Lambda(T-\epsilon C),\qquad \epsilon=\pm1.
\]
Those are still not universally paid.

The required named OTHER-account input used here is account04/B07 run
`20260922T071214Z-account04-B07-MOC4-r14`,
`MOC4-MIXED-SCHUR-SVD-PAYMENT-v1`.  Its exact genuine-Spin(4) formulas
\[
\sqrt A\,r_1+\sqrt B\,s_1=0
\]
and
\[
\delta\ge \frac{r_1^2}{B}
+\frac{A r_2^2+2\sigma_2r_2s_2+B s_2^2}{AB-\sigma_2^2}
\]
confirm that the live obstruction must respect one common unitary; no
independently selected bistochastic or compound-minor data may be substituted.

The preceding B09 run changed mechanism from local edge/face purges to a
quartic polarization of one genuine complementary-minor cofactor over an
entire support-positive outer slice.  It certified one support direction.
This run tests whether that mechanism is stable on a nontrivial continuous
support chamber rather than repeating another local face enumeration.

## 2. Fixed spectra and one-parameter support family

Retain the exact spectra from the preceding structured stress test:
\[
a=(4+2i,-2+3i,-2i,-3-2i),
\]
\[
b=(-4-4i,-2i,1+2i,-3+3i).
\]
For real `t`, define
\[
L_t(x+iy)=\operatorname{Re}((1+i(-1+t))(x+iy))
=x+(1-t)y.
\]

For the 24 permutation products, exact affine-envelope calculation gives
\[
M_t:=\max_{\sigma\in S_4}L_t\!\left(\prod_i(a_i+b_{\sigma(i)})\right)
=
\begin{cases}
240-248t,&-5/157\le t\le0,\\
240+8t,&0\le t\le1/10,\\
236+48t,&1/10\le t\le8/65.
\end{cases}
\tag{2.1}
\]

In the same 72-vertex normalized-Saxl outer representation used in the
preceding B09 certificate, the unique potentially dangerous non-Weyl atom is
\[
e_*=e_{\tau,\rho'},\qquad
\tau=(2,3,0,1),\quad \rho'=(1,2,0),
\]
with affine support
\[
E_t=L_t(e_*)=\frac{740}{3}-\frac{116}{3}t.
\tag{2.2}
\]
Every other outer vertex lies at or below `M_t` throughout each of the three
intervals in (2.1).  Moreover
\[
E_t>M_t\quad\Longleftrightarrow\quad -\frac5{157}<t<\frac8{65}.
\tag{2.3}
\]
The exact gaps are
\[
\Delta_t:=E_t-M_t=
\begin{cases}
(20+628t)/3,&-5/157<t\le0,\\
(20-140t)/3,&0\le t\le1/10,\\
(32-260t)/3,&1/10\le t<8/65.
\end{cases}
\tag{2.4}
\]

Thus this is a genuine chamber in which the outer relaxation falsely permits
positive support while the permutation roof changes twice.

## 3. The fixed genuine cofactor

Use the same even-even spinor gauge `r=c=000` and omitted row/column `0` as in
the preceding run.  For the corresponding `q^-` block put
\[
T_0=1-P_{00},\qquad
a_0=T_0-\sum_jq^-_{0j},\qquad
b_0=T_0-\sum_iq^-_{i0},
\]
\[
c=q^-_{11},\quad d=q^-_{22},\quad e=q^-_{12},\quad f=q^-_{21}.
\]
The dimension-four complementary-minor identity gives the genuine-unitary
necessary condition
\[
\boxed{F=(a_0b_0-cd-ef)^2-4cdef\le0.}
\tag{3.1}
\]
At the dangerous outer atom,
\[
F(e_*)=\frac1{81}>0.
\tag{3.2}
\]

Let `z(v)=(a_0,b_0,c,d,e,f)` denote these six linear cofactor forms at an outer
point `v`.

## 4. Perspective slice for every `t`

Fix `t` with `E_t>M_t`.  Write the other 71 outer vertices as `v_j`, and set
\[
s_j(t)=\lambda_j(t)e_*+(1-\lambda_j(t))v_j,\qquad
\lambda_j(t)=\frac{M_t-L_t(v_j)}{E_t-L_t(v_j)}.
\tag{4.1}
\]
Then `L_t(s_j(t))=M_t`, and exactly as in the preceding perspective lemma,
\[
V\cap\{L_t\ge M_t\}
=\operatorname{conv}\{e_*,s_1(t),\dots,s_{71}(t)\}.
\tag{4.2}
\]
If `x` is in this slice, its coefficient of `e_*` in the perspective
coordinates is
\[
\beta_0=\frac{L_t(x)-M_t}{E_t-M_t}
       =\frac{L_t(x)-M_t}{\Delta_t}.
\tag{4.3}
\]

In cofactor-form coordinates,
\[
z(s_j(t))
=\frac{n_j(t)}{E_t-L_t(v_j)},\qquad
n_j(t)=\bigl(M_t-L_t(v_j)\bigr)z(e_*)
       +\bigl(E_t-M_t\bigr)z(v_j).
\tag{4.4}
\]
The denominator is positive in the chamber.  On each interval of (2.1),
`n_j(t)` is affine in `t`.

At the two outer endpoints, where `E_t=M_t`,
\[
n_j(t)=\bigl(M_t-L_t(v_j)\bigr)z(e_*),
\tag{4.5}
\]
a nonnegative multiple of the dangerous vector.  Therefore the only
nontrivial affine knots are `t=0` and `t=1/10`.

## 5. New exact theorem — `MOC4-B09-TWO-KNOT-CROSS-BLOSSOM-v1`

Let `mathcal F` be the symmetric four-linear polarization of the quartic
`F`; explicitly, with
\[
h(z,w)=\tfrac12(a(z)b(w)+a(w)b(z)-c(z)d(w)-c(w)d(z)-e(z)f(w)-e(w)f(z)),
\]
\[
q(z,w)=\tfrac12(c(z)d(w)+c(w)d(z)),\qquad
r(z,w)=\tfrac12(e(z)f(w)+e(w)f(z)),
\]
one has
\[
\begin{aligned}
\mathcal F(z_1,z_2,z_3,z_4)
={}&\frac13(h_{12}h_{34}+h_{13}h_{24}+h_{14}h_{23})\\
&-\frac23(q_{12}r_{34}+q_{13}r_{24}+q_{14}r_{23}
+q_{23}r_{14}+q_{24}r_{13}+q_{34}r_{12}).
\end{aligned}
\tag{5.1}
\]

Define the two 72-element knot sets
\[
\mathcal N_0=\{z(e_*),n_1(0),\dots,n_{71}(0)\},
\]
\[
\mathcal N_1=\{z(e_*),n_1(1/10),\dots,n_{71}(1/10)\}.
\]

### Theorem

For every multiset of four vectors chosen from
`\mathcal N_0\cup\mathcal N_1`,
\[
\boxed{\mathcal F(w_1,w_2,w_3,w_4)\ge0.}
\tag{5.2}
\]

After clearing each vector's own positive rational denominator, the exact C++
verifier checks all
\[
\binom{144+4-1}{4}=18,671,940
\]
unordered quadruples using signed 128-bit integer arithmetic.  It finds
`508,792` exact zeros and minimum positive cleared numerator `2`.  The
certificate vectors are reconstructed independently by a Fraction-only Python
builder from the spectra, the 24 Weyl vertices, the 48 external vertices, and
the exact roof chambers; their deterministic vector digest is
`1dda464713aaad31ac90f9ecb15a94143a472cd5110af5edcd84e633930eccc4`.

### Why two knots certify the full interval

For a fixed generator quadruple and one of the three roof intervals, each
argument `n_j(t)` is affine in the normalized interval parameter.  Hence
\[
p(t)=\mathcal F(n_i(t),n_j(t),n_k(t),n_l(t))
\]
is a degree-at-most-four polynomial whose degree-four Bernstein coefficients
are averages of the sixteen cross-endpoint four-linear values obtained by
choosing each argument at the left or right endpoint.

On the middle interval `[0,1/10]`, all endpoint vectors belong to
`\mathcal N_0\cup\mathcal N_1`, so every such cross value is nonnegative by
(5.2).  On the left interval `[-5/157,0]`, equation (4.5) makes every left
endpoint vector a nonnegative multiple of `z(e_*)`, which is already in both
knot sets; multilinearity reduces every endpoint cross value to (5.2).
Exactly the same argument applies on `[1/10,8/65]`.

Therefore
\[
\boxed{
\mathcal F(w_i(t),w_j(t),w_k(t),w_l(t))\ge0
}
\tag{5.3}
\]
for every support-slice generator quadruple and every
\[
-\frac5{157}\le t\le\frac8{65}.
\]

## 6. Target-facing consequence: MOC4 support bound on the whole chamber

For interior `t` and any `x\in V` with `L_t(x)\ge M_t`, expand `x` in the
perspective generators (4.2).  By (5.3), every quartic Bernstein coefficient
in this expansion is nonnegative.  Retaining only the pure `e_*^4` term and
using (3.2)-(4.3) gives
\[
\boxed{
F(x)\ge
\frac{(L_t(x)-M_t)^4}{81\,\Delta_t^4}.
}
\tag{6.1}
\]

A genuine `4 x 4` unitary must satisfy the complementary-minor annulus
`F(x)\le0`.  Consequently
\[
\boxed{L_t(x)\le M_t}
\tag{6.2}
\]
for every genuine unitary and every
\[
-\frac5{157}<t<\frac8{65}.
\]
At the two boundary values `t=-5/157,8/65`, the dangerous outer value already
equals the permutation roof and every outer vertex is at or below it, so
(6.2) holds there as well.

Thus, for the fixed nontrivial complex spectra above, MOC4 is proved in the
entire closed continuum of support directions
\[
\boxed{-5/157\le t\le8/65}
\]
with the exact piecewise endpoint roof (2.1).  This is not a grid statement:
it is a finite exact certificate plus a Bernstein interpolation argument.

## 7. Relation to the live universal obstruction

This result does **not** prove MOC4 for arbitrary spectra or support directions,
and it does not universally pay the lead's `R_cross` residual budget.  Its
role is sharper: it establishes that the special complementary-minor
cofactor/blossom mechanism survives a genuine support chamber containing two
changes of the active spectral permutation, and it removes the entire
support-positive outer relaxation on that chamber before any mixed-Schur
branch analysis is needed.

The next B09 implication remains
`MOC4-COFACTOR-BLOSSOM-CHAMBER-COVER-v2`:

> Replace the fixed one-parameter spectra/support line by symbolic chamber
> inequalities in spectral/support coefficient space.  Determine conditions
> under which at least one of the 144 genuine cofactor quartics has a
> nonnegative cross-knot blossom on the support-positive Saxl slice.  Route
> uncovered chambers to `MOC4-MSQR-STRUCTURED-RESIDUAL-BUDGET-v1` rather than
> returning to local edge enumeration.

A failure of this certificate in another chamber would refute only this proof
mechanism, not MOC4, unless accompanied by an actual true unitary whose
determinant support separates from all 24 spectral products.

## 8. Verification status

The exact builder reconstructs all source data with `fractions.Fraction`,
checks the three affine permutation roofs, checks that every non-dangerous
outer atom stays below the roof on each chamber, checks the two outer
collapses (4.5), and emits the two 72-vector knot sets.

The exact C++ verifier evaluates all `18,671,940` unordered four-vector
polarization values after positive denominator clearing.  Its observed result:
`PASS`, `508,792` zeros, minimum positive integer numerator `2`.

No arbitrary bistochastic data, paid model/API/Codex, remote workflow,
cross-account native action, public posting, email, Drive, credentials, or
benchmark gold was used.

**Status:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED /
NOT DISPROVED**.
