from pathlib import Path
import hashlib,json
root=Path(r'~/brain_workers/FEI100_20261011')
run=root/'agents/A070/runs/20261021T173219Z-fleet03-A070-analytic-route-referee'
(run/'out').mkdir(parents=True,exist_ok=True)
base=Path(r'~/mop_fei100')
report=base/'reports/fei-2026-10-11'
supp=base/'research_pushes/2026-10-11-full-fei-100-agents'
paths=[report/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths+=list((supp/'sources').glob('*'))
paths+=list((root/'context').glob('*.txt'))
paths+=[root/'BOARD.md',root/'claude/B14/STREAM_NOTES.md',Path(r'~/AGENTS.md'),Path(r'~/brain_workers/PRIMARY_DIRECTIVE.md')]
paths+=list((root/'agents/A070/runs').glob('*/REPORT.md'))
paths+=list((report/'runs/B14').glob('*/REPORT.md'))
sources=[]; excerpts=[]
for p in paths:
 if not p.is_file() or p.suffix.lower() not in ['.md','.tex','.txt','.json']:continue
 raw=p.read_bytes(); enc='utf-8-sig'
 try:s=raw.decode(enc)
 except UnicodeDecodeError:enc='cp1252';s=raw.decode(enc)
 lines=s.splitlines()
 sources.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),encoding=enc))
 hits=[(i+1,x) for i,x in enumerate(lines) if any(k in x.lower() for k in ['a070','cyclic','11.51','proposition 8.6','lemma 2.1','same reference','c024'])]
 excerpts.append(dict(path=str(p),lines=len(lines),hits=hits[:16]))
(run/'out/SOURCE_MANIFEST.json').write_text(json.dumps(sources,indent=2),encoding='utf-8')
(run/'out/SOURCE_EXCERPTS.json').write_text(json.dumps(excerpts,indent=2),encoding='utf-8')
for row in excerpts:
 print(row['path'],row['lines'],'lines')
 for i,x in row['hits'][:3]:print(i,x[:220])
