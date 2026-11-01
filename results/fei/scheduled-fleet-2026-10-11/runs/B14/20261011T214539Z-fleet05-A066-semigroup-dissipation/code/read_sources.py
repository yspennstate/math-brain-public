from pathlib import Path
import hashlib
import json

run = Path(__file__).resolve().parents[1]
root = Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp = Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
context = Path(r'~\brain_workers\FEI100_20261011\context')
files = [root/name for name in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += list((root/'runs').rglob('REPORT.md'))
files += [supp/name for name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((supp/'sources').glob('*.md'))
files += list(context.glob('*.txt'))
files += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md')]
records=[]
for f in files:
    data=f.read_bytes()
    try:
        text=data.decode('utf-8-sig')
        encoding='utf-8-sig'
    except UnicodeDecodeError:
        text=data.decode('cp1252')
        encoding='cp1252'
    lines=text.splitlines()
    matches=[{'line':i+1,'text':line} for i,line in enumerate(lines)
             if any(k in line.lower() for k in ['semigroup','dissipation','point defect','point-defect','rényi','renyi','reveal','natural-log','logarithms','noise operator'])]
    records.append({'path':str(f),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'encoding':encoding,'line_count':len(lines),'matching_lines':matches})
    if f.parent==context:
        print('\nPAPER '+f.name+' SHA256 '+records[-1]['sha256'])
        print('\n'.join(f'{i+1}: {s}' for i,s in enumerate(lines[:90])))
        print('MATCHES '+json.dumps(matches[:18],ensure_ascii=False))
    if f.name=='GAMMA_ENDPOINT_LEDGER.md':
        print('\nGAMMA SOURCE\n'+text)
    if f.name=='PACKET_STATUS.json':
        obj=json.loads(text)
        def scan(x):
            if isinstance(x,dict):
                if x.get('packet_id')=='A066': print('A066 RECORD '+json.dumps(x,indent=2))
                else:
                    for v in x.values(): scan(v)
            elif isinstance(x,list):
                for v in x: scan(v)
        scan(obj)
(run/'out'/'SOURCE_READ_RECEIPTS.json').write_text(json.dumps(records,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('\nFULL FILE LOADS '+str(len(records))+'; targeted excerpts printed. These receipts record bytes read, not independent theorem acceptance.')
