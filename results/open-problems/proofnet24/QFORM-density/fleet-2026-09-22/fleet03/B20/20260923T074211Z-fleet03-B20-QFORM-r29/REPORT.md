SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B20, 2026-09-23T07:42:11Z.
attacking: the freshly isolated normalized-heavy J-core branch by conditioning exactly that finite original-coordinate core, applying fleet04/B20's conditioned-whitened theorem, and turning failure into a second universal finite physical core.

# fleet03/B20 r29 — conditioned-whitened compiler for the normalized-heavy near-coloop core

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Proof closure and keeper / quantitative inequalities  
**Fresh owner control:** revision `2026-09-22.15`; QFORM-only.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository transport is not native learned-memory ingestion.  
**Status:** `ESSENTIAL_STEP_APPLIED / HC DIFFUSE SUBBRANCH PAID / UNIVERSAL FINITE-CORE REDUCTION / FULL QFORM OPEN`.

The unrestricted conjecture remains open. This report attacks the first remaining exact-rank-three rank-two-cross branch after the fresh fleet02/B19 repartition theorem and its addendum. No moment, compact-support, connected-support, Gaussian, log-concave, post-rotation-independence, arbitrary-joint-coarea, perturbative deletion, or worst-fiber hypothesis is introduced.

## 1. Fresh incoming state

The fresh fleet02/B19 theorem is source-pinned at

`yspennstate/math-open-problems@59bf0ca9f45cc0128973ccc854f5c3697996f0b6`,

with main report

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260923T071320Z-fleet02-B19-QFORM/REPORT.md`

and late addendum

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260923T071320Z-fleet02-B19-QFORM/ADDENDUM.md`.

In its exact-rank-three rank-two-cross setup, write

`A=R M R^T`, `R^T R=I_3`,

and split the ORIGINAL physical coordinates as `I union J`. With rows `s_j` of `R_J`, put

`H=R_J^T R_J`, `W=(ker H)^perp`.

On the branch where `H|_W` is not already rank-dropping, fleet02/B19 assumes

`lambda_min(H|_W)>=1/64`

and defines normalized J-frame leverages

`ell_j=s_j^T(H|_W)^(-1)s_j`.

Its diffuse repartition theorem pays the branch continuously by `<776` when `max_j ell_j<=1/16`. Therefore every unpaid state in this chamber has the normalized-heavy core

`K0={j in J: ell_j>1/16}`.

Because `sum_{j in J} ell_j=2`, one has the strict cardinality bound

`|K0|<32`, hence

`boxed: |K0|<=31.`                                               (1.1)

The remaining alternative from the fleet02/B19 addendum is the separate near-rankdrop/double-coloop route. The present report attacks the HC branch (1.1).

## 2. Partner theorem used at its exact scope

The designated completed fleet04/B20 theorem is

`QFORM-conditioned-whitened-diffuse-extraction`,

source-pinned at

`yspennstate/math-open-problems@94bf446b8547b1124a37033e940ef594c460b64f`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B20/20260922T141640Z-fleet04-B20-QFORM-r2/REPORT.md`.

For a rank-r frame `U`, after conditioning any set `K` of ORIGINAL coordinates, put

`S=sum_{i notin K} u_i u_i^T=I-U_K^T U_K`, `delta=lambda_min(S)`.

If `S>0` and every remaining row obeys

`u_i^T S^(-1)u_i<=1/32`,                                        (2.1)

then the full quadratic law has a continuous density with

`boxed: ||p_Q||_infinity < 27/delta.`                            (2.2)

The conditioning creates only original-coordinate affine terms; no transformed random coordinates are asserted independent.

## 3. New theorem

### Theorem 3.1 — `QFORM-HC-CONDITIONED-WHITENED-FINITECORE-v1`

Retain the HC setup of Section 1 and define the spectral Gram of the normalized-heavy original-coordinate core

`T0:=sum_{j in K0}s_j s_j^T`                                    (3.1)

and the full residual frame Gram after conditioning exactly those coordinates

`S0:=I-T0`.                                                       (3.2)

Let

`delta0:=lambda_min(S0)=1-||T0||op`.                              (3.3)

Then exactly one of the following occurs.

**(A) finite-core coloop concentration.** `delta0<1/64`. Then the at-most-31 physical coordinates in `K0` carry more than `63/64` of the squared mass of some spectral unit direction:

`boxed: exists v, ||v||=1,  sum_{j in K0}<s_j,v>^2>63/64.`       (3.4)

**(B) conditioned-whitened diffuse payment.** `delta0>=1/64` and every residual row satisfies

`r_i^T S0^(-1) r_i<=1/32`.                                       (3.5)

Then fleet04/B20 applies directly and the full law has a continuous density with

`boxed: ||p_Q||_infinity < 27/delta0 <=1728.`                    (3.6)

**(C) second finite physical core.** `delta0>=1/64`, but (3.5) fails. Define

`K1={i notin K0: r_i^T S0^(-1)r_i>1/32}`.                        (3.7)

Then

`boxed: 1<=|K1|<=95`,                                             (3.8)

and every physical row outside `K0 union K1` obeys the partner's whitened diffuse threshold relative to `S0`. In particular the complete dangerous physical core has the universal cardinality bound

`boxed: |K0 union K1|<=31+95=126.`                               (3.9)

This is an exact original-coordinate finite-core reduction; no small coefficient or coordinate is deleted.

### Proof

Because `T0` is positive semidefinite and `T0<=H<=I`, equation (3.3) holds.

If `delta0<1/64`, then `||T0||op>63/64`. Let `v` be a unit top eigenvector of `T0`. Since

`v^T T0 v=sum_{j in K0}<s_j,v>^2`,

(3.4) follows. This proves (A). Notice that this is stronger than merely saying the entire J bank is near a line: a fixed set of at most 31 ORIGINAL coordinates captures the near-coloop direction.

Now assume `delta0>=1/64`. Then `S0` is positive definite. Conditioning exactly the variables in `K0` preserves independence of all residual original coordinates and leaves a conditional quadratic form with the same residual spectral frame and only affine/constant dependence on the conditioned values. Thus if (3.5) holds, the fleet04/B20 theorem (2.2) gives

`||p_Q||infinity <27/delta0 <=27*64=1728`,

with continuity. This is (B).

Finally suppose (3.5) fails and define `K1` by (3.7). Since the residual rows sum exactly to `S0`,

`sum_{i notin K0} r_i r_i^T=S0`.                                 (3.10)

Therefore the sum of the whitened residual leverages is an exact trace identity:

`sum_{i notin K0} r_i^T S0^(-1)r_i
 =tr[S0^(-1) sum_{i notin K0}r_i r_i^T]
 =tr(I_3)=3.`                                                     (3.11)

Every index in `K1` contributes strictly more than `1/32`, so

`|K1|/32<3`, hence `|K1|<96` and therefore `|K1|<=95`.            (3.12)

By definition all residual indices outside `K1` obey (3.5). Combining with (1.1) proves (3.9). QED.

## 4. Equation-level partner application

The actual inequality supplied to fleet04/B20 is not merely qualitative. On branch (B),

`delta0>=1/64`,
`max_{i notin K0} r_i^T S0^(-1)r_i<=1/32`.

Its theorem therefore gives

`||p_Q||infinity < 27/delta0 <= 1728`.

The density is continuous in this paid branch. The partner theorem is not extended into (A) or (C).

## 5. Why the finite-core count is useful

The fleet02/B19 HC alternative previously said only that normalized J leverage is non-diffuse. Theorem 3.1 now makes the obstruction finite in ORIGINAL coordinates:

- either at most 31 original coordinates themselves capture `>63/64` of one spectral direction;
- or the whole HC branch is continuously paid by `<1728`;
- or all failure of the conditioned-whitened gate is carried by a second set of at most 95 original coordinates, so at most 126 coordinates contain every currently dangerous row while the complement is whitened-diffuse relative to the exact retained residual Gram.

The count 95 is dimension-free because it comes from the exact rank-three trace `sum leverage=3`, not from a physical-coordinate pigeonhole or a good-minor selection.

## 6. First unpaid implication after this run

Within the fresh exact-rank-three rank-two-cross HC route, the first remaining implication is now

`QFORM-HC-126CORE-PAYMENT-v1`:

pay either the `<=31` finite-core coloop concentration (A), or the `<=126` finite-core plus whitened-diffuse shell (C), without deleting the shell and without assuming any moment/support control. Natural permitted mechanisms are a finite physical pair/chain compiler, grouped-coordinate/ridge payment, or a second conditioning step whose determinant loss is paid by an aggregate bank resource rather than by a vanishing atom.

The separate near-rankdrop/double-coloop branch from fleet02/B19 remains open, as do arbitrary-extra-spectrum/N3 descent and two independent end-to-end reviews.

## 7. Status

- `QFORM-HC-CONDITIONED-WHITENED-FINITECORE-v1`: **PROVED**.
- HC diffuse subbranch: **PAID**, continuous density, explicit `<1728`.
- HC obstruction: reduced to at most 31-coordinate coloop concentration or at most 126-coordinate dangerous core plus exact whitened-diffuse shell.
- Full QFORM theorem: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity: **OPEN**; continuity is proved only in branch (B) here.
