Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — the requested GPT-6/maximum setting is not authenticated by any exposed scheduler/model selector.**

# PROB10-09 — Cheeger transfer through Cayley covers removes the visible-free-subset hypothesis

Status: **PARTIAL for the Benjamini–Schramm source problem.** This run proves a complete quotient-cover criterion for iid **bond** percolation that replaces the preceding R20 theorem's visible free subgroup on the `p_c` side by edge expansion. It then derives an exact finite-degree pure spectral sufficient condition, strictly stronger than the classical `rho<1/2` spectral-radius criterion. The universal all-Cayley conjecture remains open. The proof has an executed exact-algebra self-check but **no independent other-track validation**, so source closure is not claimed.

## 0. Frozen source, R20 handoff, consumed history, aliases, and ownership

The frozen source is exactly

> For every locally finite Cayley graph `G` of every finitely generated nonamenable group, iid **BOND** percolation satisfies `p_c(G)<p_u(G)`.

No nontransitive planar SITE-percolation problem is substituted. Known nonamenable Gromov-hyperbolic quasi-transitive cases are prior art, not new results.

The required owner-refocus handoff was re-read at

`runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md`,

blob `6e1b9e54cbc01461d32b523854c3bd82e50bfd04`. Its actual predecessor state is preserved:

- **I0100 / Paley one-localization:** OPEN/PARTIAL, exact frozen metric `p_max=1213`; retain all `artifacts/R20/i0100_*` primal/dual discovery, Jacobi and certificate artifacts.
- **KNSV-2026-LOOPY-U:** OPEN/PARTIAL; retain `knsv_next_routes_check.*`, `knsv_two_terminal_n12_check.*`, `knsv_seven_vertex_dual_check.*`, `knsv_loopy_rooted_gadget_check.*`, `knsv_one_cross_edge_quotient_exact.*`, `knsv_transfer_signature_iso_n12_check.*`, and the dated KNSV idea notes.
- **BMO-2025-PUSHING-DELTA:** this was the last actual mathematical R20 target before terminal waiting; OPEN/PARTIAL with exact `n_all=9`, retaining `artifacts/R20/bmo_n9_witness_exact.cpp`, `artifacts/R20/bmo_n9_exact_check.out` and the surrounding BMO DP/modular-lifting artifacts. Its six-run handoff remains `runs/R20/2026-09-19T06-47-48Z_bmo_sixrun_handoff_deficit_sum_d4a8c2.md`.
- The terminal predecessor wait state remains `runs/R20/2026-09-19T22-59-30Z_terminal_wait_eight_claim_delta_hard_releases_no_free_5a7c31.md`. No predecessor canonical claim is edited here.

The current source alias remains

`D0061 = lyons_nonamenable_2000::conjecture_3.8_(benjamini-schramm_1996)`,

still catalogued HARD/open rather than as a closed canonical theorem.

Consumed current evidence before the new proof:

- current `operations/PROB10_2026-09-20.md`, re-read after the mathematical work to check for later owner/platform stops;
- current `POSTED.md`; the unrestricted target is not posted as closed;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/open_status.md`, blob `ee8bde8735e84ff75d3a625fed61e9bafbefd64f`;
- `probability_campaign_2026_09/benjamini_schramm_attempt_2026_06/research/proof_strategy.md`, blob `d94127841f3b335a32b7936b86d8dee7a6b8d093`;
- June `notes/round_011.md`, blob `e4b38be74ddddaa15b36aa564d31cf338f3fa4e9` (global nonbacktracking polynomial bound);
- June `notes/round_018.md`, blob `e171f9c1a80a24ca6cb8a67ce9fd563763029221` (fibre-cluster branching and low-branching obstruction);
- June `notes/round_040.md`, blob `e2de09e883e9082440e370e4cf67bd782f1e145f` (fixed-direction exponent / line-factor operator argument);
- June `notes/round_042.md`, blob `82caa389484574736ab38f75df5f41687449ea2d` (Hutchcroft–Pan prior-art correction and quotient/height abstraction agenda);
- June `notes/round_053.md`, blob `bdad4bb3aa58303dd35a7dab4c1e42d9d597245b` (fixed-endpoint NB excess criterion);
- June `notes/round_054.md`, blob `43d7d8aee783aba9fdf019d76669855483a9aea4` (weighted detour generating function);
- June `notes/round_055.md`, blob `8a06a66baca79d2fbb9dc934269e8a850b094fc1` (NB bridge-probability criterion);
- immediate R20 predecessor `runs/prob10_2026-09-20/PROB10-09/2026-09-20T11-59-30Z_arbitrary_extension_cover_lift_gap_8c4e17.md`, blob `c531f95f6ffb72f74fddcde3e0a494f5a00c4bbc`;
- newest neighboring T09 report located before delivery, `proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T14-50-30+0300__t09-dependent-free-layers-rattaggi-gap.md`, blob `9db299ec981e595afa707271aff63d48a4ddec3f`.

The older June normalized finite-set escape, BK/last-exit decomposition, killed-SAW, susceptibility/boundary-energy, global `ell^2` SAW-growth, product stress tests, quotient/fibre-shell comparisons and fixed-endpoint bridge routes remain consumed history; none is renamed as new.

**Collision boundary.** NM13-11/T09 currently owns the distinct free-core / higher-rank-lattice / Rattaggi product-of-trees / triangle-fibre / power-layer / factor-branching lane. Its newest theorem concerns relation-bearing generator layers on the Rattaggi lattice. R20 stays on the **quotient-cover / extension-operator** lane and does not edit, absorb or duplicate that claim.

No schedule, cadence, enabled state, email, Drive, public posting, `POSTED.md`, canonical claim or neighboring ownership state is changed.

## 1. Current source screen and what is prior art

The following distinctions were refreshed on 20 September 2026.

1. Hutchcroft, `https://arxiv.org/abs/1804.10191`, proves `p_c<p_u` for nonamenable Gromov-hyperbolic quasi-transitive graphs. This is a proper known subclass.
2. Hutchcroft, `https://arxiv.org/abs/1904.05804`, develops `p_{2->2}` and the `L^2` boundedness program; `p_c<p_{2->2}` implies the desired nonuniqueness phase.
3. Hutchcroft–Pan, `https://arxiv.org/abs/2409.12283`, prove subgroup-relativized uniqueness-threshold statements; they do not settle the frozen all-Cayley statement.
4. Terlov–Timár, `https://arxiv.org/abs/2502.02560`, treat weighted amenability/heavy-cluster thresholds, not the frozen universal fixed-Cayley theorem.
5. Choi–Seo, `https://arxiv.org/abs/2508.08932`, prove a nonuniqueness phase on every Cayley graph of every acylindrically hyperbolic group, again a proper group class.
6. Chatterjee–Chen–Terlov, `https://arxiv.org/abs/2609.11845`, submitted 10 September 2026, still discusses the classical Benjamini–Schramm nonamenability/nonuniqueness question in its current percolation background; this is fresh status evidence, not a worldwide-priority certificate.
7. Juschenko–Nagnibeda, `https://arxiv.org/abs/1206.2183` (Proc. AMS 2015), explicitly quote the Benjamini–Schramm estimate

   `p_c <= 1/(phi_E+1)`,

   define normalized spectral radius `rho=||A||/D`, quote the Mohar/Dodziuk estimate

   `h=phi_E/D >= D(1-rho)/(D-1)`,

   and record the classical sufficient condition `rho<1/2 => p_c<p_u`. They also prove existence of good generating sets for broad group classes, including free Burnside groups. These are prior art and are used below as inputs/benchmarks.

A bounded search did **not** locate the exact cover-Cheeger/nonbacktracking criterion or the finite-degree threshold derived below. This is negative search evidence only. **No novelty or publication-priority claim is made.**

## 2. Metrics — parent source, structural scope, frozen check, and auxiliary delta

### Parent source metric

Before: **OPEN/PARTIAL**.

After: **OPEN/PARTIAL**.

The all-nonamenable-group/all-Cayley theorem is not proved.

### Structural-scope metric

Before: the arbitrary-extension theorem in the immediate predecessor allowed an arbitrary kernel but required that the quotient generating set visibly contain `k` generator pairs freely generating `F_k`, with

`beta_D(r_Q)<2k-1`.

After: **no free subgroup or free marked subset is required.** For every connected horizontal Cayley cover `X -> Q`, it is enough that

`boxed(beta_D(r_Q) < 1 + phi_E(Q))`,

where `r_Q=||A_Q||`. This is the complete scope of the proved criterion in this run.

### Pure spectral auxiliary criterion

For `D>=5`, the preceding condition is guaranteed by

`rho_Q < theta_D`,

where `rho_Q=r_Q/D` and

`boxed(theta_D=(D^3+3D^2-4D+1)/(D^2(2D-1))).`

The threshold strictly exceeds `1/2` by

`theta_D-1/2=(7D^2-8D+2)/(2D^2(2D-1))>0`.

For `D=3,4`, the exact lower-branch thresholds are respectively

`rho_Q < (11-2 sqrt(2))/9`,

`rho_Q < (19-3 sqrt(3))/16`.

The `D>=5` threshold also strictly improves the threshold obtained by combining the **classical** Benjamini–Schramm two-point condition `r p_c<1` with the same Mohar expansion estimate. That older-combination threshold is

`rho_BS(D)=(D^2+D-1)/(D(2D-1))`,

and the exact auxiliary gain is

`boxed(theta_D-rho_BS(D)=(D-1)/D^2).`

This comparison is an auxiliary mechanism metric, not a claim that the formula has never appeared elsewhere.

### Frozen auxiliary graph

For the genus-three noncentral semidirect horizontal lift in Section 7, the new spectral-Cheeger route alone certifies

`p_u-p_c > 7/100`.

This graph was not separately numerically frozen before this run, but it is already logically subsumed by the preceding visible-free-subset theorem. Therefore **the 7/100 value is a method-validation metric, not a new source-family novelty claim.**

## 3. Idea-before-code, negation test, and genuinely different routes

The mathematical idea was persisted before any new checker at

`artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T12-52-00Z_spectral_cheeger_cover_idea.md`,

creation commit `5560753e127f3d4434bbaf8252e7aec731191624`.

The routes compared were:

1. **Cover coarea + nonbacktracking operator — SUCCESS.** Transfer edge expansion from the quotient to every finite set in the cover by fibre-count coarea; combine it with the already proved Hilbert-fibre adjacency domination and NB polynomial bound. This removes visible freeness entirely.
2. **Direct percolation coupling from quotient to cover — REJECTED.** A quotient open path does not canonically give a coherent open lifted path from a fixed fibre vertex: projection merges distinct lift endpoints, and ordinary edge monotonicity does not compare `p_c` across a nontrivial cover in the needed direction. The deterministic expansion transfer is the correct substitute.
3. **Fixed-endpoint NB bridge large deviations — NOT USED THIS RUN.** June rounds 053–055 reduce the source to a strong endpoint bridge estimate, but the cover structure by itself supplies no critical bridge large-deviation estimate. Re-entering that route without a new endpoint estimate would only restate the old obstruction.
4. **Classical Benjamini–Schramm spectral criterion — BENCHMARK.** Combining their `r p_c<1` criterion with the same Mohar estimate is rigorous but gives the strictly weaker threshold `rho_BS(D)` above. The NB `p_{2->2}` endpoint is quantitatively responsible for the exact gain `(D-1)/D^2` when `D>=5`.

A useful negation test caught a real algebraic pitfall: the anticipated rational root `r_*(D)` is **extraneous for `D=3,4`** after squaring the NB radical, because `2L_D(r_*)-r_*<0`. The final theorem therefore uses separate exact lower-branch thresholds in degrees three and four. This correction was made before the substantive report was written.

## 4. Cover expansion lemma

Let `Y=Cay(Q,S_Q)` be a simple connected `D`-regular Cayley graph with finite symmetric generating set `S_Q`. Let

`pi: Gamma -> Q`

be a surjection. Choose one inverse-compatible lift of every generator so that the resulting symmetric set `S_tilde` generates `Gamma`; equivalently,

`X=Cay(Gamma,S_tilde) -> Y`

is a connected label-preserving `D`-regular graph covering. If an involutive quotient generator occurs, its chosen lift is assumed involutive so that this is genuinely a degree-`D` cover.

Write

`phi_E(G)=inf_{empty != K finite} |partial_E K|/|K|`.

**Lemma 4.1 (edge expansion cannot decrease under the horizontal cover).**

`boxed(phi_E(X) >= phi_E(Y).)`

### Proof

Fix finite `K subset V(X)`. For each `q in Q`, let

`f(q)=|K cap pi^{-1}(q)|`.

This is a finitely supported nonnegative integer-valued function and

`sum_q f(q)=|K|`.

Fix one undirected edge `e={q,q'}` of `Y`. The lift of `e` is a perfect matching between the fibres over `q` and `q'`. If `A` and `B` are the subsets of those fibres selected by `K`, the number of matching edges crossing `K` is

`|A Delta U^{-1}B| >= ||A|-|B|| = |f(q)-f(q')|`.

Summing over undirected base edges gives

`|partial_E^X K| >= sum_{qq' in E(Y)} |f(q)-f(q')|`.

For integer-valued `f`, the discrete coarea identity is exact:

`sum_{qq'} |f(q)-f(q')| = sum_{m>=1} |partial_E^Y {q:f(q)>=m}|`.

Every nonempty level set is finite, hence

`sum_{m>=1} |partial_E^Y {f>=m}| >= phi_E(Y) sum_{m>=1}|{f>=m}| = phi_E(Y) sum_q f(q)`.

Therefore

`|partial_E^X K| >= phi_E(Y)|K|`.

Taking the infimum over finite nonempty `K` proves the lemma. `QED`

This is a deterministic statement about the cover; no percolation coupling is asserted.

## 5. Two-point/nonbacktracking cover criterion

Let

`r_Y=||A_Y||_{2->2}`.

The preceding R20 Hilbert-fibre argument applies verbatim to this cover and gives

`boxed(||A_X||_{2->2} <= r_Y).`                                      (5.1)

Indeed, after identifying `ell^2(X)` with `ell^2(Y;H)` for one fibre Hilbert space `H`, each lifted generator transports fibres unitarily. For `F(y)=||f(y)||_H`, fibrewise triangle inequality gives

`||(A_X f)(y)||_H <= (A_Y F)(y)`,

and hence `||A_X||<=||A_Y||`.

For a `D`-regular graph set `q=D-1` and

`beta_D(r)=sqrt(q)` if `r<=2sqrt(q)`,

`beta_D(r)=(r+sqrt(r^2-4q))/2` if `r>2sqrt(q)`.

June round 011 proves from the nonbacktracking recurrence that

`limsup_n ||N_n||^(1/n) <= beta_D(||A||)`.

Every open connection has a shortest open path and every shortest path is nonbacktracking, so the weighted NB series gives

`boxed(p_{2->2}(X) >= 1/beta_D(||A_X||) >= 1/beta_D(r_Y)).`          (5.2)

The standard transitive inequality gives `p_{2->2}(X)<=p_u(X)`.

On the critical side, Benjamini–Schramm's edge-isoperimetric estimate and Lemma 4.1 give

`p_c(X) <= 1/(1+phi_E(X)) <= 1/(1+phi_E(Y)).`                        (5.3)

Combining (5.2)–(5.3) proves the main structural theorem.

**Theorem 5.1 (Cheeger/nonbacktracking horizontal-cover criterion).** If

`boxed(beta_D(r_Y) < 1+phi_E(Y),)`                                   (5.4)

then

`boxed(p_c(X) <= 1/(1+phi_E(Y)) < 1/beta_D(r_Y) <= p_{2->2}(X) <= p_u(X).)`

In particular `p_c(X)<p_u(X)`.

No free subgroup, free generator pair, central kernel, abelian kernel, amenable kernel, cocycle assumption or surface-group structure appears in the theorem.

## 6. Exact pure spectral corollary

Juschenko–Nagnibeda use normalized spectral radius

`rho_Y=r_Y/D`

and normalized conductance `h=phi_E/D`, and quote

`h >= D(1-rho_Y)/(D-1)`.

Therefore

`phi_E(Y) >= D(D-r_Y)/(D-1)`.                                       (6.1)

Set

`L_D(r)=1+D(D-r)/(D-1)`.

Thus Theorem 5.1 holds whenever

`beta_D(r)<L_D(r)`.                                                   (6.2)

### Degrees `D>=5`

At the NB branch point `r=2sqrt(D-1)`, write `t=sqrt(D-1)>=2`. Exact simplification gives

`L_D(2sqrt(D-1))-sqrt(D-1)`

`=((t-1)(t^3-2t^2+t-1))/t^2 > 0`.

Hence the crossing occurs on the upper NB branch. Solving

`(r+sqrt(r^2-4(D-1)))/2=L_D(r)`

requires retaining the sign of the radical. Squaring factors exactly as

`(2L_D(r)-r)^2-(r^2-4(D-1))`

`=4(r-D)(-D^3+2D^2 r-3D^2-D r+4D-1)/(D-1)^2`.

The nontrivial root is

`r_*(D)=(D^3+3D^2-4D+1)/(D(2D-1)).`                                 (6.3)

At this root

`2L_D(r_*)-r_*=(D^3-5D^2+4D-1)/(D(2D-1))>0`

for every `D>=5`, since the numerator is `(D-5)D^2+4D-1`. The root `r=D` introduced by squaring has the wrong radical sign and is extraneous. Since the upper-branch `beta_D` is increasing and `L_D` is decreasing, (6.2) is equivalent to `r<r_*(D)`.

Thus for `D>=5` it suffices that

`boxed(rho_Y < theta_D := (D^3+3D^2-4D+1)/(D^2(2D-1)).)`             (6.4)

### Degrees three and four

Here the upper-branch rational root has the wrong sign. The actual crossing occurs while `beta_D(r)=sqrt(D-1)`.

For `D=3`,

`r < 11/3-(2/3)sqrt(2)`, equivalently

`boxed(rho_Y < (11-2sqrt(2))/9).`                                    (6.5)

For `D=4`,

`r < 19/4-(3/4)sqrt(3)`, equivalently

`boxed(rho_Y < (19-3sqrt(3))/16).`                                   (6.6)

The exact branch checks are `121<128` and `361<363`, respectively.

### Exact comparison with classical spectral criteria

The older Benjamini–Schramm condition is `r p_c<1`. Combining it with exactly the same lower bound (6.1) gives only

`r < L_D(r)`,

or normalized

`rho_Y < rho_BS(D):=(D^2+D-1)/(D(2D-1)).`                            (6.7)

For every `D>=5`,

`boxed(theta_D-rho_BS(D)=(D-1)/D^2>0).`                              (6.8)

Also

`boxed(theta_D-1/2=(7D^2-8D+2)/(2D^2(2D-1))>0).`                    (6.9)

Thus the NB endpoint gives a strict finite-degree gain over both the familiar `rho<1/2` corollary and this direct classical-BS-plus-Mohar combination.

## 7. Frozen noncentral infinite-kernel calibration

This is a calibration of the new method, not a claim of a new group class.

Let

`Q=Gamma_3=<a_1,b_1,a_2,b_2,a_3,b_3 | [a_1,b_1][a_2,b_2][a_3,b_3]=1>`

with its standard symmetric generating set, so `D=12`. Let

`M=[[0,-1],[1,3]] in SL_2(Z)`

and define `alpha:Q->SL_2(Z)` by `alpha(a_1)=M` and all other standard generators acting trivially. Set

`Gamma=Z^2 semidirect_alpha Q`.

Take `v=(-2,1)`, so

`(M-I)v=e_1`, `M e_1=e_2`.

Choose horizontal lifts

`A_1=(0,a_1)`, `B_1=(v,b_1)`,

and pure lifts `(0,a_i),(0,b_i)` for `i=2,3`, together with all inverses. As in the preceding genus-two construction, the lifted first commutator contributes `(e_1,1)`, conjugation by `A_1` gives `(e_2,1)`, and the quotient generators are present modulo the recovered kernel. Hence the twelve horizontal directions generate all of `Gamma`.

The kernel `Z^2` is genuinely noncentral and the action has infinite image because `M` is hyperbolic. The group surjects onto the nonamenable surface group, and it has an infinite amenable normal subgroup; thus this fixed group is not in the hyperbolic/all-Cayley or acylindrically-hyperbolic/all-Cayley classes used as current baselines.

Żuk's standard surface-group estimate gives normalized quotient spectral radius

`rho_Q <= 1/sqrt(3)`,

or

`r_Q <= 4sqrt(3)`.

For `D=12`,

`theta_12=2113/3312 = 0.63798...`,

while `1/sqrt(3)=0.57735...`, so the pure spectral criterion applies. Notice that the classical benchmark (6.7) is only

`rho_BS(12)=155/276=0.56159...`,

so the same available spectral estimate does **not** pass that older benchmark; the NB improvement is doing real quantitative work here.

At `r_Q=4sqrt(3)`, the Mohar bound gives

`phi_E(Q) >= (144-48sqrt(3))/11`.

Hence

`p_c(X) <= 1/(1+phi_E(Q))`

`=1705/17113 + (528/17113)sqrt(3)`,                                (7.1)

while

`beta_12(4sqrt(3))=1+2sqrt(3)`

and therefore

`p_u(X) >= p_{2->2}(X) >= 1/(1+2sqrt(3))`

`=-1/11+(2/11)sqrt(3)`.                                             (7.2)

Subtracting (7.1) from (7.2),

`p_u-p_c >= -35868/188243 + (28418/188243)sqrt(3)`

`=0.0709371389613...`.

The exact rational certificate

`boxed(p_u-p_c>7/100)`

reduces to

`2,841,800 sqrt(3) > 4,904,501`,

whose squared margin is

`3*(2,841,800)^2-(4,904,501)^2 = 173351660999 > 0`.

Again: the preceding free-subset theorem gives a stronger bound on surface quotients. This example is included because it isolates the **new expansion-only mechanism** and shows that its finite-degree spectral gain can cross a threshold that the classical `r p_c<1` route does not.

## 8. Negation tests and exact obstruction record

1. **Low-degree squaring trap.** The naive formula (6.3) is not valid in degrees `3,4`; the radical sign is wrong. Separate lower-branch thresholds (6.5)–(6.6) are mandatory.
2. **Full horizontal generation remains essential.** If the chosen lifts generate a proper subgroup, the label graph on all of `Gamma` is disconnected and is not the requested connected Cayley graph. The predecessor's exact index-two semidirect example remains the witness; nothing in the coarea proof repairs this admissibility failure.
3. **Nonamenability alone is far weaker.** Kesten gives `rho<1`, whereas `theta_D<1`. The spectral corollary therefore does not collapse the universal conjecture.
4. **Tree calibration.** The stronger Cheeger-form Theorem 5.1 behaves correctly on a `D`-regular tree: `phi_E=D-2`, `beta_D(2sqrt(D-1))=sqrt(D-1)`, and `sqrt(D-1)<D-1` for `D>=3`.
5. **No illicit `p_c` cover monotonicity.** The proof uses the deterministic inequality `phi_E(X)>=phi_E(Y)`, not an unproved assertion such as `p_c(X)<=p_c(Y)`.

## 9. Executed tests and persisted artifacts

Idea-before-code:

- `artifacts/prob10_2026-09-20/PROB10-09/2026-09-20T12-52-00Z_spectral_cheeger_cover_idea.md`
- creation commit `5560753e127f3d4434bbaf8252e7aec731191624`.

Exact checker:

- `artifacts/prob10_2026-09-20/PROB10-09/spectral_cheeger_cover_exact.py`
- creation commit `217c52ac2cf0861899ffb1542fa58d66b82399b9`.

Executed output:

- `artifacts/prob10_2026-09-20/PROB10-09/spectral_cheeger_cover_exact.out`
- creation commit `20ed0f18c297f5a15bbaa912df6854c8f91fdca5`.

Saved verdict:

`ALL_EXACT_CHECKS_PASS`.

The checker verifies the factorization leading to (6.3), the radical-sign quantity, exact gains (6.8)–(6.9), the separate `D=3,4` branch roots, tree calibration, the genus-three radical arithmetic, the exact `7/100` squared margin, and an exact algebraic-number scan for `5<=D<=500`. The finite scan is only a falsification test; the all-`D>=5` theorem is the symbolic proof in Section 6.

## 10. What remains unresolved

The universal source gap remains substantial. The new theorem reduces one broad quotient-cover lane to a base expansion/operator inequality, but an arbitrary Cayley graph need not be presented as a useful nontrivial cover, and even when it is, nonamenability alone does not force

`beta_D(r)<1+phi_E`.

In particular, the full conjecture still needs a mechanism that turns *arbitrary* nonamenability into enough critical-side branching/expansion relative to the two-point NB growth, including groups and generating sets with spectral radius close to one. The June fixed-endpoint bridge program is still a possible route, but it requires a genuinely new endpoint large-deviation estimate; merely writing `p_c<p_{2->2}` as the missing lemma would not be progress.

A next complementary route inside this conjecture would be to seek a **local-to-global lower bound on `phi_E` or on a percolative exploration rate that is sharper than Mohar precisely in the high-`rho` regime**, while preserving the NB `p_{2->2}` endpoint. That is different from NM13-11's subgroup/free-layer lane and from the exhausted June scalar escape inequalities.

## 11. Validation and verdict

- Complete written proof of the cover expansion lemma: **YES, self-check**.
- Complete written proof of the Cheeger/NB cover criterion: **YES, self-check**.
- Exact finite-degree spectral threshold with branch correction: **YES, self-check**.
- Executed algebra checker: **YES, `ALL_EXACT_CHECKS_PASS`**.
- Current bounded source/prior-art screen: **YES**.
- Independent other-track validation: **NO**.
- Worldwide priority certification: **NO**.
- Parent source closure: **NO**.
- Parent Benjamini–Schramm status: **OPEN/PARTIAL**.
- Schedule/email/Drive/public-posting/canonical-claim changes: **NONE**.

The source-level metric is unchanged (`OPEN/PARTIAL -> OPEN/PARTIAL`). The substantive advance is structural: the R20 arbitrary-extension cover mechanism no longer needs any visible free subset; quotient edge expansion plus nonbacktracking `L^2` growth suffices, with an explicit finite-degree pure spectral corollary.