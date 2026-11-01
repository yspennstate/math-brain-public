from pathlib import Path
import json

root=Path('~')
base=root/'mop_fei100/reports/fei-2026-10-11'
supp=root/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
run=Path(__file__).resolve().parent.parent
(run/'out').mkdir(exist_ok=True)
receipt=[]
def read(p, cap=2500):
    raw=p.read_bytes()
    try: s=raw.decode('utf-8')
    except UnicodeDecodeError: s=raw.decode('cp1252')
    receipt.append({'path':str(p),'characters':len(s)})
    print('\nSOURCE',p)
    if len(s)<=cap: print(s)
    else:
        lines=s.splitlines()
        hits=[(i,l) for i,l in enumerate(lines) if any(k.lower() in l.lower() for k in ['A028','C019','B06','stopping','shared','tensor','entropy identity','Theorem 8','Proposition 8'])]
        print('\n'.join(f'{i+1}: {l[:450]}' for i,l in hits)[:cap] or s[:cap])
for f in ['CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:
    read(base/f, 2500)
for f in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']:
    read(supp/f,1800)
print('SUPPLEMENT SOURCES', [str(p) for p in (supp/'sources').glob('*')])
for p in (supp/'sources').glob('*.md'): read(p,700)
ctx=root/'brain_workers/FEI100_20261011/context'
for p in ctx.glob('*.txt'): read(p,2200)
read(root/'AGENTS.md',1800)
(run/'out/context_receipts.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
