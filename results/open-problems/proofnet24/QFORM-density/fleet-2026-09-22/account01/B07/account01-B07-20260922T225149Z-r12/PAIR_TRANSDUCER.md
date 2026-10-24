# Second addendum — exact rank-one physical-pair star transducer

This is a direct analytic payment for one part of the surviving nonzero-self near-leaf geometry. It consumes the newest designated-partner theorem account02/B07 r19, `QFORM-ZEROSELF-RANDOMSHIFT-HALFRIESZ-v1`.

## Theorem — `QFORM-RANKONE-PAIR-STAR-TRANSDUCER-v1`

Let `A` be any real symmetric matrix and let the original coordinates be independent with densities at most one. Fix two physical coordinates `i!=j` and write

`a=A_ii`, `b=A_ij`, `d=A_jj`,

`u=(A_ik)_(k notin{i,j})`, `v=(A_jk)_(k notin{i,j})`.

Assume

`a!=0`,  `a d-b^2=0`.

Put

`theta=b/a`,  `w=v-theta u`.

If `w!=0`, then the **full** quadratic form `Q=X^T A X`, with every outside quadratic coefficient and coupling retained, has an essentially bounded density satisfying

`boxed:
||p_Q||_infinity
 <= (16/sqrt(3)) |a|^(-1/2) ||w||_2^(-1/2).
`

Equivalently, define the aggregate physical two-minor bank

`R_ij
 =sum_(k notin{i,j}) det A[{i,j},{i,k}]^2
 =sum_k (a A_jk-b A_ik)^2
 =a^2||w||_2^2`.

Then

`boxed:
||p_Q||_infinity <= (16/sqrt(3)) R_ij^(-1/4).
`

Thus a determinant-weighted **bank** is paid directly; no individual residual coordinate/minor is selected.

### Proof

Let `Y=X_j` and let `Z` collect every other coordinate except `X_i,X_j`. Write the outside quadratic form as `H(Z)`. The pair-plus-outside expansion is

`Q
 =a X_i^2+2b X_iY+dY^2
  +2X_i<u,Z>+2Y<v,Z>+H(Z)`.

Because `d=b^2/a`, set

`S=X_i+theta Y`.

Then exactly

`Q
 =aS^2+2S<u,Z>+2Y<w,Z>+H(Z)`.

Complete the square only in `S`:

`Q
 =a(S+<u,Z>/a)^2 + R(Y,Z)`

with

`R(Y,Z)
 =2Y<w,Z>+H(Z)-<u,Z>^2/a`.

The change `(X_i,Y)->(S,Y)` has Jacobian one. Conditional on `(Y,Z)`, the variable `S` has density

`s -> f_i(s-theta Y)`

and hence density cap one. Therefore the elementary one-dimensional square kernel gives, for almost every conditioning value,

`p_(Q|Y,Z)(t)
 <= |a|^(-1/2)|t-R(Y,Z)|^(-1/2)`.

Averaging,

`||p_Q||_infinity
 <= |a|^(-1/2) H_(1/2)(R)`.

Now `Y=X_j` is independent of `Z`, has density cap one, its self coefficient in `R` is exactly zero, and its full off-diagonal row is precisely `w`. The designated partner account02/B07 r19 theorem `QFORM-ZEROSELF-RANDOMSHIFT-HALFRIESZ-v1` applies with arbitrary complementary curvature and yields

`H_(1/2)(R)
 <=(16/sqrt(3))||w||_2^(-1/2)`.

This proves the first display. The determinant-bank identity follows from

`det [[A_ii,A_ik],[A_ji,A_jk]]
 =a A_jk-b A_ik
 =a w_k`.

QED.

No rotated independence is asserted: the only transformed scalar `S` is used through its conditional density given the untouched coordinate `Y`, and that conditional density is an original density translated by `theta Y`.

## Exact proportional-row endpoint

If instead `w=0`, then symmetry and `ad-b^2=0` imply the entire `j`th row is `theta` times the `i`th row. The quadratic form depends on `(X_i,X_j)` only through

`S=X_i+theta X_j`:

`Q=aS^2+2S<u,Z>+H(Z)`.

The variable `S` is independent of `Z` and has density cap at most one, because it is the convolution of the density of `X_i` with a rescaled probability density. Hence the two physical coordinates can be merged **exactly** into one cap-one product coordinate. This is a product-preserving grouped-coordinate reduction, not a rotation.

If the proportional pair is oriented so `|theta|<=1`, and `C` denotes the reduced symmetric coefficient matrix in `(S,Z)`, then `A=T^T C T` with `||T||^2=1+theta^2<=2`. Consequently

`sigma_k(C)>=sigma_k(A)/2`.

Thus three singular/eigenvalue magnitudes at least one in `A` become three magnitudes at least `1/2` in the reduced matrix. This records a bounded-scale exact-collapse route; it is not by itself an induction proof of full QFORM.

## Relation to the partner near-leaf geometry

For the two anchor rows, let

`p=(A_ik)_(k notin{i,j})`, `q=(A_jk)_(k notin{i,j})`,
`Delta=ad-b^2`.

The complete squared exterior area of those two physical rows decomposes exactly as

`sum_{r<s} det A[{i,j},{r,s}]^2
 =Delta^2
  +||a q-bp||^2
  +||bq-dp||^2
  +||p wedge q||^2`.

The partner checkerboard quantity is the last term `||p wedge q||^2`. On the exact singular-pair face `Delta=0`,

`q=(b/a)p+w`

and the identity becomes

`(a^2+b^2)||w||^2+||p wedge w||^2`.

Thus the new theorem pays the exact singular-pair branch whenever the physical-row proportionality defect has a quantitative determinant bank; exact zero defect is the grouped-coordinate endpoint above.

## Scope

This theorem proves an essentially bounded density only on the exact `ad-b^2=0`, `w!=0` physical-pair branch. It does not claim continuity. It does not perturb to small nonzero `ad-b^2`: the partner's square-collapse counterexample shows that arbitrary nonzero self curvature cannot be treated as a harmless perturbation of the zero-self random-shift theorem without spending additional structure.
