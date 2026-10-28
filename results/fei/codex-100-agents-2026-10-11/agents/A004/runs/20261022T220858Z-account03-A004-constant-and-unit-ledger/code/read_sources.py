from pathlib import Path
import hashlib, json
RUN=Path(__file__).resolve().parents[1]
base=Path('~/mop_fei100')
report=base/'reports/fei-2026-10-11'
supp=base/'research_pushes/2026-10-11-full-fei-100-agents'
context=Path('context')
files=[report/x for x in ['CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md']]
files += list((supp/'sources').glob('*'))
files += list(context.glob('*.txt'))
files += [RUN.parents[1]/'runs/20261014T054158Z-account05-A004-constant-and-unit-ledger/REPORT.md']
manifest=[]
for p in files:
    if not p.is_file(): continue
    b=p.read_bytes(); t=b.decode('utf-8-sig',errors='replace')
    manifest.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'scope':'source inspection; selected relevant passages printed, no fresh full theorem audit'})
    print('\nSOURCE',p.name,len(b))
    if p.suffix=='.json':
        obj=json.loads(t)
        def walk(x):
            if isinstance(x,dict):
                if any(str(x.get(k,'')) in ('A004','B01','C018','C019','C020','C024') for k in ('packet_id','stream','claim_id','id')): print(json.dumps(x,ensure_ascii=False)[:4500]); return
                for v in x.values(): walk(v)
            elif isinstance(x,list):
                for v in x: walk(v)
        walk(obj)
    elif p.suffix=='.txt':
        lines=t.splitlines()
        hits=[i for i,l in enumerate(lines) if any(s in l.lower() for s in ('logarithm','log 2','pivotal probability','shared data','entropy–influence','entropy-influence'))]
        for i in hits[:4]: print('\n'.join(lines[max(0,i-2):i+5]))
    else:
        print(t[:4500] if p.name!='REPORT.md' else t)
(RUN/'out').mkdir(exist_ok=True)
(RUN/'out/SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
