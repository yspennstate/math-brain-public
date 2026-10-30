from pathlib import Path
import json, hashlib, re
R=Path(__file__).resolve().parents[1]
base=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
ctx=Path(r'~\brain_workers\FEI100_20261011\context')
files=[base/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex','AGENT_ASSIGNMENTS.json']]
files += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list((supp/'sources').glob('*'))+list(ctx.glob('*.txt'))
files += list((base/'runs').rglob('REPORT.md'))
files += list((base/'verification'/'B09_interval_repair_20261011').glob('*'))
rows=[]; excerpts=[]
for p in files:
    if not p.is_file(): continue
    raw=p.read_bytes(); s=raw.decode('utf-8-sig',errors='replace'); lines=s.splitlines()
    rows.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'lines':len(lines)})
    selected=set()
    for i,l in enumerate(lines):
        if re.search(r'A083|B17|C018|C019|C020|C024|interval|quotient|Theorem 1\.[13]|Proposition 5\.5|Corollary 7\.2|composition identities',l,re.I):
            selected.update(range(max(0,i-2),min(len(lines),i+5)))
    excerpts.append('\nSOURCE '+str(p)+'\n'+'\n'.join(f'{i+1}: {lines[i]}' for i in sorted(selected)))
(R/'out').mkdir(exist_ok=True)
(R/'out/source_inventory.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
(R/'out/source_reading.txt').write_text('\n'.join(excerpts),encoding='utf-8')
print(json.dumps({'read_files':len(rows),'bytes':sum(r['bytes'] for r in rows),'inventory':'out/source_inventory.json','excerpts':'out/source_reading.txt'}))
