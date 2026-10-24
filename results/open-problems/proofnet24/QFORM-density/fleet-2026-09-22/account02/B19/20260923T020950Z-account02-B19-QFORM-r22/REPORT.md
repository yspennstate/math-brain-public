SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T02:09:50Z.
attacking: the first unpaid O3 two-internal-rank-two routing gate by combining the newest Claude Fresnel theorem with the designated partner's grouped 2+1 payment at its actual scale.

# account02/B19 r22 — two-rank-two transverse routing

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Outcome:** `ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING BRANCHES / FULL TARGET OPEN`  
**Continuity:** not asserted globally  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and source-pinned proof graph

The target remains: for every finite `n`, every independent real vector `X=(X_i)` whose coordinate densities satisfy `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `X^TAX` has an essentially bounded density with one universal finite cap, or give a target-valid counterexample. There are no moment, support, log-concavity, identical-law, diagonal-basis, or post-rotation-independence assumptions.

The current noncircular top-level graph is:

1. `math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`, `20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`, proves that for any fixed `tau in (0,1]`, the single strict no-pivot statement `N3(tau,C0)` implies the unrestricted theorem. `N3` asks for a universal density cap on every matrix with three actual eigenvalues of modulus at least one, all `|A_ii|<tau`, and all physical `2x2` principal determinants of magnitude `<tau`. The Gaussian padding in that source also supplies the required affine extension without adding assumptions on the original law. `N3` itself remains open.

2. Claude's completed volume-sampling/Fourier route at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially `RESULTS.md` and `FOURIER_ROUTE_REPORT.md`, pays any original-coordinate cross block with enough third volume and admissible row marginals; its `D'` version allows third-volume row marginals `<3/4`, and its `D5` version pays nonzero fifth-volume with no marginal gate. The same source's Theorem F pays an exact three-dimensional spectral packet when its physical row leverages are at most `1/2`.

3. The newer stability package `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `20260923T002323Z-volume-stability/REPORT.md` and `PEER_TAIL_EXTENSION.md`, pays a nearby diffuse rank-at-least-three cross block and also the two-large-singular-directions plus collective-tail regime under its explicit projection gate. Small total tail and high-leverage/hub states remain open there.

4. The designated partner account03/B19 r21 at `math-open-problems@4b6025f5928ab6a35f3637965dd4639768c76087` proves `QFORM-O3-ROBUST-2PLUS1-GROUPED-PAYMENT-v1`: an exact-rank-three O3 state with one rank-one original-product source bank and one robust rank-two source bank, grouped volume `det(L)^2>1/6`, has density `<362`. It identifies the next exact-rank-three O3 chamber as the state with at least two internal rank-two source banks. This report attacks exactly that chamber.

5. The cross-transverse smoothing theorem used below is `math-open-problems@8d262d18e5581cd02b8ea8be5102aa2a6d30ddd7`, account01/B16, and the orientation-free rank-two affine half-Riesz theorem is `math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`. Both retain the required original-product provenance.

No item above is promoted beyond its source scope. In particular, arbitrary-joint rank-three coarea, law-uniform pointwise Fresnel decay, worst conditional projection caps, post-rotation independence, perturbative deletion of a small quadratic matrix, and existence of one universally good physical minor remain unavailable.

## 2. Exact-rank-three two-bank setup

Write an exact-rank-three target core as

`A=R M R^T`, `R^TR=I_3`, `M=M^T`, `s_min(M)>=1`.                 (2.1)

For each original coordinate put `u_i=R^Te_i in R^3`, so

`sum_i u_i u_i^T=I_3`.                                           (2.2)

Let `G,H` be disjoint original-coordinate banks and put

`S_G=sum_(i in G)u_i u_i^T`, `S_H=sum_(i in H)u_i u_i^T`.        (2.3)

Assume both have rank two. Let `g,h>0` be their least positive eigenvalues and let `n_G,n_H` be unit kernel normals. Set

`eta=1-(n_G^Tn_H)^2`.                                            (2.4)

The source banks remain genuinely independent because `G,H` are sets of original coordinates. The vectors `u_i` and the kernels below are only deterministic spectral algebra.

## 3. Two internally diffuse rank-two banks are already a full three-dimensional Fresnel packet

### Lemma 3.1 — combined leverage monotonicity

If `u in range(S_G)` and `S=S_G+S_H` is positive definite, then

`u^T S^{-1}u <= u^T S_G^+u`.                                    (3.1)

Indeed the pseudoinverse quadratic form has the variational representation

`u^T S_G^+u = sup_x {2u^Tx-x^TS_Gx}`                             (3.2)

for `u in range(S_G)`. Since `S>=S_G`, replacing `S_G` by `S` can only decrease the supremum, proving (3.1). The same statement holds with `G,H` exchanged.

### Lemma 3.2 — exact determinant of two rank-two planes

Since

`S_G>=g(I-n_Gn_G^T)`, `S_H>=h(I-n_Hn_H^T)`,                     (3.3)

we have, for `eta>0`,

`det(S_G+S_H) >= (g+h)gh eta`.                                  (3.4)

Proof: the lower matrix in (3.3) is positive definite when the normals are not parallel. In the common-line direction of the two planes its eigenvalue is `g+h`; on the orthogonal two-plane its determinant is `gh sin^2(theta)=gh eta`. Thus

`det(g(I-n_Gn_G^T)+h(I-n_Hn_H^T))=(g+h)gh eta`.                 (3.5)

Determinant is monotone under Loewner order on positive definite matrices, giving (3.4).

### Theorem 3.3 — `QFORM-O3-TWO-RANK2-TRANSVERSE-DIFFUSE-v1`

Assume in addition that each bank is internally diffuse:

`u_i^T S_G^+u_i <=1/2` for every `i in G`,                      (3.6)

`u_i^T S_H^+u_i <=1/2` for every `i in H`.                      (3.7)

Then for every admissible cap-one product input law, after conditioning on all original coordinates outside `G union H`, the conditional and hence unconditional output density satisfies

`||p_Q||_infinity
 <=12[|det M| det(S_G+S_H)]^(-1/3)
 <=12[(g+h)gh eta]^(-1/3)`.                                    (3.8)

**Proof.** Put `S=S_G+S_H`. By `eta>0`, `S` is positive definite. Lemma 3.1 and (3.6)-(3.7) show that every active physical row has combined leverage

`u_i^TS^{-1}u_i<=1/2`.                                          (3.9)

Diagonalize only the deterministic spectral matrix `M=O Lambda O^T`. The active quadratic block is then the sum of three deterministic squares with coefficients `lambda_1,lambda_2,lambda_3`; no random coordinate is rotated. In Claude's Theorem F take its remainder `B=0` and physical set `I=G union H`. Its Gram is `O^TSO`, so its determinant is `det S` and its normalized row leverages are exactly (3.9). Theorem F therefore gives the first inequality in (3.8), uniformly in every affine term produced by the conditioned outside coordinates. Since `|det M|>=1`, Lemma 3.2 gives the second inequality. Averaging the conditional interval bound finishes the proof. QED.

For the concrete robust thresholds

`g,h>=1/3`, `eta>=1/4`,                                         (3.10)

(3.8) becomes

`||p_Q||_infinity <=12*54^(1/3)=45.3571578...<45.358`.          (3.11)

This is an equation-level application of the required newest Claude result to the designated partner's first unpaid two-rank-two chamber.

## 4. A single transverse physical row plus one rank-two bank is payable at its true scale

The preceding theorem leaves internally heavy banks. The designated partner r21 can be rescaled to give a second exact exit which does not require an entire companion bank to be rank one.

Fix a rank-two bank `G`. Choose a `3x2` matrix `W` of rank two with

`WW^T=S_G`.                                                       (4.1)

Let `i notin G` be one original physical coordinate and define

`L_i=[u_i,W]`, `delta_i=det(L_i)^2`.                             (4.2)

Because the source rows in `{i} union G` form only part of the Parseval frame (2.2),

`L_iL_i^T=u_i u_i^T+S_G <=I`.                                  (4.3)

Thus every singular value of `L_i` is at most one. If `delta_i>0`, their product is `sqrt(delta_i)`, so

`s_min(L_i)>=sqrt(delta_i)`.                                    (4.4)

Set

`B_i=L_i^T M L_i`.                                               (4.5)

Then

`s_min(B_i)>=delta_i`,                                          (4.6)

`D_i:=|det B_i|=|det M|delta_i>=delta_i`.                        (4.7)

### Product provenance

Let `R_G` be the matrix of rows `u_j^T`, `j in G`. As in the partner's r21 physicalization, one may choose `U` with orthonormal columns such that

`R_G^T=WU^T`.                                                     (4.8)

Hence the entire contribution of the original product source `X_G` to spectral space is `WZ`, with

`Z=U^T X_G`.                                                      (4.9)

The two-dimensional marginal-density theorem used in the current source map gives

`||p_Z||_infinity<=2`.                                          (4.10)

The scalar `X_i` remains genuinely independent of `Z`. Conditioning outside `{i} union G` contributes only deterministic affine terms in `(X_i,Z)`.

### Theorem 4.1 — `QFORM-PHYSICALROW-RANK2-GROUPED-SCALE-v1`

For `0<delta_i<=1`,

`boxed: ||p_Q||_infinity <105 delta_i^(-1/2).`                  (4.11)

**Proof.** Write the active symmetric matrix relative to the scalar/receiver split as

`B_i=[[a,b^T],[b,C]]`, and let `s=s_min(B_i)`, `D=D_i`.          (4.12)

By (4.6)-(4.7), `s,D>=delta_i`.

If `|a|<=delta_i/2<=s/2`, the partner r21 scaled near-null Schur identity gives, after rotating only the already-joint receiver plane,

`P=||b||^2 |e| >=D/2`,                                          (4.13)

where `e` is the transverse receiver coefficient. Apply `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1` with the genuine independent scalar and (4.10):

`||p_Q||_infinity
 <=103680^(1/3) 2^(2/3)(DP)^(-1/6)
 <=103680^(1/3)2^(5/6)delta_i^(-1/3)
 <83.707 delta_i^(-1/3).`                                       (4.14)

If instead `|a|>delta_i/2`, complete the square only in the original scalar `X_i`. The scalar square pushforward gives

`p_Q(t)<=|a|^(-1/2)
 sup_w E|Z^TSZ+ell^TZ-w|^(-1/2)`,                               (4.15)

where `S=C-bb^T/a` and

`|det S|=D/|a|`.                                                 (4.16)

The affine term lies in the same two-dimensional projection range. The sharp in-range version of `QFORM-RANK2-AFFINE-HALF-RIESZ-v1` therefore gives

`||p_Q||_infinity
 <=16sqrt(30)|a|^(-1/4)D^(-1/4)
 <=16sqrt(30)2^(1/4)delta_i^(-1/2)
 =104.21689... delta_i^(-1/2).`                                 (4.17)

Since `delta_i<=1`, (4.17) dominates (4.14), proving (4.11). QED.

This is the designated partner r21 mechanism applied at equation level to a strictly larger physical configuration: a **single original coordinate** transverse to a rank-two source bank, with its actual grouped volume retained rather than rounded to the partner's fixed `1/6` threshold.

## 5. Exact aggregate packet left when no single transverse row is large

Let `n_G` be the unit kernel normal of `S_G`. The grouped determinant in (4.2) has the exact identity

`delta_i=pdet(S_G)(n_G^Tu_i)^2`.                                (5.1)

Indeed `det(L_i)^2=det(W^TW)` times the squared normal component of `u_i`, and `det(W^TW)=pdet(S_G)`.

Summing (5.1) over the opposite bank `H`,

`sum_(i in H)delta_i
 =pdet(S_G)n_G^TS_Hn_G
 >=g^2 h eta`.                                                    (5.2)

The last inequality uses `pdet(S_G)>=g^2` and `S_H>=h(I-n_Hn_H^T)`. Symmetrically,

`sum_(i in G)det([u_i,W_H])^2 >= h^2 g eta`.                    (5.3)

Thus the two-rank-two obstruction cannot lose its transverse three-volume; it can only **spread** that volume among many individually weak physical rows.

For example under (3.10), each side has aggregate grouped determinant mass at least

`1/108`.                                                         (5.4)

If some individual `delta_i>=1/576`, Theorem 4.1 gives

`||p_Q||_infinity<105 sqrt(576)=2520`.                           (5.5)

If no individual `delta_i` reaches `1/576`, (5.4) forces at least six positive physical-row contributors on that side. This last statement is structural currency only; it is **not** converted here into a reciprocal-minor bound.

## 6. What this closes and the exact first unpaid implication

The partner's first two-internal-rank-two O3 debt now has two source-valid exits:

- if both rank-two banks are internally diffuse and their positive eigenvalues / kernel angle have fixed quantitative lower bounds, Theorem 3.3 pays the whole two-bank state directly by the newest Claude Fresnel theorem;
- if one physical row from one source bank has fixed grouped determinant against the opposite rank-two bank, Theorem 4.1 pays it directly, uniformly over all remaining conditioned coordinates and affine terms.

Therefore a surviving robust/transverse two-rank-two state must simultaneously have an internally heavy bank **and** have its cross-transverse grouped determinant currency spread over many individually small physical rows. The exact quantitative residual can be stated as follows.

### `QFORM-O3-TWO-RANK2-COHEAVY-AGGREGATE-ROUTING-v1` — OPEN

Prove that there exists a universal `c>0` such that every exact-rank-three O3 state with two disjoint rank-two source banks `G,H` which survives all previously paid O3 exits and satisfies

`g,h>=c`, `eta>=c`                                                (6.1)

must satisfy at least one of:

1. both internal leverage maxima are at most `1/2` (paid by Theorem 3.3);
2. some physical row has grouped determinant `delta_i>=c` against the opposite rank-two bank (paid by Theorem 4.1);
3. the state quantitatively descends to an already-paid rank-one-companion `2+1`, diffuse-ridge, physical-pivot, D'/D5 cross-volume, or generated-span branch.

If this implication is false, the counterexample must exhibit fixed robust bank eigenvalues and fixed transverse kernel angle, at least one internal leverage `>1/2`, yet all individual grouped determinants tending to zero while the aggregate identities (5.2)-(5.3) stay bounded below. Such a family would isolate a genuine **co-heavy / diffuse-transverse aggregation** mechanism rather than the already-refuted single-good-minor route.

Separate from (6.1), the weak-bank limit `min(g,h)->0`, the near-parallel-kernel limit `eta->0`, and the splice from exact rank three to arbitrary additional spectrum remain explicit structural debts. The newer volume-stability/tail theorem pays some higher-rank perturbative/cross-tail instances but does not make that splice automatic.

## 7. Full-target status

The full conjecture remains `OPEN / NOT PROVED / NOT DISPROVED`. The single top-level gate remains `N3(tau,C0)` from the source synthesis. This report removes a genuine subbranch inside the O3 route but does not prove that every N3 matrix enters O3, nor that every O3 state enters one of the now-paid subbranches. It also does not provide the required two independent end-to-end reviews. No continuous-density claim is inferred for branches whose source theorem supplies only essential boundedness.

The correction boundary is unchanged: no post-rotation independence, arbitrary-joint coarea, pointwise law-uniform phase decay, worst-fiber/conditional-density supremum, single uniformly good physical minor, or small-random-error perturbation is used.
