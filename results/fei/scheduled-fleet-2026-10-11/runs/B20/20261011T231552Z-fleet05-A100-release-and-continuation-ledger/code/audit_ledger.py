from pathlib import Path
import json, hashlib, re, time
from datetime import datetime, timezone

BASE=Path(r'~\brain_workers\FEI100_20261011')
CAN=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
RUN=Path(__file__).resolve().parents[1]
OUT=RUN/'out'; OUT.mkdir(exist_ok=True)
def dump(n,x): (OUT/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def read(p): return p.read_text(encoding='utf-8-sig')
def sha(b): return hashlib.sha256(b).hexdigest()
manifest=[]; contents={}
paths=[CAN/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex','PUBLICATION_RECEIPTS.json','MANIFEST.json']]
paths += list((CAN/'runs').rglob('*'))+list((CAN/'verification').rglob('*'))
paths += [SUP/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','SOURCES.json','SOURCES_README.md']]+list((SUP/'sources').glob('*'))
paths += list((BASE/'context').glob('*.txt'))+[BASE/'BOARD.md',BASE/'claude'/'B20'/'STREAM_NOTES.md']
paths += [p for p in (BASE/'agents').glob('A*/runs/**/*') if p.is_file() and p.suffix in ('.md','.json') and 'big' not in p.parts]
for p in sorted(set(paths)):
    if not p.is_file(): continue
    b=p.read_bytes()
    if len(b)>20_000_000: continue
    manifest.append({'path':str(p),'bytes':len(b),'sha256':sha(b),'observed_utc':datetime.now(timezone.utc).isoformat()})
    if p.suffix in ('.md','.json','.txt','.tex','.py'): contents[str(p)]=b.decode('utf-8-sig',errors='replace')
dump('SOURCE_RECEIPTS.json',manifest)
claims=[]; parse_errors=[]
for path,t in contents.items():
    if Path(path).name!='CLAIMS.json': continue
    try:
        j=json.loads(t); rows=j if isinstance(j,list) else j.get('claims',[])
        for c in rows:
            if isinstance(c,dict) and 'claim_id' in c:
                claims.append({'file':path,'record':c,'statement_only_sha256':sha(c.get('exact_statement','').encode())})
    except Exception as e: parse_errors.append({'file':path,'error':str(e)})
reg=json.loads(contents[str(CAN/'CLAIM_REGISTRY.json')])
for c in reg['claims']: claims.append({'file':str(CAN/'CLAIM_REGISTRY.json'),'record':c,'statement_only_sha256':sha(c.get('exact_statement','').encode())})
dump('CLAIM_CENSUS.json',claims)
dump('PARSE_ERRORS.json',parse_errors)
reviews=[x for x in claims if x['record'].get('review_records') or any(w in str(x['record'].get('status','')).upper() for w in ['ACCEPT','REVIEWED'])]
dump('ACCEPTANCE_EVIDENCE.json',reviews)
seeds=[x for x in claims if 'A096' in x['record']['claim_id'] or 'B05-SPARSE' in x['record']['claim_id']]
affected={x['record']['claim_id'] for x in seeds}; direct=set(affected)
edges=[]
for x in claims:
    for dep in x['record'].get('proof_dependencies',[]):
        d=dep.get('claim_id') if isinstance(dep,dict) else str(dep).split('@')[0]
        if d: edges.append({'from':d,'to':x['record']['claim_id'],'file':x['file'],'dependency':dep})
while True:
    new=affected|{e['to'] for e in edges if e['from'] in affected}
    if new==affected: break
    affected=new
dump('CORRECTION_DEPENDENCY_CLOSURE.json',{'seeds':sorted(direct),'reachable_claim_ids':sorted(affected),'edges':[e for e in edges if e['from'] in affected],'note':'Declared dependencies only; textual citations audited separately. No status mutation inferred from a citation alone.'})
hits=[]
pattern=re.compile(r'A096|B05-SPARSE|O-B05|sparse.activation|variance.refund|bent.defect',re.I)
for path,t in contents.items():
    if Path(path).suffix not in ('.md','.json','.tex'): continue
    lines=t.splitlines()
    for i,l in enumerate(lines):
        if pattern.search(l): hits.append({'file':path,'line':i+1,'text':l[:2500]})
dump('CORRECTION_TEXT_CITATIONS.json',hits)
runs=[]
for agent in sorted((BASE/'agents').glob('A*')):
    for r in sorted((agent/'runs').glob('*')):
        if not r.is_dir() or r==RUN: continue
        required=['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json']
        fs=[p for p in r.rglob('*') if p.is_file() and 'big' not in p.parts]
        runs.append({'agent':agent.name,'run':str(r),'required_present':{n:(r/n).is_file() for n in required},'file_count':len(fs),'local_save_verified':(r/'REPORT.md').is_file(),'remote_copy_verified_by_this_run':False,'public_release_verified_by_this_run':False})
dump('LIVE_RUN_PERSISTENCE.json',runs)
dump('FAILED_ROUTE_ARCHIVE.json',json.loads(contents[str(CAN/'OBSTRUCTION_REGISTRY.json')]))
# Focused source extracts are read next by the investigator; full bytes are hashed above.
extract=[]
for path,t in contents.items():
    p=Path(path)
    if p.suffix=='.txt' or p.name=='FEI_100_agent_research_plan.tex':
        ls=t.splitlines(); inds=[i for i,l in enumerate(ls) if re.search(r'Theorem|Proposition|Conjecture|pivotal.bound|C018|C019|C020|C024|A100|A096',l,re.I)]
        for i in inds: extract.append('\n'+path+':'+str(i+1)+'\n'+'\n'.join(ls[max(0,i-2):i+14]))
(OUT/'PAPER_AND_PLAN_EXTRACTS.txt').write_text('\n'.join(extract),encoding='utf-8')
print(json.dumps({'sources':len(manifest),'claims':len(claims),'review_records_or_statuses':len(reviews),'text_citations':len(hits),'live_runs':len(runs),'parse_errors':parse_errors,'closure':sorted(affected)},indent=2))
