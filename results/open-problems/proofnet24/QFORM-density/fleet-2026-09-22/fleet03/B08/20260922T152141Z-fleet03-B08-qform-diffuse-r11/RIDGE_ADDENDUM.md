# Fresh-control addendum — ridge-window theorem closes the tiny fourth-eigenvalue corner

This addendum was created after the mandatory pre-publication control refresh exposed a newer supporting result:

`QFORM-SPECTRAL-WINDOW-DENSITY-v1`, full proof
`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7:proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`.

Its stated consequence is: if `A` has at least three eigenvalues of modulus at least one and the spectral projection `P` onto **all** eigenspaces with `|lambda|>=1/64` satisfies

`max_i P_ii <=1/32`,

then `X^TAX` has a bounded continuous density with

`||p||_infinity <=288 sqrt(3e)/13 <64`,

for every admissible independent cap-one product law. Eigenvalues below `1/64` may be arbitrary in sign/orientation and nonseparable.

## Application to the rank-four codimension-one theorem in REPORT.md

Retain the notation of the main report:

`A=U diag(lambda_1,lambda_2,lambda_3) U^T + mu w w^T`,

with `|lambda_j|>=1`, `w perpendicular range(U)`, and

`max_i ||u_i||^2 <=1/1024`.

### Case R1: `|mu|<1/64`

The spectral projection onto `|lambda|>=1/64` is exactly

`P=UU^T`.

Therefore

`P_ii=||u_i||^2<=1/1024<1/32`.

The fresh ridge-window theorem applies **regardless of how localized `w` is**, and gives

`boxed( ||p_Q||_infinity <64 )`

with a continuous density vanishing at infinity.

This removes the entire “tiny fourth eigenvalue” portion of the residual left in the first version of REPORT.md.

### Case R2: `|mu|>=1/64` and `max_i w_i^2<=1/17`

The main report's full-range diffuse argument applies unchanged and gives the continuous bound

`||p_Q||_infinity <261`.

### Case R3: `|mu|>=1/64` and some `w_h^2>1/17`

For every such heavy coordinate with `a=A_hh!=0`, the exact Schur estimate from REPORT.md gives

`||p_Q||_infinity
 <=2sqrt(3e)(17/(|a|^2|mu|))^(1/6)`

` <=2sqrt(3e)(1088/|a|^2)^(1/6)`.

In particular, if one heavy coordinate satisfies

`|A_hh|>=1/64`,

then

`boxed(
 ||p_Q||_infinity
 <=2sqrt(3e)(1088*4096)^(1/6)
 <73.27.
)`

This branch establishes an essentially bounded density; continuity is not claimed because the final fleet04/B18 square-smoothing step supplies `L^infinity` absolute continuity but not continuity for arbitrary rough source densities.

## Sharpened codimension-one residual

Combining the fresh ridge-window theorem with the main report, any rank-four configuration still unpaid by this B08 mechanism must satisfy all of the following:

1. the three target eigenvectors remain diffuse: `max_i||u_i||^2<=1/1024`;
2. the fourth eigenvalue is **not** tiny: `|mu|>=1/64`;
3. the fourth eigenvector is localized: `max_i w_i^2>1/17`;
4. every coordinate with `w_h^2>1/17` has either `A_hh=0` or `|A_hh|<1/64`.

So the remaining codimension-one obstruction is no longer a small-spectral-tail problem. It is a localized high-spectral-leverage / small-physical-diagonal cancellation problem, precisely the regime where a two-coordinate hyperbolic pivot or disjoint-block aggregate mechanism should replace scalar square smoothing.

This addendum does not alter the full-target status: the unrestricted conjecture remains OPEN.
