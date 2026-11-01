from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
base=Path('~/mop_fei100')
paths=list((base/'reports/fei-2026-10-11').glob('*'))
paths=[p for p in paths if p.suffix in ['.json','.md','.tex']]
paths+=list((base/'reports/fei-2026-10-11/runs').rglob('REPORT.md'))
sup=base/'research_pushes/2026-10-11-full-fei-100-agents'
paths += [sup/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths+=list((sup/'sources').glob('*.md'))
paths+=list(Path('~/brain_workers/FEI100_20261011/context').glob('*.txt'))
receipts=[]
for p in paths:
    b=p.read_bytes()
    try:s=b.decode('utf-8-sig')
    except UnicodeDecodeError:s=b.decode('cp1252')
    receipts.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
    if p.suffix=='.txt':
        lines=s.splitlines()
        print('\nSOURCE',p.name,'LINES',len(lines))
        for i,line in enumerate(lines):
            if re.search(r'composition|restriction|entropy.*identity|shared.data|Theorem 1|pivotal sets|singularity',line,re.I):
                print(i+1, '\n'.join(lines[max(0,i-1):i+4]))
    if p.name=='PACKET_STATUS.json':
        data=json.loads(s)
        print('PACKET keys',list(data))
        for k,v in data.items():
            if isinstance(v,list):
                for row in v:
                    if isinstance(row,dict) and row.get('packet_id')=='A074':print(json.dumps(row,indent=2))
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out/source_receipts.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
