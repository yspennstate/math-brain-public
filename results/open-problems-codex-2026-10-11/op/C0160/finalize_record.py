from pathlib import Path
import json
R=Path(__file__).parent
assert (R/'lean_check.txt').exists(), 'Record actual Lean outcome first.'
raw=(R/'lean_check.txt').read_bytes()
# Windows PowerShell 5 Tee-Object may use UTF-16LE, while the explicit
# Add-Content exit marker uses UTF-8. Normalize only after the command finishes.
if raw.startswith(b'\xff\xfe'):
 marker=raw.rfind(b'Exit code: ')
 if marker>=0:
  log=raw[:marker].decode('utf-16',errors='replace')+raw[marker:].decode('utf-8-sig',errors='replace')
 else:
  log=raw.decode('utf-16')
else:
 log=raw.decode('utf-8-sig')
(R/'lean_check.txt').write_text(log,encoding='utf-8')
assert 'Exit code: 0' in log, 'Do not claim verification without successful Lean exit.'
p=R/'ATTEMPT.md'
t=p.read_text(encoding='utf-8').replace('Check outcome will be recorded after the shared Lean slot runs.', 'Lean completed successfully with exit code 0; see lean_check.txt. No sorry, native_decide, custom axioms or unchecked percolation assumptions occur in the formal file. The check proves only the stated order lemmas, not the published percolation theorems.')
p.write_text(t,encoding='utf-8')
p=R/'CLAIMS.jsonl'; rows=[json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x]
rows[0]['checks']=rows[0]['checks'].replace('Lean order step pending.', 'Lean endpoint-order lemmas checked with exit code 0; percolation inputs checked against primary survey. Open p_2 endpoint handled by q=(p_2+1)/2, not membership at p_2.')
rows[2]['remaining_gap']='None; written proof complete and endpoint-order lemmas kernel checked.'
rows[2]['checks']='Greatest-lower-bound argument written in full; endpoint=1 handled separately. Endpoint.lean passed lake env lean, exit 0, without sorry/native_decide; percolation is not formalized.'
p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows),encoding='utf-8')
(R/'STATUS.md').write_text('STATE: DONE\nNEXT: None; literal closed-interval assertion refuted and intended uniqueness monotonicity identified precisely in the literature.\nVERDICT: SOLVED\n2026-10-11: Source recovered from arXiv math/0612812v1. Theorem 5.6 (printed p.307) proves no-switching without unimodularity. Section 3 already covers quasi-transitive graphs.\n2026-10-11: Complete counterexample deduction: G=T_6 x Z is degree 9 and transitive, p_c<p_u<1, N(p_u)=infinity a.s., hence U=(p_u,1]. Uses verified Theorems 3.2, 5.6, 9.2. This is a correction/deduction from established results, not a new percolation theorem.\n2026-10-11: Required five-service literature searches recorded, including successful recent arXiv and Semantic Scholar citations retries; OpenAlex remained inaccessible.\n2026-10-11: Endpoint.lean successfully kernel checked (exit 0); written proof and claim records audited. No remaining gap for the literal question.\n',encoding='utf-8')
print('Final records: STATE DONE, VERDICT SOLVED',flush=True)
with (R/'STATUS.md').open('a',encoding='utf-8') as f:
 f.write('2026-10-11: Further hostile review corrected the draft misuse of p_2: the final proof uses the midpoint q=(p_2+1)/2 in (p_2,1), never assumes uniqueness at p_2.\n')
 f.write('2026-10-12 (Asia/Jerusalem): Verification completed on continuation with the smaller linear-order formalization, importing only Mathlib.Order.Bounds.Basic. The earlier interrupted run had an unknown exit status and was not counted.\n')
