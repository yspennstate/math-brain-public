from pathlib import Path
import json
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf8');s=s.replace('an independent exhaustive 2^12-edge-configurations check on R=1 is being added','an independent exhaustive 2^12-edge-configurations check on R=1 passed');s+='''

## Final verification receipt (2026-10-11)

- `check_partitions.py`: ALL_EXACT_CHECKS_PASS (all 14 noncrossing partitions, all 16 restored-star states, polynomial orbit coefficients and dual failure weights).
- `CriticalFirstStep.lean`: checked by `lake env lean` from the specified lean_verify project, exit 0. Only Mathlib.Data.Real.Basic and Mathlib.Tactic.Linarith imported; no sorry, no native_decide. Lean reports only the usual propext, Classical.choice, Quot.sound axioms. The algebra proof is kernel-checked; the complete probabilistic theorem is written above.
- `box_verification.json`: independent enumeration of all 4096 configurations of the 3 by 3 free square agrees coefficientwise with the transfer recurrence; all stated same-boundary finite-box signed counts are nonnegative.
- `verify_final.py`: free and wired 7 by 7 counts agree with recalculation in REVERSED edge order; wired 3 by 3 target-on-boundary counts equal the exact star formula 1-(1-p)^4; wired counts dominate free counts coefficientwise; the signed degree-84 polynomial factorization is exact; every stored rational Bernstein coefficient is recomputed and exceeds 3/10 on the certified intervals. All checks passed, recorded in final_verification.json.
- The free-minus-wired comparison at p=1/2 is exactly -302861607514102889507865/4835703278458516698824704, so this attempted global certificate fails there. This failure is correctly recorded as an obstruction, not a counterexample to G0008.
- Literature follow-up: Semantic Scholar's source citations endpoint eventually succeeded and returned zero indexed citations. OpenAlex remained rate-limited; literature status is a bounded negative search, not a certified exhaustive novelty assessment.

Final disposition: DONE / PARTIAL. The research pass is complete with two proved infinite-lattice first-step restrictions, exact finite-box comparisons and an explicit unresolved all-parameter/all-distance gap. No complete proof or counterexample to G0008 is claimed.
''';p.write_text(s,encoding='utf8')
rows=[json.loads(v) for v in Path('CLAIMS.jsonl').read_text().splitlines()]
rows[0]['checks']=['Independent 14-partition by 16-star-state rational enumeration passed.','CriticalFirstStep.lean passed with exit 0; only the real algebra implication is formalized.','Planarity, self-duality, FKG and strictness cylinder written out in ATTEMPT.md.']
rows[3]['checks']=['All signed Bernstein counts nonnegative.','Coefficient totals equal binomial counts.','Independent brute-force 4096-configuration radius-one verification passed.']
rows[-1]['checks']=['Exact degree-84 free/wired connection polynomials and degree-77 factorization.','All 78 normalized Bernstein coefficients exceed 3/10 on each stated interval by rational arithmetic.','Reverse-edge transfer computations agree coefficientwise.','Wired radius-one calculation agrees with exact star formula.','Every certificate coefficient recomputed and checked in verify_final.py.']
Path('CLAIMS.jsonl').write_text(''.join(json.dumps(v)+'\n' for v in rows),encoding='utf8')
Path('STATUS.md').write_text('''STATE: DONE
NEXT: Seek a width-uniform signed transfer invariant, or a larger certified boundary comparison, covering the remaining n=1 middle parameters and then n>=2.
VERDICT: PARTIAL

2026-10-11: Downloaded and verified Campos--de Lima arXiv:2601.00291v1. It explicitly calls the axial iid bond-percolation question open. Bounded arXiv, Crossref, Semantic Scholar and GitHub searches found no solution; OpenAlex rate limits prevented complete citation lookup. Exact queries and references are in LITERATURE.md.
2026-10-11: Audited prior records. Rejected crude uniform path-count reasoning and corrected the unsupported inference from supercritical truncated connectivity to full connectivity.
2026-10-11: Proved tau_1(1/2)-tau_2(1/2)>=9/2048 on Z^2, strengthening the prior critical first-step bound. Complete geometric/probabilistic proof is in ATTEMPT.md. Independent partition enumeration passed; its key real algebra implication passed Lean 4 with no sorry or native_decide.
2026-10-11: Proved tau_1(p)-tau_2(p)>=(3/10)p(1-p)^6 for 0<p<=2/5 or 23/25<=p<1 by exact free/wired 7x7 box comparison and rational Bernstein certificates. Reversed-edge recomputation, exact factorization and every rational coefficient check passed.
2026-10-11: Exact free finite-square comparisons passed for every p on B_2 (1>=2) and B_3 (1>=2>=3); independent 3x3 exhaustive enumeration agreed. These alone give no infinite-lattice theorem.
2026-10-11: Completed this research pass. Full all-p/all-n Z^2 and all-d axis monotonicity remain unresolved; no percolation counterexample was found. All work and verification artifacts are in this folder.
''',encoding='utf8')
print('FINAL RECORDS SAVED; claims',len(rows))
