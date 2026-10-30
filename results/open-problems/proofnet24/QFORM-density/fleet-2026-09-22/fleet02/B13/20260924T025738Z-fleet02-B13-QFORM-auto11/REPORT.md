SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-24T02:57:38.635043Z.
attacking: partner r41's two-projective-line survivor; eliminate its finite physical centers by product-preserving conditioning, pay the exact finite-direction/finite-diagonal-support endpoint by grouping before curvature, and isolate why the O(rho^-1/6) strip itself must remain inside the phase.

# fleet02/B13 r40 — finite-center elimination, exact finite-direction payment, and the rough two-strip obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T025738Z-fleet02-B13-QFORM-auto11`  
Role: extremal product laws / complementary constructions and source-valid counterexamples  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING REDUCTIONS AND A PAID EXACT ENDPOINT / FULL UNRESTRICTED QFORM OPEN / GLOBAL CONTINUITY OPEN**.

No moments, compact support, log-concavity, connected support, diagonal-basis assumption, post-rotation independence, attained global bathtub optimizer, common support diameter, fixed fragment count, or perturbative deletion of a coefficient-small quadratic tail is used.

## 1. First unpaid implication

The first unpaid implication is now

`QFORM-CENTERFREE-TWOSTRIP-DIAGONAL-BANK-RECEIVER-v1`:

> In the hard diffuse exact-rank-two survivor, after conditioning away the at most ten physical centers supplied by fleet03/B13 r41, prove an affine-uniform density/small-ball bound for the two original-coordinate banks whose rank-two coefficient rows lie in `O(rho^-1/6)` strips around two projective lines, while retaining the strip terms and arbitrary diagonal curvature exactly. Otherwise construct a genuine bounded-finite-union product-indicator counterexample in this center-free two-strip normal form.

The exact-line finite-diagonal-support endpoint is discharged below; the remaining difficulty is genuinely the aggregate rough strip and/or unboundedly distributed diagonal curvature.

## 2. Fresh source-pinned premises


The latest completed compatible designated-partner result is fleet03/B13 r41, canonical report at

`yspennstate/math-open-problems@37177f7694c9aab73604b36c452e2a92c612aad4`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260924T023349Z-fleet03-B13-qform-r41/REPORT.md`.

In the hard diffuse exact-rank-two chamber

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i ||u_i||^2<=1/3`, `s_3(A)>=1`,

it proves that for every sufficiently large slab witness ratio `rho` there are a physical pivot `k`, a set `Z` with `|Z|<=9`, and two latent lines `ell_0,ell_1` such that every row outside `Z union {k}` obeys

`dist(u_i,ell_0)<rho^(-1/6)`

or

`dist(u_i,ell_1)<24.540 rho^(-1/6)`.                                (2.1)

It also proves the simultaneous low-leverage cancellation estimate

`|tau_ij|<1204.339 rho^(-1)`                                        (2.2)

for every pair in its stated transverse scope, after deleting at most seven high-leverage rows. This is the partner result used below at an actual reduction, not merely cited as status.

The owner-required pinned Fourier source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Its completed unconditional fifth-volume theorem `D5` says for every disjoint physical cross block `M=A[I,J]`,

`||p_Q||_infty <=5 sqrt(2e) e_5(M^T M)^(-1/10)`.                  (2.3)

The latest compatible current versions were also reread; the counterexample search still reports no valid counterexample, but none of its numerical observations is used as proof here.

Two additional completed tools are used only at their proved scopes:

1. fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical commit `8dd33c1abd4fd64140f59032feda2b13d4351da5`, which implies that any normalized scalar linear form `sum_i a_i X_i` with `sum_i a_i^2=1` has density at most `sqrt(e)` for independent cap-one inputs;
2. the current proved fixed-dimensional theorem in `GEOMETRIC_ROUTE_REPORT.md`: for every `N`, every `N`-variable cap-one product law and every symmetric `N x N` matrix with at least three eigenvalues of modulus at least one (arbitrary linear terms allowed),

`||p_Q||_infty <=250 N (8+log N)`.                                 (2.4)

## 3. New theorem: finite physical centers can be conditioned away at zero slab-ratio cost

### Theorem 3.1 — `QFORM-FINITE-CENTER-CONDITIONING-v1`

Let `E` be any set of original coordinates and `B=E^c`. Let

`Q(X)=X^T A X`

with independent cap-one coordinates. If for some interval `J`

`rho=P(Q(X) in J)/|J|`,                                             (3.1)

then there is a center value `y` in the essential support of `X_E` such that the conditional polynomial

`Q_y(x_B)=x_B^T A_BB x_B+2(A_BE y)^T x_B+c(y)`                    (3.2)

satisfies

`P(Q_y(X_B) in J)/|J| >=rho`.                                      (3.3)

Conversely, a density bound for every `Q_y` that is uniform in the affine term controls the original form with the same constant.

#### Proof

Independence gives the original product law on `X_B` after conditioning on `X_E=y`. Fubini gives

`P(Q(X) in J)=int P(Q_y(X_B) in J) dP_{X_E}(y)`.                   (3.4)

The average in (3.4) cannot exceed every integrand, proving (3.3). The converse follows by integrating uniform conditional density bounds. No transformed coordinate is asserted independent. `QED`

### Application to partner r41

Take

`E=Z union {k}`.                                                     (3.5)

Then `|E|<=10`. By (2.1), after this lossless original-coordinate conditioning every remaining physical row belongs to one of two projective strips and every remaining input keeps its original cap-one law. Thus the named centers themselves are not a genuine obstacle: the unpaid receiver may be assumed **center-free**, at the price of allowing an arbitrary affine term. This is the first concrete application of r41.

For finite-union product-indicator witnesses the statement is exact rather than asymptotic. Conditioning a center value leaves each unconditioned coordinate uniform on precisely the same unit-measure set. Fragmentation and remote support are preserved.

## 4. Exact algebra of the center-free two-strip form

Partition the remaining coordinates `B=B_0 disjoint_union B_1` according to the partner line. Choose unit directions `v_b` spanning `ell_b`. For `i in B_b` write orthogonally

`u_i=a_i v_b+e_i`,                                                   (4.1)

and let `U^(0)` have row `a_i v_b`, `F=U_B-U^(0)`. Then

`||e_i||<delta_b`,
`delta_0=rho^(-1/6)`, `delta_1=24.540 rho^(-1/6)`.                 (4.2)

The actual quadratic coefficient block is exactly

`A_BB=D_B+U^(0)Lambda U^(0)^T+T`,                                  (4.3)

where

`T=U^(0)Lambda F^T+F Lambda U^(0)^T+F Lambda F^T`.                 (4.4)

No term in `T` is deleted.

If

`L_b(x)=sum_{i in B_b} a_i x_i`,
`alpha=v_0^T Lambda v_0`, `beta=v_0^T Lambda v_1`,
`gamma=v_1^T Lambda v_1`,                                         (4.5)

then

`x^T U^(0)Lambda U^(0)^T x`
` =alpha L_0(x)^2+2 beta L_0(x)L_1(x)+gamma L_1(x)^2`.             (4.6)

The banks are disjoint sets of original coordinates, so `L_0(X)` and `L_1(X)` are functions of independent coordinate banks. Formulae (4.3)-(4.6) are therefore a product-preserving normal form; the difficulty is entirely that the retained `T` can have order-one aggregate size despite the rowwise smallness in (4.2).

## 5. New paid endpoint: exact finite directions plus finitely supported diagonal curvature

The following grouping theorem is useful beyond the immediate rank-two chamber.

### Theorem 5.1 — `QFORM-FINITE-DIRECTION-FINITE-DIAGONAL-GROUPING-v1`

Let

`A=D+U Lambda U^T`,                                                  (5.1)

where `D` is diagonal, `U` has orthonormal columns (of arbitrary finite rank), and `Lambda` is real diagonal. Let `C` be a set of named physical centers. Assume:

1. `A` has at least three eigenvalues of modulus at least one;
2. outside `T:=C union supp(D)`, the nonzero rows of `U` lie in at most `m` one-dimensional subspaces of the latent coefficient space;
3. `N:=|T|+m` is finite.

Then for every independent cap-one input vector,

`boxed:
 ||p_(X^T A X)||_infty <=250 e N (8+log N).}`                     (5.2)

The bound is independent of the original dimension, multiplicities within the direction classes, support geometry of the input laws, and the rank/signature/size of the latent piece beyond the three-large-eigenvalue hypothesis.

#### Proof

Partition `[n]\\T` into direction classes `G_1,...,G_m`. For every nonempty class choose a nonzero latent representative `v_a` and scalars `c_i` with

`u_i=c_i v_a`, `i in G_a`.                                         (5.3)

Put

`alpha_a=(sum_{i in G_a}c_i^2)^(1/2)`,
`w_a=alpha_a^(-1) sum_{i in G_a} c_i e_i`.                         (5.4)

The vectors `w_a` are physical unit vectors with disjoint supports, and together with the singleton vectors `e_t`, `t in T`, form an orthonormal family. Let `H` be their span.

If `x perpendicular H`, then `x_t=0` for every `t in T`, and for every direction class

`sum_{i in G_a}c_i x_i=0`.                                         (5.5)

Since `D` is supported on `T`, (5.5) implies

`D x=0`,
`U^T x=sum_a v_a sum_{i in G_a}c_i x_i=0`,                          (5.6)

hence `A x=0`. Because `A` is symmetric, `A` is supported on `H`. Its compression `M=A|_H` therefore has exactly the nonzero eigenvalues of `A`, in particular at least three eigenvalues of modulus at least one.

Now define independent grouped variables

`Y_t=X_t`, `t in T`,
`Z_a=<w_a,X>=alpha_a^(-1) sum_{i in G_a}c_i X_i`.                  (5.7)

The groups are disjoint, so all variables in (5.7) are independent. Each singleton has density cap one. By `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` with `k=1`, every `Z_a` has density cap at most `sqrt(e)`.

Let `W` denote the `N`-vector consisting of all variables in (5.7). Since `A` vanishes on `H^perp`,

`X^T A X=W^T M W`.                                                  (5.8)

Scale every grouped coordinate by the common factor `sqrt(e)`:

`V=sqrt(e) W`.                                                       (5.9)

Every component of `V` has density at most one, and

`e X^T A X =V^T M V`.                                               (5.10)

The matrix in (5.10) still has at least three eigenvalues of modulus at least one. Apply the proved fixed-dimensional theorem (2.4) in dimension `N`:

`||p_(e X^T A X)||_infty <=250 N(8+log N)`.                       (5.11)

Since scaling a scalar random variable by `e` divides its density supremum by `e`, (5.2) follows. `QED`

### Corollary 5.2 — exact partner-r41 endpoint with curvature confined to the named centers

Suppose the r41 strips collapse to exact lines and `supp(D)` is contained in the at-most-ten named centers `C=Z union {k}`. Then `m<=2`, `N<=12`, and

`boxed:
 ||p_Q||_infty
 <=250 e *12*(8+log 12)
 <85503.}`                                                         (5.12)

Thus the exact two-line endpoint with all diagonal curvature confined to the finite physical center set is already universally paid. More generally, if only `r` additional physical coordinates outside the r41 center set carry diagonal curvature, (5.2) gives the explicit bound with `N<=r+12`.

This closes a real subcase of `QFORM-TWOLINE-BANK-PRODUCT-RECEIVER-v1`: a putative high-density survivor must exploit either genuinely nonzero aggregate strip geometry, diagonal curvature spread over an unbounded number of bank coordinates, or both.

## 6. New obstruction: rowwise `rho^-1/6` closeness does not imply aggregate-small strip energy

The temptation after r41 is to replace each strip by its central line and use Corollary 5.2. That implication is false even deterministically.

### Proposition 6.1 — `QFORM-ROWSTRIP-AGGREGATE-ENERGY-OBSTRUCTION-v1`

For every even `m>=6` choose signs `sigma_j in {+1,-1}` with half of each sign and set

`u_j=m^(-1/2)(1,sigma_j)`, `j=1,...,m`.                            (6.1)

Then

`U^T U=I_2`,
`max_j ||u_j||^2=2/m<=1/3`,                                       (6.2)

and every row lies within distance `m^(-1/2)` of the single line `ell=span(e_1)`. Yet if `U^(0)` is the rowwise orthogonal projection onto that line and `F=U-U^(0)`, then

`boxed: ||F||_F=||F||_op=1}`                                      (6.3)

for every `m`.

#### Proof

The two columns of `U` are `m^(-1/2)(1,...,1)` and `m^(-1/2)(sigma_1,...,sigma_m)`. They are orthonormal because the signs balance. Projection onto `ell` removes the second column, so `F` has exactly that second unit column. This proves (6.2)-(6.3). `QED`

Taking `m` on the order of `rho^(1/3)` gives row distance on the order of `rho^(-1/6)`, exactly the partner scale, while the discarded strip retains a complete latent direction of operator norm one. Hence neither Frobenius continuity nor operator-norm continuity follows from the r41 rowwise tube. Under arbitrary fragmented/unbounded product laws, the strip must remain inside the actual phase.

This proposition is a source-valid obstruction, not a QFORM counterexample.

## 7. Owner-pinned D5 theorem applied to the surviving general obstruction

Apply (2.3) to an arbitrary physical cross block `M=A[I,J]` of any slab witness of ratio `rho`. Rearranging gives

`boxed:
 e_5(M^T M) <=(5 sqrt(2e)/rho)^10.}`                              (7.1)

Since

`e_5(M^T M)>=s_1(M)^2 ... s_5(M)^2>=s_5(M)^10`,                  (7.2)

we obtain the actual spectral obstruction

`boxed:
 s_5(M)<=5 sqrt(2e)/rho
       =11.6582199079856.../rho}`                                 (7.3)

for **every** disjoint physical cut. This is the required completed pinned-Fourier result inserted into a real inequality.

The interaction with Sections 5-6 is sharp in mechanism: D5 says a general high-density survivor cannot hide five substantial physical cross directions, while Proposition 6.1 says the exact-rank-two endpoint can still store order-one aggregate energy in arbitrarily many individually tiny strip deviations. Thus the remaining rough bank receiver is not replaceable by a generic high-rank tail argument.

## 8. Extremal product-law transfer remains optimizer-free

The valid reduction is approximation/finite mixture, not an attained global bathtub optimizer. Every cap-one probability density is an `L^1` limit of finite convex mixtures of indicators of bounded finite unions of intervals of total measure one, and

`|| prod_i f_i - prod_i g_i ||_1 <=sum_i ||f_i-g_i||_1`.          (8.1)

Therefore every strict slab violation transfers with arbitrarily small prescribed loss to a finite-union unit-product witness after finite-mixture expansion. No centered interval, common support diameter, uniform fragment count, or compactness of an optimizer is asserted.

The new center-conditioning theorem is compatible with this reduction: after choosing the finite-union witness, conditioning finitely many original coordinates leaves the remaining unit-set product factors unchanged. The coefficient theorems in Sections 4-7 are independent of how fragmented or remote those sets are.

## 9. Exact remaining endpoint

A counterexample sequence surviving the exact-rank-two hard chamber may therefore be taken, after the optimizer-free approximation and finite-center conditioning, to have arbitrarily large slab ratio `rho` and a center-free two-bank form

`Q_y(x)=sum_i d_i x_i^2`
`       +alpha L_0(x)^2+2 beta L_0(x)L_1(x)+gamma L_1(x)^2`
`       +x^T T x +ell_y^T x+c_y`,                                 (9.1)

where the two banks are disjoint original-coordinate product banks, the rowwise strip generating `T` has widths at most `rho^-1/6` and `24.540 rho^-1/6`, and `T` is retained exactly. If `T=0` and the diagonal curvature is confined to a bounded number of physical coordinates, Theorem 5.1 pays the form. If a general pre-rank-two survivor carries extra physical cross directions, (7.3) forces every fifth singular direction to be `O(rho^-1)`.

The new mathematical debt is therefore no longer the finite centers, exact two-line grouping, or fifth cross mode. It is the genuinely rough **aggregate strip + distributed diagonal curvature** interaction in (9.1).

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Continuity remains separate.
