from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
REPORTS=Path(r'~\mop_fei100\reports\fei-2026-10-11')
SUPPLEMENT=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
CONTEXT=Path(r'~\brain_workers\FEI100_20261011\context')
paths=[REPORTS/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += list((REPORTS/'runs').rglob('REPORT.md'))
paths += [SUPPLEMENT/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((SUPPLEMENT/'sources').glob('*.md'))
paths += list(CONTEXT.glob('*.txt'))
paths += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md'),Path(r'~\brain_workers\FEI100_20261011\claude\B06\STREAM_NOTES.md')]
manifest=[]
for p in paths:
    b=p.read_bytes()
    try: s=b.decode('utf-8'); encoding='utf-8'
    except UnicodeDecodeError: s=b.decode('cp1252'); encoding='cp1252'
    manifest.append(dict(path=str(p),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),encoding=encoding))
(ROOT/'out/source_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
for filename,lo,hi in [('threshold_paper_38pp.txt',1948,2045),('threshold_paper_38pp.txt',2543,2640),('percolation_spectral_pivotal_entropy_30pp.txt',2115,2190)]:
    s=(CONTEXT/filename).read_bytes().decode('cp1252').splitlines()
    print(filename,lo,hi)
    print('\n'.join(f'{i+1}: {s[i]}' for i in range(lo-1,min(hi,len(s)))))
plan=(REPORTS/'FEI_100_agent_research_plan.tex').read_text(encoding='utf-8').splitlines()
print('A030 contract'); print('\n'.join(plan[695:702]))
packets=json.loads((REPORTS/'PACKET_STATUS.json').read_text(encoding='utf-8'))
print('A030 packet'); print(json.dumps([x for x in packets['packets'] if x['packet_id']=='A030'],indent=2))
print('source files hashed',len(manifest))
