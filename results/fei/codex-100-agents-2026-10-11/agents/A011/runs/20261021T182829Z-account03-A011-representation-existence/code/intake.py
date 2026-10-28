from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
base=Path('~/mop_fei100')
report=base/'reports/fei-2026-10-11'
push=base/'research_pushes/2026-10-11-full-fei-100-agents'
files=[Path('~/AGENTS.md')]
files += [report/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [push/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((push/'sources').glob('*.txt'))+list((push/'sources').glob('*.md'))
files += list(Path('context').glob('*.txt'))
files += list((R.parents[1]/'runs').glob('*/REPORT.md'))
files += [Path('BOARD.md'),Path('claude/B03/STREAM_NOTES.md')]
receipts=[]
for p in dict.fromkeys(files):
 if not p.is_file():
  receipts.append({'path':str(p),'missing':True});continue
 raw=p.read_bytes()
 try:txt=raw.decode('utf-8-sig');enc='utf-8-sig'
 except UnicodeDecodeError:txt=raw.decode('cp1252');enc='cp1252-source-fallback'
 receipts.append({'path':str(p),'encoding':enc,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'headings':[x[:180] for x in txt.splitlines() if x.startswith('#') or ('Proposition 8.6' in x)][:35]})
(R/'out').mkdir(exist_ok=True)
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
for v in receipts:
 print(v['path'],v.get('bytes','MISSING'))
 if 'SEED' in v['path'] or 'CURRENT_STATUS' in v['path']:print(v.get('headings'))
