from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parents[1]
paths=[Path(r'~\AGENTS.md'),Path(r'BOARD.md'),Path(r'claude\B06\STREAM_NOTES.md')]
campaign=Path(r'math-open-problems/reports\fei-2026-10-11')
paths += [campaign/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
sup=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
paths += [sup/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]+list((sup/'sources').glob('*.md'))
context=Path(r'context'); paths+=list(context.glob('*.txt'))
agents=root.parents[2]
for a,d,f in [('A028','20261023T144415Z-fleet03-A028-stopping-tree-payment','DERIVATION.md'),('A026','20261023T135203Z-fleet03-A026-good-coordinate-erasure','DERIVATION.md'),('A029','20261023T125429Z-fleet03-A029-child-deficit-transport','DERIVATION.md')]: paths.append(agents/a/'runs'/d/f)
receipts=[]; excerpts=[]
for p in paths:
 b=p.read_bytes(); enc='utf-8'
 try: s=b.decode(enc)
 except UnicodeDecodeError: enc='cp1252';s=b.decode(enc)
 receipts.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'encoding':enc})
 terms=['shared-data','shared data','composition identity','restriction identity'] if p.suffix=='.txt' else ['A029','C019','C024']
 ls=s.splitlines(); found=[i for i,l in enumerate(ls) if any(t in l for t in terms)]
 excerpts.append({'path':str(p),'hits':[{'line':i+1,'context':'\n'.join(ls[max(0,i-2):i+4])} for i in found[:12]]})
(root/'out'/'SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
(root/'out'/'SOURCE_EXCERPTS.json').write_text(json.dumps(excerpts,indent=2),encoding='utf-8')
print(json.dumps({'source_files_read':len(receipts),'paper_encodings':[{k:r[k] for k in ['path','encoding']} for r in receipts if r['path'].endswith('.txt')]}))
lean=Path(r'lean_check.py').read_text(encoding='utf-8')
print('\n'.join(l for l in lean.splitlines() if any(x in l for x in ['IMPORTS =','imports =','import Lean','import Mathlib','import Std'])))
