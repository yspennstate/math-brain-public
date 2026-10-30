from pathlib import Path
import hashlib,json
RUN=Path(__file__).resolve().parents[1]
P=Path(r'~\mop_fei100\reports\fei-2026-10-11')
S=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
C=Path(r'~\brain_workers\FEI100_20261011\context')
paths=[P/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']]
paths += list((P/'runs').rglob('REPORT.md'))+list((P/'source_material/reductions/paper').glob('*.tex'))
paths += [S/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]+list((S/'sources').glob('*.md'))+list(C.glob('*.txt'))
paths += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md')]
paths += list(Path(r'~\brain_workers\FEI100_20261011\agents\A001\runs').rglob('REPORT.md'))
manifest=[]
for p in paths:
    raw=p.read_bytes()
    try: content=raw.decode('utf-8'); enc='utf-8'
    except UnicodeDecodeError: content=raw.decode('cp1252'); enc='cp1252'
    manifest.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),lines=len(content.splitlines()),encoding=enc))
    if p.suffix=='.txt' or p.name=='main.tex':
        (RUN/'out'/(p.stem+'_numbered.txt')).write_text('\n'.join(f'{i+1}: {s}' for i,s in enumerate(content.splitlines())),encoding='utf-8')
    if p.name in ['PACKET_STATUS.json','AGENT_ASSIGNMENTS.json']:
        obj=json.loads(content)
        def walk(x):
            if isinstance(x,dict):
                if any(v=='A002' for v in x.values() if isinstance(v,str)): print(json.dumps(x,indent=2))
                for v in x.values(): walk(v)
            elif isinstance(x,list):
                for v in x: walk(v)
        walk(obj)
(RUN/'out/SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print('Source bytes loaded and hashed:',len(manifest),'files. Mathematical inspection is limited to reported locators.')
