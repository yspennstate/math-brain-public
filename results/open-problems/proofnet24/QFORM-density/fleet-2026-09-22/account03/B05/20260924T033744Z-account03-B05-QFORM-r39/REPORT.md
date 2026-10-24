SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-24T03:37:44Z.
attacking: QFORM-PAIR-ANCHORED-DETSTAR-COAREA-v1 — convert aggregate principal-triple determinant-star mass through one literal pair into a density bound, including the exactly isotropic physical-pair limit.

# account03/B05 r39 — pair-anchored determinant-star coarea

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: quadratic coarea / equivalent interval bound preserving arbitrary original-coordinate product densities  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING EXACT-RANK-THREE THEOREM / TRANSVERSE HEAVY-ROW STAR BRANCH PAID / FULL QFORM OPEN**  
Full-target continuity: **OPEN**. The theorem below proves absolute continuity and an essential density bound; it does not prove a continuous representative.

## 1. Fresh scope and the first missing implication

Fresh owner control was resolved from `yspennstate/math-research-brain` main at start commit `718d1f4c7d3e942886470c5f84a0df388700865a`; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. The live correction ledger was reread. In particular this report does not use arbitrary-joint rank-three coarea, conditional projection caps, independence after rotation, pointwise van-der-Corput decay, a fiber supremum, moments, compact support, connected support, or a perturbative deletion of a small random term.

The immediate own predecessor is

`yspennstate/math-open-problems@f24ae277a541417edf1ee63edcc002fd290ab6e6`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260924T023738Z-account03-B05-QFORM-r38/REPORT.md`.

It proved a determinant-only one-third coarea estimate for every nonsingular symmetric physical pair and its rank-one-environment splice. The newest account01/B05 structural addendum then exposed, in the exact-rank-three heavy-null branch, an aggregate principal-triple currency through a fixed physical pair:

`T_ij = sum_k |det A[{i,j,k}]| = S_i q_j`.

When a residual heavy row is transverse, `q_j>=1/4`, and at target normalization `S_i>=1/2`, hence `T_ij>=1/8`. The apparent obstruction was that the physical pair itself can be exactly isotropic, `det A[{i,j},{i,j}]=0`, so the r38 Schur completion cannot be written directly.

The first essential implication is proved below: **for an exact-rank-three form, the aggregate star `T_ij` itself pays the density, even when that physical pair is exactly singular.** The singular case is obtained by a rank-preserving spectral perturbation plus weak-limit interval domination; no random coefficient is thrown away.

## 2. Main theorem

### Theorem `QFORM-PAIR-ANCHORED-DETSTAR-COAREA-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities bounded by one. Let `A=A^T` have rank exactly three, and allow an arbitrary deterministic affine term `ell^T X+c`. Fix two original coordinates `I={i,j}` and define the pair-anchored principal-triple star

`T_I := sum_(k notin I) |det A[I union {k}]|.`                         (2.1)

If `T_I>0`, then

`Q=X^T A X+ell^T X+c`

is absolutely continuous and

`boxed:
 ||p_Q||_(infinity,ess)
 <= C_star T_I^(-1/3),
 C_star = 24(3+sqrt(2)) 10^(2/3)
        = 491.735145127... .
}`                                                                    (2.2)

No condition is imposed on the sign or determinant of the physical `2x2` pair `A[I,I]`. In particular the estimate remains valid when that pair is exactly singular.

### 2.1 Nonsingular physical pair

First suppose

`B=A[I,I]`

is invertible. Write `J=I^c`, `Y=X_I`, `Z=X_J`, and block-decompose

`A = [[B,F],[F^T,C]].`                                                (2.3)

Since `rank A=3` and `rank B=2`, the Schur complement

`S=C-F^T B^(-1)F`                                                     (2.4)

has rank exactly one. Therefore

`S=sigma v v^T`, `||v||_2=1`, `sigma!=0`.                            (2.5)

Complete the physical pair square, retaining the affine term. With

`h(Z)=B^(-1)(FZ+ell_I/2)`,                                           (2.6)

one has exactly

`Q=(Y+h(Z))^T B(Y+h(Z))+T(Z)`,                                      (2.7)

where

`T(Z)=sigma(v^T Z)^2+b^T Z+c_0`                                     (2.8)

for a deterministic vector `b` and constant `c_0`.

The remaining coordinates `Z` are still literal independent original coordinates with density caps one. The source-valid rank-one affine small-ball lemma from

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`

gives, uniformly in `u in R` and `rho>0`,

`P(|T-u|<rho) <= min(1, 10 sqrt(rho/|sigma|)).`                      (2.9)

Now apply the signature-free environment splice from r38 to the literal independent pair `Y=(X_i,X_j)`. Its two density caps are exactly one, and `D=|det B|`. Thus

`||p_Q||_(infinity,ess)
 <= 3 C_H D^(-1/3) [10/sqrt(|sigma|)]^(2/3),`                        (2.10)

where

`C_H=8(3+sqrt(2)).`                                                   (2.11)

It remains to identify the geometric quantity in (2.10) with the aggregate star (2.1), without selecting one small triple.

For each `k in J`, let `f_k` be the `k`th column of `F`. The principal `3x3` block on `I union {k}` has determinant

`det A[I union {k}]
 = det B [C_kk-f_k^T B^(-1) f_k]
 = det B S_kk
 = det B sigma v_k^2.`                                                (2.12)

Therefore

`boxed:
 T_I=|det B| |sigma| sum_k v_k^2
    =D |sigma|.
}`                                                                    (2.13)

Substituting (2.13) into (2.10) proves

`||p_Q||_(infinity,ess)
 <= 3 C_H 10^(2/3) T_I^(-1/3)
 = C_star T_I^(-1/3).`                                               (2.14)

This proof uses the whole determinant star before inversion. No individual principal triple is chosen.

### 2.2 Exactly singular physical pair by a rank-preserving limit

Assume now `T_I>0` but `B=A[I,I]` is singular. Because `rank A=3`, choose an exact spectral representation

`A=V Lambda V^T`, `V^T V=I_3`,                                      (2.15)

with invertible symmetric `Lambda`. Let `W=V_I` be the `2x3` matrix formed by the two selected physical rows.

For every triple `S` of physical coordinates,

`det A[S,S]=det(Lambda) det(V_S)^2.`                                 (2.16)

Exterior Cauchy-Binet gives

`sum_(k notin I) det(V_(I union {k}))^2
 = det(W W^T).`                                                       (2.17)

Hence

`boxed:
 T_I=|det Lambda| det(W W^T).
}`                                                                    (2.18)

Since `T_I>0`, `W` has row rank two, so `G=W W^T` is positive definite.

For real `epsilon` put

`Lambda_epsilon=Lambda+epsilon I_3`,
`A_epsilon=V Lambda_epsilon V^T.`                                    (2.19)

For all sufficiently small `epsilon` outside a finite exceptional set, `Lambda_epsilon` is invertible and the physical pair

`B_epsilon=W Lambda_epsilon W^T=B+epsilon G`                         (2.20)

is invertible. Indeed `det(B+epsilon G)` is a nonzero quadratic polynomial in `epsilon`, because its leading coefficient is `det G>0`. Choose any sequence `epsilon_m->0` avoiding those exceptional values.

Each `A_epsilon_m` has rank exactly three, so the nonsingular-pair proof applies. Its star is

`T_I(epsilon_m)
 =|det Lambda_epsilon_m| det G
 -> |det Lambda| det G
 =T_I.`                                                               (2.21)

Thus the laws `mu_m` of

`Q_m=X^T A_epsilon_m X+ell^T X+c`

satisfy every interval estimate

`mu_m(G_0) <= C_star T_I(epsilon_m)^(-1/3) |G_0|`                    (2.22)

for every open bounded interval `G_0`.

No moment bound is needed for the limiting step. For every sample point `X in R^n`,

`Q_m-Q=epsilon_m ||V^T X||_2^2 ->0`,                                (2.23)

so `Q_m->Q` almost surely and hence `mu_m=>mu_Q` weakly. By Portmanteau, for every open bounded interval `G_0`,

`mu_Q(G_0)
 <= liminf_m mu_m(G_0)
 <= C_star T_I^(-1/3)|G_0|.`                                         (2.24)

The standard interval-domination criterion now gives absolute continuity and (2.2).

This is a uniform-limit argument, not the forbidden claim that a small unbounded random perturbation can simply be discarded. The density constant is uniform before the limit and the conclusion is transferred at the level of interval probabilities.

## 3. Application to the current heavy-null pair-star branch

The newest account01/B05 structural addendum at

`yspennstate/math-open-problems@b8c42cc3e7d06ba1362b8138887c79de8940348b`

proves the exact identity, in its heavy-null rank-three coordinates,

`T_ij=S_i q_j`,                                                       (3.1)

where at target normalization `S_i>=1/2`. If a normalized residual heavy row is transverse, `q_j>=1/4`, then

`T_ij>=1/8.`                                                          (3.2)

Theorem 2 therefore gives, **without any nonsingularity assumption on the physical pair**, the concrete bound

`boxed:
 ||p_Q||_(infinity,ess)
 <= C_star (1/8)^(-1/3)
 =2 C_star
 <983.471.
}`                                                                    (3.3)

This pays the entire transverse-heavy alternative of that structural dichotomy, including the previously awkward exact-isotropic pair case. The only residual-heavy rows not paid by (3.3) are the longitudinal-spike alternative of the addendum,

`x_j^2/(1-c)>1/4`,                                                    (3.4)

of which there are at most three.

Thus the current exact-rank-three near-coloop obstruction is no longer “large anchored determinant star but singular physical pair.” The remaining structural debt is finite-cardinality longitudinal concentration, together with the already isolated shared-shear product-projection tube in the corresponding punctured branch.

## 4. Designated partner account04/B05 applied to an actual inequality

The completed designated-partner theorem

`QFORM-PHYSICAL-DEFINITE-PAIR-COAREA-v1`

is at

`yspennstate/math-open-problems@33cabb3bd5e466a58adc6eac49eba210ef62ef14`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260924T011830Z-account04-B05-convex-pair-r3/REPORT.md`.

For any literal original-coordinate definite pair `C`, it proves

`||p_Q||_(infinity,ess) <= pi / sqrt(|det C|)`                       (4.1)

under cap-one inputs, uniformly under arbitrary outside couplings and affine terms.

Apply it to the same transverse-heavy pair `{i,j}` whenever its physical `2x2` block is definite. On the concrete subbranch

`T_ij>=1/8`, `|det A[{i,j},{i,j}]|>=1/16`,                           (4.2)

Theorem 2 gives `<983.471`, while the designated partner gives the sharper actual inequality

`boxed:
 ||p_Q||_(infinity,ess) <=4 pi <12.567.
}`                                                                    (4.3)

The partner theorem is used only for the literal original pair; no rotated variables are declared independent.

## 5. What is new and what remains

New supporting theorem: an exact-rank-three form with any fixed literal pair carrying positive aggregate principal-triple determinant star has density bound `C_star T_I^(-1/3)`, even if the physical pair itself is exactly isotropic. The key cancellation is

`T_I=|det B| |sigma|`

between the two-dimensional coarea determinant and the rank-one Schur curvature. Exact singularity is then removable by a rank-preserving spectral perturbation whose interval constants converge.

This closes the `q_j>=1/4` transverse-heavy branch exposed by account01/B05. It does **not** by itself prove that a general higher-rank target contains a pair with `T_I` bounded below, and it does not pay the at-most-three longitudinal spikes in the near-coloop heavy-null branch. It therefore does not prove the full QFORM conjecture.

Precise next debt:

`QFORM-LONGITUDINAL-THREE-SPIKE-COAREA-v1`:

> in the exact-rank-three heavy-null near-coloop branch, after the diffuse residual chamber and every transverse-heavy row have been paid, retain the at-most-three literal longitudinal spike coordinates jointly with the hub and prove a uniform interval bound without dropping the remaining product-projection tail or taking a curved-fiber supremum.

A parallel equivalent debt is the product-projection Borel tube from account01/B05's current Witt reduction. Any attempted receiver must preserve the same-bank product provenance.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**.

## 6. Source pins

- Owner/control at start: `yspennstate/math-research-brain@718d1f4c7d3e942886470c5f84a0df388700865a`, OWNER CONTROL revision `2026-09-22.15`.
- Own determinant-only pair theorem: `yspennstate/math-open-problems@f24ae277a541417edf1ee63edcc002fd290ab6e6`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260924T023738Z-account03-B05-QFORM-r38/REPORT.md`.
- Rank-one affine small-ball source: `yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`, `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.
- Current heavy-row determinant-star addendum: `yspennstate/math-open-problems@b8c42cc3e7d06ba1362b8138887c79de8940348b`, `proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260924T015848Z-account01-B05-QFORM-auto11/STRUCTURAL_ADDENDUM.md`.
- Designated partner account04/B05: `yspennstate/math-open-problems@33cabb3bd5e466a58adc6eac49eba210ef62ef14`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260924T011830Z-account04-B05-convex-pair-r3/REPORT.md`.

Repository retrieval and Git delivery do not establish native learned-memory ingestion. `full_brain_connected=false`; execution remains `WITHOUT_VERIFIED_BRAIN`.
