"""Pin original evidence and print small source-bound orientation excerpts."""
from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parents[1]
base=Path('math-open-problems/reports/fei-2026-10-11')
supp=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
ctx=Path('context')
files=[base/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += sorted(ctx.glob('*.txt'))
files += [Path('BOARD.md'),Path('claude/B14/STREAM_NOTES.md')]
own=root.parent
files += sorted(own.glob('*/REPORT.md'))
a68=Path('agents/A068/runs/20261026T195737Z-account04-A068-antichain-beyond-one-order')
files += [a68/n for n in ['REPORT.md','PROOF.md','CLAIMS.json']]
records=[]
for p in files:
    if not p.is_file():
        records.append({'path':str(p),'status':'MISSING'});continue
    raw=p.read_bytes()
    try: txt=raw.decode('utf-8-sig'); enc='utf-8-sig'
    except UnicodeDecodeError: txt=raw.decode('cp1252'); enc='cp1252 (strict UTF-8 failed; source unchanged)'
    records.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'decoding':enc})
    if p.parent==supp or p.parent==ctx or p.name in ['CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']:
        lines=txt.splitlines(); hits=[(i+1,l[:200]) for i,l in enumerate(lines) if re.search(r'A066|B14|semigroup|Frullani|noise semigroup|point.edit|stabilizer',l,re.I)]
        print(p.name+': '+json.dumps(hits[:3],ensure_ascii=False))
(root/'out'/'SOURCES.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
print('source records',len(records),'supplement source files',len(list((supp/'sources').glob('*'))))
