SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B09, 2026-09-23T01:49:49Z.
attacking: the exact-kernel remainder from the double-null shear: aggregate transverse couplings into a disjoint rank-three physical cross bank, prove an O(interval length) payment without coordinate-max loss, and isolate the genuine global-kernel survivor.

# fleet03/B09 — double-null local kernel: aggregate transverse rank-three payment or exact global-kernel quotient

**Run:** `20260923T014949Z-fleet03-B09-QFORM-auto11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Bilinear block mechanism / disjoint physical-coordinate banks  
**Status:** `NEW_STRUCTURAL_DICHOTOMY + TARGET-SCOPE_DENSITY_BRANCH + GLOBAL-KERNEL_QUOTIENT / FULL_QFORM_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source controls

The sole target remains the unrestricted statement: for independent real coordinates `X_i` with probability densities bounded by one, and real symmetric `A` with at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has universally bounded density, or give a valid target counterexample. No Gaussian, log-concavity, moment, support, sign, diagonal-basis, or post-rotation-independence assumption is used. Continuity is tracked separately.

Fresh owner control was revision `2026-09-22.15`; QFORM remains the sole research target. The current correction ledger forbids law-uniform pointwise quadratic-phase decay, arbitrary conditional spectral density caps, naive fiber suprema, and extraction of one uniformly good physical minor. The argument below uses none of them. It instead aggregates all transverse physical couplings **before** reciprocal payment.

The immediate predecessor is fleet03/B09 `QFORM-DOUBLE-NULL-LINEAR-SHEAR-v1`, canonical mathematics

`yspennstate/math-open-problems@cf838adcab387ff12ba3b7140191433d0b80c357`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260923T005036Z-fleet03-B09-QFORM-auto11/REPORT.md`.

That theorem paid the exact left-shear chamber `a_L=0, r_L!=0` by a mass-sensitive slice Hausdorff--Young argument. It left only `a_L=r_L=0`, in which the five-coordinate packet has an exact kernel vector.

Two completed peer results are used at actual inequalities here:

1. fleet02/B07 `QFORM-CROSS-FIBER-PLANCHEREL-v1`, source
   `yspennstate/math-open-problems@7140ff63d4ff7c092cdc18ce7ad8a95e4e03e388`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B07/20260922T193347Z-b07-639234ec/REPORT.md`. For a physical cross block `M=A[L,R]` of rank `r>=3`, with `|L|=r`, it proves
   `||p_Q||_infinity <= sqrt(e) r/(r-2) det(MM^T)^(-1/(2r))`,
   retaining arbitrary self blocks and all signs. In particular for `r=3`,
   `||p_Q||_infinity <= 3 sqrt(e) det(MM^T)^(-1/6)` and the density is continuous.
2. fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, source
   `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, path
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. An orthogonal `k`-dimensional projection of an original cap-one product source has density cap at most `exp(k/2)`.

The designated partner `fleet04/B09` had no completed current-QFORM handoff, memory snapshot, or QFORM archive at the fresh checks. No partner theorem is fabricated or awaited; work proceeds asynchronously with the compatible completed sources above.

## 2. Exact notation for the double-null packet

Choose five distinct original coordinates consisting of a scalar coordinate `x`, a two-coordinate bank `I`, and a disjoint two-coordinate bank `J`. Write the quadratic coefficient blocks

`a=A_xx`,
`C=A[I,I]`,
`B=A[I,J]`,
`r=A[I,x]`,
`s=A[J,x]`,

where `B` is assumed invertible. Thus the local quadratic part contains

`a x^2 + 2x r^T u + 2x s^T v + u^T C u + 2u^T Bv + v^T A[J,J]v`.

Set

`kappa=B^(-T)s`,
`r_L=r-C kappa`,
`a_L=a-2r^T kappa+kappa^T C kappa`.                         (2.1)

This is exactly the left shear `u'=u+kappa x` used in the preceding B09 run. The present run assumes the only still-unpaid local chamber

`a_L=0`,  `r_L=0`.                                           (2.2)

Then

`r=C kappa`,  `a=kappa^T C kappa`,  `B^T kappa=s`.           (2.3)

For the five-coordinate principal packet, (2.3) gives the exact local kernel vector

`z_5=(1,-kappa,0_J)`,
`A[{x} union I union J] z_5=0`.                              (2.4)

The issue is whether outside coordinates destroy this local kernel. That question has a clean aggregate answer.

## 3. New structural theorem: transverse rank three or a genuine global kernel

Let

`K=[n] \ ({x} union I union J)`.

Write

`D=A[I,K]`,
`c=A[K,x]`,
`tau=c-D^T kappa in R^K`.                                   (3.1)

The vector `tau` is exactly the coupling of the local kernel direction to all outside physical coordinates.

Define the disjoint physical banks

`L={x} union I`,       `R=J union K`,

so `|L|=3`, and let the full cross block be

`M=A[L,R]
 = [[s^T, c^T],
    [ B , D  ]]`.                                           (3.2)

### Theorem 3.1 — `QFORM-DOUBLE-NULL-TRANSVERSE-RANK3-OR-GLOBAL-KERNEL-v1`

Under (2.2):

1. If `tau!=0`, then `rank M=3`,

   `det(MM^T)^(1/2) >= |det B| ||tau||_2`,                  (3.3)

   and the full quadratic form has a continuous density satisfying

   `boxed:
   ||p_Q||_infinity
     <= 3 sqrt(e) (|det B| ||tau||_2)^(-1/3)
     < 4.947 (|det B| ||tau||_2)^(-1/3).
   `                                                               (3.4)

   Consequently every interval `I0` obeys

   `P(Q in I0)
      <= 3 sqrt(e) (|det B| ||tau||_2)^(-1/3) |I0|`.         (3.5)

2. If `tau=0`, then the extended vector

   `z=(1,-kappa,0_J,0_K)`                                   (3.6)

   is an **exact global kernel vector** of `A`: `Az=0`.

So the former five-coordinate exact-kernel obstruction is not an analytic endpoint anymore: either its outside couplings create a paid aggregate rank-three cross bank, or it is a literal global kernel direction.

### Proof of the aggregate determinant inequality

Left-multiply (3.2) by the determinant-one shear matrix

`R_0=[[1,-kappa^T],[0,I_2]]`.

Using `s=B^T kappa`,

`R_0 M
 = [[0, tau^T],
    [B, D]].`                                               (3.7)

For every `k in K`, take the three columns consisting of the two `J` columns and column `k`. Their `3x3` determinant is exactly

`det M[:, J union {k}] = det(B) tau_k`.                     (3.8)

The equality is unaffected by the left shear because `det R_0=1`.

Cauchy--Binet therefore gives

`det(MM^T)
 = sum_(S subset R, |S|=3) det(M[:,S])^2
 >= |det B|^2 sum_(k in K) tau_k^2
 = |det B|^2 ||tau||_2^2`.                                 (3.9)

If `tau!=0`, this proves rank three and (3.3).

Now apply fleet02/B07 `QFORM-CROSS-FIBER-PLANCHEREL-v1` to the **entire** disjoint original-coordinate partition `(L,R)`. Since the left bank has exactly three original coordinates and `M` has full row rank,

`||p_Q||_infinity
 <= 3 sqrt(e) det(MM^T)^(-1/6)
 <= 3 sqrt(e)(|det B|^2 ||tau||_2^2)^(-1/6)`,              (3.10)

which is (3.4). The peer theorem also gives continuity. Equation (3.5) follows by integrating the density over an interval. No square-root loss in interval length occurs. `QED` for branch 1.

### Proof of the global-kernel alternative

Under (2.3), the `x`, `I`, and `J` rows of `Az` vanish by construction. For an outside row `K`,

`(Az)_K=A[K,x]-A[K,I]kappa=c-D^T kappa=tau`.                (3.11)

Hence `tau=0` implies `Az=0` in every physical coordinate. `QED`.

### Why the aggregate norm is essential

The payment is through `||tau||_2`, not `max_k |tau_k|`. Thus a diffuse transverse coupling spread over `m` coordinates is not charged a factor `sqrt(m)`. This is exactly the aggregate-before-inversion behavior demanded by the known local-minor counterexamples.

## 4. Target-valid diffuse stress family

The aggregate theorem is not cosmetic. For every `m>=1`, take the left bank

`L={x,u_1,u_2}`

and right bank

`R={v_1,v_2,y_1,...,y_m}`,

with a pure bipartite quadratic coefficient matrix

`A_m=[[0,M_m],[M_m^T,0]]`,

where

`M_m =
 [1,0, m^(-1/2),...,m^(-1/2);
  1,0, 0,...,0;
  0,1, 0,...,0].`                                         (4.1)

Take `I={u_1,u_2}`, `J={v_1,v_2}`. Then

`B=I_2`, `s=e_1`, `kappa=e_1`, `C=0`, `r=0`, `a=0`,

so

`a_L=r_L=0`.                                               (4.2)

The local five-coordinate packet has the exact kernel direction `x-u_1`. Each individual transverse coordinate has

`tau_k=m^(-1/2)`,                                          (4.3)

so every `3x3` minor using `{v_1,v_2,y_k}` has magnitude only `m^(-1/2)` and vanishes as `m->infinity`. However

`||tau||_2=1`, `|det B|=1`,                               (4.4)

and directly

`M_m M_m^T = [[2,1,0],[1,1,0],[0,0,1]],
 det(M_m M_m^T)=1`.                                       (4.5)

Thus the aggregate theorem remains dimension-free:

`boxed: ||p_(X^T A_m X)||_infinity <=3sqrt(e)<4.947.`       (4.6)

Moreover (4.5) has eigenvalues

`1, (3+sqrt(5))/2, (3-sqrt(5))/2`.

Hence the nonzero singular values of `M_m` are

`1, phi, phi^(-1)`, where `phi=(1+sqrt(5))/2`,

and the nonzero eigenvalues of `A_m` are

`{+phi,+1,+phi^(-1),-phi,-1,-phi^(-1)}`.                  (4.7)

So every `A_m` is a literal target matrix: it has four eigenvalues of modulus at least one. This family demonstrates precisely why one must aggregate the diffuse transverse bank before taking reciprocal determinants.

## 5. New exact quotient description of the genuine global-kernel survivor

The branch `tau=0` has additional structure that is useful for the next run and for other workers. It can be quotiented without losing the three-large-eigenvalue spectrum; the cost is a controlled two-dimensional dependent block whose provenance is an orthogonal projection of three original independent coordinates.

Let all coordinates except `x` be grouped as `(u,w)`, where `u in R^2` denotes the `I` bank and `w` contains `J union K`. Define

`T(x,u,w)=(u+kappa x,w)`.                                  (5.1)

Its kernel is exactly `span{z}` with `z` from (3.6). Because `Az=0`, there is a symmetric `(n-1)x(n-1)` matrix `N` such that

`A=T^T N T`;                                               (5.2)

in fact `N` is simply the principal coefficient matrix obtained by setting `x=0`, written in coordinates `(u,w)`.

Let

`G=TT^T=diag(I_2+kappa kappa^T, I_(n-3))`,
`S=G^(1/2)`.                                               (5.3)

Set

`H=S N S`.                                                 (5.4)

### Theorem 5.1 — `QFORM-GLOBAL-KERNEL-ORTHOPROJECTION-QUOTIENT-v1`

If `tau=0`, then:

1. the nonzero eigenvalues of `H` are exactly the nonzero eigenvalues of `A`; hence `H` still has at least three eigenvalues of modulus at least one;
2. if

   `Z=S^(-1) T X`,                                         (5.5)

   then

   `Q=X^T A X=Z^T H Z`;                                   (5.6)

3. `Z=(Z_0,X_w)`, where the two-dimensional block

   `Z_0=(I_2+kappa kappa^T)^(-1/2)(X_I+kappa X_x)`          (5.7)

   is independent of all untouched original coordinates `X_w` and is an **orthogonal two-dimensional projection** of the original independent triple `(X_x,X_I)`;
4. consequently, by fleet02/B06,

   `||p_(Z_0)||_infinity <= e`,                             (5.8)

   and for every unit `theta in R^2`,

   `||p_(theta^T Z_0)||_infinity <= sqrt(e)`.               (5.9)

Thus the global-kernel survivor is reduced exactly to a spectrum-preserving quadratic-form problem with one controlled two-dimensional projection block plus otherwise independent cap-one scalar coordinates.

### Proof

Because `T` has full row rank, the standard nonzero-spectrum identity for products gives that the nonzero eigenvalues of

`A=T^TNT`

are the eigenvalues of

`NTT^T=NG`.                                                (5.10)

But `NG` is similar to the symmetric matrix `SNS`:

`NG=S^(-1)(SNS)S`.                                         (5.11)

This proves item 1.

Writing `R=TX=SZ`,

`Q=R^T N R=Z^T S N S Z`,                                  (5.12)

which proves item 2.

For the first block, let `S_0=(I_2+kappa kappa^T)^(1/2)` and define the `3x2` matrix

`R_0=[kappa, I_2]^T S_0^(-1)`.                             (5.13)

Then

`R_0^T R_0
 =S_0^(-1)(kappa kappa^T+I_2)S_0^(-1)=I_2`.             (5.14)

Therefore

`Z_0=R_0^T (X_x,X_I)`                                      (5.15)

is an orthogonal two-dimensional projection of three original independent cap-one variables. It remains independent of `X_w`, because the source coordinate sets are disjoint. Applying the completed fleet02/B06 theorem with `k=2` gives (5.8), and applying it with `k=1` to every unit projection gives (5.9). `QED`.

### What the quotient does not prove

The two coordinates of `Z_0` are generally dependent; one must **not** rotate them and claim independence. The arbitrary-joint rank-three coarea and conditional-cap shortcuts are already refuted. Therefore Theorem 5.1 is a precise reduction, not a full solution. It identifies the exact product-provenance class that a global-kernel induction would need to tolerate.

## 6. Complete local routing after this run

For an invertible original-coordinate `2x2` cross packet `B=A[I,J]` and scalar coordinate `x`, the current left-shear route is now:

1. `a_L !=0`: paid by completed fleet01/B11 `QFORM-TWOSIDED-SHEAR-MIXED-v1`;
2. `a_L=0`, `r_L!=0`: paid by the preceding fleet03/B09 `QFORM-DOUBLE-NULL-LINEAR-SHEAR-v1`;
3. `a_L=r_L=0`, `tau!=0`: paid here by Theorem 3.1, with a continuous density and the explicit aggregate bound (3.4);
4. `a_L=r_L=tau=0`: the local kernel is a genuine **global kernel**, and Theorem 5.1 gives an exact spectrum-preserving quotient with one two-dimensional orthogonal-projection block.

So no analytic singularity remains inside the double-null packet itself. The only survivor is a structural/provenance problem attached to an actual global null direction.

The new first B09 debt is therefore

`QFORM-GLOBAL-KERNEL-PROJECTION-BLOCK-PAYMENT-v1`:

> Prove a universal density bound for the spectrum-preserving quotient class in Theorem 5.1: one two-dimensional block that is an orthogonal projection of three independent cap-one variables, independent of all remaining cap-one scalar coordinates, with a symmetric coefficient matrix having at least three eigenvalues of modulus at least one. Equivalently, show that the controlled projection provenance `(5.8)-(5.9)` is enough to continue the bilinear/ridge routing without reverting to a false arbitrary-joint coarea or conditional-fiber supremum.

A parallel structural route is to show that repeated global-kernel quotients force a paid rank-three cross bank before the dependent projection blocks accumulate. Either route would convert the exact-kernel endpoint into a dimension-reducing induction.

Full QFORM remains **OPEN**. General continuity remains **OPEN**. Continuity is proved in the transverse branch `tau!=0` through the `L^1` characteristic-function theorem of fleet02/B07.

## 7. Deterministic checks

The companion `CHECK.py` verifies the algebraic stress family for several `m`, including:

- `det(M_m M_m^T)=1`;
- Gram eigenvalues `1,(3+sqrt(5))/2,(3-sqrt(5))/2`;
- full nonzero spectrum `+-phi,+-1,+-phi^(-1)`;
- each selected local transverse determinant equals `1/sqrt(m)` while the squared aggregate determinant mass sums to one;
- `3sqrt(e)=4.946163812100385...`.

These checks are finite regression evidence only; the proofs are the exact identities above.
