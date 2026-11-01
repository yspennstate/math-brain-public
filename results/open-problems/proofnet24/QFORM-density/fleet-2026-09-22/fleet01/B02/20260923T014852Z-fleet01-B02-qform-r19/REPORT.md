SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-23T01:48:52Z.
attacking: integrated Fourier estimate — spend diffuse residual two-volume in L^r_t before a scalar-square lift, avoiding selection of one tiny pair minor.

# fleet01/B02 r19 — aggregate e2 Fourier compiler and scalar-square lift

## Status

`ESSENTIAL_STEP_APPLIED / SUPPORTING_ANALYTIC_THEOREM / FULL_QFORM_OPEN / WITHOUT_VERIFIED_BRAIN`.

This report proves a new aggregate order-two Fourier estimate and a bounded-density scalar-square lift. It does **not** prove the unrestricted three-large-eigenvalue conjecture and does **not** prove the global unweighted `L^1_t` characteristic-function criterion. No target-valid counterexample to that stronger global criterion is obtained here.

Continuity status: the residual quadratic form in Theorem 1 has an `L^p` density for an explicit `p>2`. The scalar-square lift in Theorem 2 proves an essentially bounded density, but continuity of that lifted density is **not** established by this argument.

## 1. Exact target and corrections retained

Target: for every finite `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has density bounded by one universal finite constant, or give a valid counterexample.

No Gaussian, log-concavity, moment, compact-support, connected-support, identical-law, diagonal-basis, or post-rotation-independence assumption is used. The phase-aligned fragmented-support counterexample still refutes every law-uniform scalar pointwise quadratic van-der-Corput bound. The arguments below use coupled original-coordinate volume sampling and frequency integration, not such a pointwise premise.


## 2. Partner theorem actually used

The required completed partner source is fleet02/B02 r16:

- repository: `yspennstate/math-open-problems`
- commit: `49c80441f24d6c697350119fac09426077b7e313`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260922T231047Z-fleet02-B02-qform-r16-6c4f9a1e/REPORT.md`.

For a physical cross block `M=A[I,J]`, let

`Z_k=e_k(M^T M)>0`

and let `alpha_i`, `beta_j` be the row/column inclusion probabilities under the natural squared `k`-minor volume law. The partner proves, for `q>=1` with every positive row marginal `alpha_i<=q/2`,

`|phi(t)| <= min(1,(T/|t|)^(k/(2q)))`,

where

`T = pi [B_beta prod_i H_q(alpha_i)]^(1/k) Z_k^(-1/(2k))`,

`B_beta = prod_j (1-beta_j)^(-(1-beta_j)/2)`,

`H_q(c)=q^(q/2-c)(q-c)^(-(q-c)/2)`.

It also proves the coarse entropy bound

`B_beta prod_i H_q(alpha_i) <= e^k q^(-k/2)`.

The estimate retains arbitrary same-bank quadratic terms, arbitrary outside couplings after original-coordinate conditioning, and induced affine terms. This scope is essential below.

## 3. New theorem: aggregate order-two `L^r` Fourier estimate

### Theorem 1 — `QFORM-E2-LR-FOURIER-v1`

Let `R` be an arbitrary real quadratic form of independent cap-one original-coordinate variables. Suppose it has a physical cross block `M` with

`Z_2=e_2(M^T M)>0`.

Let `alpha_i`, `beta_j` be the natural squared two-minor row/column inclusion marginals. Suppose

`1 <= q < r < 2`,

and

`max_i alpha_i <= q/2`.

Then

`boxed(
 int_R |phi_R(t)|^r dt
 <= [2 pi r/(r-q)]
    [B_beta prod_i H_q(alpha_i)]^(1/2)
    Z_2^(-1/4).
)`                                                              (3.1)

Consequently `R` has an `L^p` density with

`p=r/(r-1)>2`

and

`boxed(
 ||p_R||_p
 <= [r/(r-q)]^(1/r)
    [B_beta prod_i H_q(alpha_i)]^(1/(2r))
    Z_2^(-1/(4r)).
)`                                                              (3.2)

In particular,

`boxed(
 ||p_R||_p
 <= [r/(r-q)]^(1/r)
    e^(1/r) q^(-1/(2r))
    Z_2^(-1/(4r)).
)`                                                              (3.3)

Thus **every non-coloop natural two-volume law is covered at some exponent**: if

`h=max_i alpha_i < 1`,

choose

`q=max(1,2h)<2`

and any `r` with `q<r<2`. This spends the entire aggregate two-volume `Z_2` without selecting one physical row pair. The norm constant deteriorates as `h -> 1`, which precisely identifies the remaining near-coloop collar.

A convenient closed choice is

`r=(q+2)/2`.                                                     (3.4)

For the clean cap `h<=1/2`, take `q=1,r=3/2`; (3.3) gives

`||p_R||_3 <= (9e^2)^(1/3) Z_2^(-1/6)
            =4.0514500704... Z_2^(-1/6).`                      (3.5)

### Proof

Apply the partner fleet02/B02 estimate with `k=2`. Its exponent becomes

`k/(2q)=1/q`,

so

`|phi_R(t)| <= min(1,(T/|t|)^(1/q))`,                           (3.6)

with

`T=pi [B_beta prod_i H_q(alpha_i)]^(1/2) Z_2^(-1/4)`.           (3.7)

Although (3.6) need not be time-integrable, its `r`-th power is integrable exactly when `r>q`. Indeed

`int_R min(1,(T/|t|)^(r/q)) dt
 = 2T * [r/q]/[r/q-1]
 = 2T r/(r-q).`                                                 (3.8)

This proves (3.1).

With Fourier convention

`phi_R(t)=int e^(itx) p_R(x) dx`,

inverse Hausdorff--Young from `L^r` to `L^p`, `p=r/(r-1)`, gives

`||p_R||_p <= (2pi)^(-1/r)||phi_R||_r`.                         (3.9)

Substitution of (3.1) makes the factor `2pi` cancel exactly and gives (3.2). Finally, at `k=2` the partner entropy estimate is

`B_beta prod_i H_q(alpha_i) <= e^2 q^(-1)`,                     (3.10)

which gives (3.3). QED.

### Why this is not a disguised local-minor argument

`Z_2=e_2(M^T M)` is the sum of squares of **all** physical `2x2` cross minors. No particular minor is inverted. Hence (3.2) is useful precisely when the two-volume is diffuse over many tiny physical pairs, the branch where a fixed-pair estimate can lose dimension.

## 4. New theorem: scalar-square lift from aggregate two-volume

### Theorem 2 — `QFORM-E2-SQUARE-LIFT-v2`

Assume an original-coordinate pivot `a=A_00` is nonzero. Exact completion of the square gives

`Q = a (X_0 + a^(-1) A[0,K] X_K)^2 + R(X_K)`,                  (4.1)

where `R` is the exact physical Schur residual and the variables `X_K` remain the original independent coordinates.

Suppose `R` contains a physical cross block `M` satisfying Theorem 1 for parameters

`1 <= q < r < 2`

and `Z_2=e_2(M^T M)`. Then

`boxed(
 ||p_Q||_infinity
 <= K(q,r) |a|^(-1/2) Z_2^(-1/8),
)`                                                              (4.2)

where

`boxed(
 K(q,r)=4 sqrt(e) q^(-1/4)
        (2-r)^((r-3)/2)
        r^((1-r)/2)
        (r-q)^(-1/2).
)`                                                              (4.3)

This proves an **essentially bounded density** in the stated branch. Continuity is not asserted.

In particular, for every natural two-volume row-marginal maximum `h<1`, choosing `q=max(1,2h)` and any `q<r<2` proves a finite aggregate square-lift bound. Thus the previous artificial `h<3/4` restriction disappears completely; only the quantitative near-coloop degeneration `h -> 1` remains.

For the convenient midpoint choice `r=(q+2)/2`, numerical examples are

- `q=1` (`h<=1/2`): `K=14.1733304276...`;
- `q=4/3` (`h<=2/3`): `K=18.6493813110...`;
- `q=3/2` (`h<=3/4`): `K=22.9806675202...`;
- `q=1.8` (`h<=0.9`): `K=47.8574975273...`.

For `q=1`, optimizing `r` numerically gives `r≈1.586684` and `K≈14.03945`; the midpoint value is retained as the cleaner closed certificate.

### Proof

Condition on `X_K`. Because `X_0` has density at most one, translation of `X_0` does not change its density cap. The density of a shifted scalar square satisfies

`p_{a(X_0+c)^2}(y) <= |a|^(-1/2)|y|^(-1/2)`                    (4.4)

on the compatible half-line. Therefore

`p_Q(s) <= |a|^(-1/2) E |s-R|^(-1/2).`                         (4.5)

Let

`p=r/(r-1)`, `N=||p_R||_p`.

The conjugate exponent of `p` is exactly `r`. For any `rho>0`, Hölder on the near region gives

`int_{|u|<=rho} |u|^(-1/2)p_R(s-u)du
 <= N [int_{|u|<=rho}|u|^(-r/2)du]^(1/r)
 = N [4/(2-r)]^(1/r) rho^((2-r)/(2r)).`                        (4.6)

The far region is at most `rho^(-1/2)`. Put

`C_r=N[4/(2-r)]^(1/r)`.

Optimizing

`C_r rho^((2-r)/(2r)) + rho^(-1/2)`                            (4.7)

gives

`sup_s E|s-R|^(-1/2)
 <= 4 (2-r)^((r-3)/2) r^(-r/2) N^(r/2).`                       (4.8)

From the coarse form (3.3),

`N^(r/2)
 <= [r/(r-q)]^(1/2)
    sqrt(e) q^(-1/4) Z_2^(-1/8).`                              (4.9)

Combining (4.5), (4.8), and (4.9), and simplifying the power of `r`, gives exactly (4.2)-(4.3). QED.

## 5. Application to the live co-heavy / diffuse-e2 obstruction

A completed source used by the neighboring Fourier worker is fleet02/B01 r31:

- repository `yspennstate/math-open-problems`
- commit `3280d9fab56fe4878189ae89176887e3da29f569`
- path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260922T233020Z-fleet02-B01-qform-r31/REPORT.md`.

For a physical cross block with natural third-volume

`Z=e_3(M_0^T M_0)`,

a heavy row `u` of marginal `alpha`, and row deletion `N`, that report proves

`e_2(N^T N) >= alpha Z / ||u||^2`.                              (5.1)

Theorem 2 converts (5.1) into an **aggregate** bounded-density estimate whenever the row-deleted two-volume is not an exact coloop and the exact outer Schur step supplies a nonzero original-coordinate scalar pivot `a`. Let

`h_2=max row marginal of the natural e_2 law of N < 1`,
`q=max(1,2h_2)`,

and choose any `q<r<2`. Then

`boxed(
 ||p_Q||_infinity
 <= K(q,r)|a|^(-1/2)
    [alpha Z/||u||^2]^(-1/8).
)`                                                              (5.2)

For `h_2<=1/2`, the closed certificate is

`||p_Q||_infinity
 <=14.174 |a|^(-1/2)[alpha Z/||u||^2]^(-1/8).`                 (5.3)

This directly closes the previously named **diffuse-e2-after-coheavy** mechanism whenever there is a nonzero outer physical square: one no longer needs a single physical pair to carry a fixed fraction of `e_2`. Pair-volume concentration and pair-volume diffusion are now both paid except for the quantitative near-coloop limit and the separate zero/small outer-pivot issue.

## 6. Integrated-Fourier interpretation

This run does **not** prove the target-wide

`int_R |E exp(it X^T A X)| dt <= C`.

What is new is a continuum of exact intermediate Fourier currencies:

`boxed(
 int |phi_R(t)|^r dt
 <= [2pi r/(r-q)]
    [B_beta prod_i H_q(alpha_i)]^(1/2)
    e_2(M^T M)^(-1/4),
 q<r<2.
)`                                                              (6.1)

An order-two physical packet therefore supplies `L^r_t` for every `r` above its volume-Jensen threshold `q`, and an independent physical scalar square converts precisely any `r<2` member of this scale into an `L^infinity` density bound. This gives a frequency-space explanation of how “two aggregate directions plus one original-coordinate square” can substitute for a direct five-direction `L^1_t` packet.

The phase-aligned scalar counterexample is untouched: no individual one-dimensional quadratic characteristic function is claimed to decay uniformly.

## 7. First unpaid implication

`QFORM-E2-NEAR-COLOOP-OR-ZERO-PIVOT-CLOSURE-v2`.

After the clustered/co-heavy reduction, the newly paid branch is: nonzero original scalar pivot plus **every** residual aggregate `e_2` law with maximum natural row marginal strictly below one. The only structural losses left in this interface are therefore:

1. the two-volume law is an exact or quantitatively near coloop (`h_2 -> 1`), for which `K(q,r)` necessarily deteriorates in this route; or
2. the available outer scalar pivot is zero/too small and must be replaced by a pair, ridge, grouped-square, or bilinear product-preserving smoother.

The next step should use the near-coloop identity before absolute values: an `e_2` coloop means essentially all pair-volume contains one physical row, leaving a rank-one transverse bank. That is much more rigid than the former “diffuse e2 over many physical pairs” obstruction and should be routed to an existing mixed-hub/pair/ridge or grouped-bank mechanism without paying a vanishing local minor.

## 8. Scope checklist

- arbitrary independent cap-one input laws: yes;
- arbitrary dimension: yes within the stated structural branch;
- arbitrary same-bank curvature/outside couplings in the partner Fourier step: retained;
- post-rotation independence: never used;
- scalar law-uniform pointwise decay: never used;
- signs: scalar pivot may have either sign; cross-block Fourier estimate is sign-insensitive;
- density conclusion: essential boundedness in Theorem 2;
- continuity conclusion: **not proved** for Theorem 2; `p_R in L^p`, `p>2`, is proved for Theorem 1;
- full QFORM theorem: **OPEN**;
- full global `L^1_t` criterion: **OPEN_NOT_REFUTED**;
- two independent end-to-end reviews: not applicable because this is not a full-target proof candidate.
