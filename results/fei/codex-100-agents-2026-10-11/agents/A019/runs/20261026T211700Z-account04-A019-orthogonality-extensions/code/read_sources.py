from pathlib import Path
import json,hashlib,re
R=Path(__file__).resolve().parents[1]
base=Path('math-open-problems/reports/fei-2026-10-11')
other=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
files=[base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [other/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((other/'sources').glob('*'))
files += list(Path('context').glob('*.txt'))
files += [Path('~/.claude/compute/interventions.tsv'),Path('~/brain_workers/PRIMARY_DIRECTIVE.md'),Path('~/<private-repo>/12_cognitive_architecture/scheduled_tasks/README.md')]
files += list((R.parent/'20261023T125104Z-account03-A019-orthogonality-extensions').glob('*.json'))
receipts=[];excerpts=[]
for p in files:
    if not p.is_file():receipts.append({'path':str(p),'missing':True});continue
    raw=p.read_bytes()
    try:t=raw.decode('utf-8-sig');encoding='utf-8-sig'
    except UnicodeDecodeError:t=raw.decode('cp1252');encoding='cp1252'
    receipts.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':encoding})
    lines=t.splitlines();hits=[(i+1,l) for i,l in enumerate(lines) if re.search(r'A019|C019|C024|8\.6|collision|stopping.tree|Theorem|Proposition',l,re.I)]
    excerpts.append({'path':str(p),'matches':hits[:15]})
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
(R/'out/SOURCE_EXCERPTS.json').write_text(json.dumps(excerpts,indent=2),encoding='utf-8')
print(json.dumps({'files_read':len(receipts),'bytes':sum(x.get('bytes',0) for x in receipts),'missing':[x['path'] for x in receipts if x.get('missing')]}))
for x in excerpts:
    if 'threshold_paper_38' in x['path'] or 'CURRENT_STATUS' in x['path']:print(json.dumps(x))
