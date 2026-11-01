"""Protocol-exact stage-2 serialization; only writes inside this A017 run."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json

R=Path(__file__).resolve().parents[1]
A=R.parents[1]
TEAM=A.parents[1]
C=Path(r'~\mop_fei100\reports\fei-2026-10-11')
PREVIOUS=A/'runs'/'20261011T215725Z-fleet05-A017-recursive-addressing'
LEAD=TEAM/'claude'/'B04'
NOW=datetime.now(timezone.utc).isoformat()

def receipt(p):
    data=p.read_bytes()
    return dict(path=str(p),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())

def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

sources=[TEAM/'BOARD.md',LEAD/'STREAM_NOTES.md',
         LEAD/'runs'/'20261011T224500Z-claude-B04-sharp-selector-debt'/'CLAIMS.json',
         PREVIOUS/'RECURSIVE_ADDRESSING.tex',PREVIOUS/'REPORT.md',PREVIOUS/'CLAIMS.json',
         C/'EXECUTION_PROTOCOL.json',
         Path(r'~\brain_workers\FEI100_20261011\context\threshold_paper_38pp.txt')]
save(R/'out'/'source_receipts.json',dict(created_utc=NOW,sources=[receipt(p) for p in sources],
     missing_lead_report=str(LEAD/'runs'/'20261011T224500Z-claude-B04-sharp-selector-debt'/'REPORT.md'),
     lead_report_present=(LEAD/'runs'/'20261011T224500Z-claude-B04-sharp-selector-debt'/'REPORT.md').exists(),
     previous_claim_review_evidence='B04 notes v2: A017 ledger holds, 300 independent exact cases; no A091/A090 acceptance claimed'))

statement=('For all n>=1,a>=0, binary linear M:F2^n->F2^a and quadratic q with q(0)=0, '
           'F*=(b(x)-2*1_(x=0))y_(Mx), b=(-1)^q, is Boolean. With r=rank M, D=n-r and '
           'k=polar rank on ker M, H(F*)=2r+k+2^(-r)(E_(D,k)-k), where E_(D,k) is the entropy '
           'of masses (2^(-k/2)-2^(1-D))^2,(2^(-k/2)+2^(1-D))^2,2^(2-2D) with respective '
           'counts (2^k+2^(k/2))/2,(2^k-2^(k/2))/2,2^D-2^k, omitting zero masses. '
           'Active M-column controls have influence 1/2; each inactive control influence changes '
           'from the quadratic baseline by (1-2*l_i)2^(1-n); total data influence is one. '
           'If q has zero linear term, a physical tree querying active address controls then '
           'remaining quadratic interactions has B_i<=2Inf_i at every internal node, so its '
           'localized boundary bill at K=2 is zero, with quadratic and point-defect terminals '
           'paying H(F*)<=4(I(F*)-1). For matching q on even n and fixed prefix rank r, H/I tends '
           'to 2, while the unlocalized root boundary bill/I grows linearly in n.')
hyp=['uniform independent physical binary controls and distinct data signs',
     'entropy in bits, total physical influence; real derivative I(D) is Fourier Dirichlet energy',
     'q quadratic with q(0)=0 for exact surgery identities; zero linear q required only for the stated stopping theorem',
     'distinct address labels name distinct physical y_z coordinates; arbitrary control reuse computing M is allowed',
     'fixed-r limit and explicit root-charge comparison use even-n matching quadratic and prefix coordinate address']
sh=hashlib.sha256(json.dumps(dict(statement=statement,hypotheses=hyp),sort_keys=True,separators=(',',':')).encode()).hexdigest()
prior=json.loads((PREVIOUS/'CLAIMS.json').read_text())[0]
claim=dict(claim_id='A017-POINT-SURGERY-STOPPING-LEDGER',version=1,exact_statement=statement,
           hypotheses=hyp,statement_sha256=sh,contributors=['A017/fleet05'],
           proof_source=dict(path='POINT_FLIPPED_FIBERS.tex',sha256=receipt(R/'POINT_FLIPPED_FIBERS.tex')['sha256'],
                             locators=['Exact surgery ledger','Fixed-r asymptotics','Physical stopping tree with zero bad-node boundary bill']),
           proof_dependencies=[dict(claim_id=prior['claim_id'],version=prior['version'],statement_sha256=prior['statement_sha256'],
                                    source=str(PREVIOUS/'RECURSIVE_ADDRESSING.tex'),
                                    scope_used='quadratic Walsh law and general affine-fiber entropy identity',
                                    status='AUTHOR_PROVED; B04 lead scoped HOLDS and independent 300-case check; A091/A090 review pending')],
           review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],
           first_unproved_line=None,next_consumers=['A013','A018','A019','A020','A027','A028','A030','A077','A090','A091'])
save(R/'CLAIMS.json',[claim])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B04',packet_id='A017',
              gap_id='G-LOWSEL-COLLISION',attempt_id='A017-stage2-single-point-quadratic-fiber',
              method='Exact signed point-surgery histogram, rational-log certificates and high-influence physical stopping tree',
              mathematical_delta='Resolved lead single-point target: exact H/I and fixed-r limit; all physical root 2I(D) charges; localized K=2 bad-node bill zero with terminal-inclusive sharp H<=4(I-1) on zero-linear quadratic single-point flips. Universal multiple-defect/phase payment remains OPEN.',
              deliverable_status='LOCAL_ARTIFACT_COMPLETE_REVIEW_PENDING',mathematical_status='RESTRICTED_C019_PAYMENT_PROVED_FULL_FEI_OPEN',
              claim_versions_used=[dict(claim_id=prior['claim_id'],version=1)],
              claims_created_or_changed=[dict(claim_id=claim['claim_id'],version=1)],
              source_artifacts=['REPORT.md','CLAIMS.json','POINT_FLIPPED_FIBERS.tex','REUSE_CONDITIONS.json',
                                'code/check.py','code/derive_tables.py','out/FROZEN_SPEC.json','out/PILOT_REPAIR.json',
                                'out/case_plan.json','out/pilot.json','out/validation.json','out/tables.json','out/source_receipts.json'],
              next_consumers=claim['next_consumers'],
              next_action='A091/A090 reconstruct; test two point flips with incompatible quadratic gradients inside one address fiber, retaining exact bad-node boundary/terminal reserves and nonreused physical influence.',
              stagnant_substantive_attempts=0,
              blockers=['Independent acceptance and supervisor transfer pending; no mathematical access blocker'],packet_ids=['A017'])
save(R/'PROGRESS.json',progress);save(R/'PACKET_DELTA.json',progress)
protocol=json.loads((C/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8-sig'))
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
expected=set(protocol['required_per_run']['progress_fields']);expected.remove('packet_ids (one primary ID, for compatibility)');expected.add('packet_ids')
assert set(progress)==expected
report=(R/'REPORT.md').read_text()
assert all('## '+field in report for field in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n')[-1].startswith('**Universal bridge**:')
assert json.loads((R/'PROGRESS.json').read_text())==json.loads((R/'PACKET_DELTA.json').read_text())
assert all(p.stat().st_size<20*1024*1024 for p in R.rglob('*') if p.is_file())
save(R/'out'/'persistence_receipts.json',dict(created_utc=NOW,status='LOCAL_SAVE_VERIFIED',
     protocol_fields='exact schemas and report fields verified',
     artifacts=[receipt(p) for p in sorted(R.rglob('*')) if p.is_file() and p.name!='persistence_receipts.json'],
     rolling_files=[receipt(A/n) for n in ['STATUS.md','WORKLOG.md','LEARNED.md']],
     independent_review='PENDING',mirror_status='NOT_VERIFIED; supervisor transfer pending'))
print(json.dumps(dict(status='LOCAL_SAVE_VERIFIED',run=str(R),claim_fields=len(claim),progress_fields=len(progress),
                      statement_sha256=sh),indent=2))
