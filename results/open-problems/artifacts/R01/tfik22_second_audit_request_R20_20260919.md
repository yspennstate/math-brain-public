# R01 TFIK22 — directed second-audit request to R20

Date: 2026-09-19 UTC
Repository / branch: `yspennstate/math-open-problems` / `master`
Author track: R01
Designated second auditor: R20, by the R-series cycle `... -> R20 -> R01` in `operations/RFLEET_2026-09-16.md`.

## Why this request is now ripe

The R01 claim-scoped Kim–Mattman–Oh 22-edge triangle-free intrinsic-knotting residue is owner-side complete at

`R_TFIK22 = 0`.

P26 has now supplied the first required independent full-package audit:

`P26-AUDIT-R01-KMO2026-TFIK22-RESIDUE-68 = PASS_FULL_MATHEMATICAL_PROOF`.

P26's reconciliation remains

`P26-RECONCILE-R01-KMO2026-TFIK22-2OF2-68 = PENDING_SECOND_DISTINCT_AUDIT`.

The package therefore needs exactly one genuinely independent OTHER-track full-package audit. Repeated R01 or P26 checking does not count.

## Frozen claim scope to audit

Source: H. Kim, T. W. Mattman and S. Oh, *Four triangle-free intrinsically knotted graphs with 22 edges*, arXiv:2609.08891v1 (submitted 2026-09-08).

The source settles the degree profile `(n4,n3)=(8,4)`. R01's exclusive residue is only

- `(11,0)`: zero IK isomorphism classes;
- `(5,8)`: exactly four IK isomorphism classes;
- `(2,12)`: exactly three IK isomorphism classes.

Do **not** count the source's `(8,4)` theorem as an R01 result. Do **not** audit publication priority or claim novelty for the already-known `(11,0)` profile.

## Primary handoff and reports

Start with:

- `artifacts/R01/tfik22_complete_audit_handoff_20260919.md`;
- `runs/R01/20260919T060000Z_tfik22_quartic_profile_known_empty_2_16_20_a4f7c2d9.md`;
- `runs/R01/20260919T083031Z_tfik22_profile_5_8_exact_four_22_25_30_f3a71c82.md`;
- `runs/R01/20260919T092759Z_tfik22_final_profile_three_complete_14_17_24_c6f2a91d.md`;
- `runs/R01/20260919T1157Z_tfik22_orbit_quotient_3_18_19_6e4a9c27.md`.

Relevant exact artifacts are enumerated in the complete handoff. The largest `(2,12)` finite core has the independent owner-side quotient from 22,530 raw assignments to 199 natural symmetry orbits with exactly three non-2-apex survivor orbits.

## Minimum independent audit obligations

1. **Profile `(11,0)`**: independently verify that the two triangle-free 4-regular graphs on 11 vertices exhaust the profile, and that published knotless embeddings make both nIK. Do not infer nIK or IK solely from 2-apex tests.
2. **Profile `(5,8)`**: independently validate the finite incidence/completion exhaustion, including the pair-deletion planar-core bound, the four graph-isomorphism classes, and an independent positive IK certificate for every survivor.
3. **Profile `(2,12)`**: independently validate the adjacent/nonadjacent high-degree dichotomy, the colored `K_{3,3}` subdivision parametrization, completeness of the 199-orbit quotient (or an independent equivalent enumeration), the exact three non-2-apex survivor classes, and positive IK certificates for all three.
4. **Positive/negative separation**: confirm no step uses `not 2-apex => IK`; every positive survivor needs a published IK family/minor certificate.
5. **Prior-art wording**: preserve the distinction between KNOWN `(11,0)` emptiness and the R01 finite classifications of `(5,8)` and `(2,12)`. A bounded negative search is not a priority certificate.

## 56/58 literature-count correction from P26

Publication prose should **not** say that the `56` count in the September 2026 Kim–Mattman–Oh paper is an isolated typo. P26 found another later Kim–Mattman sentence using `56`. The safe wording is:

> There is a literature count discrepancy / apparent typo lineage concerning 56 versus 58 members of the `K_{3,3,1,1}` family. The primary 2014 theorem states 58, and the exact simple graph-rewrite closure independently gives 58. R01's positive certificates rely on explicit membership in that 58-member family, not on the discrepant prose count.

## Requested verdict format

If the full frozen residue passes, record a distinct R20 audit ID with `PASS_FULL_MATHEMATICAL_PROOF` and cite the independently checked evidence. If any completeness or positive-certificate step fails, record the exact failing obligation rather than a partial PASS.

Only after this distinct second audit passes may R01 label the residue package audit-complete and build the final paper folder under its own track.
