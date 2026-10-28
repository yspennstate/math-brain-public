import json,hashlib,datetime
from pathlib import Path
from fractions import Fraction as F
import review
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def dump(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def sha(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
initial=R/'out/INITIAL_REVIEW_CHECKS.json'
if not initial.exists():initial.write_bytes((R/'out/REVIEW_CHECKS.json').read_bytes())
review.main() # identical frozen domain, corrected pre-run count only
result=json.loads((R/'out/REVIEW_CHECKS.json').read_text(encoding='utf-8'))
assert result['literal_original_projection_profiles']==1640
assert result['row_profiles']['count']==8748
ghost=json.loads((R/'out/GHOST_ROWS.json').read_text(encoding='utf-8'))
assert ghost['assignments']==243 and F(ghost['max_ratio'])==F(16,7)
assert 16**5<2**6*7**5
assert F(11,8)-F(2*5+34,2**5)==0
assert F(11,8)-F(2*5,2**5)-F(41,2*2**5)==F(27,64)
for k in range(5,65):
    for c in (F(34),F(41,2)):
        assert F(2*(k+1)+c,2**(k+1))<F(2*k+c,2**k)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
source=Path('agents/A019/runs/20261026T211700Z-account04-A019-orthogonality-extensions')
original=json.loads((source/'CLAIMS.json').read_text(encoding='utf-8'))[0]
sourcehash='82362ae124b321eb8385a001db6c1a1f2d8f0f27790ef372e69c77d22e8b124f'
assert sha(original['exact_statement'])==original['statement_sha256']==sourcehash
def claim(cid,statement,hypotheses,status,deps,records):
    return dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hypotheses,statement_sha256=sha(statement),contributors=['A016/account04'],proof_source=['REPORT.md','code/review.py','code/ghost.py','out/BLOCK_CERTIFICATES.json','out/REVIEW_CHECKS.json','out/GHOST_ROWS.json'],proof_dependencies=deps,review_records=records,status=status,supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A019','A020','A018','A094','B04 lead'])
cid='A016-REVIEW-A019-UNBOUNDED-MIXED-CLEANED'
c1=claim(cid,
    'Independent reconstruction HOLDS unchanged for A019-UNBOUNDED-MIXED-ADAPTIVE-CLEANED-FRONTIER@1 at SHA256 '+sourcehash+': for the stated original balanced padded E-product source, k,j>=5, every finite adaptive mixed padding/source tree with compulsory terminal source cleanup retains original expected reserve greater than 27/32 for either q sign after the SAME U. Original eligibility, all full terminals, exact source coefficient and posterior partition identity are reconstructed. No material repair; no arbitrary-core supplier or full FEI conclusion.',
    original['hypotheses'],'INDEPENDENT_RECONSTRUCTION_HOLDS_FULL_STATED_SCOPE',[],[
        dict(reviewer='A016/account04',independent=True,source_claim=dict(claim_id=original['claim_id'],version=1,statement_sha256=sourcehash),verdict='HOLDS_UNCHANGED_FULL_STATED_SCOPE',substantive_repair=False,reviewed_at=now,method='Separate direct-character, physical-edge and original-parent projection reconstruction; exact integer and rational-log certificates; complete analytic review in REPORT.md')])
c2=claim('A016-POSTERIOR-WEIGHTED-GHOST-CLEANUP-BUDGET',
    'For the SAME original family, reference and U of A019-UNBOUNDED-MIXED-ADAPTIVE-CLEANED-FRONTIER@1, let q be queried first and allow any finite adaptive padding/source policy with u,mask,gate unqueried, all outcomes retained, and optional source cleanup. At a terminal let M count E blocks with at least one irrelevant remaining source coordinate, and r=Pr(original padding event V|leaf). Virtual cleanup has ghost debt D>=0 and D<=log2(16/7) M, with exact max likelihood ratio16/7 on the243-state block domain. For either q sign the SAME original full expected reserve obeys E W>=2-U-(2k+7)rho-E[rD]/4>11/8-rho[2k+7+(log2(16/7)/4)E(M|V)]. Therefore E(M|V)<=90 implies E W>0, and E(M|V)<=45 implies E W>27/64, for every k,j>=5. This supplies a sufficient posterior ghost budget, not arbitrary uncleaned-policy payment, pointwise terminal eligibility, or a universal Boolean source supplier.',
    ['Exactly the original actual Boolean family, k,j>=5, reference and unchanged booked U in the reviewed source.','Finite physical cylinder partitions retaining all outcomes; q first; u,mask,gate unqueried; E blocks disjoint but their internal shared coordinate physical.','The conditional ghost-count budget is required separately for each q sign when claiming its corresponding expected reserve.','No reference reset, renormalization, new influence credit, or discarded sibling.'],
    'PROOF_ANALYTIC_EXACT_CERTIFICATES_INDEPENDENT_REVIEW_PENDING',[dict(claim_id=cid,version=1,statement_sha256=c1['statement_sha256'])],[])
claims=[c1,c2];dump(R/'CLAIMS.json',claims)
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=R.name,stream='B04',packet_id='A016',gap_id='C024-ORIGINAL-SOURCE-EXCESS-TO-C019',attempt_id='A016-stage22-review-unbounded-mixed-and-ghost-budget',method='Independent source-bound review plus exact physical restriction certificates and posterior-weighted ghost-price extraction',mathematical_delta='A019 unbounded mixed cleaned frontier independently HOLDS unchanged. New exact per-block ghost ratio16/7 yields full same-owner residual invoice; <=90 conditional expected ghost blocks paid, <=45 retains>27/64. Arbitrary-core initial source remains unpaid; FEI OPEN.',deliverable_status='COMPLETE_LOCAL',mathematical_status='SCOPED_REVIEW_HOLDS_NEW_COROLLARY_REVIEW_PENDING_FULL_FEI_OPEN',claim_versions_used=[dict(claim_id=original['claim_id'],version=1,statement_sha256=sourcehash)],claims_created_or_changed=[dict(claim_id=c['claim_id'],version=1,statement_sha256=c['statement_sha256']) for c in claims],source_artifacts=['out/SOURCE_RECEIPTS.json',str(source/'REPORT.md'),str(source/'CLAIMS.json'),'REPORT.md','code/review.py','code/ghost.py','out/REVIEW_CHECKS.json','out/GHOST_ROWS.json'],next_consumers=['A019','A020','A018','A094','B04 lead'],next_action='Price actual posterior-weighted ORIGINAL source excess outside the disjoint-E supplier from SAME unused original reserve; A020/A018 review equation(2), ratio16/7 and90/45 budgets.',stagnant_substantive_attempts=0,blockers=['No arbitrary indecomposable influence-priced ORIGINAL source/reference supplied.','New ghost corollary independent review pending; no Lean certification, supervisor copy or mirror verification.'],packet_ids=['A016'])
dump(R/'PROGRESS.json',progress);dump(R/'PACKET_DELTA.json',progress)
(A/'STATUS.md').write_text('STATE: A016 stage22 COMPLETE_LOCAL: A019 unbounded mixed cleaned frontier HOLDS unchanged; ghost ratio16/7,conditional90 blocks paid/45 reserve>27/64; exact checks PASS;FEI OPEN.\nNEXT: A020/A018 review posterior ghost invoice;fund NECESSARY arbitrary-core ORIGINAL source excess from SAME unused owner,old U/all full terminals;no more E-family query counts.\n',encoding='utf-8')
for name,text in [('WORKLOG.md','2026-10-27 A016 stage22: independently reconstructed unchanged A019 unbounded adaptive mixed-cleaned theorem and original root/U. Main exact50472 checks plus ghost541; all243 states,1640 literal profiles,8748 row profiles. Max actual-support ghost ratio16/7; posterior invoice permits conditional expected90 ghost-bearing E blocks (>0 reserve) or45 (>27/64), SAME original owner. Frozen count underestimated literal fixtures; corrected count before identical-domain rerun, raw first result preserved. FEI OPEN; next arbitrary-core source excess, A020/A018 review.'),('LEARNED.md','2026-10-27: Source-query occupation is not the right bill in the balanced padded E family. Core source CE has exact coefficient r/2, and E[rD]=rho E[D|V] for the ORIGINAL padding event even under arbitrary adaptive mixing. Independent A019 review HOLDS. Virtual irrelevant-source cleanup has D=E_P log(R_clean/R_unclean_zero); every partial E state has actual-support ratio<=16/7, sharp at[-1,-1,1,-1,1]. Thus D<=log2(16/7) M<6M/5, and original E W>11/8-rho[2k+7+lambda E(M|V)/4]. Conditional M<=90 pays all terminals for k>=5; M<=45 leaves>27/64. This is a sufficient posterior ghost budget; arbitrary-core CE-4I remains unpaid. Spec counts must include duplicate/constant fixtures; preserve a mismatched initial output and correct before rerun.')]:
    p=A/name;old=p.read_text(encoding='utf-8') if p.exists() else ''
    if text not in old:p.write_text(old.rstrip()+'\n\n'+text+'\n',encoding='utf-8')
protocol=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
cf=set(protocol['required_per_run']['claim_fields']);pf={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
assert all(set(c)==cf for c in claims);assert set(progress)==pf
assert json.loads((R/'PACKET_DELTA.json').read_text(encoding='utf-8'))==progress
report=(R/'REPORT.md').read_text(encoding='utf-8');assert all('## '+h in report for h in protocol['required_per_run']['report_fields'])
assert '## Universal bridge' in report;assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[]
for p in R.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        b=p.read_bytes();assert len(b)<20_000_000;files.append(dict(path=str(p.relative_to(R)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest()))
dump(R/'out/PERSISTENCE_RECEIPTS.json',dict(status='PASS',saved_at=now,schemas_exact=True,statement_hashes_checked=True,progress_delta_equal=True,status_two_lines=True,final_rerun=result,ghost_checks=ghost['checks'],spec_count_correction='INITIAL_REVIEW_CHECKS preserved; identical domains rerun after corrected frozen count1640',remote_copy='UNVERIFIED',independent_review_of_new_corollary='PENDING',lean='NOT_RUN_RESOURCE_CAP',files=files))
print(json.dumps(dict(status='COMPLETE_LOCAL',claims=len(claims),files=len(files),final_rerun_checks=result['checks'],ghost_checks=ghost['checks'],full_fei='OPEN')))
