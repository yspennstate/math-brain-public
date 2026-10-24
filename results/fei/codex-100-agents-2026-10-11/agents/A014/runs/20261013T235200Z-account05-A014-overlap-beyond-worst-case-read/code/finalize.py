from pathlib import Path
from datetime import datetime, timezone
import hashlib,json
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,data): (R/name).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
previous=A/'runs/20261011T223346Z-account05-A014-overlap-beyond-worst-case-read/CLAIMS.json'
old=json.loads(previous.read_text(encoding='utf-8'))[0]
addition=(' For every pairwise-disjoint positive width-w clause union, w>=2,m>=1, put p=2^-w,c=(1-p)^(m-1). '
          'All distant-blocker conditioned derivative remainders and local pressures vanish, but the off-clause '
          'spectral degree mass is I(f)*(1-c). The normalized derivative entropy is w-1+(m-1)*h_g, '
          'h_g=h2(p)+p*log2(2^w-1), and diverges at fixed w. With a=(1-p)^m, the exact whole-function entropy '
          'is h2(4*a*(1-a))+4*a*(m*h_g-h2(a)); this is a known disjoint-product calibration. '
          'Hence conditioned-error-only off-support transfer is false and is not a FEI disproof.')
claim=dict(old); claim.update(version=2,exact_statement=old['exact_statement']+addition,
    statement_sha256=hashlib.sha256((old['exact_statement']+addition).encode()).hexdigest(),
    proof_source={'prior_version_source':str(previous),'prior_version_sha256':digest(previous),
                  'new_proof':str(R/'DERIVATION.md'),'new_proof_sha256':digest(R/'DERIVATION.md'),
                  'locators':['Exact off-support obstruction','Why derivative entropy alone also fails','Whole-function product payment']},
    proof_dependencies=[{'claim_id':old['claim_id'],'version':1,'scope_used':'Unchanged prior results only; author-proved pending independent review'},
                        {'claim_id':'ELEMENTARY-PARSEVAL-PRODUCT-CHAIN-RULE','version':'standard','scope_used':'New self-contained identities'}],
    review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
    supersedes=[{'claim_id':old['claim_id'],'version':1}],
    refutes=[{'statement':'off-clause degree mass <= sum_j conditioned remainder norm squared','witness':'w=2,m=2: left=3/8,right=0','scope':'proposed substitution, not A009 original transfer'}],
    first_unproved_line='Construct one normalized whole-set blocker reference with complete O(I) cost for overlapping linear hypergraphs.',
    next_consumers=['A009','A006','A008','A015','B03','A086','A094'])
claim['hypotheses']=old['hypotheses']+['New identities only: disjoint positive equal-width clauses, integers w>=2,m>=1; no overlap conclusion inferred']
save('CLAIMS.json',[claim])
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B03',packet_id='A014',
    gap_id='B03-WHOLE-SET-BLOCKER-PAYMENT',attempt_id='A014-stage3-conditioned-spectrum',
    method='Consume A009 all-density transfer; exact blocker spectral obstruction and product activation accounting',
    mathematical_delta='Zero local conditioned error does not imply zero off-clause cost; bad degree mass/I=1-(1-2^-w)^(m-1). Exact once-paid product entropy formula.',
    deliverable_status='COMPLETE_LOCAL',mathematical_status='SCOPED_OBSTRUCTION_PROVED_UNREVIEWED; UNRESTRICTED_LINEAR_HYPERGRAPHS_AND_FULL_FEI_OPEN',
    claim_versions_used=[old['claim_id']+'@1','A009 FOREST_TRANSFER.tex scalar transfer (scope only)'],
    claims_created_or_changed=[old['claim_id']+'@2'],
    source_artifacts=['DERIVATION.md','REPORT.md','FROZEN_SPEC.json','BLOCKER_FROZEN_SPEC.json','out/local_check.json','out/blocker_check.json'],
    next_consumers=claim['next_consumers'],next_action='Derive one-shared-variable two-blocker normalized reference with once-paid activation and signed collision cost.',
    stagnant_substantive_attempts=0,blockers=['No general overlapping-blocker whole-set payment; independent review and remote adoption pending','Prior Oct12 full validation output absent; no completion inferred'],packet_ids=['A014'])
save('PROGRESS.json',progress);save('PACKET_DELTA.json',progress)
stamp=datetime.now(timezone.utc).isoformat()
(A/'STATUS.md').write_text('STATE: A014 stage 3 complete locally: zero conditioned error still leaves bad spectral mass/I tending to 1; 21,224 exact assertions PASS; review pending; full FEI OPEN.\nNEXT: Derive one-shared-variable two-blocker whole-set reference paying activation once, then replace A009 all-density transfer error budget.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n'+stamp+' stage 20261013T235200Z: read current BOARD/B03/A009 transfer; preserved interrupted Oct12 artifacts without asserting absent full validation. Re-ran local blocker checks: 20,365 assertions, 169 physical+192 symbolic cases PASS. Independent disjoint-block spectrum implementation: 859 assertions, 7 spectra+256 symbolic cases PASS. Proved bad-degree/I=1-c despite zero conditioned residual; derivative entropy diverges. Exact product whole-function activation identity records required once-paid cost. Full FEI and arbitrary-density overlapping linear hypergraphs remain open.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nStage 3 durable obstruction: for disjoint equal-width positive clauses p=2^-w,c=(1-p)^(m-1), local conditioned derivative residual is zero but bad off-clause degree mass=I(1-c). Thus conditioned Fourier ideals are not gate-supported; never replace bad-set cost by conditioned residual alone. Normalized derivative entropy=w-1+(m-1)[h2(p)+p log2(2^w-1)] is unbounded at zero local pressure. Whole-function identity H=h2(4a(1-a))+4a[m h_g-h2(a)],a=(1-p)^m, pays product blockers once by activation, and suggests the actual overlapping-blocker reference target.\n')
protocol=json.loads(Path('~/mop_fei100/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text())
ckeys=set(protocol['required_per_run']['claim_fields']);pkeys={s.split(' (')[0] for s in protocol['required_per_run']['progress_fields']}
assert set(claim)==ckeys,(set(claim)^ckeys)
assert set(progress)==pkeys,(set(progress)^pkeys)
assert json.loads((R/'PACKET_DELTA.json').read_text())==progress
assert len((A/'STATUS.md').read_text().splitlines())==2
receipts=[]
for pth in sorted(R.rglob('*')):
    if pth.is_file() and pth.name!='RECEIPTS.json':
        assert pth.stat().st_size<20_000_000
        receipts.append({'path':str(pth.relative_to(R)),'bytes':pth.stat().st_size,'sha256':digest(pth)})
save('out/RECEIPTS.json',{'created_utc':stamp,'scope':'Local persistence only; no remote verification','files':receipts})
print(json.dumps({'protocol_schema':'PASS','files_hashed':len(receipts),'assertions':20365+859,'full_fei':'OPEN'}))
