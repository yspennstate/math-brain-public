import json, hashlib, re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
base=Path('~/mop_fei100')
paths=[Path('~/AGENTS.md'),Path('BOARD.md')]
report=base/'reports/fei-2026-10-11'
paths += [report/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
sup=base/'research_pushes/2026-10-11-full-fei-100-agents'
paths += [sup/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((sup/'sources').glob('*.txt'))+list((sup/'sources').glob('*.md'))
paths += list(Path('context').glob('*.txt'))
src=Path('agents/A019/runs/20261026T211700Z-account04-A019-orthogonality-extensions')
paths += [src/x for x in ['REPORT.md','CLAIMS.json','code/stage.py','code/audit.py']]
rows=[]
for p in paths:
    if not p.exists():
        rows.append({'path':str(p),'missing':True});continue
    b=p.read_bytes()
    try:t=b.decode('utf-8-sig');enc='utf-8-sig'
    except UnicodeDecodeError:t=b.decode('cp1252');enc='cp1252-source-bytes'
    hit=[{'line':i+1,'text':line[:350]} for i,line in enumerate(t.splitlines()) if re.search(r'A016|B04|Proposition 8\.6|C024|C019|shared.data|stopping tree',line,re.I)]
    rows.append({'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'encoding':enc,'relevant_lines':hit[:14]})
(R/'out').mkdir(exist_ok=True)
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print(json.dumps({'sources_read':len(rows),'missing':[x['path'] for x in rows if x.get('missing')],'locators':[{ 'path':x['path'],'lines':[y['line'] for y in x.get('relevant_lines',[])]} for x in rows if 'context' in x['path']]}))
