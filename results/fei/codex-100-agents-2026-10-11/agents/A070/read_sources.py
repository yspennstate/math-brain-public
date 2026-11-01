from pathlib import Path
import json, hashlib
root=Path(r'~\brain_workers\FEI100_20261011')
base=Path(r'~\mop_fei100')
paths=[]
for name in ['PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:
    paths.append(base/'reports/fei-2026-10-11'/name)
supp=base/'research_pushes/2026-10-11-full-fei-100-agents'
paths += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').rglob('*.md'))+list((supp/'sources').rglob('*.tex'))
paths += list((root/'context').glob('*.txt'))
for parent in [root/'agents/A066/runs',root/'agents/A067/runs',root/'claude/B14/runs']:
    paths += list(parent.rglob('REPORT.md'))+list(parent.rglob('CLAIMS.json'))
prior=base/'reports/fei-2026-10-11/runs'
paths += list(prior.rglob('REPORT.md'))
receipts=[]
for p in paths:
    if not p.exists():
        print('MISSING',p); continue
    raw=p.read_bytes(); s=raw.decode('utf-8-sig',errors='replace')
    receipts.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
    print('\nFILE',p,'LINES',len(s.splitlines()))
    if p.name in ['REPORT.md','CLAIMS.json','SEED_LEMMAS.md','COUNTEREXAMPLES.md'] and ('A066' in str(p) or 'A067' in str(p) or 'B14' in str(p) or 'full-fei-100' in str(p)):
        print(s)
    else:
        ls=s.splitlines(); hits=[i for i,l in enumerate(ls) if any(w.lower() in l.lower() for w in ['cyclic','non-boolean','A070','B14','semigroup','granularity','hybrid','11.51'])]
        chosen=set()
        for i in hits:
            chosen.update(range(max(0,i-2),min(len(ls),i+5)))
        for i in sorted(chosen): print(str(i+1)+': '+ls[i])
out=root/'agents/A070/source_read_receipts.json'; out.write_text(json.dumps(receipts,indent=2),encoding='utf-8')
