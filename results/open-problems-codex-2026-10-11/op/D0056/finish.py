from pathlib import Path
import json
root=Path('.')
lean=root.joinpath('lean_check.txt').read_text(encoding='utf8')
assert 'Exit: 0' in lean
src=root.joinpath('Barrier.lean').read_text(encoding='utf8')
assert 'sorry' not in src and 'native_decide' not in src
with root.joinpath('ATTEMPT.md').open('a',encoding='utf8') as f:
 f.write('\n## Final verification record\n\nThe final Lean run returned exit code 0 in 105.18 seconds. Earlier attempts failed due to a UTF-8 BOM and a missing Mathlib.Data.Real.Basic import; both were corrected before the successful run. Both theorems in Barrier.lean now pass kernel checking. The numerical script passed 4,200 exact rational cases and 50-digit normalization and criticality checks.\n')
with root.joinpath('LITERATURE.md').open('a',encoding='utf8') as f:
 f.write('\nAdditional during-attempt read-only math-store query (2026-10-11): `Chen Shi stable Derrida Retaux system criticality`; results were word matches for unrelated Chen/Shi papers and stable-distribution material, not a usable Derrida–Retaux theorem.\n')
root.joinpath('STATUS.md').write_text('''STATE: DONE
NEXT: No further work required for the stated hypothesis; a separate question would be survival asymptotics under finite E[X_0^3 m^{X_0}].
VERDICT: SOLVED
2026-10-11: Verified arXiv source Conjecture 1, including nonconstant standing assumption and warning about stronger integrability.
2026-10-11: Queried arXiv, Crossref, OpenAlex, Semantic Scholar, and GitHub. OpenAlex rate-limited; Semantic Scholar DOI citations succeeded. No exact solution theorem was identified, so not SOLVED_IN_LITERATURE.
2026-10-11: Constructed a nonconstant binary critical law p_0=cB, p_1=0, p_k=c 2^{-k}k^{-3}, k>=2. It meets every original hypothesis.
2026-10-11: Chen–Shi Theorem 1.1 gives generating-function product Q_n<=Cn. An exact-recurrence barrier proves that the proposed survival asymptotic would force Q_n>=Kn^{3/2}, a contradiction. Full proof and referee checks in ATTEMPT.md.
2026-10-11: Final Lean check exited 0; two algebraic lemmas checked without sorry or native_decide. All 4,200 exact rational checks passed. Actual heavy-tail coefficient and stronger-moment conjecture are not proved here.
''',encoding='utf8')
for name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','Barrier.lean','lean_check.txt','checks.txt']:
 p=root/name;assert p.exists() and p.stat().st_size>0
for s in root.joinpath('CLAIMS.jsonl').read_text(encoding='utf8').splitlines():json.loads(s)
assert root.joinpath('STATUS.md').read_text(encoding='utf8').splitlines()[0]=='STATE: DONE'
print(root.joinpath('STATUS.md').read_text(encoding='utf8'))
