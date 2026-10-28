from pathlib import Path
import json, hashlib
BASE=Path(r'math-open-problems/reports\fei-2026-10-11')
SUP=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
CTX=Path(r'context')
OWN=Path(__file__).parent
RUN=OWN/'runs/20261011T214745Z-account05-A081-dependency-certificates'
(RUN/'code').mkdir(parents=True,exist_ok=True)
(RUN/'out').mkdir(exist_ok=True)
files=[*BASE.glob('*.md'),*BASE.glob('*.json'),*BASE.glob('*.tex'),*BASE.glob('runs/**/*'),*SUP.glob('*.md'),*SUP.glob('sources/**/*'),*CTX.glob('*.txt')]
manifest=[]
for p in files:
    if not p.is_file() or p.suffix not in ('.md','.json','.tex','.txt','.py'): continue
    raw=p.read_bytes(); txt=raw.decode('utf-8-sig',errors='replace')
    manifest.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'lines':len(txt.splitlines())})
(RUN/'out/source_inventory.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
reg=json.loads((BASE/'CLAIM_REGISTRY.json').read_text(encoding='utf-8-sig'))
print('REGISTRY FULL',json.dumps(reg,ensure_ascii=False,indent=2))
ps=json.loads((BASE/'PACKET_STATUS.json').read_text(encoding='utf-8-sig'))
print('PACKET STRUCTURE', list(ps))
for k,v in ps.items():
    if isinstance(v,list):
        for x in v:
            if isinstance(x,dict) and 'A081' in json.dumps(x): print('PACKET',json.dumps(x,indent=2))
print('INVENTORY',json.dumps(manifest,indent=2))
