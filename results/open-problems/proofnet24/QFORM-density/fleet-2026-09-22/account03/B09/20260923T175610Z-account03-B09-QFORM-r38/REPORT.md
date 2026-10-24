SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T17:56:10Z.
attacking: dual aggregate collapse of the rank-two hub/star small-G_* endpoint; test whether G_* scale forcing is possible and compile two-sided zero/small aggregate into a diagonal plus rank-at-most-four carrier without deleting residual curvature.

# account03/B09 r38 — dual aggregate collapse and the exact rank-four carrier

## Status

**NEW DETERMINISTIC STRUCTURAL THEOREM + A SOURCE CORRECTION + TWO ACTUAL O(|L|) CONTROL PAYMENTS / FULL QFORM OPEN.**

The unrestricted conjecture remains **OPEN**. This run addresses the first missing implication left after the current B09 `G_*>0` aggregate payment: can the bare three-large-eigenvalue hypothesis force the leaf singleton aggregate `G_*` to a universal positive scale, and if not, what does the exact/small two-sided aggregate survivor look like?

The first answer is **no**: a target-valid strict local no-pivot family has `G_*=0` identically. The second answer is a quantitative two-sided collapse. When both sides of a rank-two physical cross cut have small singleton third-volume aggregate and neither cross frame has a coloop, the full matrix is quantitatively close, in Frobenius norm and hence operator norm, to an original-coordinate diagonal plus a rank-at-most-four carrier. At exact aggregate zero, the representation is exact.

No random variable is rotated. No product law is replaced by independence of projected coordinates. No small matrix residual is deleted from the random quadratic form. The quantitative residual below is only a **matrix structural certificate**; using it analytically remains a separate debt because the source laws have no moment or support bound.

Continuity is proved below only for the explicit paid controls, not for the structural theorem and not for full QFORM.

Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh source pins consumed

Fresh owner controls were resolved from `yspennstate/math-research-brain` main before this run. The later owner continuation remains QFORM-exclusive, OWNER CONTROL revision `2026-09-22.15`, with no B09 pause or reassignment.

The immediate B09 inputs are:

1. `QFORM-RANK2-NOAUGMENT-AGGREGATE-STABILITY-v1`, account03/B09 r31, canonical source
   `yspennstate/math-open-problems@e8b97d9dcd8dd85cacc8fc73c2be4e86fde4b27a`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T114612Z-account03-B09-QFORM-r31/REPORT.md`.

   For a rank-two normalized cross factor `A[H,I]=P C^T`, `P^T P=I_2`, put
   `G=C^T C`, `Delta=sqrt(det G)`, leaf leverages
   `ell_i=c_i^T G^{-1}c_i`, and `q_I=max_i ell_i<1`. If `G_I` denotes the sum of squared singleton-augmented third singular volumes on the `I` side, then there are `M=M^T` and a physical diagonal `Lambda_I` with

   `||A[I,I]-C M C^T-Lambda_I||_F
       <= sqrt(2)/(sqrt(1-q_I)) * sqrt(G_I)/Delta`.              (1.1)

   At `G_I=0`, this is the exact no-augmentation model.

2. The newest same-slot aggregate analytic payment, account03/B09 r37, canonical mathematics currently recorded in
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T164604Z-account03-B09-QFORM-r37/REPORT.md`.
   It pays every `G_I>0` rank-two hub/star instance by a continuous density estimate of order `G_I^{-1/6}` while retaining arbitrary same-side curvature.

3. `QFORM-GROUPED-HUB-PLUCKER-SMOOTHING-v1`, account03/B09 r29, canonical source
   `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T101630Z-account03-B09-QFORM-r29/REPORT.md`.
   In the `h=2,r=0` case it gives the actual continuous-density estimate

   `||p_Q||_infinity <= 2e [rho det(C^T C)]^(-1/4)`,             (1.2)

   where `rho` is the disjoint Pluecker-basis mass of the two-dimensional leaf coefficient frame.

4. The designated partner theorem, account04/B09,
   `QFORM-PHYSICAL-CROSS-DETERMINANT-SMOOTHING-v1`, canonical source
   `yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B09/20260923T101659Z-account04-B09-dense-self-cross-fourier-r1/REPORT.md`.
   A literal invertible physical `3 x 3` cross block `K` gives

   `||p_Q||_infinity <= 3 |det K|^(-1/3)`                        (1.3)

   with arbitrary same-bank curvature and a continuous density.

All current source corrections are respected: no law-uniform pointwise quadratic-phase decay, no arbitrary-joint coarea theorem, no post-rotation independence, no universally good single physical minor, and no deletion of a small random quadratic tail.

## 2. Setup and the two singleton aggregate currencies

Let the complete active physical coordinate set be split into two disjoint original-coordinate banks

`H disjoint_union I`.

Assume the physical cross block has rank exactly two. Choose the normalized factorization

`B:=A[H,I]=P C^T`,                                               (2.1)

with

`P in R^{|H| x 2}`, `P^T P=I_2`,
`C in R^{|I| x 2}`, `rank C=2`.                                 (2.2)

Put

`G=C^T C`, `Delta=sqrt(det G)>0`.                               (2.3)

For the `I`-side frame write the row of `C` at `i` as `c_i^T` and define

`ell_i=c_i^T G^{-1} c_i`, `q_I=max_i ell_i`.                    (2.4)

For each `i in I`, form the literal singleton-augmented physical cross matrix

`M_i=A[H union {i}, I\{i}]`,                                   (2.5)

and define

`Gamma_i^2=e_3(M_i^T M_i)`, `G_I=sum_{i in I} Gamma_i^2`.       (2.6)

This is the `G_*` currency of the preceding B09 chain.

Now normalize the same physical cross block in the opposite direction. Define

`R=C G^{-1/2}`, `R^T R=I_2`,                                   (2.7)

and

`C_H=P G^{1/2}`.                                                (2.8)

Then

`B^T=R C_H^T`,                                                  (2.9)

and

`C_H^T C_H=G`.                                                  (2.10)

For a hub coordinate `h`, if `p_h^T` is the `h`th row of `P`, its leverage in this opposite normalized coefficient frame is exactly

`ell_h^{(H)}=(C_H)_h^T G^{-1}(C_H)_h=||p_h||_2^2`.              (2.11)

Put

`q_H=max_{h in H} ||p_h||_2^2`.                                (2.12)

Apply the same singleton construction after interchanging `H` and `I`: for each `h in H`, form

`N_h=A[I union {h}, H\{h}]`,                                   (2.13)

and set

`Theta_h^2=e_3(N_h^T N_h)`, `G_H=sum_{h in H} Theta_h^2`.       (2.14)

The two quantities `G_I,G_H` are completely physical/source-coordinate invariants of the chosen cut. No random coordinate transformation occurs in their definition.

## 3. Main deterministic theorem — dual aggregate collapse

### Theorem `QFORM-RANK2-DUAL-AGGREGATE-COLLAPSE-v1`

Assume (2.1)-(2.14) and the no-coloop gates

`q_I<1`, `q_H<1`.                                               (3.1)

Then there exist physical diagonal matrices `Lambda_H,Lambda_I`, symmetric `2 x 2` matrices `M,N`, and residual symmetric matrices `E_H,E_I` such that

`A[H,H]=P N P^T+Lambda_H+E_H`,                                  (3.2)

`A[I,I]=C M C^T+Lambda_I+E_I`,                                  (3.3)

with

`||E_I||_F <= sqrt(2) sqrt(G_I)/(Delta sqrt(1-q_I))`,           (3.4)

`||E_H||_F <= sqrt(2) sqrt(G_H)/(Delta sqrt(1-q_H))`.           (3.5)

Consequently, with

`D_0=diag(Lambda_H,Lambda_I)`,                                  (3.6)

`U=diag(P,C) in R^{(|H|+|I|) x 4}`,                             (3.7)

and

`K=[[N,I_2],[I_2,M]]`,                                         (3.8)

one has the exact decomposition

`A = D_0 + U K U^T + E`,                                       (3.9)

where

`E=diag(E_H,E_I)`                                               (3.10)

and therefore

`rank(U K U^T)<=4`,                                             (3.11)

and

`boxed:
 ||E||_F
 <= (sqrt(2)/Delta)
    [ G_I/(1-q_I)+G_H/(1-q_H) ]^(1/2).`                         (3.12)

In particular,

`||E||_op <= ||E||_F`                                          (3.13)

with the same right side.

If `G_I=G_H=0`, then `E=0` and the active matrix is **exactly**

`boxed: A = D_0 + S,  rank S<=4`,                               (3.14)

with

`S=U K U^T`.                                                    (3.15)

#### Proof

Apply r31 equation (1.1) directly on the `I` side. This produces a symmetric `M`, physical diagonal `Lambda_I`, and residual `E_I` satisfying (3.3)-(3.4).

For the opposite side, use the normalized factorization (2.7)-(2.10). Its coefficient Gram matrix is again `G`, hence its determinant scale is again `Delta`. Its row leverages are (2.11), so the r31 hypothesis is exactly `q_H<1`. Applying r31 after swapping the physical banks gives a symmetric `N_0`, a physical diagonal `Lambda_H`, and

`A[H,H]=C_H N_0 C_H^T+Lambda_H+E_H`                             (3.16)

with (3.5). Since `C_H=P G^{1/2}`, set

`N=G^{1/2}N_0G^{1/2}`.                                         (3.17)

Then `N=N^T` and `C_H N_0 C_H^T=P N P^T`, proving (3.2).

Using the original physical cross block (2.1), the matrix `U K U^T` has block form

`[[P N P^T, P C^T],
  [C P^T,   C M C^T]]`,                                        (3.18)

so (3.9) follows immediately. Since `U` has only four columns, (3.11) follows. Finally, the two residuals occupy disjoint physical principal blocks, hence

`||E||_F^2=||E_H||_F^2+||E_I||_F^2`,                           (3.19)

and (3.4)-(3.5) give exactly (3.12). `QED`

### Why the theorem matters

The small-aggregate survivor is not an amorphous high-dimensional matrix. Subject only to the explicit no-coloop gates, **all non-diagonal curvature on both sides is forced into the same two slope planes**, leaving a diagonal plus a four-dimensional carrier and a quantitatively certified residual. This is the two-sided version of r31 and is the correct successor after the `G_I>0` projected-crossing payment.

The residual in (3.12) is not discarded. That would be invalid for arbitrary unbounded cap-one source laws. The next analytic receiver must retain it inside the phase or convert it to another physical cross packet.

## 4. Spectral transfer to the rank-four carrier

The collapse has a useful deterministic spectral corollary whenever the cut covers the whole matrix (or whenever the active matrix is separately known to have the target singular-value lower bound).

Suppose

`s_3(A)>=1`,                                                     (4.1)

and write (3.9) as

`A=D_0+S+E`, `rank S<=4`.                                       (4.2)

If

`||D_0||_op<=tau`                                               (4.3)

and the right side of (3.12) is `eps`, then Weyl's singular-value perturbation inequality gives

`boxed: s_3(S)>=1-tau-eps.`                                     (4.4)

Therefore, whenever `tau+eps<1`,

`rank S>=3`.                                                     (4.5)

At exact dual aggregate zero,

`eps=0`,                                                        (4.6)

so under a small-diagonal gate the entire third spectral resource is carried by an explicit rank-three-or-rank-four matrix on the four-dimensional coefficient carrier (3.18):

`boxed: rank S in {3,4},  s_3(S)>=1-tau.`                       (4.7)

This is a deterministic reduction only. The rank-three carrier has existing Fresnel/BL paid subbranches; the genuinely general rank-four carrier with an arbitrary retained diagonal is still part of the global closure problem.

## 5. Correction — `G_I` cannot be forced to universal scale

### Proposition `QFORM-GSTAR-SCALE-FORCING-FALSE-v1`

The bare target hypothesis `s_3(A)>=1` does **not** imply any positive lower bound on `G_I`. In fact, there are arbitrarily diffuse target-valid physical matrices with

`G_I=G_H=0` exactly.                                             (5.1)

#### Construction

Let `N` be even. Define the `N x 2` Walsh frame

`P_N(i,:)=(1,s_i)/sqrt(N)`,                                     (5.2)

where exactly `N/2` of the signs are `+1` and `N/2` are `-1`. Let `C_N=P_N`, and put

`B_N=P_N C_N^T`.                                                (5.3)

Then

`P_N^T P_N=C_N^T C_N=I_2`,                                     (5.4)

so the two nonzero singular values of `B_N` are both one. Define the `2N x 2N` symmetric matrix

`A_N=[[0,B_N],[B_N^T,0]]`.                                     (5.5)

Its nonzero spectrum is exactly

`{-1,-1,1,1}`.                                                  (5.6)

Thus it satisfies the exact target spectral hypothesis with four eigenvalues of absolute value one.

Both same-side blocks vanish, so every singleton augmented third volume on either side is zero:

`G_I=G_H=0`.                                                     (5.7)

Moreover every physical cross coefficient belongs to `{0,2/N}`. Hence every diagonal entry is zero and every cross-bank `2 x 2` principal determinant has absolute value at most

`4/N^2`.                                                        (5.8)

Thus the family becomes arbitrarily deep inside any fixed local small-coefficient/small-principal-minor chamber while retaining four unit spectral eigenvalues. In particular, a strategy whose next step is to force `G_I>=c>0` from the global target is impossible.

This refutes only that intermediate forcing idea, not the bounded-density conjecture.

## 6. The exact zero-aggregate control is nevertheless paid in this diffuse family

The family (5.5) is not a concentration counterexample. It is a control showing what the analytic successor has to recognize.

For `C_N`, a nonzero two-row Pluecker basis consists of one `+` row and one `-` row. Every such basis has determinant-squared weight `4/N^2`, so the basis law is uniform on the `(N/2)^2` opposite-sign pairs. Two iid bases are disjoint exactly when they choose different rows in both sign classes. Therefore the disjoint-basis mass is exactly

`rho_N=(1-2/N)^2`.                                              (6.1)

Since `det(C_N^T C_N)=1`, the completed grouped two-hub theorem (1.2) gives, for every admissible cap-one product input law,

`boxed:
 ||p_{X^T A_N X}||_infinity
 <=2e (1-2/N)^(-1/2).`                                         (6.2)

The characteristic function is integrable in that theorem, hence this family has a **continuous density**, and every interval `L` satisfies

`boxed:
 P{X^T A_N X in L}
 <=2e (1-2/N)^(-1/2) |L|.`                                    (6.3)

For `N=512`,

`||p_Q||_infinity <=5.447213155188511`.                         (6.4)

At the same time the maximum physical cross coefficient is only `1/256` and the maximum absolute cross-bank principal `2 x 2` determinant is `1/65536`. Thus the zero-aggregate endpoint can remain uniformly smooth even while every literal coefficient and local two-coordinate pivot vanishes with dimension.

This is a direct `O(|L|)` payment with no square-root decoupling.

## 7. Required designated-partner application

The completed account04/B09 physical-cross theorem (1.3) is applied at a separate literal target-valid endpoint, not merely cited.

Take six original coordinates and

`A_partner=[[0,I_3],[I_3,0]]`.                                 (7.1)

Its spectrum is

`{-1,-1,-1,1,1,1}`,                                            (7.2)

and the literal physical cross block is

`K=I_3`, `|det K|=1`.                                          (7.3)

Therefore the designated partner theorem gives the actual inequality

`boxed: ||p_Q||_infinity <=3`,                                 (7.4)

and for every interval

`boxed: P{Q in L}<=3|L|`.                                      (7.5)

This endpoint has a continuous density. It also supplies a useful regression for the source-coordinate convention: the partner theorem is used only on genuinely disjoint physical banks.

## 8. Updated B09 closure edge

The previous debt

`QFORM-RANK2-HUBSTAR-GSTAR-SCALE-OR-PAID-EXIT-v1`

is now split cleanly:

- **forcing `G_I` to universal scale is false**, even in arbitrarily diffuse target-valid matrices;
- `G_I>0` is already paid analytically by the r37 projected-crossing theorem, but with a scale-dependent `G_I^{-1/6}` constant;
- if **both** side aggregates are zero and both no-coloop gates hold, the matrix is exactly original-coordinate diagonal plus rank at most four;
- if both aggregates are merely small, (3.12) gives the correct deterministic residual scale, but that residual may not be thrown away probabilistically.

The next precise B09 problem is therefore

`QFORM-DUAL-SMALL-AGGREGATE-R4-CARRIER-PAYMENT-v1`:

> Starting from `A=D_0+S+E`, `rank S<=4`, with `E` carrying the explicit two-sided aggregate bound (3.12), retain `E` exactly and prove a universal `O(|L|)` receiver from the target spectral condition, or compile `E` into a new physical cross packet. The exact `E=0` rank-three/rank-four carrier is the mandatory first endpoint. Coloop cases are to be routed separately through existing physical-localization branches.

This is a mechanism change on the same QFORM target: instead of trying to force a vanished aggregate, it passes to the finite-dimensional carrier forced by vanishing on **both** sides.

Full-target essential boundedness: **OPEN**.  
Full-target continuous density: **OPEN**.

## 9. Finite checks

`CHECK.py` beside this report verifies:

1. the Walsh frames have orthonormal columns;
2. `B_N` has exactly two unit nonzero singular values;
3. the block matrix (5.5) has exactly the four nonzero eigenvalues `-1,-1,1,1`;
4. the maximum physical cross coefficient and the principal `2 x 2` determinant scale are `2/N` and `4/N^2`;
5. the exact Pluecker disjointness probability is `(1-2/N)^2`;
6. the numerical bound (6.4);
7. on seeded exact dual-collapse regressions, the constructed matrix equals `D_0+U K U^T` to numerical precision and every singleton augmented cross matrix has numerical rank at most two;
8. the partner control has spectrum `+-1` with multiplicity three and bound `3`.

No Monte Carlo density histogram is used as evidence.
