from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[1]
base=Path('~/mop_fei100/reports/fei-2026-10-11')
supp=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
paths=list(base.glob('*.json'))+list(base.glob('*.md'))+[base/'FEI_100_agent_research_plan.tex']
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths+=list((supp/'sources').glob('*.md'))+list((base/'runs').rglob('REPORT.md'))
paths+=list(Path('~/brain_workers/FEI100_20261011/context').glob('*.txt'))
records=[]; excerpts=[]
for p in paths:
    b=p.read_bytes()
    try: s=b.decode('utf-8'); encoding='utf-8'
    except UnicodeDecodeError: s=b.decode('cp1252'); encoding='cp1252'
    records.append(dict(path=str(p),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),encoding=encoding))
    if p.name=='AGENT_ASSIGNMENTS.json':
        obj=json.loads(s)
        def walk(x):
            if isinstance(x,dict):
                if x.get('packet_id')=='A054' or x.get('agent_id')=='A054': excerpts.append(json.dumps(x,indent=2))
                else:
                    for v in x.values(): walk(v)
            elif isinstance(x,list):
                for v in x: walk(v)
        walk(obj)
    if p.suffix=='.txt':
        lines=s.splitlines(); selected=set(range(min(100,len(lines))))
        for i,l in enumerate(lines):
            if any(t in l.lower() for t in ['proposition 8.9','corollary 8.10','theorem 1.1','theorem 1.2','composition','raw entropy']): selected.update(range(max(0,i-3),min(len(lines),i+12)))
        excerpts.append('\nFILE '+str(p)+'\n'+'\n'.join(f'{i+1}: {lines[i]}' for i in sorted(selected)))
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out/SOURCE_MANIFEST.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
(ROOT/'out/READ_EXCERPTS.txt').write_text('\n'.join(excerpts),encoding='utf-8')
print('Loaded and hashed',len(records),'local source files. Relevant excerpts saved.')
print('\n'.join(excerpts)[:17000])
