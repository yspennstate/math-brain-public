# MOC4 fleet01/B07 — transverse trust-square rigidity on a simple mixed-Schur equality circle

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T083513Z-b07-moc4-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and live source-bound state

For complex normal `4 x 4` matrices with spectra `a=(a_i)` and `b=(b_j)`, prove

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]

For a support direction `eta`, after diagonalizing one normal matrix and writing the relative eigenbasis as a true unitary `U`, the exact Cauchy--Binet expansion is

\[
\det(D_a+UD_bU^*)
=\sum_{S,T\subset[4],\ |S|=|T|}
a_{S^c}b_T\,|\det U[S,T]|^2. \tag{1}
\]

In the middle layer, after the complementary-pair/self-dual change of basis,
`O=Lambda^2 U in SO(6)` is a `3 x 3` array of real `2 x 2` blocks `B_{alpha beta}`. Put

\[
D_{\alpha\beta}=\det B_{\alpha\beta},\qquad
R_{\alpha\beta}=\frac12\|B_{\alpha\beta}\|_F^2.
\]

The nonconstant middle-layer support is

\[
s(O)=\langle D,K\rangle+\frac12\langle R,X\rangle. \tag{2}
\]

The latest complete campaign-lead result consumed is fleet03/B07
`20260922T074824Z-fleet03-B07-MOC4-r13`,
`MOC4-MSQR-CROSS-BLOCK-ANNIHILATION-v1` /
`MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`.  On a mixed-Schur (`MSQR`) pair boundary
at a true global support maximizer, its pair kernel is a full-Hessian kernel
and the full Lyapunov--Schmidt fourth-order gate contains a nonnegative
cross Schur-complement reserve.

A newer compatible team result, fleet02/B07
`20260922T083437Z-b07-d9295a20`,
`MOC4-MSQR-HIGHER-ORDER-SATURATION-v1`, proves that exact pair-LS
saturation forces the corrected mixed-Schur discriminant to be stationary
in every Hessian-corrected transverse direction and supplies the exact
fifth- and sixth-order necessary conditions.

The assigned OTHER-account partner result actually consumed and applied is
fleet02/B08 `MOC4-COMMON-BLOCK-EDGE-PAYMENT-v1`,
handoff commit `03a0b8d66e46aebc27be11ab59936bdafae85922`.
It proves exact one-edge safety out of every proper common reducing block
and gives the exact matched two-edge `2+2` payment criterion
`C^2 <= delta10 delta01`.  Therefore a limiting common-block escape is not
treated below as a free generic-interior perturbation.

I also retain fleet04/B09
`MOC4-ZERO-FACE-BOGOLIUBOV-COFACTOR-RIGIDITY-v1`: on a true zero-entry
face the anti-linear Bogoliubov block has singular values `(1,1,0)` and the
companion block is its rank-one cofactor complement.  This is relevant
because the double-mixed saturation branch is already known to reach an
equal-support zero-entry representative.

## 2. Exact transverse first derivative in exterior blocks

Fix three complementary row planes `alpha,gamma,delta`.  Along a Spin(4)
orbit mixing the first two planes, write the current blocks as
`A_beta`, `G_beta`; the third-plane blocks `H_beta` are fixed.

For real `2 x 2` matrices define determinant polarization

\[
\delta_2(P,Q)=\frac12\{\det(P+Q)-\det P-\det Q\}
\]

and

\[
\Phi_{r\beta}(P,Q)
=K_{r\beta}\delta_2(P,Q)+\frac{X_{r\beta}}4\langle P,Q\rangle_F.
\]

Then the contribution of block `B_{r beta}` to (2) is
`\Phi_{r beta}(B_{r beta},B_{r beta})`.

Let `L_{alpha delta}(Y)` be the true `SO(6)` root generator with off-diagonal
`2 x 2` block `Y`.  The exact first derivative is

\[
Ds[L_{\alpha\delta}(Y)]
=\langle Y,\Gamma_{\alpha\delta}\rangle_F, \tag{3}
\]

where

\[
\boxed{
\Gamma_{\alpha\delta}
=\sum_\beta\left[
K_{\alpha\beta}\operatorname{cof}(A_\beta)H_\beta^T
-K_{\delta\beta}A_\beta\operatorname{cof}(H_\beta)^T
+\frac{X_{\alpha\beta}-X_{\delta\beta}}2A_\beta H_\beta^T
\right].
} \tag{4}
\]

The analogous formula with `A` replaced by `G` gives
`\Gamma_{\gamma\delta}`.

Proof: under the root variation,
`A_beta' = Y H_beta`, `H_beta'=-Y^T A_beta`.  Since in dimension two

\[
2\delta_2(P,Q)=\langle\operatorname{cof}(P),Q\rangle_F,
\]

differentiating the quadratic block functional gives (3)--(4).

Define the nonnegative coordinate squared transverse-gradient function

\[
\Psi
=\|\Gamma_{\alpha\delta}\|_F^2
+\|\Gamma_{\gamma\delta}\|_F^2. \tag{5}
\]

Thus `Psi=0` is exactly simultaneous stationarity in all eight nontrivial
root directions connecting the active four-plane to the third two-plane.

## 3. Biaffine descent of the transverse-gradient square

A complementary Spin(4) product orbit modulo the two exact within-plane
`SO(2)` symmetries is `S^2 x S^2`.  Let its Bloch coordinates be
`n,m in S^2`.  The pair support has the exact form

\[
f(n,m)=c+p\cdot n+q\cdot m+n^T Zm. \tag{6}
\]

The same quotient structure applies to (5).

### Theorem 1 — `MOC4-TRANSVERSE-GRADIENT-BIAFFINE-v1`

There exist a scalar `a`, vectors `b,c in R^3`, and a real `3 x 3` matrix
`E` such that on the genuine pair orbit

\[
\boxed{
\Psi(n,m)=a+b\cdot n+c\cdot m+n^TEm.
} \tag{7}
\]

### Proof

The transformed four row coordinates are obtained by one `Q in SO(4)`.
Formula (4) is linear in the transformed blocks because the `2 x 2`
cofactor map is linear.  Hence the pair
`(\Gamma_{\alpha\delta},\Gamma_{\gamma\delta})` is linear in the entries of
`Q`, and `Psi` is quadratic in `Q`.

Changing bases separately inside the two active oriented two-planes acts
by the stabilizer `SO(2) x SO(2)`.  It rotates the two matrices `Gamma`
orthogonally and leaves (5) invariant.  Therefore `Psi` descends to the
oriented Grassmannian

\[
SO(4)/(SO(2)\times SO(2))\cong S^2\times S^2.
\]

In the Spin(4)=SU(2)xSU(2) parametrization, entries of `Q` are bilinear in
the two unit spinors.  A quadratic `SO(2)xSO(2)`-invariant function is
degree two in each spinor, so after the two Hopf quotients its coordinate
space is exactly spanned by

\[
1,\quad n_i,\quad m_j,\quad n_i m_j.
\]

This gives (7).  No relaxation of the common unitary is used. QED.

## 4. The exact simple-MSQR equality circle

Use the genuine Spin(4) normal form of the completed fleet02/B07
saturation-manifold theorem.  Let the present global maximizer be the
north-pole point and put

\[
d(n)=L-p\cdot n,\qquad r(n)=q+Z^Tn. \tag{8}
\]

Global maximality on the pair orbit gives the trust inequality

\[
d(n)\ge \|r(n)\|\ge0\qquad(n\in S^2). \tag{9}
\]

On a simple mixed-Schur pair with exact pair-LS saturation there are
`\Delta>0` and a real `k` such that

\[
\boxed{
d(n)^2-\|r(n)\|^2
=\Delta\,\ell(n)^2,\qquad
\ell(n)=y+k(1-z).
} \tag{10}
\]

The equality set is the genuine circle

\[
\mathcal C_k=S^2\cap\{\ell=0\}. \tag{11}
\]

For every `n in C_k` with `d(n)>0` the complementary maximizing factor is

\[
m(n)=\frac{r(n)}{d(n)}\in S^2, \tag{12}
\]

and `(n,m(n))` is not merely pair-optimal: it is an equal-support global
maximizer of the full true-unitary support.  Consequently

\[
\Psi(n,m(n))=0\qquad(n\in\mathcal C_k). \tag{13}
\]

## 5. Main new theorem — exact transverse trust-square proportionality

Extend (7), for fixed `n`, affinely from `m in S^2` to the closed unit ball.
When `d(n)>0`, define the **relaxed complementary response**

\[
\bar m(n)=\frac{r(n)}{d(n)}. \tag{14}
\]

By (9), `||bar m(n)||<=1`.  Since (7) is affine in `m` and nonnegative on
the whole unit sphere, it is nonnegative on the whole unit ball.  Thus

\[
\Psi(n,\bar m(n))\ge0. \tag{15}
\]

Write (7) as

\[
\Psi(n,m)=A(n)+u(n)\cdot m,
\quad
A(n)=a+b\cdot n,\quad
u(n)=c+E^Tn. \tag{16}
\]

Define

\[
P(n):=d(n)\Psi(n,\bar m(n))
=d(n)A(n)+u(n)\cdot r(n). \tag{17}
\]

This is a real polynomial of degree at most two in `n`.  It is nonnegative
on `S^2`, and by (12)--(13) it vanishes on the whole genuine circle
`\mathcal C_k`.

### Quadratic-circle lemma

Let `P` be a real polynomial of degree at most two, nonnegative on `S^2`,
and suppose it vanishes on a genuine circle
`S^2 cap {ell=0}`, where `ell` is a nonconstant affine function whose
plane cuts the sphere transversely.  Then there are real constants
`lambda,mu` with `mu>=0` such that

\[
\boxed{
P(n)=\lambda(\|n\|^2-1)+\mu\,\ell(n)^2.
} \tag{18}
\]

Indeed, restriction to the plane `ell=0` is a planar quadratic vanishing
on its entire Euclidean circle, hence

\[
P=\lambda(\|n\|^2-1)+\ell L
\]

for an affine `L`.  On the sphere every point of the circle is a minimum
of `P`; differentiating in a sphere-tangent direction transverse to the
circle gives `L=0` on the circle.  An affine function vanishing on a
genuine circle is a scalar multiple of its plane equation, so
`L=mu ell`.  Nonnegativity on the sphere forces `mu>=0`.

Applying the lemma to (17) gives the new exact identity

\[
\boxed{
d(n)\Psi(n,\bar m(n))
=\mu\,\ell(n)^2
\quad(n\in S^2)
} \tag{19}
\]

for one scalar `mu>=0`.

Combining (19) with the determinant-specific trust identity (10) gives

\[
\boxed{
\Psi(n,\bar m(n))
=
\frac{\mu}{\Delta}\,
\frac{d(n)^2-\|r(n)\|^2}{d(n)}
} \tag{20}
\]

wherever `d(n)>0`.

I call (19)--(20)

**`MOC4-MSQR-TRANSVERSE-TRUST-SQUARE-v1`.**

This is an exact source-valid global consequence of full transverse
stationarity on the whole simple-MSQR equality circle.  The infinitely many
transverse stationarity identities do not remain an uncontrolled family:
after the same-unitary Spin(4) structure is imposed, their aggregate
squared norm is governed by a single nonnegative scalar `mu`.

For any off-circle point `n0` with `d(n0)>0` and `ell(n0)!=0`,

\[
\boxed{
\mu
=
\frac{d(n_0)\Psi(n_0,\bar m(n_0))}
{\ell(n_0)^2}.
} \tag{21}
\]

Thus `mu` is computable from one exact off-circle evaluation of the
mixed-minor gradient matrices (4).

## 6. Zero-leakage rigidity

Equation (19) has a useful exact dichotomy.

### Theorem 2 — `MOC4-MSQR-ZERO-LEAKAGE-DECOUPLING-v1`

If `mu=0` in (19), then

\[
\boxed{\Psi(n,m)\equiv0\quad\text{on }S^2\times S^2.} \tag{22}
\]

Equivalently, both cross-root gradient matrices in (5) vanish on the
**entire genuine Spin(4) pair orbit**, not only on the equality circle.

### Proof

If `mu=0`, (19) gives `Psi(n,bar m(n))=0` for every `n` with `d(n)>0`.
Because `Delta>0`, every off-circle point with `ell(n)!=0` satisfies, by
(10),

\[
\|\bar m(n)\|<1.
\]

These points contain an open subset of `S^2`.  For each such fixed `n`,
`m -> Psi(n,m)` is affine and nonnegative on the closed unit ball, but
vanishes at an interior point.  Hence that affine function is identically
zero on the ball.  Therefore both its constant and linear coefficients
vanish for an open set of `n`.  By (7), those coefficients are affine in
`n`, so they vanish identically.  This proves (22). QED.

Thus a simple pair-LS saturated positive-gap maximizer can survive only in
one of two sharply separated transverse regimes:

1. `mu>0`: exact positive transverse leakage, with magnitude globally
   locked to the determinant pair trust slack by (20);
2. `mu=0`: total transverse first-order decoupling on the entire true
   Spin(4) pair orbit.

This is stronger than retaining an infinite list of Taylor coefficients
at the north pole.

## 7. Relation to the newest higher-order saturation result

The newer fleet02/B07 theorem proves that at exact pair-LS saturation
the corrected mixed-Schur discriminant is stationary in all
Hessian-corrected transverse directions and supplies Q5/Q6 necessary
conditions.  The present result is complementary rather than a repetition:

- the fleet02/B07 identities are higher-order local jet conditions at
  the north-pole maximizer;
- (19) is a global identity over the **entire first Bloch sphere**, derived
  from the exact equality circle and the source-valid exterior-block
  transverse gradient;
- (22) identifies a qualitatively distinct zero-leakage branch on which
  every transverse first derivative vanishes throughout the whole pair
  orbit.

The first remaining simple-saturation implication is therefore no longer
"expand all transverse stationarity equations along the circle."  It is the
finite two-case obligation

**`MOC4-MSQR-TRANSVERSE-LEAKAGE-CLOSURE-v1`:**
prove that `mu>0` is incompatible with the full-Hessian/Q5/Q6/subgroup-roof
budget at a positive-gap maximizer, while `mu=0` forces target safety,
a common-block degeneration, or the already isolated zero-face branch.

## 8. Named-partner and boundary application

The assigned fleet02/B08 theorem is used as a boundary guardrail.  If a
putative equality-circle sequence approaches a proper common reducing
block, a single cross-edge departure is already an exact convex
interpolation of safe common-block endpoint determinants.  On a `2+2`
boundary the matched two-edge torus is safe whenever

\[
C^2\le\delta_{10}\delta_{01}.
\]

Therefore neither the `mu>0` nor `mu=0` branch may claim a boundary
counterexample by replacing those source-valid payments with a free
transport or compound-minor perturbation.  The remaining common-block
structured-payment cases stay open exactly as recorded by B08.

On the separate double-mixed saturation branch, the completed equality
manifold theorem reaches an equal-support zero-entry representative.
The newer fleet04/B09 cofactor-rigidity result then forces the corresponding
Bogoliubov anti-linear block to have singular values `(1,1,0)` and the
companion block to be its rank-one cofactor complement.  That zero-face
branch is sharper but still not closed.

## 9. Compact conditional end-to-end argument after this run

Assume MOC4 fails.  By the campaign's source-valid genericization and
compactness reductions, take a genuine positive-gap global support
maximizer on the generic core.  The current proof tree is:

1. **MSQR with positive pair-LS slack:** use the lead's full cross-split
   reserve and the explicit determinant/exterior derivative formulas;
   this remains open.
2. **MSQR with exact pair-LS saturation, simple mixed singular value:** the
   genuine pair orbit contains the exact equality circle.  This run reduces
   all full transverse stationarity on that circle to the scalar
   trust-square identity (19) and the dichotomy `mu>0` versus (22).
   Closing `MOC4-MSQR-TRANSVERSE-LEAKAGE-CLOSURE-v1` closes this subbranch.
3. **MSQR with double mixed saturation:** reduce to the true zero-entry
   branch; apply the exact Bogoliubov cofactor constraints there.
4. **NDI:** all six pair Hessian blocks are negative definite; the separate
   strict-interior closure remains open.
5. **Repeated/common-block limits:** retain the assigned B08 exact
   one-edge and matched-two-edge payment results; no unsupported
   interpolation is used.

Therefore full MOC4 is not proved in this run.  The simple saturated MSQR
branch has, however, been compressed from an infinite equality-circle
stationarity problem to one explicit nonnegative scalar `mu` plus a
fully-decoupled exceptional branch.

## 10. Exact algebra check

`VERIFY_CIRCLE_IDEAL.py` uses exact SymPy rational arithmetic with
`k=1/2` and the rational parametrization

\[
x=\frac{2t}{t^2+1+k^2},\quad
y=\frac{-2k}{t^2+1+k^2},\quad
z=\frac{t^2+k^2-1}{t^2+1+k^2}.
\]

It verifies exactly that:

- the parametrization lies on `S^2` and `ell=0`;
- the restriction map from real quadratics in `(x,y,z)` to that circle has
  rank `5`, hence a `5`-dimensional kernel;
- that kernel is exactly the degree-two span of
  `sphere`, `ell`, `ell*x`, `ell*y`, `ell*z`;
- affine functions vanishing on the circle form a one-dimensional space,
  generated by `ell`.

Captured stdout:

```text
PASS MOC4-MSQR-TRANSVERSE-TRUST-SQUARE-v1 algebra check
circle_parameterization_exact = True
quadratic_restriction_rank = 5
quadratic_vanishing_dimension = 5
circle_ideal_degree2_rank = 5
combined_rank = 5
affine_vanishing_dimension = 1
affine_null_vector = (-1, 0, -2, 1)
```

The checker validates the algebraic circle lemma for an exact nondegenerate
rational sample; the theorem itself is the analytic argument above.

## 11. Claim limits

- Full MOC4 remains **OPEN**.
- No target-level counterexample is claimed.
- `mu>=0` is a necessary structural parameter, not yet proved zero or
  inconsistent.
- `mu=0` gives exact transverse decoupling, not by itself target safety.
- No arbitrary doubly stochastic matrix, free `SO(6)` point, independent
  compound-minor assignment, or spectral-only external vertex is promoted
  to a true-unitary counterexample.
- No benchmark material, sealed answer, credentials, machine path, email,
  Drive, paid/remote model call, public posting, workflow execution or
  permission change was used.

**Verdict:** `ESSENTIAL_STEP_APPLIED`.
