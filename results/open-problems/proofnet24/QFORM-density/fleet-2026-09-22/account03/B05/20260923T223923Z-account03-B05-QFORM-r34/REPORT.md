SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B05, 2026-09-23T22:39:23Z.
attacking: QFORM-HEAVY-PLUECKER-ENDPOINT-RECEIVER-v1 — bypass the r33 near-rank-one/bi-star endpoint by splitting both scalar product banks across one exact rank-three physical crossing.

# account03/B05 r34 — Schur-factor three-volume crossing by splitting both scalar banks

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: quadratic coarea / equivalent interval bound with original-product provenance  
Startup control: `yspennstate/math-research-brain@55c83b4ecbd8234367b84a1abdc8511acec25165`  
Prepublication control observed before this report: OWNER CONTROL revision `2026-09-22.15`, QFORM-only  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING PRODUCT-PRESERVING DENSITY THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Continuity: proved on the new exact-cross branch; not supplied by the designated exact-slope partner branch; full-target continuity remains open.

## 1. Premises and correction discipline

The live ratio-packet normal form is from

`yspennstate/math-open-problems@b0299facc04ea0c03276dddb1a12c027aed5a946`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260923T033640Z-account01-B05-QFORM-r26/REPORT.md`.

The determinant-sensitive exact-rank-three crossing argument used below is the product-preserving theorem proved/refined in

`yspennstate/math-open-problems@95f94696393b5ad8b0def71fa0d93082de92bd85`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T193756Z-account03-B05-QFORM-r31/REPORT.md`,

with the underlying exact-cross theorem at

`yspennstate/math-open-problems@51d2edb29d7a4c150e4d47ed3a6685875a8483ae`

`proofnet24/QFORM-density/interactive/20260923T194300Z-exact-cross-rank-fourier/REPORT.md`.

The designated partner result actually applied below is

`yspennstate/math-open-problems@59c6ff7db9aceb8b575abe0e064ebeda06f6f77f`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B05/20260923T041255Z-account04-B05-dominant-slope-r2/REPORT.md`,

which proves

`||p_Q||_infinity < 51.6 (mu m_*)^(-1/3)`

when an exact physical slope class in the first bank has `u`-mass `m_*>0`.

The predecessor r33 is

`yspennstate/math-open-problems@6167097dbe623155ea2f0a7796f7dfb41957a69a`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T214237Z-account03-B05-QFORM-r33/REPORT.md`.

The present argument respects the live corrections. In particular it does **not** use an arbitrary-joint coarea inequality, a conditional projection-density moment, post-rotation independence, a pointwise van-der-Corput estimate, a fiber supremum, deletion of small coefficient tails, or selection/inversion of one small physical minor. All independence below comes from partitions of the original independent coordinates.

## 2. Live ratio packet and physical provenance

After conditioning only original coordinates outside the three active product banks, write

`V=(S,R)^T = Gamma^T X`, with `Gamma^T Gamma=I_2`,

and let two disjoint original-coordinate banks give normalized scalar projections

`Y=sum_j eta_j U_j`,  `sum_j eta_j^2=1`,

`Z=sum_k zeta_k W_k`, `sum_k zeta_k^2=1`.

The three source banks are mutually independent. The quadratic polynomial in `(S,R,Y,Z)` has homogeneous coefficient matrix

`H = [[C,P],[P^T,B]]`,

where `C,P,B` are real `2 x 2`, `B` is invertible, and the ratio-packet Schur identity is

`C-P B^(-1) P^T = lambda m e_1 e_1^T`.                    (2.1)

Put

`L=lambda m`,  `mu=|det B| |lambda|`.

Thus

`|L det B|=mu m`.                                             (2.2)

For the first bank, write the physical rows of `Gamma` as

`g_i=(xi_i,rho_i)`,

so

`sum_i g_i g_i^T=I_2`, in particular `sum_i xi_i^2=1`.        (2.3)

In the ratio construction, `xi_i=u_i/sqrt(m)` on the packet. This relation will be used only in the exact-slope alternative.

The key idea of this run is to split **both** scalar source banks. Previous mixed-cross arguments kept all of `Y` on one side and all of `Z` on the other. That forced the crossing determinant to pay residual quantities such as `z_1 z_2`. Splitting the scalar source banks makes the Schur rank-one direction itself supply the third crossing dimension.

## 3. Exact Schur factorization

Set

`A=B^(-1)P^T`.

Define the `3 x 4` matrix

`K = [[1,0,0,0],
      [A_11,A_12,1,0],
      [A_21,A_22,0,1]]`,

and the invertible symmetric `3 x 3` matrix

`D=diag(L,B)`.

Then the Schur identity (2.1) gives the exact factorization

`boxed: H=K^T D K.`                                          (3.1)

Indeed for `v in R^2`, `w in R^2`,

`(v,w)^T H (v,w)
 = L v_1^2 +(w+B^(-1)P^T v)^T B (w+B^(-1)P^T v)`.

Consequently `rank H=3` whenever `L!=0` (the active `mu>0` packet), and

`boxed: |det D|=mu m.`                                       (3.2)

This factorization is the correct place to aggregate before selecting a physical minor.

## 4. Arbitrary physical cut and its exact rank-three volume

Partition the first packet coordinates into `I` and `J`. Partition the original coordinates supporting `Y` into `Y_L,Y_R`, and those supporting `Z` into `Z_L,Z_R`. Define

`s_I=sum_(i in I) xi_i^2`, `s_J=1-s_I`,

`y_L^2=sum_(j in Y_L) eta_j^2`, `y_R^2=1-y_L^2`,

`z_L^2=sum_(k in Z_L) zeta_k^2`, `z_R^2=1-z_L^2`.             (4.1)

Let

`G_I=sum_(i in I) g_i g_i^T`, `G_J=I_2-G_I`.                  (4.2)

The physical coefficient rows, viewed in the latent coordinates `(S,R,Y,Z)`, are

- `(g_i,0,0)` for a first-bank coordinate,
- `(0,0,eta_j,0)` for a `Y`-source coordinate,
- `(0,0,0,zeta_k)` for a `Z`-source coordinate.

Put all `I,Y_L,Z_L` coordinates on the left and all `J,Y_R,Z_R` coordinates on the right. Denote the resulting physical cross block of the conditioned quadratic matrix by `M_cross`.

Let `Phi_L,Phi_R` be the matrices of the corresponding latent coefficient rows. Then

`M_cross=Phi_L H Phi_R^T
        =(Phi_L K^T) D (Phi_R K^T)^T`.                         (4.3)

Moreover

`Phi_L^T Phi_L = diag(G_I,y_L^2,z_L^2)`,

`Phi_R^T Phi_R = diag(G_J,y_R^2,z_R^2)`.                       (4.4)

Define the two `3 x 3` Schur-factor Grams

`F_L=K diag(G_I,y_L^2,z_L^2) K^T`,

`F_R=K diag(G_J,y_R^2,z_R^2) K^T`.                             (4.5)

### Lemma 4.1 — exact crossing-volume identity

If `F_L,F_R` are positive definite, then `M_cross` has exact rank three and, writing `Pi_3(M_cross)` for the product of its three nonzero singular values,

`boxed:
 Pi_3(M_cross)
 = |det D| sqrt(det F_L det F_R).
`                                                                  (4.6)

#### Proof

Set `A_L=Phi_L K^T`, `A_R=Phi_R K^T`. Positive definiteness says both have column rank three. Thin QR factorizations give

`A_L=Q_L R_L`, `A_R=Q_R R_R`,

where `Q_L,Q_R` have orthonormal columns and `R_L,R_R` are invertible `3 x 3`. Hence the three nonzero singular values of `M_cross` are those of

`R_L D R_R^T`.

Their product is

`|det R_L| |det D| |det R_R|
 = |det D| sqrt(det(A_L^T A_L) det(A_R^T A_R))`.

But `A_L^T A_L=F_L`, `A_R^T A_R=F_R`. QED.

### Lemma 4.2 — Schur-direction Cauchy-Binet lower bound

One has

`boxed: det F_L >= s_I y_L^2 z_L^2,`

`boxed: det F_R >= s_J y_R^2 z_R^2.`                           (4.7)

#### Proof

Use Cauchy-Binet on `A_L=Phi_LK^T`. Select a triple consisting of one first-bank physical row `i`, one `Y`-source row `j`, and one `Z`-source row `k`. Under `K`, the corresponding three column vectors are

`K(g_i,0,0)^T=(xi_i,*)^T`,

`K(0,0,eta_j,0)^T=eta_j e_2`,

`K(0,0,0,zeta_k)^T=zeta_k e_3`.

Therefore that `3 x 3` minor has determinant exactly

`xi_i eta_j zeta_k`.

The Cauchy-Binet expansion of `det F_L=det(A_L^T A_L)` is a sum of squares of **all** `3 x 3` physical minors. Keeping only these one-first/one-Y/one-Z triples gives

`det F_L
 >=sum_(i in I,j in Y_L,k in Z_L) xi_i^2 eta_j^2 zeta_k^2
 =s_I y_L^2 z_L^2`.

The right side is identical. QED.

Combining (3.2), (4.6), and (4.7) gives the central geometric inequality of this run:

`boxed:
 Pi_3(M_cross)
 >= mu m * y_L y_R z_L z_R * sqrt(s_I s_J).
`                                                                  (4.8)

This is an unconditional physical-crossing estimate in the original independent coordinates. It has no reciprocal small first-bank determinant and no residual `z_1 z_2` factor from the previous mixed-partner coordinates.

## 5. Balancing the two scalar product banks

For the normalized `Y` coefficients define

`q_Y=max_j eta_j^2`.

Randomly put every `Y` source coordinate into `Y_L` with probability `1/2`. If `T=sum_(j in Y_L)eta_j^2`, then

`E[T(1-T)]
 =1/4 (1-sum_j eta_j^4)
 >=1/4 (1-q_Y)`.                                                 (5.1)

Hence some deterministic split satisfies

`boxed: y_L y_R >= (1/2)sqrt(1-q_Y).`                            (5.2)

Similarly, with `q_Z=max_k zeta_k^2`, some split satisfies

`boxed: z_L z_R >= (1/2)sqrt(1-q_Z).`                            (5.3)

These are partitions of original-coordinate source banks, so no new independence is inferred after a rotation.

## 6. First-bank dichotomy and designated partner application

Recall `sum_i xi_i^2=1` and `xi_i=u_i/sqrt(m)`.

### Alternative 1: a heavy Schur row

If some `xi_h^2>=1/2`, then

`u_h^2=m xi_h^2 >=m/2`.                                          (6.1)

The single literal coordinate `h` belongs to the exact slope class with slope `t_h/u_h`; therefore the global exact-slope mass satisfies

`m_*>=u_h^2>=m/2`.                                                 (6.2)

Applying the completed designated `account04/B05` theorem at this actual inequality gives

`boxed:
 ||p_Q||_infinity
 <51.6 (mu m/2)^(-1/3)
 =51.6 (2/(mu m))^(1/3).
`                                                                  (6.3)

For the standard ratio packet `m>=3/20`,

`boxed: ||p_Q||_infinity <122.358 mu^(-1/3).`                      (6.4)

This branch establishes essential boundedness. The designated theorem does not claim continuity, so neither do I.

### Alternative 2: no heavy Schur row

Assume

`max_i xi_i^2<1/2`.                                                (6.5)

Greedily accumulate first-bank coordinates until `s_I=sum_(i in I)xi_i^2>=1/4`. Since the final added weight is `<1/2`,

`1/4 <=s_I<3/4`, and hence `1/4<s_J<=3/4`.                         (6.6)

Therefore

`boxed: s_I s_J >=3/16.`                                          (6.7)

Use this first-bank split and independently choose the scalar-bank splits from (5.2)-(5.3). Equation (4.8) becomes

`boxed:
 Pi_3(M_cross)
 >= (sqrt(3)/16) mu m sqrt((1-q_Y)(1-q_Z)).
`                                                                  (6.8)

Whenever `q_Y,q_Z<1`, this quantity is positive, so the physical crossing has exact rank three.

## 7. Exact-cross Fourier payment

For completeness, the determinant-sensitive `k=3` exact-cross estimate says: if an original-coordinate cut has cross rank exactly three and the product of its three nonzero singular values is `Delta`, then, allowing arbitrary within-side quadratic terms and arbitrary affine terms,

`|phi_Q(t)|
 <=min{1,(2 pi)^(3/2) Delta^(-1/2)|t|^(-3/2)}`.                  (7.1)

The proof is the thin SVD of the physical cross block, the universal `2^(3/2)` cap for three-dimensional orthogonal projections of cap-one product laws, and three-dimensional Plancherel. Integrating (7.1) gives

`boxed: ||p_Q||_infinity <=6 Delta^(-1/3).`                        (7.2)

Moreover `phi_Q in L^1`, so this branch has a bounded **continuous** density.

Insert (6.8):

`boxed:
 ||p_Q||_infinity
 <=6 [16/(sqrt(3) mu m sqrt((1-q_Y)(1-q_Z)))]^(1/3).
`                                                                  (7.3)

This is the main analytic payment of the run.

For the concrete scalar-diffuse chamber

`q_Y<=3/4`, `q_Z<=3/4`, `m>=3/20`,                              (7.4)

(7.3) gives

`boxed: ||p_Q||_infinity <37.613 mu^(-1/3)`                       (7.5)

in Alternative 2, with a continuous density.

Together with the designated partner payment (6.4), the **entire** chamber (7.4) satisfies

`boxed: ||p_Q||_infinity <122.358 mu^(-1/3).`                     (7.6)

Thus, on the actual hard subbranch `mu>=1`, this gives the universal numerical bound

`boxed: ||p_Q||_infinity <122.358`                                (7.7)

through the whole scalar-diffuse ratio-packet chamber. Continuity is guaranteed on the exact-cross half of the dichotomy, but not by the partner half.

## 8. Relation to the r33 heavy-Pluecker endpoints

The r33 compiler showed that a long first-bank heavy-row descent ends in one of: a two-sided exact crossing, two near-complementary rank-one first-bank coordinate sets, or a literal bi-star. Its difficult Cases B/C arose because both sides were required to obtain all three crossing directions from the first-bank/product-partner geometry.

Equation (4.8) changes the interface. Only the **single Schur-coordinate energy** `s_I,s_J` is required from the first bank. The other two crossing directions are supplied by splitting the two independent scalar source banks. Therefore, whenever `q_Y,q_Z` are quantitatively below one, the r33 near-rank-one and bi-star endpoints need not be paid at all: either a literal first-bank row already fires the exact-slope theorem, or the Schur energy itself can be balanced and the exact rank-three crossing closes the branch.

This is an aggregate-before-inversion result. The small `<=1/32` tails from r33 Case B are never deleted; all physical coordinates remain in one of the two exact-cross sides.

## 9. Precise remaining factor

The new theorem shows that **first-bank heavy residual geometry is no longer the obstruction when both scalar projections are diffuse**.

A survivor of this B05 route must now enter at least one scalar-heavy chamber,

`q_Y ->1` or `q_Z ->1`,                                            (9.1)

unless a previously isolated small-`mu` / escaped-curvature branch has already fired. In (9.1), splitting that scalar source bank necessarily has vanishing two-sided coefficient product, so (4.8) correctly degenerates.

The next precise implication is therefore

`QFORM-SCALAR-HEAVY-PIVOT-RECEIVER-v1`:

> If one normalized scalar bank has a literal original coordinate carrying a fixed fraction of its coefficient mass, retain that literal scalar as a pivot and combine it with the first product-projection bank and the other scalar bank to obtain an O(epsilon) interval bound, without deleting the remaining scalar-bank tail and without conditioning a dependent coordinate of `(S,R)`.

This is a different mechanism from repeating the r33 first-bank Pluecker compiler. It should exploit the literal scalar source coordinate and the exact Schur factorization (3.1), while keeping the tail inside the original product integral.

## 10. Integrity and scope

- Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuity remains **OPEN**.
- The new exact-cross branch proves continuity because its characteristic function is integrable.
- The designated exact-slope branch proves an essential density bound but does not supply continuity.
- No Gaussian, moment, log-concavity, compact-support, connected-support, or diagonal-basis assumption is added.
- No rotated coordinates are declared independent.
- No arbitrary-joint coarea theorem or positive conditional-density moment is used.
- No coefficient tail is discarded as a small random error.
- No Monte Carlo histogram is used. The accompanying finite computation is only an algebraic regression check of identities already proved exactly above.
