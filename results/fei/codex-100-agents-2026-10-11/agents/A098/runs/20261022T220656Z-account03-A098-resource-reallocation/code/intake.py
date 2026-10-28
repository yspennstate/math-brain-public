from pathlib import Path
import hashlib,json,time
ROOT=Path(__file__).resolve().parents[1]
BASE=Path(r'~\brain_workers\FEI100_20261011')
CAN=Path(r'math-open-problems/reports\fei-2026-10-11')
SUP=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
OUT=ROOT/'out'; OUT.mkdir(exist_ok=True)
receipts=[]
def read(p):
    b=p.read_bytes(); s=b.decode('utf-8-sig',errors='replace')
    receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
    return s
paths=[CAN/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [p for p in SUP.rglob('*') if p.is_file() and p.suffix in ('.md','.txt','.tex','.json')]
paths += list((BASE/'context').glob('*.txt'))
paths += [p for p in (CAN/'runs').rglob('*') if p.is_file() and p.name in ('REPORT.md','CLAIMS.json','PROGRESS.json')]
paths += [p for p in (BASE/'agents'/'A098'/'runs').rglob('*') if p.is_file() and p.name in ('REPORT.md','CLAIMS.json','PROGRESS.json')]
for p in paths:
    if p.exists(): read(p)
census=[]
for d in sorted((BASE/'agents').glob('A[0-9][0-9][0-9]')):
    status=read(d/'STATUS.md') if (d/'STATUS.md').exists() else ''
    runs=[]
    if (d/'runs').exists():
        for p in (d/'runs').iterdir():
            if p.is_dir() and (p/'REPORT.md').exists(): runs.append(p)
    latest=max(runs,key=lambda p:p.name) if runs else None
    claims=[]
    if latest:
        for name in ['REPORT.md','CLAIMS.json','PROGRESS.json']:
            p=latest/name
            if p.exists():
                s=read(p)
                if name=='CLAIMS.json':
                    try: claims=json.loads(s)
                    except ValueError: claims={'parse_error':True}
    census.append({'packet':d.name,'status':status,'latest_complete_report':str(latest) if latest else None,'claims':claims})
(OUT/'SOURCE_LEDGER.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
(OUT/'PACKET_CENSUS.json').write_text(json.dumps(census,indent=2),encoding='utf-8')
for aid in ['A096','A097','A073','A046','A040','A095','A094']:
    c=next(c for c in census if c['packet']==aid)
    print('SOURCE',aid,c['latest_complete_report'])
    if aid in ['A096','A097','A073'] and c['latest_complete_report']:
        p=Path(c['latest_complete_report'])
        print(read(p/'REPORT.md'))
        print(read(p/'CLAIMS.json'))
print('INTAKE',len(receipts),'files',len(census),'packets')
