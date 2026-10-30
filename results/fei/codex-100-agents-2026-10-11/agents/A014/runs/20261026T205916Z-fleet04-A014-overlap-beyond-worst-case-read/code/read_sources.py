from pathlib import Path
import json,hashlib
RUN=Path(__file__).resolve().parents[1]
HOME=Path(r'~')
campaign=HOME/'mop_fei100/reports/fei-2026-10-11'
supp=HOME/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
paths=[HOME/'AGENTS.md',campaign/'EXECUTION_PROTOCOL.json']
paths += [campaign/n for n in ['README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += sorted((supp/'sources').glob('*.md'))
worker=HOME/'brain_workers/FEI100_20261011'
paths += sorted((worker/'context').glob('*.txt'))
paths += [worker/'BOARD.md',worker/'claude/B03/STREAM_NOTES.md',HOME/'<private-repo>/12_cognitive_architecture/scheduled_tasks/README.md']
for r in sorted((RUN.parents[0]).glob('*')):
    if r==RUN:continue
    paths += [p for p in [r/'REPORT.md',r/'CLAIMS.json',r/'PROGRESS.json'] if p.exists()]
for agent,rid in [('A015','20261023T131948Z-fleet03-A015-minterm-barrier-analysis')]:
    base=worker/'agents'/agent/'runs'/rid
    paths += [base/'REPORT.md',base/'CORE_FUSION.md']
for agent in ['A006','A007']:
    base=worker/'agents'/agent
    r=sorted((base/'runs').glob('*'))[-1]
    paths += [base/'STATUS.md',r/'REPORT.md']
records=[];locators=[]
for p in paths:
    data=p.read_bytes();encoding='utf-8-sig'
    try:text=data.decode(encoding)
    except UnicodeDecodeError:
        encoding='cp1252'
        try:text=data.decode(encoding)
        except UnicodeDecodeError:encoding='latin-1';text=data.decode(encoding)
    records.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'lines':len(text.splitlines()),'full_text_read':True,'explicit_read_encoding':encoding})
    if p.parent.name=='context':
        hits=[(i+1,line[:240]) for i,line in enumerate(text.splitlines()) if any(w in line.lower() for w in ['composition identit','overlap','occupation','read-once','normaliz'])]
        locators.append({'source':str(p),'relevant_line_locators':hits[:14],'imported_theorem':None})
(RUN/'out/SOURCES.json').write_text(json.dumps({'sources':records,'paper_locators':locators},indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'full_text_sources_read':len(records),'context_papers':len(locators),'new_paper_theorems_imported':0}))
