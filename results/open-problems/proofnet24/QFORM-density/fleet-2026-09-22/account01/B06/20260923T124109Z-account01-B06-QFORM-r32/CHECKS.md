# account01/B06 r32 finite checks

These are finite algebra/numerical checks only; the proofs are in `REPORT.md`.

## Exact constant arithmetic

For the concrete gates

- `chi=1/2`,
- `delta=1/32`,
- `r=2`,

one has

`eta=sqrt(1/2)-sqrt(1/32)=3/(4sqrt(2))`,

`eta/r=3/(8sqrt(2))=0.26516504294495535...`,

`eta^2/(4r^2)=9/512=0.017578125`,

`eta^4/(4r^4)=81/65536=0.0012359619140625`,

and, when `||K||_F>s/2`,

`(eta/r)(s/2)=3s/(16sqrt(2))=0.13258252147247765... s`.

The coefficient/curvature split uses

`sqrt((9/512)/2)=3/32`,

so the transverse row/column alternative is

`[3/(16sqrt(2))] [3/32] s = 9s/(512sqrt(2))`.

The partner area-gate constant is

`2 sqrt(e) sqrt(8sqrt(2)) = 11.091230450274296...`.

## Random bordered-identity check

For independent Gaussian test arrays in dimensions `m=3,4,6`, define

`D=J_b^T C J_a`,
`K=P_(b^perp) C P_(a^perp)`.

For each test and every coordinate `i`, the following were checked numerically:

`||D||_F^2 = ||a||^2||b||^2||K||_F^2`,

`sum_(R contains i,T) D_(R,T)^2
 =||a||^2||b||^2[(b_i^2/||b||^2)||K||_F^2+||e_i^T K||_2^2]`,

`sum_(R,T contains i) D_(R,T)^2
 =||a||^2||b||^2[(a_i^2/||a||^2)||K||_F^2+||K e_i||_2^2]`.

Across 15 random matrices the largest absolute discrepancy in the normalized one-index formulas was `1.07e-14`; the full packet identity discrepancy was at floating-point roundoff scale (`<7e-13` in the unnormalised quantities).

An additional same-index double-incidence identity was checked but is **not used** in the report, so it is not promoted as a theorem here.

`QFORM_B06_R32_CHECK_PASS`
