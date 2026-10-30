# fleet03/B06 — all-finite-Lp curved-fiber payment without transverse diffuseness

**Run:** `20260922T141942Z-fleet03-B06-qform-curved-fiber-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Curved fiber integration  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction-aware starting point

The target remains the full arbitrary-law statement: for every dimension `n`, independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric matrix `A` having at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has a density with one universal essential-supremum bound, or give a valid counterexample. Continuity is a separate desired conclusion and is not inferred from essential boundedness or absolute continuity.

This run does **not** use any of the retired mechanisms: no law-uniform pointwise quadratic-phase decay, no independence after diagonalizing `A`, no unrestricted spectral-fiber supremum, no generic X-ray-only control of an indefinite trace, no bounded conditional-density surrogate for original-coordinate independence, and no assumption that a uniformly good physical minor or Schur pivot exists.

The immediate starting point is the previous B06 heavy-isotropic normal form, source-pinned at

`yspennstate/math-open-problems@505e316c1806a352965a5781bdaa2f81929f0f42`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260922T132210Z-fleet03-B06-qform-curved-r12/REPORT.md`.

That report paid the same branch under the extra transverse-diffuseness condition `y_j^2+z_j^2<=1/2`. The present run changes mechanism: it conditions on the genuinely independent heavy physical coordinate and uses a sharp product-projection density bound plus a nonendpoint fractional-integration estimate. The transverse-diffuseness hypothesis disappears completely from the new statements below.

## 2. Other-worker results actually consumed

The assigned partner is `fleet04/B06`. At startup and again during this run, no completed current-QFORM artifact existed at the canonical shared handoff root for `fleet04/B06`; no partner PASS or theorem is fabricated.

Two compatible completed results are actually used.

1. **Product projection density.** fleet03/B02 records the sharp one-dimensional product projection estimate, sourced to Rogozin/Ball and Rudelson--Vershynin: if independent coordinates have densities at most one and a coefficient vector has Euclidean norm one, then the linear combination has density at most `sqrt(2)`. Source used here:

   `yspennstate/math-open-problems@18fb381e300dd86514835d27eedcf2507ab09227`

   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T130245Z-fleet03-B02-QFORM-r11/REPORT.md`.

2. **Compatible completed fleet04 result.** fleet04/B18 proves `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`. The source proof contains the kernel domination

   `p_{R+aV_R^2}(t) <= |a|^(-1/2) int p_R(r)|t-r|^(-1/2) dr`

   on the appropriate one-sided half-line, whenever the conditional density of `V_R` is at most one. The final theorem in that report assumes `p_R in L^infinity`; Section 6 below applies the **displayed proof inequality itself** to the new `L^4` bank proved here. Exact source:

   `yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

This is an actual inequality-level application of a completed fleet04 result, not a status-only citation.

## 3. Heavy-isotropic rank-three normal form and a spectral coefficient fact

Work in the exact rank-three indefinite heavy-isotropic state already isolated in the B06/B10 chain. In an orthonormal spectral basis `(e,f,g)`, after the isotropic heavy row is aligned with `e`, write

`Lambda = [[0,B,0],[B,r,s],[0,s,tau]]`,                              (3.1)

and let the heavy original-coordinate row be

`u_i=sqrt(c)e`, with `c>1/2`.                                        (3.2)

For every residual original coordinate `j!=i`, write

`u_j=s_j e+y_j f+z_j g`,

and define the original-product linear aggregates

`T=sum_{j!=i} s_j X_j`, `Y=sum_{j!=i} y_j X_j`, `Z=sum_{j!=i} z_j X_j`. (3.3)

The Parseval relations include

`sum y_j^2=sum z_j^2=1`, `sum y_j z_j=0`,
`sum s_j y_j=sum s_j z_j=0`, `sum s_j^2=1-c`.                        (3.4)

The quadratic form is exactly

`Q=2B(sqrt(c)X_i+T)Y+rY^2+2sYZ+tau Z^2`.                            (3.5)

No independence is claimed among `(T,Y,Z)`; they are correlated linear images of the same residual product coordinates. The only independence used below is the genuine original-coordinate fact

`X_i independent of (T,Y,Z)`.                                       (3.6)

Because all three eigenvalues of the symmetric `Lambda` have modulus at least one,

`||Lambda^(-1)||_op <=1`.                                            (3.7)

A direct inverse calculation gives

`Lambda^(-1)=
 [[(-r tau+s^2)/(B^2 tau), 1/B, -s/(B tau)],
  [1/B,                         0,     0],
  [-s/(B tau),                  0,   1/tau]]`.                        (3.8)

Every matrix entry has modulus at most the operator norm, hence

`|B|>=1`, `|tau|>=1`.                                                 (3.9)

This strengthens the determinant-only identity `|det Lambda|=B^2|tau|>=1` in this exact three-large-eigenvalue normal form.

## 4. New theorem: all finite Lp norms, with no transverse-diffuseness condition

### Theorem 4.1 — `QFORM-HEAVY-ISOTROPIC-ALL-FINITE-LP-v1`

Under (3.1)--(3.6), with all three eigenvalues of `Lambda` of modulus at least one and arbitrary independent original-coordinate input densities `0<=f_j<=1`, the law of `Q` is absolutely continuous. For every finite `p>1`,

`||p_Q||_p
 <= p [ sqrt(2)/( |B| sqrt(c) ) ]^(1-1/p)
 <= p 2^(1-1/p).`                                                    (4.1)

No hypothesis of the form `y_j^2+z_j^2<=1/2` is needed. No moment, support, connectedness, log-concavity or smoothness hypothesis is used.

#### Proof

By (3.4), the coefficient vector `(y_j)_{j!=i}` has Euclidean norm one. The product-projection theorem cited in Section 2 therefore gives a density `m` for `Y` satisfying

`||m||_infinity <= sqrt(2)`.                                         (4.2)

In particular `P(Y=0)=0`.

Let `omega` denote the residual variables `(X_j)_{j!=i}` and abbreviate

`C(omega)=2B T Y+rY^2+2sYZ+tau Z^2`,
`a=2B sqrt(c)`.                                                       (4.3)

Condition on `omega`. For `Y(omega)!=0`, (3.5) is affine in the still-independent original coordinate `X_i`:

`Q=aY X_i+C`.                                                         (4.4)

Its conditional density is

`q_omega(t)= 1/(|aY|) f_i((t-C)/(aY)).`                              (4.5)

Because `0<=f_i<=1` and `int f_i=1`, for every `p>1`,

`int q_omega(t)^p dt
 = |aY|^(1-p) int f_i(x)^p dx
 <= |aY|^(1-p)`.                                                      (4.6)

Put `beta=1-1/p in (0,1)`. Then

`||q_omega||_p <= |aY|^(-beta)`.                                     (4.7)

The exceptional set `Y=0` has residual probability zero, so mixing (4.5) gives an unconditional density. Minkowski's integral inequality yields

`||p_Q||_p <= |a|^(-beta) E|Y|^(-beta)`.                             (4.8)

It remains to estimate a one-dimensional negative moment. Among probability densities bounded by a number `H`, the integral against the symmetric decreasing kernel `|y|^(-beta)` is maximized by filling the interval nearest zero. Thus

`int |y|^(-beta)m(y)dy
 <= 2H int_0^(1/(2H)) y^(-beta)dy
 = (2H)^beta/(1-beta).`                                              (4.9)

With `H=sqrt(2)` and `1/(1-beta)=p`, (4.8) gives

`||p_Q||_p
 <= p [2sqrt(2)/|a|]^beta
 = p [sqrt(2)/(|B|sqrt(c))]^beta`,                                   (4.10)

which is the first bound in (4.1). By (3.2) and (3.9), `|B|sqrt(c)>1/sqrt(2)`, so the bracket in (4.10) is at most two. This proves the universal bound in (4.1). QED.

### What this theorem does and does not use

The curved terms involving `Z` and `tau` remain inside the conditional translation `C`; they are not thrown away probabilistically, but the proof does not yet spend their curvature. That is why the conclusion stops at every finite `L^p` rather than `L^infinity`.

This endpoint distinction is real. A rank-two hyperbolic product such as `XY` for independent interval-uniform inputs has a logarithmically unbounded density while belonging to every finite `L^p`. Therefore (4.1), by itself, cannot be promoted to the target density bound. The result is a nonendpoint bank intended to be combined with a source-valid curved smoothing step.

## 5. New corollary: a uniform half-Riesz bank without transverse diffuseness

The previous B06 half-Riesz estimate required transverse diffuseness. Theorem 4.1 removes that requirement by taking any `p>2`; choosing `p=4` makes the constants explicit.

From (4.1),

`||p_Q||_4 <= 4*2^(3/4)=2^(11/4)=6.727171322...`.                    (5.1)

### Corollary 5.1 — `QFORM-HEAVY-ISOTROPIC-UNCONDITIONAL-HALF-RIESZ-v1`

Under Theorem 4.1,

`sup_x E |x-Q|^(-1/2)
 <= 3 sqrt(3) 2^(5/3)
 < 16.497.`                                                           (5.2)

#### Proof

Let `M=||p_Q||_4`. For any `rho>0` and any `x`, split

`J(x)=int p_Q(r)|x-r|^(-1/2)dr`

into `|x-r|<=rho` and its complement. Holder with conjugate exponent `4/3` gives

`J_near(x)
 <= M [int_{|u|<=rho}|u|^(-2/3)du]^(3/4)
 = M 6^(3/4) rho^(1/4)`.                                             (5.3)

Since `p_Q` has total mass one,

`J_far(x)<=rho^(-1/2)`.                                              (5.4)

Put `A=M6^(3/4)`. Minimizing `A rho^(1/4)+rho^(-1/2)` gives

`J(x)<=3*2^(-2/3) A^(2/3)
 =3*2^(-2/3)sqrt(6) M^(2/3)`.                                       (5.5)

Substitute `M<=2^(11/4)` from (5.1). The powers simplify to

`3 sqrt(3) 2^(5/3)=16.49675564...`,                                  (5.6)

uniformly in `x`. QED.

This is strictly broader in hypothesis than the previous `QFORM-HEAVY-ISOTROPIC-HALF-RIESZ-v1`: the local transverse leverage may now be arbitrarily concentrated.

## 6. Actual application of fleet04/B18: one-extra-square closure without transverse diffuseness

The fleet04/B18 proof, at the exact source pinned in Section 2, establishes before its `L^infinity` bathtub step the pointwise kernel domination

`p_{R+alpha V_R^2}(t)
 <= |alpha|^(-1/2) int p_R(r)|t-r|^(-1/2)dr`                          (6.1)

on the appropriate half-line (reflection handles `alpha<0`), whenever the conditional density of `V_R` given `R=r` is bounded by one. Its published final lemma inserts an `L^infinity` bound for `p_R`; here we instead insert Corollary 5.1.

### Corollary 6.1 — `QFORM-HEAVY-ISOTROPIC-L4-SQUARE-CLOSURE-v1`

Let `R` be a heavy-isotropic rank-three variable satisfying Theorem 4.1, with no transverse-diffuseness assumption. Suppose that for almost every `r`, conditionally on `R=r`, a real variable `V_r` has a density bounded by one. For `alpha!=0`, put

`S=R+alpha V_R^2`.

Then `S` has an essentially bounded density and

`||p_S||_infinity
 <= 3 sqrt(3) 2^(5/3) |alpha|^(-1/2)
 < 16.497 |alpha|^(-1/2).`                                           (6.2)

#### Proof

Insert (5.2) directly into (6.1). No independence between `R` and the shifted square variable is required beyond the stated conditional density cap. QED.

This is the promised concrete application of a completed fleet04 theorem/proof to a new inequality. It upgrades the previous one-extra-square closure by removing the transverse-diffuse assumption on the rank-three base.

## 7. Why the full target is still open

The heavy-isotropic rank-three variable `Q` itself has no external square satisfying the hypothesis of Corollary 6.1 for free. Completing the existing `tau Z^2+2sYZ` term as a square does **not** justify a conditional density cap for the shifted `Z` after conditioning on the remaining base variable. The live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` explicitly forbids that shortcut.

Thus the new result narrows the exact endpoint debt:

**`QFORM-HEAVY-ISOTROPIC-ENDPOINT-CURVED-TRACE-v1` — OPEN.** Starting from (3.5), exploit the actual product-linear provenance of `(T,Y,Z)` and the genuine `tau Z^2` curvature to upgrade the uniform all-finite-`L^p` bank (4.1) to `L^infinity`, without assuming a bounded conditional density for `Z`, without transverse diffuseness, and without taking an unrestricted spectral-fiber supremum.

Equivalently, one needs a curved averaging principle that spends the third spectral direction before conditioning destroys the product structure. The present theorem proves that all nonendpoint integrability is already free from the heavy scalar pivot; what is genuinely unpaid is the endpoint gain.

For the full arbitrary-dimensional conjecture there is an additional extension debt: even an exact-rank-three endpoint theorem must be carried through extra correlated spectral components without treating them as an independent convolution. The full theorem therefore remains **OPEN / NOT PROVED**.

## 8. Continuity status

Theorem 4.1 constructs an absolutely continuous law with `p_Q in L^p` for every finite `p>1`; it does **not** prove a continuous representative. Corollary 6.1 proves an essentially bounded density for its extra-square branch; continuity is not claimed from the kernel domination alone. This is recorded separately from the target-level essential-density question as required.

## 9. Checks and provenance discipline

The inverse identity (3.8) was symbolically checked against the matrix (3.1). The constants were independently evaluated from their exact expressions:

- `2^(11/4)=6.727171322...`;
- `3 sqrt(3) 2^(5/3)=16.496755644...`.

The proof is analytic and does not rely on a numerical cutoff, simulation, histogram, Gaussian approximation, support localization, or post-rotation independence.

No exact `fleet04/B06` completed QFORM artifact was available during the source reads, so none is claimed. The compatible fleet04/B18 proof was actually inserted in Section 6. Repository transport was used; no authenticated native learned-memory receiver was invoked, hence execution remains `WITHOUT_VERIFIED_BRAIN` and `full_brain_connected=false`.

### Changed-file privacy review

The intended changed-file allowlist for this run consists only of this mathematical report, the fleet03/B06 source-bound handoff, the worker-owned memory snapshot/pointer, and this run's own login/start/receipt/finish records. The content contains only mathematical statements and sanitized operational provenance. No credentials, scheduler IDs, signed URLs, unrelated private data, machine paths, financial/company/client material or private transcripts are included. Repository-side secret-scan execution is not exposed through the current connector, so this is a manual narrow-scope fallback review, not a claim of a full repository scanner pass.
