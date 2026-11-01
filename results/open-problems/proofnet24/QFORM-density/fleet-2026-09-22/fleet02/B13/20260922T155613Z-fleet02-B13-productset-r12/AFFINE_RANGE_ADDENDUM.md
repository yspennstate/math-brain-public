# Addendum — exact range-affine translation invariance

This addendum sharpens the mechanism diagnosis in the main report. Full QFORM remains **OPEN**.

## Lemma — `QFORM-RANGE-AFFINE-GAUGE-v1`

Fix a real symmetric matrix `A`. For `b in Range(A)` and `c in R`, consider

`Q_{A,b,c}(x)=x^T A x+2b^T x+c`.

Let `M(A)` be the supremum of the essential density norm of `X^T A X` over all independent real coordinates with one-dimensional densities bounded by one, and define `M(A,b,c)` analogously for `Q_{A,b,c}(X)`. Then

`M(A,b,c)=M(A)`                                                  (1)

for every `b in Range(A)`, `c in R`.

The identical statement holds for the extremal product-indicator small-ball functional at every slab width `h>0`:

`sup_{|E_i|=1,t} |{x in prod E_i:Q_{A,b,c}(x) in [t,t+h]}|`
` = sup_{|E_i|=1,t} |{x in prod E_i:x^T A x in [t,t+h]}|`.       (2)

### Proof

Choose `m` with `A m=b`. Then

`Q_{A,b,c}(x)=(x+m)^T A(x+m)+c-m^T A m`.                         (3)

Coordinatewise translation preserves independence, every one-dimensional density cap, and Lebesgue measure of each product-indicator factor. Translation of the scalar output does not change an essential density norm and is absorbed by the optimization in `t` for (2). Thus the affine and homogeneous suprema are at most one another after the bijections `X <-> X+m` and `E_i <-> E_i+m_i`. QED.

## Consequence for the collar counterexample

The single-interval family in the main report has its fifth support translated by `11/sin(theta)`. After recentering that interval, the large translation produces an order-one linear term. This is not a new target obstruction: whenever that linear term is in the range of the comparison matrix, (1)-(3) show it is a free coordinate-translation gauge.

For the explicit family, after writing

`x=(11/sin(theta))e5+u`,

one gets

`x^T A_theta x = u^T A_theta u + 2 b_theta^T u + c_theta`,

with `b_theta=A_theta(11/sin(theta)e5) in Range(A_theta)`. Hence its density norm is exactly the homogeneous `A_theta` density supremum, as it must be.

As `theta->0`, this recentered affine polynomial converges on bounded `u` to

`(u+11w)^T A0(u+11w)`,

whose linear coefficient `11 A0 w` lies in `Range(A0)` and is therefore covered by the exact endpoint with no cost.

Thus the main report's counterexample refutes **same-support raw kernel continuity**, not affine-uniform endpoint control. The precise lesson is stronger and cleaner:

1. a successful four-direction stability theorem should be invariant under the exact range-affine gauge (1);
2. after quotienting this gauge, the unresolved obstruction is the absence of any uniformly bounded recentering/fragment decomposition for arbitrary unit-measure product indicators;
3. consequently the collar proof must aggregate product structure before applying any perturbation estimate, rather than compare homogeneous slab kernels on the same remote supports.

This is consistent with the live corrections `QFORM-BOUNDED-DIAMETER-LOCALIZATION-FALSE` and `QFORM-NO-UNIFORM-FRAGMENT-COUNT-BATHTUB-v1`.
