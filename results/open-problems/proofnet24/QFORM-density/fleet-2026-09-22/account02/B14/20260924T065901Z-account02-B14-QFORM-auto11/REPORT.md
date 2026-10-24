SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-24T06:59:01Z.
attacking: cap-weighted active-mixture localization — use the newest partner cap-saturation congruence to characterize exactly when arbitrary positive active fragments are zero-tax, and prove the sharp tiny-cell obstruction when that condition fails.

# account02/B14 — cap-weighted active-mixture localization

Run: `20260924T065901Z-account02-B14-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: translations and localization  
Status: `NEW SUPPORTING LOCALIZATION THEOREM / SHARP ACTIVE-CELL BARRIER / FULL QFORM OPEN / CONTINUITY OPEN`.

## 1. Scope and source discipline

The owner target is unchanged: independent real coordinates with probability densities at most one, arbitrary real symmetric quadratic matrix with at least three eigenvalues of modulus at least one, and one universal essential density bound. No moment, compact-support, connected-support, finite-fragment, log-concavity, post-rotation independence or diagonal-basis assumption is introduced.

The fixed required source was read at exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

folder `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md` and `COUNTEREXAMPLE_SEARCH.md`. The completed result used below is Theorem A from `COUNTEREXAMPLE_SEARCH.md`: for three independent cap-one variables, every invertible symmetric `3 x 3` quadratic matrix `H` with

`min_j |lambda_j(H)| >= sigma`

and every deterministic affine term has

`||p||_(infinity,ess) <= 6 sqrt(pi)/sigma`.                                  (1.1)

The newest compatible designated-partner result actually applied is account03/B14
`QFORM-CAP-SATURATION-CONGRUENCE-LOCALIZATION-v1`, canonical mathematics

`yspennstate/math-open-problems@27524c090248516692abfa19911c411adaa62c23`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260924T064640Z-account03-B14-QFORM-auto11/REPORT.md`.

Its spectral ingredient is the following signed threshold monotonicity. If `S>=I` is positive definite and `H` is symmetric, then for every `t>0`, the number of eigenvalues of `SHS` at least `t` is no smaller than for `H`, and likewise the number at most `-t` is no smaller. This is a Courant--Fischer consequence and is valid for indefinite matrices.

The earlier designated-partner theorem
`QFORM-DISJOINT-BANK-SCHUR-LOCALIZATION-v1` at
`math-open-problems@4366a5648435eb9bfd6dcc40d4aa6fc3b3e67f6c`
is treated as existing work, not relabelled. Section 4 below shows it is recovered as a coarse corollary of the new cap-weighted formula.

## 2. First unpaid implication

`QFORM-MASS-PROPORTIONAL-CAP-DECOMPOSITION-OR-AGGREGATE-BEFORE-ACTIVE-LOCALIZE-v1`:

> Before a three-curvature certificate is paid cell-by-cell, either the unnormalised cap of every active positive piece must be proportional to that piece's mass (so the normalized cap remains uniformly bounded), or the active marginals must be reassembled before inverse curvature is paid. Generic spatial fragments do not have this homogeneity, and the failure is sharp already for `A=I_3`.

The theorem below gives the exact positive compiler and Section 5 gives the obstruction.

## 3. Cap-weighted active-mixture compiler

### Theorem 3.1 — `QFORM-CAP-WEIGHTED-ACTIVE-MIXTURE-COMPILER-v1`

Let `Y_1,Y_2,Y_3` be independent probability variables with densities `f_r`. Let `W` be any independent environment. Let `B` be an invertible real symmetric `3 x 3` matrix, and consider

`Q = Y^T B Y + ell(W)^T Y + c(W)`,                         (3.1)

where `ell(W)` and `c(W)` are arbitrary measurable functions for which the expression is finite almost surely.

For `r=1,2,3`, let

`f_r = sum_{j in J_r} rho_{rj}`                            (3.2)

be an arbitrary finite or countable decomposition into nonnegative subdensities. Write

`m_{rj} = integral rho_{rj}`,                              (3.3)

and discard zero-mass pieces. Define the unnormalised cap and normalized cap

`L_{rj} = ||rho_{rj}||_infinity`,
`k_{rj} = L_{rj}/m_{rj}`.                                  (3.4)

For a cell `alpha=(j_1,j_2,j_3)`, put

`m_alpha = product_r m_{r j_r}`,
`K_alpha = diag(k_{1j_1},k_{2j_2},k_{3j_3})`,
`sigma_alpha = min |eig(K_alpha^{-1} B K_alpha^{-1})|`.     (3.5)

Then `sigma_alpha>0` and the output has an essentially bounded density whenever the right side below is finite, with

`boxed:
 ||p_Q||_(infinity,ess)
 <= 6 sqrt(pi) sum_alpha m_alpha / sigma_alpha .
`                                                               (3.6)

The estimate is uniform in the environment and therefore retains arbitrary conditioning-generated affine terms. No support radius, diameter, fragment count, separation or moment enters.

#### Proof

Fix one cell `alpha`. Normalize its three factors:

`g_{r,alpha}(y) = rho_{rj_r}(y)/m_{rj_r}`.                 (3.7)

These are independent probability densities with exact essential caps `k_{rj_r}`. Define

`Z = K_alpha Y`.                                           (3.8)

Coordinate scaling preserves independence, and the density of each `Z_r` has essential supremum one. On this cell,

`Y^T B Y + ell(W)^T Y + c(W)
 = Z^T H_alpha Z + ell_alpha(W)^T Z + c(W)`,               (3.9)

where

`H_alpha = K_alpha^{-1} B K_alpha^{-1}`,
`ell_alpha(W)=K_alpha^{-1} ell(W)`.                         (3.10)

Condition on `W`. The fixed-source three-dimensional Theorem A, equation (1.1), gives the normalized cell output density bound

`||p_{Q | alpha,W}||_infinity <= 6 sqrt(pi)/sigma_alpha`,  (3.11)

uniformly in the conditioned affine coefficient. The unnormalised product cell has mass `m_alpha`, hence its pushforward density has height at most

`6 sqrt(pi) m_alpha/sigma_alpha`.                           (3.12)

The original product density is the monotone sum of the product cells. Pushforward commutes with this positive sum. Summing (3.12), then averaging the independent environment, proves (3.6). QED.

### Corollary 3.2 — exact zero-tax criterion

Suppose there are finite constants `M_1,M_2,M_3>0` such that every positive piece satisfies

`L_{rj} <= M_r m_{rj}`                                    (3.13)

for every `r,j`. Put

`M=diag(M_1,M_2,M_3)`,
`H_0=M^{-1} B M^{-1}`,
`sigma_0=min |eig(H_0)|`.                                  (3.14)

Then

`boxed:
 ||p_Q||_(infinity,ess) <= 6 sqrt(pi)/sigma_0 .
`                                                               (3.15)

In particular, arbitrary finite or countable active localization has no tax at all under the mass-proportional cap condition (3.13).

#### Proof

For every cell, `K_alpha <= M` coordinatewise. Set

`R_alpha=K_alpha^{-1}M >= I`.                              (3.16)

Then

`K_alpha^{-1} B K_alpha^{-1}
 = R_alpha H_0 R_alpha`.                                   (3.17)

Apply the newest account03/B14 signed-threshold congruence lemma at threshold `sigma_0`. Since all three eigenvalues of `H_0` have modulus at least `sigma_0`, all three eigenvalues of (3.17) also have modulus at least `sigma_0`, with the signed counts preserved. Thus `sigma_alpha>=sigma_0`. Equation (3.6) becomes

`||p_Q||_infinity
 <= (6 sqrt(pi)/sigma_0) sum_alpha m_alpha
 = 6 sqrt(pi)/sigma_0`,                                    (3.18)

because `sum_alpha m_alpha=product_r sum_j m_{rj}=1`. QED.

This criterion is compatible with completely remote and unbounded mixtures. It concerns only mass and unnormalised density cap, not location.

## 4. Cap-aware disjoint-bank localization

The same calculation sharpens the existing disjoint-bank theorem without changing its structural hypotheses.

Suppose three disjoint original-coordinate banks produce independent linear forms

`Y_r=u_r^T X_{I_r}`                                       (4.1)

and, after conditioning the outside original coordinates, the active quadratic part is `Y^T B Y` plus an arbitrary affine term. Let

`k_r=||p_{Y_r}||_infinity`,
`K=diag(k_1,k_2,k_3)`.                                     (4.2)

Then the one-cell case of Theorem 3.1 gives the exact cap-aware certificate

`boxed:
 ||p_Q||_(infinity,ess)
 <= 6 sqrt(pi)/sigma_min(K^{-1} B K^{-1}).
`                                                               (4.3)

This can be strictly stronger than the earlier bank theorem because it uses the actual aggregate bank caps rather than a worst-case projection cap.

Indeed, writing `rho_r=||u_r||_2` and `R=diag(rho_r)`, Ball--Rogozin gives

`k_r <= sqrt(2)/rho_r`.                                    (4.4)

Take `M=sqrt(2) R^{-1}` in Corollary 3.2. Then

`M^{-1} B M^{-1}=(1/2)RBR`,                               (4.5)

so (3.15) gives

`||p_Q||_infinity <= 12 sqrt(pi)/sigma_min(RBR)`,          (4.6)

which is exactly the existing account03/B14 disjoint-bank Schur-localization constant. Thus (4.3) is a genuine cap-aware refinement and (4.6) is its source-matched coarse corollary.

This is the precise sense in which the newest partner cap-saturation result can compensate a weak bank Hessian: one should aggregate each bank first, measure its final density cap, and only then pay inverse curvature.

## 5. Sharp active-cell barrier inside the exact target

The mass-proportional condition (3.13) is not a harmless technicality. Generic spatial fragmentation violates it maximally.

### Proposition 5.1 — `QFORM-THREE-ACTIVE-CELL-MASS-BARRIER-v1`

For `0<m<=1`, let

`rho_m(x)=1_{[-m/2,m/2]}(x)`                              (5.1)

and use the product submeasure `rho_m^{\otimes3}``, of total mass `m^3`. For the exact-target quadratic form

`Q(x)=x_1^2+x_2^2+x_3^2`, `A=I_3`,                       (5.2)

the unnormalised pushforward density satisfies

`p_m(s)=2 pi sqrt(s)` for `0<s<m^2/4`.                    (5.3)

In particular,

`boxed: p_m(m^2/16)=pi m/2.`                              (5.4)

Therefore no universal per-cell bound linear in the cell mass, `||p_m||_infinity <= C m^3`, is possible. The natural cell height is at least order `m=(m^3)^(1/3)`.

#### Proof

For `0<s<m^2/4`, the sphere `|x|=sqrt(s)` lies entirely inside the cube `[-m/2,m/2]^3`. Hence the sublevel mass is exactly the volume of the three-dimensional ball,

`mu_m{Q<=s}=(4 pi/3)s^(3/2)`.                             (5.5)

Differentiating gives (5.3), and substituting `s=m^2/16` gives (5.4). QED.

This lower scaling agrees with the cap-weighted source theorem. The normalized interval density has cap `k=1/m`, so `K=(1/m)I_3`, `K^{-1}I_3K^{-1}=m^2I_3`; equation (3.12) gives an upper cell height `6sqrt(pi)m`. Thus the loss from normalizing a tiny three-dimensional active cell is of the correct order in `m`, not merely a loose artifact of Theorem A.

The barrier is translation-uniform in the affine formulation: translating the cube by an arbitrary vector `a` and adding the corresponding affine term `-2a^T x+|a|^2` reduces exactly to `|x-a|^2`. Hence remote fragments cannot be repaired by a bounded-diameter shortcut when conditioning-generated affine terms are retained.

## 6. Real obstruction from the fixed source theorem

Take the genuine probability law with each coordinate uniform on `[-1/2,1/2]` and `A=I_3`. The fixed source Theorem A gives the whole-law inequality

`boxed:
 ||p_Q||_(infinity,ess) <= 6 sqrt(pi)
 = 10.634723105433096... .
`                                                               (6.1)

Now partition each marginal interval into `N` subintervals of length `1/N`, retaining the corresponding positive subdensities. Every marginal piece has

`m=1/N`, `L=1`, `k=N`.                                    (6.2)

For each of the `N^3` product cells,

`K=NI_3`,
`K^{-1}I_3K^{-1}=N^{-2}I_3`,
`sigma=N^{-2}`.                                            (6.3)

Applying the *same completed source theorem* cell-by-cell yields normalized cell height at most `6sqrt(pi)N^2`; restoring the cell mass `N^{-3}` gives

`||p_cell^(sub)||_infinity <= 6 sqrt(pi)/N`.               (6.4)

Summing cell suprema gives the fragment-first certificate

`boxed:
 6 sqrt(pi) N^2,
`                                                               (6.5)

while the unchanged whole law has the source-valid constant (6.1). Thus active fragment-first normalization followed by reciprocal curvature payment can lose a factor `N^2` on a fixed exact-target law.

The same bookkeeping can become infinite for countably fragmented unbounded support. Let

`m_j = 6/(pi^2 j^2)`                                      (6.6)

and let each marginal be the cap-one comb density equal to one on pairwise disjoint, arbitrarily remote intervals of lengths `m_j`. The whole law still satisfies (6.1), because Theorem A only uses the cap and the matrix. On a product cell `(j_1,j_2,j_3)`, the normalized cap matrix is

`K=diag(1/m_{j_1},1/m_{j_2},1/m_{j_3})`,                  (6.7)

so for `B=I_3`,

`sigma_alpha=min(m_{j_1}^2,m_{j_2}^2,m_{j_3}^2)`.          (6.8)

Already fixing `j_2=j_3=1` and letting `j_1 -> infinity`, the terms in (3.6) are proportional to

`m_1^2/m_{j_1}`,                                           (6.9)

whose sum diverges. Hence the fragment-first cap-weighted compiler is infinite on an arbitrary-countable unbounded comb although the actual whole-law output remains bounded by `6sqrt(pi)`. This is a proof-interface obstruction, not a QFORM counterexample.

## 7. Consequence for localization design

The safe proof order is now quantitative:

1. Aggregate each certificate-active marginal or original-coordinate bank first.
2. Measure its *final* density cap.
3. Saturate those caps by diagonal congruence.
4. Only then pay the three-dimensional curvature scale.
5. Arbitrary localization of an independent environment remains mass-linear and free.

If active positive pieces are localized first, zero tax is available exactly under the sufficient mass-proportional cap condition `L_{rj}<=M_r m_{rj}`. Ordinary spatial teeth have `L_{rj}=1` while `m_{rj}->0`, so they fall outside this safe regime; Proposition 5.1 shows the resulting cell-scale loss is real.

This leaves the full QFORM obstruction structural rather than translational. Starting from bare `s_3(A)>=1`, one still has to expose a physical/cross-volume/overlap/hub/grouped-bank chamber before the active product structure is fragmented. The newest punctured-hub correction remains respected: no claim is made that cap scaling by itself produces the required grouped compression.

## 8. Continuity and execution status

Only essential boundedness is asserted. Continuity remains a separate full-target question.

Repository retrieval and readback are authenticated, but native receiver-memory retrieval did not recover the exact prior QFORM state in this invocation. Therefore execution remains `WITHOUT_VERIFIED_BRAIN`.

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort and provider reasoning telemetry are not exposed and remain `UNKNOWN` / null.
