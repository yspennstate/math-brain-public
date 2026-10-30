SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B14, 2026-09-23T19:38:35Z.
attacking: Fisher-information localization without fragment normalization—prove exact convex/translation mixture homogeneity for the newest projected-information theorem, then test whether rough finite-fragment extremes can enter that class with a uniform information budget.

# fleet02/B14 auto11 — Fisher translation-mixture localization and the active scale barrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **PROVED SUPPORTING LOCALIZATION THEOREM + EXACT PROOF-INTERFACE OBSTRUCTION / FULL QFORM OPEN**  
Continuity: not claimed for the full target.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The newest projected-Fisher theorem gives a dimension-free full-matrix QFORM bound when the selected large-eigenspace Fisher budget

`J_E = sum_i ell_i I(f_i)`

is quantitatively controlled. The correct localization question is therefore not whether one may split an active marginal into finitely many conveniently located pieces. It is whether the information payment can be made **after the positive pieces have been re-aggregated at full mass**, so that arbitrary translations and countably many remote components cost nothing.

This run proves that translation/positive-mixture localization is indeed zero-tax at the level of Fisher action, but also proves an exact scale obstruction: cap-one fragments of mass `m` that retain unit-height geometry at spatial scale `m` have Fisher action of order `1/m`. Equal `N`-fragment laws therefore have information of order `N^2`, even when they are perfectly Fisher-regular. Consequently the Fisher theorem is a genuine no-moment translation-mixture theorem, but it cannot be the missing closure mechanism for arbitrary fragmented cap-one laws by scale-normalized approximation.

The sharpened unpaid implication is

**`QFORM-SIGNED-SCORE-AGGREGATION-OR-WHOLE-ACTIVE-EXIT-v1`**: before active-fragment scale normalization, either estimate the signed score term in the projected-Fisher identity by a cap/product cancellation that sees the reassembled marginal rather than its absolute Fisher action, or force a whole-law D'/D5/ridge/hub/pair/rough-core certificate. A bounded fragment count, bounded diameter, moment assumption, or normalized-cell Fisher payment cannot substitute for this step.

## 2. Fisher action is exactly mass-homogeneous and convex

For a nonnegative finite subdensity `rho` with `sqrt(rho) in H^1`, define its unnormalised Fisher action

`mathcal J(rho) = integral_{rho>0} |rho'(x)|^2/rho(x) dx`
`               = 4 ||(sqrt rho)'||_2^2`.                                  (2.1)

If `rho=m f` with `f` a probability density, then

`mathcal J(rho)=m I(f)`.                                                     (2.2)

Translations are free:

`mathcal J(rho(.-a))=mathcal J(rho)`.                                       (2.3)

For finitely many positive subdensities `rho_j`, pointwise Cauchy--Schwarz gives, on the set where their sum is positive,

`|sum_j rho_j'|^2/(sum_j rho_j)
 <= sum_j |rho_j'|^2/rho_j`.                                                (2.4)

Integration yields

`boxed{ mathcal J(sum_j rho_j) <= sum_j mathcal J(rho_j). }`                (2.5)

The countable version follows by applying (2.5) to partial sums and the standard lower semicontinuity of the `H^1` norm of square roots, or equivalently by the integral-mixture Cauchy--Schwarz argument below.

For a measurable family of probability densities `f_theta` and a probability mixing law `pi`, put

`f(x)=integral f_theta(x) pi(dtheta)`.

Whenever the right side below is finite,

`|f'(x)|^2/f(x)
 <= integral |f_theta'(x)|^2/f_theta(x) pi(dtheta)`,                         (2.6)

hence

`boxed{ I(f) <= integral I(f_theta) pi(dtheta). }`                           (2.7)

No support, center, diameter, tail or moment assumption appears.

### Translation-mixture corollary

If `g` is any probability density with finite Fisher information and `nu` is an arbitrary probability measure, then

`f=g*nu`

satisfies

`boxed{ I(g*nu) <= I(g). }`                                                 (2.8)

Indeed the components in (2.7) are the translates `g(.-a)`. The mixing measure may have arbitrarily remote atoms, unbounded support, or no moments. This generalizes the newest Fisher source's particular compact kernel `cos^2(pi x/2) 1_[-1,1]` to every finite-information base kernel.

Thus arbitrary translation fragmentation is harmless **provided the active component shape/scale is not normalized separately before aggregation**.

## 3. Projected-Fisher subprobability compiler

Let `A` have an `r`-dimensional invariant subspace `E`, `r>=3`, with orthonormal frame `U`, selected eigenvalues of modulus at least `s>0`, and leverage weights

`ell_i=(UU^T)_{ii}`.

Suppose each original-coordinate probability density admits a positive decomposition

`f_i = sum_j rho_{ij}`,

where `rho_{ij}` has mass `m_{ij}`. Put

`J_i^* = sum_j mathcal J(rho_{ij})
       = sum_j m_{ij} I(rho_{ij}/m_{ij})`,                                  (3.1)

and

`J_E^* = sum_i ell_i J_i^*`.                                                (3.2)

By (2.5), the actual projected information obeys

`J_E <= J_E^*`.                                                             (3.3)

The projected-Fisher theorem at

`yspennstate/math-open-problems@4a65677d185d35154dc3dfae320c5df9f939b8a2`,
`proofnet24/QFORM-density/interactive/20260923T184054Z-fisher-continuation/FISHER_INFORMATION.md`

therefore gives immediately

`boxed{ ||p_Q||_infinity
 <= (r-1) J_E^*/[2s(r-2)^2]. }`                                             (3.4)

If the **final aggregated marginals** satisfy the owner cap `f_i<=1`, the cap-improved theorem yields

`boxed{ ||p_Q||_infinity
 <= [r d_* + sqrt(J_E^* d_*)]/(4s), }`                                      (3.5)

where

`d_* = min(D_r, J_E^*/(r-2)^2)`,
`D_r = 2 r v_r^(2/r)/(r-2)`.                                               (3.6)

The right side is monotone in the information parameter, so replacing the true `J_E` by its upper bound `J_E^*` is legitimate. Importantly, the normalized pieces `rho_{ij}/m_{ij}` need not themselves satisfy the cap one: the cap is paid only on the reassembled marginal.

### Exact zero-tax condition

If every positive piece is a translated copy of a fixed normalized shape `g_i`,

`rho_{ij}(x)=m_{ij} g_i(x-a_{ij})`,
`sum_j m_{ij}=1`,

then

`J_i^*=I(g_i) sum_j m_{ij}=I(g_i)`.                                        (3.7)

Hence (3.4)-(3.5) have **exactly the same constant for one component or arbitrarily many countable remote components**. This is a genuine localization/mixture principle compatible with arbitrary translations and unbounded support; it has no hidden fragment-count or diameter parameter.

## 4. Scale law: center is free, inverse square scale is not

Let `g` be a probability density with finite `I(g)` and define a subdensity of mass `m` at scale `a>0` and center `b` by

`rho_{m,a,b}(x)=m a^{-1} g((x-b)/a)`.                                       (4.1)

A change of variables gives the exact homogeneity

`boxed{ mathcal J(rho_{m,a,b}) = m a^{-2} I(g). }`                          (4.2)

The center `b` vanishes completely. But if `g<=1` and a fragment retains cap-one height at its natural mass scale `a=m`, then

`mathcal J(rho_{m,m,b}) = I(g)/m`.                                          (4.3)

Thus splitting unit mass into equal pieces `m=1/N` and shrinking each piece to its own mass scale produces total Fisher action `N^2 I(g)`. This is not a defect of a proof by an avoidable triangle inequality: for disjoint components the convexity inequality (2.5) is an equality.

## 5. Exact smooth-fragment obstruction inside the owner target

Take the compact cap-one probability kernel used by the Fisher continuation,

`g(x)=cos^2(pi x/2) 1_{[-1,1]}(x)`,

for which

`I(g)=pi^2`.                                                               (5.1)

Choose any centers `a_1,...,a_N` whose intervals `[a_j-1/N,a_j+1/N]` are disjoint; for a severe translation test one may take `a_j=4^j`. Define

`eta_{j,N}(x)=g(N(x-a_j))`,
`f_N(x)=sum_{j=1}^N eta_{j,N}(x)`.                                         (5.2)

Each `eta_{j,N}` has mass `1/N`, cap at most one, and square-root in `H^1`. Therefore `f_N` is a legal cap-one probability density with arbitrary fragment separation and no imposed moment bound. From (4.2),

`mathcal J(eta_{j,N})=N pi^2`.                                              (5.3)

The supports are disjoint, so equality holds in (2.5):

`boxed{ I(f_N)=N^2 pi^2. }`                                                 (5.4)

This is an exact Fisher-regular finite-fragment family, not a discontinuous indicator approximation.

### The Fisher certificate on `A=I_3`

Let `X_1,X_2,X_3` be independent with common density `f_N` and

`Q_N=X_1^2+X_2^2+X_3^2`.                                                    (5.5)

The matrix `A=I_3` has exactly three eigenvalues of modulus one, so this is squarely inside the full target. Here `r=3`, `s=1`, `ell_i=1`, and

`J_E=3 pi^2 N^2`.                                                          (5.6)

Since

`D_3=6(4pi/3)^(2/3)=15.591108358883012...`,                               (5.7)

the cap-improved Fisher theorem gives

`||p_{Q_N}||_infinity
 <= 3D_3/4 + pi N sqrt(3D_3)/4`
` = 11.69333126916226... + 5.371418661711253... N`.                        (5.8)

So the information certificate grows linearly with fragment refinement, despite the final marginal cap staying exactly one.

## 6. Required fixed-source result applied to the same obstruction

The required source at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was read through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed Theorem A states that in dimension three, if all eigenvalues have modulus at least `sigma`, then arbitrary cap-one independent inputs and arbitrary linear terms satisfy

`||p_Q||_infinity <= 6 sqrt(pi)/sigma`.                                    (6.1)

Applying it to the **same** `A=I_3` and the same fragmented laws (5.2) yields

`boxed{ ||p_{Q_N}||_infinity <= 6 sqrt(pi)
       = 10.634723105433096... }`                                           (6.2)

for every `N` and every choice of disjoint centers, including exponentially separated `a_j=4^j`.

Therefore the divergence in (5.8) is a proof-interface obstruction, not a QFORM counterexample and not evidence that the true density grows. The whole-law source certificate is completely insensitive to the active fragment scale that makes Fisher information blow up.

## 7. Material application of the designated partner fleet03/B14

The newest compatible designated partner result is

`yspennstate/math-open-problems@78e87f9d9fe723b40aa38e71426458283366f8a5`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B14/20260923T183544Z-fleet03-B14-QFORM-auto11/REPORT.md`.

It proves the rough-hub `L^3` core plus disjoint translated-square compiler. In particular, for arbitrary independent cap-one variables,

`Q_* = 2 X_0 L + (1/2) V^2 + X_5^2`,                                      (7.1)

with

`L=(X_1+X_2+X_3+X_4)/2`,
`V=(X_1+X_2-X_3-X_4)/2`,                                                   (7.2)

the nonzero spectrum is `{1,-1,1/2,1}` and the partner gives

`boxed{ ||p_{Q_*}||_infinity <= 45^(2/3) 2^(10/9)
       = 27.32872992777147... }`                                            (7.3)

uniformly over arbitrary translations, remote fragments, unbounded supports and conditioning-generated affine terms in the compiler's stated scope.

Apply (7.3) with **all six original-coordinate marginals equal to the fragmented `f_N` in (5.2)**. The partner constant is independent of `N` and of all fragment centers.

By contrast, if the projected-Fisher theorem selects the three unit-modulus directions `span(e_0,L,e_5)`, then the leverage weights sum to three. Since every original coordinate has the same information `N^2 pi^2`,

`J_E = N^2 pi^2 sum_i ell_i = 3 N^2 pi^2`,                                 (7.4)

so its cap-improved certificate is again exactly (5.8), growing linearly in `N`.

This is the complementary comparison needed for localization: the partner whole-law rough-hub/square mechanism survives arbitrary active fragmentation, whereas absolute projected Fisher payment does not. The correct order is to exploit the whole active product structure before converting rough scale into a reciprocal regularity norm.

## 8. What this proves and what it does not

**Proved.** Fisher action has exact subprobability homogeneity and convexity. Arbitrary countable translation mixtures of a fixed Fisher-regular shape have zero information tax, hence the newest projected-Fisher QFORM theorem transfers to them with no fragment count, center, support diameter, tail or moment parameter. The same remains true for arbitrary per-coordinate positive decompositions satisfying a uniform mass-weighted Fisher budget.

**Proved obstruction.** Unit-height cap-one fragmentation at mass scale `m` has Fisher action `I(g)/m`; the explicit legal family (5.2) has exact information `N^2 pi^2`. Both the required fixed-source Theorem A and the designated partner whole-law theorem remain uniformly bounded on corresponding exact-target forms. Thus bounded projected Fisher information cannot be the missing localization closure class for arbitrary cap-one inputs.

**Not proved.** No counterexample to QFORM is produced. No bounded fragment count, diameter, moment, connected-support, log-concavity or post-rotation independence is assumed. This run does not remove the Fisher regularity hypothesis by approximation. The remaining full-target possibility identified in the Fisher continuation is a new bound on the signed score term that exploits cancellation/product provenance before taking its absolute Fisher norm; alternatively one needs one of the already-completed whole-law volume/hub/pair/ridge mechanisms to fire first.

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. Full-target continuity remains a separate open issue.

## 9. Source discipline

Fresh owner control remained revision `2026-09-22.15`, QFORM-only, with no fleet02/B14 pause observed before publication. Consumed corrections include the false law-uniform pointwise oscillatory decay, spectral-fiber dimension loss, no independence after rotation, bounded-diameter localization failure, and no universal fixed fragment-count reduction. None is used as a premise.

Mathematical sources actually used:

1. `math-open-problems@4a65677d185d35154dc3dfae320c5df9f939b8a2`: projected Fisher-information theorem and its cap improvement.
2. `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`: fixed required `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`; completed Theorem A applied in (6.2).
3. `math-open-problems@78e87f9d9fe723b40aa38e71426458283366f8a5`: designated fleet03/B14 rough-hub `L^3` plus translated-square theorem, applied in (7.1)-(7.4).

No FEI/install/benchmark work, scheduler mutation, email/notification action, cross-account authentication, paid call, public release, remote workflow or permission change was used.
