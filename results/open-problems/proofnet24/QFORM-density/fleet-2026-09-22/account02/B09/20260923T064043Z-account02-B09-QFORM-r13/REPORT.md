SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-23T06:40:43Z.
attacking: the partner k=1 physical rank-split survivor by a two-physical-hub determinant-balanced mixed-hub estimate that keeps the entire physical hub core and a dense same-side leaf packet.

# account02/B09 r13 — two-hub Pluecker smoothing, arbitrary physical core, dense leaf curvature

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / complementary constructions and source-valid counterexamples  
Status: **ESSENTIAL_STEP_APPLIED / NEW TWO-HUB SUPPORTING THEOREM / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains **OPEN**. This run proves a determinant-balanced two-physical-hub extension of the newest mixed-hub Fresnel mechanism. It has two features needed by the current B09 proof map: the entire actual physical `2 x 2` hub core is retained with no nondegeneracy assumption, and a genuinely dense same-side leaf-curvature packet is retained exactly. The result therefore pays a quantitative part of the newest partner's near-null physical-core survivor without deleting a small coefficient on an unbounded product law.

No moments, compact support, connected support, log-concavity, identical laws, Gaussianity, post-rotation independence, arbitrary-joint coarea, worst conditional-density supremum, or pointwise law-uniform stationary phase is used. No probability squaring occurs; the final small-ball estimate is linear in interval length.

## 1. First unpaid implication

The newest completed designated partner result is account03/B09 r25,

`QFORM-RANKONE-HUBPAIR-RANDOM-SLOPE-v1`,

canonical source

`yspennstate/math-open-problems@b9f0099d9dc82b69a2af9ec252f22e094c193ea5`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T061516Z-account03-B09-QFORM-r25/REPORT.md`.

It consumes this worker's preceding k=1 torsion-to-wedge theorem and classifies every exact algebraic rank/sign of the selected physical pair. Its remaining debt is quantitative degeneration: a rank-one resource, a definite determinant, or an indefinite pair scale can approach zero, and a near-zero physical core cannot be discarded on arbitrary unbounded input laws.

The first unpaid B09 implication is therefore sharpened here to

`QFORM-TWOHUB-LOWRANK-OR-SMALLDISJOINT-ROUTING-v1`:

> Starting from a physical pair whose two cross rows into a disjoint original-coordinate bank have quantitative aggregate wedge, pay the entire actual physical pair core at once whenever the outside same-side block has a determinant-balanced exact low-rank-plus-diagonal packet. If that determinant-balanced certificate fails, route the resulting small-disjointness/localized leaf geometry to a finite-core, cross-volume, ridge, or genuinely higher-rank curvature payment. The routing must not treat a small matrix coefficient as a small random quadratic perturbation.

Sections 2--5 prove the first branch, including a dense same-side rank-one packet. The arbitrary high-rank/small-disjointness routing remains open.

## 2. Source-pinned inputs actually used

### 2.1 Owner-required newest-Claude package

I read the required directory at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

The exact completed input used below is Theorem H and, specifically, its proof **before** the final leverage-gated Brascamp--Lieb step. For physical hubs `H`, a leaf bank `I`, and

`A_II=D+sum_k lambda_k v_kv_k^T`,

it conditions only on disjoint original coordinates, integrates the untouched physical hub variables using their density caps, Fresnel-linearises only the displayed coefficient identity, and leaves an `(r+|H|)`-dimensional Fourier integral over the augmented physical rows. The blocks `A_HH,A_HJ,A_IJ,A_JJ` are arbitrary. Thus the mechanism retains the actual physical hub core and works before any spectral rotation of the random vector.

### 2.2 Determinant-weighted entropy Brascamp--Lieb

The second completed input is account02/B07

`QFORM-PLUCKER-ENTROPY-BL-v1`,

canonical source

`yspennstate/math-open-problems@32c257209b588141fb60af698f478f1d0ad20b8a`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T123512Z-b07-qform-minors-11/REPORT.md`.

For an `N x d` matrix `U` with orthonormal columns, Pluecker weights

`w_S=det(U_S)^2`, `|S|=d`,

and any basis law `pi` whose coordinate-inclusion marginals are at most `1/2`, it proves for arbitrary one-coordinate phases

`int_(R^d) prod_i |hat g_i(<U_i,z>+a_i)| dz
 <= exp(D(pi||w)/2) (2pi)^d e^(d/2)`.                         (2.1)

If `S,T` are iid from the Pluecker law and

`rho=P(S cap T=empty)>0`,                                     (2.2)

conditioning on disjointness produces such a `pi` and

`D(pi||w)<=log(1/rho)`.                                       (2.3)

This is the determinant-balanced replacement for the raw `<=1/2` leverage gate.

### 2.3 Latest partner theorem

The account03/B09 r25 theorem quoted in Section 1 proves that for a nonzero rank-one physical pair core

`E=[[a,b],[b,c]]`

and complementary coupling rows `u,v`, after completing a physical square the surviving random slope is

`w=v-(b/a)u`.

When `a!=0` and `w!=0`, with completely arbitrary complementary quadratic block and affine terms,

`||p_Q||_infinity
 <=4sqrt(2)e^(1/4)(|a| ||w||_2)^(-1/2).`                      (2.4)

I apply (2.4) to an actual target-valid dense-remainder inequality in Section 7.

## 3. New theorem: two physical hubs plus determinant-balanced leaf packet

Split the original independent coordinates as

`H={h_1,h_2} union I union J`,                                 (3.1)

where `h_1,h_2` are two literal physical coordinates. After conditioning on `X_J`, allow all generated affine terms. Assume that the exact leaf principal block is

`A_II=D+sum_(k=1)^r lambda_k v_kv_k^T`,                       (3.2)

where `D` is diagonal, `r>=0`, and each displayed `lambda_k` is nonzero. Put the two actual hub-to-leaf coupling columns

`c_a=A[I,h_a]`, `a=1,2`,                                      (3.3)

and define

`W=[v_1,...,v_r,c_1,c_2]`,
`G=W^T W`,
`d=r+2`.                                                       (3.4)

Assume `G>0`. Whiten only this deterministic coefficient frame,

`U=W G^(-1/2)`,                                                (3.5)

so `U^TU=I_d`; no random coordinate is rotated or declared independent. Let

`w_S=det(U_S)^2`, `|S|=d`,                                    (3.6)

and let `rho` be the probability that two iid bases from `w` are disjoint.

### Theorem `QFORM-TWOHUB-PLUCKER-SMOOTHING-v1`

If `rho>0`, then the full quadratic form has a continuous density and

`boxed:
 ||p_Q||_infinity
 <= C_r [rho det(G) prod_(k=1)^r |lambda_k|]^(-1/(r+4)),`     (3.7)

where

`C_r=((r+4)/(r+2)) exp((r+2)/(r+4)).`                          (3.8)

Consequently every interval `L` satisfies

`boxed:
 P{Q in L}
 <= C_r [rho det(G) prod_k |lambda_k|]^(-1/(r+4)) |L|.`       (3.9)

The physical hub block `A_HH` is completely arbitrary: both diagonal entries and the mutual hub edge may vanish, be near zero, be definite, indefinite, or rank one. The blocks `A_HJ,A_IJ,A_JJ` are also arbitrary, as are all affine terms.

In particular,

`r=0: C_0=2sqrt(e)<3.298`,                                    (3.10)

so, writing

`Delta=||c_1||^2||c_2||^2-<c_1,c_2>^2=det G`,                 (3.11)

we have

`boxed: ||p_Q||_infinity <=2sqrt(e) [rho Delta]^(-1/4).}`      (3.12)

For one exact same-side curvature direction,

`r=1: C_1=(5/3)e^(3/5)<3.037`,                                (3.13)

and

`boxed:
 ||p_Q||_infinity
 <=(5/3)e^(3/5)[rho det(G)|lambda|]^(-1/5).`                  (3.14)

### Proof

Condition on the original coordinates `X_J`. Their values alter only affine terms in `(X_H,X_I)` and an additive constant, while the quadratic blocks in (3.2)--(3.4) stay fixed.

For fixed hub values `x_H`, the `I`-variables see the linear tilt

`2 A_IH x_H + ell`,                                           (3.15)

where `ell` is an arbitrary conditioning-generated vector. Terms involving only `x_H` are a phase. Taking absolute values after the `I` expectation, using `f_(h_a)<=1`, and substituting

`y=2t x_H`                                                     (3.16)

gives the exact hub Jacobian

`(2|t|)^(-2)`.                                                 (3.17)

Apply Fresnel linearisation to the `r` displayed squares in (3.2). Their contribution in absolute value is

`prod_k (4pi |t lambda_k|)^(-1/2)`,                            (3.18)

and the remaining Fourier integral is

`J_t=int_(R^d) prod_(i in I)
    |hat g_(i,t)(<W_i,z>+a_i)| dz`,                            (3.19)

where `|g_(i,t)|=f_i`; the diagonal entries of `D` are harmless one-coordinate phases, and the shifts `a_i` include all conditioning-generated translations.

Substitute `z'=G^(1/2)z`. From (3.5),

`J_t=det(G)^(-1/2)
 int_(R^d) prod_i |hat g_(i,t)(<U_i,z'>+a_i)| dz'.`            (3.20)

Apply the determinant-entropy theorem (2.1)--(2.3):

`J_t <=det(G)^(-1/2)(2pi)^d e^(d/2) rho^(-1/2).`              (3.21)

Combining (3.17), (3.18), and (3.21), the powers of two cancel exactly:

`2^(-2)(4pi)^(-r/2)(2pi)^(r+2)=pi^((r+4)/2).`                 (3.22)

Hence, with

`alpha=(r+4)/2`,                                               (3.23)

we obtain

`|phi_Q(t)|
 <= A |t|^(-alpha),`                                          (3.24)

where

`A=pi^alpha e^((r+2)/2)
 [rho det(G) prod_k |lambda_k|]^(-1/2).`                      (3.25)

Together with `|phi_Q(t)|<=1`,

`int_R |phi_Q(t)| dt
 <=2 alpha/(alpha-1) A^(1/alpha).`                             (3.26)

Since `alpha>=2`, this envelope is integrable. Fourier inversion gives

`||p_Q||_infinity
 <=alpha/[pi(alpha-1)] A^(1/alpha)
 =((r+4)/(r+2))e^((r+2)/(r+4))
  [rho det(G) prod_k|lambda_k|]^(-1/(r+4)),`                  (3.27)

which is (3.7). Integrability of `phi_Q` gives a continuous density on this branch. Averaging over the conditioned original coordinates preserves the same essential bound, proving (3.9). QED.

The proof never squares a small-ball probability or characteristic function. The `|t|^-alpha` envelope is integrated directly, so the interval estimate stays `O(|L|)`.

## 4. Apply the theorem to the current k=1 torsion branch: arbitrary physical pair core

The preceding account02/B09 theorem

`QFORM-K1-TORSION-TO-PHYSICAL-WEDGE-v1`

at canonical source

`yspennstate/math-open-problems@ab1efb0930b7a16dc71c32530e155dd521289ab9`

produces, in the partner's `k=1` rank-split branch, a physical leaf `i`, the physical hub `h`, and a disjoint outside bank `T` whose two actual cross rows have Gram determinant

`Delta_i(T)
 >= [eta^2(1-eta)/3] Theta^2`,                                (4.1)

where

`Theta=|det(f,Kf,q)|`.                                        (4.2)

The latest account03/B09 r25 theorem pays each exact algebraic type of the physical pair separately. The new two-hub theorem instead pays the **whole physical pair core at once** whenever the outside packet is determinant-balanced.

### 4.1 Diagonal outside block

Assume only that the actual `T x T` principal block is diagonal. Put

`H={i,h}`, `I=T`,                                              (4.3)

condition every other original coordinate, and let `rho_2` be the disjoint-basis mass of the whitened two-frame formed by the two cross rows from `(i,h)` to `T`. Applying (3.12) and then (4.1),

`||p_Q||_infinity
 <=2sqrt(e)[rho_2 Delta_i(T)]^(-1/4)
 <=2sqrt(e)3^(1/4) eta^(-1/2)(1-eta)^(-1/4)
   rho_2^(-1/4)|Theta|^(-1/2).`                               (4.4)

At the partner scale `eta=1/16`,

`boxed:
 ||p_Q||_infinity
 <17.642 rho_2^(-1/4)|Theta|^(-1/2).`                         (4.5)

This estimate is uniform over the actual physical pair block. In particular the near-zero transition between rank zero, rank one, definite rank two and indefinite rank two requires no separate reciprocal core payment in this branch. All couplings to conditioned coordinates remain arbitrary.

### 4.2 One exact dense same-side direction

Now allow

`A_TT=D+lambda vv^T`,                                         (4.6)

with `D` diagonal and `lambda!=0`. Let the two cross rows be `a,b in R^T`; put

`tau=dist(v,span{a,b})`.                                      (4.7)

For

`W=[v,a,b]`,                                                   (4.8)

the Gram determinant identity is

`det(W^TW)=Delta_i(T) tau^2`.                                 (4.9)

Let `rho_3` be the corresponding three-dimensional determinant-weighted disjoint-basis mass. Applying (3.14), (4.1), and (4.9) gives

`boxed:
 ||p_Q||_infinity
 <=(5/3)e^(3/5)
 [rho_3 |lambda| tau^2 eta^2(1-eta)Theta^2/3]^(-1/5).`        (4.10)

At `eta=1/16`,

`boxed:
 ||p_Q||_infinity
 <11.618 [rho_3 |lambda| tau^2 Theta^2]^(-1/5).`              (4.11)

The dense rank-one operator `lambda vv^T` is retained **inside the active outside bank**. It is not conditioned away and is not treated as a small perturbation. Again the actual physical pair core is arbitrary.

This is a concrete payment of the current near-null-core debt on a nontrivial dense same-side branch.

## 5. Actual target-valid source-coordinate star where the raw leverage gate fails

The determinant-balanced theorem is not merely a reformulation of the newest-Claude raw leverage hypothesis.

Take three mutually disjoint leaf supports `I_v,I_1,I_2`. On `I_v`, choose a unit vector `v` whose squared coordinate weights are

`0.6` and one hundred copies of `0.004`.                        (5.1)

On each `I_1,I_2`, choose unit flat vectors `c_1,c_2` on 256 coordinates. Because the supports are disjoint,

`v,c_1,c_2` are orthonormal.                                   (5.2)

With two disjoint physical hubs `X_1,X_2`, define the actual source-coordinate star

`F=2X_1<c_1,Y>+2X_2<c_2,Y>+<v,Y>^2.`                          (5.3)

The same-side operator `vv^T` is dense on its 101-coordinate physical support and is retained exactly.

In the grouped orthonormal basis `(X_1,c_1,X_2,c_2,v)`, the nonzero spectrum is

`{1,-1,1,-1,1}`,                                               (5.4)

so (5.3) is a literal target matrix.

The augmented mixed frame has Gram matrix `G=I_3`, but its largest physical row leverage is

`0.6>1/2`.                                                      (5.5)

Thus the final raw leverage gate in newest-Claude Theorem H does **not** apply.

The Pluecker basis law factorises over the three disjoint supports. On the `v` support the probability that two weighted choices differ is

`1-[0.6^2+100(0.004)^2]=0.6384`,                              (5.6)

while on either flat 256-coordinate support it is `255/256`. Therefore

`rho=0.6384(255/256)^2
    =0.6334222412109375.`                                      (5.7)

Applying the new `r=1` theorem gives the actual target inequality

`boxed:
 ||p_F||_infinity
 <=(5/3)e^(3/5) rho^(-1/5)
 <3.328,`                                                      (5.8)

and hence

`boxed: P{F in L}<3.328 |L|}`                                 (5.9)

for every interval `L` and every choice of independent cap-one input densities.

This is the requested mixed-hub smoothing on an actual source-coordinate star with dense same-side couplings, in a case where the source theorem's raw leverage gate itself fails. The improvement comes from determinant-weighted disjoint physical bases, not from rotating the input law.

## 6. What small determinant-disjointness means here

The theorem deliberately retains `rho`. It is not legitimate to replace `rho>0` by a heuristic statement that the frame is merely full rank. The completed B07 identity gives, for the whitened `d`-frame,

`rho=sum_S w_S det(I-U_S^TU_S).`                               (6.1)

Thus small `rho` is a quantitative physical localization flag. For the present two-hub theorem, failure of determinant balance does not invalidate the Fourier reduction; it says the final physical-basis averaging has concentrated onto overlapping coordinate sets.

This is exactly the branch that must be sent to finite physical cores or to the partner rank-split machinery. It is also why no fixed tiny physical minor is inverted in (3.7): the determinant mass is aggregated before reciprocal payment.

The preceding B09 cancellation obstruction remains active. A favorable displayed low-rank same-side component can be canceled by an arbitrary residual operator on the same bank. Therefore (4.10) must be read as a theorem about the **actual exact** decomposition (4.6), not about a favorable component hidden inside an arbitrary residual.

## 7. Latest partner result applied to a real target inequality

Apply account03/B09 r25 equation (2.4) to a simple source-valid target family that also retains dense same-side curvature.

Let `X,Y` be two physical original coordinates. Let `Z_K` be a disjoint original-coordinate bank, and choose orthonormal unit coefficient vectors `z,w` on that bank; they may be flat on large supports. Define

`Z=<z,Z_K>`, `W=<w,Z_K>`,                                     (7.1)

and

`Q_*=X^2+2YZ+W^2.`                                            (7.2)

For the physical pair `(X,Y)`, the core is

`E=diag(1,0)`,                                                 (7.3)

which has rank exactly one. In the partner notation,

`a=1`, `b=c=0`, `u=0`, `v=z`,

so the Schur-transverse row is exactly `z` and has norm one. The full complementary quadratic block contains the dense rank-one square `ww^T`; r25 permits it to be arbitrary and does not require independence between the random slope `Z` and the quadratic environment `W^2`.

Therefore its completed theorem gives

`boxed:
 ||p_(Q_*)||_infinity
 <=4sqrt(2)e^(1/4)
 =7.2635446348...<7.264,`                                     (7.4)

with the identical coefficient multiplying every interval length.

In the grouped orthonormal basis `(X,Y,z,w)`, the coefficient matrix has spectrum

`{1,1,-1,1}`.                                                  (7.5)

Hence (7.4) is an actual target-valid application of the newest completed designated-partner result. If `w` is chosen flat, `W^2` is a genuinely dense same-side physical operator; the theorem keeps it inside the arbitrary environment rather than conditioning on the projected variable or inventing independence between `Z` and `W`.

## 8. Exact scope and remaining gap

What is newly paid:

1. Two literal physical hubs with **arbitrary actual `2 x 2` core** are paid whenever the augmented leaf frame has positive determinant-weighted disjoint-basis mass and the actual leaf self-block is diagonal plus a finite exact curvature packet.
2. The `r=0` specialization removes the newest partner's near-zero-core singularity entirely on the determinant-balanced diagonal-outside branch.
3. The `r=1` specialization retains a dense same-side rank-one operator and pays the current k=1 torsion branch by the aggregate resource `rho_3 |lambda| tau^2 Delta`, again uniformly over the physical pair core.
4. A target-valid two-hub star with maximum mixed leverage `0.6>1/2` is controlled by `<3.328`; the raw leverage-gated Theorem H does not cover this example.
5. The newest account03/B09 r25 result is applied to the explicit target `X^2+2YZ+W^2`, giving `<7.264` while an arbitrary dense same-side square stays in the environment.

What remains unpaid is not an exact core-rank classification. It is the routing of an arbitrary high-rank same-side outside operator when every useful fixed-rank exact packet has small determinant resource or small disjoint-basis mass. The next B09 implication is precisely

`QFORM-TWOHUB-HIGHRANK-OR-LOCALIZED-LEAF-ROUTING-v1`:

> Given a quantitative two-row cross wedge from a physical hub pair to a disjoint bank, prove that the actual same-side bank operator either contains a determinant-balanced exact curvature packet that makes Theorem 3 quantitative, or itself supplies an already-paid high-rank/cross-volume/ridge smoother, or the mixed frame localizes on a bounded physical core which can be retained without conditioning away the third target direction.

The source-valid cancellation example from the preceding run is a mandatory regression test: no argument may select a favorable curvature component and ignore an arbitrary cancelling residual.

Full QFORM and full-target continuity remain **OPEN**.
