SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B10, 2026-09-22T21:51:05Z.
attacking: near-coloop product-provenance bridge via the partner two-bank paving, exact Schur-defect decomposition, and a boundary hyperbolic-square closure.

# fleet01/B10 QFORM r19 — two-bank Schur defect and an exact boundary closure

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** rank-three coupled case  
**Outcome:** `ESSENTIAL_STEP_APPLIED / NEW_SUPPORTING_THEOREM / TARGET_SUBBRANCH_CLOSED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and conditional end-to-end map

The full target remains open. This report works in the exact-rank-three near-coloop state produced by the completed null-bank compression theorem, after the nested-heavy residual branch has been removed. It keeps all independence in original-coordinate banks and does not assert independence of spectral projections.

The state is as follows. Write

`A=U M U^T`, `U^T U=I_3`,

where `M=M^T`, `sigma_min(M)>=1/2`, `|det M|>=1/2`. There is one genuine original independent cap-one coordinate `X_0` whose spectral row is

`u_0=sqrt(c) r`, `c>=7/9`, `||r||=1`, `r^T M r=0`.

For every complementary physical row write

`u_j=a_j r+v_j`, `v_j in r^perp`.

Parseval gives the exact identities

`sum_j a_j^2=rho:=1-c<=2/9`,
`sum_j v_j v_j^T=I_(r^perp)`,
`sum_j a_j v_j=0`.                                                (1.1)

After the completed residual-heavy closure one may assume

`||v_j||^2<=1/2` for all complementary rows.                       (1.2)

The designated partner fleet02/B10 r12 proves that the complement can then be partitioned into two disjoint original-coordinate banks `S,T` such that, in an orthonormal basis of `r^perp`,

`G_S=sum_(j in S)v_jv_j^T`, `G_T=sum_(j in T)v_jv_j^T=I_2-G_S`,

and

`delta I_2<=G_S,G_T<=(1-delta)I_2`, `delta=9/7168`.                (1.3)

The compact end-to-end implication proved here is:

1. attach to each bank an exact nonnegative scalar Schur defect `eta_B` measuring the part of its longitudinal leakage not linearly encoded by its transverse pair;
2. if both defects are positive, the two banks themselves form an exact-rank-three cross block and the completed cross-bank Plancherel theorem gives a continuous density bound, quantitatively

`||p_Q||_infinity <=3e [|det M| delta sqrt(eta_S eta_T)]^(-1/3)`;  (1.4)

3. if either defect is exactly zero, the corresponding bank's longitudinal leakage is a deterministic linear function of its transverse pair, so the completed fleet02/B10 hyperbolic-square theorem applies with genuine independence of `X_0` from that pair and gives the uniform target-level bound

`||p_Q||_infinity<=96`.                                           (1.5)

Thus the first unpaid implication is no longer the exact degeneracy itself. It is the punctured regime `eta_S eta_T>0` with one or both defects arbitrarily small, where (1.4) degenerates although the exact boundary is uniformly paid by (1.5).

## 2. Named partner consumed: residual two-bank paving

The completed designated partner is fleet02/B10 r12:

`yspennstate/math-open-problems@2045e39c5eda8d2a94098d79932223c77f2a4db7`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T204729Z-fleet02-B10-QFORM-r12/REPORT.md`.

Its theorem `QFORM-RESIDUAL-DIFFUSE-TWO-BANK-PAVING-v1` proves (1.3) from (1.2), using Pluecker edge weights. It also proves that each unwhitened transverse bank variable

`Y_B=sum_(j in B)v_j X_j in R^2`

has joint density cap

`||p_(Y_B)||_infinity <=2/sqrt(det G_B)<=2/sqrt(delta)`.            (2.1)

The banks `S,T` are disjoint sets of original coordinates and therefore genuinely independent as random vectors. Equation (1.3), rather than merely the existence of some partition, is used quantitatively in both new branches below.

## 3. Exact bank Schur-defect decomposition

For `B=S` or `T`, define

`rho_B=sum_(j in B)a_j^2`,
`b_B=sum_(j in B)a_j v_j in R^2`,

and the full three-dimensional spectral Gram matrix of the bank

`H_B=sum_(j in B)u_j u_j^T
    =[[rho_B,b_B^T],[b_B,G_B]]`                                    (3.1)

in the splitting `R r direct_sum r^perp`.

Since `G_B` is positive definite by (1.3), define

`q_B=G_B^(-1)b_B`,
`eta_B=rho_B-b_B^T G_B^(-1)b_B`.                                  (3.2)

### Lemma 3.1 — exact product-provenance defect

For each bank,

`eta_B>=0`,
`det H_B=det G_B * eta_B`.                                         (3.3)

Moreover if

`e_(B,j)=a_j-q_B dot v_j`,

then

`sum_(j in B)e_(B,j)v_j=0`,
`sum_(j in B)e_(B,j)^2=eta_B`.                                    (3.4)

Consequently the bank's longitudinal random form

`T_B=sum_(j in B)a_j X_j`

has the exact decomposition

`T_B=q_B dot Y_B+R_B`,
`R_B=sum_(j in B)e_(B,j)X_j`.                                     (3.5)

In particular

`eta_B=0  iff  R_B=0 identically`,                                (3.6)

so `eta_B=0` means precisely that the bank's longitudinal leakage is already a linear function of its two transverse product projections.

### Proof

The matrix `H_B` in (3.1) is a sum of rank-one positive semidefinite matrices, hence `H_B>=0`. Since `G_B>0`, its scalar Schur complement is nonnegative, proving `eta_B>=0`; the block determinant formula gives (3.3).

By the definition of `q_B`,

`sum e_(B,j)v_j=b_B-G_Bq_B=0`.

Also

`sum e_(B,j)^2
 =rho_B-2q_B^T b_B+q_B^T G_Bq_B
 =rho_B-b_B^TG_B^(-1)b_B=eta_B`.

Equation (3.5) is obtained by substituting `a_j=q_B dot v_j+e_(B,j)`. Finally a sum of squares is zero exactly when every `e_(B,j)=0`, proving (3.6). QED.

The global Parseval identities add

`rho_S+rho_T=rho`, `b_S+b_T=0`, `G_S+G_T=I_2`.                    (3.7)

Because `G_T=I-G_S`, the two transverse Gram matrices commute. Writing `b=b_S=-b_T`, one also has the exact identity

`eta_S+eta_T
 =rho-b^T(G_S^(-1)+G_T^(-1))b
 =rho-b^T(G_SG_T)^(-1)b >=0`.                                     (3.8)

No probability estimate is used in this section.

## 4. Positive-defect branch: the banks themselves expose rank three

Assume

`eta_S>0`, `eta_T>0`.                                               (4.1)

Then (3.3) implies both `H_S,H_T` are positive definite, hence each bank row matrix has spectral rank three. Let `U_S,U_T` denote the row matrices on those two original-coordinate banks. The physical cross block is

`C=A[S,T]=U_S M U_T^T`.                                            (4.2)

Take thin QR factorizations

`U_S=Q_S R_S`, `U_T=Q_T R_T`.

The nonzero singular values of `C` are those of the invertible `3x3` matrix `R_S M R_T^T`, and therefore their product is exactly

`Pi_3(C)
 =|det M| sqrt(det H_S det H_T)`
` =|det M| sqrt(det G_S det G_T eta_S eta_T)`
` >=|det M| delta sqrt(eta_S eta_T)`.                              (4.3)

The completed fleet03/B19 theorem `QFORM-EXACT-CROSS-RANK-L2-v1`, canonical source

`yspennstate/math-open-problems@f82fe367b06909082f94eda2b98f4a2fd2a5bb7c`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260922T172719Z-fleet03-B19-QFORM-r16/REPORT.md`,

applies to an exact-rank-three cross bank while allowing arbitrary same-bank quadratic terms, affine terms and conditioned outside couplings. It gives

`||p_Q||_infinity<=3e Pi_3(C)^(-1/3)`.                             (4.4)

Using (4.3),

`boxed{ ||p_Q||_infinity
 <=3e [|det M| delta sqrt(eta_S eta_T)]^(-1/3). }`                  (4.5)

This branch has a bounded continuous density because the source theorem proves an `L^1` characteristic-function majorant.

Equation (4.5) is not yet uniform as a defect tends to zero. The next section proves that the exact zero boundary is nevertheless uniformly paid, showing that this blow-up is a proof-interface loss rather than an actual singular endpoint.

## 5. Exact zero-defect branch: uniform closure by genuine independent scalar plus dependent pair

Assume, without loss of generality,

`eta_S=0`.                                                         (5.1)

By (3.6),

`T_S=q_S dot Y_S` exactly.                                         (5.2)

Condition on every original coordinate in the other bank `T`. This preserves the original independence of `X_0` from the whole bank `S`, and all terms from `T` become fixed affine shifts in the active variables.

Choose an orthonormal spectral basis `(r,e_1,e_2)` with

`M r=s e_1`, `s=||Mr||>=sigma_min(M)>=1/2`.

Since `r^TMr=0`, in this basis

`M=[[0,s,0],[s,d,g],[0,g,f]]`,                                    (5.3)

and direct expansion gives

`det M=-s^2 f`,                                                    (5.4)

so `f!=0`.

Write the transverse bank variable as

`Y_S=(V,W)`.

The spectral coordinate along `r` contributed by the active variables is

`sqrt(c) X_0+q_1V+q_2W+constant`.

Using (5.3), all dependence on `X_0` is therefore exactly

`2s sqrt(c) X_0 V`.                                                (5.5)

All terms produced by `q_1V+q_2W`, the residual quadratic block, and the conditioned bank are quadratic-affine functions of `(V,W)`. Because `f!=0`, completing only the `W` square rewrites the active conditional form as

`2s sqrt(c) X_0 V + F(V) + f (W+theta(V))^2 + constant`,           (5.6)

for measurable (indeed affine/quadratic) functions `F,theta`. The affine shear `(V,W)->(V,W+theta(V))` has determinant one and is already allowed directly by the hyperbolic-square theorem; no independence between `V` and `W` is needed.

By the partner paving bound (2.1),

`H:=||p_(V,W)||_infinity<=2/sqrt(delta)`.                          (5.7)

The scalar `X_0` has density cap `K<=1` and is genuinely independent of `(V,W)`. Apply fleet02/B10 r11, Lemma 2.1 `QFORM` scaled dependence-tolerant hyperbolic-square theorem, canonical source

`yspennstate/math-open-problems@11c9ae19edfd07e3a0bd4053a910667c20e721ab`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T130225Z-b10-qform-r11/REPORT.md`.

With `a=s sqrt(c)` and `b=f`, it gives

`||p_Q||_infinity
 <=3*2^(2/3) H^(2/3) |s sqrt(c)|^(-2/3)|f|^(-1/3)`
` <=3*2^(4/3) delta^(-1/3)c^(-1/3)(s^2|f|)^(-1/3)`
` =3*2^(4/3) delta^(-1/3)c^(-1/3)|det M|^(-1/3)`.                 (5.8)

Now use the exact constants from the compressed near-coloop state,

`delta=9/7168`, `c>=7/9`, `|det M|>=1/2`.

Then

`delta^(-1) c^(-1) |det M|^(-1)
 <=(7168/9)(9/7)2=2048`,

and (5.8) simplifies exactly to

`boxed{ ||p_Q||_infinity <=96. }`                                  (5.9)

The same proof applies if `eta_T=0`. Thus **every exact zero-Schur-defect bank produced by the partner paving is uniformly paid**, despite arbitrary overlap of its original coordinates between the longitudinal and transverse coefficient forms.

The source hyperbolic-square theorem supplies essential boundedness in this generality; this section does not claim a continuous representative.

## 6. Why this is not the refuted conditional-cap shortcut

The proof of (5.9) never replaces independence by a conditional density bound. At `eta_S=0`, the offending residual longitudinal random form literally vanishes by the coefficient identity (3.6). The only scalar fed into the hyperbolic-square theorem is the original independent coordinate `X_0`, while `(V,W)` is kept as one possibly dependent pair.

This is categorically different from trying to use `p_(X_0+T|V,W)<=1`, which fleet02/B10 r11 disproves as a sufficient interface. Likewise no arbitrary-joint coarea estimate, positive conditional-density moment, fiber supremum, uniform pointwise quadratic-phase decay, or uniformly good physical minor is used.

## 7. First essential missing implication after this run

The exact boundary `eta_B=0` is now paid by (5.9), and the interior `eta_S eta_T>0` has the quantitative continuous bound (4.5). The remaining gap is therefore the punctured stability problem

`QFORM-TWOBANK-POSITIVE-SCHUR-DEFECT-BRIDGE-v1`:

> In the near-coloop two-bank state (1.1)--(1.3), prove a universal density bound when `eta_S,eta_T>0`, uniformly as one or both defects tend to zero, using the original product provenance before any conditional supremum or reciprocal local determinant is paid.

The exact decomposition (3.5) shows the right object to retain. A normalized residual `R_B/sqrt(eta_B)` is a third coefficient direction orthogonal in coefficient space to the two whitened transverse directions, but small `eta_B` cannot simply be treated as a small random perturbation: cap-one input laws can have arbitrarily large support and no moment assumptions are available. Thus a valid bridge must use the joint product-linear geometry, not perturbative magnitude of the random variable.

A natural next mechanism is a **mixed two-scale Plancherel / hyperbolic-square estimate** that keeps `R_B` inside the bank amplitude until after the exact `X_0 V` and transverse-square smoothing have been integrated. The existing cross-rank-three theorem corresponds to paying `R_B` as a third full mixed direction and loses `eta_B^(-1/6)`; the boundary theorem corresponds to eliminating it algebraically. The missing estimate must interpolate these mechanisms without a law-uniform pointwise decay claim.

## 8. Status and regularity

Proved in this run:

- exact bank Schur-defect decomposition (3.1)--(3.6);
- a direct application of the completed designated partner fleet02/B10 r12 paving to expose two uniformly nondegenerate independent residual banks;
- the exact positive-defect cross-rank-three inequality (4.5), with a continuous density in that branch;
- the new zero-defect closure `||p_Q||_infinity<=96`, valid for arbitrary product-origin overlap allowed by `eta_B=0`.

Not proved:

- a uniform bound through the punctured `eta_B downarrow0` regime;
- arbitrary exact-rank-three orientation in full;
- arbitrary additional spectrum;
- the full owner conjecture.

**Full QFORM target: OPEN / NOT PROVED / NOT DISPROVED.**
