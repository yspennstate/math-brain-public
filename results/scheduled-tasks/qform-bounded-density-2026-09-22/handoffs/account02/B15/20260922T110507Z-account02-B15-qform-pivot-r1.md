# account02/B15 qform handoff — principal-triple theorem + flat rank-three obstruction

**Live target:** `Quadratic_Form_Bounded_Density_Conjecture`  
**Owner control:** revision `2026-09-22.4`  
**Full target:** `OPEN / NOT PROVED`.

## Immutable source

`yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8`

`qform/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`

Claims commit: `9d217e93968b43ca68bd4e6ba21b7324e6094955`.

## New theorem

For independent `Y_1,Y_2,Y_3` with densities bounded by `1`, any symmetric invertible `3x3` matrix `B`, and arbitrary affine terms,

`Z=Y^T B Y + 2 b^T Y + c`,

one has

`||p_Z||_infinity <= (2*pi+3*sqrt(3))/sigma_min(B)`.

The proof is source-exact and uses two regions:

1. `|By|<=1`: transform by `z=|B|^{1/2}y`; the quadratic becomes the canonical signature form `z^T sign(B) z`, the Jacobian is <=1 after normalization, and the unit-ball shell volume is <=`2*pi*eta` for every output interval of length `eta`.
2. `|By|>1`: one original coordinate has `|(By)_i|>1/sqrt(3)`; on each monotonic branch of the corresponding one-variable quadratic the interval preimage length is <=`sqrt(3) eta/2`, hence after the two branches and three coordinates the far contribution is <=`3 sqrt(3) eta`.

Therefore any high-dimensional symmetric `A` with a principal coordinate triple `I` satisfying `sigma_min(A_II)>=kappa` has

`||p_{X^TAX}||_infinity <= (2*pi+3*sqrt(3))/kappa`

by conditioning on all other coordinates. Cross-couplings to the conditioned variables are harmless affine terms.

A definite `2x2` principal coordinate block `C` gives the sharper conditional theorem

`||p_Q||_infinity <= pi/sqrt(det C)`.

## Mechanism obstruction

Fixed principal-triple selection cannot close the owner target. For Sylvester orders `n=2^m`, let `U` be any three normalized Hadamard columns and set `A=UU^T`. Then `A` has exactly three eigenvalues equal to `1`, but every row of `U` has squared norm `3/n`; hence for every coordinate triple `I`,

`trace(A_II)=9/n`, so `sigma_min(A_II)<=3/n`.

Thus any argument that selects one triple and applies the theorem above loses order `n` on a genuine rank-three spectral example.

However Cauchy-Binet retains the exact aggregate resource

`sum_{|I|=3} det(A_II) = sum det(U_I)^2 = det(U^T U)=1`.

The next bridge should aggregate many principal triples / minors rather than choose one. A multilinear coarea or Brascamp-Lieb mechanism that turns this determinant mass into a density bound is the concrete target.

## Consumed fleet result

I used account03/B17

`yspennstate/math-open-problems@c64fcff680b0a252a3c92002c60eedba02bbb9ec:qform/fleet-2026-09-22/account03/B17/account03-B17-20260922T112131Z/REPORT.md`.

That source-backed report already proves the failure of law-uniform pointwise Fresnel decay and the coordinate-diagonal `C=pi` theorem. The current result extends the positive branch to arbitrary nonsingular three-coordinate principal blocks and isolates the delocalized projector obstruction.
