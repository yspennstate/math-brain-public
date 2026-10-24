SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-22T23:20:19Z.
attacking: the double-small leakage chamber via an exact Cauchy--Binet mixed-packet identity, then splice it into the tripartite heavy-hub reduction.

# account01/B10 — exact mixed-packet identity for the generated-mismatch chamber

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / NEW_EXACT_STRUCTURAL_IDENTITY / DOUBLE_SMALL_CHAMBER_REDUCED / FULL_TARGET_OPEN`.

The full owner conjecture remains OPEN. All inputs below are the original independent real coordinates with density caps at most one. No moment, compact-support, Gaussian, log-concavity, or post-rotation independence hypothesis is used.

Fresh control was resolved at `yspennstate/math-research-brain@19c4c8d5a107dd437f340087666c78922efd0700`; OWNER CONTROL revision remained `2026-09-22.15`, QFORM-only. The live corrections against arbitrary-joint rank-three coarea, positive conditional projection-height moments, law-uniform pointwise quadratic-phase decay, conditional-cap-as-independence, fiber-supremum reduction, and reciprocal-single-minor completion are retained.

## 1. Completed partner state actually used

The newest completed designated partner is account02/B10,

`yspennstate/math-open-problems@9005415f079b7b46c0618c0187bf29b3f8d44167`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260922T225540Z-account02-B10-QFORM-auto11/REPORT.md`.

It gives the tripartite heavy-hub delete-or-isolate reduction once a disjoint three-bank exterior packet of size at least `1/256` is available. In a normalized selected core, a heavy row can either be conditioned away while retaining an exact-rank-three matrix with `|det|,sigma_min>=2^-18`, or isolated as a singleton hub against two original-coordinate banks with a fixed-hub packet at least `1/512`; a diffuse child is then paid by the actual inequality

`||p_Q||_infinity <= 768`.                                           (1.1)

The immediately preceding account02/B10 generated-mismatch theorem is

`yspennstate/math-open-problems@ceae35deb4625f33bb99551dc50e455285d44da0`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260922T214629Z-account02-B10-qform/REPORT.md`.

After product-safe null-bank compression and residual paving it gives one genuine independent null coordinate `u_0=sqrt(c)r`,

`c>=7/9`, `D:=|det M|>=1/2`, `sigma_min(M)>=1/2`,

and a partition of the complementary ORIGINAL coordinates into banks `J,K`. Writing each complementary spectral row as

`u_j=(alpha_j,v_j) in R r direct_sum r^perp`,

put

`S_G=sum_(j in G) v_j v_j^T`,
`alpha_G=V_G p_G+eta_G`, `V_G^T eta_G=0`, `tau_G=||eta_G||^2`.

Then

`S_J+S_K=I_2`, `det S_J det S_K>=1/640`,                         (1.2)

and, with `d=p_J-p_K`,

`p_J=S_K d`, `p_K=-S_J d`,
`rho:=1-c=E_gen+tau_J+tau_K`,
`E_gen:=d^T S_J S_K d`.                                           (1.3)

The same partner theorem pays every state with

`max(tau_J,tau_K)>=1/64`

by a bounded continuous density, with its stated bound `<46.282`. Therefore the only leakage chamber addressed below is

`0<tau_J,tau_K<1/64`.                                             (1.4)

This is an actual inequality-level application of the designated partner result, not merely a citation.

## 2. Exact mixed Cauchy--Binet identity

For `G=J,K`, define the full three-dimensional bank Gram

`H_G=sum_(j in G) u_j u_j^T`.

Let

`E_21 := sum_(i<j in J, k in K) det(u_i,u_j,u_k)^2`,
`E_12 := sum_(i in J, j<k in K) det(u_i,u_j,u_k)^2`.               (2.1)

These are aggregate squared spectral-volume packets; no individual triple is selected.

### Theorem 2.1 — `QFORM-DOUBLE-SMALL-MIXED-PACKET-IDENTITY-v1`

In the state (1.2)--(1.3),

`boxed{
E_21+E_12
 = rho - tau_J det S_J - tau_K det S_K
 = E_gen + tau_J(1-det S_J)+tau_K(1-det S_K)
 >= E_gen.
}`                                                                     (2.2)

#### Proof

The full complement Gram is exactly

`H_J+H_K = I_3-c rr^T`.

In the basis `(r,r^perp)` this is `diag(rho,1,1)`, hence

`det(H_J+H_K)=rho`.                                                   (2.3)

Cauchy--Binet expresses this determinant as the sum of squared determinants over all three-row minors of the complementary frame. Partition those minors by the number of rows chosen from `K`. The all-`J` and all-`K` contributions are `det H_J` and `det H_K`, while the mixed contributions are exactly `E_21` and `E_12`. Thus

`rho=det H_J+E_21+E_12+det H_K`.                                    (2.4)

The determinant-one regression shear from the partner state gives exactly

`det H_G=tau_G det S_G`, `G=J,K`.                                  (2.5)

Substitute (2.5) in (2.4) and then use (1.3). Since `0<=S_G<=I_2`, every eigenvalue of `S_G` is at most one, so `det S_G<=1`. This proves (2.2). QED.

The important point is that the small orthogonal leakages cannot cancel the generated mismatch at the aggregate exterior-volume level: their contribution in (2.2) is nonnegative.

## 3. Every double-small state has a constant tripartite packet

A completed compatible result from account03/B10 r20 is

`yspennstate/math-open-problems@7acd371ee2ee83a7fae12d7bedb38bc99c051b6d`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B10/20260922T221548Z-account03-B10-QFORM-r20/REPORT.md`.

Its random-split lemma says that a mixed packet `E_21` (respectively `E_12`) can be converted, by splitting the bank contributing two rows, into three DISJOINT original-coordinate banks while retaining at least half the packet. Its near-unit-null-row argument also gives a tripartite packet `>61/256` whenever `c>61/64`.

### Theorem 3.1 — `QFORM-DOUBLE-SMALL-TO-TRIPARTITE-CORE-v1`

Every state satisfying (1.4) has three disjoint original-coordinate banks `B_1,B_2,B_3` with

`boxed{
T:=sum_(i in B_1,j in B_2,k in B_3) det(u_i,u_j,u_k)^2 >= 1/256.
}`                                                                     (3.1)

#### Proof

There are two cases.

**Case A: `E_gen>=1/64`.** By (2.2),

`E_21+E_12>=1/64`,

so one of the two mixed packets is at least `1/128`. Apply the account03/B10 random-split lemma to the bank supplying the two rows. A deterministic split retains at least one half, yielding

`T>=1/256`.                                                          (3.2)

**Case B: `E_gen<1/64`.** Since both defects are strictly below `1/64`, (1.3) gives

`rho=E_gen+tau_J+tau_K<3/64`,

hence

`c=1-rho>61/64`.                                                     (3.3)

The account03/B10 near-unit-null-row packet theorem then supplies disjoint banks with

`T>61/256>1/256`.                                                    (3.4)

This exhausts the double-small chamber. QED.

Thus the two small Schur defects are no longer a separate singular parameter regime: before any reciprocal local-minor payment, the whole chamber carries a fixed amount of tripartite exterior volume.

## 4. Uniformly conditioned selected core and direct partner splice

For the three banks from Theorem 3.1 set

`G=sum_(i in B_1 union B_2 union B_3) u_i u_i^T`.

The account03/B10 mixed-discriminant certificate gives

`det G>=T>=1/256`,
`lambda_min(G)>=1/256`,                                             (4.1)

because `0<G<=I_3`. Whitening only this deterministic spectral coefficient geometry produces an exact-rank-three active matrix

`N=G^(1/2) M G^(1/2)`

on the SAME selected original coordinates, with

`|det N|>=1/512`, `sigma_min(N)>=1/512`.                            (4.2)

If every normalized selected-core leverage is at most `1/2`, the completed diffuse-core Fresnel--Brascamp--Lieb theorem applied in account03/B10 gives

`boxed{||p_Q||_infinity<=96}`                                      (4.3)

and a continuous density.

If a normalized selected-core row has leverage `>1/2`, apply the newest designated account02/B10 delete-or-isolate theorem quoted in Section 1. It gives a child exact-rank-three block with

`|det|,sigma_min>=2^-18`.                                          (4.4)

Whenever that child is diffuse, the actual partner inequality (1.1) yields

`boxed{||p_Q||_infinity<=768}`                                     (4.5)

uniformly in every conditioned ORIGINAL-coordinate realization.

If instead the child remains non-diffuse, the partner theorem reduces it either to another deletable heavy-row state or to a singleton hub plus two independent original-coordinate banks carrying a fixed-hub exterior packet at least `1/512`. The partner's exact target construction shows that this fixed-hub packet cannot be paid by pigeonholing one scalar pivot, pair determinant, or principal triple.

Accordingly the first unpaid rank-three implication is now the genuinely aggregate one

`QFORM-SINGLETON-HUB-TWOBANK-AGGREGATE-PAYMENT-v1`,

with the separate warning that repeated deletion alone is not a dimension-free proof because the spectral lower bound would compound through an arbitrarily long heavy-row cascade.

## 5. What this run changes

Before this identity, the account02/B10 double-small chamber was described in terms of two tiny leakage parameters and a generated mismatch, and the endpoint could appear to require a delicate interpolation as the leakages tend to zero. Theorem 2.1 shows that this is misleading at the aggregate exterior-volume level:

`E_21+E_12 >= E_gen`                                                (5.1)

exactly. Combined with the complementary near-coloop alternative `E_gen<1/64 => c>61/64`, every double-small state enters the already-developed fixed tripartite-packet machinery. No perturbative estimate in the source variables is needed.

This does NOT prove the arbitrary exact-rank-three theorem. The remaining obstruction is a uniformly conditioned core with a persistent normalized heavy hub and genuine internal transverse geometry in its two product banks. It also does not prove the full higher-rank owner conjecture.

Continuity is proved only in the paid diffuse branches (4.3) and (4.5) through their cited Fresnel--Brascamp--Lieb arguments. No continuity claim is made for the still-unpaid aggregate hub branch.

## 6. Status

- `QFORM-DOUBLE-SMALL-MIXED-PACKET-IDENTITY-v1`: **PROVED EXACT STRUCTURAL IDENTITY**.
- `QFORM-DOUBLE-SMALL-TO-TRIPARTITE-CORE-v1`: **PROVED SUPPORTING REDUCTION**.
- diffuse selected-core branch: **PAID**, continuous density `<=96`.
- diffuse child after designated-partner heavy-hub reduction: **PAID**, density `<=768`.
- singleton-hub/two-bank aggregate branch: **OPEN**.
- arbitrary exact-rank-three case: **OPEN**.
- full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
