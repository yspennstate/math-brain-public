SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T15:39:09Z.
attacking: scalar completion plus a bounded-density Schur remainder, using the newest volume-stability exit to pay a higher-rank opposite-sign branch without false independence.

# Scalar-square transfer over a bounded Schur remainder

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `fleet01/B11`  
Run: `20260923T153909Z-fleet01-B11-QFORM-auto11`  
Status: `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / NEWEST-CLAUDE-RESULT-APPLIED / PARTNER-RESULT-APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Fresh sources and exact obligation


The newest required volume-stability source used below is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

Its exact theorem says that if an ORIGINAL-coordinate cross block of a quadratic-plus-affine remainder satisfies

\[
M=M_0+E,\qquad s_3(M_0)\ge c_0>0,\qquad
\max_i(P_{\mathrm{range}(M_0)})_{ii}\le\frac12,\qquad
\|E\|_{op}\le c_0/16,
\]

then the remainder has a continuous `C_0` density with

\[
\|p_R\|_\infty\le {24\sqrt3 e\over5c_0}< {23\over c_0}.       \tag{1.1}
\]

All self blocks and affine terms are retained in that theorem.

The designated fleet02/B11 result actually used below is

`yspennstate/math-open-problems@15189fa11c0c752c1d9022c60e253a9e8d457df8`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260923T124731Z-fleet02-B11-QFORM-r31/REPORT.md`.

For its explicit six-coordinate target family with nonzero spectrum `{1,1,-1}`, partner Theorem 4.1 gives

\[
\boxed{\|p_{Q_*}\|_\infty\le12}                                      \tag{1.2}
\]

for every independent cap-one input law, with a continuous density. Removing the genuine square direction in that same family leaves the mandatory logarithmically singular opposite-sign rank-two product branch.

This run changes mechanism from the preceding four-row matching argument. The goal is to pay a higher-rank scalar/pair-completion branch by transferring a proved bound on the Schur remainder through a correlated scalar square. No post-rotation independence is used.

## 2. New theorem: bounded Schur density survives arbitrary scalar cross coupling

### Theorem 2.1 — `QFORM-SCALAR-SCHUR-DENSITY-TRANSFER-v1`

Let `X_0,Z_1,...,Z_m` be independent real random variables with probability densities bounded by one. Consider

\[
Q=aX_0^2+2X_0b^TZ+Z^TDZ+\ell_0X_0+\ell^TZ+c,\qquad a\ne0.          \tag{2.1}
\]

Define the exact scalar Schur remainder

\[
R(Z)=Z^T\left(D-{bb^T\over a}\right)Z
 +\left(\ell-{\ell_0\over a}b\right)^TZ
 +c-{\ell_0^2\over4a}.                                                \tag{2.2}
\]

Suppose `R` has a probability density satisfying

\[
\|p_R\|_\infty\le K<\infty.                                           \tag{2.3}
\]

Then `Q` has a density and

\[
\boxed{
\|p_Q\|_\infty\le 2\sqrt{ {2K\over |a|} } .}                        \tag{2.4}
\]

The shift of the scalar square may be an arbitrary function of the same `Z` that generates `R`; no independence between the completed square and the remainder is asserted or needed.

### Proof

Complete the scalar square exactly:

\[
Q=a\left(X_0+m(Z)\right)^2+R(Z),\qquad
m(Z)={b^TZ+\ell_0/2\over a}.                                          \tag{2.5}
\]

For every deterministic shift `m`, the pushforward of `a(X_0+m)^2` has density bounded by

\[
p_{a(X_0+m)^2}(y)\le |a|^{-1/2}|y|^{-1/2}                           \tag{2.6}
\]

on its appropriate half-line, because the two inverse branches each carry the Jacobian `1/(2\sqrt{|a y|})` and `f_{X_0}\le1`.

Condition on the ORIGINAL complement variables `Z`. Equation (2.6) is uniform in their value, so Tonelli/Fubini gives, for almost every `t`,

\[
p_Q(t)
\le |a|^{-1/2}\,\mathbb E|t-R|^{-1/2}.                               \tag{2.7}
\]

Now use only the marginal density cap (2.3). Layer cake gives

\[
\begin{aligned}
\mathbb E|t-R|^{-1/2}
&=\int_0^\infty
  \Pr\{|t-R|<u^{-2}\}\,du\\
&\le\int_0^\infty \min\{1,\,2K u^{-2}\}\,du\\
&=2\sqrt{2K}.                                                         \tag{2.8}
\end{aligned}
\]

The last equality splits at `u=\sqrt{2K}`. Combining (2.7)-(2.8) proves (2.4).

This argument is sign-free in `a`: a negative pivot is handled by reflection. It uses no moments, support bounds, log-concavity, connected support, or continuity of the input densities. QED.

### Why this does not violate the conditional-cap correction

The random shift `m(Z)` is generally correlated with `R(Z)`. We never call `X_0+m(Z)` independent of `R`. We condition on the original coordinates `Z`, use the translated scalar density cap pointwise in `Z`, and then average the resulting singular kernel against the **unconditional** law of `R`. Thus the live correction `conditional density cap != independence` is respected exactly.

## 3. Newest volume theorem applied at an actual inequality

Combining Theorem 2.1 with (1.1) gives the following higher-rank branch.

### Corollary 3.1 — `QFORM-SCALAR-PIVOT-PLUS-VOLUME-SCHUR-v1`

Under (2.1), suppose the Schur remainder (2.2) has an ORIGINAL-coordinate cross block satisfying the volume-stability hypotheses with scale `c_0`. Then

\[
\boxed{
\|p_Q\|_\infty
\le
2\sqrt{ {48\sqrt3 e\over5|a|c_0} }
< {13.447\over\sqrt{|a|c_0}}.}                                      \tag{3.1}
\]

The full form may have arbitrary scalar-to-complement cross coupling `b`; the bound is not a convolution argument.

### Concrete target-valid rotated family

Let

\[
M_0={1\over\sqrt2}\binom{I_3}{I_3}\in\mathbb R^{6\times3},\qquad
S=\begin{pmatrix}0&M_0\\M_0^T&0\end{pmatrix}\in\mathbb R^{9\times9}. \tag{3.2}
\]

Then all three singular values of `M_0` equal one and the row-range projection of `M_0` has every diagonal exactly `1/2`. For any `b\in\mathbb R^9` with `\|b\|_2\le1/4`, put

\[
A_b=
\begin{pmatrix}
2&b^T\\
b&2S+\frac12bb^T
\end{pmatrix}.                                                        \tag{3.3}
\]

The corresponding quadratic form completes exactly as

\[
X^TA_bX
=2\left(X_0+\frac12b^TZ\right)^2+2Z^TSZ.                         \tag{3.4}
\]

The Schur remainder has cross block `2M_0`, so the newest volume theorem applies with `c_0=2`, `E=0`, and gives

\[
K_R\le {12\sqrt3 e\over5}=11.2996853668\ldots.                       \tag{3.5}
\]

Theorem 2.1 therefore gives

\[
\boxed{\|p_{X^TA_bX}\|_\infty
\le2\sqrt{K_R}
=6.7230009272\ldots.}                                                 \tag{3.6}
\]

This is a genuinely cross-coupled family when `b!=0`.

It also satisfies the original target spectral hypothesis uniformly. At `b=0`, `diag(2,2S)` has four `+2` eigenvalues, three `-2` eigenvalues, and three zero eigenvalues. The perturbation in (3.3) has operator norm at most

\[
\|b\|+\frac12\|b\|^2\le\frac14+\frac1{32}=\frac9{32}.               \tag{3.7}
\]

Hence Weyl gives at least seven eigenvalues of modulus at least

\[
2-\frac9{32}={55\over32}>1.                                          \tag{3.8}
\]

Thus (3.6) is an actual inequality inside the full target class, not merely a matrix-algebra toy.

## 4. Required fleet02/B11 result applied to a cross-coupled target family

Let `A_*` be the explicit six-coordinate fleet02/B11 matrix from source (1.2). Its nonzero spectrum is exactly

\[
\{1,1,-1\},                                                           \tag{4.1}
\]

and partner Theorem 4.1 gives `\|p_{Z^TA_*Z}\|_\infty\le12`.

For any `b\in\mathbb R^6` with `\|b\|_2\le1/4`, define

\[
\widetilde A_b=
\begin{pmatrix}
2&b^T\\
b&2A_*+\frac12bb^T
\end{pmatrix}.                                                        \tag{4.2}
\]

Then

\[
X^T\widetilde A_bX
=2\left(X_0+\frac12b^TZ\right)^2+2Z^TA_*Z.                            \tag{4.3}
\]

Scaling the partner result by two gives

\[
\|p_{2Z^TA_*Z}\|_\infty\le6.                                        \tag{4.4}
\]

Theorem 2.1 applied with `a=2,K=6` now gives the new cross-coupled estimate

\[
\boxed{
\|p_{X^T\widetilde A_bX}\|_\infty
\le2\sqrt6
=4.8989794856\ldots.}                                                 \tag{4.5}
\]

This is an actual use of the completed designated partner theorem. When `b!=0`, (4.5) is not obtained by convolving the scalar square with the partner output: the square translation depends on the same `Z` that generates the partner remainder.

The family is target-valid. At `b=0` the nonzero eigenvalues are `2,2,2,-2`; the same perturbation estimate (3.7) implies that for `\|b\|\le1/4` at least the three positive eigenvalues remain at least `55/32>1` in magnitude (and the negative one also remains below `-55/32`). Hence (4.5) is a target-level indefinite cross-coupled inequality.

## 5. Opposite-sign logarithmic control and where the third direction enters

The mandatory rank-two obstruction is unchanged. For independent centered unit uniforms,

\[
p_{2XY}(t)=\log{1\over2|t|},\qquad0<|t|<1/2.                         \tag{5.1}
\]

The designated partner family contains exactly this mechanism: removing its `U^2` square leaves an opposite-sign/bilinear product with logarithmically divergent density, while the genuine third square contributes the missing Fresnel `|t|^{-1/2}` factor and the full partner form has density bounded by 12.

The present theorem is a **second-stage completion principle**. Once a genuinely rank-three/product-safe mechanism has paid an indefinite Schur remainder (by the partner Fresnel theorem, or by the newest three-volume theorem), an additional physical scalar pivot may be arbitrarily cross-coupled to that remainder. Completing the scalar square creates the half-order kernel `|y|^{-1/2}`; the already bounded remainder has uniformly finite half-Riesz potential (2.8), so the cross coupling cannot recreate the rank-two logarithmic singularity.

Thus this run does not claim that a rank-two saddle became bounded by itself. The third direction remains essential in the remainder theorem that supplies `K`.

## 6. What this pays and what remains unpaid

The new theorem removes a specific higher-rank interface that was previously left implicit:

> **paid:** a nonzero physical scalar pivot whose exact Schur remainder already lies in any dimension-free bounded-density branch can be reattached with arbitrary scalar-to-remainder coupling at cost only `2 sqrt(2K/|a|)`.

In particular, it composes directly with the newest volume-stability branch and with the designated fleet02/B11 null-sum branch, without an independence-after-completion error.

It does **not** prove that every indefinite target matrix possesses a scalar pivot `a` and Schur remainder scale `c_0` with `|a|c_0` bounded below. Such a claim would conflict with the live no-good-single-minor / low-cross-rank counterexamples. The estimate also deteriorates as `a->0`, so the genuinely zero/near-zero physical-diagonal chamber is not closed by this theorem.

The first B11 implication now is

`QFORM-INDEFINITE-SMALL-PIVOT-SCHUR-ALTERNATIVE-v1`:

> In the remaining `(+,+,-)` / `(+,-,-)` no-pivot geometry, prove an exhaustive product-preserving alternative that either (i) finds a scalar pivot and a bounded-density Schur remainder with `|a|K^{-1}` at a dimension-free scale, or (ii) forces one of the already-paid physical-pair, null-sum/Fresnel, volume-stability, ridge, ruled, or grouped-bank exits. The alternative must retain arbitrary additional spectrum and may not assert a universally good single physical minor.

The previous exact-rank-three near-star/matching-mass transition also remains open; this run deliberately changed mechanism rather than repeat the same matching estimate.

## 7. Continuity and verification

Theorem 2.1 proves existence of an essentially bounded density. It does **not** by itself prove continuity, even when the Schur remainder has a continuous density, because the translated scalar-square kernel depends on `Z` and the input density `f_0` may be fragmented. Continuity should therefore be recorded separately as OPEN for this transfer theorem.

The deterministic checker verifies the fleet02/B11 nonzero spectrum, the diffuse cross-block leverage `1/2`, the Weyl target floor `55/32`, and the constants in (3.5)-(4.5). Its executed output ends

`QFORM_B11_SCHUR_SQUARE_CHECK_PASS`.

No numerical histogram or simulation is used as evidence for the theorem.
