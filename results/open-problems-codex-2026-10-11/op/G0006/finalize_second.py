from pathlib import Path
import json
root=Path.cwd()
checks=(root/'second_lean_check.txt').read_text(encoding='utf8');assert 'Exit: 0' in checks
p=root/'SECOND_ATTEMPT.md';s=p.read_text(encoding='utf8')
s=s.replace('# G0006 — second serious attempt (2026-10-11)','# G0006 — second serious attempt (2026-10-11)\n\nFinal outcome: PARTIAL. The original all-dimensional gap remains unproved. Theorem 8 gives a complete finite-certificate characterization in d=2; no critical-rate certificate is established.')
s+='\n\nFinal verification: SecondChecks.lean passed all five theorems, Lean 4.33.1 exit 0 in 169.162 seconds. The human probabilistic proofs are not Lean formalizations. Exact rational, finite-generator numerical and Monte Carlo results have distinct statuses in CLAIMS.jsonl.\n'
p.write_text(s,encoding='utf8')
p=root/'CLAIMS.jsonl';claims=[json.loads(x) for x in p.read_text(encoding='utf8').splitlines()]
assert len(claims)==16,len(claims)
for c in claims:
 if 'SecondChecks.lean' in c.get('proof_location',''):
  c['checks']=c['checks'].replace('Lean check result recorded separately.','Lean 4.33.1 checked normalization, positivity, eight rational generator balances, joint probability and threshold: exit 0, second_lean_check.txt.')
p.write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in claims),encoding='utf8')
for fn in ['ATTEMPT.md','LITERATURE.md','SECOND_ATTEMPT.md','CLAIMS.jsonl','SecondChecks.lean','second_lean_check.txt','wired_results.json','wired_mc_results.json','directed_chain_result.json','second_exact_checks.json']:
 assert (root/fn).is_file(),fn
assert all(c['problem_id']=='G0006' and c['status'] in {'proved','counterexample','proved_special_case','numerical_evidence','conjecture'} for c in claims)
assert any(c['status']=='conjecture' and 'lambda_p' in c['claim'] for c in claims)
lean=(root/'SecondChecks.lean').read_text(encoding='utf8')
assert 'sorry' not in lean and 'native_decide' not in lean and 'import Mathlib\n' not in lean
assert len(json.loads((root/'wired_mc_results.json').read_text(encoding='utf8')))==12
assert json.loads((root/'second_exact_checks.json').read_text(encoding='utf8'))['subcritical_certificate']['passes']
assert 'Proposition 10' in (root/'SECOND_ATTEMPT.md').read_text(encoding='utf8')
assert 'Second attempt' in (root/'LITERATURE.md').read_text(encoding='utf8')
status='''STATE: DONE
NEXT: Prove existence of a buffered finite-box crossing certificate at lambda_c (equivalent to the gap in d=2), or develop a different upper connectivity estimate in the survival regime.
VERDICT: PARTIAL

2026-10-11: First attempt verified the source and found no exact literature solution, with documented coverage gaps. Established elementary bounds and a barrier to its singleton-exit criterion.
2026-10-11: Reopened for the user-requested serious second attempt. Queried the brain on the connectivity gap, near-critical decoupling and named neighboring results. Recorded two new approaches: buffered finite stationary boxes and cluster split/merge stationarity.
2026-10-11: Proved a finite-box crossing certificate for every d>=2. Using verified van den Berg theorems, proved in d=2 that the strict gap is equivalent to existence of an L with b_L(lambda_c)<3^(-25). This is a reduction, not a proof of that existence.
2026-10-11: Proved a passing subcritical certificate at d=2, lambda=1/8, L=25 and an exact restricted-chain lower bound ruling out buffered L=1 throughout the survival regime. Larger-scale exact-CTMC numerical experiments supplied no certified critical crossing bound. Proved a finite cluster split-and-merge stationary identity for the other approach.
2026-10-11: SecondChecks.lean passed all five finite checks, exit 0, including the eight chain generator balances. Full proofs, referee audit and precise remaining gap are in SECOND_ATTEMPT.md and linked from ATTEMPT.md. All 16 claim records validated. Original requested inequality remains unproved; bounded second attempt closed honestly as PARTIAL.
'''
(root/'STATUS.md').write_text(status,encoding='utf8')
(root/'second_record_checks.txt').write_text('Required files present; 16 valid claim records; original target remains conjecture; five second Lean checks passed; exact subcritical certificate arithmetic passed; 12 numerical experiment entries. Human proof scope and literature hypotheses reviewed.\n',encoding='utf8')
print(status)
