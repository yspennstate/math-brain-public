# Late-source addendum — correction integration and a lower-order robust exit

Status remains `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.

A later source-backed correction/event arrived after the main report was written: fleet02/B01 r30, brain commit `3e5a801b6cb1b5a4bd82b04dce31affb65290937`, corrected canonical report `math-open-problems@9cb571de79e312d740f10979dadaa943669235f8`. It independently records the same strict-N3 star-plus-square stress family used in Section 4 of this run and explicitly withdraws a different proposed shear-stable extension of Theorem H. Accordingly, Section 4 of the main report is now treated as an **independent confirmation/application, not a novelty claim**. This run does not use the withdrawn shear step; the exact Theorem-H application has separable product amplitude and remains valid.

A second fresh compatible result, fleet01/B01 at brain handoff `8b4f6e58fd48bca00b7c76f3c0a2b060372b17da`, canonical `math-open-problems@86f318f0826325e6df3504e1e8ec15f4316cc861`, proves a mixed-order minor Fourier theorem. This permits a useful strengthening of the dense-twist routing in the main report.

## Theorem `QFORM-MIXED-HUB-DPRIME-ROBUST-v1`

Keep the physical light-bank decomposition

`A_LL = D + B_0 + E`,

with `D` diagonal and `rank(B_0)<=r`. Let `I,J subset L` be disjoint and put `M=A[I,J]`. Suppose

`s_{r+3}(E[I,J]) >= gamma >0`.                                                        (A.1)

Let `Z=e_3(M^T M)` and let `alpha_i` be the natural 3-volume row marginal of row `i`. If

`max_i alpha_i <= h < 3/4`,                                                           (A.2)

then

`||p_Q||_infinity <= 6 sqrt(e) (2h)^(-1/2) (3-4h)^(-1) gamma^(-1)`.                  (A.3)

### Proof

The rank-`r` perturbation inequality gives

`s_3(M) >= s_{r+3}(E[I,J]) >= gamma`.

Therefore the top three singular values of `M` are at least `gamma`, and

`Z=e_3(M^TM) >= prod_{k=1}^3 s_k(M)^2 >= gamma^6`.

Apply the completed source theorem D' to the actual physical cross block `M`. Its bound is

`6 sqrt(e)(2h)^(-1/2)(3-4h)^(-1) Z^(-1/6)`,

which is at most (A.3). All other self blocks, hub terms, affine terms and extra spectrum remain arbitrary. QED.

At the concrete choice `h=2/3`,

`||p_Q||_infinity <= 9 sqrt(3e) gamma^(-1) <25.702 gamma^(-1)`.                       (A.4)

For the canonical rank-one light part (`r=1`) and `gamma=1/64`, every leaf cut with `s_4(E[I,J])>=1/64` and natural 3-volume row marginals at most `2/3` is therefore paid with density below `1644.866`.

## Mixed-order payment of a one-heavy-row residue

Still on such a cut, suppose the natural 3-volume law has a heavy row `i` with marginal `alpha>1/2`, but every conditional co-marginal given `i` is at most `1/2`. The fresh fleet01/B01 theorem gives

`||p_Q||_infinity <= 10 sqrt(e) [2 alpha Z / ||r_i||]^(-1/5)`.                       (A.5)

From (A.1), `Z>=gamma^6`, hence

`||p_Q||_infinity <= 10 sqrt(e) ||r_i||^(1/5) gamma^(-6/5)`.                         (A.6)

(the factor `2 alpha>1` was discarded). Thus, for any fixed row-norm threshold `R`, this branch is uniformly paid whenever `||r_i||<=R`. A surviving cut with `s_{r+3}(E[I,J])>=gamma` must consequently exhibit either a **clustered conditional co-heavy row** or a **large physical cross-row norm**, unless it was already paid by D'.

Combining this with the main report's unconditional D5 transfer gives the following rigorous hybrid routing for fixed `gamma`:

- `s_{r+5}(E[I,J])>=gamma` on some cut -> D5, density `<=5 sqrt(2e)/gamma`;
- `s_{r+3}(E[I,J])>=gamma` and natural 3-volume is `h`-diffuse -> D', (A.3);
- `s_{r+3}(E[I,J])>=gamma`, one row is heavy, no conditional row is co-heavy, and that row has norm at most `R` -> mixed-order theorem, (A.6);
- otherwise the unresolved dense-twist geometry has low higher cross rank, clustered co-heavy volume, or a genuinely large diffuse hub row.

This is a strict narrowing of the source-identified hybrid robustness gap. It does not claim that every N3 matrix admits the light-bank decomposition above; the end-to-end unpaid statement remains N3 itself.
