from pathlib import Path
import hashlib, json

root=Path(r'~\brain_workers\FEI100_20261011')
campaign=Path(r'math-open-problems/reports\fei-2026-10-11')
supp=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
receipt=[]
def read(p,cap=None):
    if not p.exists():
        print('MISSING',p);return
    s=p.read_text(encoding='utf-8-sig');receipt.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'characters':len(s)})
    print('\nFILE',p,'CHARS',len(s))
    print(s if cap is None else s[:cap])
for name in ['README.md','CURRENT_STATUS.md','STREAM_NEXT_ACTIONS.json']:
    read(campaign/name,10000)
for name in ['CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json']:
    p=campaign/name;s=p.read_text(encoding='utf-8-sig');receipt.append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'characters':len(s)})
    data=json.loads(s)
    print('\nINDEX',name,'chars',len(s),'keys',list(data) if isinstance(data,dict) else len(data))
    def walk(x):
        if isinstance(x,dict):
            if any(str(x.get(k,'')) in ['A088','A067','A070','C018','C019','C024'] for k in ['packet_id','claim_id','gap_id']):
                print(json.dumps(x,ensure_ascii=False));return
            for v in x.values():walk(v)
        elif isinstance(x,list):
            for v in x:walk(v)
    walk(data)
read(campaign/'FEI_100_agent_research_plan.tex',9000)
for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:
    read(supp/name,9000)
print('\nSUPPLEMENT SOURCES',*[str(p.relative_to(supp)) for p in (supp/'sources').rglob('*') if p.is_file()],sep='\n')
for agent in ['A067','A070','A038','A039']:
    d=root/'agents'/agent
    read(d/'STATUS.md')
    runs=sorted((d/'runs').iterdir())
    for run in runs[-2:]:
        print('AGENT RUN',run)
        read(run/'REPORT.md',19000)
own=root/'agents/A088/runs/20261014T053751Z-fleet05-A088-booleanity-referee'
for name in ['REPORT.md','CLAIMS.json']:
    read(own/name,24000)
for run in sorted((root/'agents/A088/runs').iterdir()):
    if run.name.startswith('2026102') and run.name!='20261022T215524Z-fleet03-A088-booleanity-referee':
        print('PRIOR RUN',run.name,*[p.name for p in run.iterdir()])
out=Path(__file__).resolve().parents[1]/'out';out.mkdir(exist_ok=True)
(out/'source_receipts.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
