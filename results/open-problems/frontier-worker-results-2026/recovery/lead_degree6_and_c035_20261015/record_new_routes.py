from pathlib import Path
from datetime import datetime
import json,hashlib,subprocess
H=Path(__file__).resolve().parent;B=Path('~/brain-repo')
PY='C:/Python314/python.exe';M=B/'12_cognitive_architecture/agent_mesh/agent_mesh.py';A='codex-term-362ebe34'
def mesh(verb,p,extra=[]):
 r=subprocess.run([PY,str(M),verb,'--agent',A,'--resource',str(p),*extra],capture_output=True,text=True,encoding='utf-8');assert r.returncode==0,r.stderr
rows=[('T170','Exact unary-hypercube horizontal boundary rates improve finite Dhar certificate to dimension16','T170-LEAD-D16-001_v1.md','live','Own exact finite proof/arithmetic complete, frozen candidate4bf76e; two independent exact-content audits pending; no admission.'),('T170','Rolling count-window controlled infection with finite Poisson bias inequalities and canonical regeneration','T170_ROLLING_WINDOW_ROUTE.md','live','New physical comparison proposed; independent cap1/cap2 finite controls pass. d15 caps32/64/128 miss comparison, cap256 follows measured left-cap bottleneck. Finite inequalities do not establish physical coupling.'),('T186','Coordinate-coalesced monotone proposal closure with distinct-input collision flags','T186_COORDINATE_COALESCED_CLOSURE.md','live','Finite exhaustive/random controls pass and lower-subsolution proof proposed; no exact all-token containment, conditional sampler or sparse collision transfer. Existing author critique pending.')]
records=[]
for row,route,note,status,why in rows:
 p=B/f'06_math_research/frontier/rows/{row}/routes.jsonl'
 mesh('claim',p,['--mode','write','--ttl','1800','--purpose','Record new routes and measured barriers to prevent duplicate work'])
 old=p.read_bytes() if p.exists() else b''
 if route.encode() in old:continue
 assert not old or old.endswith(b'\n')
 r={'at':datetime.now().astimezone().isoformat(),'by':A,'row':row,'route':route,'status':status,'why':why,'evidence':str(H/note),'evidence_sha256':hashlib.sha256((H/note).read_bytes()).hexdigest()}
 mesh('assert',p);p.write_bytes(old+(json.dumps(r)+'\n').encode());records.append(r)
 with (H/'ROUTES.jsonl').open('ab') as f:f.write((json.dumps(r)+'\n').encode())
(H/'NEW_ROUTES_RECORD.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
store=B/'12_cognitive_architecture/task_checklist'
mesh('claim',store,['--mode','write','--ttl','600','--purpose','Update authorized frontier lead checklist progress'])
message='17:4x recovery: cutoff91 Potts admitted after two actual distinct-account full audits, archivee0a5fea verified; dimension17 FPP admitted archivecd6226. New exactd16 candidate4bf76e (margin.000885609), archive90326a verified, existingw683/account4 and5a8/account3 audits pending. T186 finite empty/positive ranges recorded; exact onset open. New rolling-window physical method proposed, finite controls pass; no further theorem claim. Continue until19:25, no newagents.'
for item in ['T-20261014-145','T-20261015-197']:
 mesh('assert',store)
 r=subprocess.run([PY,'~/.claude/dreaming/task_checklist_hook.py','note',item,message,'--by',A,'--runtime','headless'],capture_output=True,text=True,encoding='utf-8');assert r.returncode==0,r.stderr
 print(item,r.stdout[:150])
print('Recorded',len(records),'routes; checklists current')
