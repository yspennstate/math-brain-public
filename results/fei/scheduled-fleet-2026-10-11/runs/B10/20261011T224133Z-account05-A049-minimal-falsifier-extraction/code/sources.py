from pathlib import Path
import hashlib, json
RUN=Path(__file__).resolve().parents[1]
root=Path('~/mop_fei100')
report=root/'reports/fei-2026-10-11'
supp=root/'research_pushes/2026-10-11-full-fei-100-agents'
team=Path('~/brain_workers/FEI100_20261011')
paths=[report/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json',
 'OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex','AGENT_ASSIGNMENTS.json']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += sorted((supp/'sources').glob('*'))
paths += sorted((report/'runs').rglob('REPORT.md'))
paths += sorted((team/'context').glob('*.txt'))
paths += [team/'BOARD.md']
for agent in ['A046','A047','A048','A096']:
    paths += sorted((team/'agents'/agent/'runs').rglob('REPORT.md'))
records=[]; excerpts=[]
for path in paths:
    if not path.is_file(): continue
    data=path.read_bytes(); text=data.decode('utf-8-sig',errors='replace')
    records.append({'path':str(path),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),
        'scope':'byte-complete ingestion; relevant locators/excerpts inspected; no full proof audit claimed'})
    if path.suffix=='.txt':
        lines=text.splitlines(); excerpt=lines[:145]
        if 'threshold_paper_38pp' in path.name:
            excerpt += lines[1900:1985]+lines[2195:2260]
        excerpts.append('FILE '+str(path)+'\n'+'\n'.join(excerpt))
    if path.name=='AGENT_ASSIGNMENTS.json':
        obj=json.loads(text)
        def find(o):
            if isinstance(o,dict):
                if o.get('packet_id')=='A049' or o.get('agent_id')=='A049': return o
                for v in o.values():
                    r=find(v)
                    if r: return r
            if isinstance(o,list):
                for v in o:
                    r=find(v)
                    if r: return r
        print('A049 CONTRACT',json.dumps(find(obj)))
lead=team/'claude/B10/STREAM_NOTES.md'
records.append({'path':str(lead),'exists':lead.exists()})
if lead.exists(): print(lead.read_text(encoding='utf-8'))
(RUN/'out/SOURCE_MANIFEST.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
(RUN/'out/PAPER_SCOPE_EXCERPTS.txt').write_text('\n\n'.join(excerpts),encoding='utf-8')
print('SOURCE_MANIFEST',len(records),'files; paper context excerpt saved')
for path in [supp/'COUNTEREXAMPLES.md',supp/'sources/BLOCK_RESTRICTION_IDENTITY_2026-09-18.md']:
    print('\n'+str(path)+'\n'+path.read_text(encoding='utf-8')[:18000])
