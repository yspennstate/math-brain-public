from pathlib import Path
import hashlib,json,re
root=Path(r'~\brain_workers\FEI100_20261011')
run=root/'agents/A012/runs/20261027T062634Z-fleet04-A012-sparse-activation-accounting'
base=Path(r'~\mop_fei100')
paths=[Path(r'~\AGENTS.md')]
paths += [base/'reports/fei-2026-10-11'/n for n in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [base/'research_pushes/2026-10-11-full-fei-100-agents'/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((root/'context').glob('*.txt'))
paths += list((base/'research_pushes/2026-10-11-full-fei-100-agents/sources').glob('*.txt'))
rows=[]
for p in paths:
    if not p.is_file():
        rows.append({'path':str(p),'missing':True});continue
    data=p.read_bytes();encoding='utf-8-sig'
    try:s=data.decode(encoding)
    except UnicodeDecodeError:
        encoding='cp1252';s=data.decode(encoding)
    lines=s.splitlines()
    hits=[(i+1,l[:500]) for i,l in enumerate(lines) if re.search(r'A012|C024|C020|Jensen|spectral marginal|projection|Proposition 8.6|G-J-COST',l,re.I)]
    rows.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'encoding':encoding,'lines':len(lines),'target_excerpts':hits[:14]})
(run/'out').mkdir(exist_ok=True)
(run/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
for row in rows:
    print(Path(row['path']).name, row.get('lines','MISSING'))
    for no,s in row.get('target_excerpts',[])[:3]:print(no,s)
