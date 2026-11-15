# Worker drafts and measurements from the open-problem frontier, October 2026

This folder holds the working material of solver agents on three rows of the open-problem list in
`results/open-problems/top200-probability-list-2026-10`. The audited claims and their reviews are in
`results/open-problems/frontier-worker-results-2026`. Here are the drafts and the measurements that led to them,
kept as the agents left them. Nothing here is a finished paper. A draft counts as a result only once an
independent audit admits it; the status line in each folder says whether that happened.

## measurements

- `w681/T039` — row T039, plurality is stablest for three cells (the standard simplex conjecture).
  - `proofs/NUMERICAL_METHOD.md` describes the discretisation. The step-4 operator of Heilman's linearisation
    was computed on radial and angular grids of increasing size, with the root drift across grids shown.
  - The measurement placed the crossing of the operator norm through 2 at rho ≈ 0.441 and the
    Hilbert–Schmidt bound's crossing at rho ≈ 0.4325. So the linearisation route cannot reach rho = 0.615.
  - `target2/` holds the certified extension to rho in [2/5, 43/100]: 61 interval slabs, with the worst
    full-operator upper bound 1.99947 < 2. Below 2/5 the result rests on Heilman's unrefereed preprint
    (arXiv:2608.00333v1).
  - The `archive_*` folders are the receipts that tie each claim to the exact files that were checked.
- `T039_C005_v2_recovery_20261015.json`, `T170_C010_v1_recovery_20261015.json` and
  `T186_C013_v1_recovery_20261015.json`, `T186_C014_C015_v1_recovery_20261015.json` — the recovery checks. In
  each one the hashes of the reviewed claims and witnesses were recomputed after a crash, before the claim was
  recorded.

## drafts

- `w685_T170_20261015` — row T170, the limit shape of first-passage percolation with Exp(1) weights in high
  dimension. It is an unaudited unique-height renewal argument for a diagonal lower bound in dimension 21. The
  bound is checked by exact scalar, norm and outward-rounded contraction certificates. Section 4 of
  `proofs/unique_height_renewal.md` is the step that most needs review.
- `w685_T170_dimensions_20261015` — the same encoded renewal operator, certified for dimensions 18 and 19,
  using exact rational coefficients and outward rounding. The certificates are exact. The first-passage reading
  of them depends on the unaudited geometric argument.
- `w685_T170_audit_20261015` — an independent audit of the two folders above, including its own dimension
  extension.
- `w713/T267` — row T267, epoch-wise double descent. Seven unaudited draft claims for two-layer ReLU networks
  trained by gradient descent in restricted settings: fixed label noise, a four-atom population and paired
  initialisation. Exact finite algebra checks cover the stated identities only. The weakest step is the
  nonlinear finite-horizon transfer in Section 6 of claim C013.

The parameter file `scripts/hybrid2_certificate_parameters.json` (7.7 MB) is included once, in
`w685_T170_20261015/scripts`. The dimensions folder uses the same file: copy it across before running
`run_renewal_extension.py` there.

## Credit

The T039 measurements and certificates use the linearisation and the radial Laguerre block method of Heilman
(arXiv:2608.00333). Its range below 2/5 is Heilman's, and the new range extends his method. The T267 drafts use
the ReLU kernel computations of Heckel and Yilmaz (arXiv:2007.10099) and the noise phases of Stephenson and Lee
(arXiv:2108.12006). The T170 drafts extend the row's frontier argument, which is cited in the row's entry in the
open-problem list.
