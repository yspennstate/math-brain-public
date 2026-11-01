from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[1]; A=R.parents[1]
r=json.loads((R/'out/LEAN_RESULT.json').read_text()); log=(R/'out/LEAN_CHECK.txt').read_text(encoding='utf-8')
assert r['exit_code']==0 and 'error:' not in log and 'sorryAx' not in log
for name in ['coefficient_cross_comparison','rational_normalized_coefficient','scalar_series_coefficient','factorial_split','even_factorial','all_partial_sums']:
    assert f"'FEIJS.{name}' depends on axioms:" in log
s='Let O_0=E_0=1, O_(n+1)=(2n+1)O_n and E_(n+1)=(2n+2)E_n. For all natural n>=1, E_n<=2n O_n, 1/(2n)<=O_n/E_n and 1/[2n(2n-1)]<=(O_n/E_n)/(2n-1). Also (2n)!=O_n E_n and E_n=2^n n!. For every rational t>=0 and natural N, the first N entropy-series coefficient terms times t^n sum to at most the first N square-root-series coefficient terms times t^n, as defined in JSCoefficients.lean.'
h=['exact recursively defined natural O_n,E_n and factorial','n>=1 for coefficient comparisons','rational t>=0 for finite partial sums','no real-series, Fourier, Boolean or entropy assumptions in formal theorem']
payload=json.dumps({'exact_statement':s,'hypotheses':h},sort_keys=True,separators=(',',':'))
c={'claim_id':'A083-JS-COEFFICIENT-CORE','version':1,'exact_statement':s,'hypotheses':h,'statement_sha256':hashlib.sha256(payload.encode()).hexdigest(),'contributors':['A083'],'proof_source':{'run_id':R.name,'path':'code/JSCoefficients.lean','theorems':['coefficient_cross_comparison','rational_normalized_coefficient','scalar_series_coefficient','factorial_split','even_factorial','all_partial_sums']},'proof_dependencies':[],'review_records':[],'status':'KERNEL_CHECKED_PENDING_INDEPENDENT_REVIEW','supersedes':[],'refutes':[],'first_unproved_line':None,'next_consumers':['A081','A085','A090','A094','B17']}
(R/'CLAIMS.json').write_text(json.dumps([c],indent=2)+'\n',encoding='utf-8')
p={'protocol_revision':'2026-10-11-execution-v2','run_id':R.name,'stream':'B17','packet_id':'A083','gap_id':'G-A083-B17-JS-COEFFICIENT-COMPARISON','attempt_id':'A083-JS-1','method':'Lean core Nat induction, factorial product identities, rational coefficient and finite partial-sum comparison','mathematical_delta':'Kernel-checks all-index coefficient step of B17-JS-PACKET-SCALAR and all rational nonnegative finite partial sums. Real analytic identities and endpoint passage explicitly outside formal scope; no new universal FEI payment.','deliverable_status':'COMPLETE_LOCAL','mathematical_status':'COEFFICIENT_CORE_KERNEL_CHECKED_FULL_SCALAR_ANALYTIC_ONLY_FEI_OPEN','claim_versions_used':[],'claims_created_or_changed':['A083-JS-COEFFICIENT-CORE-v1'],'source_artifacts':['REPORT.md','FORMAL_SCOPE.md','code/JSCoefficients.lean','out/LEAN_CHECK.txt','out/LEAN_RESULT.json','out/SOURCE_RECEIPTS.json'],'next_consumers':['A081','A085','A090','A094','B17'],'next_action':'A090/A094 check coefficient/analytic interface; A081 annotate C005 JS scope, then prioritize an unpaid C018/C019 erasure residual rather than another formal baseline.','stagnant_substantive_attempts':0,'blockers':['Independent review and supervisor mirror pending; full real analytic scalar theorem is not formalized'],'packet_ids':['A083']}
for f in ['PROGRESS.json','PACKET_DELTA.json']:
    (R/f).write_text(json.dumps(p,indent=2)+'\n',encoding='utf-8')
protocol=json.loads(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json').read_text())['required_per_run']
assert set(p)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert set(c)==set(protocol['claim_fields'])
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(A/'STATUS.md').write_text('STATE: A083 stage 2 complete: JS all-index coefficient, factorial identities and rational finite partial sums kernel-checked; real analytic scalar bridge reconstructed outside Lean; FEI OPEN, review pending.\nNEXT: A090/A094 audit formal-to-analytic scope; A081 use it for C005 JS only, then target an unpaid C018/C019 erasure residual rather than repeat closed baselines.\n',encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp}: Followed B17 v2 JS coefficient assignment. Core Nat/Rat formalization checked product positivity, factorial bridges, E_n<=2nO_n for all n>=1, divided coefficient comparison and every rational nonnegative finite partial sum. First draft rational simplification required mul_one; repaired. memok exit 1 postponed retry. Final check: {r["seconds"]:.3f}s, peak commit {r["peak_commit_bytes"]} bytes. Real series and endpoints remain outside kernel scope; universal erasure debt untouched.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('\nJS coefficient core: O_n=product_(j=1..n)(2j-1), E_n=product_(j=1..n)2j. Kernel-checked E_n<=2n O_n (n>=1), factorial(2n)=O_n E_n and E_n=2^n factorial(n). Hence normalized central-binomial coefficients dominate 1/(2n); after division by 2n-1 every JS scalar-series coefficient is paid. All rational t>=0 finite partial sums checked. Real-series identities, convergence, endpoint continuity and spectral packet reduction are analytic interfaces, not Lean claims.\n')
rows=[]
for f in sorted(R.rglob('*')):
    if f.is_file() and f.name!='ARTIFACT_RECEIPTS.json':
        b=f.read_bytes(); assert len(b)<20*2**20
        rows.append({'path':str(f.relative_to(R)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(R/'out/ARTIFACT_RECEIPTS.json').write_text(json.dumps({'saved_at':stamp,'scope':'local persistence; mirror pending','files':rows},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'schema':'PASS','claims':1,'artifact_count':len(rows),'Lean':r['status'],'seconds':r['seconds'],'peak_commit_bytes':r['peak_commit_bytes'],'full_FEI':'OPEN'}))
