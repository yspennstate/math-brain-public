from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1];B=Path('~');R.joinpath('out').mkdir(exist_ok=True)
paths=[B/'AGENTS.md',B/'brain_workers/FEI100_20261011/BOARD.md',B/'brain_workers/FEI100_20261011/claude/B14/STREAM_NOTES.md',R.parent.parent/'STATUS.md']
P=B/'mop_fei100/reports/fei-2026-10-11'
paths += [P/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
S=B/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
paths += [S/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((S/'sources').glob('*.md'))+list((B/'brain_workers/FEI100_20261011/context').glob('*.txt'))
old=R.parent/'20261021T224913Z-fleet03-A067-hypercontractive-refinement'
audit=B/'brain_workers/FEI100_20261011/agents/A088/runs/20261022T215524Z-fleet03-A088-booleanity-referee'
paths += [old/x for x in ['DERIVATION.md','CLAIMS.json','REPORT.md','out/CHECK.json']]
paths += [audit/x for x in ['PROOF.md','CLAIMS.json','REPORT.md']]
rows=[]
for p in paths:
    raw=p.read_bytes()
    try:txt=raw.decode('utf-8-sig');enc='utf-8-sig'
    except UnicodeDecodeError:txt=raw.decode('cp1252');enc='cp1252'
    rows.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':enc})
(R/'out/SOURCES.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(json.dumps({'sources_byte_pinned':len(rows),'primary_dependency':'A067-POSTCORE-BENT-FLAG-SAME-CHILD-BANK@1','independent_acceptance':'A088 PROOF1 and CLAIMS unchanged source hash'}))
