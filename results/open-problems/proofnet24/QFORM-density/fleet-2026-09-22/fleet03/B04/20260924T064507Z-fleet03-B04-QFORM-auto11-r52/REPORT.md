SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B04, 2026-09-24T06:45:07Z.
attacking: the fixed-pair overlap-two survivor through a determinant-free Schur-numerator two-volume Riesz splice, before any reciprocal pair determinant is paid.

# fleet03/B04 r52 — pair Schur-numerator two-volume receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: **NEW SUPPORTING THEOREM / GENERAL-RANK OVERLAP-TWO BRANCH COMPRESSED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Regularity: the new receiver proves absolute continuity and an essential density bound; it does **not** by itself prove continuity. Full-target continuity remains OPEN.

The unrestricted target remains unchanged. All random coordinates below are literal ORIGINAL independent coordinates with one-dimensional density caps one. No moment, Gaussian, log-concave, compact-support, connected-support, iid, diagonal-basis, post-rotation-independence, arbitrary-joint coarea, worst-fiber supremum, law-uniform pointwise quadratic-phase decay, or deletion of a nonzero random tail is used.


## 1. Source-valid analytic inputs

Two completed product-coordinate estimates are spliced.

### 1.1 Physical-pair one-third density envelope

The preceding B04 r51 report records the completed determinant-only physical-pair envelope: for two ORIGINAL independent cap-one variables, any invertible symmetric physical pair `B`, any deterministic translation, and `D=|det B|`, the centered pair-quadratic output `T` satisfies

`p_T(u) <= C_pair D^(-1/3)|u|^(-1/3)` for a.e. `u!=0`,             (1.1)

with

`C_pair=2+2*pi`.                                                     (1.2)

The translation may depend on coordinates conditioned outside the pair; conditional on those coordinates it is deterministic, and the two physical input densities remain cap one.

Source: B04 r51 canonical report
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B04/20260924T054741Z-fleet03-B04-QFORM-auto11-r51/REPORT.md`.

### 1.2 Sharp critical two-volume half-Riesz

B04 r40 proved `QFORM-SHARP-ROW-MARGINAL-FREE-2VOLUME-COLLISION-v1`. If a quadratic-plus-affine form on two disjoint ORIGINAL-coordinate banks has physical cross block `M` with

`Z_2=e_2(MM^T)>0`,                                                   (1.3)

then

`sup_s E|R-s|^(-1/2)
 <= C_H Z_2^(-1/8),`
`C_H=8*2^(3/8)=10.374716437208077... .`                             (1.4)

All same-bank quadratic terms and affine terms are retained. No continuity is asserted from this critical endpoint.

Source: `yspennstate/math-open-problems@8192c4990fff2ba5dee1ce62fdf92e815b5b89c1`.

## 2. Exact pair Schur-numerator algebra

Fix a literal physical pair `H={h_1,h_2}` and put `K=H^c`. In physical coordinates write

`A = [[B, C^T],
      [C, D]],`                                                     (2.1)

where `B=A[H,H]` is symmetric `2x2`, `C=A[K,H]`, and `D=A[K,K]`.
Define the **Schur numerator matrix**

`N_H := det(B) D - C adj(B) C^T.`                                  (2.2)

This definition is polynomial in the physical coefficients and makes sense even when `B` is singular.

For any distinct `i,j in K`, the bordered determinant formula is

`boxed:
 (N_H)_(ij)
 = det A[H union {i}, H union {j}].`                               (2.3)

Hence the fixed-pair overlap-two third-compound packet is exactly

`boxed:
 J_2(H)=sum_(i!=j, i,j in K) (N_H)_(ij)^2.`                        (2.4)

When `det B!=0`, the exact physical Schur complement is

`S_H=D-CB^(-1)C^T=N_H/det B.`                                     (2.5)

No individual bordered determinant is selected or inverted.

## 3. Main theorem: determinant-free two-volume receiver

Let `I,J` be disjoint subsets of `K` and put

`Z_N(I,J):=e_2(N_H[I,J]N_H[I,J]^T).`                              (3.1)

### Theorem `QFORM-PAIR-SCHUR-NUMERATOR-2VOLUME-v1`

If `Z_N(I,J)>0`, then the full ambient quadratic form `Q=X^TAX` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= C_SN Z_N(I,J)^(-1/12),`
`C_SN=8*2^(1/4)(1+pi)
    =39.40169160873585... .`                                      (3.2)

The theorem holds for **every** symmetric physical pair `B`, including singular pairs. Arbitrary coefficients on `K`, arbitrary same-bank curvature inside `I` and `J`, all coordinates outside `I union J`, and all affine terms created by conditioning are retained.

### 3.1 Proof for `det B!=0`

Complete the actual physical pair, without rotating random variables. With `Y=X_K`,

`Q=(X_H+h(Y))^T B (X_H+h(Y)) + R(Y),`                             (3.3)

where `h(Y)` is an affine physical-coordinate translation and the quadratic part of `R` is the Schur complement `S_H` from (2.5).

Condition on `Y=y`. By (1.1), uniformly in the translation `h(y)`,

`p_(Q|Y=y)(q)
 <= C_pair |det B|^(-1/3)|q-R(y)|^(-1/3).`                        (3.4)

Averaging,

`p_Q(q)
 <=C_pair |det B|^(-1/3)
   E|q-R(Y)|^(-1/3).`                                              (3.5)

The literal `I-J` cross block of the residual is

`S_H[I,J]=N_H[I,J]/det B`,                                        (3.6)

so

`e_2(S_H[I,J]S_H[I,J]^T)
 = Z_N(I,J)/|det B|^4.`                                            (3.7)

Apply the sharp critical half-Riesz theorem (1.4) to the **whole residual form** `R`, keeping every same-bank term:

`sup_q E|q-R|^(-1/2)
 <=C_H |det B|^(1/2) Z_N(I,J)^(-1/8).`                            (3.8)

Lyapunov/Jensen with exponent `2/3` gives

`E|q-R|^(-1/3)
 <=[E|q-R|^(-1/2)]^(2/3)`
` <= C_H^(2/3)|det B|^(1/3)Z_N(I,J)^(-1/12).`                    (3.9)

Insert (3.9) into (3.5). The physical pair determinant cancels **exactly**:

`||p_Q||_infinity
 <=C_pair C_H^(2/3) Z_N(I,J)^(-1/12).`                            (3.10)

Since

`C_H^(2/3)
 =(8*2^(3/8))^(2/3)=4*2^(1/4),`                                  (3.11)

(3.10) is precisely (3.2).

The first reciprocal is therefore taken only after the pair packet has been converted into the polynomial numerator currency `Z_N`; no small `det B` remains in the final bound.

### 3.2 Singular physical pair by coefficient perturbation

Now let `B` be arbitrary singular and assume `Z_N(I,J)>0`. Put

`B_e=B+e I_2`,
`A_e=A+e(e_(h1)e_(h1)^T+e_(h2)e_(h2)^T)`.                         (3.12)

Choose a sequence `e_m->0` avoiding the finitely many roots of `det B_e`. Define

`N_e=det(B_e)D-C adj(B_e)C^T`.                                    (3.13)

Polynomial continuity gives

`N_e[I,J]->N_H[I,J]`,
`Z_e:=e_2(N_e[I,J]N_e[I,J]^T)->Z_N(I,J)>0`.                       (3.14)

For every `m`, the nonsingular-pair proof yields

`||p_(Q_e_m)||_infinity <= C_SN Z_e_m^(-1/12).`                   (3.15)

For every sample point, all physical coordinates are finite and

`Q_e_m-Q=e_m(X_(h1)^2+X_(h2)^2)->0`.                              (3.16)

Thus the laws converge weakly. Interval domination and Portmanteau transfer the limiting cap in (3.15), proving exactly (3.2) for singular `B`. No moment bound and no deletion of a nonzero random term is used.

Notice the boundary geometry: if `rank B=1`, then `det B=0` and `adj(B)` has rank one, so `N_H=-C adj(B)C^T` has rank at most one; consequently every `Z_N(I,J)` vanishes. The new theorem therefore does not falsely claim to pay the genuine rank-one kernel-star obstruction isolated by fleet03/B07.

## 4. Aggregate-before-inversion corollary

Define the disjoint Schur-numerator two-volume

`D_2^disj(N_H)
 :=sum_(|R|=|T|=2, R cap T=emptyset)
     det N_H[R,T]^2,`                                               (4.1)

where the row/column pairs are ordered.

Randomly color every coordinate of `K` into literal banks `I,J` with probability `1/2`. Cauchy-Binet gives

`e_2(N_H[I,J]N_H[I,J]^T)
 =sum_(R subset I, T subset J, |R|=|T|=2)
   det N_H[R,T]^2.`                                                 (4.2)

A fixed disjoint ordered pair `(R,T)` is captured with probability `2^-4=1/16`. Therefore

`E e_2(N_H[I,J]N_H[I,J]^T)
 =D_2^disj(N_H)/16.`                                                (4.3)

Some actual original-coordinate cut attains at least the mean. Theorem 3 then yields

### Corollary `QFORM-PAIR-SCHUR-NUMERATOR-DISJOINT-v1`

If `D_2^disj(N_H)>0`, then

`boxed:
 ||p_Q||_infinity
 <= C_disj [D_2^disj(N_H)]^(-1/12),`
`C_disj=8*2^(7/12)(1+pi)
      =49.64302065931249... .`                                    (4.4)

Again, only essential boundedness is asserted.

## 5. Spend the fresh general-rank overlap-two localization

The completed fleet03/B20 r42 operator-overlap theorem is at

`yspennstate/math-open-problems@7e9f6e73f1f1f5304cc30a6204caf7ee0629904a`.

Under the full owner hypothesis `s_3(A)>=1`, it proves the dimension-free four-way funnel

`P_3>=1/4`, or `J_2^*>=1/144`, or `J_1^*>=1/144`, or `J_0>=1/16`,  (5.1)

where `J_2^*=max_H J_2(H)` is exactly the fixed-pair packet (2.4).

Take the overlap-two branch and choose `H` with

`J:=J_2(H)>=1/144.`                                                 (5.2)

Introduce the scale-free **tetrad ratio**

`theta_H := D_2^disj(N_H)/J^2.`                                    (5.3)

If

`theta_H>=1/64`,                                                    (5.4)

then (4.4) and (5.2) give the explicit full-ambient bound

`||p_Q||_infinity
 <=C_disj theta_H^(-1/12) J^(-1/6)`
` <=C_disj *sqrt(2)*144^(1/6)`
` =160.73123410505744... .`                                        (5.5)

Thus the general-rank overlap-two debt is now compressed to the genuinely coherent chamber

`boxed:
 J_2(H)>=1/144,
 D_2^disj(N_H)<J_2(H)^2/64.`                                      (5.6)

This is a stronger description than “large overlap-two mass”: every still-unpaid pair packet must have very small disjoint `2x2` tetrad volume relative to its total bordered-minor energy. Exact rank-one pair numerators lie on the extreme face `D_2^disj=0`, consistent with the existing kernel-star theory.

For context, the other two already-paid ends of (5.1) sharpen with current B04 constants: `P_3>=1/4` is paid by r51 at `<78.893`; `J_0>=1/16` is paid by a random physical cut plus the optimized cross-`E_3` theorem at `<26.837` with a continuous `C_0` density. The overlap-one `J_1^*` and the coherent low-tetrad survivor (5.6) remain distinct structural debts.

## 6. Genuinely rotated indefinite dense example

Let

`B=[[3,1/5],[1/5,-3]],`                                            (6.1)

`C=(1/20)*[[1,2],[2,-1],[-1,3],[3,1]],`                           (6.2)

and

`R=[[1/10, 1/20, 3, 1],
    [1/20,-1/10, 1,-3],
    [3,1,1/20,-1/25],
    [1,-3,-1/25,-1/20]].`                                         (6.3)

Define

`D=R+C B^(-1)C^T`,
`A_*=[[B,C^T],[C,D]].`                                             (6.4)

Every entry of this `6x6` symmetric matrix is nonzero. It is not diagonal in the independent coordinates and all four outside coordinates couple to both physical pair coordinates.

The Schur complement of the first physical pair is **exactly** `R`, hence

`N_H=det(B)R`,
`det B=-226/25.`                                                    (6.5)

Take residual banks `I={3,4}`, `J={5,6}` in the displayed ordering. Their Schur cross block is

`R[I,J]=[[3,1],[1,-3]],`
`det R[I,J]=-10.`                                                   (6.6)

Therefore

`Z_N(I,J)
 =det(N_H[I,J])^2
 =100*(226/25)^4
 =10435031104/15625
 =667841.990656.`                                                   (6.7)

The new theorem gives, for **every** admissible cap-one product input law,

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=39.40169160873585...
    * Z_N(I,J)^(-1/12)
 =12.8862155235537... .`                                           (6.8)

The target spectral condition is rigorous without numerical eigensolver evidence. Write `A_0=diag(B,R)`. The eigenvalues of `B` are `+/-sqrt(226)/5`. Split `R=R_0+E_R`, where `R_0` has pure cross block `[[3,1],[1,-3]]`; hence `spec(R_0)={+sqrt(10),+sqrt(10),-sqrt(10),-sqrt(10)}`. The same-bank perturbation obeys

`||E_R||_op<=sqrt(5)/20`,                                         (6.9)

so every eigenvalue of `R` has modulus at least

`sqrt(10)-sqrt(5)/20 >3.05.`                                      (6.10)

Also

`||A_*-A_0||_op
 <=||C||_op+||C||_op^2||B^(-1)||_op`
` <=sqrt(3/40)+3/(8sqrt(226))`
` =0.2988059076989983... .`                                       (6.11)

Since

`sqrt(226)/5-0.2988059076989983...
 =2.7078533679755834...>1,`                                       (6.12)

Weyl's inequality shows that `A_*` has three positive and three negative eigenvalues, all of modulus greater than one. This is a fully dense genuinely rotated indefinite target matrix. Exact rational checks also give numerical eigenvalues approximately

`-3.24141657,-3.11190981,-2.97932762,
 +2.97932762,+3.11190981,+3.24141657`.                              (6.13)

The theorem and the spectral proof do not rely on Monte Carlo output.

## 7. Required designated-partner application

The newest completed `fleet04/B04` handoff remains r2:

`yspennstate/math-open-problems@4a54666abf2316bb79b939cef3ea940605a0af57`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B04/20260924T001353Z-fleet04-B04-QFORM-r2/REPORT.md`.

On its high-carrier branch, failure of the anchored entropy gate produces a literal physical row pair `{a,b}` in a cross block `M` with canonical fourth-volume pair mass

`eta_ab=P(a,b in R)>2/75.`                                         (7.1)

Thus its aggregate pair-anchored fourth-volume is

`H_ab^(4)=eta_ab E_4(M)>(2/75)E_4(M).`                            (7.2)

Apply the completed B04 pair-anchored `E_4` promotion theorem at this actual inequality:

`||p_Q||_infinity
 <=2^(17/8)[H_ab^(4)]^(-1/8)`
` <4*75^(1/8) E_4(M)^(-1/8)`
` =6.861872579851902... E_4(M)^(-1/8).`                            (7.3)

That partner branch has a continuous `C_0` density. This is equation-level use of the designated partner result; the new Schur-numerator theorem in Sections 2--5 is a separate mechanism.

## 8. What remains

Full QFORM remains **OPEN**. Full-target continuity remains **OPEN** separately.

The first nonduplicate B04 debt is now

`QFORM-LOW-TETRAD-PAIR-NUMERATOR-TO-KERNELSTAR-OR-RIDGE-v1`:

> starting from the target-scale fixed pair packet `J_2(H)>=1/144` and the now-forced coherent condition `D_2^disj(N_H)<J_2(H)^2/64`, prove a dimension-free structural alternative that routes the Schur numerator to (i) the completed rank-one physical-pair kernel-star receiver, (ii) a grouped star/ridge/square-bank endpoint, or (iii) a renewed positive disjoint numerator two-volume. The proof must keep arbitrary same-bank curvature and must not select a tiny bordered minor before aggregation.

The exact singular-pair face is consistent: `rank B=1` forces `rank N_H<=1`, so it belongs to the kernel-star side rather than the new two-volume side. The difficult new work is quantitative stability of that rank-one/tetrad geometry when (5.6) is small but nonzero.

No scheduler state, cadence, task identity, email/push notification, public release, repository visibility, paid API/model, or cross-account authentication state was changed.
