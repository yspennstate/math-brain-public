from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
protocol_path=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8-sig'))
now=datetime.now(timezone.utc).isoformat()
validation=json.loads((RUN/'out/VALIDATION.json').read_text(encoding='utf-8'))
assert validation['status']=='PASS'
statement=('The already refuted product-biased singleton helper J_X<=M_X has a '
 'dimension-minimal genuine Boolean witness f(X,Y)=1-2XY with independent '
 'Pr(X=1)=Pr(Y=1)=1/4, squared spectrum (49,3,3,9)/64, and '
 '1/16<J_X-M_X<3/32 bits. Its sign and bounds follow from '
 '4*13^52<2^48*3^6*7^49<8*13^52. Dimension 2 is minimal among '
 'all interior product biases; dimension 3 is minimal if all residual '
 'inputs are fair; dimension 4 is minimal if additionally both actual '
 'physical children are balanced. These restricted witnesses have exactly '
 'the same debt. The fixed common dyadic bias 1/4 has the smallest possible '
 'interior dyadic denominator for a two-bit witness. These are finite '
 'helper certificates, not counterexamples to uniform FEI or valid taxed bounds.')
claim={
 'claim_id':'A049-MINIMAL-TAXFREE-CERTIFICATE','version':1,
 'exact_statement':statement,
 'hypotheses':['Boolean signs, actual product-biased orthonormal Fourier spectra',
  'Singleton physical reveal with actual branch probabilities',
  'Shannon entropy in bits including the empty atom',
  'Interior selector bias; fair residual/balanced hypotheses only in their stated minimum-dimension variants'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['fleet05/A049'],
 'proof_source':['REPORT.md sections 1-5','code/check.py','out/MINIMAL_CERTIFICATE.json',
  'out/FAIR_RESIDUAL_CERTIFICATE.json','out/BALANCED_CERTIFICATE.json','out/PAIR_MINIMALITY.json'],
 'proof_dependencies':[], 'review_records':[],
 'status':'EXISTING_REFUTATION_EXTRACTED_AND_CHECKED_LOCAL_REVIEW_PENDING',
 'supersedes':[],
 'refutes':['B09-TAXFREE-BIASED-UNCERTAINTY (existing known refutation; minimized certificate only)'],
 'first_unproved_line':None,
 'next_consumers':['A050','A042','A057','A071','A084','A092','A090','B09','B20']
}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
(RUN/'CLAIMS.json').write_text(json.dumps([claim],indent=2)+'\n',encoding='utf-8')
progress={
 'protocol_revision':protocol['revision'], 'run_id':RUN.name,'stream':'B10',
 'packet_id':'A049','gap_id':'G-R-MISMATCH','attempt_id':'A049-EXTRACTION-01',
 'method':'Minimize an existing failed helper; direct rational spectra and integer-product entropy certificate; all-bias analytical dimension classification',
 'mathematical_delta':'Replace unequal-bias finite witness by p=q=1/4; certify n=2, fair-residual n=3, balanced-child fair-residual n=4 minima and one shared exact debt; no new taxed-bound refutation',
 'deliverable_status':'COMPLETE_LOCAL_REVIEW_AND_SUPERVISOR_COPY_PENDING',
 'mathematical_status':'MINIMAL_EXISTING_HELPER_CERTIFICATE_PROVED_LOCALLY; UNIVERSAL_FEI_OPEN',
 'claim_versions_used':[],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'kind':'verification/extraction of existing refuted statement'}],
 'source_artifacts':['REPORT.md','FROZEN_SPEC.json','code/check.py','code/sources.py','code/finalize.py',
  'out/SOURCE_MANIFEST.json','out/VALIDATION.json','out/MINIMAL_CERTIFICATE.json',
  'out/SHARED_DYADIC_BASELINE.json','out/PAIR_MINIMALITY.json','out/FAIR_RESIDUAL_CERTIFICATE.json',
  'out/BALANCED_CERTIFICATE.json'],
 'next_consumers':claim['next_consumers'],
 'next_action':'A050 apply one explicitly versioned repaired ledger to the n=4 balanced circuit, retaining actual M, valid tax, physical influence ownership and terminal entropy; A049 resume on a new found violation/review objection.',
 'stagnant_substantive_attempts':0,
 'blockers':['No full-FEI falsifier supplied or found in read board/registry; not a blocker to completed extraction',
  'B10 lead notes absent at stage start','Independent review and supervisor repository copying pending'],
 'packet_ids':['A049']
}
# The protocol lists the canonical key followed by a parenthetical description.
expected_progress_fields={key.split(' (',1)[0] for key in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected_progress_fields
payload=json.dumps(progress,indent=2)+'\n'
for name in ['PROGRESS.json','PACKET_DELTA.json']:
    (RUN/name).write_text(payload,encoding='utf-8')
report=(RUN/'REPORT.md').read_text(encoding='utf-8')
report=report.replace('The preliminary check passed 1,358 assertions in approximately 1.22 seconds; final strengthened checks include the rational margin and exact invariant-debt comparisons.',
 f'The final strengthened check passed {validation["assertions"]:,} assertions in {validation["runtime_seconds"]:.6f} seconds, including the rational margin and exact invariant-debt comparisons.')
(RUN/'REPORT.md').write_text(report,encoding='utf-8')
for field in protocol['required_per_run']['report_fields']:
    assert '# '+field in report
assert report.rstrip().split('\n\n')[-1].startswith('**Universal bridge:**')
(AGENT/'STATUS.md').write_text(
 'STATE: A049 extraction complete locally: minimal n=2 fixed-common-bias witness, fair-residual n=3 and balanced-child n=4 minima; 1,363 exact checks PASS; review pending; full FEI OPEN.\n'
 'NEXT: A092/A090 review; A050 test a versioned repaired ledger on the balanced certificate with M, valid tax, terminal entropy and nonreused influence; resume extraction only on a new violation or review objection.\n',encoding='utf-8')
logline=(f'\n{now} — Stage {RUN.name}: read protocol/board/original B09 and A046/A047/A096; B10 notes absent. '
 'Extracted AND with p=q=1/4; rational truth-table spectra and prime-log collection reduce sign to '
 '4*13^52<2^48*3^6*7^49<8*13^52. Proved minima 2 variables, 3 with fair residual bits, '
 '4 with fair residual bits and balanced children. Final 1,363 exact checks PASS. '
 'Saved protocol outputs locally; no full FEI falsifier, no independent acceptance or mirror claim.\n')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f: f.write(logline)
learned=('\n'+now+' — A049 minimal-falsifier extraction\n'
 '- The tax-free biased physical singleton helper J<=M is already false; its two-bit AND witness can use one common fixed bias 1/4. Spectrum (49,3,3,9)/64, residual (13,3)/16, children (1,0) and (1,3)/4.\n'
 '- 32(J-M)=log2(2^48*3^6*7^49/13^52); exact integer comparisons give 1/16<J-M<3/32. Clearing rational entropy coefficients into integer products avoids signed interval-division bugs.\n'
 '- For fair residual inputs, m<=1 child pairs are equal/opposite/disjoint Fourier characters, so J-M<=0 for every selector bias. Minimum total dimension is 3. If both children are balanced, all m<=2 children are signed characters and minimum total dimension is 4. Multiply both children by a fresh fair character to preserve the debt while balancing them.\n'
 '- The common bias 1/4 is a finite certificate simplification, not a replacement for the rare-selector endpoint with fixed residual bias. No tax-free-helper witness refutes a valid taxed repair or full uniform FEI.\n'
 '- Next reusable artifact: balanced circuit (-1)^Z(1-2XUV) with selector bias 1/4 and three fair residual bits; retain actual conditional entropy, bias tax, terminal entropy and single-use influence when testing a repaired C019 ledger.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f: f.write(learned)
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
receipts=[]
for path in sorted(RUN.rglob('*')):
    if path.is_file() and path.name!='PERSISTENCE.json':
        data=path.read_bytes(); assert len(data)<20*1024*1024
        receipts.append({'path':str(path.relative_to(RUN)),'bytes':len(data),
                         'sha256':hashlib.sha256(data).hexdigest()})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
    data=(AGENT/name).read_bytes()
    receipts.append({'path':'../../'+name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
(RUN/'out/PERSISTENCE.json').write_text(json.dumps({'status':'PASS','at_utc':now,
 'claim_fields_match':True,'progress_fields_match':True,'report_fields_present':True,
 'progress_copy_identical':True,'all_files_under_20mb':True,
 'independent_review':'PENDING','repository_copy':'PENDING_SUPERVISOR',
 'files':receipts},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','files_receipted':len(receipts),'assertions':validation['assertions']}))
