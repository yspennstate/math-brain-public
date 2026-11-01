# Source pins

## Current control and campaign sources actually read

- Owner control revision `2026-10-12.1`, commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
  - `ORDER.md` blob `81b6d6f988aee4489512c6e62543253900620453`
  - `CASE_TARGETS.json` blob `97e41262ebb4f09eec53630a918acae09efc9a48`
- Canonical `CURRENT_STATUS.md` blob
  `c416d4b4a83fc67965cb95d06a0cc80c5c29a520`.
- B12 compact contract blob
  `40935ac651643a17815d0addf664ec4c1c0313cc`.
- Canonical branch head refreshed before save:
  `8e917b7f2190d0d624de3469053f5cda4625978f`.
- Brain branch head refreshed before save:
  `4d0308f0be5bba148bbd0cc2be11b4e53e9c9b5a`.

## Exact original proof inputs used

- Previous B12 changing-witness theorem, canonical final commit
  `6cd9af0fa3ad7546a5559e504675bf750d5828e8`, folder
  `reports/fei-2026-10-11/runs/B12/20261012T042255Z-fleet01-B12-changing-witness-potential/`.
  - `REPORT.md` blob `1c71de9ea5cf83821aa7f0eaed69373ac5335c48`
  - `CLAIMS.json` blob `6ede93878f896c7bf621fba8adc43c33400cb334`
  - `PROGRESS.json` blob `19a296564ba03377b879c7a6224d28159b018e3a`
  - `CHANGING_WITNESS_TELESCOPE.tex` blob
    `632570123b40ce3f89ab9ecb11740c980dd30635`
- Independent fixed-source review by B19/A094, commit
  `e412fb2e8f85a78d807ff6d6c9c805254377ed88`, folder
  `reports/fei-2026-10-11/runs/B19/20261012T034859Z-fleet01-B19-b12-envelope-review-a094/`.
  - `REPORT.md` blob `fc09be40dc170838a26a342206595b6337365097`

The B19 review is evidence only for the fixed-source predecessor claim.  It is
not review evidence for the new shared-coordinate formula or no-go family.

## Standing mathematical controls used

The current obstruction registry was consulted at revision
`2026-10-12-a096-tree-slack`, in particular `OVERLAP_PRODUCT`,
`RAW_CONV_TENSOR`, weighted-local-total-correlation failures, and activation
equivalence.  This run does not infer failure of disjoint additivity, does not
confuse raw derivative entropy with normalized output entropy, and does not
claim that the tensor lift is an FEI counterfamily.

