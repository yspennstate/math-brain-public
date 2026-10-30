from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1];TEAM=A.parents[1]
OLD=A/'runs/20261023T035732Z-fleet03-A099-candidate-assembly'
def rd(p):return json.loads(p.read_text(encoding='utf-8'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(R/'code/prior_exact.py').write_bytes((OLD/'code/check.py').read_bytes())
save(R/'out/FROZEN_SPEC.json',{'at':stamp,'helper_version':'A099-v9 '+hashlib.sha256((R/'code/check.py').read_bytes()).hexdigest(),
 'own_exact_primitive_sha256':hashlib.sha256((R/'code/prior_exact.py').read_bytes()).hexdigest(),
 'actual_Boolean_family':'G=a+sigma*(1-a^2)*h, fixed displayed four-bit controller, ALL labelled2-bit pilot/3-bit primary seeds; exact physical128-vertex witness; parity3 boundary',
 'parameter_domain':'all seed coordinates, signs +/-1, exact-spectrum and linearly weighted complete tail sources, two pre-outcome sign bins; A093 energy at d0, A097 energy otherwise',
 'case_count':'pilot16*2*2*2=128 transactions; main256*3*2*2=3072;81 controller faces checked separately',
 'symmetry':'NONE; all labelled seeds; two fixed source families only; no assertion enumerating all references',
 'arithmetic':'Fraction, exact prime-log cancellations,18-term atanh with geometric error, outward80-bit dyadic log2 bounds',
 'memory_estimate_MB':140,'pilot_max_seconds':50,'main_max_seconds':180,'automatic_dimension_increase':False,
 'target':'other actual child nonempty spectrum (or uniform if its tail zero), specified for both outcomes before query; every full terminal retained',
 'claim_scope':'finite corroboration of analytic reconstruction; no all-dimensional extrapolation and no FEI proof'})
save(R/'CLAIMS.json',rd(OLD/'CLAIMS.json'))
p=rd(OLD/'PROGRESS.json');p.update(run_id=R.name,attempt_id='A099-assembly-v9',method='One-source phase/bin/JS/discrepancy synthesis and independent complete-reference reconstruction',
 mathematical_delta='CHECKPOINT: new phase-funded nonempty changes consumed; independent synthesis/validation in progress.',deliverable_status='CHECKPOINT',mathematical_status='FULL_FEI_OPEN_VALIDATION_PENDING',claims_created_or_changed=[],source_artifacts=[str(R/'out/FROZEN_SPEC.json')],
 next_action='Reconstruct phase-bin and JS refinements, identify exact matched-isospectral nullspace, preserve universal source-price leaf.')
save(R/'PROGRESS.json',p);save(R/'PACKET_DELTA.json',p)
protocol=rd(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json'))
(R/'REPORT.md').write_text('# A099 version9 checkpoint\n\n'+'\n\n'.join('## '+s+'\n\nCheckpoint: source intake complete, independent validation pending.' for s in protocol['required_per_run']['report_fields'])+'\n\n## Universal bridge\n\nC024/C019 supplied-source profile payment is being assembled; all-dimensional influence-priced source admission remains open.\n',encoding='utf-8')
(A/'STATUS.md').write_text('STATE: A099 v9 checkpoint saved; reconstructing actual phase-funded nonempty changes, JS refinement and inherited-reference discrepancy; FEI OPEN.\nNEXT: Finish complete-reference audit; assemble exact nullspace and source-admission leaf without repeating canonical-return work.\n',encoding='utf-8')
sources=[TEAM/'BOARD.md',TEAM/'claude/B20/STREAM_NOTES.md',OLD/'CANDIDATE_MANUSCRIPT.tex',OLD/'CLAIMS.json',OLD/'out/PROOF_DEPENDENCIES.json',Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')]
for agent,run,files in [('A096','20261023T053800Z-fleet03-A096-live-gap-ledger',['REPORT.md','DERIVATION.md','CLAIMS.json']),('A097','20261023T062140Z-fleet03-A097-cross-route-transfer',['REPORT.md','DERIVATION.md','CLAIMS.json']),('A093','20261023T070224Z-fleet03-A093-literature-and-priority',['REPORT.md','DERIVATION.md','CLAIMS.json']),('A003','20261023T062246Z-fleet03-A003-minimal-target-formulation',['REPORT.md','DERIVATION.md','CLAIMS.json'])]:
 sources += [TEAM/'agents'/agent/'runs'/run/f for f in files]
save(R/'out/SOURCE_RECEIPTS.json',[{'path':str(pth),'bytes':len(pth.read_bytes()),'sha256':hashlib.sha256(pth.read_bytes()).hexdigest()} for pth in sources])
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:f.write('\n'+stamp+': v9 checkpoint: new phase-bin and JS/ref-discrepancy proofs consumed. Frozen complete-reference audit before evaluation. Universal price stays open; only own research directory written.\n')
print('CHECKPOINT_AND_SPEC_SAVED')
