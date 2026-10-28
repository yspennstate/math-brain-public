from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
TEAM=Path(r'~\brain_workers\FEI100_20261011')
C=Path(r'math-open-problems/reports\fei-2026-10-11')
S=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
sources=[C/f for f in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
sources += [S/f for f in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sources += list((S/'sources').glob('*.md'))+list((TEAM/'context').glob('*.txt'))
sources += [TEAM/'BOARD.md',TEAM/'claude/B06/STREAM_NOTES.md']
sources += [TEAM/'agents/A029/runs/20261026T213208Z-account04-A029-child-deficit-transport'/f for f in ['CLAIMS.json','DERIVATION.md','REPORT.md']]
sources += [TEAM/'agents/A094/runs/20261026T232939Z-account04-A094-proof-chain-challenger'/f for f in ['CLAIMS.json','DERIVATION.md','REPORT.md']]
sources += [TEAM/'agents/A026/runs/20261023T135203Z-account03-A026-good-coordinate-erasure'/f for f in ['CLAIMS.json','DERIVATION.md','code/check.py']]
receipts=[];excerpts=[]
keys=['B06','A026','C018','C019','C024','restriction','shared data','shared-data','composition','erasure','Theorem 1.1']
for p in sources:
 b=p.read_bytes()
 try:s=b.decode('utf-8-sig');enc='utf-8-sig'
 except UnicodeDecodeError:s=b.decode('cp1252');enc='cp1252'
 lines=s.splitlines(); hits=[i for i,v in enumerate(lines) if any(k.lower() in v.lower() for k in keys)]
 receipts.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'encoding':enc,'matching_lines':len(hits)})
 inds=set()
 for i in hits[:10]:inds.update(range(max(0,i-1),min(len(lines),i+4)))
 excerpts.append({'path':str(p),'lines':[{'number':i+1,'text':lines[i]} for i in sorted(inds)]})
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8',newline='\n')
(R/'out/SOURCE_EXCERPTS.json').write_text(json.dumps(excerpts,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'files':len(receipts),'paper_decodings':[x for x in receipts if x['path'].endswith('.txt')]}))
