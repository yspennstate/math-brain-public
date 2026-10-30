from pathlib import Path
import json,hashlib,runpy
R=Path(__file__).resolve().parent.parent; A=R.parent.parent
old='achieve a nonconstant prescribed nonempty profile change '
new='achieve a prescribed nonempty profile change, proper only if E(1-a^2)>0, '
p=R/'CLAIMS.json'; cs=json.loads(p.read_text(encoding='utf-8'))
c=next(c for c in cs if c['claim_id'].startswith('A031-SHARP'))
assert old in c['exact_statement']
c['exact_statement']=c['exact_statement'].replace(old,new)
c['statement_sha256']=hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
p.write_text(json.dumps(cs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=R/'code/package_stage.py';p.write_text(p.read_text(encoding='utf-8').replace(old,new),encoding='utf-8')
p=R/'DERIVATION.md'; s=p.read_text(encoding='utf-8')
s=s.replace('every minimizing ghost tilt saturates at','every minimizing ghost tilt with q_S>0 saturates at')
s=s.replace('new source or per-query bank is introduced. The proof', 'new source or per-query bank is introduced. Proper profile change requires beta>0; inactive controllers have unchanged references and zero cost. The proof')
p.write_text(s,encoding='utf-8')
p=R/'REPORT.md'; s=p.read_text(encoding='utf-8')
s=s.replace('The proof extends to every coherent controller', 'The profile change is proper for active controllers beta>0; inactive beta=0 controllers have unchanged references and zero cost. The proof extends to every coherent controller')
s=s.replace('out/MANIFEST.json records artifact hashes;', 'A packaging receipt-name mismatch was corrected before final save; the initial hash audit detected live BOARD updates, recorded explicitly in out/LIVE_SOURCE_CHANGES.json, with mathematical source hashes unchanged. out/MANIFEST.json records artifact hashes;')
p.write_text(s,encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write('\nStage20 final audit: agent-root cwd attempts failed before inputs; corrected explicit run cwd. Packaging initially expected REPRODUCE_GHOST.json instead of actual GHOST_REPRODUCE.json; corrected before save. Source hash audit detected only live BOARD drift, explicitly recorded. Final scope wording patch initially did not match the generator source; no change made by that failed patch. Tightened controller statement: proper profile change requires beta>0; all162 existing fixtures include inactive cases. Saturation asserted only on q>0 ghost cells. No new mathematical computation needed.\n')
st=(A/'STATUS.md').read_text(encoding='utf-8').splitlines()
st[1]+=' Cwd/receipt-name failures corrected; live BOARD drift isolated in readback.'
(A/'STATUS.md').write_text('\n'.join(st)+'\n',encoding='utf-8')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write('\nStage20 scope refinement: every controller has zero CE conversion, but the changed profile is proper only for active beta=E(1-a^2)>0; inactive controllers remain unchanged. Saturated ghost tilts are asserted only on positive-reference-mass cells.\n')
runpy.run_path(str(R/'code/readback.py'),run_name='__main__')
