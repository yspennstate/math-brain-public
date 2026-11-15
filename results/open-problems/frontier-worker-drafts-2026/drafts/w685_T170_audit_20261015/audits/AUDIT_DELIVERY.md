# T170 target 2: completed requested internal audit

C013-v4 and C018-v1: INTERNAL CLEAN. This is a same-worker proof audit, not independent-model approval. No first unrederived load-bearing step remains after the derivations and arithmetic checks below. Novelty remains unverified. The independently approved fallback remains C003-v2.

The audit rederives shortcut-edge disjointness and the conditional joint survival law, the pending-moment pair integration and similarity direction, seed and terminal factors, exhaustive state closure, the scalar bridge recurrence and omitted tail, all-length prefix/no-cut/suffix quotas, and the passage from a finite tilted sum to the Euclidean FPP bound. The complete derivation is proofs/renewal_self_audit.md.

| Check | Measured coverage |
|---|---:|
| Coordinate state and transition inventory | 641 states, 1,282 mark rows, 7,952 transition records |
| Exact rational common-norm inequalities | 2,564 per dimension, 7,692 total |
| Scalar renewal coefficients from killed-walk counts | 400 per dimension, 1,200 total |
| Outward renewal rows | 330 per dimension, 990 total |
| Strict irreducible profiles through length 21 | 8,912 per dimension |

| d | Original stated kappa upper, denominator 10^18 | Second implementation upper, denominator 10^18 | Exact downward ratio floor |
|---|---:|---:|---:|
| 21 | 999987264585312187 | 999987264583446072 | 0.073881518494 |
| 19 | 999936480509838187 | 999936480507989273 | 0.077855718601 |
| 18 | 999907618879537695 | 999907618877687690 | 0.080099928228 |

Every second upper bound is below the original stated upper bound and below one. The second implementation imports no producer. It uses full coordinate histories for graph closure, killed-walk counts instead of reflection counts, a polynomial dictionary for the exact integrals, and a separately proved positive-sum rounding enclosure with explicit binary-bin accumulation. Earlier, looser audit enclosures are retained locally as operator_initial_gamma_*; the tighter audit changes the arithmetic enclosure only, not the operator or its parameter point.

C019-v1 records the d18/d19 FPP consequences as proof (unaudited), with full hypotheses in proofs/renewal_dimension_theorem.md. Relative to the earlier C011-v3 candidates, the floors rise by 0.000007999952 and 0.000007999688 respectively. Both exceed CEG's 0.3313/sqrt(d) first-moment floor by more than 2.4 percent. No d18 non-ball conclusion is asserted. The received frontier brief independently records non-ball dimensions d19, d20 and d21 using the reviewed C003-v2 lower bounds and w676 upper bounds.

Reproduce from this directory:

```text
python -X utf8 scripts/audit_renewal_independent.py graph
python -X utf8 scripts/audit_renewal_independent.py arithmetic --d 21
python -X utf8 scripts/audit_renewal_independent.py operator --d 21
python -X utf8 scripts/audit_renewal_independent.py arithmetic --d 19
python -X utf8 scripts/audit_renewal_independent.py operator --d 19
python -X utf8 scripts/audit_renewal_independent.py arithmetic --d 18
python -X utf8 scripts/audit_renewal_independent.py operator --d 18
```

The checker runs on Windows/Python with NumPy, one core below normal, with at least 2 GB free and estimated peak below 1 GB. All seven phases exited zero. Every original certificate hash (25 files) was checked unchanged. Original producer snapshots are already backed up in commits 647cf9d076c0eca6151903bf8958a98dbcb218fd and 590dc71719c184f5cbe0511a675a0ba995731ac0 in the research repository.

One additional owner-work concept draft is staged in bundles/bundle_004.json; four bundles now contain 14 cards. No live store was changed. NEXT: independent review of the exact C013-v4, C018-v1 and C019-v1 claims, with the all-length encoding checked before any independent-proof designation.
