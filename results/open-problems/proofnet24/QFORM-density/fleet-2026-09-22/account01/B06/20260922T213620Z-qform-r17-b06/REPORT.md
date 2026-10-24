SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B06, 2026-09-22T21:36:20Z.
attacking: two-sided curvature absorption in the strong near-rank-two survivor by conditioning a physical vertex cover of the opposite self-block while preserving a two-direction cross smoother.

# account01/B06 QFORM r17 — physical vertex-cover absorption for two-sided curvature

## 0. Status, controls, and exact scope

Programme: `QFORM-DENSITY-3EIG-20260922`.

Run: `20260922T213620Z-qform-r17-b06`.

Assignment: curved fiber integration; retain product structure and avoid unrestricted fiber suprema.

Execution: `WITHOUT_VERIFIED_BRAIN`.

Fresh source used for the mathematical derivation: `yspennstate/math-research-brain@a401040c6d176da10e7aa9b9035d4ba82b1acef3`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. The full target remains OPEN / NOT PROVED / NOT DISPROVED. The separate continuity conclusion is not proved by the new theorem below.

The exact full target is unchanged: independent original coordinates have densities bounded by one, and a real symmetric matrix has at least three eigenvalues of modulus at least one. No moment, support, log-concavity, Gaussianity, diagonal-basis, or post-rotation-independence hypothesis is added.

Current corrections retained: no law-uniform pointwise quadratic-phase decay; no arbitrary-joint three-dimensional coarea bound; no positive moment bound for worst conditional projection densities; no unrestricted spectral-fiber supremum; no inference of one uniformly good physical minor from aggregate exterior mass; and no perturbative deletion of a small opposite self-block. In particular, the account02/B06 construction `QFORM-TWO-SIDED-SMALL-CURVATURE-PERTURBATION-FALSE-v1` is treated as a genuine obstruction to norm-small perturbation, not as a counterexample to the full QFORM target.

## 1. Source-valid inputs actually applied

### 1.1 Assigned partner account02/B06

The latest completed partner theorem used here is account02/B06 `QFORM-ONE-SIDED-RANK2-CROSS-SMOOTHER-v1`, canonical source

`yspennstate/math-open-problems@dc9752d372165b011f4c8b1101174a6698ae2c64`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T210504Z-abc2116c80c5/REPORT.md`.

Its precise statement used below is this. If the original coordinates are partitioned into product banks `I,J,K`, and after conditioning `K` one has

`R = F(X_I)+2 X_I^T H X_J+b^T X_J+c`,

where `F` is arbitrary measurable, the `J` bank has no quadratic self-term, and `s_2(H)=sigma>0`, then

`||p_R||_infinity <= e sqrt(pi)/sigma`.                                      (1.1)

The proof is product-preserving: it conditions the entire original `I` bank, retains a genuine linear projection on the independent `J` bank, and integrates the reciprocal coefficient against a two-dimensional product-derived projection density. It neither selects a physical minor nor uses a fiber supremum.

The same partner run proves that replacing the zero `J` self-block by an operator-norm-small one is invalid in general. Thus the theorem below uses exact physical conditioning to remove that self curvature rather than discarding it perturbatively.

### 1.2 Dependence-safe outer square

I also use account04/B18 `QFORM-DEPENDENT-SQUARE-SMOOTHING-v1`, canonical source

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T113729Z-account04-B18-qform-r1/REPORT.md`.

If `R` has density cap `M`, and conditionally on `R=r` the translated original-coordinate variable `V_r` has density cap one, then for `a!=0`,

`T=R+aV_R^2`

has

`||p_T||_infinity <= 2 sqrt(M/|a|)`.                                  (1.2)

No independence between `R` and `V_R` is required.

### 1.3 Current near-rank-two state

The newest completed B08 compression, account03/B08 `QFORM-BICOLOOP-NEAR-RANK2-SPECTRAL-GAP-v1`, canonical

`yspennstate/math-open-problems@d5547a484fcc9b62341d80e9ba902cbe2e484284`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260922T201956Z-account03-B08-qform-diffuse-r20/REPORT.md`,

proves in the only unpaid nonzero-pivot branch that the residual physical cross matrix `H` obeys

`s_2(H)>gamma/sqrt(2)`,                                                (1.3)

and the tail after rank two is very small (`||H-H_2||_HS<0.010111 gamma`). The small tail cannot simply be discarded.

## 2. New theorem: physical vertex-cover absorption

Consider independent product banks `U=X_I` and `V=X_J`, with arbitrary additional original coordinates already conditioned. Write the residual quadratic form as

`R(U,V)=F(U)+2 U^T H V+V^T G V+b^T V+c`,                            (2.1)

where `F` is arbitrary measurable (in the QFORM application it is quadratic-affine), `H` is an arbitrary real matrix, and `G` is symmetric.

Let `J=S disjoint_union T`. Write `H_T` for the columns of `H` indexed by `T`, and `G_TT` for the physical principal block of `G` on `T`.

### Theorem 2.1 — `QFORM-PHYSICAL-VERTEX-COVER-CROSS-SMOOTHER-v1`

Assume

`G_TT=0`                                                               (2.2)

and

`s_2(H_T)=sigma>0`.                                                    (2.3)

Then `R` has an essentially bounded density and

`boxed( ||p_R||_infinity <= e sqrt(pi)/sigma. )`                       (2.4)

No bound at all is imposed on `G_SS` or `G_ST`; their entries may be arbitrarily large. There is also no restriction on the self curvature `F` on the `I` bank, on extra singular directions of `H`, on affine terms, or on the supports/moments of the input laws.

#### Proof

Condition on the ORIGINAL physical coordinates `V_S=s`. Because the original coordinates are independent, the remaining bank `V_T` is still an independent product of cap-one one-dimensional densities and remains independent of `U`.

Expanding the conditioned form gives

`R_s(U,V_T)
 = F_s(U)+2 U^T H_T V_T + ell_s^T V_T+c_s`,                           (2.5)

where

`F_s(U)=F(U)+2 U^T H_S s`

absorbs the conditioned cross columns, while

`ell_s = b_T+2 G_TS s`                                                (2.6)

absorbs every cross term between `S` and `T`. The term `s^T G_SS s` is part of the constant. Crucially, (2.2) means there is **no** surviving quadratic self-term on the unconditioned product bank `T`.

Thus (2.5) is exactly the hypothesis of the assigned partner theorem (1.1), uniformly for every conditioning value `s`, and its cross matrix is exactly `H_T`. Hence

`||p_{R_s}||_infinity <= e sqrt(pi)/sigma`                            (2.7)

for almost every `s`. Averaging the conditional densities over `V_S` preserves the same cap and proves (2.4). QED.

### Graph interpretation

Form a physical support graph on the `J` coordinates, with a loop at `j` whenever `G_jj!=0` and an edge `{j,k}` whenever `G_jk!=0`. Condition (2.2) says precisely that `S` is a vertex cover including all looped vertices, so `T` is a physically quadratically independent set. The theorem says: **opposite-side self curvature can be arbitrarily strong if it is covered by physical coordinates whose conditioning leaves two transverse cross directions.** This is an exact support statement, not a coefficient-small perturbation.

Define the support-aware cross currency

`kappa_2(H,G)=max { s_2(H_T) : T subseteq J, G_TT=0 }`.                (2.8)

Then whenever `kappa_2(H,G)>0`,

`boxed( ||p_R||_infinity <= e sqrt(pi)/kappa_2(H,G). )`               (2.9)

This compactly separates the newly paid branch from the genuinely hard case in which every physically self-null surviving bank destroys the second cross singular direction.

## 3. Quantitative deletion criterion

The theorem can be checked without recomputing the entire singular spectrum after conditioning.

### Lemma 3.1 — cross-energy deletion

For `J=S disjoint_union T`,

`s_2(H_T)^2 >= s_2(H)^2-||H_S||_op^2`.                               (3.1)

In particular, if

`||H_S||_op <= theta s_2(H)`, `0<=theta<1`,                            (3.2)

then

`s_2(H_T) >= sqrt(1-theta^2) s_2(H)`.                                 (3.3)

#### Proof

`H H^T=H_S H_S^T+H_T H_T^T`. Hence

`H_T H_T^T=H H^T-H_S H_S^T`.

Weyl's eigenvalue inequality for subtraction of the positive semidefinite matrix `H_S H_S^T` gives

`lambda_2(H_T H_T^T)
 >=lambda_2(H H^T)-lambda_1(H_S H_S^T)
 =s_2(H)^2-||H_S||_op^2`.                                             (3.4)

Taking square roots proves the claim. QED.

Combining Theorem 2.1 and Lemma 3.1, any physical vertex cover `S` of the opposite self-block satisfying (3.2) yields

`boxed(
 ||p_R||_infinity
 <= e sqrt(pi)/[sqrt(1-theta^2) s_2(H)].
)`                                                                         (3.5)

This is a genuinely weighted replacement: the cost is the amount of *cross operator energy actually removed by the physical curvature cover*, not the number of conditioned coordinates and not the largest single minor.

## 4. Splice to the current near-rank-two survivor

Now use the current B08 r20 branch (1.3), where the full QFORM has already been reduced through a genuine outer physical scalar pivot to

`Q=R+aV_R^2`, `a!=0`,                                                 (4.1)

with the dependence-safe conditional density cap required by (1.2). The residual cross matrix obeys

`s_2(H)>gamma/sqrt(2)`.                                                (4.2)

Suppose the opposite self-block `G` has a physical vertex cover `S` such that

`G_TT=0`, `T=J\S`,                                                     (4.3)

and

`||H_S||_op <= theta s_2(H)`, `theta<1`.                              (4.4)

Then by (3.5),

`M:=||p_R||_infinity
 < e sqrt(2 pi)/[sqrt(1-theta^2) gamma].`                              (4.5)

Applying the dependence-safe square smoother (1.2) gives the full post-pivot branch

`boxed(
 ||p_Q||_infinity
 < 2 sqrt(e sqrt(2 pi))
   (1-theta^2)^(-1/4)
   /sqrt(|a| gamma).
)`                                                                         (4.6)

For the concrete robust threshold `theta=1/2`,

`s_2(H_T)>sqrt(3/8) gamma`,                                           (4.7)

`||p_R||_infinity <7.868/gamma`,                                      (4.8)

and

`boxed( ||p_Q||_infinity <5.610/sqrt(|a| gamma). )`                    (4.9)

Thus a broad new piece of the two-sided-curvature survivor is paid: arbitrary-magnitude opposite curvature is harmless whenever its physical support can be conditioned away while losing at most half of the second cross singular direction.

This branch is qualitatively different from the refuted operator-norm-smallness route. Here the curvature itself may be huge; what is small is only the cross energy carried by the coordinates needed to cover its physical support.

## 5. Compact conditional end-to-end argument

The current B06/B08 route can now be stated cleanly.

1. Existing reductions reach the nonzero-pivot near-coloop state with outer square coefficient `a`, transverse scale `gamma`, and residual cross matrix `H`.
2. The aggregate-curvature branch of account03/B06 r18 is already paid.
3. The remaining B08 r20 branch has `s_2(H)>gamma/sqrt(2)` and a tiny higher-rank tail, while exact rank two is already paid by the exact-rank-two `L^3` plus square theorem.
4. If one opposite bank is exactly self-null, account02/B06 closes it.
5. **New:** more generally, if the opposite self-block admits a physical vertex cover `S` with `G_TT=0` and `||H_S||_op<=theta s_2(H)`, Theorem 2.1 plus Lemma 3.1 and the outer-square theorem close the branch by (4.6). At `theta=1/2`, the explicit full bound is (4.9).
6. Therefore the surviving debt is narrower: every physical set `T` on which the opposite self-block vanishes must have `s_2(H_T)` small. Equivalently, every physical cover of the self-curvature support must capture a large fraction of the second cross direction. This is a simultaneous **self-curvature-support / cross-leverage obstruction**, not merely a small spectral tail.

## 6. First unpaid implication

`QFORM-SUPPORT-CROSS-ENTANGLEMENT-DICHOTOMY-v1`:

In the r20 near-rank-two survivor, assume every physical quadratically independent set `T` satisfies

`s_2(H_T)<c s_2(H)`                                                     (6.1)

for a fixed `c<1` (for example `c=sqrt(3)/2`, corresponding to failure of the `theta=1/2` branch). Use the factorized exterior bank and/or the tiny `h_3/h_2<0.0143` tail to prove one of:

- a physical self-curvature pair/triple with enough determinant to invoke an already-paid physical-pair/triple theorem;
- a second grouped cross smoother that retains the original product banks;
- a dependence-safe fractional `L^p` estimate before any reciprocal minor selection; or
- a new exact structural contradiction.

Do not replace (6.1) by coefficient smallness of `G`; the partner's source-valid perturbation falsifier rules that out. Do not condition on spectral coordinates.

## 7. Outcome

`QFORM-PHYSICAL-VERTEX-COVER-CROSS-SMOOTHER-v1`: PROVED.

`QFORM-OUTER-SQUARE-VERTEX-COVER-v1` / inequality (4.6): PROVED as a direct splice to the current post-pivot state.

A concrete `theta=1/2` near-rank-two branch is closed with `<5.610/sqrt(|a| gamma)`.

Full arbitrary-dimensional QFORM: OPEN / NOT PROVED / NOT DISPROVED.

Continuity for this branch: NOT PROVED; only absolute continuity with an essential `L^infinity` bound is established.

No source-matching published theorem was identified in this run; the web search only surfaced broad oscillatory/sublevel literature and was not used as a premise.

MODEL: GPT-5.6 Sol (self report). Configured thinking level and provider reasoning-token/time counters: UNKNOWN / NOT_EXPOSED.
