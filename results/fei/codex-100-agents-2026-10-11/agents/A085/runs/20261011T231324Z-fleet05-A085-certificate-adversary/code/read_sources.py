from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'; OUT.mkdir(exist_ok=True)
repo=Path(r'~\mop_fei100')
team=Path(r'~\brain_workers\FEI100_20261011')
files=[]
base=repo/'reports/fei-2026-10-11'
files += [base/f for f in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += list((base/'runs').rglob('REPORT.md'))
sup=repo/'research_pushes/2026-10-11-full-fei-100-agents'
files += [sup/f for f in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((sup/'sources').glob('*.md'))
files += list((team/'context').glob('*.txt'))
files += [team/'BOARD.md',team/'claude/B17/STREAM_NOTES.md']
for a in ['A071','A042','A047']:
    run=next((team/'agents'/a/'runs').iterdir())
    files += [p for p in run.rglob('*') if p.is_file() and p.suffix in ['.py','.md','.json','.tex'] and 'out' not in p.parts]
records=[]; excerpts=[]
for p in files:
    if not p.exists(): records.append({'path':str(p),'missing':True}); continue
    data=p.read_bytes(); txt=data.decode('utf-8-sig',errors='replace')
    records.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'lines':len(txt.splitlines())})
    if p.name=='PACKET_STATUS.json':
        obj=json.loads(txt)
        excerpts.append({'path':str(p),'A085_mentions':[line for line in txt.splitlines() if 'A085' in line]})
    elif p.suffix=='.txt' or p.suffix=='.tex' or p.parent.name=='sources':
        lines=txt.splitlines(); hits=[]
        for i,line in enumerate(lines):
            if re.search(r'(?i)(theorem [1-6ABC]|bias|endpoint|finite|certificate|A085|B17|Maassen|uncertainty)',line):
                hits.append({'line':i+1,'text':' '.join(lines[max(0,i-1):i+3])})
        excerpts.append({'path':str(p),'hits':hits[:50]})
(OUT/'source_receipts.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf8')
(OUT/'source_locators.json').write_text(json.dumps(excerpts,indent=2)+'\n',encoding='utf8')
print(json.dumps({'files_read':len(records),'missing':[r for r in records if r.get('missing')],'locators':str(OUT/'source_locators.json')},indent=2),flush=True)
for e in excerpts:
    if 'context' in e['path'] or e['path'].endswith('FEI_100_agent_research_plan.tex'):
        print(e['path'],json.dumps(e.get('hits',[])[:12]),flush=True)
