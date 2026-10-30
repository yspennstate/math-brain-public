from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
base=Path(r'math-open-problems/reports\fei-2026-10-11')
supp=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
context=Path(r'context')
files=[base/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += sorted((supp/'sources').glob('*.md'))+sorted(context.glob('*.txt'))
files += [Path(r'~\AGENTS.md'),Path(r'BOARD.md'),Path(r'claude\B07\STREAM_NOTES.md')]
receipts=[]; excerpts=[]
for p in files:
 raw=p.read_bytes()
 try:text=raw.decode('utf-8-sig');enc='utf-8-sig'
 except UnicodeDecodeError:text=raw.decode('cp1252');enc='cp1252 (explicit export fallback)'
 relevant=[line for line in text.splitlines() if any(w.lower() in line.lower() for w in ['A032','G-PHASE-COND','C018','C019','C020','C024','signed Boolean','restriction','abstract'])]
 receipts.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':enc,'relevant_lines':len(relevant),'scope':'baseline recovery; only explicitly derived mathematics used'})
 excerpts.append({'path':str(p),'selected_lines':relevant[:12]})
for p in [ROOT.parent.parent/'runs/20261023T141525Z-fleet03-A032-boolean-phase-realizability/PROOF.md',Path(r'agents\A079\runs\20261026T230307Z-fleet04-A079-correlated-auxiliaries\PROOF.md')]:
 raw=p.read_bytes();receipts.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'scope':'actual proof dependency independently reconstructed'})
(ROOT/'out/SOURCE_MANIFEST.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
(ROOT/'out/SOURCE_EXCERPTS.json').write_text(json.dumps(excerpts,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'sources':len(receipts),'papers':len(list(context.glob('*.txt'))),'source_status':'read and pinned; no unseen theorem used'}))
