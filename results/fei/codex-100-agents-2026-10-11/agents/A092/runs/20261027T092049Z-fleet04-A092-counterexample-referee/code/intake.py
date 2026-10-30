from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
P=Path(r'~\brain_workers\FEI100_20261011')
C=Path(r'math-open-problems/reports\fei-2026-10-11')
S=Path(r'math-open-problems/research_pushes\2026-10-11-full-fei-100-agents')
files=[Path(r'~\AGENTS.md')]
files += [C/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [S/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += [f for f in (S/'sources').rglob('*') if f.is_file() and f.suffix in ('.md','.txt','.tex','.json')]
files += list((P/'context').glob('*.txt'))+[P/'BOARD.md',P/'claude/B19/STREAM_NOTES.md']
files += [f for f in (P/'agents/A092').glob('*.md')]
files += list((P/'agents/A092/runs').glob('*/REPORT.md'))
for agent,run in [('A071','20261027T050628Z-fleet04-A071-search-space-design'),('A080','20261027T015619Z-fleet04-A080-universal-counterexample-standard')]:
    files += [P/'agents'/agent/'runs'/run/n for n in ['PROOF.md','REPORT.md','CLAIMS.json','PROGRESS.json']]
files += list((C/'runs/B19').glob('*/REPORT.md'))[-2:]
files += [Path(r'~\.claude\compute\compute_state.json'),Path(r'~\.claude\compute\interventions.tsv')]
records=[]
for f in dict.fromkeys(files):
    if not f.exists():
        records.append(dict(path=str(f),status='MISSING'));continue
    b=f.read_bytes()
    try: t=b.decode('utf-8-sig'); enc='utf-8-sig'
    except UnicodeDecodeError: t=b.decode('cp1252'); enc='cp1252 (source export)'
    rec=dict(path=str(f),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),encoding=enc)
    if f.suffix=='.txt':
        words=('composition','spectral','entropy','singular','Theorem')
        rec['locators']=[dict(line=i+1,text=l[:160]) for i,l in enumerate(t.splitlines()) if any(w in l for w in words)][:8]
    if f.name=='interventions.tsv': rec['tail']=t.splitlines()[-3:]
    records.append(rec)
(R/'out/SOURCE_INTAKE.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(read=len(records),missing=[x['path'] for x in records if x.get('status')=='MISSING'],papers=[x for x in records if x['path'].endswith('.txt')]),ensure_ascii=True))
