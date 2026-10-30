from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];A030=ROOT.parents[1]
campaign=Path(r'math-open-problems/reports\fei-2026-10-11')
supp=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
team=Path(r'~\brain_workers\FEI100_20261011')
paths=[Path(r'~\AGENTS.md'),Path(r'~\<private-repo>\12_cognitive_architecture\scheduled_tasks\README.md'),Path(r'~\brain_workers\PRIMARY_DIRECTIVE.md')]
paths += [campaign/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').glob('*'))
paths += list((team/'context').glob('*.txt'))
paths += [team/'BOARD.md',team/'claude/B06/STREAM_NOTES.md']
paths += [A030/'runs/20261014T062839Z-fleet05-A030-restriction-plateau-tests'/n for n in ['REPORT.md','PROOF.md','CLAIMS.json','code/check.py']]
paths += [A030/'runs/20261013T212321Z-fleet05-A030-restriction-plateau-tests/code/check.py',A030/'runs/20261014T032502Z-fleet05-A030-restriction-plateau-tests/code/check.py']
paths += [team/'agents'/a/'runs'/r/f for a,r,f in [('A028','20261014T051435Z-fleet05-A028-stopping-tree-payment','REPORT.md'),('A029','20261014T055200Z-fleet05-A029-child-deficit-transport','REPORT.md'),('A087','20261014T045317Z-fleet05-A087-restriction-referee','CLAIMS.json')]]
receipts=[];excerpts=[]
for p in paths:
    if not p.is_file():
        receipts.append({'path':str(p),'status':'NOT_PRESENT'});continue
    raw=p.read_bytes()
    try:text=raw.decode('utf-8-sig');enc='utf-8-sig'
    except UnicodeDecodeError:text=raw.decode('cp1252');enc='cp1252'
    loc=[];lines=text.splitlines()
    for i,line in enumerate(lines):
        if any(k in line for k in ['A030','B06','C019','C024','Proposition 8.6','Theorem 1.1 (Crossing','FIRST UNSUPPORTED','First unsupported']):
            loc.append(i+1)
            if len(excerpts)<100:excerpts.append(f'{p.name}:{i+1}: {line[:500]}')
    receipts.append({'path':str(p),'status':'READ_ONLY_BYTES_LOADED','sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':enc,'target_line_locators':loc[:80]})
# Read prior central B06 report records without mutating any source.
earlier=campaign/'runs/B06'
if earlier.is_dir():
    candidates=sorted(earlier.glob('*/REPORT.md'))[:2]
    for p in candidates:
        raw=p.read_bytes();receipts.append({'path':str(p),'status':'EARLIER_B06_REPORT_READ','sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)})
        excerpts.append(raw.decode('utf-8-sig',errors='replace')[:1200])
(ROOT/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
(ROOT/'out/SOURCE_EXCERPTS.txt').write_text('\n'.join(excerpts)+'\n',encoding='utf-8')
print(json.dumps({'source_files':len(receipts),'missing':[r['path'] for r in receipts if r['status']=='NOT_PRESENT'],'total_bytes_read':sum(r.get('bytes',0) for r in receipts),'paper_text_encoding':'explicit utf-8-sig, fallback cp1252; source bytes unchanged'},indent=2))
print('Lean runtime evidence:')
lr=json.loads((ROOT/'out/LEAN.json').read_text(encoding='utf-8'))
print(json.dumps({k:v for k,v in lr.items() if any(s in k.lower() for s in ['output','error','seconds','timeout','compiler','return'])},indent=2)[:2800])
