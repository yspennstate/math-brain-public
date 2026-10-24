from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
BASE=Path('~')
paths=[BASE/'AGENTS.md',BASE/'brain_workers/FEI100_20261011/BOARD.md',BASE/'brain_workers/FEI100_20261011/claude/B14/STREAM_NOTES.md']
campaign=BASE/'mop_fei100/reports/fei-2026-10-11'
paths += [campaign/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
supp=BASE/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += sorted((supp/'sources').glob('*.md'))+ sorted((supp/'sources').glob('*.txt'))
paths += sorted((BASE/'brain_workers/FEI100_20261011/context').glob('*.txt'))
paths += sorted(ROOT.parent.glob('*/REPORT.md'))
paths += [BASE/'brain_workers/FEI100_20261011/agents/A088/runs/20261014T053751Z-account05-A088-booleanity-referee/CONDITIONAL_FLAG_OBSTRUCTION.md', BASE/'brain_workers/FEI100_20261011/agents/A096/runs/20261014T042803Z-account05-A096-live-gap-ledger/DERIVATION.md']
receipts=[];excerpts=[]
for p in paths:
    if not p.is_file():
        receipts.append({'path':str(p),'missing':True});continue
    b=p.read_bytes()
    try: s=b.decode('utf-8-sig');enc='utf-8-sig'
    except UnicodeDecodeError: s=b.decode('cp1252');enc='cp1252'
    receipts.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'encoding':enc})
    if p.name in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','CURRENT_STATUS.md','README.md'] or p.suffix=='.txt':
        ls=s.splitlines();hits=[(i+1,x[:260]) for i,x in enumerate(ls) if re.search('hypercontract|entropy|threshold|point.defect|same.C|reserve|A067|B14',x,re.I)]
        excerpts.append({'path':str(p),'hits':hits[:12]})
    if p.name in ['PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']:
        def walk(o):
            if isinstance(o,dict):
                for k,v in o.items():
                    if k in ('A067','B14'): excerpts.append({'path':str(p),'key':k,'value':v})
                    else: walk(v)
            elif isinstance(o,list):
                for v in o:
                    if isinstance(v,dict) and (v.get('packet_id')=='A067' or v.get('stream')=='B14'): excerpts.append({'path':str(p),'value':v})
        walk(json.loads(s))
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
(ROOT/'out/INTAKE_EXCERPTS.json').write_text(json.dumps(excerpts,indent=2),encoding='utf-8')
print(json.dumps({'read_sources':len(receipts),'missing':[x['path'] for x in receipts if x.get('missing')],'excerpts':excerpts},ensure_ascii=True)[:20000])
