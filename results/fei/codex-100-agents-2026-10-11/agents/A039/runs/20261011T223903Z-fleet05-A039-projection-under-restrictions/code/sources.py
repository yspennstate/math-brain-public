from pathlib import Path
import hashlib,json,re
run=Path(__file__).resolve().parents[1]
base=Path('~/mop_fei100/reports/fei-2026-10-11')
sup=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
team=Path('~/brain_workers/FEI100_20261011')
paths=[base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex','AGENT_ASSIGNMENTS.json']]
paths += [sup/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += sorted((sup/'sources').glob('*.md'))
paths += sorted((base/'runs').glob('**/REPORT.md'))
paths += sorted((team/'context').glob('*.txt'))
paths += [team/'BOARD.md']
for agent in ['A037','A038']:
    paths+=sorted((team/'agents'/agent/'runs').glob('**/REPORT.md'))
    paths+=sorted((team/'agents'/agent/'runs').glob('**/CLAIMS.json'))
paths += [team/'agents/A038/runs/20261011T221733Z-fleet05-A038-occupancy-term-audit/out/sources/K_OCC_DEFINITION.md']
receipts=[]; excerpts=[]
for p in paths:
    data=p.read_bytes(); text=data.decode('utf-8',errors='replace'); lines=text.splitlines()
    receipts.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'scope':'read-only full-file load; relevant mathematical interfaces inspected, not full theorem audit'})
    if p.name in ['PACKET_STATUS.json','AGENT_ASSIGNMENTS.json']:
        obj=json.loads(text)
        def visit(x):
            if isinstance(x,dict):
                if any(v=='A039' for v in x.values() if isinstance(v,str)): excerpts.append(str(p)+'\n'+json.dumps(x,indent=2))
                else:
                    for v in x.values(): visit(v)
            elif isinstance(x,list):
                for v in x: visit(v)
        visit(obj)
    elif p.suffix=='.txt':
        hits=[i for i,s in enumerate(lines) if re.search(r'Proposition 5\.5|Lemma 2\.1 \(Refinement|Gibbs.*subprobability|scope of the refinement',s,re.I)]
        excerpts.append(str(p)+'\n'+'\n'.join('\n'.join(lines[max(0,i-3):i+28]) for i in hits[:3]))
    elif p.parent.name=='sources' and p.name!='K_OCC_DEFINITION.md':
        hits=[s for s in lines if re.search(r'projection|physical restriction|KL|erasure|conditioning|monotonic',s,re.I)]
        excerpts.append(str(p)+'\n'+'\n'.join(hits[:10]))
(run/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
(run/'out/SOURCE_INTERFACE_EXCERPTS.txt').write_text('\n\n'.join(excerpts),encoding='utf-8')
lead=team/'claude/B08/STREAM_NOTES.md'
print(json.dumps({'read_only_files':len(paths),'B08_lead_exists':lead.exists()}))
print('\n'.join(excerpts[:2])[:6000])
