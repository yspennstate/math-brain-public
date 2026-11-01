from pathlib import Path
import json, hashlib, re
root=Path(r'~\brain_workers\FEI100_20261011')
own=root/'agents/A033'
run=own/'runs/20261022T210100Z-fleet03-A033-derivative-hierarchy'
run.mkdir(exist_ok=True)
for sub in ['code','out']: (run/sub).mkdir(exist_ok=True)
prev=own/'runs/20261014T051927Z-fleet05-A033-derivative-hierarchy'
print('CURRENT FILES', [p.name for p in run.iterdir()])
for name in ['REPORT.md','PROOF.md','CLAIMS.json']:
 p=prev/name
 if p.exists(): print('\nPREVIOUS',name,'\n',p.read_text(encoding='utf-8')[:26000])
base=Path(r'math-open-problems/reports\fei-2026-10-11')
supp=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
paths=[base/n for n in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((root/'context').glob('*.txt'))
records=[]
for p in paths:
 if not p.exists(): print('MISSING',p); continue
 raw=p.read_bytes()
 try: s=raw.decode('utf-8-sig'); enc='utf-8-sig'
 except UnicodeDecodeError: s=raw.decode('cp1252'); enc='cp1252'
 lines=s.splitlines()
 hits=[(i+1,l[:500]) for i,l in enumerate(lines) if re.search(r'A033|B07|signed.convolution|atom.cap|quartic|granular|Booleanity|8\.6|^#|^\\(?:section|subsection)',l,re.I)]
 print('\nSOURCE',p.name,'lines',len(lines),'selected',hits[:20])
 records.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'encoding':enc,'lines':len(lines),'selected':hits})
(run/'out/source_read_manifest.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print('SUPP SOURCES', [p.name for p in (supp/'sources').iterdir()])
for p in [root/'agents/A032/LEARNED.md',root/'agents/A079/LEARNED.md',root/'agents/A034/LEARNED.md']:
 print('\nPEER',p, p.read_text(encoding='utf-8')[-12000:])
