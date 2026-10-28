# account04/B08 MOC4 report — double-antipode mixed-Schur flat curve

Run: `20260922T101001Z-account04-B08-MOC4-r14`  
Status: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN**.  
Execution status: `WITHOUT_VERIFIED_BRAIN_RESEARCH`; `full_brain_connected=false`.

## Target and control

The target is the source-exact `n=4` Marcus–de Oliveira statement: for every complex normal `4 x 4` pair `A,B`, with eigenvalues `a_i,b_i` counted with multiplicity,

`det(A+B) in conv{ prod_i (a_i+b_{sigma(i)}) : sigma in S_4 }`,

including singular and repeated spectra.


## Exact incoming lead state

Consumed the latest complete MOC4 lead report:

`proofnet24/collective-MOC4/account03/B07/20260922T095337Z-account03-B07-MOC4-r12/REPORT.md`

Its theorem `MOC4-MSQR-ANTIPODE-BUDGET-v1` analyzes a genuine two-pair `SU(2) x SU(2)` orbit at a true-unitary global support maximizer. In its exact Bloch variables,

`f(x,y)=c+p.x+q.y+x^T M y`, `x,y in S^2`,

with the current maximum at `(e_3,e_3)`. Put

`lambda=p_3+m_33`, `mu=q_3+m_33`.

On a mixed-Schur singular direction choose unit tangent singular vectors `a,b` with

`a^T M_TT b=sqrt(lambda mu)`

and canonical kernel speeds

`alpha=sqrt(mu)`, `beta=sqrt(lambda)`.

The three exact finite antipode deficits are

`Delta_L=2 lambda`, `Delta_R=2 mu`,

`Delta_LR=2(lambda+mu-2m_33)`.

The lead proved

`J4=-(3/8) Delta_L Delta_R Delta_LR`

and, after Lyapunov–Schmidt elimination,

`E4=J4+3R <= 0`, `R=<beta#,A^+ beta#> >=0`,

hence

`R <= (1/8) Delta_L Delta_R Delta_LR`.

The lead left a determinant-specific positive-deficit payment inequality and the higher-order equality branch unpaid.

## Named OTHER-account result consumed

Consumed assigned partner account01/B09 run

`proofnet24/collective-MOC4/account01/B09/20260922T091722Z-b09-moc4-r11/`.

Its exact verifier exhibits a genuine rational orthogonal unitary with exactly one zero entry and all 36 two-minors nonzero. For actual complex spectral coefficients its degree-two Birkhoff-fiber roof is violated by the exact positive amount

`4662468244876966038 / 2231328125`,

while the determinant is nevertheless certified as a strict positive convex combination of three target permutation vertices. It is also not stationary: a genuine pair derivative is the positive rational

`237314454727650397056 / 2231328125`.

Therefore a zero entry, or even full nonvanishing of the two-minors away from that zero, does not justify the false degree-two spectral roof. The boundary argument below deliberately uses the exact global-maximizer and common-unitary two-pair geometry instead of that invalid relaxation.

## Compact conditional end-to-end argument

A target counterexample supplies a support direction and a true-unitary global maximizer above all 24 permutation endpoints. Existing genericization/continuity work reduces the generic branch to simple nonsingular spectra, while the lead's Hessian analysis splits the mixed-Schur singular case according to the exact finite deficit `Delta_LR`.

The strict branch `Delta_LR>0` retains the lead's determinant-specific payment problem. The first degenerate boundary is `Delta_LR=0`, where the global maximum ties its simultaneous left-right antipode. This run resolves the exact geometry of that boundary: the tie forces a one-parameter **physical true-unitary curve of global maxima**, and on the simple-kernel stratum it pays the lead's sixth-order Lyapunov–Schmidt reserve exactly. Thus `Delta_LR=0` is not an isolated mysterious sixth-order maximizer.

The remaining MOC4 work is then: (i) exclude/pay the genuinely positive-deficit mixed-Schur branch using determinant/exterior-square compatibility; (ii) handle the multiple-kernel sub-stratum; and (iii) close the lead's negative-definite interior branch. No target closure is claimed here.

## New theorem 1: `MOC4-MSQR-DOUBLE-ANTIPODE-FLAT-CURVE-v1`

Assume the lead's exact two-pair Bloch model at a genuine global maximum `(e,e)`, with `e=e_3`, and assume the unresolved scalar-strict mixed-Schur case `lambda,mu>0`. Let `a,b` be a saturated singular-vector pair with

`a^T M_TT b=sqrt(lambda mu)`.

If

`Delta_LR=0`,

then the two-point great-circle support on that same genuine `SU(2) x SU(2)` orbit has the exact factorization

`f(x(theta),y(phi))-f(e,e)`

`= -2 [ sqrt(lambda) sin(theta/2) cos(phi/2)`

`       - sqrt(mu) sin(phi/2) cos(theta/2) ]^2`,

where

`x(theta)=cos(theta)e+sin(theta)a`,

`y(phi)=cos(phi)e+sin(phi)b`.

Consequently the zero set contains the exact one-parameter curve

`sqrt(lambda) tan(theta/2) = sqrt(mu) tan(phi/2)`,

which joins `(theta,phi)=(0,0)` to the double antipode `(pi,pi)`. Every point on this curve is a genuine unitary global maximizer with exactly the same support value.

### Proof

Because `Delta_LR=0`, the double antipode `(-e,-e)` has the same support as `(e,e)`. Since `(e,e)` is a global maximum, so is `(-e,-e)`. Sphere stationarity at both points gives, for tangent projections,

at `(e,e)`:

`p_T+M_T3=0`, `q_T+M_3T=0`;

at `(-e,-e)`:

`p_T-M_T3=0`, `q_T-M_3T=0`.

Hence

`p_T=q_T=M_T3=M_3T=0`.

In particular all radial-tangent couplings vanish on the selected singular directions.

The equality `Delta_LR=0` gives

`m_33=(lambda+mu)/2`.

On the selected mixed-Schur singular pair, orient `a,b` so that

`m_ab=a^T M_TT b=sqrt(lambda mu)`.

Substitution into the exact Bloch form yields

`E(theta,phi)`

`= lambda(cos theta-1)+mu(cos phi-1)`

`  +(lambda+mu)/2 (cos theta-1)(cos phi-1)`

`  +sqrt(lambda mu) sin theta sin phi`.

Put `s=sin(theta/2)`, `c=cos(theta/2)`, `r=sin(phi/2)`, `d=cos(phi/2)`. Using `cos theta-1=-2s^2`, `sin theta=2sc` and the analogous formulas for `phi`, direct collection gives

`E(theta,phi)=-2( sqrt(lambda) s d - sqrt(mu) r c )^2`.

This proves both global nonpositivity on the selected product of great circles and the stated zero locus. Because these circles are actual coordinate `SU(2)` pair actions, the zero locus is a curve of true unitaries, not a stochastic surrogate.

## New theorem 2: `MOC4-MSQR-DOUBLE-ANTIPODE-LS6-PAYMENT-v1`

Retain the hypotheses above and suppose additionally that the mixed-Schur Hessian kernel is one-dimensional in the full local problem. Write

`A0=-D^2F(0) >=0`, `z in ker A0`,

`beta(Y)=D^3F(0)[z,z,Y]`,

`delta(Y)=D^4F(0)[z,z,z,Y]`.

Then on `Delta_LR=0`:

1. `R=<beta#,A0^+ beta#>=0` and in the simple-kernel case `beta#=0`;
2. along the lead's canonical kernel geodesic,

`J2=J3=J4=J5=0`,

`J6=-(5/2) lambda mu (lambda-mu)^2`;

3. the exact flat maximizing curve forces the sixth-order transverse reserve equality

`boxed: <delta#,A0^+ delta#> = (1/4) lambda mu (lambda-mu)^2`.

In particular, if `lambda=mu`, then this reserve is zero and the canonical kernel great-circle itself is exactly flat.

### Proof

The lead's quartic antipode budget becomes `R<=0` when `Delta_LR=0`, hence `R=0`. Cubic stationarity already gives `D^3F[z,z,z]=0`. With a one-dimensional kernel, `beta#` has no kernel component, and positivity of `A0^+` on the range gives `beta#=0`.

Set `A=sqrt(mu)`, `B=sqrt(lambda)`. The canonical kernel geodesic is `theta=At`, `phi=Bt`. The square factorization above becomes

`E_geo(t)=-2[B sin(At/2) cos(Bt/2)-A sin(Bt/2) cos(At/2)]^2`.

Exact differentiation gives

`J2=J3=J4=J5=0`,

`J6=-(5/2) A^2 B^2 (A^2-B^2)^2`.

The flat curve can be parameterized locally by

`theta=At`,

`phi=2 arctan( (B/A) tan(At/2) )`.

Its expansion is

`phi=Bt + B(A^2-B^2)t^3/12`

`    +(A^4B/120-A^2B^3/48+B^5/80)t^5+O(t^7)`.

Thus in Lie coordinates the flat curve has tangent `z` and a cubic transverse correction. Since every point of the curve is a global maximum, the full gradient vanishes along it. At order `t^3`, with `beta#=0`, transverse stationarity gives

`A0 y_3 = delta#/6`.

The order-six value coefficient is therefore

`J6/720 - <A0 y_3,y_3>/2 + delta(y_3)/6`

`= (J6 + 10 <delta#,A0^+delta#>)/720`.

But the exact curve has identically constant value, so this coefficient is zero. Hence

`<delta#,A0^+delta#>=-J6/10`

`=(1/4) lambda mu (lambda-mu)^2`.

When `lambda=mu`, the square on the canonical geodesic vanishes identically, giving the balanced exact-flat sub-stratum.

### Multiplicity caveat

If the saturated mixed singular value has multiplicity greater than one, the Hessian kernel can have dimension greater than one. The square factorization and the physical flat zero locus still hold for each selected saturated singular direction, but the simple-kernel conclusion `beta#=0` and the unique pseudoinverse payment identity require a kernel-projection analysis. That is an explicit degenerate branch, not silently absorbed into the theorem.

## Exact verification

`verify_msqr_double_antipode.py` checks by exact symbolic algebra:

- the independent two-angle square factorization via rational half-angle variables;
- the exact flat-curve equation;
- `J2=J3=J4=J5=0` and the stated `J6`;
- the standard simple-kernel Lyapunov–Schmidt sixth-order coefficient `J6+10S`;
- the required reserve `S=(1/4)lambda mu(lambda-mu)^2`;
- exact geodesic flatness in the balanced case `lambda=mu`.

The captured output terminates with

`PASS MOC4-MSQR-DOUBLE-ANTIPODE-FLAT-CURVE-v1`.

This is an algebraic verification of the formulas, not a machine proof of full MOC4.

## What this changes

The lead's higher-order equality branch at `Delta_LR=0` is now geometrically identified. A tied double antipode on a scalar-strict mixed-Schur boundary forces an exact continuum of equal-support true-unitary maxima connecting the two antipodes. On the simple-kernel stratum, the sixth-order pseudoinverse reserve is not merely bounded: it is exactly determined by `lambda,mu`.

This matters for the extremal classification. A hypothetical counterexample on this boundary cannot be an isolated nonmonomial stationary point or an isolated sixth-order maximizer. It belongs to a positive-dimensional maximizing orbit stratum. Any target-level exclusion of this branch should therefore exploit that exact family (for example through simultaneous endpoint/subgroup roofs or exterior-minor compatibility), rather than treat it as a generic isolated critical point.

The account01/B09 adversary also shows why the next step cannot be replaced by a degree-two Birkhoff-fiber roof: that roof is false on a genuine zero-entry unitary even though the target hull itself remains valid there.

## First remaining implication

The first essential mixed-Schur implication can now be sharpened to

`MOC4-MSQR-POSITIVE-DOUBLE-ANTIPODE-PAYMENT-v1`:

> At a positive-gap true-unitary global support maximizer in the simple nonsingular generic regime, on a simple mixed-Schur singular block with `Delta_LR>0`, prove the determinant-specific same-unitary payment
>
> `R >= (1/8) Delta_L Delta_R Delta_LR`,
>
> or directly derive the target support bound from the exact exterior-square compatibility.

The `Delta_LR=0` boundary is no longer an unknown higher-order local shape; it is the flat-family degeneracy above. The separate multiple-kernel and all-pair-negative-definite branches remain open.

## Verdict

`ESSENTIAL_STEP_APPLIED`. This run exactly characterizes the tied-double-antipode mixed-Schur boundary and derives its simple-kernel sixth-order payment identity. It does **not** prove MOC4, does not promote a nonmonomial maximizer to a counterexample, and does not claim the remaining positive-deficit payment inequality.
