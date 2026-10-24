from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
base=Path('~')
camp=base/'mop_fei100/reports/fei-2026-10-11'
push=base/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
team=base/'brain_workers/FEI100_20261011'
files=[camp/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [push/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((push/'sources').glob('*.md'))+list((push/'sources').glob('*.txt'))
files += list((team/'context').glob('*.txt'))
files += [team/'BOARD.md',team/'claude/B05/STREAM_NOTES.md',base/'AGENTS.md']
files += list((team/'agents/A025/runs').glob('*/REPORT.md'))
files += [team/'agents/A021/runs/20261014T075029Z-account05-A021-rare-core-asymptotics'/n for n in ['REPORT.md','DERIVATION.md','CLAIMS.json']]
files += list((team/'claude/B05/runs').glob('*/REPORT.md'))
files += list((camp/'runs/B05').glob('*/REPORT.md'))
out=[]
for f in files:
    b=f.read_bytes()
    try: s=b.decode('utf-8-sig'); enc='utf-8-sig'
    except UnicodeDecodeError: s=b.decode('cp1252'); enc='cp1252 (source bytes are not UTF-8)'
    keys=('A025','B05','C018','C019','C024','shared-data','Shared data','composition','odd-face')
    hits=[{'line':i+1,'text':l[:180]} for i,l in enumerate(s.splitlines()) if any(k in l for k in keys)]
    out.append({'path':str(f),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'encoding':enc,'relevant_locators':hits[:20]})
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({'files_read':len(out),'non_utf8_sources':[x['path'] for x in out if x['encoding'].startswith('cp')],'primary_use':'A021 final owner section, own prior proof, protocol'}))
