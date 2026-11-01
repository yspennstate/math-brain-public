from pathlib import Path
import hashlib,json,re
root=Path(__file__).resolve().parents[1]
report=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
ctx=Path(r'~\brain_workers\FEI100_20261011\context')
paths=[report/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((supp/'sources').glob('*'))+list(ctx.glob('*.txt'))+list((report/'runs').rglob('REPORT.md'))
records=[]
for p in paths:
    raw=p.read_bytes(); txt=raw.decode('utf-8',errors='replace'); lines=txt.splitlines()
    needles=r'A035|B07|convolution|min.entropy|H_inf|H.inf|cancellation|signed|singularity'
    hits=[(i+1,line[:500]) for i,line in enumerate(lines) if re.search(needles,line,re.I)]
    records.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),lines=len(lines),relevant_lines=hits))
    print(p.name,len(raw),'bytes',len(hits),'relevant lines')
    if p.suffix=='.json':
        data=json.loads(txt)
        def visit(x):
            if isinstance(x,dict):
                if x.get('packet_id')=='A035' or x.get('native_stream')=='B07' or x.get('claim_id') in ['C018','C019','C020','C022']: print(json.dumps(x,ensure_ascii=False))
                else:
                    for v in x.values(): visit(v)
            elif isinstance(x,list):
                for v in x:visit(v)
        visit(data)
(root/'out').mkdir(exist_ok=True)
(root/'out'/'source_manifest.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
