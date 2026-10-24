from pathlib import Path
import hashlib, json

RUN=Path(__file__).resolve().parents[1]
ROOT=Path(r'~\mop_fei100')
TEAM=Path(r'~\brain_workers\FEI100_20261011')
report=ROOT/'reports/fei-2026-10-11'
supp=ROOT/'research_pushes/2026-10-11-full-fei-100-agents'
files=[report/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex','AGENT_ASSIGNMENTS.json']]
files += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((supp/'sources').glob('*.md'))
files += list((report/'runs').rglob('REPORT.md'))
files += list((TEAM/'context').glob('*.txt'))
files += [TEAM/'BOARD.md',TEAM/'claude/B05/STREAM_NOTES.md']
for agent in ['A023','A041','A042','A056','A057','A096','A091']:
    files += list((TEAM/'agents'/agent/'runs').rglob('REPORT.md'))
    files += list((TEAM/'agents'/agent/'runs').rglob('CLAIMS.json'))
files += list((TEAM/'agents/A057/runs').rglob('NEXT_HANDOFF.md'))
files += [report/'source_material/reductions/paper/biased.tex']
receipts=[]; excerpts=[]
keys=['normaliz','composition','mismatch','rebate','dictator','deterministic','biasfull:hplus','A024','Universal bridge']
for p in files:
    if not p.exists(): continue
    raw=p.read_bytes()
    try: s=raw.decode('utf-8-sig'); encoding='utf-8-sig'
    except UnicodeDecodeError: s=raw.decode('cp1252'); encoding='cp1252'
    lines=s.splitlines()
    receipts.append({'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'encoding':encoding,'scope':'full file ingestion; mathematical examination focused on relevant normalization, restriction and composition sections'})
    excerpts.append('\nFILE '+str(p))
    chosen=set(range(min(18,len(lines))))
    for i,line in enumerate(lines):
        if any(k.lower() in line.lower() for k in keys):
            chosen.update(range(max(0,i-2),min(len(lines),i+4)))
    excerpts.extend(f'{i+1}: {lines[i]}' for i in sorted(chosen))
(RUN/'out').mkdir(exist_ok=True)
(RUN/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
(RUN/'out/SOURCE_EXCERPTS.txt').write_text('\n'.join(excerpts),encoding='utf-8')
print(json.dumps({'files_read':len(receipts),'lead_notes_exists':(TEAM/'claude/B05/STREAM_NOTES.md').exists(),'source_receipts':str(RUN/'out/SOURCE_RECEIPTS.json')}))
