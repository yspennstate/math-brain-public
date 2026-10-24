SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T13:14:06Z.
attacking: the near-zero physical-pivot survivor; test whether tiny local pivots force an approximate null-bank split, and if not compress the diffuse mixed bank before paying reciprocal minors.

# account03/B11 r32 — four-ray obstruction to rowwise splitting and grouped-bank compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** indefinite signatures; quantitative inequalities and rigorous computations  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / ROUTE_CORRECTION / PARTNER_RESULT_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and source boundary

The full conjecture remains OPEN. This run starts from account03/B11 r31, which resolved the **exact zero-pivot** two-plane boundary and left the near-zero regime open. It respects the live corrections: small nonzero pivots are not silently treated as zero; bounded projected density is not treated as independence; no pointwise quadratic-phase decay is used; and no arbitrary-joint 3D coarea bound is used.

The exact-rank-three setting is

`A = R M R^T`, `R^T R=I_3`, `M=M^T` invertible and indefinite.

The completed designated partner used below is account04/B11 r5:

`yspennstate/math-open-problems@50b07997bec888ff7cc6820cd42be8e34d0ffc48`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260923T111608Z-account04-B11-disjoint-volume-compiler-r5/REPORT.md`.

For disjoint physical triples `K,L`, with

`v_K = det(R_K R_K^T)=det(R_K)^2`, `v_L=det(R_L)^2`,

and `s=min |lambda(M)|`, it gives

`||p_Q||_infinity <= (3/s)(v_K v_L)^(-1/6)`.                         (1.1)

The previous B11 report is

`yspennstate/math-open-problems@07ecf405a0ca22d41d0cb17f7555165d65ad18fc`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T121207Z-account03-B11-QFORM-r31/REPORT.md`.

Its near-zero physical-pivot quantities in the two-plane chamber are

`theta_j = rho v_j^2 |A_jj|` on the T bank,                              (1.2)

and, after reflection,

`theta_i^S = (1-rho) x_i^2 |A_ii|` on the S bank.                        (1.3)

The question tested first is whether `max theta ->0` forces a rowwise approximation to the exact product split from r31.

## 2. A diffuse four-ray family with vanishing local pivots

Fix `0<rho<1` and an integer `k>=1`. Use `n=8k` original independent coordinates, divided into four ray types `S_+,S_-,T_+,T_-`, each containing `2k` coordinates. Put one spectral row on every coordinate as follows:

for `i in S_+`,

`r_i = (1/(2 sqrt(k)), +sqrt(rho)/(2 sqrt(k)), 0)`;                   (2.1)

for `i in S_-`,

`r_i = (1/(2 sqrt(k)), -sqrt(rho)/(2 sqrt(k)), 0)`;                   (2.2)

for `j in T_+`,

`r_j = (0, sqrt(1-rho)/(2 sqrt(k)), +1/(2 sqrt(k)))`;                 (2.3)

for `j in T_-`,

`r_j = (0, sqrt(1-rho)/(2 sqrt(k)), -1/(2 sqrt(k)))`.                 (2.4)

The sign cancellation and the four multiplicities give exactly

`R^T R = I_3`.                                                         (2.5)

Thus `A=RMR^T` has the same three nonzero eigenvalues as `M`.

For the obstruction take

`M_* = [[1,0,0],[0,0,1],[0,1,0]]`,                                    (2.6)

whose spectrum is `{1,1,-1}`. Hence this is a genuine target-scope signature `(2,1)`; replacing `M_*` by `-M_*` gives `(1,2)`.

For every S row,

`A_ii = r_i^T M_* r_i = 1/(4k)`.                                      (2.7)

For T rows,

`A_jj = +sqrt(1-rho)/(2k)` on `T_+`,
`A_jj = -sqrt(1-rho)/(2k)` on `T_-`.                                  (2.8)

Since `v_j^2=1/(4k)` on T, the r31 pivot certificate is

`theta_j = rho sqrt(1-rho)/(8 k^2)`.                                  (2.9)

The reflected S certificate is

`theta_i^S = (1-rho)/(16 k^2)`.                                       (2.10)

Both vanish like `k^{-2}`.

Nevertheless this family stays a fixed distance from the exact rowwise split. Every mixed S row has

`|y_i|/|x_i| = sqrt(rho)`,                                             (2.11)

and every mixed T row has

`|u_j|/|v_j| = sqrt(1-rho)`.                                           (2.12)

In particular at `rho=1/2`, both ratios equal `1/sqrt(2)` for every row, independently of k. Even in aggregate,

`sum_{j in T} u_j^2 = 1-rho`, `sum_{j in T} v_j^2=1`,                  (2.13)

so the mixed T bank does not become L2-close to the exact `e_2/e_3` coordinate split as the local pivot certificates vanish.

### Correction 2.1 — `QFORM-SMALL-PIVOT-NOT-ROWWISE-SPLIT-v1`

The implication

> uniformly small per-coordinate quantities `rho v_j^2|A_jj|` (and their reflected S analogues) force rowwise, or even bank-L2, proximity to the exact zero-pivot product split

is false without an additional aggregate hypothesis.

This is a correction to a possible **near-zero mechanism**, not a counterexample to QFORM.

## 3. Why fixed raw triples also lose the scale

At `rho=1/2`, every original spectral row has squared norm

`||r_i||^2 = 3/(8k)`.                                                  (3.1)

For any physical triple `K`, Hadamard's determinant inequality therefore gives

`v_K=det(R_K)^2 <= (3/(8k))^3 = 27/(512 k^3)`.                         (3.2)

Thus every fixed raw three-coordinate volume tends to zero. Applying a reciprocal-minor theorem to one or two unaggregated triples necessarily loses powers of k. This family therefore simultaneously defeats:

1. rowwise near-zero splitting from the local pivot certificates; and
2. fixed-cardinality triple selection at a universal scale.

The correct operation must aggregate independent source coordinates **before** reciprocal volume is paid.

## 4. Main theorem: exact product-preserving grouped-bank compression

Split each of the four ray types into two disjoint groups of exactly k original coordinates. There are now eight disjoint groups. For a group `g`, define

`Y_g = k^(-1/2) sum_{i in g} X_i`.                                     (4.1)

The eight `Y_g` are mutually independent because the groups are disjoint. By the scalar Rogozin--Ball projection bound for independent cap-one coordinates,

`||p_{Y_g}||_infinity <= sqrt(2)`.                                     (4.2)

Set

`Z_g = sqrt(2) Y_g`.                                                    (4.3)

Then the eight `Z_g` remain independent and each has density cap at most one.

Because the spectral row is constant inside every group, the form depends on the original variables only through these eight normalized sums. Let `R_0` be the `8 x 3` matrix with rows

`(1/2,+sqrt(rho)/2,0)` twice,
`(1/2,-sqrt(rho)/2,0)` twice,
`(0,sqrt(1-rho)/2,+1/2)` twice,
`(0,sqrt(1-rho)/2,-1/2)` twice.                                       (4.4)

Directly,

`R_0^T R_0 = I_3`.                                                     (4.5)

Moreover

`R^T X = R_0^T Y = (1/sqrt(2)) R_0^T Z`,                              (4.6)

and hence exactly

`Q = Z^T R_0 (M/2) R_0^T Z`.                                          (4.7)

No approximation and no rotation of the independent variables has occurred. The only change is grouping disjoint original-coordinate sums, followed by scalar rescaling.

### Theorem 4.1 — `QFORM-FOUR-RAY-GROUPED-BANK-COMPILER-v1`

For the family (2.1)--(2.4), let `M` be any invertible symmetric `3 x 3` matrix and let

`s = min |lambda(M)|`.

Then for arbitrary independent original inputs with density caps at most one, if `s>0`,

`boxed:
 ||p_Q||_infinity <= (6*2^(4/3)/s) [max(rho,1-rho)]^(-1/3)
 <= (6*2^(5/3))/s.`                                                   (4.8)

In particular, under the exact target normalization `s>=1`,

`boxed:
 ||p_Q||_infinity <= 6*2^(5/3)
 = 19.0488126236184... .`                                             (4.9)

This includes both indefinite signatures `(2,1)` and `(1,2)`.

### Proof

The effective spectral matrix in (4.7) is `M/2`, so its minimum nonzero eigenvalue magnitude is `s/2`.

If `rho>=1/2`, take two disjoint effective physical triples, each consisting of one `S_+`, one `S_-`, and one T row, using the two different copies. For example

`K={S_+^(1),S_-^(1),T_+^(1)}`,
`L={S_+^(2),S_-^(2),T_-^(2)}`.                                       (4.10)

For either triple,

`|det R_(0,K)| = sqrt(rho)/4`,
`v_K = rho/16`, and similarly `v_L=rho/16`.                            (4.11)

Apply account04/B11 r5 to (4.7):

`||p_Q||_infinity
 <= 3/(s/2) [(rho/16)^2]^(-1/6)
 = (6*2^(4/3)/s) rho^(-1/3).`                                        (4.12)

If `rho<=1/2`, instead choose two disjoint triples with one S row and one `T_+`, one `T_-` row. Each has

`v_K=v_L=(1-rho)/16`,                                                  (4.13)

so

`||p_Q||_infinity
 <= (6*2^(4/3)/s)(1-rho)^(-1/3).`                                     (4.14)

Since `max(rho,1-rho)>=1/2`, both cases imply (4.8)--(4.9). QED.

## 5. Actual partner inequality and why it matters

Equation (4.12) is the required actual application of the completed designated partner result. At the most symmetric point `rho=1/2` and `s=1`, it reads

`boxed:
 ||p_Q||_infinity <= 6*2^(5/3)
 =19.0488126236184... .`                                              (5.1)

By contrast, before grouping, every raw triple has volume at most `27/(512 k^3)`, so the same disjoint-volume compiler applied to raw triples can lose order k. Grouping converts diffuse repeated source mass into two **fixed-volume independent physical triples** while preserving the cap-one product hypotheses after a harmless scalar rescaling.

This is precisely the sort of aggregate-before-inversion step that the live corrections require.

## 6. Opposite-sign rank two and the third-direction mechanism

The mandatory control remains: for independent `X,Y ~ Uniform[-1/2,1/2]`,

`p_(2XY)(t)=log(1/(2|t|))`, `0<|t|<1/2`,                              (6.1)

so opposite-sign rank two is logarithmically unbounded.

In the present four-ray family the third direction is not exposed by any fixed original coordinate when k is large. It is collective. The grouping map (4.1) recovers three-dimensional volume from eight disjoint source banks. Once that volume is recovered, the partner rank-three compiler supplies the integrable third-direction smoothing. Thus this run identifies a second concrete way the third direction removes the rank-two logarithm:

> not by a local pivot becoming large, but by aggregating diffuse product mass until two disjoint rank-three source volumes become macroscopic.

No spectral rotation is treated as preserving independence.

## 7. What remains

This theorem is deliberately scoped. It handles an exact repeated four-ray two-plane family; it does **not** prove that a general near-zero-pivot bank admits such an exact finite grouping, and it does not absorb arbitrary additional nonseparable spectrum.

The corrected next implication is:

`QFORM-APPROXIMATE-RAY-CLUSTER-GROUPING-v1`:

> Starting from a genuinely rotated indefinite exact-rank-three two-plane survivor in which all local pivot certificates are small, either extract finitely many disjoint original-coordinate groups whose normalized aggregate coefficient vectors have two disjoint rank-three volumes bounded below by a universal constant, or route the failure (angular spread / lack of cluster concentration) to an already-paid diffuse, ridge, pair-area, or cross-volume receiver. The grouping must be performed on disjoint original-coordinate banks so that product independence is retained.

A promising quantitative invariant is not `max_j theta_j`, but the amount of coefficient L2 mass carried by angular sectors in each spectral plane. The four-ray theorem proves the exact clustered endpoint and shows why per-row perturbation is the wrong parameter.

The theorem above gives an **essentially bounded density**. Continuity is not proved by this argument. Global continuity and the unrestricted full conjecture remain open.

## 8. Verification

`VERIFY.py` checks symbolically:

1. `R_0^T R_0=I_3`;
2. the two `SST` triple volumes `rho/16`;
3. the two `STT` triple volumes `(1-rho)/16`;
4. `spec(M_*)={1,1,-1}`;
5. the exact pivot formulas (2.9)--(2.10);
6. the `rho=1/2` raw-triple Hadamard scale `27/(512k^3)`;
7. the grouped universal constant `6*2^(5/3)=19.0488126236184...`.

The execution terminates with

`QFORM_B11_R32_GROUPED_FOUR_RAY_CHECK_PASS`.

No installation, Monte Carlo inference, unsupported independence, public release, scheduler mutation, email, notification change, paid model/API, Codex call, or permission expansion was used.
