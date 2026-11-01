from pathlib import Path
import json
p=Path(__file__).resolve().parent
s=(p/'STATUS.md').read_text(encoding='utf-8')
s=s.replace('STATE: WORKING','STATE: DONE').replace('NEXT: Obtain the queued Lean arithmetic check result, then finalize DONE/SOLVED records.','NEXT: None for the general question; suggested scl test case remains separate.')
line='2026-10-11: Lean ExponentCheck.lean completed with exit code 0, no diagnostics; arithmetic lemmas kernel-checked. Complete counterexample proof, finite checks, literature ledger and claims saved. DONE/SOLVED.\n'
if line not in s:s+=line
(p/'STATUS.md').write_text(s,encoding='utf-8')
a=(p/'ATTEMPT.md').read_text(encoding='utf-8').replace('A follow-up author query is pending.','A follow-up author query likewise returned off-topic cards.')
(p/'ATTEMPT.md').write_text(a,encoding='utf-8')
claims=[json.loads(x) for x in (p/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()]
assert s.splitlines()[0]=='STATE: DONE' and 'VERDICT: SOLVED' in s
assert len(claims)==4
for name in ['STATUS.md','LITERATURE.md','ATTEMPT.md','CLAIMS.jsonl','finite_checks.json','ExponentCheck.lean','lean_check.txt']:assert (p/name).is_file()
print(s,flush=True)
print('Four claims parsed; all required records present.',flush=True)
