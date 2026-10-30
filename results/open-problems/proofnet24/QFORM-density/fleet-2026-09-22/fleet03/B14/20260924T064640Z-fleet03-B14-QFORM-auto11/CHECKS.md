# Checks — QFORM cap-saturation congruence localization

Run: `20260924T064640Z-fleet03-B14-QFORM-auto11`.

## A. Marginal scaling

For `k=||f||_infinity in (0,1]`, let `Y=kX`. Then

`g(y)=f(y/k)/k`,

`int g(y)dy=int f(x)dx=1`,

and

`||g||_infinity=||f||_infinity/k=1`.

No support or moment property is invoked.

## B. Exact output identity

With `D=diag(k_i)`, `Y=DX`, `S=D^{-1}` and `B=SAS`,

`Y^T B Y = X^T D (D^{-1} A D^{-1}) D X = X^T A X`.

Thus all density/continuity statements concern exactly the same one-dimensional law.

## C. Threshold-count variational check

If `S>=I`, then `||Sx||>=||x||`. If `E_+(A;t)` is the spectral subspace on which `y^TAy>=t||y||^2`, its inverse image `S^{-1}E_+` has the same dimension and satisfies

`x^T SAS x >= t||Sx||^2 >=t||x||^2`.

The negative subspace analog satisfies

`x^T SAS x <=-t||Sx||^2 <=-t||x||^2`.

Courant-Fischer therefore preserves separately the counts above `+t` and below `-t`.

## D. Concrete matrix algebra

For

`B_*=I_3-(2/3)11^T`

and

`S=diag(2,2,1)`,

`S B_* S = [[4/3,-8/3,-4/3],[-8/3,4/3,-4/3],[-4/3,-4/3,1/3]]`.

The antisymmetric vector `(1,-1,0)` has eigenvalue `4`.

On vectors `(a,a,b)`, the eigenvalue equations are represented by

`[[-4/3,-4/3],[-8/3,1/3]] [a,b]^T = lambda [a,b]^T`,

whose characteristic polynomial is

`lambda^2+lambda-4`.

Therefore the other eigenvalues are

`(-1+sqrt(17))/2`, `(-1-sqrt(17))/2`.

The smallest absolute eigenvalue is

`(sqrt(17)-1)/2 = 1.5615528128088303...`.

The fleet04/B14 r10 height is therefore

`6 sqrt(pi) / ((sqrt(17)-1)/2)
 =12 sqrt(pi)/(sqrt(17)-1)
 =6.810351221041301...`.

For comparison `6 sqrt(pi)=10.634723105433096...`.

## E. Scope checks

- General rotations are never used.
- Independence is preserved because only coordinatewise scalar maps are applied.
- No conditional density cap is asserted after a non-coordinate transform.
- No pointwise oscillatory estimate is used.
- No bounded support, fragment count, connected support or moment is assumed.
- The theorem does not extract a good physical triple from the global spectral hypothesis.
- Full QFORM remains open.
- Continuity is not newly proved globally, but the exact-law transformation preserves continuity whenever it is known on the saturated representation.
