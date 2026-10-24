SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T05:42:56Z.
attacking: mixed-hub smoothing for a source-coordinate star with dense same-side couplings; convert the partner small-disjointness rank split into a genuine physical bilinear wedge and a direct O(interval length) estimate without square-root decoupling.

# account02/B09 auto11 — k=1 rank-split torsion becomes a physical two-hub wedge

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / complementary constructions and source-valid counterexamples  
Status: **ESSENTIAL_STEP_APPLIED / NEW RANKSPLIT PAYMENT / REQUIRED SOURCE APPLIED / FULL TARGET OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains **OPEN**. This report does not claim that the spectral hypothesis automatically forces the new torsion or an exact-zero physical hub pair. It proves a source-coordinate implication inside the newest account03/B09 rank-split survivor and reduces the failed endpoint to an explicit coefficient-space degeneracy or a genuinely nonzero physical core that must retain the external third spectral resource.

No moments, compact support, connected support, log-concavity, identical laws, Gaussianity, independence after rotation, law-uniform pointwise stationary phase, arbitrary-joint coarea, worst conditional projection-density supremum, or small-random-error argument is used.

## 1. First unpaid implication, stated before the proof

The latest completed designated-partner result is account03/B09 r24,

`QFORM-PLUCKER-SMALLRHO-RANKSPLIT-v1`,

source

`yspennstate/math-open-problems@9fcac412f233f09c6ee5e8a1140207d596cce8a2`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T045157Z-account03-B09-QFORM-r24/REPORT.md`.

For a whitened three-dimensional active mixed frame, its small-disjointness branch gives a physical triple `S` and one of three literal original-coordinate alternatives: `k=3` three-core, `k=2` two-core plus a disjoint outside line, or `k=1` one-core plus a disjoint outside plane. At the concrete scale `eta=1/16`, the core singular values are at least `sqrt(15/16)` and the outside line/plane singular values are greater than `1/4`.

The first B09 debt is therefore `QFORM-RANKSPLIT-PHYSICAL-PAYMENT-v1`: turn those aggregate coefficient-space ranks into a source-coordinate anti-concentration theorem while arbitrary same-bank residual quadratic curvature remains present. The present report proves the following genuine part of the `k=1` branch:

> if the partner outside plane has quantitative coefficient-space torsion relative to the hub/curvature packet, then one of the three physical core leaves has a quantitative two-row wedge to the outside bank; if that leaf and the physical hub have exact zero `2 x 2` core, the previously completed zero-hubpair theorem immediately yields a direct linear small-ball bound while **all** complementary quadratic curvature remains arbitrary.

What remains after this run is the small-torsion/invariant-plane endpoint and the genuinely nonzero/near-null physical two-hub core. Those cases cannot be obtained by declaring their coefficients small on arbitrary unbounded product inputs.

## 2. Sources actually used at equations

Fresh owner control remained QFORM-only, OWNER CONTROL revision `2026-09-22.15`. The required newest-Claude directory was read at the requested source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The later compatible continuation of `RESULTS.md` was also read through commit `7ffd1ed79398611eb06752f622be0ce33dcacb5a`; it adds the proved `n=3` and pivot reductions but still leaves the no-pivot problem open. Theorem H from this package is applied to a new actual target inequality in Section 7.

The analytic endpoint used below is this worker's completed

`QFORM-ZERO-HUBPAIR-ARBITRARY-REMAINDER-v1`,

source

`yspennstate/math-open-problems@03ec6ccf1de2e2544e850cbda25d460aacae6a1b`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T024331Z-account02-B09-QFORM-auto12/REPORT.md`.

For two original physical coordinates `{h,s}` with

`A_hh=A_ss=A_hs=0`

and full complementary coupling rows `u,v`, it proves, with **arbitrary** dense complementary symmetric block and affine terms,

`||p_Q||_infinity <=2sqrt(2)
 [||u||^2||v||^2-<u,v>^2]^(-1/4)`,                       (2.1)

and the identical coefficient multiplies every interval length. Its proof conditions only on the complementary original-coordinate bank and uses conditional linear anti-concentration; there is no probability squaring.

## 3. Mixed-hub coefficient geometry

Split the original coordinates as one physical hub `{h}`, a leaf bank `I`, and an arbitrary further bank `J`. After conditioning `J`, allow all generated affine terms. Assume the **exact** leaf principal block is

`A_II=D+lambda_1 v_1v_1^T+lambda_2v_2v_2^T`,                 (3.1)

where `D` is diagonal and `lambda_1 lambda_2 !=0`. Put

`c=A[I,h]`,
`W=[v_1,v_2,c]`,
`G=W^T W`,                                                     (3.2)

and assume `G>0`. Whiten only the coefficient frame, not the random vector:

`U=W G^(-1/2)`, so `U^TU=I_3`.                               (3.3)

Write the physical rows of `U` as `u_i^T`. Define

`L=diag(lambda_1,lambda_2,0)`,
`K=G^(1/2)L G^(1/2)`,
`q=G^(1/2)e_3`.                                                (3.4)

Because `W=U G^(1/2)`, for distinct physical leaves `i,j`, the diagonal twist `D` contributes nothing and

`A_ij=u_i^T K u_j`,                                           (3.5)

while the actual physical hub edge is

`A_hj=u_j^T q`.                                                (3.6)

Thus (3.5)-(3.6) are identities among **original physical coefficients**. No whitened coordinate is declared independent.

Fix a physical triple `S subset I`, put `T=I\S`, and let

`R_T=U_T^T U_T`.                                               (3.7)

Assume this triple is in the partner's `k=1` rank-split branch. Thus there is a unit vector `f`, with `H=f^perp`, such that

`R_T f=mu f`, `0<=mu<=eta`,                                   (3.8)

and

`R_T|_H >= eta I_H`.                                          (3.9)

For the partner's standard quantitative choice, `eta=1/16`.

## 4. New theorem: torsion-to-physical-wedge extraction

For `i in S`, take the actual cross rows from the physical pair `(i,h)` to the disjoint physical bank `T`:

`a_i=(A_ij)_(j in T)=U_T K u_i`,
`b=(A_hj)_(j in T)=U_T q`.                                    (4.1)

Define their wedge currency

`Delta_i(T)=||a_i||^2||b||^2-<a_i,b>^2`.                      (4.2)

The coefficient-space scalar that decides whether the outside plane is genuinely seen by this bilinear pair is

`Theta=|det(f,Kf,q)|`.                                         (4.3)

### Theorem `QFORM-K1-TORSION-TO-PHYSICAL-WEDGE-v1`

Under (3.8)-(3.9), at least one physical leaf `i in S` satisfies

`boxed:
Delta_i(T) >= [eta^2(1-eta)/3] Theta^2.`                       (4.4)

### Proof

For fixed `i`, the `2 x 2` Gram matrix of the two rows in (4.1) is

`B_i^T R_T B_i`, where `B_i=[K u_i,q]`.                        (4.5)

From (3.9), as a positive-semidefinite operator on coefficient space,

`R_T>=eta P_H`.                                                (4.6)

Hence

`B_i^T R_T B_i >= eta B_i^T P_H B_i`.                         (4.7)

For positive `2 x 2` matrices determinant is monotone under Loewner order, so

`Delta_i(T)
 >=eta^2 det(B_i^T P_H B_i)`.                                 (4.8)

Since `H=f^perp` is two-dimensional, the projected area identity gives

`det(B_i^T P_H B_i)=det(f,K u_i,q)^2`.                         (4.9)

Now put

`z=K(q cross f)`.                                              (4.10)

The scalar triple product is linear in the physical row:

`det(f,K u_i,q)=u_i^T z`.                                     (4.11)

Because the rows form a tight frame,

`sum_(i in S) det(f,K u_i,q)^2
 =z^T U_S^T U_S z
 =z^T(I-R_T)z`.                                                (4.12)

The splitting `span(f) direct_sum H` is spectral for `R_T`. By (3.8), `I-R_T` is at least `1-eta` on `span(f)` and is positive semidefinite on `H`. Therefore

`z^T(I-R_T)z
 >=(1-eta)|f^Tz|^2
 =(1-eta)|det(f,Kf,q)|^2
 =(1-eta)Theta^2`.                                             (4.13)

There are three physical leaves in `S`, so one of them has square at least one third of (4.13). Combining with (4.8)-(4.9) proves (4.4). QED.

This proof spends the partner's aggregate outside two-volume **before** selecting a physical leaf. The selected row appears only after the sum identity (4.12), so there is no reciprocal-small-minor loss.

## 5. New density consequence: the exact-zero two-hub endpoint of `k=1`

Let `i in S` be the leaf supplied by Theorem 4. Suppose its physical `2 x 2` core with the hub is exactly zero:

`A_hh=A_ii=A_hi=0`.                                           (5.1)

Let `Delta_full` denote the full two-row wedge from `(i,h)` to **all** remaining physical coordinates. Restricting those rows to `T` gives the Gram matrix in (4.5); adding the other complementary coordinates adds a positive-semidefinite `2 x 2` Gram contribution. Therefore

`Delta_full>=Delta_i(T)`.                                     (5.2)

Apply the source-pinned zero-hubpair theorem (2.1). From (4.4)-(5.2),

`boxed:
||p_Q||_infinity
 <=2sqrt(2) 3^(1/4)
   eta^(-1/2)(1-eta)^(-1/4)|Theta|^(-1/2).`                   (5.3)

Every interval `L` satisfies

`boxed:
P{Q in L}
 <=2sqrt(2) 3^(1/4)
   eta^(-1/2)(1-eta)^(-1/4)|Theta|^(-1/2)|L|.`                (5.4)

At `eta=1/16`, the numerical prefactor before `|Theta|^(-1/2)` is

`15.131865744... <15.132`.                                    (5.5)

The crucial scope is the arbitrary remainder: once (5.1) holds, **every** quadratic coefficient among the remaining coordinates, including dense same-side curvature and all conditioning-generated affine terms, remains inside the arbitrary `H(X_K)` of the zero-hubpair theorem. No residual quadratic operator is discarded or declared small.

There is no Cauchy-Schwarz probability squaring, so this is directly an `O(|L|)` small-ball estimate rather than an `O(sqrt(|L|))` estimate.

## 6. Target-valid exact `k=1` packet and retained dense curvature

The extraction is nonvacuous and has a clean source-coordinate model. In coefficient space let

`f=(e_1+e_2)/sqrt(2)`,
`g=(e_1-e_2)/sqrt(2)`.                                        (6.1)

Use five physical leaf rows

`u_i=f`,
`u_1=u_2=g/sqrt(2)`,
`u_3=u_4=e_3/sqrt(2)`.                                        (6.2)

They form an orthonormal three-frame. Take

`G=I`, `lambda_1=1`, `lambda_2=-1`,                           (6.3)

and use the third column as the physical hub slope. Then

`A_hh=A_ii=A_hi=0`.                                           (6.4)

The cross row from `i` to `u_1,u_2` has entries `1/sqrt(2),1/sqrt(2)` and the hub cross row to `u_3,u_4` has the same two entries on the disjoint support. Thus

`Delta_full=1`.                                                (6.5)

The exact zero-hubpair theorem gives the sharper instance-specific inequality

`boxed: ||p_Q||_infinity <=2sqrt(2)<2.829.`                    (6.6)

The active grouped coefficient matrix has eigenvalues

`{1,-1,1,-1}`.                                                 (6.7)

To make the retained same-side curvature visibly dense without changing this packet, adjoin a disjoint original-coordinate bank `Z` and any dense rank-one square `<w,Z>^2` with `||w||_2=1`. The full matrix then has nonzero spectrum containing

`{1,-1,1,-1,1}`,                                               (6.8)

so it is a literal target matrix. The entire dense square lies in the arbitrary complementary remainder of (2.1), and (6.6) is unchanged. More generally the analytic estimate permits an arbitrary symmetric operator on the complement; the rank-one choice in (6.8) only makes the target spectrum transparent.

For (6.2), the outside covariance is exactly zero on `f` and equals `1/2` on `f^perp`, so this is an exact partner `k=1` endpoint. Also `Theta=1`.

## 7. Required newest-Claude result applied to a distinct real target inequality

The newest-Claude Theorem H is not merely cited. Let `m=2^r>=8`, let `Y` be an `m`-coordinate original product bank, and choose four orthonormal flat Walsh vectors

`c,v_1,v_2,v_3`,                                              (7.1)

all with entries of magnitude `m^(-1/2)`. With one disjoint physical hub `X_h`, define

`F_m=2X_h<c,Y>
    +<v_1,Y>^2+<v_2,Y>^2-<v_3,Y>^2`.                          (7.2)

This is an actual source-coordinate star with a dense rank-three same-side operator. In the grouped orthonormal basis `(e_h,c,v_1,v_2,v_3)`, its nonzero spectrum is

`{1,-1,1,1,-1}`,                                               (7.3)

so it satisfies the full target spectral hypothesis.

For Theorem H, the augmented rows are

`rho_i=((v_1)_i,(v_2)_i,(v_3)_i,c_i)`.                        (7.4)

Their Gram matrix is `I_4` and every normalized leverage equals `4/m<=1/2`. With one hub and three Fresnel directions, Theorem H gives

`|phi_F(t)|
 <=(2|t|)^(-1)(4pi|t|)^(-3/2)(4pi)^4
 =16 pi^(5/2)|t|^(-5/2)`.                                    (7.5)

Integrating `min(1,16pi^(5/2)|t|^(-5/2))` exactly and applying Fourier inversion gives

`boxed:
||p_(F_m)||_infinity
 <=(5/3)2^(8/5)
 =5.052388555... .`                                           (7.6)

Hence

`boxed: P{F_m in L}<=5.053 |L|}`                              (7.7)

for every interval and every admissible collection of independent cap-one input laws. Theorem H also allows a diagonal leaf twist and arbitrary conditioned outside blocks at its exact stated scope. This is a distinct r=3 dense-same-side application of the required source, not a repetition of the previous r=2 Walsh packet.

## 8. Why a nonzero physical core cannot be deleted: source-valid obstruction

A tempting but false extension of (2.1) is that a quantitative two-row cross wedge alone should control an arbitrary nonzero physical `2 x 2` hub core. The obstruction is exact.

Let `X,Y,U,V` be independent `Uniform[-1/2,1/2]` and set

`R=(X+U)^2-(Y-V)^2`.                                          (8.1)

Viewed with physical hubs `(X,Y)` and complement `(U,V)`, the cross map is the identity, so its two-row wedge is exactly one. The physical hub core is `diag(1,-1)`, while the complementary curvature is `diag(1,-1)` and exactly aligns the critical values.

Put `S=X+U`, `T=Y-V`. Then `S,T` are independent triangular variables and each density is at least `1/2` on `[-1/2,1/2]`. With

`r=S-T`, `w=S+T`,                                              (8.2)

the joint density of `(r,w)` is at least `1/8` on `[-1/2,1/2]^2`, and

`R=rw`.                                                        (8.3)

Therefore, for sufficiently small `0<|z|`,

`p_R(z)
 >=(1/8) integral_(2|z|)^(1/2) dr/r
 =(1/8) log(1/(4|z|))`,                                       (8.4)

so the density is logarithmically unbounded.

This is **not** a QFORM counterexample: the coefficient matrix of (8.1) has only the two nonzero eigenvalues `2,-2`. It proves the exact logical point needed here: once the physical hub core is nonzero, the outside quadratic operator can cancel the apparent cross-wedge smoothing down to a rank-two lightcone. A target proof must spend the third spectral direction rather than perturbatively delete the hub core.

## 9. Correct degeneracy statement and next B09 obligation

The substantive checkpoint for this run included one over-strong wording, corrected immutably in `CORRECTION.md`. The theorem itself is unaffected. The universally correct degeneracy condition is simply

`Theta=|det(f,Kf,q)|=0`.                                       (9.1)

If `f` and `q` are linearly independent, (9.1) is equivalent to

`Kf in span(f,q)`.                                             (9.2)

If `q` is parallel to `f`, then `Theta=0` automatically and this is a separate hub-slope degeneracy; (9.2) need not follow.

The first unpaid implication is now

`QFORM-K1-INVARIANTPLANE-OR-NEARNULL-CORE-v1`:

> Starting from the partner `k=1` rank split, either obtain a quantitative torsion and an exact-zero physical pair, as paid in (5.3), or keep the third target direction explicitly through the `Theta`-small invariant-plane / `q parallel f` geometry and through the genuinely nonzero or near-null physical two-hub core. Do not treat the latter coefficients as a small random perturbation. In parallel, the partner `k=2` outside-line and `k=3` finite-core branches still require product-preserving payment; the updated `n=3` theorem is usable only when an actual physical three-coordinate principal block has a quantitative three-eigenvalue gap, which the aggregate rank split alone does not assert.

This narrows the partner's `k=1` outside-plane debt from an arbitrary high-dimensional curvature interaction to one explicit scalar torsion plus a near-null physical-core interpolation.

## 10. Scope and review status

The full QFORM conjecture remains **OPEN**. Full-target continuity remains **OPEN**. The new zero-core torsion branch has the bounded continuous density inherited from `QFORM-ZERO-HUBPAIR-ARBITRARY-REMAINDER-v1`; the newest-Claude Fourier branch in Section 7 also has a continuous density because its characteristic function is integrable.

The new theorem has not received the two independent end-to-end reviews required of a full candidate. It is a supporting implication only.
