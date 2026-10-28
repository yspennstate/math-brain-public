import json,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
base=Path(r'math-open-problems/reports\fei-2026-10-11')
sup=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
files=[base/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [sup/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((sup/'sources').glob('*.txt'))+list(Path(r'context').glob('*.txt'))
files += [Path(r'BOARD.md'),Path(r'claude\B06\STREAM_NOTES.md')]
files += [Path(r'agents\A096\runs\20261027T055827Z-account04-A096-live-gap-ledger')/n for n in ['REPORT.md','DERIVATION.md','CLAIMS.json']]
files += [Path(r'agents\A029\runs\20261026T213208Z-account04-A029-child-deficit-transport')/n for n in ['REPORT.md','CLAIMS.json']]
files += list((root.parents[1]/'20261023T144415Z-account03-A028-stopping-tree-payment').glob('*.md')) if False else []
receipts=[];excerpts=[]
for p in files:
    if not p.exists():receipts.append({'path':str(p),'status':'MISSING'});continue
    raw=p.read_bytes()
    try:s=raw.decode('utf-8-sig');enc='utf-8-sig'
    except UnicodeDecodeError:s=raw.decode('cp1252');enc='cp1252, explicit fallback after UTF-8 failure'
    receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'encoding':enc,'mode':'full byte/decoding intake; mathematical review limited to locators named in REPORT'})
    needles=('C019','A028','vacuum','cardinality','product','composition','stopping')
    selected=[{'line':i+1,'text':line[:500]} for i,line in enumerate(s.splitlines()) if any(k.lower() in line.lower() for k in needles)][:16]
    excerpts.append({'path':str(p),'selected':selected})
(root/'out'/'SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
(root/'out'/'SOURCE_EXCERPTS.json').write_text(json.dumps(excerpts,indent=2),encoding='utf-8')
print(json.dumps({'source_files':len(receipts),'missing':sum(r.get('status')=='MISSING' for r in receipts),'notice':'machine intake is not a new independent paper audit'}))
