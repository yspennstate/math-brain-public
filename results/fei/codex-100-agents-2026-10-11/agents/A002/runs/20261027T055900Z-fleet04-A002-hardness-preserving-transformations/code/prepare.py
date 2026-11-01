from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parents[1]
for d in ('out','code'): (R/d).mkdir(exist_ok=True)
base=Path('~/mop_fei100')
report=base/'reports/fei-2026-10-11'
supp=base/'research_pushes/2026-10-11-full-fei-100-agents'
files=[report/x for x in ('README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex')]
files += [supp/x for x in ('CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md')]
files += list((supp/'sources').glob('*.md'))
files += list(Path('context').glob('*.txt'))
receipts=[]; excerpts=[]
for p in files:
 if not p.exists(): receipts.append({'path':str(p),'status':'MISSING'});continue
 data=p.read_bytes()
 try: s=data.decode('utf-8-sig');enc='utf-8-sig'
 except UnicodeDecodeError: s=data.decode('cp1252');enc='cp1252'
 lines=s.splitlines(); hits=[(i+1,line[:600]) for i,line in enumerate(lines) if re.search(r'A002|tensor|activat|composition|erasure|critical|log.Sobolev',line,re.I)]
 receipts.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'encoding':enc,'lines':len(lines),'scope':'baseline refresh; targeted lines, not full independent audit','matches':hits[:24]})
 excerpts.append(str(p)+'\n'+'\n'.join(f'{i}: {v}' for i,v in hits[:5]))
(R/'out/BASELINE_RECEIPTS.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
(R/'out/BASELINE_EXCERPTS.txt').write_text('\n\n'.join(excerpts),encoding='utf-8')
spec={'helper':'check_tree.py v1','family':'all labelled Boolean signs on n=0,1,2,3; canonical exact affine/character reset at each child','domain':'K=2,4,8,16; all stopping/query-coordinate policies after deterministic canonical reset','case_count':'278 root tables; 244 policies per 3-bit root, 9 per 2-bit root, 2 per 1-bit root, 1 per 0-bit root; 250472 root/K/policy comparisons','symmetry':'none on labelled functions; deterministic optimal-basis choice is policy definition, not symmetry quotient','arithmetic':'integer Walsh, Fraction, exact prime-log vectors; integer products certify signs','memory_estimate_mb':100,'pilot_max_seconds':55,'main_max_seconds':180,'no_automatic_escalation':True,'checks':['affine minimum by direct directional costs and exhaustive independent bases','node Gibbs identity; all conditional dependence retained','adaptive tree telescoping with actual reaches and full terminals','occupied-event and zero-mass boundaries','negative-reserve and omitted-reset controls']}
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2),encoding='utf-8')
print(json.dumps({'baseline_files':len(receipts),'spec_saved':True}))
