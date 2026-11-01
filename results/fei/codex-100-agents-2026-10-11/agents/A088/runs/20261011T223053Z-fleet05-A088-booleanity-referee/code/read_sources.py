from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
base=Path(r'~')
report=base/'mop_fei100/reports/fei-2026-10-11'
supp=base/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
team=base/'brain_workers/FEI100_20261011'
files=[report/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += list((report/'runs').rglob('REPORT.md'))
files += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]+list((supp/'sources').glob('*'))
files += [supp/'baseline/current-threshold-paper.tex']
files += list((team/'context').glob('*.txt'))+[team/'BOARD.md']
if (team/'claude/B18/STREAM_NOTES.md').exists():files.append(team/'claude/B18/STREAM_NOTES.md')
for i in list(range(31,41))+list(range(66,71)):
    d=team/'agents'/('A%03d'%i)
    files+=list(d.glob('STATUS.md'))
    files += [p for p in d.rglob('*') if p.is_file() and p.suffix in ['.md','.tex','.json','.py'] and 'big' not in p.parts]
rows=[]; extracts=[]
for p in dict.fromkeys(files):
    raw=p.read_bytes()
    try: s=raw.decode('utf-8-sig'); enc='utf-8-sig'
    except UnicodeDecodeError: s=raw.decode('cp1252'); enc='cp1252'
    rows.append(dict(path=str(p),sha256=hashlib.sha256(raw).hexdigest(),bytes=len(raw),encoding=enc,lines=len(s.splitlines())))
    if p.name in ['CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json']:
        ob=json.loads(s)
        def walk(x):
            if isinstance(x,dict):
                if any(v in ['A088','B18','C018','C019','C020','C024'] for v in x.values() if isinstance(v,str)): extracts.append({'path':str(p),'record':x})
                else:
                    for v in x.values():walk(v)
            elif isinstance(x,list):
                for v in x:walk(v)
        walk(ob)
    elif p.suffix=='.txt' or p.name=='FEI_100_agent_research_plan.tex':
        lines=s.splitlines(); hits=[i for i,l in enumerate(lines) if re.search('Boolean|composition|entropy|A088|B18',l,re.I)]
        extracts.append({'path':str(p),'opening':'\n'.join(lines[:70]),'targeted_excerpts':['\n'.join(lines[max(0,i-2):i+4]) for i in hits[:30]]})
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out/SOURCE_MANIFEST.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
(ROOT/'out/CONTEXT_EXCERPTS.json').write_text(json.dumps(extracts,indent=2),encoding='utf-8')
print(json.dumps({'loaded_files':len(rows),'excerpts':len(extracts),'lead_notes_exist':(team/'claude/B18/STREAM_NOTES.md').exists()}))
for x in extracts:
    if 'record' in x: print(json.dumps(x))
