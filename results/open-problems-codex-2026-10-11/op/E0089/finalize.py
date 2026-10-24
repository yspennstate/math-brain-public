from pathlib import Path
import json
for name in ['ATTEMPT.md','LITERATURE.md','STATUS.md']:
 p=Path(name);p.write_text(p.read_text(encoding='utf-8-sig'),encoding='utf8')
rows=[json.loads(s) for s in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(rows)==10
assert all(x['problem_id']=='E0089' for x in rows)
assert 'Exit: 0' in Path('lean_check.txt').read_text(encoding='utf8')
assert json.loads(Path('profile_checks.json').read_text())['nonconstant_monotone_functions']==166
assert json.loads(Path('experiments.json').read_text())['forced_endpoint_check']=='all 256 masks passed'
assert 'Proposition 4' in Path('ATTEMPT.md').read_text(encoding='utf8')
status='''STATE: DONE
NEXT: Establish the fixed-K independent-replica factorization (ATTEMPT.md equation (6)), or a graph-specific central profile gap with probability tending to one.
VERDICT: PARTIAL

2026-10-12: Completed bounded literature search, source verification, and proof attempt. No exact published solution found. OpenAlex returned HTTP 429; Semantic Scholar citation endpoint succeeded and all three returned citing PDFs were screened.
2026-10-12: Corrected the intake: source Remark 3.4 defines phi(G), a conditional success probability, not a critical density; the source already discusses the Azuma obstruction. Distinguished graph-specific and annealed medians.
2026-10-12: Proved median-threshold tightness q_G-p*=O_P(n^-1/2) from the source theorem, an explicit finite profile/noise lower bound, a fixed-K conditional-success sufficient criterion, the replica variance identity, a valid switching comparison, and bootstrap/core duality.
2026-10-12: Proved a counterexample to a general annealed-window-only inference using random ensembles of block-majority functions. This is not a counterexample to E0089.
2026-10-12: Exact enumeration of two 8-vertex 4-regular graphs completed; Lean core decide +kernel checked regularity, a seed-changing switch, and all 256 forced-endpoint cases (exit 0). Exact rational checks of all 166 nonconstant monotone functions on four bits passed.
2026-10-12: Final referee review completed. E0089 remains unresolved here: fixed-K quenched concentration/two-replica factorization is unproved. Ten claim records saved in CLAIMS.jsonl. This bounded attempt is complete, with its remaining gap documented.
'''
Path('STATUS.md').write_text(status,encoding='utf8')
print('Final records validated:',len(rows),'claims; Lean exit 0; 166 exact profile checks. STATE: DONE, VERDICT: PARTIAL.')
