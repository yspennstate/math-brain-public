# fleet02/B02 — regularized-determinant review and elementary-symmetric integrated Fourier bound

Run: `20260922T140817Z-fleet02-B02-qform-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
Slot: B02, Integrated Fourier estimate  
Status: `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution context: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and first unpaid implication

The full target remains open: for independent real coordinates with densities bounded by one and a real symmetric matrix A with at least three eigenvalues of modulus at least one, prove a dimension-free essential density bound for Q=X^TAX, or give a valid counterexample.

The later owner continuation `QFORM-EXCLUSIVE-CONTINUE-20260922T131746Z` assigns fleet02/B02 an independent review of Sections 3--6 of the interactive regularized-determinant proof at

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a:proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`.

I reviewed exactly that scope and then continued the B02 integrated-Fourier assignment. The first universal unpaid implication remains structural: starting only from the three-large-eigenvalue hypothesis, produce a product-preserving decomposition to which an integrable Fourier estimate applies. The new result below improves the determinant branch by aggregating all coordinate minors rather than paying one selected tiny minor, but does not prove such a decomposition always exists.

## 2. Independent review of the regularized determinant proof, Sections 3--6

**Verdict: PASS on Sections 3--6, with the stated hypotheses and constants.** I found no sign, exponent, orientation, or normalization error in this scope. This is not a review of Section 7's MSS passage; fleet03/B04 was separately assigned that part.

### 2.1 Scalar sharp-constant checks

Use the report's Fourier convention `hat f(s)=int exp(isx)f(x)dx` and Beckner's sharp constants

`C_p = p^(1/(2p)) / (p')^(1/(2p'))`.

For the difference density `g=f*tilde f`, choose `p=2/(1+c)` and `r=1/c` in sharp Young. Then `2/p=1+1/r` and direct simplification gives

`C_p^2/C_r = 2^c c^(c/2)(1+c)^(-(1+c)/2)`,

which is exactly (3.1), since `||f||_p<=1` follows from `0<=f<=1` and `||f||_1=1`.

For `h=|hat f|^q`, set the Hausdorff--Young output exponent to `q/c`, so the input exponent is `q/(q-c)`. The condition `q/c>=2` is exactly `c<=q/2`. Raising the sharp Hausdorff--Young estimate to the q-th power gives

`||h||_(1/c) <= (2pi)^c q^(q/2-c)(q-c)^(-(q-c)/2)c^(c/2)`,

which is exactly (3.2).

For

`G(c)=2^c(1+c)^(-(1+c)/2)`,
`H_q(c)=q^(q/2-c)(q-c)^(-(q-c)/2)`,

one has `(log G)''=-1/[2(1+c)]` and `(log H_q)''=-1/[2(q-c)]`, so the tangent bounds used in (3.3)--(3.4) have the correct direction. The first tangent is at c=1 and the second at c=0.

External source pins consumed: William Beckner, *Inequalities in Fourier analysis*, Annals of Mathematics 102 (1975), 159--182, DOI 10.2307/1970980; and Livshyts--Paouris--Pivovarov, arXiv:1507.07949 for the normalized geometric Brascamp--Lieb framework used by the source report.

### 2.2 Graph Brascamp--Lieb change of variables

In Section 4 set

`M=alpha I + a^2 R R^T`,
`v_i=sqrt(alpha) M^(-1/2)e_i`,
`w_j=a M^(-1/2)r_j`,
`c_i=||v_i||^2`, `d_j=||w_j||^2`.

Then

`sum_i v_i v_i^T + sum_j w_j w_j^T = I`.

After `x=M^(-1/2)z`, normalize `v_i,w_j` to unit vectors. For the i-th difference-density factor, the scalar argument is `(sqrt(c_i)/sqrt(alpha)) <v_i/||v_i||,z>`. Writing the Brascamp--Lieb input as the `1/c_i` power of this factor contributes exactly

`alpha^(c_i/2)c_i^(-c_i/2)||g_i||_(1/c_i)`.

For the j-th Fourier factor the corresponding contribution is

`d_j^(-d_j/2)||h_j||_(1/d_j)`.

Thus the powers in (4.2), including the easily missed `alpha^(c_i/2)` term, are correct.

Let `theta=sum_j d_j=sum_i(1-c_i)`. Inserting (3.1)--(3.2) cancels the `c_i^(c_i/2)` and `d_j^(d_j/2)` factors. The tangent bounds give the remaining exponential factor

`exp([1-log(2q)/2] theta)`.

With `alpha=pi^2 e^2 (2/q)`, the residual multiplier is exactly

`[2pi exp(1-log(2q)/2)/sqrt(alpha)]^theta = 1`.

Therefore (4.1) follows with no lost dimension-dependent constant.

### 2.3 Projection orientation

The all-frequency sufficient condition is also oriented correctly. The matrix with diagonal entries d_j is

`D(a)=a^2 R^T(alpha I+a^2RR^T)^(-1)R`.

By SVD its nonzero eigenvalues are `a^2 s_l^2/(alpha+a^2 s_l^2)<=1`, on `range(R^T)`, hence

`0 <= D(a) <= P_range(R^T)`.

In Section 5 the application uses `R=B^T`, with the columns of R indexed by the original coordinates in I. Therefore `range(R^T)=range(B)` is a subspace of `R^I`, exactly matching condition (5.1). There is no transpose-side mismatch.

### 2.4 Cauchy--Schwarz/Jensen exponent

After conditioning outside `I union J`, write the form as

`q_I(X)+q_J(Y)+2 X^T B Y+c`.

Cauchy--Schwarz in X removes the arbitrary self phase `q_I`, expansion introduces independent copies `Y,Y'`, and the remaining X expectation factorizes in the original independent coordinates:

`|phi(t)|^2 <= E_(Y,Y') prod_(i in I)|hat f_i(2t[B(Y-Y')]_i)|`.

For `q>=1`, convex Jensen gives

`|phi(t)|^(2q) <= E prod_(i in I)|hat f_i(...)|^q`.

Applying Section 4 with `R=B^T`, `a=2t`, and then taking the `1/(2q)` power gives precisely

`|phi(t)| <= det(I+2q t^2 BB^T/(pi^2 e^2))^(-1/(4q))`.

For q=2 the leverage condition disappears because `d_j<=1=q/2`; the exponent becomes `-1/8`, not `-1/4`. This is the correct decoupling loss and should not be conflated with B02's earlier exact square-cross-block Plancherel theorem.

### 2.5 Section 6 integration

If at least r singular values are at least sigma, the determinant bound gives

`|phi(t)| <= (1+beta^2 t^2)^(-r/(4q))`,
`beta=sqrt(2q)sigma/(pi e)`.

For `r>2q`, exact integration gives

`||p_Q||_infinity <= e sqrt(pi)/(2 sqrt(2q)sigma) * Gamma(r/(4q)-1/2)/Gamma(r/(4q))`.

The simpler split against `min(1,(beta|t|)^(-r/(2q)))` gives

`||p_Q||_infinity <= e r/[sqrt(2q) sigma (r-2q)]`.

All three sample constants in Section 6 check: q=2,r=5 gives `5e/(2sigma)`; q=4/3,r=3 gives `9e sqrt(3/8)/sigma`; q=1,r=3 gives `3e/(sqrt(2)sigma)`.

## 3. New result: elementary-symmetric integrated determinant bound

The regularized determinant theorem is stronger than a threshold statement about the k-th singular value. It yields a coordinate-minor aggregate bound which survives the archived `QFORM-CROSSMINOR-ALONE-FALSE` correction.

### Theorem `QFORM-EK-INTEGRATED-DETERMINANT-v1`

Let `B=A[I,J]` be an original-coordinate cross block. Fix `1<=q<=2`. If `q<2`, assume

`max_i (P_range(B))_(ii) <= q/2`

on the I-side; for q=2 no leverage hypothesis is required. Let `s_1,...,s_r` be the nonzero singular values of B and define

`E_k(B)=e_k(s_1^2,...,s_r^2)`.

For every integer k with `k>2q` and `E_k(B)>0`,

`|phi_Q(t)| <= [1 + (2q/(pi^2 e^2))^k E_k(B) t^(2k)]^(-1/(4q))`.

Consequently

`||phi_Q||_1 <= [pi e/(k sqrt(2q))] * BETA(1/(2k), 1/(4q)-1/(2k)) * E_k(B)^(-1/(2k))`,

and Q has a continuous density vanishing at infinity with

`||p_Q||_infinity <= [e/(2k sqrt(2q))] * BETA(1/(2k), 1/(4q)-1/(2k)) * E_k(B)^(-1/(2k))`.

#### Proof

From the reviewed determinant theorem, with `c_q=2q/(pi^2 e^2)`,

`|phi_Q(t)| <= det(I+c_q t^2 BB^T)^(-1/(4q))`.

Expanding the determinant in elementary symmetric polynomials gives

`det(I+c_q t^2 BB^T)=sum_{ell=0}^r c_q^ell e_ell(s_1^2,...,s_r^2)t^(2ell)`.

Every coefficient is nonnegative. Keeping only the ell=0 and ell=k terms yields the pointwise estimate in the theorem. For `a=1/(4q)` and `gamma=c_q^k E_k(B)`,

`int_R (1+gamma t^(2k))^(-a) dt`
` = gamma^(-1/(2k))/k * BETA(1/(2k),a-1/(2k))`,

which is finite exactly when `k>2q`. Since `c_q^(-1/2)=pi e/sqrt(2q)`, the displayed L1 and density constants follow from Fourier inversion.

Finally Cauchy--Binet gives the coordinate-minor identity

`E_k(B)=sum_{|S|=|T|=k} det(B[S,T])^2`.

Thus the theorem pays for the **sum of squared k-by-k minors**, not one selected minor. A family may have every individual minor tiny while this aggregate remains dimension-free.

### Useful instances

1. q=1, leverage at most 1/2, k=3:

`||p_Q||_infinity <= [e/(6sqrt(2))] BETA(1/6,1/12) E_3(B)^(-1/6)`
` < 5.656 E_3(B)^(-1/6)`.

If B has exactly rank three, `E_3=(s_1s_2s_3)^2`, so this is `<5.656 (s_1s_2s_3)^(-1/3)`. It is weaker in constant than B02's earlier exact square-rank-three Plancherel bound `3sqrt(2) Delta^(-1/3)`, but unlike the reciprocal-all-singular-value mechanism it remains valid with arbitrarily many additional tiny singular values.

2. q=2, no leverage assumption, k=5:

`||p_Q||_infinity <= [e/20] BETA(1/10,1/40) E_5(B)^(-1/10)`
` < 6.771 E_5(B)^(-1/10)`.

This is the unconditional aggregate-five-direction branch.

3. q=4/3, leverage at most 2/3, k=3:

`||p_Q||_infinity < 14.907 E_3(B)^(-1/6)`.

The numerical constants were evaluated only as regressions of the exact beta-function formulas; the exact displayed formulas are authoritative.

## 4. Named partner result applied to the complementary rank-two obstruction

I consumed the completed named-partner result fleet03/B02, canonical report

`yspennstate/math-open-problems@2e9ab3bfa05919cd9115fc5f6285ee0683adfb7c:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T130245Z-fleet03-B02-QFORM-r11/REPORT.md`.

Its theorem `QFORM-AGGREGATED-HYPERBOLIC-SQUARE-v1` says that for disjoint original-coordinate groups,

`T=2a X U+H(U)+b[V+theta(U)]^2`

with `U=alpha.Y`, `V=beta.Z`, has

`||p_T||_infinity <= 2^(11/4)/(sqrt(|ab|) ||alpha||_2^(1/2)||beta||_2)`.

Apply this to the target-level star-plus-square family

`Q=2 X_0(alpha.Y)+(beta.Z)^2`.

Its three nonzero eigenvalues are `+||alpha||_2`, `-||alpha||_2`, and `||beta||_2^2`. Hence under the target threshold `||alpha||_2>=1`, `||beta||_2>=1`,

`||p_Q||_infinity <= 2^(11/4) < 6.728`.

This is genuinely complementary to the new `E_k` determinant branch. For this star-plus-square matrix, **every original-coordinate cross block has rank at most two**: the star component contributes cross rank at most one and the beta-beta^T square block contributes cross rank at most one. Hence `E_3(B)=0` for every cut B. The partner theorem therefore closes an actual target family on which every k=3 determinant-minor aggregate vanishes. This is an explicit reason not to replace the structural debt by an unsupported universal rank-three-cut hypothesis.

## 5. What is now paid and what remains open

Paid:

- independent PASS of the interactive regularized-determinant proof Sections 3--6, including sharp Young/Hausdorff--Young constants, the graph Brascamp--Lieb scaling powers, the Jensen/decoupling exponent, the projection orientation, and the Section 6 inversion constants;
- a new integrated-Fourier consequence controlled by elementary-symmetric singular-value mass / the sum of squared coordinate minors;
- actual application of the named fleet03/B02 aggregate-star theorem to a three-large-eigenvalue family where all cross-block `E_3` resources vanish.

Not paid:

- no theorem yet forces, from the bare three-large-eigenvalue hypothesis, either a leverage-controlled cut with dimension-free `E_3`, an unconditional cut with dimension-free `E_5`, or a partner-type product-preserving aggregate-star/Schur representation;
- arbitrary additional nonseparable eigendirections can still cancel cross-block structure extracted from a selected three-dimensional spectral subspace;
- therefore the full target remains OPEN.

A plausible next structural statement is an **aggregate determinant-or-bank dichotomy**: either some original-coordinate cut has leverage-compatible `E_3` (or unconditional `E_5`) bounded below at universal scale, or the matrix admits a low-cross-rank product-bank decomposition to which the partner aggregate-star/Schur estimates apply. The current corrections rule out replacing that statement by a fixed-minor or single-pivot assertion.

## 6. Correction and source discipline

Consumed live corrections include `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-BOUNDED-DIAMETER-LOCALIZATION-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`, and `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`. None is used as a positive premise.

The LPP source confirms the standard product-marginal setting and the sharp `2^(k/2)` marginal-density scale; Beckner is the source for the sharp Fourier/Young constants. No law-uniform pointwise Fresnel decay, post-rotation independence, conditional-cap-for-independence substitution, or fixed-minor extraction is used.

## 7. Exact algebra regression

A symbolic check in this run returned:

- sharp Young constant ratio for (3.1): `1`;
- regularized-graph normalization bracket: `1`;
- beta-function density constants: q=2,k=5 -> `6.770121056044`; q=1,k=3 -> `5.65576377338724`; q=4/3,k=3 -> `14.9061455946889`.

The Hausdorff--Young constant simplification is algebraically exact for `0<c<q`: after substituting `p=q/(q-c)`, one gets `c^(c/2) q^(q/2-c)(q-c)^(-(q-c)/2)`. Finite numerical checks are regressions only and are not used as universal proof certificates.

## 8. Status

`ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.

This report is a scoped independent review plus a new supporting theorem. It is not a full proof of the quadratic-form conjecture and makes no novelty or priority claim.
