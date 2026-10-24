import pathlib,json
root=pathlib.Path('.')
claims=[json.loads(l) for l in (root/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert len(claims)==9
assert all(c['problem_id']=='P0315' for c in claims)
assert 'exit_code=0' in (root/'lean_check.txt').read_text(encoding='utf8')
lean=(root/'Coefficient.lean').read_text(encoding='utf8')
assert 'sorry' not in lean and 'native_decide' not in lean
checks=json.loads((root/'checks.json').read_text(encoding='utf8'))
assert len(checks['beta4_remainders'])==8 and len(checks['beta1_remainders'])==7
assert all(mpval['fraction_of_bound'] and float(mpval['fraction_of_bound'])<=1 for mpval in checks['beta4_remainders'])
assert all(float(v['fraction_of_beta1_bound'])<=1 for v in checks['beta1_remainders'])
status='''STATE: DONE
NEXT: To advance the open problem, prove a weighted asymptotic decomposition of the SDE-selected infinite moment hierarchy, including mode amplitudes and summable pointwise remainders.
VERDICT: PARTIAL
2026-10-11: Fetched Dumaz-Malvy and verified the fixed-beta continuous pair-density target and density conventions.
2026-10-11: Queried arXiv, Crossref, OpenAlex, Semantic Scholar, and GitHub; OpenAlex and Semantic Scholar remained HTTP 429. No full solution verified; literature search coverage is incomplete.
2026-10-11: Checked Qu-Valko Theorem 3: it is a pointwise upper bound, not exact leading asymptotics. Found July 2026 beta=6 expansion and October 2026 tail-triviality paper; neither solves general beta.
2026-10-11: Proved density rescaling, beta=2 exact formula, beta=1 and beta=4 explicit remainder expansions, formal nonoscillatory coefficient recurrence, necessary formal harmonic exponents, and weighted Fourier tail bound.
2026-10-11: Identified a missing beta=1 sine descendant in Lewin (148) and insufficient literal truncation in (149); neither is a counterexample to the intended full family.
2026-10-11: Fifteen high-precision classical remainder checks passed. Finite coefficient cancellation passed Lean 4 with exit code 0; no sorry or native_decide.
2026-10-11: Attempt concluded with precise general-beta analytic gap in ATTEMPT.md. No complete proof or counterexample to P0315 claimed.
'''
(root/'STATUS.md').write_text(status,encoding='utf8')
print('Final audit passed. STATUS: DONE / PARTIAL. Required records present.')
print('\n'.join(p.name for p in root.iterdir() if p.name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','Coefficient.lean','lean_check.txt','checks.json']))
