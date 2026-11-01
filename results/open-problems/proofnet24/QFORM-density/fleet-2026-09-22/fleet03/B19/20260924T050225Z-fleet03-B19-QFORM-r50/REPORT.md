SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B19, 2026-09-24T05:02:25Z.
attacking: QFORM-HEAVY6-PEEL-ROBUST-R2-OR-HUBSTAR-v1 — peel the at-most-six leverage-heavy physical hubs from the r49 ultra-thin rank-two crossing and force either a robust literal light-light rank-two crossing with full-law fractional smoothing or a fixed-strength literal hub star.

# fleet03/B19 r50 — leverage-heavy peel gives robust physical R2 smoothing or a fixed physical hub star

Programme: `QFORM-DENSITY-3EIG-20260922`.

Status: **NEW TARGET-RELEVANT COMPILER / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Repository transport is not native authenticated brain ingestion.

Continuity: this run obtains a uniform fractional-potential / interval-concentration estimate on one surviving branch, not an `L^infinity` density theorem. Full-target continuity remains **OPEN**.

All coordinates below are literal ORIGINAL coordinates. No random variable is rotated. No Gaussian, log-concave, moment, compact-support, connected-support, iid, arbitrary-joint-coarea, fiber-supremum, or law-uniform pointwise oscillatory-decay hypothesis is introduced. No nonzero coefficient tail is discarded.

## 1. Source-pinned frontier


The immediate inherited source is fleet03/B19 r49:

`yspennstate/math-open-problems@35b71af9bbf9feb9542681486f190155c71ff247`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260924T040014Z-fleet03-B19-QFORM-r49/REPORT.md`.

It supplies disjoint original-coordinate banks `R,C` and the ACTUAL literal cross block

`N=A[R,C]`

such that, if `N_2` is its top-two SVD truncation,

`||N-N_2||_F < tau`, `tau=2^-16`,                                 (1.1)

`sigma_2(N)>=1/64`.                                                (1.2)

Write

`N_2=U Sigma V^T`, `Sigma=diag(sigma_1,sigma_2)`,                 (1.3)

where `U,V` have two orthonormal columns. r49 already shows that there are at most three top-two-leverage-heavy physical coordinates per bank and converts the same-bank curvature, in its transverse-anchor branch, to a four-latent / six-physical-hub carrier plus spectrally diffuse residuals. Its first remaining debt is to couple that structure to an endpoint density receiver.

The fresh analytic input used here is fleet02/B19:

`yspennstate/math-open-problems@f4d95bc33caf8db11888cceb817c005484f67d31`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260924T031336Z-fleet02-B19-QFORM-auto11/REPORT.md`,

`QFORM-PHYSICAL-R2-FRACTIONAL-SMOOTHING-v1`.

For any literal disjoint physical cross block `M`, put

`Z_2(M)=e_2(M^T M)`.

If `Z_2(M)>0`, the full ambient quadratic form, retaining arbitrary same-bank curvature, outside blocks/couplings, affine terms, signs and extra spectrum, obeys

`H_(1/4)(Q):=sup_s E |Q-s|^(-1/4)
 <= C_R2 Z_2(M)^(-1/16)`,                                        (1.4)

with

`C_R2=3.929131770449763...`.                                     (1.5)

Equivalently, since `Z_2>=sigma_1(M)^2 sigma_2(M)^2`,

`H_(1/4)(Q)<=C_R2 [sigma_1(M)sigma_2(M)]^(-1/8)`.                (1.6)

This is a fractional smoothing theorem, not an endpoint density theorem.

## 2. Heavy sets and the exact dichotomy

Define the top-two leverage scores

`ell_i^R=||U_{i,*}||_2^2`, `ell_j^C=||V_{j,*}||_2^2`.            (2.1)

Set

`H_R={i in R: ell_i^R>1/2}`, `L_R=R\H_R`,
`H_C={j in C: ell_j^C>1/2}`, `L_C=C\H_C`.                       (2.2)

Because the two columns of `U` and `V` are orthonormal,

`sum_i ell_i^R=sum_j ell_j^C=2`,                                 (2.3)

hence

`|H_R|<=3`, `|H_C|<=3`.                                          (2.4)

Introduce the two `2x2` light Gram matrices

`G_R=U[L_R,:]^T U[L_R,:]`,
`G_C=V[L_C,:]^T V[L_C,:]`.                                       (2.5)

### Theorem 2.1 — `QFORM-HEAVY6-PEEL-ROBUST-R2-OR-HUBSTAR-v1`

Under (1.1)-(1.3), at least one of the following holds.

**Robust light-light branch.**

`lambda_min(G_R)>=1/4` and `lambda_min(G_C)>=1/4`.                (2.6)

Then the ACTUAL literal physical light-light cross block

`M=N[L_R,L_C]`                                                    (2.7)

satisfies

`boxed: sigma_2(M) > 1/256-2^-16 = 255/65536`.                  (2.8)

Consequently

`Z_2(M)>(255/65536)^4`                                           (2.9)

and the full ambient quadratic law obeys

`boxed: H_(1/4)(Q)<15.731913`.                                   (2.10)

In particular every interval `I` of length `delta` obeys

`boxed: P{Q in I}<13.228910 delta^(1/4)`.                        (2.11)

**Physical-hub-star branch.**

At least one of the Gram inequalities in (2.6) fails. If the `R` inequality fails, some ACTUAL literal physical coordinate `i in H_R` satisfies

`boxed: ||A[i,C]||_2 > 1/128-2^-16 = 511/65536`.                (2.12)

If the `C` inequality fails, some ACTUAL literal physical coordinate `j in H_C` satisfies

`boxed: ||A[R,j]||_2 > 511/65536`.                              (2.13)

Thus the r49 six-heavy-coordinate carrier cannot hide all of the strong rank-two crossing inside the latent heavy directions without exposing a fixed-strength original-coordinate star.

### Proof of the robust branch

Let

`U_L=U[L_R,:]`, `V_L=V[L_C,:]`.                                 (2.14)

From (2.6),

`sigma_min(U_L)=sqrt(lambda_min(G_R))>=1/2`,
`sigma_min(V_L)>=1/2`.                                           (2.15)

The rank-two light restriction of the SVD truncation is

`N_2[L_R,L_C]=U_L Sigma V_L^T`.                                  (2.16)

Take thin QR factorizations `U_L=Q_R R_R`, `V_L=Q_C R_C`. The two nonzero singular values in (2.16) equal those of the `2x2` matrix

`R_R Sigma R_C^T`.

Therefore

`sigma_2(N_2[L_R,L_C])
 >=sigma_min(R_R) sigma_2(N) sigma_min(R_C)
 >=(1/2)(1/64)(1/2)
 =1/256`.                                                         (2.17)

Let `F=N-N_2`. Restriction cannot increase Frobenius or operator norm, so

`||F[L_R,L_C]||_op<=||F||_F<2^-16`.                              (2.18)

Weyl's singular-value inequality applied to (2.16)-(2.18) proves (2.8).

Since `sigma_1(M)>=sigma_2(M)`,

`Z_2(M)=sum_{a<b}sigma_a(M)^2 sigma_b(M)^2
 >=sigma_1(M)^2 sigma_2(M)^2
 >=sigma_2(M)^4`,                                                 (2.19)

which proves (2.9). Applying the completed fleet02/B19 theorem (1.4) to the literal physical cut `L_R|L_C` gives

`H_(1/4)(Q)
 <C_R2 (255/65536)^(-1/4)
 =15.73191283402618...`,                                         (2.20)

proving (2.10). No conditioning or tail deletion is needed because the source theorem itself retains the entire ambient coefficient matrix.

For an interval `I` of length `delta` with midpoint `s`,

`1_{Q in I} <= (delta/2)^(1/4)|Q-s|^(-1/4)`,                    (2.21)

so (2.10) gives

`P(Q in I)<15.731912835 (delta/2)^(1/4)
 =13.228909108 delta^(1/4)`,                                     (2.22)

which is (2.11).

### Proof of the hub-star branch

Suppose `lambda_min(G_R)<1/4`. Since `U^T U=I_2`,

`U[H_R,:]^T U[H_R,:]=I_2-G_R`,                                  (2.23)

so

`lambda_max(U[H_R,:]^T U[H_R,:])>3/4`.                          (2.24)

Hence its trace is `>3/4`. Using `V^T V=I_2` and `Sigma^2>=sigma_2(N)^2 I_2`,

`||N_2[H_R,C]||_F^2
 =tr(Sigma^2 U[H_R,:]^T U[H_R,:])
 > (3/4)sigma_2(N)^2`.                                           (2.25)

There are at most three rows in `H_R`. Therefore some `i in H_R` has

`||N_2[i,C]||_2 > sigma_2(N)/2 >=1/128`.                         (2.26)

The actual row differs by at most the global Frobenius tail:

`||N[i,C]-N_2[i,C]||_2<=||F||_F<2^-16`.                         (2.27)

Equations (2.26)-(2.27) give (2.12). The proof of (2.13) is identical after transposition. QED.

## 3. What this changes in the r49 carrier

The r49 frontier already localized arbitrary same-bank curvature in its transverse-anchor/no-large-self-star branch to

`diagonal + four-latent carrier + interactions on at most six literal heavy physical coordinates + two diffuse residual self blocks + retained nonzero cross tail`.

The present theorem adds a second, independent piece of information about the same at-most-six heavy coordinates:

* either deleting all six leverage-heavy coordinates still leaves a literal light-light physical cross block whose **full ambient law** has the uniform `H_(1/4)` bound (2.10);
* or one of the exceptional physical hubs necessarily carries a literal cross-star of norm `>511/65536`.

The first branch is a product-safe smoothing currency available simultaneously with the r49 diffuse-residual geometry. The second branch turns failure of robust peeling into a finite physical-star resource rather than an abstract loss of singular mass.

This does **not** yet imply an endpoint density bound. In particular, the known fleet04/B19 moving-ridge construction forbids replacing the remaining product-linear structure by an arbitrary bounded joint density, and the fleet correction to generic `L^3 + 1/2`-Holder interpolation forbids upgrading a fractional/Frostman estimate to `L^infinity` abstractly.

Accordingly the first essential implication on this branch is sharpened to

`QFORM-H1/4-PLUS-DIFFUSE-THIRD-SOURCE-OR-HUBSTAR-ENDPOINT-v1`:

> In the robust branch, combine the full-law `H_(1/4)<15.732` resource with the r49 diffuse high-spectrum residual / retained third target resource to reach `L^infinity` without generic interpolation or loss of product provenance. In the failure branch, spend the fixed literal hub star `>511/65536` jointly with the finite carrier or route it into an already-paid physical pair / grouped-star / physical-volume receiver.

Parallel debts remain the giant near-rank-one crossing, small-Pluecker aggregate branch, and extra-spectrum / low-rank-carrier glue. None is renamed as solved.

## 4. Fresh fleet01/B19 integration

Fresh fleet01/B19 r12 is

`yspennstate/math-open-problems@1c7cd60173b1c7836e2613e3a096989ae76d6fff`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B19/20260924T044522Z-fleet01-B19-QFORM-auto11-r12/REPORT.md`.

It proves a pair-plus-rank-two-Schur fractional/logarithmic receiver and an aggregate incident-four-volume receiver

`||p_Q||_infinity <=21.128271915 J_T^(-1/24)`                    (4.1)

for its exact physical-pair scope, with `J_T=D^6 kappa^4 W_T`, and proves exact zero incident-volume rigidity `S=Delta+K`, `rank K<=2`. The new hub-star branch (2.12)-(2.13) is therefore a concrete place to seek that pair/incident-volume resource, but a star norm alone does **not** force the required invertible pair or positive `J_T`; no such implication is claimed here.

## 5. Designated fleet04/B19 result applied at an actual inequality

The designated partner theorem consumed is

`yspennstate/math-open-problems@5b5cea245bb2f9f6e85e0efb7f9bc28183fc5f1a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B19/20260922T222052Z-fleet04-B19-QFORM-r2/REPORT.md`,

`QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1`.

Inside its exact residual-diffuse rank-three null-coloop normal form, for `0<D_res<=1` and `|det M_3|>=1`, it proves a continuous `C_0` density satisfying

`||p_Q||_infinity<34 sqrt(log(e/D_res))`.                         (5.1)

Thus at the concrete gate

`2^-48<=D_res<=1`,                                                (5.2)

one has

`boxed: ||p_Q||_infinity
 <34 sqrt(log(e 2^48))
 =199.041078059...<200`,                                         (5.3)

with continuous density. This application is kept strictly inside the partner's proved exact-null-coloop scope. It is not asserted for the merely near-null r49/r50 carrier.

The partner's newer moving-ridge barrier remains active: a bounded arbitrary joint density is insufficient after product provenance is forgotten.

## 6. Verification

The exact singular-value/Gram dichotomy above was tested on 5,000 random noncommuting rectangular matrices. Each test recomputed the ACTUAL top-two SVD truncation, enforced `sigma_2(N)>=1/64` and tail Frobenius norm `<2^-16`, built the leverage-heavy sets, and checked the appropriate branch.

Observed branch counts:

- robust light-light branch: 3,668;
- `R`-side Gram failure / hub-star tests: 699;
- `C`-side Gram failure / hub-star tests: 724.

There were zero violations. The minimum observed ratio of actual `sigma_2(M)` to the sharper instance-specific lower bound was `1.00000028577`; the minimum observed star norm divided by its instance-specific lower bound was `1.56882950357`. These computations are diagnostics only; Theorem 2.1 has the exact proof above.

## 7. Status

Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.

Full universal continuous-density conclusion: **OPEN**.

New r50 robust branch: source-valid full-law fractional smoothing `H_(1/4)<15.732`, hence interval concentration `<13.229 delta^(1/4)`, but no `L^infinity` conclusion.

New r50 failure branch: an actual literal physical hub-star `>511/65536`; no endpoint density conclusion from that star alone.

No task, schedule, enabled/paused state, notification, email setting, permission, installation, public release, paid call, remote workflow or cross-account authentication is changed by this report.
