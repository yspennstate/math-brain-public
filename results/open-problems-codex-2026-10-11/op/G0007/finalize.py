from pathlib import Path
import json
p=Path('ATTEMPT.md')
s=p.read_text(encoding='utf8')
s+='''\n## 12. Why the qualitative method does not determine derivatives\n\nEven within independent invariant insertion-tolerant tree measures, a smooth choice of the density parameter can yield either a kink or continuous differentiability. On a small neighborhood of c, choose healthy occupied density p_1(lambda)=p_c-(lambda-c) or p_3(lambda)=p_c-(lambda-c)^3. Both are decreasing smooth densities in (0,1). The Section 11 expansion gives Theta_1(lambda)=A(c-lambda)+O((c-lambda)^2) on lambda<c, so it has a kink. For p_3 it gives Theta_3(lambda)=A(c-lambda)^3+O((c-lambda)^6); the analytic supercritical branch has derivative tending to zero and the zero branch on lambda>=c gives a continuously differentiable transition. These are not contact-process laws. They demonstrate that weak continuity and insertion tolerance alone cannot settle the derivative assertions; additional rate-dependent contact-process information is essential.\n'''
p.write_text(s,encoding='utf8')
checks='''# Verification record — G0007, 2026-10-11

- checks.py completed successfully: 1,442 finite labeled trees, 24 Bernoulli branching-excess cases, 76 Poisson-count density cases. Exact counts/float discrepancies in checks.json.
- surrogate_checks.py completed successfully: near-critical independent site-percolation slopes for d=3,5,7,20 converge to 2d/(d-2); detailed results in surrogate_checks.json. This is a different-model sanity check, not numerical evidence about nu_lambda derivatives.
- The analytic proofs were reviewed for sample-dependent mark insertion, strict time ordering, preservation of outside final states, exclusion of all-constant configurations, continuity of reciprocal cluster size, all possibilities for the number of infinite clusters, and fixed-ball merging. The precise arguments appear in ATTEMPT.md Sections 2--7. No branch independence or uniform finite-energy bound is assumed.

## Lean status

File: ~/brain_workers/TRIO_1011/op/G0007/MarkovObstruction.lean.
Command launched from ~/lean_verify:

    lake env lean ~/brain_workers/TRIO_1011/op/G0007/MarkovObstruction.lean

Only one Lean command was launched. It imports Mathlib.Tactic.FieldSimp and Mathlib.Tactic.Linarith, contains no sorry and no native_decide, and isolates the three-variable algebraic contradiction in ATTEMPT.md Section 8. The shared Lean wrapper reported that it was waiting for a slot. As of this record, no kernel result has returned. This file is NOT described as Lean-checked. The main continuity proof is a written analytic proof and has not been formally verified in Lean. The pending check does not replace any human proof step.

## Path error

The initial Lean setup command used Set-Content with a relative path while its working directory was ~/lean_verify. Consequently it also created ~/lean_verify/MarkovObstruction.lean outside the authorized G0007 folder. This was an execution mistake, acknowledged to the user. All subsequent artifact writes used G0007; no outside file was deleted or moved, in accordance with the user's prohibition. The accidental copy is not an output artifact of this folder and was not altered after the mistake.
'''
Path('CHECKS.md').write_text(checks,encoding='utf8')
# Update a claim without claiming a pending kernel check as successful.
rows=[json.loads(l) for l in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
for r in rows:
 if r['claim'].startswith('A nontrivial homogeneous'):r['checks']='Complete algebraic proof in Section 8. Lean command launched once but still queued; NOT kernel-checked. See CHECKS.md.'
Path('CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf8')
Path('STATUS.md').write_text('''STATE: DONE
NEXT: Independently review the finite Poisson surgery proof; seek near-critical quantitative estimates for healthy continuous differentiability and infected failure of continuous differentiability; collect the pending Lean result.
VERDICT: PARTIAL

2026-10-11: Source downloaded and exact hypotheses verified (d-regular tree, d>=3, recovery rate 1, transmission rate lambda per neighbor). Accessible arXiv/Crossref/Semantic Scholar/GitHub searches found no exact later solution; OpenAlex was budget-blocked and some other endpoints rate-limited. Complete author proofs in ATTEMPT.md establish no infected cluster at lambda_p and no healthy cluster at lambda_p^c, and hence continuity of both transitions. Proof ingredients: weak continuity, continuous invariant-tree branching excess, sample-dependent finite Poisson insertions, stationary final-state surgeries, and fixed-ball merging. The two derivative assertions remain unresolved; this is not a solution of the full problem. Finite/numerical sanity checks passed. The optional Lean algebra command is still waiting for a shared slot and is not reported as checked. CHECKS.md documents the accidental outside-folder Lean setup file. No brain/ledger/repository write, commit or push was performed.
''',encoding='utf8')
print('Final records saved; verdict PARTIAL, state DONE')
