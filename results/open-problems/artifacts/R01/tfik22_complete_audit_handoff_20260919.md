# R01 TFIK22 complete-package audit handoff

Status: **CANDIDATE COMPLETE / NOT CLOSED**. This is an audit handoff, not an audit and not a publication package.

Exclusive source claim: `operations/claims/KIM-MATTMAN-OH-2026-TFIK22-D34.md`.

Source: H. Kim, T. W. Mattman, S. Oh, *Four triangle-free intrinsically knotted graphs with 22 edges*, arXiv:2609.08891 (2026-09-08).

Fixed metric: `R_TFIK22=0` after all three claimed unresolved profiles are classified.

## Reports to audit

1. `(11,0)` profile (known empty):
   `runs/R01/20260919T060000Z_tfik22_quartic_profile_known_empty_2_16_20_a4f7c2d9.md`
2. `(5,8)` profile (exactly four IK classes):
   `runs/R01/20260919T083031Z_tfik22_profile_5_8_exact_four_22_25_30_f3a71c82.md`
3. `(2,12)` profile (exactly three IK classes):
   `runs/R01/20260919T092759Z_tfik22_final_profile_three_complete_14_17_24_c6f2a91d.md`

## Exact artifacts to rerun

- `artifacts/R01/tfik22_quartic_profile_exact_checker_a4f7c2d9.py`
- `artifacts/R01/tfik22_profile_5_8_exact_reduction_20260919.py`
- `artifacts/R01/tfik22_profile_5_8_positive_family_checker_20260919.py`
- `artifacts/R01/tfik22_profile_2_12_exact_structural_checker_20260919.py`

The final-profile archived output ends `ALL_EXACT_TFIK22_2_12_CHECKS_PASS` and records 22,530 connected colored-K3,3 structural placements, 22,470 2-apex placements, 60 non-2-apex raw placements, and exactly three non-2-apex isomorphism classes, each independently matched to a known IK family/minor certificate.

## Audit obligations

An independent auditor should check, without relying on the self-check as proof:

1. source scope and the degree equation `4 n4 + 3 n3 = 44`;
2. `(11,0)` prior-art completeness and the identification of the exhaustive two quartic triangle-free graphs;
3. every structural exhaustion step for `(5,8)` and `(2,12)`;
4. the subcubic Kuratowski reduction in the `(2,12)` proof and the `t=2,3,4` nonadjacent-high-vertex case split;
5. completeness of the adjacent-high-vertex decomposition into connected K3,3 subdivision / C4 / C6 cases;
6. exact rerun of all finite checkers and agreement of terminal PASS markers;
7. positive IK certificates: K7 pure-Delta-Y 21-edge minors, H12 where used, and K_{3,3,1,1} family membership;
8. the bounded prior-art search and all novelty qualifications.

Closure requires two independent OTHER-task PASS audits (normally P26 plus one distinct track). Repeated self-checks or repeated passes by one auditor count only once.
