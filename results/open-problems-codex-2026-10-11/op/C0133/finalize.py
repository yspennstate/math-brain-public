from pathlib import Path
import json
r=json.loads(Path('lean_result.json').read_text(encoding='utf8'));assert r['returncode']==0
p=Path('ATTEMPT.md');s=p.read_text(encoding='utf8');s+='\n\nFormal verification: lake env lean ~/brain_workers/TRIO_1011/op/C0133/FiniteChecks.lean, run from ~/lean_verify with a 3600-second timeout, completed with exit code 0. The saved source imports only Mathlib.Data.Real.Basic, Mathlib.Tactic.Linarith, and Mathlib.Tactic.Ring. It checks finite harmonic-profile uniqueness and the returning-excursion length inequality, with no sorry or native_decide. The probability proofs and literature theorem are not formalized by that file. See lean_result.json and lean_check.log.\n';p.write_text(s,encoding='utf8')
p=Path('CHECK_HISTORY.md');s=p.read_text(encoding='utf8');s+='\nFinal Lean run passed with exit code 0. Both theorem declarations are kernel-checked; no axiom placeholders were introduced. The complete stochastic conclusions remain handwritten proofs with the scope stated in ATTEMPT.md.\n';p.write_text(s,encoding='utf8')
rows=[json.loads(l) for l in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
for c in rows:
 if 'return-time ratio' in c['claim'] or 'tail 1/(2L)' in c['claim']:
  c['checks'].append('FiniteChecks.lean passed: finite harmonic profile and two-sided excursion-gap arithmetic only; probability and limit argument not formalized.')
Path('CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in rows),encoding='utf8')
Path('STATUS.md').write_text('''STATE: DONE
NEXT: If resumed, investigate sublinear range on the non-transient event for bounded IID cookie stacks in d=2, which would close the drift-budget reduction in that special case.
VERDICT: PARTIAL

2026-10-12: Confirmed exact Problem 4.7 in arXiv:1204.1895v2, p.19: IID whole stacks, EL, all d>=1, arbitrary nonzero direction; infinite stacks allowed.
2026-10-12: Searched arXiv, OpenAlex including both source citation sets, Crossref, Semantic Scholar (429) and GitHub (403). No full exact-hypothesis literature solution verified; failed API requests and bot-challenge PDFs are recorded as coverage gaps.
2026-10-12: Verified the full d=1 case using Amir-Berger-Orenshtein Theorem 1.3 plus bounded return subsequences. Proved balanced-cookie zero speed, exact martingale-drift reduction, conditional range/return-gap criteria, and a sign-restricted timed-return bound.
2026-10-12: Constructed a recurrent uniformly elliptic adaptive process with normalized liminf 0 and limsup 1/2, explicitly outside the fixed IID cookie model; it refutes a generic submartingale proof route, not C0133.
2026-10-12: Exact rational computations and exhaustive 4096-path checks passed; short IID cookie-stack simulations were recorded without asymptotic claims. Lean finite harmonic uniqueness and return-gap algebra passed (exit 0), after documented encoding and substitution corrections.
2026-10-12: Attempt closed with precise remaining gap: D_n=o(n) on returning paths for arbitrary signed-drift IID elliptic stacks in d>=2. No complete proof or counterexample is claimed.
''',encoding='utf8')
assert Path('STATUS.md').read_text().splitlines()[0]=='STATE: DONE'
print('STATE: DONE; VERDICT: PARTIAL; Lean exit',r['returncode'],'elapsed',r['elapsed_seconds'],'claims',len(rows))
