from pathlib import Path
import hashlib,json,re
BASE=Path(r'~\brain_workers\FEI100_20261011')
REP=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUP=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
RUN=Path(__file__).resolve().parents[1]
paths=[REP/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths+=list((REP/'runs').rglob('REPORT.md'))
paths += [SUP/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths+=list((SUP/'sources').glob('*.md'))+list((BASE/'context').glob('*.txt'))
paths += [BASE/'BOARD.md',BASE/'claude/B19/STREAM_NOTES.md',REP/'source_material/reductions/paper/forests.tex']
for agent in ['A006','A007','A086','A087','A088','A089','A090']:
    paths+=list((BASE/'agents'/agent/'runs').rglob('REPORT.md'))
    if agent in ['A006','A007','A086']: paths+=list((BASE/'agents'/agent/'runs').rglob('CLAIMS.json'))
paths+=list((BASE/'agents/A086/runs').rglob('JOINT_CODE_REVIEW.md'))
manifest=[]; excerpts=[]
for path in paths:
    raw=path.read_bytes()
    try: s=raw.decode('utf-8-sig'); enc='utf-8-sig'
    except UnicodeDecodeError: s=raw.decode('cp1252'); enc='cp1252'
    manifest.append({'path':str(path),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'encoding':enc})
    if path.suffix=='.txt':
        excerpts.append('\nSOURCE '+str(path)+'\n'+s[:6500])
        for match in re.finditer(r'(?i)joint witness|scope of the refinement|shared.data|conditional entropy|root entropy|pivotal.bound',s):
            excerpts.append(s[max(0,match.start()-350):match.start()+1600])
    elif 'sources' in path.parts or 'runs' in path.parts and path.name=='REPORT.md' and 'agents' not in path.parts:
        excerpts.append('\nSOURCE '+str(path)+'\n'+s[:4500])
    elif path.name=='FEI_100_agent_research_plan.tex':
        for match in re.finditer(r'Endpoint J|A094|A006|A007|eq:residual|eq:forest',s): excerpts.append(s[max(0,match.start()-200):match.start()+2000])
    elif path.name=='PACKET_STATUS.json':
        excerpts.append(json.dumps([x for x in json.loads(s)['packets'] if x['packet_id'] in ['A006','A007','A086','A094']],indent=2))
(RUN/'out/SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(RUN/'out/INTAKE_EXCERPTS.txt').write_text('\n'.join(excerpts),encoding='utf-8')
print(json.dumps({'source_count':len(manifest),'excerpts_bytes':(RUN/'out/INTAKE_EXCERPTS.txt').stat().st_size}))
