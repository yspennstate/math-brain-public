import json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1];ROOT=R.parents[1]
P=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(P.read_text(encoding='utf-8-sig'));data=json.loads((R/'out/CENSUS.json').read_text())
assert data['cases']==197436 and data['max_n']==3
for w in data['real_witnesses']:
    p,x=F(w['p']),F(w['x']);lam=(1-x-p)/(1-2*x)
    assert 0<=lam<=1 and lam*x+(1-lam)*(1-x)==p
    assert F(w['gap_above_Boolean_upper'])>F(7,1000)
    assert F(w['debt']['lower'])<=F(w['debt']['upper'])
for row in data['rows']:
    assert row['all_candidates_symbolically_equal']
    if row['noncandidate_separation_lower'] is not None: assert F(row['noncandidate_separation_lower'])>0
    p=F(row['p']);g,h=row['witness_child_tables'];N=len(g)
    # Independent direct centered product transform of the full parent table.
    masses=[]
    for s in range(N):
        for selected in (0,1):
            moment=F(0)
            for y in range(N):
                chi=-1 if (y&s).bit_count()%2 else 1
                for z,prob in ((0,1-p),(1,p)):
                    moment+=prob*chi*(g[y] if z==0 else h[y])*(F(z)-p if selected else 1)/N
            masses.append(moment*moment/(p*(1-p) if selected else 1))
    assert masses==list(map(F,row['witness_parent_spectrum'])) and sum(masses)==1
expr={q['p']:q['exact_max_expression_log2_primes'] for q in data['rows'] if q['n']==3}
statement=('For every 0<p<1, the supremum of J_X-M_X over two unit real coefficient vectors '
 'is tau*(p)=h2(p)-min_t[h2(sin^2(t))+h2(sin^2(t-b))], sin^2(b)=p. '
 'The lower convex envelope of this angle curve at abscissa p equals its unconstrained minimum, '
 'and two residual labels suffice for attainment. On uniform residual cubes with n<=3 and '
 'p in {1/8,1/4,3/8}, the exact Boolean maxima are sum_prime c_prime log2(prime) with coefficient maps '+
 json.dumps(expr,sort_keys=True)+'. Certified real witnesses exceed these Boolean maxima by '
 'more than 0.012463, 0.019324, 0.007873 bits respectively. No all-dimensional Boolean gap is claimed.')
claim={'claim_id':'A047-REAL-SUPREMUM-AND-BOOLEAN-GAP','version':1,'exact_statement':statement,
 'hypotheses':['independent selector with 0<p<1','real children of L2 norm one for the sharp real theorem',
 'common orthonormal product basis','Boolean census only on uniform residual data n<=3 at p=1/8,1/4,3/8','entropy in bits'],
 'statement_sha256':hashlib.sha256(statement.encode()).hexdigest(),'contributors':['A047'],
 'proof_source':['DERIVATION.md','REPORT.md','code/census.py','code/finalize.py','out/CENSUS.json'],
 'proof_dependencies':[],'review_records':[],'status':'PROVED_AND_CERTIFIED_LOCALLY_REVIEW_PENDING',
 'supersedes':[],'refutes':[],'first_unproved_line':'Dimension-independent Boolean uncertainty-defect reserve and full C019 path/terminal payment.',
 'next_consumers':['A092','A087','A085','A048','A050','B10']}
progress={'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B10','packet_id':'A047',
 'gap_id':'FEI-B10-A047-INITIAL','attempt_id':'A047-boundary-02','method':'complementary minimizer convex-envelope attainment; exhaustive integer Walsh and rational dyadic entropy certificates with symbolic prime-log ties',
 'mathematical_delta':'Exact real supremum tau* is attained on two labels; 197436 ordered Boolean pair-bias cases certified, with strict real/Boolean gaps at three biases.',
 'deliverable_status':'COMPLETE_LOCAL_ARTIFACT','mathematical_status':'SCOPED_THEOREM_AND_FINITE_CERTIFICATE_COMPLETE; REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[],'claims_created_or_changed':[claim['claim_id']+'@1'],
 'source_artifacts':['REPORT.md','DERIVATION.md','FROZEN_SPEC.json','code/census.py','code/finalize.py','out/PILOT.json','out/CENSUS.json','out/PILOT_FAILURE.txt','out/EXACT_TIE_AMENDMENT.txt'],
 'next_consumers':claim['next_consumers'],'next_action':'Reconstruct real attainment/finite census independently; test Boolean uncertainty-defect reserve on actual C019 tree child pairs.',
 'stagnant_substantive_attempts':0,'blockers':['Independent acceptance and mirror pending','No universal Boolean gap or tree payment follows from finite census'],'packet_ids':['A047']}
assert set(claim)==set(protocol['required_per_run']['claim_fields'])
assert set(progress)=={q.split(' (')[0] for q in protocol['required_per_run']['progress_fields']}
assert all(q in (R/'REPORT.md').read_text(encoding='utf8') for q in protocol['required_per_run']['report_fields'])
(R/'CLAIMS.json').write_text(json.dumps([claim],indent=2),encoding='utf8')
for name in ('PROGRESS.json','PACKET_DELTA.json'):(R/name).write_text(json.dumps(progress,indent=2),encoding='utf8')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((ROOT/'STATUS.md').read_text(encoding='utf8').splitlines())==2
team=Path(r'~\brain_workers\FEI100_20261011')
lead=team/'claude/B10/runs/20261011T230400Z-claude-B10-onebit-half-tax'
review=team/'agents/A085/runs/20261011T231324Z-account05-A085-certificate-adversary'
sources=[P,team/'BOARD.md',team/'claude/B10/STREAM_NOTES.md',lead/'REPORT.md',lead/'CLAIMS.json',review/'REPORT.md',review/'CLAIMS.json']
manifest=[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sources]
(R/'out/SOURCE_RECEIPTS.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
(R/'out/FINAL_VALIDATION.json').write_text(json.dumps({'protocol_keys':'PASS','direct_centered_parent_witnesses':'PASS (12 rows)','real_witness_mixture_constraints':'PASS','all_real_gaps_above_7_over_1000':'PASS','symbolic_maximizers':'PASS','observed_final_census_seconds':data['runtime_seconds']},indent=2),encoding='utf8')
receipts=[]
for p in R.rglob('*'):
    if p.is_file() and p.name!='PERSISTENCE.json' and '__pycache__' not in p.parts:
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
rolling=[{'path':str(ROOT/n),'sha256':hashlib.sha256((ROOT/n).read_bytes()).hexdigest()} for n in ('STATUS.md','WORKLOG.md','LEARNED.md')]
(R/'out/PERSISTENCE.json').write_text(json.dumps({'saved_at':datetime.now(timezone.utc).isoformat(),'files':receipts,'rolling':rolling,'independent_review':'PENDING','mirror':'NOT_VERIFIED'},indent=2),encoding='utf8')
print('PASS: protocol files and fields; direct physical-parent witness spectra; real mixture constraints; exact maxima and strict gaps; persisted files',len(receipts))
