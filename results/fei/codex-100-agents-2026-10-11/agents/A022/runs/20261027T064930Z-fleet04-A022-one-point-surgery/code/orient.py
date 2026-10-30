from pathlib import Path
import json,hashlib
run=Path(__file__).resolve().parents[1]
own=run.parents[1]
base=Path(r'math-open-problems/reports\fei-2026-10-11')
sup=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
ctx=Path(r'context')
files=[base/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files +=[sup/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]+list((sup/'sources').glob('*.md'))+list(ctx.glob('*.txt'))
files += list((base/'runs/B05').glob('*/REPORT.md'))+[p/'REPORT.md' for p in (own/'runs').iterdir() if p!=run and (p/'REPORT.md').exists()]
receipts=[];excerpts=[]
for p in files:
 if not p.exists():continue
 raw=p.read_bytes()
 try:s=raw.decode('utf-8-sig');encoding='utf-8-sig'
 except UnicodeDecodeError:s=raw.decode('cp1252');encoding='cp1252 explicit fallback'
 receipts.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':encoding})
 lines=s.splitlines();hits=[]
 for i,line in enumerate(lines):
  if any(k in line.lower() for k in ['a022','b05','composition identit','proposition 8.6','theorem 1.1','universal','c024']):hits.append({'line':i+1,'text':line[:400]})
 excerpts.append({'path':str(p),'hits':hits[:8]})
(run/'out/SOURCE_READS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
(run/'out/SOURCE_EXCERPTS.json').write_text(json.dumps(excerpts,indent=2),encoding='utf-8')
print('Read/hash/explicit decode receipts:',len(receipts),'; targeted excerpts saved; not a full independent review.')
for p in [own.parent/'A021/runs/20261027T031920Z-fleet04-A021-rare-core-asymptotics/CLAIMS.json']:
 d=json.loads(p.read_text(encoding='utf-8'));print('DEPENDENCY',json.dumps(d)[:1200])
board=(own.parents[1]/'BOARD.md').read_text(encoding='utf-8')
print('\n'.join(x for x in board.splitlines() if any(k in x for k in ['- A087','- A094','- A096','- A097'])))
