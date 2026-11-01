SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B20, 2026-09-23T09:04:22Z.
attacking: exact-rank-three normalized-heavy closure by source-valid sequential Fresnel peeling, then the newest designated-partner three-packet compiler.

# fleet02/B20 auto11 — sequential Fresnel coloop compiler and strengthened three-packet endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control on publication refresh:** revision `2026-09-22.15`, QFORM sole target, no fleet02/B20 pause.  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval occurred; no learned-memory receiver ingestion was exposed).  
**Status:** `ESSENTIAL_STEP_APPLIED / GLOBAL EXACT-RANK3 18-CORE REDUCTION / PARTNER-R30 STRENGTHENED / FULL QFORM OPEN`.

The unrestricted conjecture remains OPEN. No Gaussian/log-concavity, moment, support, diagonal-basis, or post-rotation independence assumption is introduced. Continuity is not claimed from the arguments below.

## 1. Sources consumed and corrections preserved

Fresh protected brain source was read from `yspennstate/math-research-brain` main, including `AGENTS.md`, owner README/control, `fleet.json`, `roles.json`, `PROTOCOL.md`, the QFORM manifest/current research/claims/deltas/correction inbox/pathways/memory protocol, proof-first request, newest-Claude request, and the exact fleet02/B20 assignment. The publication refresh used brain main commit `63f10ac0853a06df9a3861a46f1a8b328e8137d2`; owner control still reports revision `2026-09-22.15`.

The required pinned interactive source was read at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. In particular, Theorem F is used below at its exact formula. The pointwise-decay, unrestricted-fiber-supremum, and post-rotation-independence corrections are retained throughout.

The newest compatible **completed** designated partner found on refresh is fleet03/B20 r30, canonical mathematics

`yspennstate/math-open-problems@2c0131b6830892a77a8faaf3521388d3a51e7514`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B20/20260923T084738Z-fleet03-B20-QFORM-r30/REPORT.md`.

A newer fleet03/B20 r31 had a start record but no completed result when this source decision was made, so r30 is the newest completed designated-partner input and is consumed below rather than waiting.

## 2. Exact-rank-three setup

Work in the exact-rank-three chamber

`A = R M R^T`, `R^T R = I_3`, `M=M^T`, `s_min(M)>=1`.              (2.1)

The rows of `R` are `r_i in R^3`. Thus

`sum_i r_i r_i^T = I_3`, `||r_i||^2<=1`.                         (2.2)

Conditioning original coordinates is source-valid: the unconditioned coordinates remain independent with their original cap-one densities, and the conditioned values create only affine/constant terms. No spectral coordinate is declared independent.

For an original-coordinate conditioned set `K`, define the residual spectral Gram

`S_K := sum_(i notin K) r_i r_i^T = I_3 - sum_(i in K) r_i r_i^T`. (2.3)

Whenever `S_K>0`, put

`U_K := R_(K^c) S_K^(-1/2)`, `B_K := S_K^(1/2) M S_K^(1/2)`.      (2.4)

Then `U_K^T U_K=I_3`, the residual physical-row leverages in the whitened frame are

`ell_i(K) = r_i^T S_K^(-1) r_i`,                                 (2.5)

and

`det B_K = det(S_K) det(M)`.                                     (2.6)

## 3. New theorem — global sequential Fresnel/coloop compiler

### Theorem 3.1 — `QFORM-EXACTR3-SEQUENTIAL-FRESNEL-COLOOP-v1`

Fix `0<tau<1`. Under (2.1), exactly one of the following procedures terminates after at most

`N_tau := ceil(3 log_2(1/tau))`                                  (3.1)

original-coordinate removals:

1. **Fresnel payment.** For some conditioned original set `K`, `lambda_min(S_K)>=tau` and every residual whitened leverage satisfies `ell_i(K)<=1/2`; then

`||p_Q||_infinity <= 12/tau`.                                    (3.2)

2. **Near-coloop core.** There is an original-coordinate set `K`, `|K|<=N_tau`, such that

`lambda_min(S_K)<tau`, equivalently
`lambda_max(sum_(i in K) r_i r_i^T)>1-tau`.                       (3.3)

#### Proof

Start with `K=empty`, `S=I_3`. At a stage with `lambda_min(S)>=tau`, whiten as in (2.4). If all residual row leverages are at most `1/2`, apply pinned Fresnel--Brascamp--Lieb Theorem F to the residual exact-rank-three form. Its exact bound is

`||p_(Q | X_K)||_infinity <= 12 |det B_K|^(-1/3)`.                (3.4)

Because `|det M|>=1` and `det S_K>=tau^3`,

`12 |det B_K|^(-1/3)
 <=12 (det S_K)^(-1/3)
 <=12/tau`.                                                       (3.5)

This is uniform in all affine terms created by the conditioning, so averaging the conditional laws gives (3.2) for the full `Q`.

If instead some residual physical row `r` has whitened leverage

`ell=r^T S^(-1)r>1/2`,                                           (3.6)

condition that ORIGINAL coordinate and replace `S` by

`S' = S-r r^T`.                                                   (3.7)

Since `S'` is the Gram of the still-unconditioned rows, it is positive semidefinite. If singular, the near-coloop alternative already holds. Otherwise the matrix determinant lemma gives the exact descent

`det S' = det S (1-ell) < (1/2) det S`.                           (3.8)

After `m` such heavy-leverage removals, as long as the near-coloop alternative has not yet occurred,

`tau^3 <= det S_m < 2^(-m)`.                                     (3.9)

For `m=N_tau`, `2^(-m)<=tau^3`, contradicting (3.9). Hence payment or near-coloop occurs after at most `N_tau` original-coordinate removals. QED.

### Corollary 3.2 — fixed 18-coordinate compiler

Take

`tau=1/64`, `N_tau=18`.                                          (3.10)

Then every exact-rank-three target state is either paid by

`boxed(||p_Q||_infinity <= 768)`                                 (3.11)

or has an original-coordinate core `K`, `|K|<=18`, with

`lambda_1(T)>63/64`, `T:=sum_(i in K)r_i r_i^T`.                 (3.12)

This is a global exact-rank-three reduction; it does **not** require the partner's earlier HC pre-core.

## 4. Adding the finite-core receiver: an 18-coordinate double-coloop or payment

The completed fleet02/B20 r25 finite-core theorem states that if an original core `K`, `|K|=m`, satisfies

`sum_(i in K) r_i r_i^T >= kappa I_3`,                            (4.1)

then

`||p_Q||_infinity <= 2 sqrt(6 pi m)/kappa`.                       (4.2)

Apply this to the near-coloop core from Corollary 3.2 with `kappa=1/64`. If `lambda_3(T)>=1/64`, then `m<=18` and

`||p_Q||_infinity
 <= 128 sqrt(108 pi)
 = 2357.744735... <2358`.                                         (4.3)

Therefore every still-unpaid exact-rank-three state admits an ORIGINAL core `K`, `|K|<=18`, such that

`boxed(lambda_1(T)>63/64, lambda_3(T)<1/64).`                    (4.4)

Moreover, if every physical leverage `||r_i||^2<=1/2`, pinned Theorem F applied at `K=empty` gives `||p_Q||_infinity<=12`. Hence every state surviving (4.3) and the global Fresnel branch also has an ORIGINAL physical row `h` with

`boxed(c_h:=||r_h||^2>1/2).`                                     (4.5)

Thus the entire exact-rank-three chamber is now reduced, with explicit universal constants, to a <=18-coordinate double-coloop plus one physical high-leverage row.

This strictly improves the previous <=126-core r25 state and the early <=49-core checkpoint of this same run.

## 5. Newest designated partner r30 applied at an exact expression

Fleet03/B20 r30 proves the exact rank-one update lemma: if `T>=0`, `v` is a minimum-eigenvalue eigenvector of `T`, `lambda_2(T)>=a`, and `|<r,v>|^2>=b`, then

`lambda_min(T+r r^T) >= ab/(1+a)`.                               (5.1)

Apply this exact expression to the stronger core (4.4), with

`a=b=1/64`.                                                       (5.2)

Then

`ab/(1+a)=1/4160`.                                               (5.3)

If `h notin K`, `lambda_2(T)>=1/64`, and `|<r_h,v_3>|^2>=1/64`, the enlarged original core `K union {h}` has size at most `19` and Gram at least `I/4160`. The finite-core theorem therefore pays this branch by

`||p_Q||_infinity
 <= 2 sqrt(6 pi*19)*4160
 = 8320 sqrt(114 pi)
 =157452.9088... <157453`.                                        (5.4)

The numerical constant is not optimized; finiteness and source-validity are the point.

## 6. Strengthened three-packet compiler

### Theorem 6.1 — `QFORM-18CORE-THREEPACKET-COMPILER-v1`

Every exact-rank-three state surviving (3.11), (4.3), (4.5), and (5.4) has a partition of ORIGINAL coordinates

`[n]=B_1 disjoint_union B_2 disjoint_union B_3`                  (6.1)

and an orthonormal spectral basis `(e_1,e_2,e_3)` such that

`boxed(sum_(i in B_k)<r_i,e_k>^2 > c_**  for k=1,2,3)`           (6.2)

with

`boxed(c_** = 1953/16384 = 0.11920166015625),`                   (6.3)

and, in every case, one of the packets (`B_1` in the construction below) has cardinality at most `18`. Consequently there is an ORIGINAL physical coordinate `p in B_1` satisfying

`boxed(|<r_p,e_1>|^2 > c_**/18 = 217/32768).`                   (6.4)

#### Proof

Diagonalize the core Gram `T` in an orthonormal basis `(v_1,v_2,v_3)` with eigenvalues `lambda_1>=lambda_2>=lambda_3`. By (4.4),

`lambda_1>63/64`, `lambda_3<1/64`.                               (6.5)

### Case A: `h notin K`, `lambda_2>=1/64`

The complement carries less than `1/64` mass in `v_1`, so

`|<r_h,v_1>|^2<1/64`.                                            (6.6)

The branch `|<r_h,v_3>|^2>=1/64` was paid in (5.4), so for a survivor

`|<r_h,v_3>|^2<1/64`.                                            (6.7)

Using `||r_h||^2>1/2`,

`|<r_h,v_2>|^2
 >1/2-1/64-1/64
 =15/32`.                                                         (6.8)

Take

`B_1=K`, `B_2={h}`, `B_3=K^c\{h}`,
`e_1=v_1`, `e_2=v_2`, `e_3=v_3`.                                (6.9)

The packet masses are respectively

`>63/64`, `>15/32`, `>1-1/64-1/64=31/32`,                       (6.10)

all larger than `c_**`.

### Case B: `h notin K`, `lambda_2<1/64`

Put `O=K^c`. Along `v_2,v_3`, the total masses in `O` satisfy

`A=1-lambda_2>63/64`, `B=1-lambda_3>63/64`.                     (6.11)

For `i in O`, set

`a_i=<r_i,v_2>^2`, `b_i=<r_i,v_3>^2`.                            (6.12)

As in fleet03/B20 r30,

`a_i b_i <=(a_i+b_i)^2/4 <=(a_i+b_i)/4`,                        (6.13)

so

`sum_i a_i b_i <=(A+B)/4`.                                      (6.14)

Split `O=U disjoint_union V` by independent fair coins. Then

`E[(sum_(i in U)a_i)(sum_(j in V)b_j)]
 = [AB-sum_i a_i b_i]/4
 >= [AB-(A+B)/4]/4
 > [(63/64)^2-(126/64)/4]/4
 =1953/16384`.                                                    (6.15)

Hence some deterministic split has product `>c_**`. Each factor is at most one, therefore each factor itself is `>c_**`. Take

`B_1=K`, `B_2=U`, `B_3=V`,
`e_1=v_1`, `e_2=v_2`, `e_3=v_3`.                                (6.16)

Then (6.2) holds.

### Case C: `h in K`

Because `v_3` is the minimum-eigenvalue direction of `T`,

`|<r_h,v_3>|^2 <=lambda_3<1/64`.                                (6.17)

Thus the transverse vector `q=Proj_(v_3^perp)r_h` obeys

`||q||^2>1/2-1/64=31/64`.                                       (6.18)

Put `e_1=q/||q||`, let `e_2` be the unit vector in `v_3^perp` perpendicular to `e_1`, and put `e_3=v_3`. The singleton `{h}` carries `>31/64` mass in `e_1`, while `r_h` has zero `e_2` component. On `O=[n]\{h}`, the total `e_2` mass is exactly `1`, and the total `e_3` mass is `>63/64`. The same fair-split computation gives a split `O=U disjoint_union V` for which both designated packet masses exceed

`125/1024 =2000/16384 > c_**`.                                   (6.19)

Take `B_1={h}`, `B_2=U`, `B_3=V`.

This proves (6.2). Finally `|B_1|<=18` in Cases A/B and `|B_1|=1` in Case C. Since the total designated mass in `B_1` exceeds `c_**`, pigeonhole gives a row `p` satisfying (6.4). QED.

### Comparison with designated partner r30

The designated partner's compiler had core size `<=126`, finite-core payment `<13309`, and packet constant

`453/4096 =1812/16384`.                                         (6.20)

The source-valid sequential Fresnel descent above changes the live endpoint to a core of size `<=18`, while rerunning the partner's **exact** rank-one update formula at `a=b=1/64` raises the packet constant to

`1953/16384 >453/4096`.                                         (6.21)

The resulting physical witness (6.4) is new and will be useful for the next grouped/hub receiver.

## 7. Why this does not collapse to a local physical pivot

The newest compatible fleet02/B19 r31 stress family proves that an extreme normalized coloop can coexist with every fixed-scale physical scalar and principal-pair pivot tending to zero. Hence (6.4) must **not** be converted by fiat into a uniformly nondegenerate physical scalar or pair pivot. That shortcut is refuted inside the exact target.

Likewise, fleet03/B20 r30 gives an explicit packet frame for which the first two packet ranges coincide and every one-row-from-each packet triple has zero determinant. Therefore the packet masses (6.2) do **not** by themselves imply a uniformly positive third-volume. The next receiver must use aggregate range/mixed-row structure.

## 8. Required pinned source applied at an actual inequality

The owner-required pinned Fresnel--Brascamp--Lieb Theorem F is not merely cited: it is the engine of (3.2). At `tau=1/64`, every residual state with all whitened physical leverages at most `1/2` satisfies

`||p_Q||_infinity
 <=12 |det(S^(1/2) M S^(1/2))|^(-1/3)
 <=12 (tau^3)^(-1/3)
 =768`.                                                          (8.1)

This use preserves original-coordinate independence and accepts arbitrary affine terms produced by the conditioning.

## 9. Strongest current conditional end-to-end argument

Inside the exact-rank-three chamber, the present run now gives the following exhaustive source-valid chain:

1. sequential original-coordinate Fresnel peeling pays a branch by `<=768`, or produces `K`, `|K|<=18`, with `lambda_1(T)>63/64`;
2. the finite-core receiver pays `lambda_3(T)>=1/64` by `<2358`;
3. all-leverage-`<=1/2` is already paid by pinned Theorem F (`<=12`), so a survivor has a physical row `h` with leverage `>1/2`;
4. the newest designated-partner rank-one update expression pays the robust `h`/minimum-direction branch by `<157453`;
5. every residual state has three disjoint ORIGINAL-coordinate packets with designated spectral masses `>1953/16384`, one packet of size `<=18`, a physical row `p` with designated component squared `>217/32768`, and (after the partner's fleet04 overlap is removed) genuinely mixed longitudinal/transverse physical geometry relative to a leverage-`>1/2` row.

Every conditioning is on original coordinates. No rotated random coordinates are used as independent variables.

## 10. First unpaid universal implication

The first unpaid implication in this strengthened exact-rank-three route is now

`QFORM-SMALLPACKET-THREEPACKET-MIXED-RANGE-PAYMENT-v1`:

Assume (2.1), the original independent cap-one product source, and a partition `(B_1,B_2,B_3)` plus orthonormal spectral basis `(e_1,e_2,e_3)` satisfying

`|B_1|<=18`,
`sum_(i in B_k)<r_i,e_k>^2 >1953/16384` for `k=1,2,3`,           (10.1)

with an ORIGINAL physical row `h` of leverage `>1/2`, failure of the already-paid exact longitudinal/transverse partition relative to `h`, and hence a genuinely mixed residual physical row. Prove a universal linear small-ball/density bound, or source-preservingly reduce this packet to an already-paid volume, grouped-square/hyperbolic, ridge, mixed-hub, or physical-pair class.

The packet masses cannot be converted for free into one nonzero packet-transversal determinant; the fixed-size first packet and physical witness (6.4) are the extra new currency. A promising next mechanism is a quantitative Hall/mixed-discriminant alternative **with the small packet retained**: either aggregate cross-packet third-volume is fixed-scale and feeds an existing Theorem D/D' receiver, or two packet ranges align near a common spectral line; in the latter case the bounded first packet should be kept as genuine physical hubs while the other two independent original banks supply the grouped hyperbolic/square smoothing. Another bare local-pivot selection is ruled out by the B19 stress family.

## 11. Scope and remaining debts

This report does **not** prove the full QFORM target. It makes a strong exact-rank-three closure advance. Separate arbitrary-extra-spectrum/N3/O0 debts remain, and the required two independent end-to-end reviews of a full candidate do not exist. Global continuity remains separate and OPEN.

Model self-report for this run is `GPT-5.6 Sol`; requested effort is `maximum actually supported`; configured and known actual effort are unexposed/`UNKNOWN`; provider reasoning-token and pure-thinking-time counters are unexposed/null. Elapsed execution is wall-clock execution and is not pure thinking.
