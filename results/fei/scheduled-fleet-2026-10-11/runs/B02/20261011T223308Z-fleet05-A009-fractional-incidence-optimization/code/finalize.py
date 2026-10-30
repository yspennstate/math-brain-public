from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]
ROOT=R.parents[1]
P=Path(r'~\mop_fei100\reports\fei-2026-10-11')
S=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
C=Path(r'~\brain_workers\FEI100_20261011\context')
sources=[]
paths=[P/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex']]
paths += list((P/'runs').rglob('REPORT.md'))
paths += [S/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
paths += list((S/'sources').glob('*.md'))+list(C.glob('*.txt'))
paths += [P/'source_material'/'reductions'/'paper'/'forests.tex']
paths += [Path(r'~\brain_workers\FEI100_20261011\claude\B02\STREAM_NOTES.md')]
for a in ['A006','A007','A008']:
    paths+=list((ROOT.parent/a/'runs').rglob('REPORT.md'))
for p in paths:
    data=p.read_bytes()
    txt=data.decode('utf-8',errors='replace')
    sources.append({'path':str(p),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'lines':len(txt.splitlines()),'scope':'Full local byte intake; mathematical sections inspected as described in REPORT.md, not blanket independent validation'})
(R/'out'/'SOURCES.json').write_text(json.dumps(sources,indent=2),encoding='utf-8')
protocol=json.loads((P/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
progress={
 'protocol_revision':protocol['revision'],
 'run_id':R.name,'stream':'B02','packet_id':'A009','gap_id':'G-J-COST',
 'attempt_id':'A009-fixed-posterior-logweight-v1','method':'convex log-weight primal; direct Gibbs coordinate-price dual; rational KKT; shared-core actual forest continuation',
 'mathematical_delta':'Fixed-law exact dual and actual (1,2) KKT; joint posterior convexity fails on duplicate dictators; all-r,m singleton-petal residual <=8I/prior<=10I. New lead direction: geometric sunflower pressure <41I; affine-plane positive pressure >=7I log((Q+1)/2) for ALL feasible global weights.',
 'deliverable_status':'COMPLETE_LOCAL_CONTINUATION_EVIDENCE_PENDING_REVIEW',
 'mathematical_status':'PROVISIONAL_SOURCE_COMPLETE_SCOPED_PROOF; FULL_FEI_OPEN',
 'claim_versions_used':[{'source':'source_material/reductions/paper/forests.tex','locator':'thm:posteriorforest','sha256':next(x['sha256'] for x in sources if x['path'].endswith('forests.tex'))},{'source':'SEED_LEMMAS.md','locator':'Section 2 complete-reference prior','sha256':next(x['sha256'] for x in sources if x['path'].endswith('SEED_LEMMAS.md'))}],
 'claims_created_or_changed':[],
 'source_artifacts':['REPORT.md','INCIDENCE_OPTIMIZATION.tex','WEIGHT_CERTIFICATE.json','FROZEN_SPEC.json','LEAD_FROZEN_SPEC.json','code/check.py','code/lead_check.py','out/CHECK.json','out/LEAD_CHECK.json','out/SOURCES.json'],
 'next_consumers':['A006','A007','A010','A014','A086','A094'],
 'next_action':'A086/A094 reconstruct continuation and affine-plane obstruction; then test PI-J whole-set posterior on affine-plane prime implicants, retaining all labels/ranks/congestion.',
 'stagnant_substantive_attempts':0,
 'blockers':['B02 pending broad-candidate cap: no new registry claim opened; independent review/adoption pending.','Universal arbitrary-base structural expectation remains unpaid.'],
 'packet_ids':['A009']}
assert set(progress)==set(x.split(' (')[0] for x in protocol['required_per_run']['progress_fields'])
for n in ['PROGRESS.json','PACKET_DELTA.json']:
    (R/n).write_text(json.dumps(progress,indent=2),encoding='utf-8')
(R/'CLAIMS.json').write_text('[]\n',encoding='utf-8')
report=(R/'REPORT.md').read_text(encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:
    assert '## '+field in report,field
check=json.loads((R/'out'/'CHECK.json').read_text())
lead=json.loads((R/'out'/'LEAD_CHECK.json').read_text())
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
(ROOT/'STATUS.md').write_text('STATE: A009 local dual/certificates complete; shared-core R<=8I; geometric sunflower outer pressure bounded; affine-plane outer pressure >=7I log((Q+1)/2) for all weights; '+str(check['assertions']+lead['assertions'])+' exact checks; review pending; FEI OPEN.\nNEXT: A086/A094 review; following B02 lead test prime-implicant whole-set posterior on affine-plane DNF, where coordinatewise fractional pressure fails uniformly.\n',encoding='utf-8')
with (ROOT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+now+' — Read protocol/board and full forest source. Fixed-law log-weight dual, exact (1,2) Boolean KKT, duplicate-dictator nonconvex joint optimization witness. Shared-core singleton R<=8I/prior<=10I. Consumed B02 lead notes when they appeared: geometric sunflower pressure <41I; affine-plane DNF pressure >=7I log((Q+1)/2) for all global weights and all prime powers Q>=16. '+str(check['assertions']+lead['assertions'])+' exact assertions across two frozen checks. Kept CLAIMS empty at B02 review cap; continuation and obstruction evidence awaits A086/A094. All writes local.\n')
(ROOT/'LEARNED.md').write_text('Fixed posterior laws give F(t)=v ln(product(1+pi exp(t))-1)-c dot t, convex in log weights. Rational root marginals plus coordinate prices certify KKT exactly; this proves an optimum only for fixed actual-run laws. Joint posterior optimization is nonconvex: duplicate dictators have negative log-weight Hessian direction.\n\nFor common r-core AND private-singleton OR, uniform global weights 1/m and actual-root/child-order posteriors pay every residual term: R<=8I; paid scale prior <=10I. Functions already satisfy formula/LTF FEI: this is a DNF cost calibration. General overlapping base-gate cost remains unpaid.\n\nFirst-index sunflower derivative tie has geometric q_l; lambda_l=2^-l gives outer positive pressure <41I. Affine-plane line DNF on Q^2 bits has read Q+1; for prime powers Q>=16 every point witness mass is <=2/(Q+1), for any disjoint pivotal tie rule. Holder and each coordinate incidence row force pressure >=7I log((Q+1)/2) for ALL weights. This is a coordinatewise pressure obstruction, not a full conditioned-cost/PI-J/FEI disproof. Next: its whole-set posterior.\n\nAbstract KKT inputs need not be Boolean-realizable. Duplicate labels stay distinct. Common scaling can have a boundary infimum. B02 notes appeared mid-stage and superseded the heterogeneous-petal next target.\n',encoding='utf-8')
receipt=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='RECEIPTS.json':
        data=p.read_bytes(); assert len(data)<20_000_000
        receipt.append({'path':str(p.relative_to(R)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(R/'out'/'RECEIPTS.json').write_text(json.dumps({'saved_at_utc':now,'files':receipt,'mirror':'PENDING_SUPERVISOR_COPY','independent_review':'PENDING'},indent=2),encoding='utf-8')
print(json.dumps({'files':len(receipt),'schema_fields':'EXACT','checks':check['assertions'],'run':str(R),'claims':'no new broad candidate; continuation evidence'}))
