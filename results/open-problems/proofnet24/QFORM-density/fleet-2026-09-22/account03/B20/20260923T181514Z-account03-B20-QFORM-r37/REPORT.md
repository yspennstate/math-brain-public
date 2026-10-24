SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B20, 2026-09-23T18:15:14Z.
attacking: the fresh B19 exact common-plane 2+2+2 receiver; force any genuinely nonsymmetric normalized cycle into a literal original-coordinate rank-three crossing, leaving only a physical heavy-row anchor or an approximately symmetric rank-two-completable cycle.

# account03/B20 r37 — common-plane relative-skew compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: proof closure and keeper  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / GLOBAL CONTINUITY OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

## 1. Fresh source frontier

Fresh protected control was resolved before the mathematics from `yspennstate/math-research-brain` main. OWNER CONTROL remains revision `2026-09-22.15`, QFORM is the sole target, and the live correction inbox was consumed. No post-rotation independence, pointwise quadratic-phase decay, arbitrary-joint coarea cap, worst-fiber supremum, one-good-minor selection, or small random-tail deletion is used below.

The immediate synthesis source is account03/B19 r37,

`yspennstate/math-open-problems@735e91d0d47eb10655192981f38b7e965d23521a`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260923T170040Z-account03-B19-qform-r37/REPORT.md`.

Its unpaid exact common-plane receiver has three disjoint original-coordinate banks and two-dimensional orthogonal frames. In frame coordinates the pairwise cross matrices are `C,N,P`, with `N,P` invertible. The normalized cycle is

`R = N^{-1} C P^{-T}`,

and after the block congruence `T=diag(N^{-T},P^{-T},I_2)` the cross-only part has off-diagonal blocks `R,I_2,I_2`. Same-bank quadratic phases remain arbitrary.

The B19 constants give

`rho_* = 63(1-2^-20)^2/16384`,
`x2_* = (64/259) rho_*`,
`sigma_*^2 = (3/8)x2_* = 0.000356312664981148...`.

For the first leg, `s_min(N)^2 >= sigma_*^2`. For the second common-plane leg, the principal-angle defect is `<1/64`, so the restriction to the common K-plane has

`s_min(P)^2 > m_*^2 := (63/64) sigma_*^2
                  = 0.0003507452795908176...`.                 (1.1)

I also use the completed account03/B20 r34 physical-third-volume theorem:

> for every literal original-coordinate cross block `M=A[L,R]`, if `Z=e3(MM^T)>0`, then the full ambient quadratic law has a continuous density and
>
> `||p_Q||_infty <= K3 Z^(-1/6)`,
> `K3=3*2^(4/3)*exp(1/3)<10.551`,
>
> with no row-volume marginal gate.

The designated partner actually applied is account04/B20 r10,

`yspennstate/math-open-problems@c6f29397b3d45a7cf7ab67633a5451767b478912`.

Its unrestricted fifth-volume theorem remains valid for every literal physical cross block and retains arbitrary same-bank terms and extra spectrum.

## 2. A two-dimensional physical split with no MSS machinery

### Lemma 2.1 — `QFORM-2FRAME-QUARTER-SPLIT-v1`

Let `U` be an `m x 2` matrix with orthonormal columns and rows `u_i^T`. If

`max_i ||u_i||^2 <= 1/64`,                                      (2.1)

then the original physical coordinates can be partitioned `L sqcup R=[m]` so that

`(1/4)I_2 < U_L^T U_L < (3/4)I_2`,
`(1/4)I_2 < U_R^T U_R < (3/4)I_2`.                              (2.2)

Proof. Independently put each row in `L` with probability `1/2` and write

`G_L=sum_i xi_i u_i u_i^T`.

Then `E G_L=I_2/2`, and independence plus centering gives

`E ||G_L-I_2/2||_F^2
 = (1/4) sum_i ||u_i u_i^T||_F^2
 = (1/4) sum_i ||u_i||^4
 <= (1/4)(1/64)sum_i||u_i||^2
 =1/128`.                                                       (2.3)

If every split had operator deviation at least `1/4`, its Frobenius-square deviation would be at least `1/16`, contradicting (2.3). Hence some split has `||G_L-I/2||_op<1/4`. Since `G_R=I-G_L`, (2.2) follows. QED.

This is an original-coordinate partition. No rotated coordinates are declared independent.

## 3. Exact algebra: skew is the obstruction to rank-two completion

For arbitrary real `2 x 2` blocks `D_1,D_2,D_3`, put

`K_R(D) = [[D_1,R,I],
           [R^T,D_2,I],
           [I,I,D_3]]`.                                        (3.1)

### Lemma 3.1 — `QFORM-2x2x2-CROSSRATIO-RANK2-GAP-v1`

Let `epsilon=s_3(K_R(D))`. Then

`boxed:
 epsilon >= min(1/4,
                 (3/16) ||R-R^T||_op/(1+||R||_op)).`           (3.2)

Proof. If `epsilon>=1/4` there is nothing to prove. Otherwise Eckart--Young gives a rank-at-most-two matrix `L`, partitioned into the same `2 x 2` blocks, with

`||K_R(D)-L||_op=epsilon`.                                      (3.3)

Every block differs by at most `epsilon`. In particular `L_13,L_23,L_31,L_32` are within `epsilon<1/4` of `I_2`, hence invertible, and `rank L=2` because `L_13` is invertible.

A rank-two block matrix with invertible `L_13` factorizes through its pivot block. Eliminating the unknown diagonal blocks gives the exact cross-ratio identity

`L_21 L_31^{-1} L_32 = L_23 L_13^{-1} L_12`.                   (3.4)

For the target matrix the two sides are respectively `R^T` and `R`. Since an `epsilon`-perturbation of `I` has inverse norm at most `4/3` and norm at most `5/4`, direct three-factor perturbation gives

`||R^T-L_21 L_31^{-1}L_32||
 <= (8/3)(1+||R||) epsilon`,                                    (3.5)

and

`||R-L_23 L_13^{-1}L_12||
 <= (8/3)(1+||R||) epsilon`.                                    (3.6)

Using (3.4),

`||R-R^T|| <= (16/3)(1+||R||)epsilon`,                          (3.7)

which is (3.2). QED.

The symmetric endpoint is genuine. If `R=R^T` is invertible, then choosing

`D_1=D_2=R`, `D_3=R^{-1}`                                      (3.8)

gives the exact factorization

`K_R(D) = [I; I; R^{-1}] [R, R, I]`,                            (3.9)

so `rank K_R(D)=2`. Thus no theorem based only on the three normalized cross edges can force a third singular direction when the cycle is symmetric; the remaining endpoint is not an artifact of the estimate.

## 4. Main compiler: diffuse frames + relative skew produce a literal D3 block

### Theorem 4.1 — `QFORM-COMMON-PLANE-SKEW-OR-HEAVY-COMPILER-v1`

Assume the exact B19 common-plane receiver scope: the three pairwise cross interactions factor through the three two-dimensional orthogonal frames, with frame matrices `C,N,P` above; arbitrary same-bank quadratic matrices are retained. Then at least one of the following holds.

1. **Physical heavy-frame anchor.** In at least one of the three frame matrices, some original coordinate row has leverage `>1/64`.

2. **Relative-symmetric normalized cycle.** 

   `||R-R^T||_op < (1/64)(1+||R||_op)`.                         (4.1)

3. **Continuous density payment.** The full ambient quadratic law has a continuous density and

   `boxed: ||p_Q||_infty < 4.107e7.`                            (4.2)

Proof. Suppose neither (1) nor (2) holds. Apply Lemma 2.1 independently inside each of the three original-coordinate banks. Let `L_j,R_j` be the resulting physical halves and put

`L=L_1 union L_2 union L_3`, `R'=R_1 union R_2 union R_3`.

Set `G_{j,L}=U_{j,L}^T U_{j,L}` and similarly on the right. By (2.2), every eigenvalue of each Gram lies in `(1/4,3/4)`.

The literal physical cross block

`M=A[L,R']`                                                     (4.3)

has a six-dimensional compression obtained by orthonormalizing the restricted frames. Its off-diagonal `2 x 2` blocks are

`G_{j,L}^{1/2} M_{jk} G_{k,R}^{1/2}`,                           (4.4)

while its three diagonal `2 x 2` blocks are whatever the actual same-bank cross-halves produce. Therefore this compressed matrix is

`K_phys = G_L^{1/2} K_0(D) G_R^{1/2}`,                          (4.5)

where `K_0(D)` has off-diagonal blocks `C,N,P` and arbitrary diagonal blocks.

Normalize `K_0(D)` by the B19 congruence `T=diag(N^{-T},P^{-T},I)`. Then

`T^T K_0(D) T = K_R(D')`                                       (4.6)

for some arbitrary diagonal blocks `D'`. Because (4.1) fails, Lemma 3.1 gives

`s_3(K_R(D')) >= 3/1024`.                                      (4.7)

Also

`sigma_min(T^{-1})^2
 = min{s_min(N)^2,s_min(P)^2,1}
 > m_*^2`.                                                      (4.8)

Hence singular-value monotonicity under invertible left/right factors yields

`s_3(K_0(D)) > m_*^2 (3/1024)`.                                 (4.9)

The Gram square roots in (4.5) have minimum singular value `>1/2`, so

`s_3(K_phys) > gamma_* := 3 m_*^2/4096
                           =2.568935153253058e-7`.              (4.10)

Compression by orthonormal frames cannot increase singular values, hence the actual physical cross block satisfies

`s_3(M) >= s_3(K_phys) > gamma_*`.                              (4.11)

Therefore its physical third exterior volume obeys

`Z=e_3(MM^T) >= [s_1(M)s_2(M)s_3(M)]^2 > gamma_*^6`.            (4.12)

Apply the completed physical-E3 theorem. It gives a continuous density and

`||p_Q||_infty
 < K3 gamma_*^{-1}
 = 41068256.6969... <4.107e7`,                                  (4.13)

which is (4.2). QED.

### What was gained

The exact common-plane 2+2+2 receiver no longer needs to handle a generic normalized matrix `R`. Every unpaid state is now forced into one of two highly structured endpoints:

- a literal original-coordinate leverage anchor in one of the three two-dimensional frames; or
- an approximately symmetric normalized cycle in the relative sense (4.1).

The exact symmetric invertible model (3.8)-(3.9) shows why the latter endpoint is the correct hard algebraic residue: arbitrary same-bank curvature can genuinely complete that normalized cycle to rank two.

## 5. Designated account04/B20 theorem applied to an actual inequality

The partner r10 fifth-volume theorem applies independently to the literal B19 side blocks `M_r=[C,N_r]`. The live B19 constants give

`||M_r||_F^2
 = ||C||_F^2+||N_r||_F^2
 > F+2 Delta
 =0.059598614828412805`.                                       (5.1)

Thus, if the first four squared singular values carry at most `63/64` of this physical energy, account04/B20 r10 gives the continuous bound

`boxed: ||p_Q||_infty <406.822.`                                (5.2)

Accordingly every common-plane state surviving into Theorem 4.1 is already in the partner's strong-top-four side regime. This is an equation-level application of the designated partner theorem, not a scope extension.

For completeness, applying the same partner theorem to the new split block (4.3) is also legitimate: (4.11) implies `||M||_F^2>3 gamma_*^2`; its fifth-volume diffuse-tail branch is therefore continuously paid. The sharper unconditional payment in this run is (4.13), so the partner bound is not used to inflate the final constant.

## 6. First remaining implication

The next exact closure edge is

`QFORM-COMMON-PLANE-RELATIVE-SYMMETRIC-OR-HEAVY-ANCHOR-PAYMENT-v1`:

> pay either a `>1/64` physical frame-leverage anchor while retaining all same-bank curvature, or the normalized cycle satisfying `||R-R^T|| < (1+||R||)/64`. In the latter branch the exact symmetric completion (3.9) must be treated as a genuine rank-two control, so the third target singular direction has to be recovered from residual/off-plane geometry rather than asserted from the cycle itself.

The unrestricted conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains open; continuity is proved on the relative-skew branch (4.2) and on the partner fifth-volume branch (5.2).

Repository transport and source-memory reads are distinct from native learned-memory ingestion; no native receiver use was verified, so execution remains `WITHOUT_VERIFIED_BRAIN`.
