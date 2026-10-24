from pathlib import Path
import json, hashlib
BASE=Path(__file__).resolve().parents[1]
OUT=BASE/'out'; OUT.mkdir(exist_ok=True)
campaign=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
context=Path(r'~\brain_workers\FEI100_20261011\context')
files=[campaign/x for x in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']]
files+=list(campaign.glob('*.tex'))
files+=[supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files+=list((supp/'sources').glob('*.md'))+list(context.glob('*.txt'))
files+=[Path(r'~\brain_workers\FEI100_20261011\agents\A086\LEARNED.md'),Path(r'~\brain_workers\FEI100_20261011\agents\A086\WORKLOG.md')]
receipts=[]
for p in files:
    if not p.is_file():
        receipts.append({'path':str(p),'missing':True}); continue
    raw=p.read_bytes()
    try: text=raw.decode('utf-8-sig'); encoding='utf-8-sig'
    except UnicodeDecodeError:
        text=raw.decode('cp1252'); encoding='cp1252-explicit-fallback-after-utf8-failure'
    receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'lines':len(text.splitlines()),'encoding':encoding})
    lines=text.splitlines()
    wanted=[(i+1,s[:260]) for i,s in enumerate(lines) if any(t.lower() in s.lower() for t in ['A086','A095','C020','C024','normaliz','source reference','history admission'])]
    print(str(p), 'bytes',len(raw),'sha256',receipts[-1]['sha256'])
    for i,s in wanted[:5]: print(i,s)
(OUT/'INTAKE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
print('A086 recent run file names:')
own=BASE.parents[1]
for p in sorted((own/'runs').iterdir())[-4:]: print(p.name, [x.name for x in p.iterdir()])
