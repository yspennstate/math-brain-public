import pathlib,json,hashlib,runpy,sys
R=pathlib.Path(__file__).resolve().parent
assert len(sys.argv)==2 and sys.argv[1]=='lean-exit-0', 'Run only after the expanded Lean command actually returns exit 0.'
lean=R/'AuxiliaryAlgebra.lean'
record={'date':'2026-10-11','command':'lake env lean '+str(lean).replace('\\','/'),
 'working_directory':'~/lean_verify','exit_code':0,'diagnostics':'No Lean diagnostics returned.',
 'sha256':hashlib.sha256(lean.read_bytes()).hexdigest(),'shared_queue_wait_seconds':124,
 'checked_lemmas':9,'scope':'Rational identities, strict sign certificates, trap parameter arithmetic, and tail-sign algebra only.'}
(R/'auxiliary_lean_expanded_result.json').write_text(json.dumps(record,indent=2),encoding='utf8')
for name in ['SECOND_CLAIMS.jsonl','CLAIMS.jsonl']:
 p=R/name; rows=[json.loads(x) for x in p.read_text(encoding='utf8').splitlines() if x.strip()]
 for x in rows:
  x['checks']=x['checks'].replace('Expanded Lean certificate pending.','Expanded nine-lemma Lean check passed with exit code 0; only finite algebra is formalized.')
 p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows),encoding='utf8')
runpy.run_path(str(R/'validate_second.py'),run_name='__main__')
runpy.run_path(str(R/'validate_artifacts.py'),run_name='__main__')
for name,text in [
 ('SECOND_ATTEMPT.md','\n## Final disposition\n\nThe two new routes were pursued through exact auxiliary-drift summation, whole-pair exit compensation, discounting, local acceleration, and finite-path reversal. Five additional auxiliary claims were saved. Exact rational checks passed, and both sequential Lean checks passed: the expanded current file contains nine kernel-checked finite algebraic lemmas. auxiliary_lean_expanded_result.json records the final input hash and scope. The probability and path-counting arguments are written proofs, not Lean formalizations.\n\nFinal verdict: **PARTIAL**. The original spatial repeated-visit gap is not closed. The explicit examples refute proposed proof premises, not the F0137 conjecture. No full proof or counterexample to (T)gamma/(T prime) is claimed.\n'),
 ('CHECKS.md','\nSecond-attempt final result: the expanded nine-lemma AuxiliaryAlgebra.lean check returned **exit code 0**, with no diagnostics, after a 124-second shared-slot wait. All exact rational certificates and eight reversal identities passed. Five new claim records were validated; the full claim ledger now has thirteen records. Only the finite algebraic lemmas are kernel-checked.\n'),
 ('ATTEMPT.md','\nSecond-attempt final status: **DONE / PARTIAL**. Five new auxiliary claims, exact computations, and nine Lean algebraic lemmas are recorded in SECOND_ATTEMPT.md, CLAIMS.jsonl, auxiliary_results.json, and auxiliary_lean_expanded_result.json. The global repeated-visit spatial estimate remains unproved.\n')]:
 p=R/name; p.write_text(p.read_text(encoding='utf8')+text,encoding='utf8')
p=R/'STATUS.md'; lines=p.read_text(encoding='utf8').splitlines()
lines[0]='STATE: DONE'
lines=[('NEXT: Future continuation: derive an aggregate slab-crossing bound from the exact reversal identity (S7); uniform auxiliary-drift and individual-path exponential-tilt reductions fail on the explicit examples.' if x.startswith('NEXT:') else x) for x in lines]
lines.append('2026-10-11 continuation complete: Both new approaches pursued and hostile-referee checks saved. Explicit A>1, kappa>1 Dirichlet obstructions to auxiliary drift and pair-exit positivity proved; discounting and holding-time changes do not repair the auxiliary sign. Exact reversal identity proved, with loop-heavy paths defeating uniform individual-path tilts. Nine finite algebraic Lean lemmas passed. Full (T prime)/(T gamma) remains unproved; final VERDICT: PARTIAL.')
p.write_text('\n'.join(lines)+'\n',encoding='utf8')
assert not any('pending' in x['checks'] for x in map(json.loads,(R/'CLAIMS.jsonl').read_text(encoding='utf8').splitlines()))
print('STATE: DONE; VERDICT: PARTIAL. All second-attempt records validated.')
