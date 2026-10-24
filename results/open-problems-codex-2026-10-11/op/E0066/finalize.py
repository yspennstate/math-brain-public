import pathlib,json
p=pathlib.Path('.')
log=p.joinpath('lean_check.log').read_text(encoding='utf8');assert 'EXIT_CODE: 0' in log
with p.joinpath('ATTEMPT.md').open('a',encoding='utf8') as f:f.write('''

Lean verification completed successfully: `lake env lean ~/brain_workers/TRIO_1011/op/E0066/PeriodBound.lean`, invoked from ~/lean_verify with a 3600-second subprocess timeout. Exit code 0. The file imports only Mathlib.Data.Fintype.Perm and uses `decide +kernel` for both finite statements. Reported axioms: propext, Classical.choice, Quot.sound. No sorry, no native_decide. The initial UTF-8 BOM parse failure is preserved in lean_check_initial.log; the BOM was removed and the successful rerun is in lean_check.log. Only the finite permutation-order statements are kernel checked; the analytic and support-rigidity proofs are written mathematical proofs.

Final referee conclusion: the proofs above survive the listed checks. The bounded literature search does not establish novelty or complete resolution of the source programme. STATE: DONE means this attempt is finished with its gap explicitly recorded; VERDICT remains PARTIAL.
''')
rows=[json.loads(l) for l in p.joinpath('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
for c in rows:
 if 'For m=3' in c['claim']:c['checks']='Full proof in ATTEMPT.md; Fin 3 permutation order disjunction kernel checked by decide +kernel in PeriodBound.lean, exit 0, lean_check.log. Full analytic theorem not formalised.'
 if c['checks']=='Full proof and boundary audit in ATTEMPT.md; further checks pending.':c['checks']='Full written proof and hostile-referee checks in ATTEMPT.md; exact rational permutation and boundary controls in experiments.py.'
p.joinpath('CLAIMS.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in rows),encoding='utf8')
p.joinpath('STATUS.md').write_text('''STATE: DONE
NEXT: For a future attempt, classify cycles with repeated positive coordinate values in m>=4, or prove or refute that every such cycle is induced by one fixed coordinate permutation; first check the inaccessible older dynamics papers.
VERDICT: PARTIAL

2026-10-12: Verified Ganikhodzhaev–Rozikov arXiv:0902.4207, Problem 13, PDF p. 8, with full-simplex QSO and majorisation hypotheses. Queried arXiv, OpenAlex including source/survey citations, Crossref, Semantic Scholar (429 twice), and GitHub (no repositories). Makhmudov 2021 records substantial known trajectory structure; no exact-scope source-wide solution certificate found.
2026-10-12: Wrote complete proofs of general asymptotic periodicity, interior rigidity, its extension to boundary cycles with distinct positive coordinates, the sharp three-type period bound 3, and the complete two-type coefficient/trajectory classification. No novelty asserted.
2026-10-12: Hostile-referee audit and exact boundary controls complete. Sixty face-rigidity LP checks in dimensions 2–6 passed (worst discrepancy 1.49e-14); 48 sampled repeated-coordinate long-cycle LPs were infeasible (numerical evidence only).
2026-10-12: Lean finite permutation steps for Fin 2 and Fin 3 passed, exit code 0, using decide +kernel and one narrow Mathlib import. The full analytic proof is not formalised. Final gap: higher-dimensional repeated-positive-coordinate cycles and a full trajectory/basin classification remain unresolved by this attempt. DONE records completion of the bounded partial attempt, not solution of the programme.
''',encoding='utf8')
for name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','PeriodBound.lean']:
 assert p.joinpath(name).exists() and p.joinpath(name).stat().st_size>0
assert p.joinpath('STATUS.md').read_text(encoding='utf8').splitlines()[0]=='STATE: DONE'
assert 'sorry' not in p.joinpath('PeriodBound.lean').read_text(encoding='utf8')
print('STATE: DONE; VERDICT: PARTIAL. Required files saved and validated. Lean exit 0.')
