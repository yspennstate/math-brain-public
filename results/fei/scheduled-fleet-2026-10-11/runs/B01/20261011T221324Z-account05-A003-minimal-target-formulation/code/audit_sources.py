from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
base=Path(r'~\mop_fei100')
campaign=base/'reports/fei-2026-10-11'
supp=base/'research_pushes/2026-10-11-full-fei-100-agents'
context=Path(r'~\brain_workers\FEI100_20261011\context')
paths=[campaign/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths+=list((campaign/'runs').rglob('REPORT.md'))
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths+=list((supp/'sources').glob('*.md'))+list(context.glob('*.txt'))
paths += [campaign/'source_material/reductions/paper'/x for x in ['forests.tex','restrictions.tex','main.tex']]
team=Path(r'~\brain_workers\FEI100_20261011')
paths += [team/'BOARD.md',team/'agents/A001/runs/20261011T210330Z-account05-A001-quantifier-audit/REPORT.md',team/'agents/A031/runs/20261011T214115Z-account05-A031-convolution-identity/DERIVATION.md']
manifest=[]
ROOT.joinpath('out').mkdir(parents=True,exist_ok=True)
for p in paths:
    b=p.read_bytes(); s=b.decode('utf-8-sig',errors='replace')
    manifest.append(dict(path=str(p),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),lines=len(s.splitlines())))
    if p.suffix=='.txt':
        ROOT.joinpath('out',p.stem+'_numbered.txt').write_text('\n'.join(f'{i+1}: {x}' for i,x in enumerate(s.splitlines())),encoding='utf-8')
ROOT.joinpath('out/SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'sources':len(manifest),'seed_bytes':(supp/'SEED_LEMMAS.md').stat().st_size,'missing_lead_notes':not (team/'claude/B01/STREAM_NOTES.md').exists()}))
for filename,lo,hi in [('threshold_paper_38pp.txt',1190,1260),('threshold_paper_29pp_earlier_version.txt',1,55),('percolation_spectral_pivotal_entropy_30pp.txt',1,100),('percolation_spectral_pivotal_entropy_31pp_other_version.txt',1,85)]:
    lines=(context/filename).read_text(encoding='utf-8',errors='replace').splitlines()
    print(filename, '\n'.join(lines[lo-1:hi]))
