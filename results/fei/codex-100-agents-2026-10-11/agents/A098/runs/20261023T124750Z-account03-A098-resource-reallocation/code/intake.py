from pathlib import Path
import json,hashlib
RUN=Path(__file__).resolve().parents[1]; OUT=RUN/'out';OUT.mkdir(exist_ok=True)
BASE=RUN.parents[3]; CAN=Path(r'math-open-problems/reports\fei-2026-10-11')
SUP=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
receipts=[]
def read(p):
    b=p.read_bytes();receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
    return b.decode('utf-8-sig',errors='replace')
for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:read(CAN/name)
for p in SUP.rglob('*'):
    if p.is_file() and p.suffix in ('.md','.txt','.json','.tex'):read(p)
for p in (BASE/'context').glob('*.txt'):read(p)
for p in (CAN/'runs').rglob('REPORT.md'):read(p)
board=read(BASE/'BOARD.md');(OUT/'BOARD_SNAPSHOT.md').write_text(board,encoding='utf-8')
read(BASE/'claude/B20/STREAM_NOTES.md')
prev=RUN.parent/'20261023T105358Z-account03-A098-resource-reallocation'
old={x['packet']:x for x in json.loads(read(prev/'out/PACKET_CENSUS.json'))}
census=[];changes=[];pending=[]
for d in sorted((BASE/'agents').glob('A[0-9][0-9][0-9]')):
    status=read(d/'STATUS.md') if (d/'STATUS.md').exists() else ''
    runs=[p for p in (d/'runs').iterdir() if p.is_dir() and (p/'REPORT.md').exists()]
    latest=max(runs,key=lambda p:p.name) if runs else None
    raw=[]
    if latest:
        for name in ['REPORT.md','CLAIMS.json','PROGRESS.json']:
            p=latest/name
            if p.exists():
                s=read(p)
                if name=='CLAIMS.json':
                    try:raw=json.loads(s)
                    except ValueError:raw={'parse_error':True}
    row={'packet':d.name,'status':status,'latest_complete_report':str(latest) if latest else None,'claims':raw}
    census.append(row)
    if row['latest_complete_report']!=old.get(d.name,{}).get('latest_complete_report'):changes.append({'packet':d.name,'old':old.get(d.name,{}).get('latest_complete_report'),'new':row['latest_complete_report'],'status':status})
    if d.name=='A098':
        for p in (d/'runs').glob('*/REPORT.md'):read(p)
for aid in ['A096','A097','A085','A099','A003','A050','A079','A046','A040']:
    row=next(x for x in census if x['packet']==aid)
    if row['latest_complete_report']:
        p=Path(row['latest_complete_report'])
        for name in ['DERIVATION.md','PROOF.md']:
            if (p/name).exists():read(p/name)
for name,obj in [('SOURCE_LEDGER.json',receipts),('PACKET_CENSUS.json',census),('CHANGED_SOURCES.json',changes)]:
    (OUT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'sources':len(receipts),'packets':len(census),'changed_latest_reports':len(changes)}))
