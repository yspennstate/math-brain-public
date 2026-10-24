from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
from fractions import Fraction as F

RUN=Path(__file__).resolve().parents[1]; AGENT=RUN.parents[1]; OUT=RUN/'out'
TEAM=AGENT.parents[1]; now=datetime.now(timezone.utc).isoformat()
protocol_path=Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8-sig'))
def save(name,v): (RUN/name).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
data=json.loads((OUT/'CENSUS.json').read_text(encoding='utf-8'))
verify=json.loads((OUT/'INDEPENDENT_RECONSTRUCTION.json').read_text(encoding='utf-8'))
extremal=json.loads((OUT/'EXTREMAL_CERTIFICATE.json').read_text(encoding='utf-8'))
assert data['status']==verify['status']=='PASS'
assert data['full_cases']==1052928 and data['representatives']==526464
refs={r['a']:r['witness']['debt_prime_log_vector'] for r in data['rows'] if r['m']==2 and r['b']==4}
assert all(r['witness']['debt_prime_log_vector']==refs[min(r['a'],r['b'])] for r in data['rows'] if r['m']==2)
assert all(r['witness']['debt_prime_log_vector']=={} for r in data['rows'] if r['m']<=1)

sources=[protocol_path,TEAM/'BOARD.md',TEAM/'claude/B10/STREAM_NOTES.md',AGENT/'STATUS.md',
 TEAM/'claude/B10/runs/20261011T230400Z-claude-B10-onebit-half-tax/REPORT.md',
 TEAM/'agents/A047/runs/20261012T003641Z-account05-A047-boundary-search/REPORT.md',
 TEAM/'agents/A047/runs/20261012T003641Z-account05-A047-boundary-search/DERIVATION.md',
 TEAM/'agents/A047/runs/20261013T221434Z-account05-A047-boundary-search/REPORT.md',
 TEAM/'agents/A047/runs/20261013T221434Z-account05-A047-boundary-search/out/HALF_I_COUNTEREXAMPLE.json',
 TEAM/'agents/A050/runs/20261013T212442Z-account05-A050-repair-with-scope/REPORT.md']
receipts=[]
for path in sources:
 raw=path.read_bytes()
 receipts.append({'path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),
  'scope':'Inspected locators stated in REPORT; hash does not imply full proof audit or repository-pin verification'})
save('out/SOURCE_RECEIPTS.json',receipts)

statement=('For every Boolean sign on two revealed bits and m=0,1,2 fair residual bits, '
 'at every ordered revealed-bias pair in {1/8,1/4,3/8,1/2}^2, the actual physical-block '
 'debt J_A-M_A is at most tau*(p1)+tau*(p2). All 1,052,928 truth-table/bias cases '
 'are covered by output-negation symmetry and exact rational certificates; no '
 'additivity theorem is assumed. Every nonuniform pair has a certified gap greater '
 'than 7/1000 bit to explicit lower witnesses for the sum tau*. The uniform pair '
 'has maximum debt exactly zero. The maximum of (J_A-M_A)/(Delta_A/2), excluding '
 'the zero-denominator uniform pair, lies strictly between 68132470/100000000 '
 'and 68132471/100000000 and is attained by '
 'f=(-1)^X2(1-2X1UV), Pr(X1=1)=1/8 and X2,U,V fair. '
 'Both revealed coordinates are essential; four total variables are minimal '
 'for a positive debt inside this frozen domain. This is not an all-dimensional '
 'block-additivity theorem or a FEI falsifier.')
claim={
 'claim_id':'A049-BLOCK-SHARP-TAX-GRID','version':1,'exact_statement':statement,
 'hypotheses':['Genuine Boolean signs with complete truth tables',
  'Two actual revealed physical coordinates; inherited product-biased orthonormal basis',
  'Zero, one or two uniform residual coordinates; only the explicitly specified revealed bias grid',
  'Shannon entropy in bits, including empty atoms; Delta_i=p_i log2((1-p_i)/p_i)'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),
 'contributors':['account05/A049'],
 'proof_source':['REPORT.md','FROZEN_SPEC.json','code/census.py','code/verify.py',
  'out/CENSUS.json','out/TAU_LOWER_WITNESSES.json','out/EXTREMAL_CERTIFICATE.json',
  'out/INDEPENDENT_RECONSTRUCTION.json'],
 'proof_dependencies':[],'review_records':[],
 'status':'FINITE_EXISTING_HELPER_VERIFICATION_COMPLETE_LOCAL_REVIEW_PENDING',
 'supersedes':[],'refutes':[],'first_unproved_line':None,
 'next_consumers':['A074','A092','A085','A050','A048','A047','B09','B10','B20']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
save('CLAIMS.json',[claim])
next_action=('A074 reproduce the finite block maximum with an independent transform; '
 'A049 minimize the new actual descendant-reference injection failure of A048/A047 '
 'on an essential tree, retaining one prescribed root witness, terminal entropy '
 'and one removed-influence account. Do not repeat or escalate the completed bias grid.')
progress={
 'protocol_revision':protocol['revision'],'run_id':RUN.name,'stream':'B10','packet_id':'A049',
 'gap_id':'G-R-MISMATCH','attempt_id':'A049-BLOCK-GRID-01',
 'method':'Exhaustive actual-Boolean two-block rational-spectrum census, sharp-tax lower witnesses, exact maximizer ties and independent centered-basis reconstruction',
 'mathematical_delta':'Closed all 1,052,928 frozen cases; no sharp-tax violation; exact global half-tax ratio in (0.68132470,0.68132471); minimal essential four-bit attaining certificate',
 'deliverable_status':'COMPLETE_LOCAL_REVIEW_AND_SUPERVISOR_COPY_PENDING',
 'mathematical_status':'FINITE_BLOCK_HELPER_VERIFIED; UNIVERSAL_BLOCK_ADDITIVITY_AND_FEI_OPEN',
 'claim_versions_used':[],
 'claims_created_or_changed':[{'claim_id':claim['claim_id'],'version':1,'kind':'finite verification of existing conditional helper'}],
 'source_artifacts':['REPORT.md','FROZEN_SPEC.json','code/census.py','code/verify.py','code/finalize.py',
  'out/PILOT.json','out/CENSUS.json','out/TAU_LOWER_WITNESSES.json','out/EXTREMAL_CERTIFICATE.json',
  'out/INDEPENDENT_RECONSTRUCTION.json','out/SOURCE_RECEIPTS.json','out/SPEC_NOTES.md',
  'out/VERIFIER_REPAIR.md','out/A074_HANDOFF.json'],
 'next_consumers':claim['next_consumers'],'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['Independent-agent review and supervisor copy pending',
  'No finite counterexample in searched domain; extension beyond domain and universal reference payment remain unsupported'],
 'packet_ids':['A049']}
expected={field.split(' (',1)[0] for field in protocol['required_per_run']['progress_fields']}
assert set(progress)==expected
save('PROGRESS.json',progress); save('PACKET_DELTA.json',progress)
save('out/A074_HANDOFF.json',{'to':'A074','status':'SAVED_LOCAL_NOT_SENT',
 'task':'Independently reproduce finite maximum and target signs; source-bound full rerun optional',
 'full_case_count':1052928,'symmetry':'Global output negation only; first output +1',
 'witness':extremal,'bias_pairs_attaining_global_ratio':[['1/8','1/2'],['1/2','1/8']],
 'required_checks':['Direct actual Boolean spectra and physical child marginals',
 'Rational log sign bounds; zero debt via prime-log cancellation',
 'Output-negation coverage; exact tied candidate vectors and exclusion margins',
 'All m<=1 maxima zero; four-bit minimum only in searched domain',
 'Do not interpret a finite pass as all-dimensional additivity or FEI'],
 'commands':['python -X utf8 code/census.py --max-m 1','python -X utf8 code/census.py --max-m 2','python -X utf8 code/verify.py']})

report=(RUN/'REPORT.md').read_text(encoding='utf-8')
assert all('# '+field in report for field in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n\n')[-1].startswith('**Universal bridge:**')
(AGENT/'STATUS.md').write_text(
 'STATE: A049 block-grid stage complete: all 1,052,928 cases certified; no sharp-tax violation; maximal half-tax ratio in (0.68132470,0.68132471); essential four-bit minimum in domain; FEI OPEN, review pending.\n'
 'NEXT: A074/A092 reproduce and review; minimize A048/A047 actual descendant-reference injection failure with prescribed root witness, terminal entropy and one removed-influence budget; no grid escalation.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{now} — {RUN.name}: read updated board and B10 v2; executed lead-assigned two-block census. '
 'Pilot 4,352 cases PASS (2.712464 s); full 1,052,928 cases/526,464 representatives PASS (48.831366 s, '
 '20,473 assertions); direct attaining-record reconstruction PASS (543 assertions, 2.223789 s). '
 'All debts pass explicit sharp-tax lower witnesses. Global half-tax ratio in '
 '(0.68132470,0.68132471), attained by (-1)^X2(1-2X1UV), both block bits essential; '
 'four-bit minimum in domain. Verifier zero-rounding assertion repaired; dangerous fine-bound '
 'integer powers removed before they were reached. No oversized job occurred. '
 'Protocol files and A074 handoff saved locally; independent acceptance/copy pending; FEI OPEN.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
 f.write(f'\n{now} — A049 block sharp-tax finite interface\n'
 '- On the frozen revealed-bias grid {1/8,1/4,3/8,1/2}^2, all Boolean four-child combinations '
 'on <=2 fair residual bits satisfy the additive sharp tax. Explicit scalar real witnesses '
 'are lower bounds on tau*, so passing them does not assume the unreviewed block-additivity theorem.\n'
 '- Exact maximum debt at m=2 equals the singleton maximum at the smaller bias; m<=1 maximum '
 'is zero. This is a finite certificate only. The ratio to half-Delta is maximal at (1/8,1/2), '
 'in (0.68132470,0.68132471). Essential circuit (-1)^X2(1-2X1UV) attains it: a fair queried '
 'character preserves debt while keeping that physical bit essential.\n'
 '- Exact spectrum kernel: integer child Walsh with denominator N, two selector biases a/8,b/8 '
 'give parent squared masses over 4096N^2. Output negation is a valid exact quotient. '
 'Outward entropy lattice endpoints for an exact zero can straddle zero; use empty prime-log vectors for equality.\n'
 '- Do not clear a fine rational margin into unbounded integer powers. Check exponent sizes first; '
 'range-reduced rational log intervals prove ratio signs cheaply. The interrupted verifier failed '
 'before that oversized calculation; no oversized job ran.\n'
 '- Local block checks now close the lead-assigned finite domain. The updated unpaid cost is '
 'reference injection/reset on actual descendants with one prescribed root witness and terminal entropy; '
 'next extraction should target that new failure rather than grow the bias grid.\n')
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
files=[]
for path in sorted(RUN.rglob('*')):
 if path.is_file() and path.name!='PERSISTENCE.json':
  raw=path.read_bytes(); assert len(raw)<20*1024*1024
  files.append({'path':str(path.relative_to(RUN)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
for name in ['STATUS.md','WORKLOG.md','LEARNED.md']:
 raw=(AGENT/name).read_bytes()
 files.append({'path':'../../'+name,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()})
save('out/PERSISTENCE.json',{'status':'PASS','at_utc':now,'claim_fields_match':True,
 'progress_fields_match':True,'report_fields_present':True,'progress_copy_identical':True,
 'all_files_under_20mb':True,'independent_review':'PENDING','repository_copy':'PENDING_SUPERVISOR','files':files})
print(json.dumps({'status':'PASS','files_receipted':len(files),'full_cases':data['full_cases'],
 'search_assertions':data['assertions'],'independent_implementation_assertions':verify['assertions']}))
