from pathlib import Path
import hashlib,json
OUT=Path(__file__).resolve().parents[1]/'out'
base=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
context=Path(r'~\brain_workers\FEI100_20261011\context')
paths=[base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').glob('*.md')) + list(context.glob('*.txt')) + list((base/'runs').rglob('REPORT.md'))
paths += [supp/'baseline/current-threshold-paper.tex',Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\agents\A056\runs\20261011T214407Z-fleet05-A056-balanced-composition\REPORT.md')]
manifest=[]; excerpts=[]
for p in paths:
    raw=p.read_bytes()
    try: s=raw.decode('utf-8-sig'); enc='utf-8-sig'
    except UnicodeDecodeError: s=raw.decode('cp1252',errors='replace'); enc='cp1252'
    manifest.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'decoded_as':enc,'inspection':'full text loaded; targeted mathematical passages extracted'})
    terms=['prime','composition','product measure','FEI+','weighted threshold','booleanity','counterexample']
    lines=s.splitlines()
    hits=[i for i,line in enumerate(lines) if any(t in line.lower() for t in terms)]
    excerpts.append('\nSOURCE '+str(p)+'\n'+'\n'.join(f'{i+1}: {lines[i]}' for i in hits[:40]))
(OUT/'source_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
(OUT/'source_excerpts.txt').write_text('\n'.join(excerpts),encoding='utf-8')
print('Manifest saved:',len(manifest),'sources')
print('\n'.join(excerpts[-8:])[:18000])
