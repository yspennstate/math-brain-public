SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-24T06:15:15Z.
attacking: the operator-selected overlap-two tiny-pair branch by splitting its complete Schur-numerator packet into transverse physical pair-E3 currency versus a genuinely low-rank/singular collar.

# account03/B04 r51 — overlap-two transverse promotion to pair-anchored E3

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Product Fourier rearrangement  
Run: `20260924T061515Z-account03-B04-QFORM-auto11-r51`  
Control: OWNER CONTROL revision `2026-09-22.15`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING COMPILER / OPERATOR-H2 TRANSVERSE SUBBRANCH PAID CONTINUOUSLY / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.

The unrestricted conjecture is not proved or disproved here. Every random variable remains an ORIGINAL independent coordinate. No post-rotation independence, pointwise quadratic-phase decay, arbitrary-joint coarea estimate, moment/support hypothesis, deletion of a nonzero tail, or selection of a tiny reciprocal minor is used.

## 1. Fresh source-pinned frontier

Fresh `math-research-brain/main` was read at run start, together with `AGENTS.md`, the full owner message in `scheduled_tasks/README.md`, `fleet.json`, `roles.json`, `PROTOCOL.md`, and the QFORM shared manifest/current-research/claims/correction/memory/assignment files. OWNER CONTROL remains revision `2026-09-22.15`, QFORM is the sole target, and the full theorem remains OPEN.

The immediate analytic input from this slot is

`QFORM-PAIR-ANCHORED-E3-PROMOTION-v1`,

`yspennstate/math-open-problems@81a90afb15045c054702e4029d6016b82a16118b`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260924T051824Z-account03-B04-QFORM-auto11-r50/REPORT.md`.

For a literal original-coordinate cross block `N=A[I,J]`, a physical row pair `{a,b} subset I`, and

`K_ab=sum_{r notin {a,b}} det Gram(n_a,n_b,n_r)>0`,

it gives a continuous `C_0` density with

`||p_Q||_infinity <= C_E3 K_ab^(-1/6)`,

where

`C_E3=3*2^(5/6)=5.345392308842036...`.                    (1.1)

The structural input is account01/B07 r38,

`QFORM-C3-OVERLAP-OPERATOR-STAR-FUNNEL-v1`,

`yspennstate/math-open-problems@c897f02e56b6a62bacbed52b4fc3670f15f7b782`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/20260924T011014Z-account01-B07-qform-auto11-r38/REPORT.md`.

On its overlap-two operator branch it produces one literal physical pair `H` with

`W_H^(2)>=1/144`.                                                (1.2)

If `m_H=max{|A_ii|,|A_jj|,|A_ij|}>=1/64`, that source already pays the branch. Thus the live operator-H2 survivor has

`m_H<1/64,  W_H^(2)>=1/144`.                                    (1.3)

The point of this run is to show that a large part of (1.3) automatically promotes to the already-paid pair-anchored E3 Fourier receiver. The remainder is no longer an undifferentiated “tiny pair”; it is a precise rank-two star channel / near-rank-one collar.

## 2. Physical split of a fixed overlap-two packet

Fix a physical pair `H={h1,h2}`. For distinct outside coordinates `r,c`, set

`d_rc=det A[H union {r}, H union {c}]`,

and

`W_H^(2)=sum_{r!=c; r,c notin H} d_rc^2`.                         (2.1)

Independently colour every outside physical coordinate red or blue. A fixed ordered pair `(r,c)` lands with `r` red and `c` blue with probability `1/4`. Therefore there is a deterministic disjoint split of outside coordinates into `R,C` such that

`W:=sum_{r in R,c in C} d_rc^2 >= W_H^(2)/4`.                    (2.2)

Write the corresponding coefficient blocks

`B=A[H,H]`, `delta=det B`,
`V=A[R,H]`, `U=A[H,C]`, `M=A[R,C]`.                              (2.3)

The bordered determinant identity gives the COMPLETE split packet as

`D:=delta M - V adj(B) U`,

`boxed: W=||D||_F^2.`                                            (2.4)

No inverse has been introduced.

Let `P_U` be the orthogonal projection in `R^C` onto `row(U)`, and `P_V` the orthogonal projection in `R^R` onto `col(V)`. Put

`D_00=P_V D P_U`,
`T=||D-D_00||_F^2`.                                              (2.5)

The central part `D_00` has rank at most two. The transverse packet `T` is the part of the overlap-two Schur numerator that genuinely escapes the two pair-to-leaf star spaces.

## 3. Exact transverse identities

Because `U(I-P_U)=0`, the low-rank bordered term disappears on the right transverse space:

`D(I-P_U)=delta M(I-P_U)`.                                       (3.1)

Similarly,

`(I-P_V)D=delta (I-P_V)M`.                                       (3.2)

Define

`R_U=||D(I-P_U)||_F^2`,
`R_V=||(I-P_V)D||_F^2`.                                         (3.3)

The four mutually orthogonal Frobenius blocks determined by `P_V` and `P_U` show

`R_U+R_V
 =T+||(I-P_V)D(I-P_U)||_F^2
 >=T`.                                                           (3.4)

Hence if

`T>=W/2`,                                                        (3.5)

then at least one of

`R_U>=W/4`,  `R_V>=W/4`                                         (3.6)

holds.

Now define the two physical pair-to-leaf areas

`Delta_U=det(UU^T)>=0`,
`Delta_V=det(V^T V)>=0`.                                        (3.7)

Consider the literal disjoint cross block

`N_U=A[H union R,C]=[U;M]`.                                     (3.8)

The pair-anchored third-volume mass of its first two physical rows is, by the Gram height identity,

`K_U
 =sum_{r in R} det Gram(U_row1,U_row2,M_r)
 =Delta_U ||M(I-P_U)||_F^2`.                                    (3.9)

If `delta!=0`, (3.1) gives the exact aggregate-before-reciprocal identity

`boxed: K_U=(Delta_U/delta^2) R_U.`                              (3.10)

The transposed literal cross block `A[H union C,R]=[V^T;M^T]` similarly has pair-anchored E3 mass

`boxed: K_V=(Delta_V/delta^2) R_V.`                              (3.11)

Equations (3.10)-(3.11) are the new bridge. The entire overlap-two packet is aggregated first; only the dimensionless area ratio `Delta/delta^2` remains. No individual `3x3` determinant is inverted.

## 4. Main theorem — `QFORM-OMEGA2-TRANSVERSE-PAIR-E3-PROMOTION-v1`

Assume `delta!=0`. Take a physical split satisfying (2.2). If

`T>=W/2`                                                         (4.1)

and, for one side `sigma in {U,V}` obeying `R_sigma>=W/4`,

`Delta_sigma>=delta^2`,                                         (4.2)

then the FULL ambient quadratic form has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= C_E3 (W/4)^(-1/6)
 <= C_E3 (W_H^(2)/16)^(-1/6).
`                                                                 (4.3)

### Proof

If the active side is `U`, (3.10), (3.6) and (4.2) give

`K_U >=R_U>=W/4`.                                                (4.4)

The block `N_U` is a literal cross block between disjoint ORIGINAL-coordinate banks. Apply `QFORM-PAIR-ANCHORED-E3-PROMOTION-v1` to its first two physical rows. This gives (4.3) and a continuous `C_0` density. The `V` branch is identical after transposition. QED.

### Operator-H2 numerical consequence

On the account01/B07 operator-selected branch (1.2), `W>=1/576`. Therefore any state satisfying (4.1)-(4.2) obeys

`K_sigma>=1/2304`,                                               (4.5)

and hence

`boxed:
 ||p_Q||_infinity
 <=3*2^(5/6)*2304^(1/6)
 =2^(13/6) 3^(4/3)
 =19.4264448823268... .
`                                                                 (4.6)

This is a continuous-density payment, substantially stronger in regularity than the existing fixed-pair all-sign endpoint, which asserted only essential boundedness.

## 5. What exactly survives

The new theorem does NOT claim that every operator-H2 pair is paid. It sharpens the remaining state to a concrete collar.

For a split with (2.2), if (4.3) cannot be invoked, then at least one of the following holds:

1. **central two-star channel:**

   `||P_V D P_U||_F^2>W/2`;                                     (5.1)

2. **right near-rank-one star:** `R_U>=W/4` but

   `Delta_U<delta^2`;                                           (5.2)

3. **left near-rank-one star:** `R_V>=W/4` but

   `Delta_V<delta^2`;                                           (5.3)

4. **exact singular pair:** `delta=0`.                           (5.4)

In (5.1), `P_VDP_U` has rank at most two. Since on the live operator branch `W>=1/576`, (5.1) implies

`||P_VDP_U||_F>1/(24 sqrt(2))`

and therefore, by rank at most two,

`boxed: ||P_VDP_U||_op>1/48.`                                   (5.5)

So the central survivor carries a fixed-strength rank-at-most-two physical star channel.

On the tiny-pair branch `m_H<1/64`,

`|delta|=|A_h1h1 A_h2h2-A_h1h2^2|<=2m_H^2<1/2048`.              (5.6)

Hence (5.2), for example, forces

`s_1(U)s_2(U)=sqrt(Delta_U)<|delta|<1/2048`,                     (5.7)

and similarly for `V`. Thus the unpaid transverse survivor is quantitatively a near-rank-one pair-to-leaf star, not merely a small physical pair.

This is exactly the collar geometry isolated independently by the fleet's singular-pair work. No small coefficient matrix is discarded here.

## 6. Designated account04/B04 partner applied at an actual inequality

The completed designated partner is account04/B04 r2,

`yspennstate/math-open-problems@4a54666abf2316bb79b939cef3ea940605a0af57`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B04/20260924T001353Z-account04-B04-QFORM-r2/REPORT.md`.

Its double-anchor branch produces, on one literal fourth-volume cross block, a physical row pair `{a,b}` satisfying

`H_ab^(4)>(2/75) E_4(M)`.                                       (6.1)

For that same pair, write `D_2=det Gram(m_a,m_b)` and let `C` be the residual row block projected off the pair. Then

`H_ab^(4)=D_2 e_2(CC^T)`,
`K_ab=D_2 e_1(CC^T)`.                                           (6.2)

The Newton inequality `e_1^2>=2e_2` gives the actual quantitative bridge

`K_ab^2
 >=2D_2 H_ab^(4)
 >(4/75)D_2 E_4(M)`.                                            (6.3)

Applying this slot's completed pair-E3 theorem (1.1) yields

`boxed:
 ||p_Q||_infinity
 <6.824377206888847 [D_2 E_4(M)]^(-1/12),
`                                                                 (6.4)

with a continuous `C_0` density. This is an equation-level use of the designated partner result on its proved scope; no new assumption is inserted.

## 7. Genuinely rotated indefinite stress test

Let

`epsilon=1/128`,

`B=epsilon [[1,1/2],[1/2,-1]]`,

so

`delta=det B=-5/65536`,  `m_H=1/128<1/64`.                       (7.1)

Take the dense orthogonal matrix

`O=(1/7) [[6,-2,-3],[-2,3,-6],[-3,-6,-2]]`,                    (7.2)

and set

`N=diag(2,2,4096/5) O`.                                         (7.3)

On six original coordinates, with left bank `{0,1,2}` and right bank `{3,4,5}`, define

`A_*=[[L,N],[N^T,0_3]]`,

where

`L=[[B,0],[0,0]]`.                                               (7.4)

Every entry of the cross block `N` is nonzero. Its singular values are exactly

`2,2,4096/5`.                                                    (7.5)

The pure-cross matrix `[[0,N],[N^T,0]]` therefore has eigenvalues

`+-2, +-2, +-(4096/5)`.                                         (7.6)

The perturbation `L` has operator norm `sqrt(5)/256<0.009`, so Weyl gives all six eigenvalues of `A_*` absolute value greater than `2-sqrt(5)/256>1` except the huge pair, which is even farther from zero. Thus the example is target-valid, indefinite, and genuinely non-diagonal in the independent coordinates.

Take `H={0,1}`, `R={2}`, `C={3,4,5}`. Here

`V=0`,
`U=2*(first two rows of O)`,
`M=(4096/5)*(third row of O)`.                                   (7.7)

Orthogonality of `O` gives

`Delta_U=det(UU^T)=16`,
`||M||_2^2=16777216/25`,
`M(I-P_U)=M`.                                                    (7.8)

Moreover

`D=delta M`,
`W=||D||_F^2=1/256`,
`T=W`,                                                           (7.9)

and

`K_U=Delta_U ||M||_2^2
 =268435456/25`.                                                 (7.10)

Thus the new promotion theorem applies very far from its threshold and gives

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=3*2^(5/6) (268435456/25)^(-1/6)
 =0.3598843319374658... .
`                                                                 (7.11)

The complete fixed-pair overlap-two mass for `H` is

`W_H^(2)=7031/702464=0.0100090538447...>1/144`,                  (7.12)

so the same matrix also lies inside the operator-H2 scale rather than merely illustrating an unrelated local theorem.

All identities in (7.1)-(7.12), the orthogonality of `O`, and the spectrum margin were checked deterministically; no Monte Carlo histogram is used.

## 8. Status and next implication

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains OPEN.

This run removes the generic transverse part of the operator-selected overlap-two tiny-pair branch. The first B04 debt is now

`QFORM-OMEGA2-CENTRAL-R2-STAR-OR-RANKONE-COLLAR-ENDPOINT-v1`:

> Starting from `W_H^(2)>=1/144`, `m_H<1/64`, and the physical split above, spend either the fixed-strength central rank-at-most-two channel `||P_VDP_U||op>1/48`, the active-side near-rank-one condition `s_1(U)s_2(U)<|delta|` / transpose, or the exact `delta=0` collar, while retaining arbitrary same-leaf curvature. The acceptable exits are the completed singular-star, grouped-hub, ridge, square-hyperbola or physical crossing receivers. Do not delete a near-rank-one coefficient tail or condition on a projection fiber with an unproved density cap.

The completed account02/B09 singular-pair work shows that the exact rank-one collinear star with zero active leaf curvature is already paid; its remaining debt is precisely arbitrary same-leaf curvature. The present theorem reaches that collar from the global third-compound operator funnel without a dimension-dependent single-minor extraction.

No scheduler state, task identity, email/push notification, public-release, paid-model/API, repository visibility, or cross-account authentication state was changed.
