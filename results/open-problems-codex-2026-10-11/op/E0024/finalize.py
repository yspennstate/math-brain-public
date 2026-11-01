from pathlib import Path
import json
lean=Path('lean_check.txt').read_text(encoding='utf8')
assert 'exit=0;' in lean and 'sorryAx' not in lean
ls=Path('SharpComparison.lean').read_text(encoding='utf8')
assert 'import Mathlib\n' not in ls and 'native_decide' not in ls and 'sorry' not in ls
rows=[json.loads(x) for x in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(rows)==10 and all(r['problem_id']=='E0024' for r in rows)
for r in rows:
 if 'SharpComparison.lean' in r['proof_location']:
  r['checks']+=' Final Lean exit code 0; axioms [propext, Classical.choice, Quot.sound], no sorryAx.'
Path('CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf8')
p=Path('ATTEMPT.md');s=p.read_text();s=s.replace('- Lean: final result is recorded verbatim in lean_check.txt.', '- Lean: final run exited 0. Both shear_bound and shear_comparison have only [propext, Classical.choice, Quot.sound] as reported axioms; no sorryAx. The first run failed because PowerShell wrote a UTF-8 BOM; a subsequent run caught the multiplication-order helper error. Both were corrected and the final result is recorded verbatim in lean_check.txt.');s+='\nOperational caveat: the user-prescribed brain.py recall command unexpectedly reported handing an index refresh to a detached process (pid 30276). No explicit brain-writing command was issued, and no process was killed. Subsequent work and result writes remained in this problem folder. The tool’s self-refresh is not mathematical evidence.\n';p.write_text(s,encoding='utf8')
Path('STATUS.md').write_text('STATE: DONE\nNEXT: Investigate uniform integrability of complex-slice energies for a general (H) factor paired with a symmetric factor, as specified in ATTEMPT.md Section 7.\nVERDICT: PARTIAL\n\n2026-10-12: Confirmed unrestricted Question 4/4′ from source pp.15,18; queried arXiv, OpenAlex including both source citation records, Crossref, Semantic Scholar, and GitHub. No exact literature solution found; service failures logged.\n2026-10-12: Proved universal product/sum closure equivalence, a density-qualified common-Rao special case, sharp sector-perturbation comparison and symmetric-partner reduction. Earlier reduction is acknowledged; no general solution claimed.\n2026-10-12: Refuted two shortcut assertions (automatic resolvent-density tensorization and pointwise marginal-kernel domination); constructed a finite-energy diagonal measure outside finite-product domination. These are not counterexamples to (H).\n2026-10-12: Sharp algebra passed Lean with exit 0 and no sorryAx; 20000 seeded numerical checks and equality tests passed. Full proofs, imported theorem hypotheses, and precise unresolved correlated-measure gap saved. Bounded attempt complete; problem unresolved.\n2026-10-12: Operational caveat: prescribed brain.py recall reported its own detached index refresh; no explicit brain writes or process interventions were performed.\n',encoding='utf8')
assert Path('STATUS.md').read_text().splitlines()[0]=='STATE: DONE'
print('Validated all four research records; 10 claims; Lean exit 0, no sorryAx.')
print(lean)
