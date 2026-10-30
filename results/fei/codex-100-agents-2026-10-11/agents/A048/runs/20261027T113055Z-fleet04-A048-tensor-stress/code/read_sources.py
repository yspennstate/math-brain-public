from pathlib import Path
import json, hashlib, re
R=Path(__file__).resolve().parents[1]
base=Path('~/mop_fei100')
camp=base/'reports/fei-2026-10-11'
supp=base/'research_pushes/2026-10-11-full-fei-100-agents'
paths=[camp/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').glob('*.md'))
paths += list(Path('context').glob('*.txt'))
paths += [Path('~/brain_workers/PRIMARY_DIRECTIVE.md'),Path('~/<private-repo>/12_cognitive_architecture/scheduled_tasks/README.md'),Path('~/AGENTS.md')]
receipts=[]
for p in paths:
    if not p.exists():
        print('MISSING',p); continue
    raw=p.read_bytes(); enc='utf-8-sig'
    try: text=raw.decode(enc)
    except UnicodeDecodeError:
        enc='cp1252'; text=raw.decode(enc)
    lines=text.splitlines()
    receipts.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),lines=len(lines),encoding=enc))
    relevant=[(i+1,s) for i,s in enumerate(lines) if re.search(r'A048|B10|C019|C024|tensor|activation|composition|full.fei.only',s,re.I)]
    print('\nSOURCE',p.name,'lines',len(lines))
    for i,s in relevant[:5]: print(f'{i}: {s[:320]}')
R.joinpath('out').mkdir(exist_ok=True)
R.joinpath('out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
