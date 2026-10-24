SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T19:54:43Z.
attacking: literature-to-proof transfer for a private transverse source bank in the null-hub normal form; sharpen the disjoint-square half-Riesz smoother with the exact Livshyts--Paouris--Pivovarov marginal theorem and splice account04/B18 r4.

# account03/B18 r34 — sharp LPP square smoother and a private-transverse-bank null-hub exit

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** literature-to-proof transfer  
**Status:** `NEW SUPPORTING TARGET-LEVEL RECEIVER + LITERATURE SCOPE CORRECTION + PARTNER SPLICE / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** essential boundedness is proved in the new branch; continuity is **not** proved here.

## 1. Scope and source boundary

The target remains: independent original-coordinate real inputs with probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of absolute value at least one. No Gaussian, log-concave, moment, compact-support, connected-support, iid, centering, smoothness, or diagonal-basis assumption is introduced.

This run consumed the current correction set. In particular, it does not use law-uniform pointwise quadratic-phase decay, an arbitrary-joint coarea bound, independence after a rotation, a conditional density cap as a substitute for independence, deletion of a small nonzero edge, or a uniformly good physical minor.

The current owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` was also consumed. The same-hour B18 canonical login already existed from the preceding invocation and was preserved rather than overwritten; this run has its own immutable start/finish records.

## 2. Primary literature audit

### 2.1 Sharp one-dimensional product projection

Primary source:

Galyna Livshyts, Grigoris Paouris, Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel Journal of Mathematics 216 (2016), 877--889, arXiv:1507.07949, DOI 10.1007/s11856-016-1431-5.

Their theorem says: if a probability density on `R^n` factors as `prod_i f_i(x_i)` with every `||f_i||_infinity<=1`, then every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. Thus for every nonzero deterministic coefficient vector `r`,

`||p_(r dot X)||_infinity <= sqrt(2)/||r||_2`.                         (2.1)

This is exactly within the owner hypotheses: no moment, support, log-concavity, symmetry, centering, smoothness, or identical-law assumption is present.

### 2.2 Banks--Garza Vargas--Kulkarni--Srivastava: exact prior overlap, but not the new branch

I also checked the primary Section 2 of Banks--Garza Vargas--Kulkarni--Srivastava, *Overlaps, Eigenvalue Gaps, and Pseudospectrum under real Ginibre and Absolutely Continuous Perturbations*, arXiv:2005.08930. Their Theorem 2.1 treats matrix-valued bilinear quadratic maps with two independent entrywise bounded-density banks. Importantly, their **Corollary 2.4** improves the `k=1` case and already has content for `j>=2`; in particular, a two-bank scalar bilinear form with a rank-two cross matrix and only affine same-bank terms is prior-covered with the correct `(sigma_1 sigma_2)^(-1/2)` scale.

Therefore no novelty claim should be made for the pure affine rank-two bilinear subcase. This does **not** subsume fleet theorem `QFORM-RANK2-BILINEAR-DIRECT-v1` in its full scope, because that theorem permits an arbitrary measurable `H(U)` on one bank. It also does not cover the theorem below: here the square has a random center sharing the `J` bank with the hyperbolic residual.

This is a literature-scope correction, not a correction to the mathematics of the fleet bilinear theorem.

## 3. Two elementary potential facts

### Lemma 3.1 — capped density gives a half-Riesz budget

If a real random variable `W` has a density bounded by `M`, then for every `t`,

`E |W-t|^(-1/2) <= 2 sqrt(2M)`.                                      (3.1)

**Proof.** By layer cake,

`E |W-t|^(-1/2)
 = int_0^infinity P(|W-t|<u^(-2)) du
 <= int_0^infinity min(1,2M u^(-2)) du`.

Split at `u=sqrt(2M)`. The two pieces are equal to `sqrt(2M)`, proving (3.1). QED.

### Lemma 3.2 — sharp product-bank square smoother with a random center

Let `Gcal` be a sigma-field. Let `R,C` be arbitrary real `Gcal`-measurable variables. Let `X_K` be an original-coordinate product bank independent of `Gcal`, with every one-dimensional density bounded by one. Fix `r!=0`, `lambda!=0`, and put

`Y=r dot X_K`,
`Q=R + lambda (Y+C)^2`.

If

`H := sup_t E |R-t|^(-1/2) < infinity`,                              (3.2)

then `Q` has a density and

`boxed:
 ||p_Q||_infinity
 <= [sqrt(2) H]/[||r||_2 sqrt(|lambda|)].`                            (3.3)

**Proof.** LPP gives `M_Y:=||p_Y||_infinity<=sqrt(2)/||r||_2`. Conditional on `Gcal`, the center `C` is deterministic. For the sign-compatible half-line, the two inverse branches of `s=lambda(Y+C)^2` give

`p_(lambda(Y+C)^2 | Gcal)(s)
 <= M_Y/[sqrt(|lambda|) sqrt(|s|)]`.                                 (3.4)

The bound is uniform in the random center. Mixing the conditional densities therefore gives, for every `t`,

`p_Q(t)
 <= M_Y/sqrt(|lambda|) * E|t-R|^(-1/2)
 <= sqrt(2)H/[||r||_2 sqrt(|lambda|)].`

Conditional absolute continuity also proves absolute continuity of the mixture. QED.

This sharpens the valid source-separated-square lemma recorded in account02/B20 run `20260923T155833Z-account02-B20-QFORM-auto11c`, which used a `sqrt(e)` linear-projection cap from a different receiver. For a unit `r`, the source-valid constant is `sqrt(2)` rather than `sqrt(e)`, an improvement factor `sqrt(2/e)=0.85776388496...`. Thus its two displayed credits improve numerically as follows:

`H<38.907, |lambda|>=1  => ||p||_infinity <55.022808`,
`H<39.919, |lambda|>=1  => ||p||_infinity <56.453992`.

The source separation remains mandatory; no rotated-coordinate independence is inferred.

## 4. New theorem: a private transverse bank pays arbitrary `J`-side shear

Use the exact-rank-three null-hub normal form already established in the fleet,

`Q = 2 (X_0 + ell dot X_L)(g dot X_L) + d (beta dot X_L)^2`,          (4.1)

with independent original-coordinate cap-one inputs, `||beta||_2=1`, `beta dot g=0`,

`gamma:=||g||_2>0`, `d!=0`.                                         (4.2)

### Theorem `QFORM-NULLHUB-PRIVATE-TRANSVERSE-BANK-v1`

Suppose the leaf indices admit a literal original-coordinate split

`L=J disjoint_union K`                                               (4.3)

such that

`g_K=0`,                                                             (4.4)
`rho:=||beta_K||_2>0`,                                                (4.5)
`ell_K=a beta_K` for some real `a`.                                  (4.6)

There is **no restriction at all on `ell_J`**. Then `Q` has a density satisfying

`boxed:
 ||p_Q||_infinity
 <= 2^(13/4) / [rho sqrt(|d| gamma)].`                               (4.7)

Numerically `2^(13/4)=9.513656920021768...`.

### Proof

Put

`B=beta_K dot X_K`,
`C=beta_J dot X_J`,
`G=g_J dot X_J=g dot X_L`,
`L0=ell_J dot X_J`.                                                   (4.8)

By (4.6),

`Q=2(X_0+L0+aB)G+d(B+C)^2`.                                         (4.9)

Complete the square in the **literal independent K-bank projection** `B`:

`Q=R+d(B+C+aG/d)^2`,                                                  (4.10)

where the exact residual is

`R=2X_0G+2L0G-2aCG-(a^2/d)G^2`.                                    (4.11)

The K bank is independent of the sigma-field generated by `(X_0,X_J)`, so Lemma 3.2 will apply once we bound the half-Riesz potential of `R`.

Condition on `X_J`. Then `G,L0,C` are fixed and (4.11) is an affine function of the genuine original coordinate `X_0`, with slope `2G`. On the event `G!=0`, its conditional density is capped by

`1/(2|G|)`.                                                          (4.12)

The event `G=0` has probability zero because `G` has an absolutely continuous density. Applying Lemma 3.1 conditionally gives

`sup_t E[|R-t|^(-1/2) | X_J]
 <= 2 |G|^(-1/2)`.                                                   (4.13)

Now apply LPP again, this time to the normalized original-product projection `G/gamma`. Equation (2.1) gives

`||p_G||_infinity <= sqrt(2)/gamma`.                                (4.14)

Another use of Lemma 3.1, with `t=0`, yields

`E |G|^(-1/2)
 <= 2 sqrt(2) (sqrt(2)/gamma)^(1/2)
 = 2^(7/4) gamma^(-1/2)`.                                           (4.15)

Average (4.13):

`H:=sup_t E|R-t|^(-1/2)
 <= 2^(11/4) gamma^(-1/2)`.                                         (4.16)

Finally apply Lemma 3.2 to (4.10) with `r=beta_K`, `lambda=d`. Since `||r||=rho`,

`||p_Q||_infinity
 <= sqrt(2)/[rho sqrt(|d|)] * 2^(11/4) gamma^(-1/2)
 = 2^(13/4)/[rho sqrt(|d| gamma)].`

This is (4.7). QED.

### Why this is genuinely different from r32

The earlier B18 source-separated-shear theorem r32 required a bank on which **both** `g` and `beta` vanished and routed arbitrary `ell` from that bank into the hub variable. The new theorem is the complementary geometry: the private K bank can carry a substantial part of `beta`; it requires `g_K=0` and only the one-dimensional alignment `ell_K parallel beta_K`, while `ell_J` may be completely source-entangled and need not lie in `span(g,beta)`.

The proof spends the private transverse square *after* retaining the arbitrary J-side shear inside the half-Riesz residual. No small nonzero coefficient is deleted.

## 5. Spectral normalization and useful currency

In the exact-rank-three null-hub normalization used by the fleet,

`|d| gamma^2 = h D`,                                                 (5.1)

where `h` is hub spectral leverage and `D=|pdet A|`. Thus (4.7) is equivalently

`||p_Q||_infinity
 <= 2^(13/4) sqrt(gamma) / [rho sqrt(hD)].`                           (5.2)

It is convenient to define the **private transverse square currency**

`Theta_K := rho^2 |d| gamma = rho^2 hD/gamma`.                       (5.3)

Then simply

`boxed: ||p_Q||_infinity <= 2^(13/4) Theta_K^(-1/2).`                (5.4)

This is scale-correct under `A -> cA`.

## 6. Actual splice with the designated account04/B18 partner

The latest completed compatible account04/B18 result is corrected run r4:

`yspennstate/math-open-problems@3460488b1a730f54dbac848cddc3e2761d3f348e`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260923T162049Z-account04-B18-QFORM-r4/REPORT.md`.

Inside the target-normalized null-hub `N3(1/64)` state it proves

`q_i>1/2 and |g_i|>=1/64
  => ||p_Q||_infinity <64.1795826152`.                               (6.1)

The present theorem gives the independent aggregate exit

`Theta_K >= (2^(13/4)/64.1795826152)^2
          =0.021973599015858086...
  => ||p_Q||_infinity <=64.1795826152`.                              (6.2)

This is an actual inequality-level splice with the designated partner. Therefore the null-hub compiler can now route either a moderate heavy physical edge by (6.1), or a source-private transverse bank satisfying (4.4)--(4.6) with currency (6.2), without forcing a single good minor.

In the common target-normalized `r>=1/2` regime, `h>=1/5` and `D>=1`, so the simpler sufficient condition

`rho^2/gamma >=0.10986799507929043...`                               (6.3)

implies (6.2).

This does not assert that the spectral hypothesis forces (6.3); it records the exact newly paid branch.

## 7. Literal target family in the punctured geometry

The theorem is not restricted to a diagonal or post-rotation-independent example. Fix a private K bank and let its normalized coefficient vector be `u_K`. Take `rho=1/2` and

`beta_J=(4/5, sqrt(11)/10, 0)`,
`beta_K=(1/2)u_K`.                                                    (7.1)

Then `||beta||=1`. On three J coordinates set

`g_1=1/128`,
`g_2=-1/(16 sqrt(11))`,
`g_3=sqrt(1-g_1^2-g_2^2)`.                                          (7.2)

Thus `||g||=1` and `beta dot g=0`, while the first leaf has

`beta_1^2=16/25>1/2`, `0<|g_1|=1/128<1/64`.                         (7.3)

Let `q` be the unit vector in the J-space orthogonal to both `g` and `beta_J`, let `ell_J=cq` with arbitrary `c`, and set `ell_K=0`. Then the new theorem applies with `a=0`, `gamma=d=1`, `rho=1/2`, giving for every cap-one product law

`boxed: ||p_Q||_infinity <= 2^(17/4)=19.027313840043536...`.         (7.4)

Moreover the deterministic coefficient directions

`w=e_0+cq`, `g`, `beta`

are mutually orthogonal. Hence the physical matrix of

`Q=2(w dot X)(g dot X)+(beta dot X)^2`

has nonzero spectrum exactly

`{+sqrt(1+c^2), -sqrt(1+c^2), 1}`.                                  (7.5)

So this is a literal exact-rank-three target family for every `c`, and it exhibits a small nonzero hub edge on a leaf where the transverse-square coefficient is already large. The proof remains uniform in the arbitrary J-side shear parameter `c`.

## 8. What is and is not proved

The new theorem establishes **absolute continuity and an essentially bounded density** on its stated private-bank branch. I do **not** claim continuity: LPP supplies an `L^infinity` projection density for an arbitrary rough product bank, and the argument above does not prove a continuous representative after the random-centre square mixture.

The unrestricted conjecture remains **OPEN / NOT PROVED**, and unrestricted continuity remains open. The still-unpaid null-hub configurations include source-entangled small nonzero edges where no quantitatively useful private K bank satisfies both `g_K=0` and `ell_K parallel beta_K`. In that regime the transverse square and hyperbolic slope share the same rough original coordinates and Lemma 3.2 cannot be invoked by fiat.

A useful next mechanism is therefore to relax the exact one-dimensional alignment `ell_K parallel beta_K` while preserving product provenance, probably by spending a two-dimensional K-bank projection jointly rather than conditioning it into a false independent pair.

## 9. Literature conclusion

- LPP is used exactly at its published hypotheses, twice, in dimension one.
- Banks et al. Corollary 2.4 already covers the pure affine rank-two two-bank bilinear subcase; record that overlap and do not claim it as new literature.
- Banks et al. does not close the new random-centre square branch because the J-side shear and square centre are not a second independent bilinear bank.
- No exact published theorem found in this source check settles the unrestricted rough-input three-large-eigenvalue conjecture.

The last statement is a scope report, not a novelty claim.
