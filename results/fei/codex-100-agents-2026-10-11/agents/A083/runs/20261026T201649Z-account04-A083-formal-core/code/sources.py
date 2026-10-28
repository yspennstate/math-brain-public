from pathlib import Path
import json,hashlib,re
R=Path(__file__).resolve().parents[1]
home=Path('~')
base=home/'mop_fei100/reports/fei-2026-10-11'
supp=home/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
worker=home/'brain_workers/FEI100_20261011'
paths=[base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').glob('*.txt')) + list((supp/'sources').glob('*.md'))
paths += list((worker/'context').glob('*.txt'))
paths += [worker/'BOARD.md',worker/'claude/B17/STREAM_NOTES.md',home/'AGENTS.md']
peer=worker/'agents/A097/runs/20261023T143952Z-account03-A097-cross-route-transfer'
paths += [peer/x for x in ['PROOF.md','REPORT.md','CLAIMS.json','code/check.py']]
prior=R.parent/'20261023T124306Z-account03-A083-formal-core'
paths += [prior/x for x in ['REPORT.md','CLAIMS.json','REVIEW.md']]
out=[]; excerpts=[];encoding_notes=[]
for p in paths:
 if not p.exists():
  out.append({'path':str(p),'status':'MISSING'});continue
 raw=p.read_bytes(); encoding='utf-8-sig'
 try: s=raw.decode(encoding)
 except UnicodeDecodeError as error:
  # Legacy manuscript text, read-only: retain byte hash and explicit decoder.
  # Mathematical proof premises must never silently switch decoding.
  if p.parent==peer: raise
  encoding='cp1252'; s=raw.decode(encoding)
  encoding_notes.append({'path':str(p),'utf8_error':str(error),'read_only_decoder':encoding,'rewritten':False})
 out.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':encoding,'lines':len(s.splitlines()),'role':'proof premise' if p.parent==peer else 'orientation/read-only baseline; not newly independently audited'})
 # Exact relevant lines only; surrounding manuscript context stays on disk.
 if p.suffix=='.json':
  obj=json.loads(s)
  def walk(x):
   if isinstance(x,dict):
    if any(isinstance(v,str) and ('A083'==v or v in ('C018','C019','C020','C024','B17')) for v in x.values()):
     excerpts.append({'path':str(p),'record':x})
    else:
     for v in x.values(): walk(v)
   elif isinstance(x,list):
    for v in x:walk(v)
  walk(obj)
 elif p.parent==worker/'context':
  hits=[(i+1,line) for i,line in enumerate(s.splitlines()) if re.search('composition|cross.entropy|stopping|shared.data|reference distribution',line,re.I)]
  excerpts.append({'path':str(p),'relevant_lines':hits[:18]})
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
(R/'out/SOURCE_ENCODING_NOTE.json').write_text(json.dumps(encoding_notes,indent=2)+'\n',encoding='utf-8')
(R/'out/BASELINE_EXCERPTS.json').write_text(json.dumps(excerpts,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'source_files':len(out),'missing':[v['path'] for v in out if v.get('status')=='MISSING'],'relevant_record_files':len(excerpts)}))
