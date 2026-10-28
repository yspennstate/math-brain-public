# account03/B07 MOC4 report — mixed-Schur antipode budget

Run: `20260922T095337Z-account03-B07-MOC4-r12`  
Status: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN**.  
Execution status: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## Target and fresh control

For every complex normal `4 x 4` pair `A,B` with spectra `a_i,b_i`, prove

`det(A+B) in conv{ prod_i(a_i+b_{sigma(i)}) : sigma in S_4 }`,

including singular and repeated spectra.


## Newest compatible n=4 state

The incoming B07 state is the genuine-unitary support-functional reduction. For a support direction `eta`,

`h_eta(U)=Re(conj(eta) det(D_a+U D_b U*))`,

and a counterexample is equivalent to a true unitary global maximizer `U_*` with support above all 24 permutation endpoints.

On the mixed-Schur singular branch (`MSQR`), the previous lead theorem `MOC4-MSQR-HIGHER-LS-RESERVE-v1` supplies the full Lyapunov-Schmidt quartic condition. In real Lie-algebra coordinates around a global maximizer, with

`A=-D^2F(0)>=0`, `z in ker A`, `beta(Y)=D^3F(0)[z,z,Y]`,

and `R=<beta#,A^+ beta#> >= 0`, one has

`E4 = D^4F[z,z,z,z] + 3 R <= 0`.

If `E4=0`, the previous run also derived exact fifth- and sixth-order necessary conditions. Thus the first unpaid MSQR piece entering this run was the strict branch `E4<0` and the question of converting its local reserve into determinant-specific finite support information.

## Named other-account result consumed

Consumed the preserved source-bound statement of assigned partner **account04/B08** theorem `MOC4-PAIR-FLAT-BOUNDARY-v1` from the latest complete B07 predecessor. It states that the support restricted to a genuine coordinate row/column `SU(2)` pair orbit is exactly Bloch-affine and that a flat pair orbit through a global maximizer can be moved, at equal support, to a true unitary with a zero entry. This is exactly the true-unitary pair geometry used below; no arbitrary bistochastic array is introduced.

Provenance note: the predecessor binds that theorem to an historical account04/B08 scientific report/commit, but that historical commit does not resolve from current main in this invocation. The current account04/B08 r13 directory has only its immutable `START.json` so far. Therefore this run treats the theorem as **PRESERVED_PREDECESSOR_SOURCE-BOUND**, not as independently re-fetched upstream current-main evidence, and makes no claim about a newer B08 result.

## Mechanism change

The previous run pushed local Lyapunov-Schmidt jets to orders five and six. This run changes mechanism on the same target: use the exact finite antipodes of the same genuine `SU(2) x SU(2)` pair orbit. The result turns the local quartic term into an exact product of three finite support deficits.

## New exact theorem: `MOC4-MSQR-ANTIPODE-BUDGET-v1`

Consider the exact two-pair Bloch form supplied by the genuine pair-orbit geometry,

`f(x,y)=c+p.x+q.y+x^T M y`, with `x,y in S^2`,

and suppose `(e3,e3)` is a global maximum. Sphere stationarity gives

`p_T=-(M e3)_T`, `q_T=-(M^T e3)_T`.

Write

`lambda=p_3+m_33`, `mu=q_3+m_33`.

On a mixed-Schur kernel choose unit tangent vectors `a,b in R^2` such that

`a^T M_TT b = sqrt(lambda mu)`

and use the canonical kernel speeds

`alpha=sqrt(mu)`, `beta=sqrt(lambda)`.

The genuine unitary pair orbit through the maximizer has Bloch great-circle coordinates

`x(t)=cos(alpha t)e3+sin(alpha t)a`,

`y(t)=cos(beta t)e3+sin(beta t)b`.

After using sphere stationarity, its exact support difference is

`f(t)-f(0)`

`= lambda(cos(alpha t)-1) + mu(cos(beta t)-1)`

`  + m_33(cos(alpha t)-1)(cos(beta t)-1)`

`  + m_a3 sin(alpha t)(cos(beta t)-1)`

`  + m_3b(cos(alpha t)-1)sin(beta t)`

`  + m_ab sin(alpha t)sin(beta t)`.

The quadratic term vanishes by the mixed-Schur kernel equation. Since the base point is a maximum, the cubic derivative on this kernel ray vanishes too, giving

`m_a3 beta + m_3b alpha = 0`.

Now define three **finite support deficits on this same true-unitary pair orbit**:

`Delta_L  = f(e3,e3)-f(-e3,e3) = 2 lambda`,

`Delta_R  = f(e3,e3)-f(e3,-e3) = 2 mu`,

`Delta_LR = f(e3,e3)-f(-e3,-e3) = 2(lambda+mu-2m_33)`.

All three are nonnegative because `(e3,e3)` is a global maximum. Direct differentiation gives

`J4 := d^4/dt^4 f(x(t),y(t))|_{t=0}`

`= 3 lambda mu (2m_33-lambda-mu)`

and therefore the exact identity

`boxed:  J4 = -(3/8) Delta_L Delta_R Delta_LR.`

This identity is finite, source-valid and same-unitary: the three deficits are values reached by actual antipodal moves in the same pair subgroup that generated the mixed-Schur kernel.

Combining it with the previous full Lyapunov-Schmidt inequality

`E4 = J4 + 3R <= 0`, `R=<beta#,A^+beta#>`,

gives the exact **antipode reserve budget**

`boxed:  R <= (1/8) Delta_L Delta_R Delta_LR`,

and

`boxed:  E4 = -(3/8) Delta_L Delta_R Delta_LR + 3R.`

Hence:

1. the strict MSQR branch is exactly `R < (1/8) Delta_L Delta_R Delta_LR`;
2. the quartic equality branch is exactly equality in that budget;
3. if any one of the three finite antipode deficits vanishes, the budget forces `R=0` and `E4=0`, so a strict MSQR point necessarily has all three finite pair-orbit antipode deficits positive.

The scalar-strict branch entering MSQR has `lambda,mu>0`; scalar saturation is already handled by the earlier Spin(4)-to-zero-face reduction. Thus the canonical kernel scaling above is legitimate on the unresolved strict MSQR branch.

## Exact check

A symbolic checker committed beside this report imposes the mixed-Schur singular value relation and cubic stationarity, then differentiates the exact trigonometric pair-orbit formula. It returns

`J2=0`,

`J3=0`,

`J4=3*lambda*mu*(-lambda+2*m33-mu)`,

`J4+(3/8)*Delta_L*Delta_R*Delta_LR=0`.

This verifies the coefficients and signs of the identity; it is not evidence that the remaining determinant-specific payment inequality is true.

## Smallest conditional full deduction now

On the dense simple, nonsingular spectral set supplied by the existing genericization reduction, it is enough to prove the following two target-level pieces.

**MSQR payment/equality closure.** At every positive-gap mixed-Schur global maximizer, prove the determinant-specific same-unitary compatibility implication

`MOC4-MSQR-ANTIPODE-PAYMENT-v1:`

`R >= (1/8) Delta_L Delta_R Delta_LR`.

Together with the necessary antipode budget proved above, this forces equality, so the entire strict `E4<0` MSQR branch disappears. The remaining equality branch is then subject to the already-derived LS5 identity and LS6 positive-reserve inequality; prove that those determinant tensors fail unless the support is target-safe.

**NDI closure.** Exclude a positive-gap global maximizer for which all six genuine pair Hessian blocks are negative definite.

If those two pieces hold on the dense simple/nonsingular set, the prior perturbation/continuity reduction gives singular and repeated spectra as well, because both the determinant support value and the 24 endpoint support values vary continuously with the spectral data.

## Direct attack on the first missing implication

The first missing implication is therefore no longer an unstructured local fourth-order estimate. It is the concrete inequality

`R >= (1/8) Delta_L Delta_R Delta_LR`

for the actual determinant support function. The right side is now completely identified by three finite true-unitary support drops. This gives a specific bridge to attack with the retained same-unitary `P/R/D`, exterior-square and cross-block Hessian identities: the pseudoinverse cubic reserve must be compared to a product of finite pair-orbit deficits, rather than to an unspecified quartic coefficient.

The abstract Bloch-affine geometry alone cannot prove that lower bound: its universal maximum condition only gives the opposite inequality proved above. Thus the next run must use determinant/exterior-square compatibility essentially. A failure to derive that lower bound from the determinant structure would be informative and should trigger a different same-unitary mechanism rather than a bistochastic relaxation.

## Verdict

`ESSENTIAL_STEP_APPLIED`. The strict mixed-Schur branch has been converted into an exact finite antipode reserve problem on the same true-unitary orbit. Full MOC4 remains **OPEN**: `MOC4-MSQR-ANTIPODE-PAYMENT-v1`, the LS5/LS6 equality payment, and the NDI branch are not yet proved.
