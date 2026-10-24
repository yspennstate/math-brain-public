# MOC4 account01/B07 r11 — exact covariance commutator closure and sharpness witness

Outcome: **ESSENTIAL_STEP_APPLIED**. Full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.

Execution context: `WITHOUT_VERIFIED_BRAIN`.

## Scope and dependencies actually consumed

Target: for normal complex `4 x 4` matrices `A,B`, prove

`det(A+B) in conv{ prod_i (a_i+b_{sigma(i)}) : sigma in S_4 }`.

This run continues the exact exterior-square reduction in the complementary-pair basis. The nonconstant support functional is

`S(U)=<D,K> + (1/2)<R,X>`, `O=Lambda^2 U in SO(6)`,

where `O` is written as a `3 x 3` array of real `2 x 2` blocks `B_{alpha beta}`,

`R_{alpha beta}=||B_{alpha beta}||_F^2/2`, `D_{alpha beta}=det B_{alpha beta}`,

and `X_{alpha beta}=Re(eta p_alpha q_beta)` with the exact spectral pair-products from the degree-two Cauchy--Binet term.

Latest complete campaign-lead result consumed and applied: **account03/B07 r13**, `MOC4-MSQR-CROSS-BLOCK-ANNIHILATION-v1` and `MOC4-MSQR-CROSS-SPLIT-RESERVE-v1`, source-bound handoff commit `73578304570fda959a94d9788b739fe9690586cd`. It gives the generic strict-sector split into (i) at least one mixed-Schur pair-Hessian boundary and (ii) all six pair Hessians negative definite; on the mixed-Schur branch a kernel vector annihilates the full Hessian cross-block and the fourth-order Lyapunov--Schmidt reserve acquires an additional nonnegative cross-split Schur-complement term.

Assigned partner result retained and applied on the boundary side: **account02/B08**, `MOC4-2PLUS2-EVC-TRANSVERSAL-CLOSURE-v1` (run `B08-20260922T053946Z-bf1307`, report blob `a361d4996c79854aa569c85a83b94ea43367b66d`), which closes the exact-four `2+2` common-block face outside its explicit double-interlacing sign chamber. The later account02/B08 run visible at this run's start had not yet supplied a completed result and was not promoted.

The immediate predecessor from account01/B07 is `MOC4-EXACT-SPECTRAL-COVARIANCE-RECONSTRUCTION-v1`: for a fixed block row `alpha`, define

`V_beta = tf(B_{alpha beta} B_{alpha beta}^T)`,

so that `sum_beta V_beta=0` and

`rho(V_beta)^2 := tr(V_beta^2)/2 = R_{alpha beta}^2-D_{alpha beta}^2`.

For two spectral coefficient differences `c,d in R^3`, let

`W(c)=sum_beta c_beta V_beta`, `W(d)=sum_beta d_beta V_beta`.

The prior run identified the cross-inner-product `<W(c),W(d)>_rho` as the first local datum not controlled by separate pair-anisotropy norm bounds. This run resolves that datum exactly and proves the resulting local ceiling is nevertheless sharp on a genuine true-unitary family.

## 1. Exact covariance commutator identity

Every real symmetric trace-free `2 x 2` matrix has the form

`V(x,y) = [[x,y],[y,-x]]`.

Under the isometry `V(x,y) <-> v=(x,y)`, one has

`rho(V)^2=x^2+y^2`, `<V,W>_rho=v dot w`,

and

`||[V(x,y),V(x',y')]||_F^2 = 8 det(v,v')^2`.                           (1)

Write `v_1+v_2+v_3=0`, as follows from block-row orthogonality. Since adding a constant to `c` or `d` does not change `W`, put

`a=c_1-c_3`, `b=c_2-c_3`, `r=d_1-d_3`, `s=d_2-d_3`,

`Delta = a s - b r`.

Then

`w(c)=a v_1+b v_2`, `w(d)=r v_1+s v_2`,

and therefore

`det(w(c),w(d)) = Delta det(v_1,v_2)`.                                 (2)

Let `P0=I-(1/3)11^T` and let

`S = [c;d] P0 [c;d]^T`.

A direct `2 x 2` determinant calculation gives

`det S = Delta^2/3`.                                                     (3)

Combining (1)--(3) proves the exact identity

**MOC4-COVARIANCE-COMMUTATOR-CLOSURE-v1**

`rho(W(c))^2 rho(W(d))^2 - <W(c),W(d)>_rho^2`

`= (3 det S / 8) ||[V_1,V_2]||_F^2`.                                   (4)

Because `V_3=-V_1-V_2`, the three row commutators agree up to sign, so the right side is independent of which pair is used.

There is an identical column theorem with

`V^R_alpha=tf(B_{alpha beta}^T B_{alpha beta})`.

### Direct formula in the observable nonconformality variables

Put

`q_beta = rho(V_beta)^2 = R_{alpha beta}^2-D_{alpha beta}^2`.

Closure gives

`<v_1,v_2>=(q_3-q_1-q_2)/2`,

hence the previously missing cross-inner-product is not an independent phase variable:

`<W(c),W(d)>_rho`

`= a r q_1 + b s q_2 + (a s+b r)(q_3-q_1-q_2)/2`.                      (5)

Also

`||[V_1,V_2]||_F^2 = 2 H(q)`,                                           (6)

where

`H(q)=2(q_1q_2+q_2q_3+q_3q_1)-(q_1^2+q_2^2+q_3^2) >= 0`.

Thus (4) is an exact Heron/area law for the three block nonconformalities. `H(q)=0` iff the three row covariance defects are collinear/commuting.

## 2. Exact slack decomposition: why the old eight-orientation ceiling is locally sharp

Let the prior exact reconstruction be

`E_alpha = G11 u^2 + 2 G12 t + G22 v^2`,                                (7)

where

`u=rho(W(c))`, `v=rho(W(d))`, `t=<W(c),W(d)>_rho`, `G=S^{-1}`.

Suppose the two genuine pair-Hessian bounds available at this row are

`u <= U`, `v <= V`.

The row-local Cauchy ceiling used in the predecessor is

`B_alpha = G11 U^2 + G22 V^2 + 2 |G12| U V`.                           (8)

For `G12 != 0`, put `eps=sign(G12)`. Subtracting (7) from (8) gives the **exact nonnegative slack decomposition**

`B_alpha-E_alpha`

`= G11(U^2-u^2) + G22(V^2-v^2)`

`  + 2|G12|(UV-uv) + 2|G12|(uv-eps t)`.                                (9)

The last term is the exact covariance-angle reserve. From (4), for `uv>0`,

`2|G12|(uv-eps t)`

`>= 2|G12|(uv-|t|)`

`= 2|G12| * [(3 det S/8)||[V_1,V_2]||_F^2]/(uv+|t|)`

`>= (3 |G12| det S / (8uv)) ||[V_1,V_2]||_F^2`.                         (10)

If the pair bounds are the inherited `U=2 sqrt(Q_1)`, `V=2 sqrt(Q_2)`, then

`2|G12|(uv-eps t)`

`>= (3 |G12| det S /(32 sqrt(Q_1 Q_2))) ||[V_1,V_2]||_F^2`              (11)

whenever `Q_1 Q_2>0`.

Therefore every genuinely noncommuting row gives an explicit strict decrement relative to the old row ceiling. More importantly, (9) shows that this mechanism is **sharp**: when the two pair budgets saturate and the covariance defects commute with the sign required by `G12`, there is no row-local reserve left.

So the predecessor's request for a cross-angle relation is now fully answered. A further bound depending only on this row's two pair norms and row closure cannot improve the eight-orientation ceiling uniformly; any additional uniform payment must be global (cross-row/column, full-Hessian, Cartan, subgroup-roof, or spectral-structure information).

## 3. Genuine source-valid sharpness witness; genericity does not force a positive commutator reserve

The sharpness branch is not an artifact of relaxing `Lambda^2 U` to an arbitrary block matrix. It contains a large true-unitary family.

For every real `U in SO(4)`, `Lambda^2 U` commutes with the Hodge star. In the signed complementary-pair basis

`(e12,e34 | e13,-e24 | e14,e23)`,

each `2 x 2` block commutes with the exchange matrix and therefore has the form

`B=[[m,n],[n,m]]`.

Then

`tf(BB^T)=2mn [[0,1],[1,0]]`,

so **all row covariance defects commute**, and because the blocks are symmetric the same is true for every column covariance triple. Hence every real `SO(4)` relative eigenbasis has zero commutator reserve in (4), simultaneously on all rows and columns.

This persists inside the fully nonzero, compound-nondegenerate true-unitary locus. An exact rational example is

`U =`

`[[ 11/14, -1/2, -1/14,   5/14],`
` [ -5/14, -1/2,-11/14,  -1/14],`
` [  1/14, -1/2,  5/14, -11/14],`
` [   1/2,  1/2,  -1/2,   -1/2]]`.

It satisfies `U^T U=I`, `det U=1`, all 16 entries are nonzero, and all 36 `2 x 2` minors are nonzero. In the basis above, `Lambda^2 U` has block rows

`[[-4/7, 2/7],[2/7,-4/7]],  [[-9/14,-3/14],[-3/14,-9/14]], [[1/14,5/14],[5/14,1/14]]`,

`[[-5/14,-1/14],[-1/14,-5/14]], [[2/7,-4/7],[-4/7,2/7]], [[-9/14,-3/14],[-3/14,-9/14]]`,

`[[9/14,3/14],[3/14,9/14]], [[-5/14,-1/14],[-1/14,-5/14]], [[-4/7,2/7],[2/7,-4/7]]`.

All nine block determinants are nonzero; all nine nonconformality quantities `R^2-D^2` are positive. Nevertheless every row and column covariance commutator is exactly zero.

Thus the implication

`generic true-unitary interior => some uniformly positive covariance-commutator payment`

is **false**. This is a source-valid counterexample to that proof mechanism, not a counterexample to MOC4.

## 4. Interaction with the latest lead result

The campaign lead's `MOC4-MSQR-CROSS-SPLIT-RESERVE-v1` is exactly of the type that survives the sharpness obstruction above: it uses the **full true-unitary Hessian**, not merely one row's covariance cone. At a mixed-Schur pair kernel `z`, positive semidefiniteness of `-H` gives full cross-block annihilation `Hz=0`, and the fourth-order gate acquires the nonnegative cross-split reserve

`3 <r,S_cross^+ r>`.

The present theorem shows why such a cross-split/global term is necessary. The row/column covariance-angle reserve can vanish identically on a six-dimensional genuine `SO(4)` family even with no zero entries and no zero two-minors.

The assigned partner's `MOC4-2PLUS2-EVC-TRANSVERSAL-CLOSURE-v1` remains the boundary complement: it removes the exact-four common-block face outside the explicit double-interlacing chamber. Hence the surviving proof problem is not a missing local covariance identity or an ordinary common-block edge.

## 5. Compact conditional end-to-end argument and first remaining implication

A support violation gives a positive-gap global true-unitary maximizer. Using the current team reductions, singular/repeated/common-block strata are reduced to explicit boundary obligations, while the generic core splits into:

1. **MSQR:** at least one genuine pair Hessian is mixed-Schur singular;
2. **NDI:** all six left/right pair Hessians are negative definite.

For either branch, (9)--(11) now give an exact quantitative payment whenever a row or column covariance triple is noncommuting. If this payment plus the already proved subgroup/endpoint reserves closes the support gap, that datum is safe.

The only way the covariance part can be simultaneously sharp is the commuting-covariance regime. This regime is genuinely source-valid and includes real `SO(4)` relative eigenbases, so it cannot be discarded by genericity.

The new first essential implication is therefore:

**`MOC4-GLOBAL-COMMUTING-COVARIANCE-PAYMENT-v1`.** At a positive-gap global maximizer satisfying the structured spectral formulas for `(K,X)`, prove that either

- some row/column commutator term from (10) supplies enough strict reserve, together with the current roofs/Hessian bounds, to pay the gap; or
- all relevant covariance triples commute, in which case use the resulting simultaneous singular-axis structure together with the lead's full-Hessian cross-split equations (MSQR) or the six negative-definite pair blocks (NDI) to force target safety.

Equivalently, on MSQR the immediate computational target is to express the lead's cross residual `r` in the commuting/noncommuting covariance variables and show that `r=0` plus the exact commutator equalities forces a safe Spin(4)/boundary configuration, while `r!=0` gives a positive global reserve. On NDI the corresponding target is a cross-row/column compatibility inequality; another row-local norm or angle bound cannot suffice by the exact sharpness witness above.

## 6. Exact verification performed in this run

Symbolic/rational checks performed locally (no remote model/API):

- for `V(x,y)`, `||[V,V']||_F^2=8 det(v,v')^2` exactly;
- `det([c;d] P0 [c;d]^T)=Delta^2/3` exactly;
- rational test `v1=(1,2)`, `v2=(3,-1)`, `v3=(-4,-1)`, `c=(2,-1,4)`, `d=(3,5,-2)` gives
  `rho(Wc)^2=290`, `rho(Wd)^2=685`, `<Wc,Wd>=-439`,
  and both sides of (4) equal `5929` exactly;
- the displayed rational `U` has determinant one, all 16 entries nonzero, all 36 two-minors nonzero, all nine exterior blocks invertible and nonconformal, and all row/column covariance commutators exactly zero.

No MOC4 proof or MOC4 counterexample is claimed. The substantive advance is an exact closure of the previously missing covariance cross-angle, a quantitative commutator reserve, and a genuine true-unitary sharpness/no-go showing that the next proof step must use global full-Hessian/spectral compatibility rather than another local covariance inequality.
