SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B04, 2026-09-22T18:17:02Z.
attacking: sharp decreasing-rearrangement control of the hyperbolic-pair logarithmic kernel, then a grouped rank-one bank lift over a partner-controlled residual.

# account02/B04 QFORM — logarithmic rearrangement and rank-one bank lift

Programme: `QFORM-DENSITY-3EIG-20260922`
Run: `B04-20260922T181702Z-dac07509`
Assignment: Product Fourier rearrangement
Outcome: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / LOCAL_SELECTION_COUNTEREXAMPLE / FULL_TARGET_OPEN`
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Fresh scope and first unpaid implication

Fresh owner control for this run is revision `2026-09-22.11`; QFORM remains the sole target. The live correction set was consumed before derivation. In particular this report does not use the false uniform one-dimensional pointwise Fresnel estimate, post-rotation independence, arbitrary-joint-density coarea, positive conditional-projection density moments, a universal good principal triple, or a one-Schur-extraction implication from the global spectral hypothesis.

The exact target remains: independent real physical coordinates with density caps at most one, arbitrary real symmetric `A`, and at least three eigenvalues with `|lambda|>=1`; prove a dimension-free density cap for `X^T A X` or give a true target-level counterexample.

The first unpaid implication at start was `QFORM-HYPERBOLIC-PAIR-SELECTION-v1`: in the unresolved high-leverage / near-isotropic branch, select a useful original-product mixed packet or route to an already controlled ridge/grouped branch. The prior B04 run paid the analytic cost of one physical pair only by the crude estimate `|c|^{-1}+4B`. This run strengthens that analytic step to a sharp logarithmic rearrangement, extends it from bounded residual density to a general Hölder small-ball residual, and then lifts a physical pair to a whole rank-one pair of disjoint original-coordinate banks. It also gives a source-valid family showing that any selection rule demanding a single mixed entry of constant size is false.

Named partner actually applied: account03/B04, theorem `QFORM-RANK2-SCHUR-NOLEVERAGE-v1`, canonical source
`yspennstate/math-open-problems@2761bd3896c56a1f929761e69035ba7cb8ebc2bc`,
path
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/B04-20260922T164839Z-r14/REPORT.md`,
report blob `fe77dd5ab13c1de27d93fc2ba0b8c9f637d4a523`.
Its theorem is used below in an actual all-input-law inequality, not merely cited.

## 2. Input from the preceding B04 run: the hyperbolic product envelope

For independent real `U,V` with densities at most one and `c!=0`, the preceding B04 report proved the translation-uniform envelope
\[
 p_{2cUV}(s)\le |c|^{-1}\left(1+\log_+\frac{2|c|}{|s|}\right)
 \qquad\text{for a.e. }s\ne0. \tag{2.1}
\]
The same estimate holds after arbitrary deterministic translations of `U,V`.

Consequently, if `Y,Z,W` are independent physical-coordinate groups, `Y,Z` are scalar cap-one coordinates,
\[
 Q=2cYZ+2Y L_1(W)+2Z L_2(W)+R(W),
\]
and
\[
 H(W)=R(W)-\frac{2L_1(W)L_2(W)}c,
\]
then conditioning on `W` and completing the product gives
\[
 Q=2c\left(Y+\frac{L_2(W)}c\right)
       \left(Z+\frac{L_1(W)}c\right)+H(W), \tag{2.2}
\]
hence
\[
 p_Q(t)\le |c|^{-1}\left[
 1+\mathbb E\log_+\frac{2|c|}{|t-H|}
 \right] \quad\text{for a.e. }t. \tag{2.3}
\]
No independence between `H` and either shift is asserted; (2.3) is uniform in the shifts after conditioning.

## 3. New sharp rearrangement: only a small-ball modulus of the residual is needed

Define
\[
 \Psi(m)=
 \begin{cases}
 m,&0\le m\le1,\\
 1+\log m,&m\ge1.
 \end{cases} \tag{3.1}
\]

### Theorem 3.1 — `QFORM-HYPERBOLIC-PAIR-HOLDER-TRANSFER-v1`

In the setting of (2.2), assume only that for some `0<alpha<=1` and `K>0`,
\[
 \sup_{t\in\mathbb R}\Pr(|H-t|<r)
 \le \min\{1,K r^\alpha\}
 \qquad(r>0). \tag{3.2}
\]
Then `Q` has an essentially bounded density and
\[
 \boxed{
 \|p_Q\|_\infty
 \le |c|^{-1}\left[
 1+\alpha^{-1}\Psi\!\left(K(2|c|)^\alpha\right)
 \right].
 } \tag{3.3}
\]

**Proof.**
Put `R0=2|c|`. For every nonnegative `d`,
\[
 \log_+\frac{R0}{d}
 =\int_0^\infty {\bf1}_{\{d<R0e^{-s}\}}\,ds.
\]
Tonelli and (3.2) give, uniformly in `t`,
\[
 \mathbb E\log_+\frac{R0}{|t-H|}
 \le\int_0^\infty
 \min\{1,M e^{-\alpha s}\}\,ds,\qquad
 M=K R0^\alpha. \tag{3.4}
\]
If `M<=1`, the integral equals `M/alpha`. If `M>=1`, split at
`s_0=(\log M)/alpha`; the integral is
`(\log M+1)/alpha`. Thus (3.4) equals
`alpha^{-1} Psi(M)`. Substitute in (2.3). QED.

This is a decreasing-rearrangement/layer-cake estimate. It does not ask for a pointwise characteristic-function decay estimate.

### Corollary 3.2 — bounded-density residual, sharp bathtub form

If `H` has density bounded by `B`, then
\[
 \Pr(|H-t|<r)\le\min\{1,2Br\}.
\]
Thus Theorem 3.1 with `alpha=1`, `K=2B` yields
\[
 \boxed{
 \|p_Q\|_\infty
 \le |c|^{-1}\left[1+\Psi(4|c|B)\right].
 } \tag{3.5}
\]
This strictly improves the preceding B04 estimate
`|c|^{-1}+4B` whenever `4|c|B>1`, replacing a linear residual-density cost by a logarithm.

Equivalently, (3.5) is the exact bathtub bound under only `0<=p_H<=B` and total mass one: among all such residual densities, the logarithmic kernel in (2.3) is maximized by filling the central interval at height `B`.

## 4. Rank-one quadratic residual and a sharper zero-diagonal packet

### Lemma 4.1 — scalar quadratic small ball

Let `X` have density at most one and let
\[
 h(X)=aX^2+dX+e,\qquad a\ne0.
\]
Then for every `t` and `r>0`,
\[
 \Pr(|h(X)-t|<r)
 \le \min\left\{1,\,2\sqrt{\frac{2r}{|a|}}\right\}. \tag{4.1}
\]

**Proof.**
Complete the square, so only sets
`{|y^2-s|<r/|a|}` matter. If `s<=r/|a|`, their total length is at most
`2 sqrt(2r/|a|)`. If `s>r/|a|`, the total length is
\[
2\left(\sqrt{s+r/|a|}-\sqrt{s-r/|a|}\right)
\le2\sqrt{2r/|a|}.
\]
The probability is at most the Lebesgue length because the density cap is one. QED.

Apply Theorem 3.1 with `alpha=1/2` and
`K=2sqrt(2/|a|)`. Then
\[
 \boxed{
 \|p_Q\|_\infty
 \le |c|^{-1}\left[
 1+2\Psi\!\left(4\sqrt{\frac{|c|}{|a|}}\right)
 \right].
 } \tag{4.2}
\]

### Corollary 4.2 — `QFORM-TWO-ZERO-DIAGONAL-PACKET-LOG-v2`

For independent cap-one `X,Y,Z`, let
\[
 M=\begin{pmatrix}
 d&r&s\\ r&0&c\\ s&c&0
 \end{pmatrix},
 \qquad c\ne0,\quad\det M\ne0,
\]
and allow arbitrary affine terms (including coefficients fixed after conditioning on outside coordinates). Then the quadratic polynomial has a density satisfying
\[
 \boxed{
 \|p\|_\infty
 \le |c|^{-1}\left[
 1+2\Psi\!\left(
 \frac{4|c|^{3/2}}{\sqrt{|\det M|}}
 \right)\right].
 } \tag{4.3}
\]
Indeed completing the `YZ` product leaves a scalar quadratic in `X`
with coefficient
\[
 \kappa=d-\frac{2rs}{c}
 =-\frac{\det M}{c^2}. \tag{4.4}
\]
Equation (4.3) follows from (4.2).

If additionally `sigma_min(M)>=1`, the inverse-entry identities used in the preceding B04 packet proof give
\[
 |\det M|\ge c^2,\qquad |c|\ge\frac12. \tag{4.5}
\]
For completeness:
`|(M^{-1})_{11}|=c^2/|\det M|<=1`;
also `r^2,s^2<=|\det M|` and
`|rs-cd|<=|\det M|`, while
`\det M=c[rs+(rs-cd)]`, so
`|\det M|<=2|c||\det M|`.
Therefore the argument of `Psi` in (4.3) is at most `4sqrt(|c|)`.
For `|c|>=1/2` this argument is already above one, and
\[
 F(x)=x^{-1}\left(3+2\log4+\log x\right)
\]
is decreasing for `x>=1/2`. Hence
\[
 \boxed{
 \|p\|_\infty
 \le 2(3+\log8)
 =10.1588830834\ldots .
 } \tag{4.6}
\]
This improves the preceding packet constant `2+8sqrt(2)<13.314`.

## 5. New aggregate step: a whole rank-one pair of original-coordinate banks

The physical-pair transfer can be lifted without rotating the product law when each active scalar is itself a linear projection of a **disjoint** bank.

Let `I,J,W` be pairwise disjoint sets of original coordinates. Put
\[
 U=u^\top X_I,\qquad V=v^\top X_J,\qquad
 s=\|u\|_2,\quad t=\|v\|_2,\quad \sigma=st>0.
\]
The standard one-dimensional product-projection theorem used in the
account03/B04 source gives
\[
 \|p_U\|_\infty\le\frac{\sqrt2}{s},\qquad
 \|p_V\|_\infty\le\frac{\sqrt2}{t}. \tag{5.1}
\]
Since the banks are disjoint, `U,V` are independent.

Consider
\[
 Q=2UV+2U L_1(W)+2V L_2(W)+R(W),\qquad
 H=R-2L_1L_2. \tag{5.2}
\]
Scale
\[
 U'=\frac{\sqrt2}{s}U,\qquad
 V'=\frac{\sqrt2}{t}V.
\]
Then `U',V'` are independent with density caps at most one and
\[
2UV=2(\sigma/2)U'V'.
\]
The scaled shifts in (5.2) complete to the same residual `H`.

### Theorem 5.1 — `QFORM-RANK1-BANK-HOLDER-LIFT-v1`

If `H` satisfies (3.2), then
\[
 \boxed{
 \|p_Q\|_\infty
 \le \frac2{\sigma}
 \left[
 1+\alpha^{-1}\Psi(K\sigma^\alpha)
 \right].
 } \tag{5.3}
\]
If `H` instead has density cap `B`, then
\[
 \boxed{
 \|p_Q\|_\infty
 \le \frac2{\sigma}\left[1+\Psi(2\sigma B)\right].
 } \tag{5.4}
\]

This pays the **aggregate singular scale** `sigma=||u||_2||v||_2`.
No individual physical coefficient `u_i v_j` needs to be bounded below.
The scope is exact: the bank variables may enter the form through `U,V`
and the displayed aligned shifts only. Arbitrary in-bank quadratic
leakage or a misaligned second cross singular direction is not being
declared independent and is not covered by this theorem.

## 6. Source-valid local-selection counterexample and explicit rotated target estimate

Take any integer `m>=1`,
\[
 u=v=m^{-1/2}(1,\ldots,1)\in\mathbb R^m,
\]
and the `(2m+1)`-dimensional symmetric matrix
\[
 A_m=
 [1]\oplus
 \begin{pmatrix}
 0&uv^\top\\
 vu^\top&0
 \end{pmatrix}. \tag{6.1}
\]
Its spectrum is exactly
\[
 \{1,1,-1,0,\ldots,0\}. \tag{6.2}
\]
Thus it lies in the exact target for every `m`: exactly three
eigenvalues have modulus at least one, the form is indefinite, and the
`+1/-1` eigenvectors are genuinely spread over the two original
coordinate banks.

Every nonzero physical mixed coefficient in the bank block equals
`1/m`, so no universal selection lemma can demand a single
constant-size physical hyperbolic coefficient from the bare target
hypothesis.

Nevertheless let `X_0` be the singleton coordinate and
`U=u^T X_I`, `V=v^T X_J`. Then
\[
 Q=X_0^2+2UV.
\]
Here `sigma=1`. Lemma 4.1 for `H=X_0^2` gives
`alpha=1/2`, `K=2sqrt2`. Theorem 5.1 yields the dimension-free,
all-input-law estimate
\[
 \boxed{
 \|p_Q\|_\infty
 \le2\left[1+2\Psi(2\sqrt2)\right]
 =2(3+\log8)
 =10.1588830834\ldots .
 } \tag{6.3}
\]
Thus the correct selector must be aggregate (a bank singular value,
ridge effective dimension, or another grouped certificate), not a
single large entry.

This is a counterexample only to the **local-pair selection mechanism**,
not to QFORM.

## 7. Actual named-partner inequality and improved fully coupled example

The completed account03/B04 theorem states that if an effective
residual has a nonzero physical scalar pivot `a` and rank-two Schur
complement with nonzero eigenvalues `mu_1,mu_2`, then
\[
 B:=\|p_H\|_\infty
 \le C_* |a|^{-1/2}|\mu_1\mu_2|^{-1/4},\qquad
 C_*=23.390590510770\ldots . \tag{7.1}
\]
Substituting this **actual partner inequality** into (3.5) gives
\[
 \boxed{
 \|p_Q\|_\infty
 \le |c|^{-1}
 \left[
 1+\Psi\!\left(
 4|c|C_*|a|^{-1/2}|\mu_1\mu_2|^{-1/4}
 \right)
 \right].
 } \tag{7.2}
\]
This replaces the preceding B04 combination
`|c|^{-1}+4C_*|a|^{-1/2}|mu_1mu_2|^{-1/4}`
by logarithmic dependence in the large-residual regime.

Apply (7.2) to the preceding B04 fully coupled six-coordinate rotated
indefinite example. There `c=1/2`, and the partner's sharper heavy-row
analysis gives
\[
 B_{\rm partner}=9.8345318556.
\]
The old transfer gave `41.3381274224`. The new rearrangement gives
\[
 \boxed{
 \|p_Q\|_\infty
 \le2\left[2+\log(19.6690637112)\right]
 =9.9580940629.
 } \tag{7.3}
\]
The matrix and its checked eigenvalues are unchanged from the preceding
report:
\[
(-1.997504888364,-0.500189249266,\approx0,
0.499951120822,1.869581593576,2.143161423232).
\]
Hence at least three eigenvalues have modulus greater than one, both
signs are present, the physical matrix has nontrivial couplings, and the
estimate is uniform over all admissible independent input laws. No
post-rotation independence is used.

## 8. Conditional end-to-end route and first remaining implication

The current proof route is now:

1. use the completed spectral-window/ridge branch whenever the
   high-spectrum projection is sufficiently diffuse;
2. in the complementary high-leverage branch, use a scalar-pivot /
   rank-two-Schur certificate when available (account03/B04);
3. if the near-isotropic geometry exposes an aligned rank-one pair of
   disjoint original-coordinate banks, Theorem 5.1 pays that entire
   bank at aggregate scale even when every physical entry tends to zero;
4. if it exposes a physical two-zero-diagonal three-coordinate packet,
   Corollary 4.2 pays it with the sharper logarithmic constant;
5. otherwise an additional routing theorem is still needed.

The first unpaid implication is therefore sharpened to

`QFORM-RANK1-BANK-OR-RIDGE-ROUTING-v1`:

> In every unresolved high-leverage / near-isotropic target matrix,
> either obtain a one-scale ridge certificate already covered by the
> completed ridge theorem, or obtain a product-preserving grouped
> packet whose active cross dependence is an aligned rank-one bank over
> a residual with a completed density/small-ball certificate, or pass to
> another already completed packet branch.

The new family (6.1) proves that this statement cannot be weakened to
“find one physical mixed entry bounded below by an absolute constant”.
What remains genuinely open is **misaligned in-bank leakage / several
overlapping cross singular directions on the same original coordinates**.
That is the next B04 interface. Arbitrary additional spectral
components cannot simply be dropped.

Full QFORM remains OPEN. There is no target-level counterexample,
continuity claim, novelty claim, or full-proof claim in this report.

## 9. Exact calculation record

The committed checker `check.py` evaluates the displayed constants and
the spectrum of (6.1) for representative bank sizes. Its saved output is
`check_output.txt`. The calculation is finite supporting evidence only;
the theorems above are analytic.

No external data, private transcripts, credentials, scheduler
identifiers, benchmark material, machine paths, email, or remote
workflow were used.
