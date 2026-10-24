SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B07, 2026-09-24T11:33:34Z.
attacking: the r52 bounded carrier-heavy packet — project away a weak fourth carrier direction, force an actual physical E3 crossing when the strong three-plane is diffuse, and otherwise extract a single energetic physical row without selecting a minor.

# account02/B07 r53 — projected strong-three carrier or energetic physical row

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / complementary constructions and source-valid counterexamples  
Status: **NEW PROJECTED-R3 PHYSICAL-CUT THEOREM / r52 HEAVY64 REDUCED TO ONE ENERGETIC ROW / PINNED-e5 HUB THEOREM APPLIED TO TARGET-VALID REGRESSION / FULL QFORM OPEN**.

The unrestricted conjecture remains OPEN / not proved / not disproved. Full-target continuity remains OPEN. Every coordinate used below is an original physical coordinate. No moment, bounded-support, log-concavity, iid, post-rotation independence, arbitrary-joint coarea, pointwise stationary-phase estimate, or universally good individual minor is used. Small operator tails are restored in the actual crossing rather than discarded as random quadratic perturbations.

## 1. First unpaid implication after this run

`QFORM-R53-ENERGETIC-ROW-SCALAR-PIVOT-OR-ROUGH-STAR-RECEIVER-v1`.

On the captured r52 packet, after the physical-E3 exits proved below and in r52, one can now force one literal physical row `h` with

`sum_j A_hj^2=(A^2)_{hh}>1/8192`.                                      (1.1)

Hence either

`|A_hh|>1/128`,                                                        (1.2)

or

`sum_{j!=h} A_hj^2>1/16384`.                                          (1.3)

The next receiver must spend this scalar-pivot / aggregate-star dichotomy while retaining arbitrary quadratic curvature on all other coordinates and all additional spectral directions. It may not replace (1.3) by one large edge: Section 6 gives an exact target family with star energy one, every edge tending to zero, and every fixed-cardinality three-eigenvalue principal core degenerating. The completed pinned mixed-hub theorem pays that family for the correct aggregate reason.

The partner's separate spectral-escape branch `a_K<1/4`, the earlier T-side three-curvature branch, and the older same-bank-star branch remain separate debts.

## 2. Incoming state and exact dependencies

Latest completed designated partner actually consumed: account03/B07 r52,

`yspennstate/math-open-problems@4f5ee2dc112f258cb5dad4c9be03a9ae3573be6b`,

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B07/20260924T104017Z-account03-B07-qform-r52/REPORT.md`.

Its captured physical packet `K`, together with account02/B07 r52, gives the following hard substate after earlier exits. Write

`B=A[K,K]`, `D=A[K,K^c]`, `eps=1/64`,

and assume

`s_3(B)<eps`, `s_3(D)<eps`.                                            (2.1)

Let `B_2` be the top-two spectral truncation of the symmetric `B`, and `D_2` the top-two SVD truncation of `D`. The joint positive row carrier

`C_0=B_2^2+D_2D_2^T`                                                   (2.2)

satisfies

`lambda_3(C_0)>=gamma:=1/4-2eps^2=511/2048`, `rank(C_0)<=4`.            (2.3)

The proof is the target identity

`B^2+DD^T=(A^2)[K,K]>=U_KU_K^T`,                                      (2.4)

with `lambda_min(U_K^TU_K)>=1/4`, followed by removal of the two positive squared tails of operator norm `<eps^2`.

For analytic payment I use the completed marginal-free physical-crossing theorem from account02/B03,

`yspennstate/math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`,

which states that every literal physical cut `M=A[I,J]` with `Z_3=e_3(MM^T)>0`, arbitrary same-side curvature and affine terms satisfies

`||p_Q||_infinity <= C_3 Z_3^(-1/6)`,
`C_3=3*2^(4/3)*e^(1/3)=10.550168831164775...`,                          (2.5)

with a continuous density on that branch.

The mandatory pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

was read at `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its completed Theorem H is applied at a real target-valid obstruction in Section 6.

## 3. Project away a weak fourth carrier mode

Let the eigenvalues of `C_0` be

`theta_1>=theta_2>=theta_3>=gamma`, `theta_4>=0`,                       (3.1)

where `theta_4=0` when `rank(C_0)=3`. Let `P` be the top-three spectral projection and `Q_4=I-P`. Define

`B_3=P B_2 P`, `D_3=P D_2`, `C_3=B_3^2+D_3D_3^T`.                     (3.2)

### Lemma 3.1 — strong-three compression

One has

`lambda_3(C_3)>=gamma-theta_4`.                                       (3.3)

Moreover

`||B_2-B_3||_op<=2 sqrt(theta_4)`,
`||D_2-D_3||_op<=sqrt(theta_4)`.                                      (3.4)

### Proof

Because both summands in (2.2) are positive,

`B_2^2<=C_0`, `D_2D_2^T<=C_0`.                                       (3.5)

On the fourth spectral space,

`Q_4 C_0 Q_4<=theta_4 Q_4`; hence

`||Q_4B_2||_op=||B_2Q_4||_op<=sqrt(theta_4)`,
`||Q_4D_2||_op<=sqrt(theta_4)`.                                       (3.6)

Also

`P B_2^2 P
 =P B_2(P+Q_4)B_2P
 =B_3^2+P B_2Q_4B_2P`,                                                 (3.7)

and the last positive term has operator norm at most `theta_4`. Therefore

`C_3>=P C_0P-theta_4P`.                                               (3.8)

The three eigenvalues of `P C_0P` are `theta_1,theta_2,theta_3`, proving (3.3). Finally

`B_2-PB_2P=Q_4B_2+PB_2Q_4`,                                          (3.9)

which together with (3.6) proves (3.4). QED.

## 4. Diffuse strong three-plane gives an actual physical E3 crossing

Fix the convenient threshold

`tau=1/512`.                                                           (4.1)

Assume first

`theta_4<=tau`.                                                        (4.2)

Let `R` be an `|K| x 3` orthonormal frame spanning `range(P)`, and write

`ell_h=||R_{h,*}||_2^2`.

### Theorem 4.1 — `QFORM-R52-PROJECTED-R3-CARRIER-CUT-v1`

If

`max_h ell_h<=1/12`,                                                   (4.3)

then there is a literal physical partition `K=I disjoint_union J`, with every coordinate of `K^c` placed on the `J` side, such that the ACTUAL crossing

`M=A[I,J union K^c]`                                                   (4.4)

satisfies

`boxed:
 s_3(M)>=mu_*:=
 (1/4)sqrt(gamma-tau)
 -sqrt((eps+2sqrt(tau))^2+(eps+sqrt(tau))^2)
 =0.004400193079861364... .`                                          (4.5)

Consequently

`boxed:
 ||p_Q||_infinity<=C_3/mu_*
 =2397.6604298230423... .`                                            (4.6)

No `3x3` minor is selected; (4.6) spends the entire third-volume bank of the actual crossing.

### Proof

For independent Rademacher signs, the signed Gram matrix

`S=sum_h epsilon_h R_{h,*}^T R_{h,*}`

has

`E||S||_F^2=sum_h ell_h^2<= (1/12)sum_h ell_h=1/4`.                    (4.7)

Hence some sign choice has `||S||_op<=1/2`. The resulting partition obeys

`R_I^TR_I,R_J^TR_J>=I_3/4`.                                           (4.8)

Form the projected base crossing

`M_3=[B_3[I,J],D_3[I,:]]`.                                            (4.9)

The range of the symmetric `B_3` lies in `range(P)`. Thus (4.8) gives

`B_3[I,J]B_3[I,J]^T>=(1/4)(B_3^2)[I,I]`.                              (4.10)

The outside block keeps all of its columns, so trivially

`D_3[I,:]D_3[I,:]^T>=(1/4)(D_3D_3^T)[I,I]`.                           (4.11)

Therefore

`M_3M_3^T>=(1/4)C_3[I,I]`.                                           (4.12)

Since `C_3` has range `P`, (4.8) and (3.3) imply

`lambda_3(C_3[I,I])>=(1/4)(gamma-theta_4)`,                           (4.13)

and hence

`s_3(M_3)>=(1/4)sqrt(gamma-theta_4)`.                                 (4.14)

Now restore the actual matrices. By (2.1) and (3.4),

`||B-B_3||_op<eps+2sqrt(theta_4)`,
`||D-D_3||_op<eps+sqrt(theta_4)`.                                     (4.15)

For horizontal concatenation, the actual-crossing error therefore has norm at most

`E(theta_4)
 :=sqrt((eps+2sqrt(theta_4))^2+(eps+sqrt(theta_4))^2)`.                (4.16)

The signal term in (4.14) decreases and (4.16) increases with `theta_4`, so under (4.2)

`s_3(M)>= (1/4)sqrt(gamma-tau)-E(tau)=mu_*>0`,                         (4.17)

which is (4.5). Since `Z_3(M)>=s_3(M)^6`, (2.5) proves (4.6). QED.

This is the missing stability point: the weak fourth carrier direction is removed at matrix level, while its contribution is explicitly restored through (4.16). It is never interpreted as a small random quadratic perturbation.

## 5. Failure of the paid branches forces one energetic physical row

### Theorem 5.1 — `QFORM-R52-CARRIER-TO-ENERGETIC-ROW-v1`

In the hard state (2.1)-(2.3), if neither the r52 diffuse full-carrier cut nor Theorem 4.1 pays the law, then there is a physical coordinate `h in K` such that

`boxed:
 (A^2)_{hh}=sum_j A_hj^2>1/8192.`                                     (5.1)

### Proof

**Case 1: `theta_4<=1/512`.** If Theorem 4.1 does not apply, (4.3) fails, so some physical row has `ell_h>1/12`. Since the top three eigenvalues of `C_0` are at least `gamma`,

`C_0>=gamma P`.                                                       (5.2)

Thus

`(A^2)_{hh}>=(C_0)_{hh}>=gamma ell_h>gamma/12
 =511/24576
 =0.0207926432291666...`,                                             (5.3)

which is much stronger than (5.1). Here `(A^2)[K,K]>=C_0` because the discarded squared tails are positive.

**Case 2: `theta_4>1/512`.** Then `rank(C_0)=4`. Let `R_0` be an orthonormal frame for its full range. If every full-carrier leverage is at most `1/16=1/(4*4)`, account02/B07 r52 already supplies an actual physical crossing with `s_3>0.10278`, so we are in a paid branch. Otherwise some row has full-carrier leverage `ell_h^(0)>1/16`. Since

`C_0>=theta_4 R_0R_0^T`,                                              (5.4)

we get

`(A^2)_{hh}>=(C_0)_{hh}>theta_4/16>1/(512*16)=1/8192`.                 (5.5)

This proves the theorem. QED.

Because

`(A^2)_{hh}=A_hh^2+sum_{j!=h}A_hj^2`,                                 (5.6)

(5.1) implies the explicit pivot/star alternative (1.2)-(1.3). This is an actual original-coordinate output of the bounded-dimensional carrier extraction; it does not claim that `A[{h}, {h}]` or any bounded principal block already has three large eigenvalues.

## 6. Target-valid regression: aggregate star energy does not imply one good edge or bounded core

The star alternative (1.3) cannot be converted into a universal large edge or a fixed-cardinality three-eigenvalue principal block.

For even `m>=4`, let

`g=m^(-1/2)(1,...,1)`

and let `v` be the flat sign vector with `m/2` plus signs and `m/2` minus signs, so `g,v` are orthonormal. On one hub coordinate `0` and `m` leaves define

`A_m = [[0,g^T],[g,vv^T]]`.                                           (6.1)

On `span{e_0,g,v}` this is the orthogonal direct sum of

`[[0,1],[1,0]]` and `[1]`,                                            (6.2)

so

`spec(A_m)={1,-1,1,0,...,0}`.                                         (6.3)

This is an exact owner-target family. The hub has

`sum_{j!=0}A_{0j}^2=1`,                                               (6.4)

while every individual edge is only `m^(-1/2)`.

Moreover, for every fixed `L` and every physical principal set `C` with `|C|<=L`,

`boxed:
 s_3(A_m[C,C])<=L/m ->0.`                                             (6.5)

Indeed, if the hub is absent the principal block has rank at most one. If the hub is present and `S` is the selected leaf set, the pure star has rank two and third singular value zero, while the rank-one perturbation `v_Sv_S^T` has operator norm `||v_S||^2=|S|/m`; Weyl gives (6.5).

Thus even order-one physical star energy inside the exact three-large-eigenvalue class does not justify selecting one edge or one bounded spectral core.

### The mandatory pinned `e5f71d79...` result pays this obstruction

Use the completed Theorem H from the pinned `RESULTS.md` with

`H={0}`, `I={1,...,m}`, `J=empty`,

`A_II=vv^T` (rank `r=1`, eigenvalue `lambda=1`, diagonal twist zero), and hub coupling column `A_IH=g`.

Its augmented physical frame has rows

`rho_i=(v_i,g_i) in R^2`,                                             (6.6)

with Gram matrix

`G=sum_i rho_i rho_i^T=I_2`                                           (6.7)

and normalized leverage

`rho_i^T G^(-1)rho_i=2/m<=1/2`.                                      (6.8)

The pinned theorem therefore gives, for arbitrary independent cap-one input laws and arbitrary affine terms,

`|phi_Q(t)|
 <=[(4pi)^(3/2)/2]|t|^(-3/2)`.                                       (6.9)

Combining with the trivial cap one and Fourier inversion,

`boxed:
 ||p_Q||_infinity
 <=(1/(2pi))*6*[(4pi)^(3/2)/2]^(2/3)
 =12*2^(-2/3)
 =7.559526299369239... .`                                             (6.10)

This is a real application of a completed pinned theorem to the exact obstruction. The family that destroys both single-edge selection and every fixed small spectral core is nevertheless uniformly controlled because the original-coordinate product law sees the whole hub coupling and the diffuse rank-one leaf direction simultaneously.

## 7. What is now genuinely left

The r52 `<=64` carrier-heavy residual has been replaced by the much sharper physical alternative (1.1)-(1.3). In the exact low-rank-plus-diagonal leaf geometry of Section 6, pinned Theorem H already supplies the needed aggregate receiver even when all individual edges vanish. The missing analytic statement is therefore specifically a **rough-hub stability theorem**: spend a row with `sum_{j!=h}A_hj^2>=1/16384` (or a scalar pivot `|A_hh|>=1/128`) while the entire leaf quadratic block is arbitrary and may contain non-diagonal curvature, without deleting that curvature or imposing moments. A valid proof must preserve original-coordinate product provenance and cannot invoke one good edge/minor.

The separate partner spectral-escape branch, T-side three-curvature branch, and older large same-bank-star branch remain distinct. Full unrestricted QFORM remains OPEN. Continuity is obtained on the physical-E3 and pinned-H exits above, not asserted for the full target.
