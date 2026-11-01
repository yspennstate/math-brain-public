from pathlib import Path
import json, hashlib
BASE=Path(r'~')
RUN=Path(__file__).resolve().parents[1]
rep=BASE/'mop_fei100/reports/fei-2026-10-11'
supp=BASE/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
ctx=BASE/'brain_workers/FEI100_20261011/context'
paths=[rep/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += sorted((supp/'sources').glob('*.md'))
paths += sorted((rep/'runs/B17').glob('*/REPORT.md'))[-3:]
paths += sorted(ctx.glob('*.txt'))
paths += [BASE/'brain_workers/FEI100_20261011/BOARD.md',BASE/'brain_workers/FEI100_20261011/claude/B17/STREAM_NOTES.md']
paths += [BASE/'brain_workers/FEI100_20261011/agents/A075/runs/20261023T133516Z-fleet03-A075-search-to-theorem-bridge'/x for x in ['PROOF.md','CLAIMS.json']]
paths += [BASE/'brain_workers/FEI100_20261011/agents/A089/runs/20261023T130925Z-fleet03-A089-repair-specialist/PROOF.md']
receipts=[]
for p in paths:
    if not p.is_file():
        receipts.append({'path':str(p),'status':'MISSING'}); continue
    raw=p.read_bytes()
    try:s=raw.decode('utf-8-sig');encoding='utf-8-sig'
    except UnicodeDecodeError:s=raw.decode('cp1252');encoding='cp1252-explicit-fallback'
    lines=s.splitlines()
    hits=[(i+1,l[:280]) for i,l in enumerate(lines) if any(w in l.lower() for w in ['a084','c018','c019','c024','composition identity','proposition 8.6','singularity'])]
    receipts.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'encoding':encoding,'lines':len(lines),'locators':hits[:12]})
state=json.loads((BASE/'.claude/compute/compute_state.json').read_text(encoding='utf-8-sig'))
summary={k:state[k] for k in state if any(x in k.lower() for x in ['status','commit','free','timestamp','top_private_groups'])}
(RUN/'out/INTAKE.json').write_text(json.dumps({'sources':receipts,'compute':summary},indent=2),encoding='utf-8')
print(json.dumps({'source_count':len(receipts),'compute':summary,'relevant':[{ 'file':Path(r['path']).name,'locators':r.get('locators',[])[:3]} for r in receipts if r.get('locators')]},indent=2))
