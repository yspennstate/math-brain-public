from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
report=Path('~/mop_fei100/reports/fei-2026-10-11')
supp=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
context=Path('~/brain_workers/FEI100_20261011/context')
files=[report/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [supp/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += list(context.glob('*.txt'))+list((supp/'sources').glob('*.md'))+list((report/'runs').rglob('REPORT.md'))
manifest=[]; excerpts=[]
for f in files:
    b=f.read_bytes(); s=b.decode('utf-8',errors='replace'); lines=s.splitlines()
    manifest.append({'path':str(f),'sha256':hashlib.sha256(b).hexdigest(),'lines':len(lines),'read_scope':'complete text scanned; relevant locators extracted'})
    chosen=[]
    for i,line in enumerate(lines):
        if any(w.lower() in line.lower() for w in ['A084','B17','biased restriction','product-biased','Maassen','continuum','uniform over','Theorem 7.1','Theorem 3.1']):
            chosen.extend(range(max(0,i-2),min(len(lines),i+7)))
    excerpts.append('\nSOURCE '+str(f)+'\n'+'\n'.join(f'{i+1}: {lines[i]}' for i in sorted(set(chosen))))
(root/'out').mkdir(exist_ok=True)
(root/'out'/'SOURCE_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(root/'out'/'SOURCE_EXCERPTS.txt').write_text('\n'.join(excerpts),encoding='utf-8')
print('Read',len(files),'source texts; saved hashes and relevant excerpts.')
