Model requested: GPT-6 maximum. Authenticated applied model/effort telemetry is unavailable to the worker; do not infer it from this prompt.

# PROB10-09 idea before code — quantitative surface-product family

Frozen parent target: iid bond percolation on every Cayley graph of every finitely generated nonamenable group, with target `p_c<p_u`. This note is an idea record, not a proof or closure claim.

## Continuity and collision boundary

Continue the preceding R20 report
`runs/prob10_2026-09-20/PROB10-09/2026-09-19T23-58-00Z_surface_product_strict_gap_4c91e2.md`.
Do not duplicate the neighboring NM13-11 `SL_3(Z)` subgroup/nonbacktracking route in
`proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T02-52-26+0300__t09-subgroup-nonbacktracking-sl3z-gap.md`.

A current prior-art correction is essential: Peres (2000), *Percolation on nonamenable products at the uniqueness threshold*, applies directly to Cartesian products `X x Y` with nonamenable `Aut(X)` and proves nonuniqueness at `p_u`. Thus the previous report's suggestion that the surface-product graph sits wholly outside known product results was too strong. The present route is retained only as an explicit quantitative `p_u-p_c` certificate and a self-contained structural comparison; no novelty is asserted.

## New mathematical route

For the standard Cayley graph
`X_{g,h}=Cay(Gamma_g x Gamma_h,S_g union S_h)` of closed orientable surface groups, assume `2<=g<=h`. Put

- `a=4g-3`, `b=4h-3`, `D=4(g+h)=a+b+6`;
- by Magnus Freiheitssatz, `X_{g,h}` contains `T_{a+1} square T_{b+1}`;
- `||A_{X_{g,h}}|| <= R=4+2 sqrt(a)+2 sqrt(b)`;
- the nonbacktracking threshold lower bound is `p_{2->2} >= 1/beta(D,R)`.

Instead of the preceding radius-one cluster lower bound, expose the vertical tree cluster to depth two. For a `d`-regular vertical tree and bond parameter `p`, the probability that no horizontal child edge is found in the radius-two exposed cluster is

`Q_d^(2)(p) = (1-p) * [(1-p) + p(1-p)(1-p^2)^(d-1)]^d`,

so

`Phi_d^(2)(p)=1-Q_d^(2)(p) <= phi_{T_d}(p)`.

If the oriented second tree has `q` forward children and `q Phi_d^(2)(p)>1`, the standard fiber-cluster branching comparison gives `p_c(T_d square T_{q+1})<p`, hence `p_c(X_{g,h})<p`.

## Concrete targets for the checker/proof

1. Improve the frozen `(g,h)=(3,4)` metric by proving exactly
   `13 Phi_10^(2)(19/400)>1`; then
   `p_c(X_{3,4})<19/400<1/beta(28,10+2sqrt(13))<=p_u`.

2. Prove a whole-family quantitative scope. The intended classification is every standard product `X_{g,h}` with `g,h>=2` except possibly `(2,2)`:
   - `(2,3)`: depth-two certificate at `p=73/1000`;
   - `(2,4)`: radius-one certificate at `p=1/16`;
   - `(3,3)`: radius-one certificate at `p=137/2000`;
   - `g>=3,h>=4`: monotone radius-one lower bound from `x=sqrt(4h-3)>18/5`;
   - `g=2,h>=5`: monotone radius-one lower bound from `x=sqrt(4h-3)>41/10`.

3. Stress-test the negation at `(2,2)`. Do not force a theorem: if the one-sided tree-fiber mechanism misses the nonbacktracking threshold even with the full tree cluster, record it only as a diagnostic unless an exact obstruction is proved.

The source-level universal conjecture remains OPEN regardless of success on this family. A restricted standard surface-product family is PARTIAL, and Peres's product theorem must be recorded in the prior-art section.