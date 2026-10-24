# Conditional/overlap energy ledger

Family: `f_{d,h}=q_0 q_z`, the product of two point defects on the same
physical `d`-cube, with `wt(z)=h`.

| Quantity | `h=1` | `h>=2` |
|---|---:|---:|
| Negative vertices | 2 adjacent | 2 nonadjacent |
| Nonempty spectral support | `2^(d-1)-1` | `2^(d-1)-1` |
| Each nonempty squared coefficient | `16*2^(-2d)` | same |
| Influence | `4(d-1)2^(-d)` | `4d2^(-d)` |
| `H/I` limit | point defect in `d-1` dimensions | `4` uniformly in `h` |
| `U/I` limit | point defect in `d-1` dimensions | `1` uniformly in `h` |

The physical inputs are shared: the two component defects use the same
coordinates, and Fourier coefficients are rederived from the two-atom truth
table. No disjoint-product additivity is invoked.

The adjacent endpoint exhibits real overlap cancellation: compared with the
sum of the two component influences, exactly `4*2^(-d)` is removed. This is
fully reflected by the reduction to a `(d-1)`-dimensional point defect.

The repaired payments stay bounded:

- `H < 4 I` for every `(d,h)`;
- `U < 3 I` for every `(d,h)`;
- for all sequences `2<=h_d<=d`, `H/I -> 4` and `U/I -> 1`.

Thus finite-site overlap changes spectral geometry but supplies no divergent
actual FEI or upper-set-potential ratio. A growing cluster or gate with a
nontrivial boundary/spectral tradeoff is the next mechanism to test.
