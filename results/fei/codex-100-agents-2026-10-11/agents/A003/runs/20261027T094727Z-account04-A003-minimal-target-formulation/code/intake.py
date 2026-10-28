from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parents[1]
base=Path('math-open-problems/reports/fei-2026-10-11')
supp=Path('math-open-problems/research_pushes/2026-10-11-full-fei-100-agents')
ctx=Path('context')
paths=[base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
paths += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += sorted(ctx.glob('*.txt'))
paths += [Path('~/AGENTS.md'),Path('BOARD.md'),Path('claude/B01/STREAM_NOTES.md')]
paths += sorted((R.parent/'20261023T144012Z-account03-A003-minimal-target-formulation').glob('*.md'))
receipts=[]; excerpts=[]
for p in paths:
    if not p.exists():
        receipts.append({'path':str(p),'status':'MISSING'}); continue
    data=p.read_bytes(); s=data.decode('utf-8-sig',errors='replace'); lines=s.splitlines()
    receipts.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'scope':'full UTF8 load; targeted excerpts below; not a fresh whole-paper proof audit'})
    selected=[]
    for i,line in enumerate(lines):
        if re.search(r'A003|C018|C019|C020|C024|tensor|sublinear|signed.Boolean|G-J-COST|G-BOOLEANITY',line,re.I):
            selected.append(f'{i+1}: {line[:700]}')
        if len(selected)>=8: break
    excerpts.append('\n## '+str(p)+'\n'+'\n'.join(selected))
src=supp/'sources'
receipts.append({'path':str(src),'entries':[p.name for p in src.iterdir()] if src.exists() else 'MISSING','scope':'inventory only; no external theorem imported'})
(R/'out/SOURCES.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
(R/'out/INTAKE.md').write_text('\n'.join(excerpts)+'\n',encoding='utf-8')
print((R/'out/INTAKE.md').read_text(encoding='utf-8')[:17000])
