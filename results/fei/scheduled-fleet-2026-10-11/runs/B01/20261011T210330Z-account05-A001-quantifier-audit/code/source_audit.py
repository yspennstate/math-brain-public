from pathlib import Path
import hashlib, json, re

RUN = Path(__file__).resolve().parents[1]
REPORTS = Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUPPLEMENT = Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
CONTEXT = Path(r'~\brain_workers\FEI100_20261011\context')
files = [REPORTS / n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex','AGENT_ASSIGNMENTS.json']]
files += list((REPORTS/'runs').rglob('REPORT.md'))
files += list((REPORTS/'source_material'/'reductions'/'paper').glob('*.tex'))
files += [SUPPLEMENT/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((SUPPLEMENT/'sources').glob('*.md'))
files += list(CONTEXT.glob('*.txt'))
files += [SUPPLEMENT/'baseline'/'current-threshold-paper.tex']
files += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md')]
manifest=[]
out=RUN/'out'; out.mkdir(parents=True,exist_ok=True)
for p in files:
    raw=p.read_bytes()
    encoding='utf-8'
    try: content=raw.decode(encoding)
    except UnicodeDecodeError:
        encoding='cp1252'; content=raw.decode(encoding)
    lines=content.splitlines()
    manifest.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),lines=len(lines),encoding=encoding))
    if p.suffix in ['.txt','.tex']:
        (out/(p.stem+'_numbered.txt')).write_text('\n'.join(f'{i+1}: {s}' for i,s in enumerate(lines)),encoding='utf-8')
(out/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(f'Read and hashed {len(manifest)} source files; text normalization is cp1252 where UTF-8 fails.')
print('This is provenance and text extraction, not a proof check.')
