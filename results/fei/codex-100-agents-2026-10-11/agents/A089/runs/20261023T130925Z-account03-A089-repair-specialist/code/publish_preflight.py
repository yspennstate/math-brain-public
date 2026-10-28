"""Named-file scan and leased, byte-preserving GitHub package; no git commands."""
from pathlib import Path
import contextlib,hashlib,importlib.util,io,json,sys
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parents[1]
AGENT='codex-A089-stage10-save'
PREFIX='reports/fei-2026-10-11/runs/B18/'+ROOT.name
RESOURCE='file:math-open-problems/'+PREFIX
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
def call(m,args):
    out=io.StringIO()
    with contextlib.redirect_stdout(out),contextlib.redirect_stderr(out):rc=m.main(args)
    return rc,out.getvalue()
mesh=module('a089_mesh',r'~\<private-repo>\12_cognitive_architecture\agent_mesh\agent_mesh.py')
hello=call(mesh,['--json','hello','--agent',AGENT,'--runtime','codex','--task','Checkpoint completed A089 FEI stage10 only; no new worker','--cwd',str(BASE),'--ttl','20m'])
assert hello[0]==0,hello
claim=call(mesh,['--json','claim','--agent',AGENT,'--resource',RESOURCE,'--mode','write','--purpose','Append only this immutable A089 run via GitHub connector; open-problems master routing exception','--ttl','20m'])
if claim[0]:
    print(json.dumps({'status':'BLOCKED_MESH_CLAIM','rc':claim[0],'detail':claim[1]}));raise SystemExit(claim[0])
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:(ROOT/'out'/('ROLLING_'+name)).write_bytes((BASE/name).read_bytes())
scanner=module('a089_scanner',r'scan_secrets.py')
paths=sorted(p for p in ROOT.rglob('*') if p.is_file())
scanned=call(scanner,[str(p) for p in paths])
pre={'status':'PASS' if scanned[0]==0 else 'BLOCKED_SECRET_SCAN','mesh_agent':AGENT,'mesh_resource':RESOURCE,'mesh_claim':claim[1],'secret_scan_exit':scanned[0],'secret_scan_output':scanned[1],'scan_mode':'Explicit named text files; REPO_ROUTING.md open-problem exception to range scan; GitHub connector uses no local git.','repository':'yspennstate/math-open-problems','branch':'master','branch_authority':'REPO_ROUTING.md Open-problem solving work explicitly master (not main)','remote_prefix':PREFIX}
(ROOT/'out/PUBLISH_PREFLIGHT.json').write_text(json.dumps(pre,indent=2)+'\n',encoding='utf-8',newline='\n')
if scanned[0]:print(json.dumps(pre));raise SystemExit(scanned[0])
# Include the preflight receipt itself in a second named-file scan.
finalscan=call(scanner,[str(ROOT/'out/PUBLISH_PREFLIGHT.json')]);assert finalscan[0]==0,finalscan
receipt=json.loads((ROOT/'out/PERSISTENCE.json').read_text(encoding='utf-8'))
paths=sorted(p for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json')
receipt['files']=[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths]
receipt['publish_preflight']='named files clean; exact remote branch lease still required'
(ROOT/'out/PERSISTENCE.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
assert call(scanner,[str(ROOT/'out/PERSISTENCE.json')])[0]==0
files=sorted(p for p in ROOT.rglob('*') if p.is_file())
assert all(p.stat().st_size<20*1024*1024 for p in files)
elements=[];manifest=[]
for p in files:
    b=p.read_bytes();rel=p.relative_to(ROOT).as_posix();target=PREFIX+'/'+rel
    elements.append({'path':target,'mode':'100644','type':'blob','content':b.decode('utf-8')})
    manifest.append({'path':target,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'git_blob_sha1':hashlib.sha1(('blob '+str(len(b))+'\0').encode('ascii')+b).hexdigest()})
print(json.dumps({'status':'PASS','repository':pre['repository'],'branch':'master','prefix':PREFIX,'mesh_agent':AGENT,'mesh_resource':RESOURCE,'tree_elements':elements,'manifest':manifest}))
