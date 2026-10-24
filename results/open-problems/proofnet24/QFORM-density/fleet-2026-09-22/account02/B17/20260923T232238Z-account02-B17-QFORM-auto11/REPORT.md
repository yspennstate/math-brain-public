# QFORM-PLANAR-ROTATION-CUBE-GLOBAL-v1

**Account/slot:** account02 / B17  
**Programme:** QFORM-DENSITY-3EIG-20260922  
**Status of full theorem:** OPEN / NOT PROVED / NOT DISPROVED  
**Execution context:** WITHOUT_VERIFIED_BRAIN  
**Pinned source:** `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `COUNTEREXAMPLE_SEARCH.md`, Theorem C.  
**Fresh math master before this bundle:** `755c765f98cdc9d2a2107f2f075273e7b0960e75`.

## 1. First unpaid implication paid

The preceding B17 run proved global cone-tip maximality for all one-sheet levels in arbitrary rotated three-bank cube laws, but the genuinely non-aligned two-sheet side was still unpaid. This run closes a nontrivial continuum of that branch: all centered physical three-cubes for which one positive eigendirection remains a physical coordinate while the remaining `(+,-)` plane is arbitrarily rotated.

Let

\[
C=\begin{pmatrix}a&b\\b&-a\end{pmatrix},\qquad a^2+b^2=1,
\]

and in the original physical coordinates `(X_1,X_2,X_3)` define

\[
A_C=\begin{pmatrix}
a&0&b\\
0&1&0\\
b&0&-a
\end{pmatrix}.
\]

Take `X_1,X_2,X_3` independent `Unif[-1/2,1/2]`. Directly,

\[
A_C^2=I_3,\qquad \operatorname{tr}A_C=1,\qquad \det A_C=-1,
\]

so every finite matrix in the continuum has exact spectrum

\[
\boxed{\operatorname{spec}(A_C)=\{1,1,-1\}.}
\]

No diagonal-basis or post-rotation independence is used.

Write

\[
S=(X_1,X_3)C(X_1,X_3)^T,\qquad W=X_2^2,\qquad Q=S+W.
\]

The theorem proved below is

\[
\boxed{\|p_Q\|_\infty=p_Q(0)\le {4\pi\over3}<3\sqrt2.}
\]

Thus a continuous family of genuinely non-aligned two-sheet witnesses cannot break the candidate sharp constant.

## 2. The planar indefinite law is even and radially monotone in output

Parameterize the square `[-1/2,1/2]^2` in polar coordinates by

\[
(x_1,x_3)=r(\cos\theta,\sin\theta),\qquad
0\le r\le R(\theta),
\]

where

\[
R(\theta)={1\over2M(\theta)},\qquad
M(\theta)=\max(|\cos\theta|,|\sin\theta|).
\]

For a phase `\delta` depending on `(a,b)`,

\[
S=r^2c(\theta),\qquad c(\theta)=\cos(2\theta-\delta).
\]

For `s>0`, direct delta integration in `r` gives, for a.e. `s`,

\[
f_S(s)
={1\over2}\int_{\substack{c(\theta)>0\\s\le c(\theta)R(\theta)^2}}
{d\theta\over c(\theta)}.
\]

The integration set only shrinks as `s` increases, hence `f_S(s)` is nonincreasing on `(0,\infty)`.

Moreover every real traceless symmetric `2\times2` matrix satisfies

\[
J^TCJ=-C,\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

The square is invariant under `J`, so `S\stackrel d=-S`. Consequently `f_S` is even and nonincreasing as a function of `|s|`.

This is the special structure that pays the previously unpaid two-sheet side.

## 3. Negative/two-sheet side: direct monotonicity, no X-ray shortcut

The square `W=X_2^2` has density

\[
b_W(w)=w^{-1/2}\mathbf 1_{(0,1/4)}(w).
\]

Therefore for `r>0`,

\[
p_Q(-r)
=\int_0^{1/4}w^{-1/2}f_S(r+w)\,dw
\le
\int_0^{1/4}w^{-1/2}f_S(w)\,dw
=p_Q(0).
\]

This is a genuine two-sheet estimate obtained in the original product law. It does **not** use the corrected-false implication from a generic X-ray norm to a two-sheet quadratic trace.

## 4. Positive/one-sheet side: apply pinned Theorem C to a real inequality

The required completed result from the pinned `e5f71d79...` source is Theorem C in `COUNTEREXAMPLE_SEARCH.md`: for signature `(+,+,-)` it gives the exact one-sheet ruling/coarea identity

\[
p_Q(s)={\pi\over\sqrt2}\operatorname{avg}_{\theta}
\rho_\theta(\sqrt{s}\,e_\theta),\qquad s\ge0,
\]

where `\rho_\theta` is the relevant two-dimensional marginal of the density after an orthogonal spectral rotation.

Here the original centered-cube density is centrally symmetric and log-concave. Orthogonal rotation preserves both properties, and Prekopa preserves them under marginalization. Hence every `\rho_\theta` is centrally symmetric log-concave and is maximized at zero. The exact pinned identity therefore yields

\[
\boxed{p_Q(s)\le p_Q(0),\qquad s\ge0.}
\]

The generic numerical ceiling `\pi\sqrt2` from Theorem C would be too large to settle the proposed sharp constant. The completed source result is useful here through its exact ruling identity, combined with this source-valid special law.

Together with the previous section,

\[
\boxed{\|p_Q\|_\infty=p_Q(0).}
\]

## 5. Uniform cone-tip bound below `3 sqrt(2)`

At zero, integrate out `X_2` directly:

\[
p_Q(0)
=
\int_{[-1/2,1/2]^2}
\mathbf1_{\{-1/4\le S<0\}}(-S)^{-1/2}\,dx_1dx_3.
\]

Dropping only the restriction `-S\le1/4` gives

\[
p_Q(0)
\le
\int_{c(\theta)<0}{R(\theta)\over\sqrt{-c(\theta)}}\,d\theta.
\]

Since `M(\theta)\ge1/\sqrt2`,

\[
R(\theta)\le{1\over\sqrt2}.
\]

The angular singular integral is phase independent, and with

\[
J=\int_0^{\pi/2}(\cos u)^{-1/2}\,du
\]

one has

\[
\int_{c<0}(-c)^{-1/2}\,d\theta=2J.
\]

Hence

\[
p_Q(0)\le\sqrt2 J.
\]

A completely elementary bound avoids any special-function constant. On `[0,\pi/3]`, `\cos u\ge1/2`, so that part of `J` is at most `\pi\sqrt2/3`. On `[\pi/3,\pi/2]`, concavity of cosine places the graph above its endpoint chord,

\[
\cos u\ge {3\over\pi}\left({\pi\over2}-u\right),
\]

and therefore the second part is also at most `\pi\sqrt2/3`. Thus

\[
J\le{2\pi\sqrt2\over3},
\qquad
\boxed{p_Q(0)\le{4\pi\over3}.}
\]

Finally, `\pi<22/7`, and

\[
{22\over7}<{9\sqrt2\over4}
\]

because `88<63\sqrt2`, equivalently after squaring `7744<7938`. Therefore

\[
\boxed{{4\pi\over3}<3\sqrt2.}
\]

Numerically, `4\pi/3=4.188790204786391...`, while `3\sqrt2=4.242640687119285...`.

## 6. Explicit midpoint check

At the fully off-diagonal midpoint

\[
C=\begin{pmatrix}0&-1\\-1&0\end{pmatrix},
\qquad
Q=X_2^2-2X_1X_3.
\]

The density of `-2X_1X_3` is

\[
f(z)=\log {1\over2|z|},\qquad 0<|z|<1/2.
\]

Therefore

\[
p_Q(0)
=\int_0^{1/4}w^{-1/2}\log {1\over2w}\,dw
=\boxed{2+\log2}
=2.693147180559945... .
\]

This is a useful exact stress check deep inside the new continuum.

## 7. Latest account03/B17 result consumed

The latest compatible account03/B17 handoff proves `QFORM_TWO_HEAVY_ONE_DIFFUSE_GLOBAL` for the same midpoint latent orientation

\[
Q=V^2-2UZ
\]

with `(U,V)` allowed an arbitrary joint density at most one and `Z\sim N(0,1/12)` independent. Its global constant is

\[
C_{2H1G}
=2^{13/6}\sqrt{3/\pi}\,\Gamma(5/4)^{2/3}
=4.109270566451296...<3\sqrt2,
\]

and its finite diffuse-bank transfer keeps exact nonzero spectrum `{1,1,-1}`.

Thus the midpoint is obstructed in two complementary directions: the present theorem controls the finite centered cube exactly (and simultaneously all planar rotations), while the partner theorem allows far rougher heavy laws once the third coordinate is a Gaussian/diffuse bank. In particular

\[
\max\{4\pi/3,C_{2H1G}\}=4\pi/3<3\sqrt2.
\]

This is a supporting sharp-constant obstruction, not a proof of the full theorem.

## 8. What remains unpaid

This theorem does **not** cover an arbitrary `O(3)` mixing of all three physical cube axes. It keeps one positive eigendirection equal to one physical coordinate and rotates only the complementary `(+,-)` plane. It also does not cover arbitrary rough laws in all three bank coordinates, general non-aligned larger uniform banks, several shared/intermediate-leverage rows, extra active spectrum, or the full arbitrary-product-law problem.

The next sharp witness class is therefore a fully three-axis mixed negative direction (or equivalently a genuinely non-planar orthogonal spectral rotation) on a source-valid finite cube/bank, followed by its rough-law and multiscale-fragment analogues.

Failure of the present monotonicity mechanism outside this planar family would only be failure of a proof mechanism. A finite example with peak above `3\sqrt2` would refute the proposed **sharp constant** but not existence of a larger universal QFORM bound; a genuine QFORM counterexample must defeat every finite universal constant.

## 9. Verification

`verify_planar_rotation_cube.py` checks the exact involution/spectrum algebra on several rational points, the numerical constants, the partner constant, the explicit midpoint value, and the rational comparison `7744<7938`. Local deterministic evaluation in this invocation returned

```
PASS QFORM-PLANAR-ROTATION-CUBE-GLOBAL-v1
4pi/3 = 4.188790204786391
3sqrt2 = 4.242640687119285
gap = 0.05385048233289416
partner C_2H1G = 4.109270566451296
midpoint tip 2+log2 = 2.6931471805599454
```

Privacy/secret review for the explicit changed-file allowlist was done manually because this connector-only write path did not expose the repository scanner in-run. The files contain only QFORM mathematics and source commit identifiers; no credentials, personal data, notifications, task mutations, permissions, or unrelated material are present.
