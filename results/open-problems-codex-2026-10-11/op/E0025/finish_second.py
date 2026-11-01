import pathlib,json
p=pathlib.Path(__file__).resolve().parent
lean=(p/'second_lean_check.txt').read_text(encoding='utf8')
assert lean.startswith('exit_code=0\n'), 'Second Lean check not yet passed'
src=(p/'SecondMargins.lean').read_text(encoding='utf8')
assert 'sorry' not in src and 'native_decide' not in src
checks=json.loads((p/'second_checks.json').read_text(encoding='utf8'))
assert len(checks['parameter_checks'])==15
proof=(p/'SECOND_ATTEMPT.md').read_text(encoding='utf8')
if '## Second Lean verification' not in proof:
 with (p/'SECOND_ATTEMPT.md').open('a',encoding='utf8') as f:
  f.write('\n## Second Lean verification\n\nSecondMargins.lean passed lake env lean from ~/lean_verify, with no sorry or native_decide (see second_lean_check.txt). It kernel-checks the general algebraic implication from K>K_crit to existence of p<q in the admissible exponent interval, and five exact rational margin checks. The analytic theorems and path-singularity argument are not formalized.\n')
new=[
 {'claim':'For full density pulses with exact recursion r_(n+1)=r_n^K, 1<K<=Kcrit, the moment criterion fails for every possible cutoff and endpoint sequence with the fixed alpha base.',
  'status':'proved','proof_location':'SECOND_ATTEMPT.md, Stronger boundary obstruction',
  'remaining_gap':'This is a counterexample to applicability of the criterion, not to Hunt hypothesis.',
  'checks':'Uniform lower bound M(h)^((1-alpha)/alpha)L(h)>=c by a three-case cutoff split; contradiction to wide-band assumptions.'},
 {'claim':'The general admissible exponent interval and rational example margins in Theorem B are Lean-checked.',
  'status':'proved','proof_location':'SecondMargins.lean; second_lean_check.txt',
  'remaining_gap':'Full analytic and probabilistic arguments are not formalized.',
  'checks':'lake env lean exit 0; no sorry; no native_decide.'},
 {'claim':'Second-attempt checks validate 15 exact parameter choices, six finite atomic-obstruction cases, and three numerical Poisson-affinity sums.',
  'status':'numerical_evidence','proof_location':'second_checks.py; second_checks.json',
  'remaining_gap':'Only the rational cases are exact; finite checks do not substitute for universal analytic proofs.',
  'checks':'Fraction arithmetic for parameter/atomic cases; 80-digit affinity sums with relative errors below 1e-70.'}
]
existing={json.loads(x)['claim'] for x in (p/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()}
with (p/'CLAIMS.jsonl').open('a',encoding='utf8') as f:
 for c in new:
  if c['claim'] not in existing: f.write(json.dumps({'problem_id':'E0025',**c})+'\n')
status=(p/'STATUS.md').read_text(encoding='utf8').replace('STATE: WORKING','STATE: DONE',1)
status=status.replace(next(x for x in status.splitlines() if x.startswith('NEXT:')),
 'NEXT: General case unresolved; a further advance must control bad frequencies beyond moment separation or use a different potential-theoretic method.')
status+='''
2026-10-12: Further sharpened the boundary: full-pulse type-(alpha,beta) measures with 1<K<=Kcrit cannot meet the moment criterion at any cutoff, not just between pulses. This does not disprove (H).
2026-10-12: Exact rational and supplementary Poisson-affinity computations passed. Second Lean check passed for general exponent selection and rational margins; no full analytic formalization.
2026-10-12: Second requested serious attempt closed STATE: DONE, VERDICT: PARTIAL. Stronger theorems and method obstructions saved; both universal questions remain unresolved.
'''
(p/'STATUS.md').write_text(status,encoding='utf8')
assert (p/'STATUS.md').read_bytes().splitlines()[0]==b'STATE: DONE'
assert 'VERDICT: PARTIAL' in status
claims=[json.loads(x) for x in (p/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
assert all(x['problem_id']=='E0025' for x in claims)
print('Final second-attempt audit passed. STATE: DONE; VERDICT: PARTIAL; claims:',len(claims))
