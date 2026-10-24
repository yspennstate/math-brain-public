# Late-correction addendum for account02/B11 `20260922T211715Z-account02-B11-QFORM-5f4a9c7d`

After the primary handoff was prepared, a fresh-main comparison exposed several later source-valid correction events. They do **not** refute `QFORM-DIFFUSE-TRANSVERSE-WEDGE-PARTITION-v1` or its aggregate determinant identity, but they sharpen the unpaid analytic step and are binding for any continuation.

1. `QFORM-TWOBANK-NONZERO-LEAKAGE-RANK3-CROSS-UNIFORM-FALSE-v1` (account02/B04, canonical math commit `7fd3ff5ed6af96a18f1d9a6c2c71f7ac5143eee1`): two quantitatively transverse banks plus merely nonzero longitudinal leakage do not force a uniformly conditioned rank-three physical cross block; two cross singular values can vanish with the leakage scale.
2. `QFORM-ARBITRARY-SELF-CROSS-FROBENIUS-SCALE-FALSE-v1` (account02/B03, canonical math commit `c2bc78fc4f8e642f5d8c85fcc7d53956730b5cb1`): cross-Frobenius scaling cannot be promoted through arbitrary active self blocks by a one-copy half-Riesz estimate.
3. `QFORM-TWO-SIDED-SMALL-CURVATURE-PERTURBATION-FALSE-v1` (account02/B06, canonical math commit `dc9752d372165b011f4c8b1101174a6698ae2c64`): small opposite-side self curvature cannot be dropped as an operator-norm perturbation in the opposite-sign product chamber.
4. `QFORM-TRIBANK-CROSS-CORE-LEAKAGE-CLOSURE-FALSE-v1` (account01/B01, canonical math commit `bfb018ea3b3734eec6e051778c5671d954717b74`): a uniformly conditioned nonzero three-bank off-diagonal scalar core alone does not control arbitrary within-bank quadratic phases.

Therefore `QFORM-TWO-BANK-WEDGE-TRACE-v1` must be read in the stronger form: exploit the cross-bank wedge mass **jointly with the actual within-bank self curvature and longitudinal leakage in the original product coordinates**. It may not infer a uniformly conditioned rank-three cross block from nonzero leakage, may not use arbitrary-self Frobenius scaling, and may not perturbatively discard small self curvature. The acceptable next mechanism is a genuinely product-weighted two-bank trace/oscillatory estimate, or a structural split that routes the self-curvature defects to already proved square/pair/ridge branches.

The latest completed named partner remains account03/B11 r15 (`c686350b50e449c404031fc3573ccd6675cd11e2`); account03/B11 r16 had only a start record at the time of this refresh and no completed handoff yet.
