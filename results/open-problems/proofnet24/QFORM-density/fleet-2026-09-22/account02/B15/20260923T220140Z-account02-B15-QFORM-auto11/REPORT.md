SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-23T22:01:40Z.
attacking: a product-preserving grouped pivot/leaf receiver that tolerates dense cross-pair couplings; use the completed ruled one-sheet theorem on an actual target family and keep rough essential boundedness logically prior to continuity.

# account02/B15 — grouped determinant receiver, ruled rough bridge, and a full-target constant-2 chamber

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T220140Z-account02-B15-QFORM-auto11`  
Status: `GROUPED_D_LEAF_RECEIVER_PROVED / SHARP_D2 / RULED_ROUGH_BRIDGE_CHECKED / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The unrestricted theorem remains OPEN. The new result below closes a genuine dense-cross-coupling extension of the newest partner branch, but it assumes that one original-coordinate leaf group has zero internal quadratic block. The first unpaid implication in this branch is therefore:

> absorb a nonzero leaf-leaf quadratic block while retaining the grouped determinant payment, or prove a product-preserving structural reduction that routes every remaining three-large-eigenvalue matrix into this receiver or another already-paid receiver.

Small operator norm of that leaf block is not a small random perturbation under arbitrary unbounded cap-one laws. Globally the product-provenance-sensitive minority/two-sheet problem and the no-uniform-single-minor structural gap remain; the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids replacing the former by a generic X-ray estimate.

## 2. Grouped d-leaf determinant receiver

### Theorem 2.1 — `QFORM-GROUPED-D-LEAF-DET-v1`

Let `d>=2`. Select `2d` ORIGINAL coordinates and write them as two groups

`P=(P_1,...,P_d)`, `L=(L_1,...,L_d)`.

Condition on all remaining original coordinates `W=w`. Suppose the selected physical principal block, in the `(P,L)` ordering, is

`[[C,M],[M^T,0]]`,                                                   (2.1)

where `C` is an arbitrary real symmetric `dxd` matrix and `M` is invertible. Every outside quadratic coefficient and every coupling to `W` is arbitrary. Then for independent cap-one coordinate densities,

`boxed( P(Q in I) <= [d/(d-1)] |det M|^(-1/d) |I| )`               (2.2)

for every interval `I`. Consequently

`boxed( ||p_Q||_infinity <= [d/(d-1)] |det M|^(-1/d). )`            (2.3)

Moreover the same law has a canonical density in `C_0(R)` with the same height bound; this continuity conclusion is proved only after (2.2)-(2.3), not used to obtain them.

### Proof of the height bound

After conditioning `W=w`, the polynomial is

`Q_w(P,L)=P^T C P+2P^TML+alpha(w)^TP+beta(w)^TL+c(w).`             (2.4)

The selected coordinates remain independent with the original density caps. Fix `P=p`. Put

`a(p,w)=2M^T p+beta(w)`.                                            (2.5)

The only remaining random leaf term is the affine linear form `a^T L`. If `a!=0`, choose `j` with

`|a_j|=||a||_infinity`.

The scaled variable `a_j L_j` has density at most `1/|a_j|`. Convolution with the independent probability law of the other leaf terms cannot increase `L^infinity`. Therefore, for every interval `I`,

`P(Q_w in I | P=p) <= |I| / ||a(p,w)||_infinity.`                  (2.6)

The exceptional point set `a=0` has `P`-probability zero because `M` is invertible and `P` has an absolutely continuous density.

Now `A_w=2M^T P+beta(w)` has a `d`-dimensional density bounded by

`B=1/(2^d |det M|)`,                                                 (2.7)

since the product density of `P` is at most one and the affine Jacobian is `2^d|det M|`. Thus layer cake in the `l^infinity` norm gives

`E[1/||A_w||_infinity]`
` = int_0^infinity P(||A_w||_infinity < 1/t) dt`
` <= int_0^infinity min(1, B(2/t)^d) dt`
` = |det M|^(-1/d) + |det M|^(-1/d)/(d-1)`
` = [d/(d-1)] |det M|^(-1/d).`                                     (2.8)

The estimate is independent of `w`, every affine term and the arbitrary pivot block `C`. Integrating (2.6) in `p` and then in `w` proves (2.2). The interval domination itself yields absolute continuity and the essential density height (2.3). No output continuity has entered.

### d=2 consequence

For two pivots and two leaves,

`boxed( ||p_Q||_infinity <= 2/sqrt(|det M|). )`                    (2.9)

In particular, this handles an arbitrary dense `2x2` cross-coupling matrix `M`; it is not restricted to two separated hyperbolic pairs.

## 3. Sharpness of the d=2 determinant constant

The factor `2` in (2.9) is sharp. Let `P_1,L_1,P_2,L_2` be iid `Uniform[-1/2,1/2]`, take `C=0`, `M=I_2`, and

`Q=2(P_1L_1+P_2L_2).`                                              (3.1)

For one product term `T=2P_1L_1`,

`p_T(t)=log(1/(2|t|)) 1_{0<|t|<1/2}.`                              (3.2)

The two terms in (3.1) are independent, so

`p_Q(0)=int_{-1/2}^{1/2} log^2(1/(2|t|)) dt`
`      =int_0^1 log^2(1/u) du`
`      =2.`                                                         (3.3)

Thus the determinant scaling and the coefficient in (2.9) cannot be improved for this receiver class.

## 4. Partner result actually applied: continuity after the height is paid

The newest designated partner result is account03/B15 at

`math-open-problems@07ce749022db2bb11f390431409b013fe30457cc`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260923T212617Z-account03-B15-qform-auto12/REPORT.md`.

Its Theorem 2.1 says that a measurable mixture of conditional convolutions `a_omega*b_omega`, with `a_omega in L^1 cap L^infinity`, `b_omega in L^1`, and an integrable conditional `L^infinity` bound, has a canonical `C_0` density and preserves the averaged height.

Apply it here with `omega=(w,p)`. For almost every `(w,p)`, at least two coefficients of `a(p,w)` are nonzero: the exceptional set where at most one is nonzero is a finite union of affine subspaces of codimension at least `d-1`, hence has zero `P`-measure. Choose a largest coefficient as the bounded component; the sum of the remaining nonzero leaf terms is an absolutely continuous probability component. After absorbing the output shift from (2.4) into one convolution factor, the partner's dominating function is precisely

`M(w,p)=1/||a(p,w)||_infinity`,                                    (4.1)

whose conditional expectation is bounded by (2.8), uniformly in `w`. The partner theorem therefore gives

`boxed( p_Q in C_0(R) )`                                           (4.2)

with no height loss from (2.3). This use is logically one-way: the interval bound was already proved; the partner theorem supplies the stronger continuous representative afterwards.

## 5. Completed ruled result applied to a real full-target inequality

I independently rechecked the owner-pinned completed Theorem C in

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

For an exact rank-three signature `(+,+,-)` form with eigenvalue magnitudes `lambda_1,lambda_2,mu>=1`, its majority one-sheet side satisfies

`p_+(s) <= (lambda_1 lambda_2 mu)^(-1/2)`
`          * int_0^{2pi} [sin^2(theta)/lambda_1 + cos^2(theta)/lambda_2 + 1/mu]^(-1/2) dtheta`
`       <= pi sqrt(2)`                                              (5.1)

for the nonnegative side relative to the critical value. The source's ruling has exact coarea measure `(1/2)dtheta dt`; the line parameter is not arclength, so the reciprocal ruling speed is essential before invoking the two-dimensional product-projection cap.

Now take four arbitrary independent cap-one variables `X,Y,Z,U` and

`Q=2XY+Z^2+2ZU.`                                                    (5.2)

Its matrix has eigenvalues

`1, -1, (1+sqrt(5))/2, (1-sqrt(5))/2`,                             (5.3)

so it is a genuine owner-target matrix with three eigenvalues of modulus at least one.

Condition on `U=u`. Then

`Q_u=2XY+(Z+u)^2-u^2.`                                              (5.4)

The deterministic translation `Z -> Z+u` preserves the original-coordinate product structure and the cap. The quadratic part of `2XY+(Z+u)^2` has eigenvalue magnitudes `(1,1,1)` and signature `(+,+,-)`. Applying (5.1) conditionally and averaging `u` gives the concrete majority-submeasure inequality

`boxed( P(Q in I, Q>=-U^2) <= pi sqrt(2) |I|. )`                   (5.5)

Equivalently, for every `epsilon>0` and `y`,

`boxed( E[(epsilon-|Q-y|)_+ 1_{Q>=-U^2}] <= pi sqrt(2) epsilon^2. )` (5.6)

The new grouped theorem pays the whole law more strongly. In the ordering `P=(X,Z)`, `L=(Y,U)`, (5.2) has

`C=diag(0,1)`, `M=I_2`, leaf block zero. Hence

`boxed( ||p_Q||_infinity <=2,  p_Q in C_0(R). )`                   (5.7)

In particular the previously unruled minority submeasure also obeys

`boxed( P(Q in I, Q<-U^2) <=2|I|. )`                               (5.8)

This pays the two-sheet complement in this actual target family by retaining the independent external coordinate `U` inside the grouped bilinear receiver, not by the refuted generic X-ray shortcut.

## 6. Independent rough-input audit of the ruled bridge

The one-sheet height can be passed to arbitrary measurable cap-one marginals without smuggling in continuity.

For the three active ORIGINAL coordinates, set

`f_i^(eta)=f_i * gamma_eta`.

Then

`||f_i^(eta)||_infinity<=1`,                                       (6.1)

independence is preserved, and

`||f_i^(eta)-f_i||_1 ->0.`                                         (6.2)

Consequently the active product laws obey

`||prod_i f_i^(eta)-prod_i f_i||_1`
` <= sum_i ||f_i^(eta)-f_i||_1 ->0.`                               (6.3)

When outside coordinates have been conditioned, completing the square uses only deterministic translations of these original coordinates, so (6.3) is unchanged and no spectral-basis independence is asserted. Total variation contracts under deterministic quadratic pushforward. It also contracts under restriction to the fixed majority event relative to the conditional critical value. Therefore the smooth interval domination supplied by the ruling passes to the rough majority submeasure with exactly the same constant.

At the cone vertex there is no hidden atom: the zero set of the nonzero quadratic polynomial has Lebesgue measure zero under the absolutely continuous product law. Thus the limiting statement is an essential-density/interval bound. It is not a continuity theorem. In the grouped theorem, by contrast, continuity is obtained separately from the partner endpoint convolution compiler only after the height has been paid.

## 7. What the new receiver says about the near-null branch

The newest partner branch treated the sparse block, in coordinates `(X,Y,Z,U)`,

`[[a,b,0,0],`
` [b,0,0,0],`
` [0,0,gamma,c],`
` [0,0,c,0]]`

and obtained `4/sqrt(|bc|)` by conjugate `L^p*L^q` convolution, uniformly in the near-null curvature `gamma`.

Reorder as pivots `(X,Z)` and leaves `(Y,U)`. Then

`C=diag(a,gamma)`, `M=diag(b,c)`,                                  (7.1)

so Theorem 2.1 immediately sharpens that branch to

`boxed( ||p_Q||_infinity <=2/sqrt(|bc|). )`                        (7.2)

More importantly, `M` can now be an arbitrary invertible `2x2` matrix and `C` arbitrary symmetric. Thus nonzero cross-pair couplings `XU` and `ZY`, and a pivot coupling `XZ`, are allowed at no extra analytic cost. The near-null diagonal `gamma` never appears in the bound.

The exact obstruction is correspondingly narrower: arbitrary curvature INSIDE the pivot group is harmless here; arbitrary dense pivot-to-leaf coupling is harmless provided its determinant is paid; what remains outside this receiver is internal leaf curvature or lack of a quantitatively nondegenerate grouped cross determinant.

## 8. Regularity ledger

1. **Absolute continuity.** In this branch it follows directly from (2.2). More generally, for any nonzero quadratic form under an absolutely continuous joint law, local coarea away from `ker A` gives qualitative absolute continuity; this has no universal-height content.
2. **Essential boundedness.** Equations (2.2)-(2.3) and (5.5) are direct interval bounds. No continuity premise is used.
3. **Continuous density.** Equation (4.2) follows later from the partner endpoint convolution theorem and the already-integrable height dominator. It is a stronger representative statement, not the source of (2.3).
4. **Full target.** Still OPEN. The three-large-eigenvalue hypothesis alone does not guarantee a uniformly nondegenerate physical grouped cross determinant with zero leaf block, and the live corrections prohibit pretending otherwise.

## 9. Next exact step

Try to replace the zero leaf block in (2.1) by a nonzero `D` while retaining product provenance. The indefinite rank-two leaf block can have a logarithmic critical singularity, so the useful quantity is not a worst conditional leaf height. The natural next question is whether averaging that logarithmic singularity against the affine coefficient vector `2M^TP+beta` yields a determinant-paid bound before any fiber supremum. A successful estimate here would directly extend (2.9) into the dense transverse-coupling chamber identified by the partner.
