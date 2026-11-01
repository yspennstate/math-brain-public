from pathlib import Path
import json
lean=Path('tensor_lean_check.txt').read_text(encoding='utf8');assert lean.startswith('exit_code=0')
checks={name:json.loads(Path(name).read_text(encoding='utf8')) for name in ['tensor_checks.json','global_classification_checks.json','inhomogeneous_checks.json','babp_positive_control.json','midpoint_checks.json']}
assert all(x['status']=='PASS' for x in checks.values())
with Path('FOLLOWUP.md').open('a',encoding='utf8') as f:
 f.write('''
## Final verification and verdict

From ~/lean_verify ran `lake env lean ~/brain_workers/TRIO_1011/op/D0027/TensorObstruction.lean`, with a 3600-second timeout. It passed with exit code 0, elapsed 2317.851 seconds including shared-machine waiting. The file imports only Mathlib.Data.Real.Basic, Mathlib.Tactic.Linarith and Mathlib.Tactic.Ring. Its five auxiliary theorems are kernel checked; the rational instance uses decide +kernel. There is no sorry and no native_decide. Output: tensor_lean_check.txt. This is a check of the finite algebraic core, not a Lean formalization of the full classifications or stochastic martingale theorem.

Exact checks passed: 792 local tensor candidates; 24 parity-harmonic full five-cycle candidates; 18 site-dependent candidates with two full matrix similarities; three BABP positive controls; and 381 midpoint-generator cases. The global homogeneous grid passed 225 cases before its job budget and remains explicitly non-exhaustive. The all-parameter statements rely on the complete written proofs.

Verdict: PARTIAL. This additional attempt supplies a complete homogeneous tensor-Markov representation classification, a site-dependent parity no-go theorem and transpose-duality corollary, a checked failure of domain-wall lumping, and a compensated-midpoint concentration bound. No proof or counterexample to Conjecture 2 was found. The original uniform deterministic local-forgetting estimate remains unproved. For the geometric alternative, control of the edge-imbalance compensator and quantitative bilateral invasion/interior forgetting remain missing. Two new approaches were recorded and the more promising tensor route was pursued to its explicit obstruction; no claim of bibliographic novelty is made.
''')
rows=[json.loads(x) for x in Path('CLAIMS.jsonl').read_text(encoding='utf8').splitlines()]
for r in rows:
 r['checks']=r['checks'].replace('Lean finite algebra check pending.','Five Lean auxiliary algebra lemmas passed the kernel check, exit 0.').replace('Lean finite algebra checks pending.','Five Lean auxiliary algebra lemmas passed the kernel check, exit 0.')
assert len(rows)==16
assert all('pending' not in r['checks'].lower() and 'running' not in r['checks'].lower() for r in rows)
assert all(r['status'] in ['proved','counterexample','proved_special_case','numerical_evidence','conjecture'] for r in rows)
Path('CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf8')
with Path('ATTEMPT.md').open('a',encoding='utf8') as f:f.write('\nFinal follow-up verification: TensorObstruction.lean passed the kernel check, exit 0 (2317.851 seconds on the shared machine). FOLLOWUP.md contains the complete statements, proofs, hostile-referee audit, computational outcomes and remaining gaps. The follow-up verdict is PARTIAL; the full conjecture remains undecided by this work.\n')
p=Path('STATUS.md');s=p.read_text(encoding='utf8');s=s.replace('STATE: WORKING','STATE: DONE',1);s=s.replace(s.splitlines()[1],'NEXT: Prove uniform deterministic local forgetting; possible future routes require a non-tensor/block representation or concentration of the edge-imbalance compensator plus interior forgetting. Current additional attempt is complete.');s+='2026-10-11: Final additional-attempt audit completed. Five auxiliary algebra lemmas passed Lean kernel verification (exit 0, 2317.851 seconds). All completed exact checks passed; the time-limited global grid is explicitly non-exhaustive. Saved two approaches, full representation-obstruction proofs and the midpoint martingale reduction in FOLLOWUP.md. STATE: DONE; VERDICT: PARTIAL. No full proof or counterexample to D0027 was obtained.\n';p.write_text(s,encoding='utf8')
assert p.read_text(encoding='utf8').splitlines()[0]=='STATE: DONE'
print('STATE: DONE; VERDICT: PARTIAL; claims',len(rows),'Lean exit 0',flush=True)
