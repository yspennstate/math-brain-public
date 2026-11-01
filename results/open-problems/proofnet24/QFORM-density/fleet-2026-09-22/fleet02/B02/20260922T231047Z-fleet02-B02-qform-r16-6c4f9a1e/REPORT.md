SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B02, 2026-09-22T23:10:47Z.
attacking: sharp-Hausdorff-Young upgrades of the newest D'/D5 volume-sampling Fourier bounds, then apply them to the live transverse physical cross-block branch and the named partner fleet03/B02 result.

# fleet02/B02 QFORM r16 — sharp-HY volume/Jensen compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T231047Z-fleet02-B02-qform-r16-6c4f9a1e`  
**Assignment:** Integrated Fourier estimate  
**Fresh control:** owner revision `2026-09-22.15`; later continuation `QFORM-CLAUDE-LATEST-20260922T225732Z` consumed during this run  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Continuity:** proved on every branch below because the displayed characteristic-function envelope is in `L^1`; full-target continuity remains open.

## 1. Exact target and fresh-source discipline

The target is unchanged. For every finite `n`, every vector `X=(X_1,...,X_n)` of independent real coordinates with one-dimensional probability densities at most one, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential density bound for `Q=X^T A X`, or give a target-valid counterexample. No moment, Gaussian, log-concavity, compact-support, connected-support, identical-law, diagonal-basis, or post-rotation-independence assumption is introduced.

After this invocation began, fresh main added the owner-required continuation `QFORM-CLAUDE-LATEST-20260922T225732Z`; later owner directions win, so I consumed it before publication. The required newest source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

in

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

I read the updated `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`; I also re-read `FOURIER_ROUTE_REPORT.md` at a later master snapshot and found the same D'/D5 statements. The source-specific review is

`yspennstate/math-open-problems@9844891a9fbe96a65e37f71122bf0300b53dcc80`

at `proofnet24/QFORM-density/interactive/20260922T220600Z-claude-review/REVIEW.md`.

That review supplies a correct sharp-Hausdorff-Young refinement of the original order-three theorem D at exactly D's scope, improving `6 sqrt(e)` to `3e`. The newest Fourier report separately proves the Jensen extension D' (row volume marginal threshold up to `h<3/4`) and the unrestricted fifth-volume theorem D5, but states them with the older rough `L^p` constant. The first task here is to combine those two completed arguments without changing scope.

The live correction `QFORM-RIDGE-VOLUME-NONEXHAUSTIVE-v1` is also binding: there are exact-target families where one-scale ridge and current low-order volume marginal gates fail badly. Nothing below promotes D', D5, or any ridge certificate to an exhaustive target reduction. Likewise the new no-uniform-coefficient-perturbation correction forbids treating a small dense matrix tail as harmless under arbitrary fragmented inputs. The estimates below retain the full physical cross block rather than discarding such a tail.

## 2. Source theorem D_k and notation

Let `I,J` be disjoint sets of ORIGINAL coordinates, condition on every coordinate outside `I union J`, and write

`M=A[I,J]`.

The conditional quadratic phase has arbitrary self terms on `I` and `J` and arbitrary induced affine terms. Weyl differencing/Cauchy-Schwarz on the `I` bank gives the source-valid inequality

`|phi_Q(t)|^2 <= E_W F_t(W)`,

where `W=X_J-X_J'` has independent coordinates with densities at most one and

`F_t(w)=prod_(i in I) |psi_i(2t (Mw)_i)|`,

with `psi_i` the original one-dimensional characteristic functions. All same-bank quadratic phases have disappeared from this inequality, so no post-rotation independence or small-self perturbation hypothesis is present.

Fix an integer `k>=1` with

`Z_k := e_k(M^T M) > 0`.

By Cauchy-Binet,

`Z_k = sum_(|S|=|T|=k) det(M_ST)^2`.

Put the volume-sampling weight

`w_ST = det(M_ST)^2 / Z_k`,

and define row and column inclusion probabilities

`alpha_i = P_w(i in S)`, `beta_j=P_w(j in T)`.

Then

`sum_i alpha_i = sum_j beta_j = k`,

with `0<=alpha_i,beta_j<=1`.

The Gaussian-exhaustion Brascamp-Lieb calculation in the newest source, with the determinant written by the valid diagonal-plus-PSD expansion so that `beta_j=1` endpoints are harmless, gives

`C_BL <= Z_k^(-1/2) prod_i alpha_i^(-alpha_i/2)
                 prod_j (1-beta_j)^(-(1-beta_j)/2).`          (2.1)

Rows with `alpha_i=0` are dropped. If `beta_j=1`, the corresponding difference density is used only in `L^infinity` and dropped by its cap one; all formulas below use the continuous endpoint value one.

## 3. Sharp Hausdorff-Young at the Jensen exponent

The source D' step first uses Jensen/Hölder on the probability law of `W`: for every `q>=1`, since `0<=F_t<=1`,

`E F_t <= (E F_t^q)^(1/q).`                                   (3.1)

Assume

`alpha_i <= q/2` for every row with positive volume marginal.  (3.2)

Then the Fourier exponent `q/alpha_i` is at least two, so Beckner's sharp Hausdorff-Young inequality applies. Since each original density `f_i` is a probability density bounded by one,

`||f_i||_(q/(q-alpha_i)) <= 1`.

With the Fourier convention used by the source, the exact scalar estimate is

`(||psi_i||_(q/alpha_i))^q
 <= (2pi)^alpha_i
    q^(q/2-alpha_i)
    (q-alpha_i)^(-(q-alpha_i)/2)
    alpha_i^(alpha_i/2).`                                     (3.3)

Define

`H_q(c)=q^(q/2-c)(q-c)^(-(q-c)/2)`, `H_q(0)=1`.              (3.4)

After the scale change `u=2t y`, the row factor entering Brascamp-Lieb is bounded by

`(2|t|)^(-alpha_i)(2pi)^alpha_i
 alpha_i^(alpha_i/2) H_q(alpha_i).`                            (3.5)

The `alpha_i^(alpha_i/2)` in (3.5) cancels exactly against the Gaussian Brascamp-Lieb factor in (2.1). Therefore

`E F_t^q
 <= Z_k^(-1/2) (pi/|t|)^k
    B_beta prod_i H_q(alpha_i),`                               (3.6)

where

`B_beta = prod_j (1-beta_j)^(-(1-beta_j)/2).`                 (3.7)

This is the exact sharp-HY replacement for the rough `L^p` row estimate in D' and D5.

### A uniform simplification

The elementary functions needed for the coarse universal constant are concave in exactly the right variables. First,

`-(1-beta) log(1-beta) <= beta`,

so, using `sum beta=k`,

`B_beta <= exp(k/2).`                                         (3.8)

Second,

`log H_q(c)
 =(q/2-c)log q - (q-c)log(q-c)/2`

satisfies

`(log H_q)''(c) = -1/[2(q-c)] < 0`,
`log H_q(0)=0`,
`(log H_q)'(0)=(1-log q)/2`.

Hence its tangent at zero gives

`log H_q(c) <= (1-log q)c/2`,

and therefore, since `sum alpha=k`,

`prod_i H_q(alpha_i) <= exp(k/2) q^(-k/2).`                   (3.9)

Combining (3.6)-(3.9),

`E F_t^q
 <= Z_k^(-1/2) (pi e/|t|)^k q^(-k/2).`                  (3.10)

No endpoint is hidden: at `alpha_i=q/2`, (3.3) is the Plancherel endpoint; at `alpha_i=0` the row is omitted; at `beta_j=1` the column factor has continuous endpoint one.

## 4. New theorem: sharp-HY volume/Jensen compiler

### Theorem 4.1 — `QFORM-SHARP-HY-VOLUME-JENSEN-v1`

Under the setup of Section 2, let `q>=1` satisfy

`max_i alpha_i <= q/2`, `k>2q`.                               (4.1)

Then the full quadratic form, with arbitrary self blocks, outside couplings, and affine terms, has a continuous density and

`boxed(
 ||p_Q||_infinity
 <= [k/(k-2q)]
    [B_beta prod_i H_q(alpha_i)]^(1/k)
    Z_k^(-1/(2k)).
)`                                                             (4.2)

In particular,

`boxed(
 ||p_Q||_infinity
 <= e q^(-1/2) [k/(k-2q)] Z_k^(-1/(2k)).
)`                                                             (4.3)

#### Proof

From (3.1) and (3.6),

`|phi_Q(t)|
 <= [B_beta prod_i H_q(alpha_i)]^(1/(2q))
    pi^(k/(2q)) Z_k^(-1/(4q)) |t|^(-k/(2q)).`                 (4.4)

Set

`a=k/(2q)>1`,
`T=pi [B_beta prod_i H_q(alpha_i)]^(1/k) Z_k^(-1/(2k)).`       (4.5)

Then (4.4), together with `|phi_Q|<=1`, is exactly

`|phi_Q(t)| <= min(1,(T/|t|)^a).`                              (4.6)

The envelope is integrable because `a>1`, and

`int_R min(1,(T/|t|)^a) dt
 = 2T a/(a-1)
 = 2T k/(k-2q).`                                               (4.7)

Fourier inversion gives a continuous density vanishing at infinity and

`||p_Q||_infinity <= (2pi)^(-1)||phi_Q||_1`,

which turns (4.7) into (4.2). Applying (3.8)-(3.9) gives

`[B_beta prod_i H_q(alpha_i)]^(1/k) <= e q^(-1/2)`,

hence (4.3). QED.

This theorem is an algebraic/compiler improvement of completed D'/D5, not a claim that the volume condition follows from the bare three-eigenvalue hypothesis.

## 5. The requested D' check and improved constant

For the third exterior volume `Z_3`, suppose

`h := max_i alpha_i < 3/4`.                                    (5.1)

If `h<=1/2`, take `q=1` and recover the source review's sharp theorem D constant

`boxed(||p_Q||_infinity <= 3e Z_3^(-1/6))`,                   (5.2)

with exact refined form `3(B_alpha B_beta)^(1/3)Z_3^(-1/6)`.

For the genuinely new D' range `1/2<=h<3/4`, take the smallest admissible Jensen exponent

`q=2h`.

(The coarse constant in (4.3) is increasing in `q` throughout `q>=1`, so there is no reason to enlarge `q`.) Then

`boxed(
 ||p_Q||_infinity
 <= [3e/(sqrt(2h)(3-4h))] Z_3^(-1/6).
)`                                                             (5.3)

This improves the newest source's

`6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1) Z_3^(-1/6)`

by the uniform factor `sqrt(e)/2 = 0.8243606...` while keeping exactly the same hypotheses and endpoint interpretation.

Examples of the new coefficient are

`h=1/2: 8.154845485...`,
`h=2/3: 21.186910063...`,

and it diverges, necessarily for this envelope argument, as `h` approaches `3/4` from below.

## 6. The requested D5 check and improved no-marginal constant

For `k=5`, every volume marginal satisfies `alpha_i<=1`. Take

`q=2`.

Then `alpha_i<=q/2` automatically, including the endpoint `alpha_i=1`, and `k=5>4=2q`. Therefore Theorem 4.1 gives the completely ungated fifth-volume estimate

`boxed(
 ||p_Q||_infinity
 <= (5e/sqrt(2)) Z_5^(-1/10)
 < 9.611 Z_5^(-1/10).
)`                                                             (6.1)

The newest source's D5 constant is `5 sqrt(2e)=11.66...`; (6.1) again improves it by the same factor `sqrt(e)/2` with no new structural hypothesis.

More generally, for every `k>=5`, the universal choice `q=2` yields

`||p_Q||_infinity
 <= [e k/(sqrt(2)(k-4))] Z_k^(-1/(2k)).`                       (6.2)

For a physical cross block with five singular values at least `sigma`, `Z_5>=sigma^10`, so

`boxed(||p_Q||_infinity <= (5e/sqrt2) sigma^(-1).)`            (6.3)

This is a genuine arbitrary-self, arbitrary-extra-direction integrated-Fourier branch with no volume-marginal gate.

## 7. Named partner fleet03/B02 consumed at equation level

The completed named partner result is

`yspennstate/math-open-problems@484c89f85cda352b2c4318364a6206ebc4154950`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T230126Z-fleet03-B02-QFORM-r17/REPORT.md`.

I read the complete immutable proof, not only its handoff. It proves `QFORM-EXACT-RANK3-CROSSBLOCK-FOURIER-v1`: if a physical cross block has exact rank three with singular-value product `Gamma`, then

`|phi_Q(t)| <= min(1,(2pi)^(3/2) Gamma^(-1/2)|t|^(-3/2))`,

and

`boxed(||p_Q||_infinity <= 6 Gamma^(-1/3))`,                  (7.1)

with arbitrary self phases and outside couplings.

It also proves the exterior identity for its live two-sided rank-two packet. If `B` has exact rank two with singular product

`Delta=sigma_1(B)sigma_2(B)`

and an added physical row `beta` has transverse distance

`eta=dist(beta,Row(B))`,

then for

`N=[beta^T;B]`

one has

`e_3(N^T N)=Delta^2 eta^2`.                                   (7.2)

The partner uses this to close the exact-rank-three augmented cross block by (7.1):

`||p_Q||_infinity <= 6(Delta eta)^(-1/3)`.                    (7.3)

### New application: robustness to extra cross directions

Now let `M` be a larger physical cross block containing that transverse core `N` as a row/column submatrix. Cauchy-Binet immediately gives

`Z_3(M)=e_3(M^T M) >= e_3(N^T N)=Delta^2 eta^2`.              (7.4)

The partner exact-rank-three theorem no longer applies if the extra directions raise `rank(M)>3`. But the new sharp D' compiler does. If the full order-three volume marginal of `M` satisfies

`max_i alpha_i <= h < 3/4`,

then (5.3) and (7.4) give the actual robust inequality

`boxed(
 ||p_Q||_infinity
 <= [3e/(sqrt(2h)(3-4h))]
    (Delta eta)^(-1/3),
)`                                                             (7.5)

for `h>=1/2`, with the `3e` coefficient when `h<=1/2`.

Thus the partner's transverse closure is stable under arbitrary additional cross directions whenever their full volume distribution remains below the relaxed `3/4` row-marginal threshold. No coefficient-smallness or perturbative output-continuity step is used; the extra directions are retained in `Z_3`.

If the larger cross block also has fifth volume `Z_5>0`, there is a completely different gate-free branch:

`boxed(||p_Q||_infinity <= (5e/sqrt2) Z_5^(-1/10).)`          (7.6)

For example, if its fourth and fifth singular values are at least `tau`, while the embedded transverse rank-three core has product `Gamma=Delta eta`, singular-value monotonicity under taking submatrices gives `s_1(M)s_2(M)s_3(M)>=Gamma`; hence

`Z_5(M) >= (s_1...s_5)^2 >= Gamma^2 tau^4`,

and therefore

`boxed(
 ||p_Q||_infinity
 <= (5e/sqrt2) Gamma^(-1/5) tau^(-2/5).
)`                                                             (7.7)

Equations (7.5)-(7.7) are the requested actual use of both the newest Claude result and the named partner result on a live surviving physical cross-block mechanism.

## 8. What the combined cross-block picture now says

For a candidate physical cross block, three complementary integrated-Fourier mechanisms are now source-valid:

1. **Exact rank three:** partner r17, no volume-marginal gate, coefficient `6 Z_3^(-1/6)`.
2. **Arbitrary rank with diffuse third-volume rows:** sharp D', coefficient (5.3), valid up to `alpha_max<3/4`.
3. **Five substantial cross directions:** sharp D5, no marginal gate, coefficient (6.1).

Consequently, a state that escapes all three mechanisms must simultaneously avoid a useful exact-rank-three cut, carry its relevant third exterior volume on at least one row with volume marginal at least `3/4`, and have insufficient fifth exterior volume at the target scale. This is a much more specific obstruction than “the cross block has no good minor.”

The live correction `QFORM-RIDGE-VOLUME-NONEXHAUSTIVE-v1` demonstrates that such concentrated states genuinely occur: its bicolop examples have order-two/order-three volume marginals above `24/25`. That correction is therefore not contradicted; it is exactly the reason the first unpaid implication is a concentrated low-effective-cross-rank problem rather than an assertion that D' is exhaustive.

Likewise, the no-uniform-coefficient-perturbation correction is respected: (7.5) is not obtained by saying that extra cross directions are small. They enter `Z_3` and the actual volume marginals. Theorem D5 similarly consumes the full physical block rather than discarding a dense tail.

## 9. First unpaid implication after this run

The first missing mechanism is now the **high-volume-coloop / effective-rank-at-most-four collar**.

More concretely, after applying the exact-rank-three partner theorem, sharp D', and sharp D5, the difficult cross-block state is one in which

- the useful order-three exterior mass exists but every admissible orientation has a row volume marginal at least `3/4` (or the relevant `Z_3` is itself too small),
- the fifth exterior volume is too small to pay at the target scale, so the cross interaction is effectively supported on at most four singular directions,
- and the remaining two-sided rank-two packet may be exactly span-aligned, so adjoining the scalar coordinate does not create a transverse third cross direction.

A valid next step must convert that concentrated Pluecker/volume mass into one of the already-paid product-preserving mechanisms: a physical principal pair/triple, a one-sided square-rank-two packet, a grouped hyperbolic/star packet, or a dependence-safe Schur fractional-potential resource. It may not use a random-variable shear, infer a uniformly good single minor, discard arbitrary same-bank self curvature, or treat a small dense coefficient tail as a uniformly small output perturbation.

No target-valid counterexample to the stronger global criterion

`int_R |phi_Q(t)| dt < infinity`

was found in this run. The stronger criterion therefore remains OPEN at full target scope rather than refuted.

## 10. Checks

`CHECK.py` and its actually executed `CHECKS.txt` are saved beside this report. They verify:

- 800 capped-simplex samples for the tangent inequality `prod H_q(alpha_i)<=e^(k/2)q^(-k/2)` at `(k,q)=(3,1),(3,1.2),(3,1.48),(5,2)`;
- the constants `3e=8.154845485377136` and `5e/sqrt2=9.610577570397790`;
- 100 seeded random exact-rank-two matrices for the partner exterior identity `e_3([beta;B]^T[beta;B])=Delta^2 eta^2`, with maximum scaled numerical error `4.301e-15`.

The output ends `STATUS=PASS`. These are regression checks of algebra and constants only; the analytic theorem is proved above and the checks are not evidence for the full conjecture.

## 11. Source pins and correction status

Newest required Claude-attributed source:

- `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`.

Source-specific independent review and sharp-HY order-three refinement:

- `math-open-problems@9844891a9fbe96a65e37f71122bf0300b53dcc80`, `proofnet24/QFORM-density/interactive/20260922T220600Z-claude-review/REVIEW.md`.

Named partner actually consumed:

- `math-open-problems@484c89f85cda352b2c4318364a6206ebc4154950`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T230126Z-fleet03-B02-QFORM-r17/REPORT.md`.

Fresh corrections explicitly respected:

- `QFORM-RIDGE-VOLUME-NONEXHAUSTIVE-v1`, canonical `math-open-problems@60f013f7f3f239bd33f90946478d7ddbcebc4ea5`.
- `QFORM-NO-UNIFORM-COEFFICIENT-PERTURBATION-CONTINUITY-v1`, canonical `math-open-problems@84093fddd5e3d3c692449d49c8b01537b28eb8d8`.
- The older pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea, conditional projection-cap positive-moment, single-good-minor, and universal rank-three-cross-cut routes remain unavailable.

The full QFORM conjecture is not proved or disproved by this report.
