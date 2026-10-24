# MOC4 account03/B20 — exact global Spin(4) product-orbit / trust-region gate

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** Marcus–de Oliveira, complex normal `4 x 4` case (`MOC4`)  
**Run:** `20260922T064515Z-account03-B20-MOC4-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Source-exact state used

The target remains

\[
\det(D_a+UD_bU^*)\in\operatorname{conv}\left\{
\prod_i(a_i+b_{\sigma(i)}):\sigma\in S_4
\right\}
\]
for every true `4 x 4` unitary `U` and all complex spectra, including repeated and singular cases.

The newest complete account03 lead report read in this run is account03/B07 `20260922T060726Z-account03-B07-MOC4-r11`, theorem `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`. Its prior input `MOC4-MIXED-CONFORMAL-HESSIAN-GATE-v1` gives, for every complementary pair split, the genuine four-real-dimensional local Hessian condition

\[
\|M\|_{\rm op}^2\le4(T^2-C^2).
\]

The exact assigned OTHER-account partner result consumed and applied is account04/B09 `20260922T060924Z-b09-moc4-r12`, `MOC4-ROOT-SATURATION-EXCLUSION-v1`. It proves that a support-violating genuine global maximizer cannot saturate any elementary pair gate: for every complementary split both Spin(4) factors are strictly curved, equivalently `T>|C|`. Thus the surviving branch is genuinely strict and the next target-level problem is `MOC4-STRICT-SPIN6-SIX-WITNESS-v2`.

This report directly strengthens that strict branch. The prior Hessian gate is only a second-order condition. Here the entire commuting `SU(2) x SU(2)` product orbit is solved exactly, and its global-maximality condition is reduced to one scalar trust-region inequality on `S^2`, equivalently a `4 x 4` positive-semidefinite certificate with one real multiplier.

## 2. Exterior-power support and the complementary Spin(4) orbit

For a real support functional `h(U)=Re(eta det(D_a+UD_bU*))`, Cauchy–Binet gives

\[
h(U)=\operatorname{Re}\eta\sum_{k=0}^4\sum_{|I|=|J|=k}
a_{I^c}b_J\,|\det U[I,J]|^2.\tag{1}
\]

Fix a complementary row partition, say `{1,2}|{3,4}`. Let the two disjoint embedded groups `SU(2)_{12}` and `SU(2)_{34}` act on the left. They commute. Left diagonal phases commute with `D_a`, hence leave (1) invariant, so each factor descends from `SU(2)` to its Bloch sphere `S^2=SU(2)/U(1)`.

Write the two Bloch variables as `n,m in S^2` and let `f(n,m)` be the restriction of `h` to this genuine-unitary product orbit through the present `U`.

### Theorem 1 — `MOC4-SPIN4-BIAFFINE-ORBIT-v1`

There are uniquely determined real data

\[
c\in\mathbb R,\quad p,q\in\mathbb R^3,\quad Z\in\mathbb R^{3\times3}
\]
such that

\[
\boxed{f(n,m)=c+p\cdot n+q\cdot m+n^T Zm.}\tag{2}
\]

#### Proof

Every term in (1) is a squared compound minor. Under the chosen row split:

- degrees `k=0,4` are invariant;
- a `k=1` row selector lies in exactly one `SU(2)` factor, so its squared amplitude is linear in the corresponding rank-one density matrix `(I+n dot sigma)/2` or `(I+m dot sigma)/2`, hence affine in one Bloch vector;
- `k=3` reduces to `k=1` by complementary-minor duality for a unitary;
- for `k=2`, a row set equal to `{1,2}` or `{3,4}` is invariant because the corresponding `SU(2)` determinant is one, while a row set taking one row from each pair is a product-state selector in the tensor product of the two fundamental two-dimensional factors. Its squared amplitude is therefore linear in each rank-one density matrix separately, hence bilinear in `(n,m)`.

The real support functional preserves this degree. Summing gives (2). No bistochastic or independent-minor surrogate is introduced. `QED`

The coefficients are source-observable from genuine subgroup evaluations. For coordinate axes `e_i,e_j`, if `f_{st}=f(s e_i,t e_j)` for `s,t=+-1`, then

\[
Z_{ij}=\frac{f_{++}-f_{+-}-f_{-+}+f_{--}}4,\tag{3a}
\]
\[
p_i=\frac{f_{++}+f_{+-}-f_{-+}-f_{--}}4,\qquad
q_j=\frac{f_{++}-f_{+-}+f_{-+}-f_{--}}4.\tag{3b}
\]
The four-value average gives `c`. Thus the gate below can be reconstructed from exact true-unitary support evaluations alone.

## 3. Pole normalization and application of the assigned partner theorem

Suppose `U` is a genuine global support maximizer. Rotate Bloch coordinates so the identity in both factors is the north pole

\[
e=(0,0,1).
\]
Stationarity on the two individual spheres implies

\[
p+Ze=Ae,\qquad q+Z^Te=Be\tag{4}
\]
for `A,B>=0`.

If `A=0`, then `f(n,e)` is constant on the entire first pair sphere; if `B=0`, the second sphere is flat. The assigned partner account04/B09 `MOC4-ROOT-SATURATION-EXCLUSION-v1` rules either situation out at a support-violating global maximizer. Hence on the only surviving target branch

\[
\boxed{A>0,\qquad B>0.}\tag{5}
\]

Write

\[
Z=\begin{pmatrix}M&r\\s^T&z\end{pmatrix},
\quad M\in\mathbb R^{2\times2},\quad r,s\in\mathbb R^2.\tag{6}
\]
Equation (4) is exactly

\[
p=(-r,A-z),\qquad q=(-s,B-z).\tag{7}
\]

The tangent expansion at `(e,e)` is

\[
f-f(e,e)=-\frac A2\|x\|^2-\frac B2\|y\|^2+x^TMy+O(3),\tag{8}
\]
so the tangent Hessian is

\[
\begin{pmatrix}-AI_2&M\\M^T&-BI_2\end{pmatrix}.\tag{9}
\]
Its negative semidefiniteness is

\[
\|M\|_{op}^2\le AB.\tag{10}
\]
Under the lead's normalization `A=2(T-C)`, `B=2(T+C)`, this is exactly
`||M||_op^2<=4(T^2-C^2)`. Thus (10) is precisely the existing local mixed-Hessian gate, not a new assumption.

## 4. New theorem — exact global product-orbit gate

### Theorem 2 — `MOC4-SPIN4-GLOBAL-TRUST-REGION-GATE-v1`

With (2)–(7), `(e,e)` is a global maximizer of `f` on the complete genuine-unitary product orbit `S^2 x S^2` if and only if

\[
\boxed{
p\cdot n+\|q+Z^Tn\|\le p_3+B
\qquad\text{for every }n\in S^2.}\tag{11}
\]

Hence every support-violating global MOC4 maximizer satisfies (11) for each of the three complementary left Spin(4) products and, by the identical right-action argument, each of the three complementary right Spin(4) products.

#### Proof

For fixed `n`, (2) is affine in `m`:

\[
f(n,m)=c+p\cdot n+(q+Z^Tn)\cdot m.
\]
The exact maximum over `m in S^2` is therefore

\[
\max_m f(n,m)=c+p\cdot n+\|q+Z^Tn\|.\tag{12}
\]
At the north pole, (4) and `B>0` give `q+Z^Te=Be`, so

\[
f(e,e)=c+p_3+B.\tag{13}
\]
Thus `(e,e)` is the global product-orbit maximizer exactly when (12) is at most (13) for every `n`. This is (11). `QED`

This is not a local Taylor condition: it is the exact global optimization of the four-real-dimensional commuting pair orbit, reduced to one two-sphere.

## 5. Exact finite PSD certificate

Put

\[
L:=p_3+B=f(e,e)-c.\tag{14}
\]
The unsquared side of (11) first requires

\[
\boxed{L\ge\|p\|.}\tag{15}
\]
Under (15), (11) may be squared without changing its meaning. Define

\[
Q_0=pp^T-ZZ^T,\qquad
b_0=-(Lp+Zq),\qquad
c_0=L^2-\|q\|^2.\tag{16}
\]
Then (11) is equivalent to

\[
n^TQ_0n+2b_0^Tn+c_0\ge0\qquad(\|n\|=1).\tag{17}
\]

By the equality form of the real S-lemma / exact trust-region duality (the quadratic constraint `||n||^2-1=0` is indefinite after homogenization), (17) is equivalent to the existence of one real scalar `lambda` such that

\[
\boxed{
\begin{pmatrix}
Q_0-\lambda I_3&b_0\\
b_0^T&c_0+\lambda
\end{pmatrix}\succeq0.}\tag{18}
\]

For completeness, the forward implication in (18) is immediate by evaluating the quadratic form on `(n,1)` with `||n||=1`. Conversely, homogenize (17) to the cone `x^Tx=t^2`; because the constraint form `diag(I_3,-1)` takes both signs, Finsler's equality lemma separates the two quadratic forms and yields a scalar multiplier, exactly (18). Equivalently this is the zero-duality-gap trust-region subproblem.

Thus each complementary Spin(4) global-maximality condition is not an unspecified continuum restriction: it is exactly one norm inequality (15) plus one `4 x 4` PSD certificate (18) with one scalar multiplier. All coefficients come from the same true unitary.

Two explicit necessary consequences, obtained by testing the south pole in one factor and then interchanging the factors, are

\[
\sqrt{4\|s\|^2+(B-2z)^2}\le 2A+B-2z,\tag{19a}
\]
\[
\sqrt{4\|r\|^2+(A-2z)^2}\le A+2B-2z.\tag{19b}
\]
The simultaneous antipode also gives

\[
2z\le A+B.\tag{20}
\]
These are only shadows of the full trust-region gate (18).

## 6. Why this strictly strengthens the current local gate

The companion exact verifier checks the following rational bi-affine model:

\[
A=B=1,\quad z=\tfrac12,\quad r=s=(1,0),\quad M=0,
\]
so

\[
p=q=(-1,0,\tfrac12),
\qquad
Z=\begin{pmatrix}0&0&1\\0&0&0\\1&0&1/2\end{pmatrix}.
\]
At the north pole,

\[
f(e,e)=\tfrac32.
\]
Both individual pair antipodes and the simultaneous antipode have value `-1/2`, and the tangent Hessian is exactly `-I_4`; hence the individual strict pair gates, the full local mixed-Hessian gate, and the obvious antipodal subgroup tests all pass strictly.

Nevertheless at

\[
n=m=(-1,0,0)
\]
one has

\[
f(n,m)=2>\tfrac32.
\]
Moreover `L^2=9/4>||p||^2=5/4`, so even the unsquared sign condition (15) passes. The failure is genuinely in the trust-region quadratic:

\[
(L-p\cdot n)^2-\|q+Z^Tn\|^2=-1.
\]

This abstract model is **not claimed to be a target counterexample or even a source-realizable MOC coefficient tuple**. Its purpose is exact logical separation: the existing strict pair gates plus the full local Hessian inequality and antipodal tests do not by themselves imply global maximality on the same Spin(4) product orbit. Gate (18) contains additional nonlocal information that the surviving strict branch must satisfy.

## 7. Updated first unpaid implication

The assigned partner result removes every root-saturated branch. The lead's local Hessian theorem supplies (10). This run upgrades each such local strict gate to the exact global finite certificate (15),(18).

The first target-level residual may therefore be sharpened to:

> **`MOC4-SIX-SPIN4-TRUST-GATE-EXCLUSION-v1` (OPEN).**  
> For structured spectral support coefficients coming from one MOC4 direction and one genuine `O=Lambda^2 U`, prove that no positive support residual can satisfy simultaneously: the exact same-unitary `P/R/D` identities, full left/right stationarity, all strict root gates from account04/B09, the campaign subgroup roofs, and the six global Spin(4) trust-region certificates (15),(18). Alternatively produce a genuine normal-matrix witness satisfying all of these and separating from all 24 target vertices.

This is narrower than `MOC4-STRICT-SPIN6-SIX-WITNESS-v2`: each four-real-dimensional complementary product-orbit condition has been eliminated to explicit finite algebraic data. A next exact route is to insert the spinor/Vandermonde coefficient identities into the six `4 x 4` PSD matrices and use their principal-minor inequalities jointly with the shared `SO(6)=Lambda^2 SU(4)` constraints.

## 8. Status and non-claims

- `MOC4-SPIN4-BIAFFINE-ORBIT-v1`: **PROVED**.
- `MOC4-SPIN4-GLOBAL-TRUST-REGION-GATE-v1`: **PROVED**.
- Exact rational strictness witness for the gap between local and global gates: **VERIFIED**.
- account04/B09 `MOC4-ROOT-SATURATION-EXCLUSION-v1`: consumed source-bound and used to obtain `A,B>0`; not re-claimed as this run's theorem.
- Full MOC4: **OPEN / NOT PROVED / NOT DISPROVED**.
- No arbitrary bistochastic surrogate, independent compound-minor assignment, benchmark work, paid model/API/Codex, email/Drive delivery, public posting, credentials, scheduler identifiers, machine paths, or unrelated private transcript was used.
