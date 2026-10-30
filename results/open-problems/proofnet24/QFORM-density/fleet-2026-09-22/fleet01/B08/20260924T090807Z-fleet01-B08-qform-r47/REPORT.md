SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-24T09:08:07Z.
attacking: strengthen the row-aware diffuse cut after the global scalar/edge compiler, using exact second moments to preserve almost one-half of the distributed physical star while keeping the top-three spectral frame balanced; then spend non-alignment through the marginal-free third-compound crossing receiver.

# fleet01/B08 r47 — edge-capped star-aware cut and relative rank-two carrier router

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case  
Status: **NEW SUPPORTING END-TO-END BRANCH + SHARPER PRODUCT-SAFE SURVIVOR / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture remains OPEN. Full-target continuity remains OPEN. The new paid branch below has a continuous `C_0(R)` density because it is paid by the completed marginal-free physical third-compound theorem. No moment, support, iid, Gaussian, log-concavity, connected-support, diagonal-basis, post-rotation independence, arbitrary-joint coarea, fiber-supremum, law-uniform pointwise quadratic-phase decay, or deletion of a nonzero coefficient tail is used.

## 1. Fresh premises and designated partner

Fresh owner control was read from `yspennstate/math-research-brain/main`; the live owner revision remains `2026-09-22.15`, QFORM-only. The programme MANIFEST, CURRENT_RESEARCH, CLAIMS, live CORRECTION_INBOX, MEMORY_PROTOCOL and this B08 assignment were reread. Repository transport is not native learned-memory ingestion.

The immediate own input is r43,

`yspennstate/math-open-problems@5eceb142f1c4ebaa8c6096d0333a9c1995f39c69`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B08/20260924T051232Z-fleet01-B08-qform-r43/REPORT.md`.

After its already-paid scalar and fixed-edge branches, a still-unpaid state with the localized physical row `k` satisfies, with

`rho=0.0006247538095703261`,

`B:=||A[k,-k]||_2 > rho L`,                                      (1.1)

`max_(j!=k)|A_kj| < rho L/16 < B/16`,                            (1.2)

and on the genuinely diffuse source branch the selected top-three eigenspace frame `U` obeys

`U^T U=I_3`, `max_i ||U_i||_2^2<=1/48`.                          (1.3)

The completed designated-partner result actually applied is fleet02/B08 r35,

`yspennstate/math-open-problems@087cf5aa5cfcee4eb6ae243facb9e0fcf2391e29`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/fleet02-B08-20260924T083643Z-r35/REPORT.md`.

Its row-aware cancellation router proves that for a physical cut with both selected-frame Grams at least `3I_3/10`, deleting a selected row of leverage at most `1/48` leaves selected crossing singular value

`c0 L`, `c0=sqrt(67/800)=0.28939592256975566...`;                (1.4)

at the gate

`sigma=c0/2=0.14469796128487783...`                              (1.5)

one either has a two-mode complementary-cancellation branch when the literal deleted crossing has `s_2<sigma L`, or a rank-two-carrier branch when `s_2>=sigma L`. The same source records the exterior inequality used below and the completed physical third-compound receiver

`||p_Q||_infinity <= 6^(4/3) e_3(MM^T)^(-1/6)`                  (1.6)

for a literal ORIGINAL-coordinate crossing `M`, with arbitrary same-side curvature, outside couplings and affine terms retained; this branch has `p_Q in C_0(R)`.

## 2. New star-aware balanced cut

### Theorem 2.1 — `QFORM-EDGE-CAPPED-STAR-AWARE-THREEFRAME-CUT-v1`

Let `U in R^(n x 3)` satisfy `U^T U=I_3` and

`max_i ||U_i||_2^2<=1/48`.                                      (2.1)

Fix an ORIGINAL coordinate `k`, and let `b=(b_j)_(j!=k)` be any physical row vector with

`B=||b||_2>0`, `||b||_infinity < B/16`.                         (2.2)

Then there is an ORIGINAL-coordinate partition `S union T=[n]`, `k in S`, such that simultaneously

`boxed: U_S^T U_S >=3I_3/10,  U_T^T U_T>=3I_3/10,`              (2.3)

and

`boxed: ||b_T||_2^2 >=(9/20)B^2.`                               (2.4)

In particular `||b_T||_2 >=3B/sqrt(20)=0.6708203932...B`.

#### Proof

Put `u_i=U_i^T`. For every `i!=k`, independently take `xi_i in {0,1}` with mean `1/2`; let `T={i!=k:xi_i=1}` and force `k in S`. Set

`G_T=sum_(i!=k) xi_i u_i u_i^T`.

Then

`E G_T=(I-u_k u_k^T)/2`.                                        (2.5)

The least eigenvalue of this mean is at least `47/96`. Thus if

`||G_T-EG_T||_op <= delta`, `delta=47/96-3/10=91/480`,           (2.6)

then `G_T>=3I/10`. The same event also gives

`G_T<=I/2+(91/480)I <7I/10`,

so `G_S=I-G_T>=3I/10`.

Independence and centering give the exact second moment

`E||G_T-EG_T||_F^2
 =(1/4) sum_(i!=k)||u_i||_2^4
 <=(1/4)(1/48) sum_i ||u_i||_2^2
 =1/64.`                                                        (2.7)

Hence Markov gives

`P(frame bad) <= (1/64)(480/91)^2 =3600/8281.`                  (2.8)

For the physical star set

`Z=sum_(i!=k) xi_i b_i^2`.

Then `EZ=B^2/2`, while from (2.2)

`Var Z=(1/4)sum_i b_i^4
 <(1/4)(B^2/256)sum_i b_i^2
 =B^4/1024.`                                                    (2.9)

Chebyshev therefore gives

`P(Z<9B^2/20)
 <= (B^4/1024)/(B^4/20^2)=25/64.`                               (2.10)

Finally

`3600/8281+25/64=0.8253551050...<1`.                            (2.11)

So with positive probability both desired events occur, proving existence of the required literal physical cut. QED.

This improves the designated partner's generic `B/sqrt(6)` crossing-star guarantee to `sqrt(9/20)B` precisely in the edge-capped survivor forced by r43.

## 3. Actual application to the QFORM survivor

Use `b=A[k,-k]` in Theorem 2.1. Equations (1.1)-(1.2) verify its hypotheses, so there is a physical cut with

`z:=A[k,T]`,

`boxed: ||z||_2 >=sqrt(9/20) B >sqrt(9/20) rho L,`               (3.1)

while both selected-frame Grams remain at least `3I/10`.

Delete row `k` from the crossing and write

`D=A[S\{k},T]`.                                                  (3.2)

Because `||U_k||^2<=1/48`, the designated partner's exact deletion calculation applies at this actual cut and gives the selected top-three deleted crossing the lower singular scale `c0 L` from (1.4). Put `sigma=c0/2` as in (1.5).

### Branch A: `s_2(D)<sigma L`

The partner's two-mode cancellation argument applies at the actual matrix `D`: if `A_3=U Lambda U^T` is the selected top-three component and

`C^-=(A-A_3)[S\{k},T]`,

then

`boxed: s_2(C^-) > sigma L.`                                     (3.3)

For completeness, choose a top right singular vector `v_1` of `D`. The space `range(U_T) cap v_1^perp` has dimension at least two. On it, `||Dx||<sigma L||x||` while the selected deleted crossing has norm at least `c0L||x||`; hence `||C^-x||>(c0-sigma)L||x||=sigma L||x||`, and min-max gives (3.3).

### Branch B: `s_2(D)>=sigma L`

Let `V_2(D)` be a top-two right singular subspace. The exterior identity in the partner source gives for the actual full crossing `M=[z^T;D]`

`e_3(MM^T)
 >=s_1(D)^2 s_2(D)^2 dist(z,V_2(D))^2.`                          (3.4)

If

`dist(z,V_2(D)) >= ||z||_2/2`,                                  (3.5)

then (3.1), `s_1>=s_2>=sigma L`, and (3.4) imply

`e_3(MM^T)^(1/6)
 >= kappa L`,                                                     (3.6)

where

`kappa=[ sigma^2 * (sqrt(9/20)rho/2) ]^(1/3)
       =0.016370803646028022... .`                               (3.7)

Applying the completed physical-crossing theorem (1.6) to this **actual literal crossing** yields

`boxed: ||p_Q||_infinity <=665.985848511/L,  p_Q in C_0(R).`     (3.8)

All same-side quadratic curvature, complementary spectrum and induced affine terms remain present.

Therefore every state in this B08 survivor that is still unpaid even at the finite benchmark (3.8), and that lies in Branch B, must satisfy the genuinely relative alignment tube

`boxed: dist(z,V_2(D)) < ||z||_2/2.`                             (3.9)

This is stronger structurally than the preceding absolute-angle tube: the residual misalignment is controlled relative to the actual physical star norm, not merely by a fixed multiple of `L`.

## 4. Original-coordinate bank explosion

The same cut also turns (1.2) into a product-safe many-bank statement. From (2.4),

`max_(j in T) b_j^2 / ||z||_2^2
 < (B^2/256)/[(9/20)B^2]
 =5/576.`                                                        (4.1)

For nonnegative weights of total `W` and maximum at most `eta W`, whenever `eta<1/m` one can partition the indices into `m` nonempty groups each of mass greater than `W/m-eta W`: order the indices arbitrarily and cut at the first cumulative crossings of `jW/m`. The overshoot at every cut is at most one maximum weight.

Taking `eta=5/576` and `m=16`, the physical set `T` therefore has sixteen pairwise-disjoint ORIGINAL-coordinate banks `J_1,...,J_16` with

`boxed:
 ||z_{J_r}||_2^2 > (31/576)||z||_2^2,
 ||z_{J_r}||_2 > (sqrt(31)/24)||z||_2,
}`                                                                (4.2)

for every `r`. Combining with (3.1),

`boxed:
 ||z_{J_r}||_2 > sqrt(31/1280) B
 >9.722652753e-5 L.
}`                                                                (4.3)

Thus the current diffuse survivor contains sixteen genuinely disjoint physical star banks before any random-variable rotation.

## 5. Relative alignment forces a three-bank rank-two carrier footprint

There is an additional rigid consequence in the unpaid aligned Branch B. Apply the preceding partition lemma with `m=4`. It gives four disjoint physical banks `K_1,...,K_4 subset T` satisfying

`||z_{K_r}||_2 > (sqrt(139)/24)||z||_2`.                         (5.1)

Write the orthogonal decomposition

`z=v+e`, `v=P_(V_2(D))z`, `e=(I-P_(V_2(D)))z`.                   (5.2)

By (3.9), `||e||<||z||/2`. Suppose two of the four banks obeyed

`||v_{K_r}||<||z||/8`.                                          (5.3)

Then on each such bank

`||e_{K_r}||
 >=||z_{K_r}||-||v_{K_r}||
 >(sqrt(139)/24-1/8)||z||.`                                     (5.4)

The exact inequality

`sqrt(139)/24-1/8 >1/(2sqrt(2))`                                (5.5)

then makes two such banks contribute more than `||z||^2/4` to `||e||^2`, contradicting `||e||^2<||z||^2/4`.

Hence at least three of the four disjoint physical banks satisfy

`||v_{K_r}||_2 >=||z||_2/8.`                                    (5.6)

Normalizing `u=v/||v||` (nonzero because `||e||<||z||`) and using `||v||<=||z||` gives

`boxed:
 u in V_2(D), ||u||_2=1,
 and on at least three pairwise-disjoint ORIGINAL-coordinate banks K_r,
 ||u_{K_r}||_2 >=1/8.
}`                                                                (5.7)

Call this `QFORM-ROWAWARE-RELATIVE-ALIGNMENT-THREEBANK-FOOTPRINT-v1`.

This is coefficient geometry only; it does not declare the singular-vector coordinate `u^T X` independent of anything. Its value is that the actual top-two right singular carrier of the literal child crossing must have macroscopic support on three disjoint product banks.

## 6. New exhaustive B08 router in the edge-capped diffuse survivor

Combining Sections 2--5 with the completed fleet02/B08 r35 router gives:

### `QFORM-EDGECAPPED-ROWAWARE-R2-ROUTER-v1`

In the diffuse selected-three chamber after the earlier scalar/edge payments, the r35 spectral/localized-row gates, and the benchmark branches already paid by the fleet, at least one of the following holds:

1. **new paid branch:**
   `||p_Q||_infinity <=665.986/L` and `p_Q in C_0(R)`;
2. **two-mode complementary cancellation:** for the literal deleted child crossing `D`, `s_2(D)<sigma L`, while the actual complementary crossing satisfies `s_2(C^-)>sigma L`;
3. **relative rank-two alignment:** `s_2(D)>=sigma L`, the physical star obeys `dist(z,V_2(D))<||z||/2`, there are sixteen disjoint physical star banks satisfying (4.2)-(4.3), and the actual carrier `V_2(D)` contains a unit vector with the three-bank footprint (5.7).

No easy subclass is substituted for the full target. The full universal conjecture and the full continuity conclusion remain OPEN.

The first unpaid implication is now

`QFORM-THREEBANK-R2-CARRIER-OR-DOUBLECANCEL-COMPILER-v1`:

pay either the rank-two carrier with a genuine three-bank physical footprint, or the two-mode complementary-cancellation branch, while retaining arbitrary same-bank child curvature, all complementary spectrum and all induced affine terms. Any receiver must continue to work in ORIGINAL independent coordinates; the carrier footprint is not permission to rotate the product law.

## 7. Integrity

The numerical decimals above evaluate exact rational/radical expressions only. No Monte Carlo or histogram is used as proof. No scheduler/task state, enabled/paused state, notification/email setting, permission, repository visibility, cross-account authentication, paid API/model setting or installation was changed. The run remains `WITHOUT_VERIFIED_BRAIN`.
