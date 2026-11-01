from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parents[1]
B=Path(r'~\mop_fei100')
W=Path(r'~\brain_workers\FEI100_20261011')
paths=[B/'reports/fei-2026-10-11'/n for n in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [B/'research_pushes/2026-10-11-full-fei-100-agents'/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((B/'research_pushes/2026-10-11-full-fei-100-agents/sources').glob('*.txt'))
paths += list((B/'research_pushes/2026-10-11-full-fei-100-agents/sources').glob('*.md'))
paths += list((W/'context').glob('*.txt'))
paths += [W/'agents/A012/runs/20261027T062634Z-fleet04-A012-sparse-activation-accounting'/n for n in ['REPORT.md','DERIVATION.md','CLAIMS.json']]
receipts=[]
for p in paths:
    data=p.read_bytes();enc='utf-8-sig'
    try:s=data.decode(enc)
    except UnicodeDecodeError:enc='cp1252';s=data.decode(enc)
    lines=s.splitlines()
    hits=[(i+1,l[:240]) for i,l in enumerate(lines) if re.search(r'A013|C024|C020|Proposition 8.6|shared.data|initial.source|full FEI|Fourier.*marginal',l,re.I)]
    receipts.append(dict(path=str(p),sha256=hashlib.sha256(data).hexdigest(),encoding=enc,lines=len(lines),excerpts=hits[:6]))
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
for row in receipts:
    print(Path(row['path']).name,row['lines'],row['encoding'])
    for no,line in row['excerpts'][:1]:print(no,line)
