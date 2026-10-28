from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
home=Path('~');campaign=home/'mop_fei100/reports/fei-2026-10-11';push=home/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents';team=home/'brain_workers/FEI100_20261011'
paths=[campaign/x for x in ('README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json')]
paths+=list(campaign.glob('*.tex'))
paths +=[push/x for x in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md')]
paths+=list((push/'sources').glob('*.md'))
paths+=list((team/'context').glob('*.txt'))
paths += [team/'BOARD.md',team/'claude/B01/STREAM_NOTES.md',home/'AGENTS.md']
paths += [team/'agents/A052/runs/20261023T142511Z-account03-A052-critical-source-structure'/x for x in ('REPORT.md','CLAIMS.json','RIGIDITY_REVIEW.md')]
out=[]
for p in paths:
 if not p.is_file():out.append({'path':str(p),'missing':True});continue
 b=p.read_bytes();encoding='utf-8-sig'
 try:s=b.decode(encoding)
 except UnicodeDecodeError:
  encoding='cp1252';s=b.decode(encoding)
 lines=s.splitlines();hits=[]
 for i,line in enumerate(lines):
  if any(k in line.lower() for k in ('a005','c019','composition','restriction','noncircular','least-dimensional','rigidity')):hits.append({'line':i+1,'text':line[:450]})
 out.append({'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'lines':len(lines),'encoding':encoding,'read_scope':'Full file loaded; targeted lines inspected, no new full-paper audit','excerpts':hits[:8]})
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
for item in out:
 print(Path(item['path']).name,item.get('bytes','MISSING'))
 for hit in item.get('excerpts',[])[:2]:print(' ',hit['line'],hit['text'][:260])
