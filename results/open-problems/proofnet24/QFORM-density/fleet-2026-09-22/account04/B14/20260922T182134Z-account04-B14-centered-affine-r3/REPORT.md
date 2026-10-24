# account04/B14 — constant-preserving centered affine localization

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T182134Z-account04-B14-centered-affine-r3`  
**Status:** `TARGET_LEVEL_REDUCTION / ESSENTIAL_STEP_APPLIED / FULL_CONJECTURE_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target constants

For a real symmetric matrix (A), an interval (I), and independent real
random variables with densities bounded by one, write

\[
 R(A,X;I)=\frac{\Pr\{X^TAX\in I\}}{|I|}.
\]

Let (C_{\rm hom}) be the supremum of (R(A,X;I)) over all dimensions,
all admissible inputs, all nondegenerate bounded intervals, and all (A)
having at least three eigenvalues of absolute value at least one.

Let (C_{\rm ca}) be the analogous supremum for

\[
 F_{A,b,c}(Y)=Y^TAY+2b^TY+c,
\]

where the independent inputs (Y_i) have compactly supported cap-one
densities, satisfy \(\mathbb EY_i=0\), and the affine vector obeys the exact
compatibility condition

\[
                         b\in\operatorname{Ran}A.
\]

Finally let (C_{\rm ff}) be the same supremum as (C_{\rm ca}), restricted
further to densities (1_{E_i}), where every (E_i) is a compact finite
union of intervals, has measure one, and has barycenter zero.

## 2. Main theorem

### `QFORM-CENTERED-AFFINE-LOCALIZATION-EQUIVALENCE-v1`

In the extended nonnegative reals,

\[
                 \boxed{C_{\rm hom}=C_{\rm ca}=C_{\rm ff}.}
\]

Thus arbitrary global translations, unbounded supports, and fractional input
densities may all be removed simultaneously with **no loss in the sharp
constant**, provided the translation-generated affine term is retained.
The centered compact supports may have arbitrary diameters, and the centered
finite unions may have arbitrarily many components and arbitrary internal
separations.

## 3. Proof that \(C_{\rm hom}\le C_{\rm ca}\)

Fix an admissible homogeneous instance.  For each marginal density (f_i),
the preceding B14 compact-localization theorem supplies compactly supported
cap-one probability densities (g_{i,R}) such that

\[
 d_{\rm TV}(g_{i,R}(x)\,dx,f_i(x)\,dx)\longrightarrow0.
\]

For fixed finite dimension, product total variation is at most the sum of the
marginal total variations, and measurable pushforwards contract total
variation.  Hence it is enough to bound the compact approximants with the
same constant.

Let (X^{(R)}) have product density \(\prod_i g_{i,R}\), put

\[
 m_R=\mathbb E X^{(R)},\qquad Y^{(R)}=X^{(R)}-m_R.
\]

Compact support makes every coordinate of (m_R) finite.  Translation
preserves independence and the cap-one property, and the centered variables
have compact support and mean zero.  Exactly,

\[
 (X^{(R)})^TA X^{(R)}
 = (Y^{(R)})^TA Y^{(R)}
   +2(Am_R)^TY^{(R)}+m_R^TAm_R.
\]

The generated affine vector (b_R=Am_R) lies in \(\operatorname{Ran}A\), so
this is an instance counted by (C_{\rm ca}).  Therefore

\[
 \Pr\{(X^{(R)})^TAX^{(R)}\in I\}\le C_{\rm ca}|I|.
\]

Passing to the total-variation limit proves the same inequality for the
original instance.  No moment bound on the original variables was used; the
possibly divergent sequence (m_R) is harmless because the affine estimate
is uniform in (b_R) and in the scalar shift.

## 4. Proof that \(C_{\rm ca}\le C_{\rm hom}\)

Take a centered compact affine instance and choose (m\in\mathbb R^n) with

\[
                              Am=b.
\]

This is possible precisely because (b\in\operatorname{Ran}A).  Put
(X=Y+m).  Then (X_i) remain independent with cap-one densities and

\[
 Y^TAY+2b^TY+c=X^TAX+c-m^TAm.
\]

The final scalar only translates the output law, so it does not change any
interval small-ball ratio or the essential supremum of a density.  Hence the
affine instance is bounded by (C_{\rm hom}).

The range condition is essential to this exact equivalence.  For example, if
(A=\operatorname{diag}(1,0)), an affine term in the second coordinate cannot
be produced by translating (X^TAX).  No such unsupported arbitrary-affine
claim is made here.

## 5. Finite-fragment extreme inputs

The earlier coordinatewise bathtub theorem shows that (C_{\rm hom}) is
unchanged when every input density is restricted to (1_{E_i}),
(|E_i|=1).  The earlier finite-fragment approximation then replaces every
(E_i) in total variation by a compact finite union of intervals of total
length one, again without changing the sharp constant.

For such a compact set let

\[
 \mu_i=\int_{E_i}x\,dx,
 \qquad F_i=E_i-\mu_i.
\]

Because (|E_i|=1), (1_{F_i}) is a cap-one probability density of mean
zero.  Translating the product by \(\mu=(\mu_i)\) replaces the homogeneous
quadratic by the range-compatible affine form with (b=A\mu), exactly as in
Section 3.  Conversely Section 4 removes that affine term.  This proves
(C_{\rm ff}=C_{\rm hom}).

This reduction removes global coordinate locations but **does not** bound the
diameters, fragment counts, or separations inside any (F_i).  That distinction
is required by the correction inbox.

## 6. Applying the completed account01/B14 theorem

The completed partner result is account01/B14
`QFORM-GROUPED-SCHUR-RANK2-OUTSIDE-FREE-v1`, source-pinned at brain commit
`5a332df9b12f3403cac5c68cc07bfc8a768648b1` and canonical mathematical source
`yspennstate/math-open-problems@c7303438b647f318f0c2a052cb0bec1557f47b37`.

It states: pivot an original coordinate with (a=A_{ii}\ne0), let (S) be
the full Schur complement, and suppose a physical coordinate bank (J) has
(S_{JJ}) of exact rank two with nonzero eigenvalues \(\mu_1,\mu_2\).  With

\[
                         \Delta_2=|\mu_1\mu_2|,
\]

one has, for every homogeneous cap-one product input,

\[
 \|p_{X^TAX}\|_\infty
 \le128\,|a|^{-1/2}\Delta_2^{-1/4}.
\]

The present theorem applies it to an actual localized affine inequality.  If
(Y) is any compact mean-zero cap-one product input, (b\in\operatorname{Ran}A),
and (c\in\mathbb R), choose (m) with (Am=b).  Then for every interval (I),

\[
\begin{aligned}
 \Pr\{Y^TAY+2b^TY+c\in I\}
 &=\Pr\{(Y+m)^TA(Y+m)\in I-(c-m^TAm)\}\\
 &\le128\,|a|^{-1/2}\Delta_2^{-1/4}|I|.
\end{aligned}
\]

Thus the partner estimate survives arbitrary global coordinate translations,
arbitrary scalar shifts, compact localization, and the return to unbounded
original laws with **zero translation or tail tax**.  Its own mass-linear
outside conditioning also allows arbitrary additional coordinates and
couplings outside the active rank-two bank.

## 7. Scope and remaining implication

This is a target-level equivalence, not a proof that the universal constant is
finite.  It proves an essentially bounded-density transfer whenever the
corresponding affine compact estimate is available.  It does not prove
continuity: translation preserves continuity for a fixed law, but total-
variation limits of uniformly bounded continuous densities need not be
continuous.

The first unpaid implication is now purely internal/structural.  It suffices
to prove the universal bound for mean-zero uniforms on compact finite interval
unions, with arbitrary internal fragment geometry and range-compatible affine
terms.  Equivalently, one must derive from the three-large-eigenvalue hypothesis
either the partner's grouped-Schur condition with a uniform parameter bound or
another mass-linear mechanism that controls the remaining rotated indefinite
branch.  No moment, bounded-diameter, connected-support, fixed-fragment-count,
or diagonal-basis assumption may enter that step.

