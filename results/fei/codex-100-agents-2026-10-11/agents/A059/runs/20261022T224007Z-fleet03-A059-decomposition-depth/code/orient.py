from pathlib import Path
import json, hashlib, re
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(parents=True,exist_ok=True)
base=Path('math-open-problems/reports/fei-2026-10-11')
supp=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
files=[base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((supp/'sources').glob('*.md'))
files += list(Path('context').glob('*.txt'))
receipts=[]
for p in files:
    if not p.exists():
        print('MISSING',p);continue
    raw=p.read_bytes()
    try:s=raw.decode('utf-8-sig');encoding='utf-8-sig'
    except UnicodeDecodeError:s=raw.decode('cp1252');encoding='cp1252 (legacy source bytes, explicit fallback)'
    receipts.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),encoding=encoding))
    if p.suffix=='.json':
        obj=json.loads(s)
        def walk(v):
            if isinstance(v,dict):
                if any(str(v.get(k,'')) in ['A059','B12','C019','C024'] for k in ['packet_id','stream','claim_id','id']):
                    print(p.name,json.dumps(v,ensure_ascii=False)[:1800]);return
                for val in v.values():walk(val)
            elif isinstance(v,list):
                for val in v:walk(val)
        walk(obj)
    elif p.name in ['CLAIMS.md','COUNTEREXAMPLES.md']:
        print(p.name,s[:1800])
    elif p.suffix=='.tex' or p.parent.name=='context':
        lines=s.splitlines(); hits=[i for i,l in enumerate(lines) if re.search(r'composition|read.once|selector|stopping|decomposition',l,re.I)]
        print(p.name,'lines',len(lines),'locators',hits[:30])
        for i in hits[-3:]:print('\n'.join(lines[max(0,i-1):i+3]))
(R/'out'/'SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
print('READ_FILES',len(receipts))
