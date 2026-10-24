# Deterministic checks for affine-shear Borel receiver

Run `20260923T200516Z-account02-B05-QFORM-auto11c`.

The constants were independently recomputed during the run:

- `K0=(8/3)(4-sqrt(2)) = 6.8954305003384135`.
- `A0=(K0/2)(1+sqrt(2)) = 8.323520916159048`.
- `Cstar=3*2^(-2/3)*A0^(2/3) = 7.761982175235497`.
- With a two-dimensional product-projection cap `2/|tau|`, a normalized scalar cap `sqrt(2)`, and transverse coefficient `T/tau^2`, the factor is exactly
  `(2*sqrt(2)/|tau|)^(2/3)*(|T|/tau^2)^(-1/3)=2|T|^(-1/3)`,
  so the numerical constant is `2*Cstar = 15.523964350470994`.

Algebraic shear check:

For

`q(L,V)=aL^2+2bLV+cV^2+dL+eV+f`, `c!=0`,

set `V'=V+(b/c)L+e/(2c)`. Then

`q=cV'^2+(a-b^2/c)L^2+(d-be/c)L+(f-e^2/(4c))`.

The map `(L,V)->(L,V')` has determinant one, so a joint density cap is unchanged.

Dyadic-sum check:

`sum_{k>=0} sqrt(2^(-k-1)R) = sqrt(R/2)/(1-2^(-1/2)) = (1+sqrt(2))sqrt(R)`.

For `A>0`, minimizing `A sqrt(R)+m/R` gives `R^(3/2)=2m/A` and minimum

`3*2^(-2/3) A^(2/3)m^(1/3)`.

Status: arithmetic/algebra checks PASS. These finite checks support but do not replace the proof in `REPORT.md`.
