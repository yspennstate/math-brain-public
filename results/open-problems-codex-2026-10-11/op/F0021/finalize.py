from pathlib import Path
import json,re
p=Path('.')
lean=json.loads(p.joinpath('LEAN_CHECK.json').read_text(encoding='utf-8'))
assert lean['exit_code']==0
code=p.joinpath('F0021.lean').read_text(encoding='utf-8')
assert not re.search(r'\b(sorry|native_decide)\b',code)
claims=[json.loads(x) for x in p.joinpath('CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
for c in claims:
 c['checks']=c['checks'].replace('Lean exponent arithmetic pending.','F0021.lean union_exponents_negative kernel-checked (exit 0).').replace('Lean ratio algebra pending.','F0021.lean restricted_mass_transfer kernel-checked (exit 0).').replace('Lean rational exponent check pending.','F0021.lean balanced_exponent_below_kpz kernel-checked (exit 0).')
p.joinpath('CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf-8')
with p.joinpath('ATTEMPT.md').open('a',encoding='utf-8') as f:f.write('''\n\n## Formal verification and final assessment\n\n`F0021.lean` passed Lean 4.33.1 / Mathlib, using only targeted imports (`Mathlib.Data.Real.Basic`, `Mathlib.Tactic.Linarith`, `Mathlib.Tactic.Positivity`). Command: `lake env lean ~/brain_workers/TRIO_1011/op/F0021/F0021.lean`, run from `~/lean_verify`, with a 3600-second timeout. Final exit code 0; elapsed 152.67 seconds. The file contains neither `sorry` nor `native_decide`. The four kernel-checked lemmas verify the union-bound exponent signs, the restricted-partition ratio inequality, the entropy-balanced exponent comparison with 1/3, and existence of the tube-cap exponent interval. They do not formalize the probability, regular variation, logarithm, or limiting-distribution arguments, whose complete handwritten proofs are above. The first run failed on a PowerShell-inserted UTF-8 BOM; that failure was corrected and is preserved separately in LEAN_INITIAL_CHECK.json and lean_initial_failure.txt.\n\n**Final verdict: PARTIAL.** The fixed-temperature KPZ/Airy assertion has neither been proved nor refuted. The current attempt proves the entropy-corrected isolated-spike bound, including an L1 rate; tail truncation facts in tubes and in the full cone; the original-confinement conditional free-energy transfer; and the raw/penalized maximum distinction. It refutes the earlier attempt's constant bare-walk access-cost argument. No reviewed later theorem closes the exact question; OpenAlex could not be accessed successfully. A future attempt must prove original-polymer confinement on a somewhat enlarged KPZ tube and establish a KPZ law for the capped nonintegrable model (or find a different universality method); an Airy process additionally requires spatial uniformity and tightness. No part of the wider, unaddressed phase diagram is claimed solved.\n''')
p.joinpath('STATUS.md').write_text('''STATE: DONE
NEXT: In a future attempt, prove -log Q_n=o_P(n^(1/3)) for an original-polymer tube of width n^(2/3+delta), and a KPZ limit for the corresponding capped model.
VERDICT: PARTIAL

2026-10-12: Fetched arXiv:2401.01757v4; confirmed Question 5 (p. 42) and Assumption 3 (p. 37). Corrected intake's stable-law wording and theorem-number description.
2026-10-12: Searched arXiv, Crossref, Semantic Scholar (including 30 citing works), OpenAlex and GitHub; no checked matching solution located. OpenAlex requests returned HTTP 429, so literature status is bounded by this access gap.
2026-10-12: Proved entropy-corrected single-site maximum is o(n^(1/3)) in L1 for alpha>5, deterministic-tube and full-cone truncation bounds, and conditional transfer using original-polymer confinement. Proved the distinct roles of thresholds 5 and 6. Corrected F0021-A001's false constant-cost argument.
2026-10-12: Exact finite computations passed; four Lean algebraic lemmas kernel-checked, exit 0. Full KPZ/Airy distribution and original-polymer confinement remain unproved. Current attempt concluded with complete proofs and explicit gaps in ATTEMPT.md.
''',encoding='utf-8')
assert p.joinpath('STATUS.md').read_text(encoding='utf-8').splitlines()[0]=='STATE: DONE'
for c in claims:
 assert set(c)=={'problem_id','claim','status','proof_location','remaining_gap','checks'}
 assert 'pending' not in c['checks']
print('Final records valid:',len(claims),'claim rows; STATE DONE; VERDICT PARTIAL; Lean exit 0.')
