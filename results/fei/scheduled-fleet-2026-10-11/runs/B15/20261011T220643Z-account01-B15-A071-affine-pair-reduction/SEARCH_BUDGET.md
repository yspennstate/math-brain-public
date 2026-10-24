# A071 signed affine-cell search budget

## Frozen domain

- Two address bits and four physical bits.
- Three pairwise-disjoint signed two-point conditional cells.
- Product normalized squared Walsh law required for every conditional row.
- Same residual search domain as the prior immutable A071 baseline.

## Precomputed counts

| quantity | count |
|---|---:|
| unordered physical pairs | 120 |
| relative signs per pair | 2 |
| signed local cells | 240 |
| product-law signed cells | 64 |
| relative sign patterns for three slices | 8 |
| naive prior representatives times signs | 8,126,464 |

The analytic product-support lemma and monotonicity identity replace the
8,126,464-case rerun.  Completeness does not rely on sampling.

## Hard caps and actual execution

| resource | cap | observed |
|---|---:|---:|
| local signed cells | 240 | 240 |
| assembled witness controls | 8 | 8 |
| wall time | 30 seconds | under 1 second |
| memory | 64 MiB | below cap |
| randomness | none | none |

No increase in dimension is authorized by this design.  Any later search must
freeze a higher-support conditional-row family and prove its count first.
