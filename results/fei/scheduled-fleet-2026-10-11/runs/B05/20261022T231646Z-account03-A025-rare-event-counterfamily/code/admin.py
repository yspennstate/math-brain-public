from pathlib import Path
import json,hashlib,subprocess,sys,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]; B=Path('~'); T=B/'brain_workers/FEI100_20261011'
def js(name,v): (R/'out'/name).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8',newline='')
files=[]
for rel in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:
    files.append(B/'mop_fei100/reports/fei-2026-10-11'/rel)
push=B/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
files += [push/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((push/'sources').glob('*.md'))+list((push/'sources').glob('*.txt'))+list((T/'context').glob('*.txt'))
files += [B/'AGENTS.md',T/'BOARD.md',T/'claude/B05/STREAM_NOTES.md']
files += list((A/'runs').glob('*/REPORT.md'))
q=T/'agents/A021/runs/20261021T184331Z-account03-A021-rare-core-asymptotics'
files += [q/n for n in ['REPORT.md','PROOF.md','OBSTRUCTION.md','CLAIMS.json']]
q=T/'agents/A021/runs/20261014T075029Z-account05-A021-rare-core-asymptotics'
files += [q/n for n in ['REPORT.md','DERIVATION.md','CLAIMS.json']]
files += list((T/'claude/B05/runs').glob('*/REPORT.md'))
files += list((B/'mop_fei100/reports/fei-2026-10-11/runs/B05').glob('*/REPORT.md'))
inv=[]
for f in files:
    raw=f.read_bytes()
    try:s=raw.decode('utf-8-sig');encoding='utf-8-sig'
    except UnicodeDecodeError:s=raw.decode('cp1252');encoding='cp1252 (actual source bytes)'
    hits=[{'line':i+1,'text':l[:180]} for i,l in enumerate(s.splitlines()) if any(k in l for k in ['A025','C019','C024','ancestor','owner','all-cut','shared-data','Proposition 8.9'])]
    inv.append({'path':str(f),'sha256':hashlib.sha256(raw).hexdigest(),'encoding':encoding,'bytes':len(raw),'locators':hits[:15]})
js('SOURCE_RECEIPTS.json',inv)
(A/'STATUS.md').write_text('STATE: A025 stage7 in progress: all-mixed-cut ancestor identity proved; 29160 node/75816 edge production census and361942 exact assertions PASS; independent replay pending; FEI OPEN.\nNEXT: Finish independent DFT replay and all-cut source receipts, preserve A021 final-owner obstruction, save protocol artifacts.\n',encoding='utf-8',newline='')
replay=subprocess.run([sys.executable,'-X','utf8',str(R/'code/replay.py')],capture_output=True,text=True,encoding='utf-8')
js('REPLAY_COMMAND.json',{'returncode':replay.returncode,'stdout':replay.stdout,'stderr':replay.stderr})
print('REPLAY',replay.returncode,replay.stdout[:500],flush=True)
assert replay.returncode==0
mem=subprocess.run([sys.executable,'-X','utf8',str(T/'tools/memok.py')],capture_output=True,text=True,encoding='utf-8')
js('MEMOK.json',{'returncode':mem.returncode,'stdout':mem.stdout,'stderr':mem.stderr})
stmt='example (s e p q l r : Int) (h : s+e = s+2*p+10*q-l+r) : s+e+l-r = s+2*p+10*q := by omega'
(R/'code/Transport.lean').write_text(stmt+'\n',encoding='utf-8',newline='')
if mem.returncode==0:
    lean=subprocess.run([sys.executable,'-X','utf8',str(B/'.claude/dreaming/lean_check.py'),'--core','--stmt',stmt],capture_output=True,text=True,encoding='utf-8')
    js('LEAN.json',{'returncode':lean.returncode,'stdout':lean.stdout,'stderr':lean.stderr,'statement':stmt,'scope':'Int algebra only; Fourier proof not formalized','formal_target_verified':False,'note':'No formal certification asserted without trusted compiler/source/axiom audit'})
    print('LEAN',lean.returncode,lean.stdout[:1500],flush=True)
else:
    js('LEAN.json',{'status':'HELD_FRESH_ADMISSION_FAILED','memok_returncode':mem.returncode,'statement':stmt,'formal_target_verified':False,'scope':'Int algebra only; no compiler started'})
    print('LEAN_HELD_MEMOK',mem.returncode,flush=True)
print(json.dumps({'source_files':len(inv),'administration':'saved inside A025 only, except mandatory helper state'}),flush=True)
