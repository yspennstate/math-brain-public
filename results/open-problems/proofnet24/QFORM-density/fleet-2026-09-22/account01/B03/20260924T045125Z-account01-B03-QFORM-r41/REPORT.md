SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-24T04:51:25Z.
attacking: the singular physical-pair part of overlap-two exterior mass — prove a source-preserving parabolic two-coordinate density bound, interpolate it with the transverse linear bound, and make the rank-one pivot scale cancel against J2.

# account01/B03 r41 — rank-one physical-pair compiler for overlap-two exterior mass

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: `Decoupled time integral`  
Status: **NEW SUPPORTING THEOREM / SINGULAR-RANK-ONE PHYSICAL-PAIR J2 PACKETS PAID / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

## 0. Scope and live corrections

The target remains the full arbitrary-product-law theorem: independent real coordinates with densities bounded by one, and a real symmetric matrix with at least three eigenvalues of modulus at least one. No Gaussianity, moments, support bounds, connected support, log-concavity, or rotation of the product law is assumed.

This run preserves the live corrections. In particular it does **not** conditionally re-cap one member of `(X-X',X+X')`, does not use law-uniform pointwise quadratic van der Corput, does not rotate the product law and then claim independence, and does not invoke the refuted arbitrary-joint rank-three coarea statement.

The previous B03 run paid every overlap-two packet whose physical `2 x 2` pair is invertible, with a determinant-free final `J2^{-1/6}` bound. The first missing local case was a **singular** physical pair carrying positive overlap-two third-minor mass. This run closes that local case.

## 1. Required partner result applied at an actual inequality

Use the completed account02/B03 theorem

`QFORM-DISJOINT-EXTERIOR-MASS-EXIT-v1`,

source-pinned in the brain at commit `c2cf502ba91445ad3119cfb9991131ec7d32d725`, with canonical mathematics

`yspennstate/math-open-problems@5e5366b98337d13ba24bf666f4e42155553de7c2`.

For

`E_r(A)=sum_{|S|=|T|=3, |S cap T|=r} det(A[S,T])^2`, `r=0,1,2,3`,

it proves

`sum_r E_r(A)=e_3(A^2)>=1`,

and

`||p_Q||_infinity <=16.9060424511 E_0(A)^(-1/6)`.                 (1.1)

Therefore at the actual global fork

`E_0(A)>=1/4`,                                                     (1.2)

we have

`||p_Q||_infinity <21.301`.                                       (1.3)

So the present local analysis is legitimately needed only after passing to the overlap-heavy alternative `E_0<1/4`; no assertion that this alone exhausts the overlap sectors is made.

## 2. Sharp input: one-dimensional product projection

I use the source-valid Rogozin--Ball consequence already recorded in the QFORM package: for independent cap-one variables `Y_j` and nonzero `b in R^m`, the linear form

`L=b dot Y`

has a density satisfying

`||p_L||_infinity <= sqrt(2)/||b||_2`.                             (2.1)

A pinned package source is

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a`

`proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

No moment, support or log-concavity hypothesis is attached to `(2.1)`.

We will also use the elementary fractional-potential consequence: if a real random variable has density cap `M`, then for every center `c`,

`E|L-c|^(-2/3) <= 3*2^(2/3) M^(2/3)`.                             (2.2)

Indeed the decreasing kernel is maximized, under mass one and cap `M`, by filling the centered interval of length `1/M`, so

`M*2*int_0^(1/(2M)) x^(-2/3) dx
 =3*2^(2/3) M^(2/3)`.

Combining `(2.1)` and `(2.2)` gives the translation-uniform estimate

`sup_c E|b dot Y-c|^(-2/3) <=6 ||b||_2^(-2/3)`.                   (2.3)

## 3. New physical two-coordinate parabola theorem

Let `X_1,X_2` be independent with densities `f_1,f_2<=1`. Let `v,w` be an orthonormal basis of `R^2`, let `lambda !=0`, `ell !=0`, and let `h,k` be arbitrary real translations. Put

`T=lambda(v dot X+h)^2+2 ell(w dot X+k)`.                          (3.1)

### Theorem 3.1

The law of `T` has a density and

`||p_T||_infinity <=2^(5/3)|lambda|^(-1/3)|ell|^(-2/3)`.          (3.2)

The bound is uniform in `h,k` and in the two cap-one laws.

### Proof: exact level curve

Write

`y=v dot x+h`, `z=w dot x+k`.

The change `(x_1,x_2)<->(y,z)` has Jacobian one. On the level `T=s`,

`z=(s-lambda y^2)/(2 ell)`.                                       (3.3)

Hence, after absorbing the translations into the physical-coordinate parametrization,

`p_T(s)=1/(2|ell|) int_R f_1(x_1(y)) f_2(x_2(y)) dy`,              (3.4)

where

`x'(y)=v-(lambda/ell)y w`,

so

`||x'(y)||_2^2=1+(lambda y/ell)^2`.                               (3.5)

Each physical coordinate `x_j(y)` is a polynomial of degree at most two and therefore has multiplicity at most two unless it is affine, in which case the same or better multiplicity bound holds.

### First envelope: transverse linear smoothing

At every `y`, at least one physical derivative has magnitude at least `1/sqrt(2)`. Partition the real line into the set where `|x_1'|>=1/sqrt(2)` and its complement, where `(3.5)` forces `|x_2'|>=1/sqrt(2)`. The one-dimensional area formula and `int f_j=1` give at most `2sqrt(2)` on each piece. Thus the integral in `(3.4)` is at most `4sqrt(2)`, and

`||p_T||_infinity <=2sqrt(2)|ell|^(-1)`.                          (3.6)

### Second envelope: parabolic curvature plus product mass

Fix `a>0`. On the head `|y|<=a`, the integral in `(3.4)` is at most `2a` because both densities are at most one.

On the tail `|y|>a`, `(3.5)` gives `||x'(y)||_2>=|lambda|a/|ell|`; hence at every tail point at least one coordinate derivative has magnitude at least

`|lambda|a/(sqrt(2)|ell|)`.

Partition the tail according to which coordinate pays this derivative. Area formula and multiplicity at most two then give a total tail contribution at most

`4sqrt(2)|ell|/(|lambda|a)`.                                      (3.7)

Therefore the integral in `(3.4)` is at most

`2a+4sqrt(2)|ell|/(|lambda|a)`.                                   (3.8)

The minimizing value is

`a=2^(3/4) sqrt(|ell|/|lambda|)`,

for which `(3.8)` equals

`2^(11/4) sqrt(|ell|/|lambda|)`.

Dividing by `2|ell|` in `(3.4)` yields

`||p_T||_infinity <=2^(7/4)|lambda ell|^(-1/2)`.                  (3.9)

### Interpolation

Take the minimum of `(3.6)` and `(3.9)` and use `min(A,B)<=A^(2/3)B^(1/3)` with `(3.9)` carrying exponent `2/3`. The constant is

`(2^(7/4))^(2/3)(2^(3/2))^(1/3)=2^(5/3)`,

and the powers are `|lambda|^(-1/3)|ell|^(-2/3)`, proving `(3.2)`.

This is a genuinely product-coordinate estimate. It does not replace `(X_1,X_2)` by independent rotated coordinates; the rotation is used only to parameterize the level curve, while the density factors remain `f_1(x_1(y))f_2(x_2(y))` in the original independent coordinates.

## 4. Singular physical pair: exact overlap-two identity

Fix a genuine original-coordinate pair `H={h_1,h_2}` and suppose the physical principal matrix

`B=A[H,H]`

is singular and carries positive overlap-two mass. If `B=0`, every mixed `3 x 3` determinant sharing `H` is zero, so positive mass forces `rank B=1`.

Write

`B=lambda v v^T`, `lambda !=0`,                                    (4.1)

with `v` unit, and choose a unit `w perpendicular v`. For every external original coordinate `i`, put

`c_i=A[H,i]`,
`alpha_i=v dot c_i`,
`beta_i=w dot c_i`.                                                (4.2)

Define

`J_2(H)=sum_{i!=j, i,j notin H} det A[H union {i},H union {j}]^2`. (4.3)

For the block determinant,

`det [[B,c_j],[c_i^T,A_ij]]
 =det(B) A_ij-c_i^T adj(B)c_j`.                                   (4.4)

Since in the basis `(v,w)`, `B=diag(lambda,0)`,

`adj(B)=lambda w w^T`.

Thus

`det A[H union {i},H union {j}] =-lambda beta_i beta_j`,           (4.5)

and therefore the exact identity is

`boxed:
 J_2(H)=lambda^2 sum_{i!=j} beta_i^2 beta_j^2
       =lambda^2[(sum_i beta_i^2)^2-sum_i beta_i^4].`              (4.6)

In particular `J_2(H)>0` implies `beta !=0`.

## 5. Rank-one pair compiler with arbitrary external curvature

Let the two physical variables on `H` be `X_H`, and let `Y` denote **all** external original coordinates. The full form has the exact decomposition

`Q=lambda u^2+2u alpha dot Y+2z beta dot Y+Y^T D Y`,                (5.1)

where

`u=v dot X_H`, `z=w dot X_H`.

Complete only the rank-one square:

`Q=lambda[u+h(Y)]^2+2 z L(Y)+R(Y)`,                               (5.2)

with

`h(Y)=(alpha dot Y)/lambda`,
`L(Y)=beta dot Y`,
`R(Y)=Y^T D Y-(alpha dot Y)^2/lambda`.                            (5.3)

No term of `R` is discarded; it may have arbitrary sign, rank and nonseparable curvature.

Condition on the external original coordinates `Y`. The two variables on `H` retain their original independent cap-one product density. For every realization with `L(Y)!=0`, Theorem 3.1 applies with `ell=L(Y)` and with the random center `h(Y)`; the residual `R(Y)` is only an output translation. Hence

`p_{Q|Y}(s) <=2^(5/3)|lambda|^(-1/3)|L(Y)|^(-2/3)`.              (5.4)

Because `beta!=0`, `(2.1)` gives a genuine density for `L`, so `P(L=0)=0`. Averaging `(5.4)` and using `(2.3)` yields

`||p_Q||_infinity
 <=6*2^(5/3)|lambda|^(-1/3)||beta||_2^(-2/3)
 =6*2^(5/3)(|lambda| ||beta||_2^2)^(-1/3)`.                       (5.5)

Finally `(4.6)` implies

`J_2(H) <=lambda^2 ||beta||_2^4`,

so

`|lambda| ||beta||_2^2 >=sqrt(J_2(H))`.                           (5.6)

Substitute `(5.6)` into `(5.5)`:

`boxed:
 ||p_Q||_infinity
 <= C_rank1 J_2(H)^(-1/6),
 C_rank1=6*2^(5/3)=19.048812623618396... .}`                       (5.7)

This proves absolute continuity and linear one-copy small-ball scaling

`P(Q in I)<=C_rank1 J_2(H)^(-1/6)|I|`                             (5.8)

for every interval `I` in the rank-one physical-pair overlap-two branch. The argument does not establish continuity of the resulting mixture density.

## 6. Combined local overlap-two conclusion

The previous B03 r40 theorem proves, for every **invertible** physical pair `H`,

`||p_Q||_infinity <=129.924435862525374 J_2(H)^(-1/6)`.           (6.1)

Section 5 proves the sharper `(5.7)` whenever `A[H,H]` has rank one. If `A[H,H]=0`, then `(4.4)` gives `J_2(H)=0`.

Therefore:

### Theorem 6.1 — every positive localized overlap-two packet is paid

For every physical pair `H` with `J_2(H)>0`, irrespective of whether `A[H,H]` is invertible or singular,

`boxed:
 ||p_Q||_infinity
 <=129.924435862525374 J_2(H)^(-1/6).}`                            (6.2)

No condition number, determinant lower bound, nonzero diagonal, sign, or support assumption is required.

The unresolved global issue in the `E_2` sector is now **purely aggregation/selection**: since

`E_2(A)=sum_{|H|=2} J_2(H)`,                                      (6.3)

large aggregate `E_2` need not force one dimension-free large `J_2(H)`. The singular-pair analytic collar itself is no longer an obstruction.

## 7. Dependence-safe independent-copy time integral

The assignment-specific identity is retained only in the safe whole-output form

`|phi_Q(t)|^2=E exp(it(Q-Q'))`,                                   (7.1)

where `Q'` is an independent copy of the **entire** scalar output. No conjugate coordinate pair is split or conditionally re-capped.

Let

`M=C_rank1 J_2(H)^(-1/6)`

in the rank-one branch. Since `p_{Q-Q'}=p_Q*p_{-Q}`,

`||p_{Q-Q'}||_infinity<=M`.                                      (7.2)

The bathtub estimate at exponent `1/2` gives

`E|Q-Q'|^(-1/2)<=2sqrt(2M)`.                                     (7.3)

Using the one-dimensional Riesz Fourier identity

`int_R |t|^(-1/2) e^{itx} dt=sqrt(2pi)|x|^(-1/2)`

in the standard positive-kernel regularized sense, `(7.1)`--`(7.3)` imply

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2 dt
 <=4 sqrt(pi M)
 =4 sqrt(pi C_rank1) J_2(H)^(-1/12).}`                            (7.4)

Numerically the coefficient in `(7.4)` is approximately `30.9427`.

This weighted collision estimate is recorded as a consequence of the stronger one-copy density argument. It is **not** used backwards as an invalid `L^infinity` criterion.

## 8. What remains

The full conjecture remains open. The new theorem removes a specific analytic gap: positive overlap-two mass attached to a singular rank-one physical pair is now controlled at the same scale `J_2^{-1/6}` as the invertible-pair branch, with arbitrary external curvature retained.

The remaining global overlap-two implication is to convert aggregate `E_2>=c` into a product-preserving receiver **without** demanding a single large `J_2(H)`. The other overlap sectors `E_1` and `E_3`, plus the current low-rank/high-leverage carrier branches, remain separate structural debt.

Continuity of the density is not proved in the new rank-one mixture branch. Full-target continuity remains open.

## 9. Sources consumed

- Fresh owner control and programme files from `yspennstate/math-research-brain/main`, OWNER CONTROL revision `2026-09-22.15`.
- Current corrections including the false conditional sum/difference cap, false law-uniform pointwise quadratic decay, false arbitrary-joint coarea gate, and fiber-sup dimension loss.
- account02/B03 completed partner theorem `QFORM-DISJOINT-EXTERIOR-MASS-EXIT-v1`, brain commit `c2cf502ba91445ad3119cfb9991131ec7d32d725`, canonical math `5e5366b98337d13ba24bf666f4e42155553de7c2`.
- Rogozin--Ball one-dimensional product-projection consequence, pinned QFORM source `e542b1a6ef471b329e4e88a6553e1aacb45acc1a`.
- Previous account01/B03 r40 invertible-pair compiler, `8c0a57c02e40335ba9f2e27e6f53889b130cfa47` / checks `a3b7f8899b5e8f95a62811bb4b78885ace2f9c4d`.

Full QFORM: **OPEN**. Full-target continuity: **OPEN**.
