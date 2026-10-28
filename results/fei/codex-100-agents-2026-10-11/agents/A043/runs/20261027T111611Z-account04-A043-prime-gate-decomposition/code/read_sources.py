from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];out=R/'out';out.mkdir(exist_ok=True)
base=Path('math-open-problems/reports/fei-2026-10-11')
push=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
context=Path('context')
files=[base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [push/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += sorted(context.glob('*.txt'))
files += [Path('BOARD.md'),Path('claude/B09/STREAM_NOTES.md')]
files += [Path('agents/A041/runs/20261027T041724Z-account04-A041-weighted-threshold-fei/PROOF.md'),Path('agents/A045/runs/20261027T005611Z-account04-A045-biased-realizability-referee/PROOF.md')]
files += sorted((push/'sources').glob('*.txt'))
receipts=[];excerpts=[]
for p in files:
 if not p.exists():
  receipts.append({'path':str(p),'missing':True});continue
 b=p.read_bytes()
 try:s=b.decode('utf-8-sig');enc='utf-8-sig'
 except UnicodeDecodeError:s=b.decode('cp1252');enc='cp1252'
 receipts.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'decoding':enc})
 hits=[(i+1,line[:250]) for i,line in enumerate(s.splitlines()) if any(k in line.lower() for k in ['prime','composition','b09','c018','c020','full_fei_status'])]
 excerpts.append({'path':str(p),'matching_lines':hits[:8]})
(out/'source_receipts.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
(out/'source_excerpts.json').write_text(json.dumps(excerpts,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'files':len(receipts),'missing':[r['path'] for r in receipts if r.get('missing')],'excerpts':excerpts[:3]},indent=2))
