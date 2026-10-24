from pathlib import Path
import json
p=Path('.')
log=p.joinpath('radial_lean_check.log').read_text(encoding='utf8');assert 'EXIT_CODE: 0' in log
src=p.joinpath('RadialRigidity.lean').read_text(encoding='utf8');assert 'sorry' not in src and 'native_decide' not in src
for name in ['radial_followup_checks.json','boundary_followup.json','exact_linearisation_checks.json']:json.loads(p.joinpath(name).read_text(encoding='utf8'))
with p.joinpath('FOLLOWUP.md').open('a',encoding='utf8') as f:f.write('''

## Final verification and verdict

RadialRigidity.lean compiled successfully, exit code 0, using `lake env lean ~/brain_workers/TRIO_1011/op/E0066/RadialRigidity.lean` from ~/lean_verify with a 3600-second timeout. It imports only Mathlib.Data.Real.Basic and Mathlib.Tactic.Linarith. Its proof uses nlinarith to construct a kernel-checked proof of the scalar midpoint rigidity step. Reported axioms: propext, Classical.choice, Quot.sound. No sorry or native_decide. The complete linearisation, finite-group, block-mass, and asymptotic arguments remain written mathematical proofs rather than fully formalised Lean results. Initial missing-module and missing-real-import failures are preserved in radial_lean_check_initial.log and radial_lean_check_import_failure.log; the repaired successful result is radial_lean_check.log.

The serious follow-up is complete. VERDICT: PARTIAL. It supplies a complete asymptotic description and basin classification for every interior initial state, an exact affine-linear interior periodic locus, a sharp permutation-order bound, and a shorter rigidity proof. It also covers all constant-support boundary cycles. These deductions survived the stated referee checks; novelty is not asserted. The unsolved case in this attempt is boundary periodic cycles with repeated positive values and changing supports. The alternative nonnegative tensor-lift approach remains an unproved representation question and is not used in any result. No full-source solution or exact literature-solution claim is made.
''')
rows=[json.loads(l) for l in p.joinpath('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
for row in rows:
 if row['proof_location'].startswith('FOLLOWUP.md'):
  row['checks']='Complete proofs and hostile audit in FOLLOWUP.md; radial scalar algebra Lean checked, exit 0; 48 LP linearisation controls and exact rational nonlinear example/global projection identity passed. Full analytic theorem not formalised.'
p.joinpath('CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf8')
with p.joinpath('ATTEMPT.md').open('a',encoding='utf8') as f:f.write('\n\n## Second-attempt conclusion, 2026-10-12\n\nTwo previously untried approaches and complete follow-up proofs are in FOLLOWUP.md. The uniform-point reduction now gives explicit limits and basins for all interior trajectories: V^n(x)-P^n R x tends to zero. The partition-averaging projection R and permutation P are determined by the uniform linearisation. All interior periodic points form an affine-linear slice; the sharp limiting period bound is g(m). Constant-support boundary cycles are also covered. The remaining gap is repeated-positive-value boundary cycles with moving supports, and their full classification. Lean radial algebra, exact symbolic examples, and hostile LP checks passed. Final STATE: DONE, VERDICT: PARTIAL.\n')
p.joinpath('STATUS.md').write_text('''STATE: DONE
NEXT: For a future attempt, classify boundary cycles with repeated positive values and varying supports; investigate the recorded nonnegative tensor-lift representation or seek exact certificates for the small support-cycle LP exclusions.
VERDICT: PARTIAL

2026-10-12: Serious follow-up requested and completed. Read ATTEMPT.md and its gap. Wrote two new approaches: uniform-point linearisation/radial rigidity, and a nonnegative tensor lift to state-weighted doubly stochastic matrices. Pursued the first; the second remains unproved and unused.
2026-10-12: Asked the brain for the exact repeated-coordinate cycle gap and for Birkhoff–von Neumann/equality. Birkhoff card was relevant; a full matching/decomposition proof was written rather than relying on recall as a verdict.
2026-10-12: Proved B=DV(c)-J/m is doubly stochastic; all interior norm-equality points satisfy V(x)=Bx. Computed the exact affine-linear interior periodic locus via at most m-1 linear preimage intersections. All interior cycles and all constant-support boundary cycles follow one coordinate permutation; limiting interior periods obey the sharp maximal-permutation-order bound g(m).
2026-10-12: A further block-mass rigidity argument proves RV(x)=PRx globally, for a computable block-averaging projection R and one fixed permutation P. Every interior trajectory satisfies norm(V^n(x)-P^nRx) tending to zero, explicitly determining its limiting cycle and basin. Full proofs: FOLLOWUP.md Theorems 6, 9, 10.
2026-10-12: Hostile audit completed. Forty-eight repeated-coordinate interior LP controls agree with the linearisation (largest Bx error 9.16e-16). Four hundred eighty boundary cycle LP cases were infeasible; these are numerical evidence only. Exact rational symbolic tests verified the nonlinear example, global projection identity, and finite preimage chains.
2026-10-12: RadialRigidity.lean passed with exit 0; narrow Real.Basic and Tactic.Linarith imports, nlinarith kernel proof, no sorry or native_decide. The full mathematics is not formalised. Final gap: moving-support boundary cycles with repeated positive values, and a complete source-wide boundary classification. No novelty or literature-solution claim. DONE means this strengthened partial attempt is finished.
''',encoding='utf8')
assert p.joinpath('STATUS.md').read_text(encoding='utf8').splitlines()[0]=='STATE: DONE'
print('STATE: DONE; VERDICT: PARTIAL. Follow-up proofs, Lean success, claims, and narrowed gap saved.')
