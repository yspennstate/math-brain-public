from pathlib import Path
import json,hashlib

ROOT=Path(__file__).resolve().parents[1]
AGENT=ROOT.parents[1]
P=Path(r'~\mop_fei100\reports\fei-2026-10-11')
S=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
CTX=Path(r'~\brain_workers\FEI100_20261011\context')
def digest(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
source=[]
paths=[P/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex','AGENT_ASSIGNMENTS.json']]
paths += [S/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((S/'sources').glob('*.md'))+list(CTX.glob('*.txt'))+list((P/'runs').rglob('REPORT.md'))
paths += [AGENT.parents[1]/'BOARD.md']
paths += list((ROOT/'out'/'sources').glob('*'))
peer=AGENT.parent
for name in ['A036','A037']:
    paths += list((peer/name/'runs').glob('*/REPORT.md'))
excerpts=[]
for p in paths:
    if not p.exists():continue
    text=p.read_text(encoding='utf-8-sig',errors='replace')
    source.append(digest(p))
    if p.name=='FEI_100_agent_research_plan.tex' or p.suffix=='.txt' or ('runs' in p.parts and str(P) in str(p)):
        lines=text.splitlines()
        selected=set()
        for i,l in enumerate(lines):
            if any(w.lower() in l.lower() for w in ['K_occ','occupancy','nonempty','relative entropy','KL credit','normalization']):
                selected.update(range(max(0,i-2),min(len(lines),i+5)))
        excerpts.append('\nSOURCE '+str(p)+'\n'+'\n'.join(f'{i+1}: {lines[i]}' for i in sorted(selected)))
(ROOT/'out'/'SOURCE_RECEIPTS.json').write_text(json.dumps(source,indent=2)+'\n',encoding='utf-8')
(ROOT/'out'/'SOURCE_INTERFACE_EXCERPTS.txt').write_text('\n'.join(excerpts),encoding='utf-8')
protocol=json.loads((P/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
claims=json.loads((ROOT/'CLAIMS.json').read_text(encoding='utf-8'))
for c in claims:
    value={'statement':c['exact_statement'],'hypotheses':c['hypotheses']}
    c['statement_sha256']=hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest()
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
(ROOT/'CLAIMS.json').write_text(json.dumps(claims,indent=2)+'\n',encoding='utf-8')
progress=json.loads((ROOT/'PROGRESS.json').read_text(encoding='utf-8'))
expected=[x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']]
assert set(progress)==set(expected)
assert progress==json.loads((ROOT/'PACKET_DELTA.json').read_text(encoding='utf-8'))
assert progress['packet_ids']==['A038']
for p in ROOT.rglob('*'):
    if p.is_file():assert p.stat().st_size<20*1024*1024
manifest=[digest(p) for p in ROOT.rglob('*') if p.is_file() and p.name!='ARTIFACT_SHA256.json']
(ROOT/'out'/'ARTIFACT_SHA256.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'schema_check':'PASS','claim_hash':claims[0]['statement_sha256'],'artifacts_hashed':len(manifest),'sources_hashed':len(source),'all_files_under_20MB':True}))
