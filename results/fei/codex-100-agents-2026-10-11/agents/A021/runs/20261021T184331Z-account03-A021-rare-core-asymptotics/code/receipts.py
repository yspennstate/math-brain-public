from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
base=Path('~'); team=base/'brain_workers/FEI100_20261011'
camp=base/'mop_fei100/reports/fei-2026-10-11'; push=base/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
files=[camp/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [push/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += [f for f in (push/'sources').rglob('*') if f.is_file() and f.suffix in ('.txt','.md','.tex','.json')]
files += list((team/'context').glob('*.txt'))
files += [team/'BOARD.md',team/'claude/B05/STREAM_NOTES.md',base/'AGENTS.md']
files += list((team/'claude/B05/runs').glob('*/REPORT.md'))+list((camp/'runs/B05').glob('*/REPORT.md'))
files += list((team/'agents/A021/runs').glob('*/REPORT.md'))
files += [team/'agents/A021/runs/20261014T075029Z-account05-A021-rare-core-asymptotics'/n for n in ['DERIVATION.md','CLAIMS.json']]
files += [team/'agents/A025/runs/20261021T162308Z-account03-A025-rare-event-counterfamily'/n for n in ['REPORT.md','PROOF.md','CLAIMS.json','code/check.py']]
rows=[]
for f in files:
    b=f.read_bytes()
    try: s=b.decode('utf-8-sig'); enc='utf-8-sig'
    except UnicodeDecodeError: s=b.decode('cp1252'); enc='cp1252 source'
    hits=[{'line':i+1,'text':l[:220]} for i,l in enumerate(s.splitlines()) if any(k.lower() in l.lower() for k in ('A021','A025','B05','C019','C024','8.9','8.10','composition','point','rare','odd-face'))]
    rows.append({'path':str(f),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'encoding':enc,'locators':hits[:30]})
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps({'source_files':len(rows),'primary_mathematical_sources':'A021 old final owner section; A025 PROOF entire continuation; all new claims reconstructed in PROOF.md'}))
