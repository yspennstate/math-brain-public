import hashlib,json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
campaign=Path('~/mop_fei100/reports/fei-2026-10-11')
supp=Path('~/mop_fei100/research_pushes/2026-10-11-full-fei-100-agents')
context=Path('~/brain_workers/FEI100_20261011/context')
files=[campaign/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
files += [supp/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
files += sorted(context.glob('*.txt'))
files += [campaign/'source_material/reductions/paper/forests.tex',Path('~/brain_workers/FEI100_20261011/BOARD.md'),Path('~/brain_workers/FEI100_20261011/claude/B02/STREAM_NOTES.md')]
agents=Path('~/brain_workers/FEI100_20261011/agents')
for agent,run,names in [
 ('A008','20261021T234312Z-fleet03-A008-gate-label-compression',['ROOT_PAYMENT.md','REPORT.md','CLAIMS.json','REVIEW_A009.md']),
 ('A007','20261021T211258Z-fleet03-A007-root-normalization',['KMM_PAYMENT.md','REPORT.md']),
 ('A006','20261021T182437Z-fleet03-A006-posterior-forest-optimization',['REPORT.md']),
 ('A009','20261014T054349Z-fleet05-A009-fractional-incidence-optimization',['PRIVATE_LEAF_PAYMENT.md','REPORT.md','CLAIMS.json'])]:
 files += [agents/agent/'runs'/run/x for x in names]
receipts=[]; excerpts=[]
for p in files:
    if not p.exists():
        receipts.append({'path':str(p),'status':'MISSING'}); continue
    raw=p.read_bytes()
    try:
        body=raw.decode('utf-8-sig')
    except UnicodeDecodeError as err:
        receipts.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'status':'NOT_UTF8','error_offset':err.start,'nearby_bytes_hex':raw[max(0,err.start-16):err.start+16].hex()})
        print(json.dumps(receipts[-1]))
        try:
            body=raw.decode('cp1252')
        except UnicodeDecodeError:
            continue
        receipts[-1]['decoding_view']='Explicit strict cp1252 legacy PDF-text view, not an assertion of producer encoding; original bytes untouched'
    lines=body.splitlines()
    receipts.append({'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'mode':'full byte receipt; selected mathematical excerpts; earlier baseline inherited'})
    hits=[i for i,line in enumerate(lines) if re.search(r'A009|B02|C020|fractional|forestconditioning|Fourier|pivotal|normaliz',line,re.I)]
    excerpt=[]
    for i in hits[:3]: excerpt.extend(lines[max(0,i-1):i+2])
    excerpts.append({'path':str(p),'excerpt':excerpt})
root.joinpath('out','SOURCES.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
root.joinpath('out','BASELINE_EXCERPTS.json').write_text(json.dumps(excerpts,indent=2),encoding='utf-8')
print(json.dumps({'source_receipts':len(receipts),'missing':[x['path'] for x in receipts if x.get('status')=='MISSING'],'excerpt_artifact':'out/BASELINE_EXCERPTS.json'}))
