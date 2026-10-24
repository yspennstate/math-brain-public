from pathlib import Path
import json,hashlib,datetime
import copy
R=Path(__file__).resolve().parents[1];AGENT=R.parents[1]
BASE=Path(r'~\brain_workers\FEI100_20261011')
PROTO=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(PROTO.read_text(encoding='utf-8'))
def js(p,obj):p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def statement_hash(c):return hashlib.sha256(json.dumps({'statement':c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
statement='For every balanced Boolean g, integer r>=1 and complete nonempty core spectral subprobability reference R_g of finite cost c_g, with p=2^(-r) and F=1+A_r(g-1) on fresh independent point controls, the explicit complete output subprobability reference Q_F has vacuum mass (1-p)^2, control-only nonempty mass p^2 per set, and mass p^2 R_g(T) for every control set U and nonempty data set T. It has total mass 1-p+p sum R_g and exact cost CE(P_F,Q_F)=p*c_g+A_r, A_r=2rp(2-p)+(1-p)^2 log2(1/(1-p)^2). The sharp universal selector coefficient is max_{r>=1} A_r/(rp)=C_act=15/4+(49/12)log2(8/7) in (4.536,4.537), uniquely attained at r=3. For the true control-first witness W retaining its physical stopping/core leaf J, actual leaf spectrum and queried membership bits, H(W|S)=2(1-p)+sum_{k=1}^r 2^(-(r-k)) B_k-A_r, B_k=q_k h2(epsilon_k)+(1-m_k^2)/2, m_k=1-2^(-(k-1)), q_k=(1+m_k^2)/2, epsilon_k=2^(-2(k-1))/(2(1+m_k^2)). This posterior is independent of the balanced core and tends to two bits. Disjoint-reference composition and fresh-character balancing preserve the full core bill; no arbitrary-core influence bound or shared-control transfer is assumed.'
hyp=['Uniform finite data cube, Boolean sign g, Eg=0','r>=1 fresh independent point controls','Fixed complete nonempty spectral subprobability core reference with finite cross entropy; all costs in bits','Actual control-first coupling using the original Boolean child coefficients; zero packets omitted','Ideal cross-entropy cost; one-symbol integer prefix rounding is separate','Disjoint original variable blocks for reference-product claims']
new=dict(claim_id='A012-CONTROL-FIRST-POSTERIOR-REPAIR',version=1,exact_statement=statement,hypotheses=hyp,statement_sha256='',contributors=['account05/A012'],proof_source={'path':str(R/'DERIVATION.md'),'tex':str(R/'POSTERIOR_ACTIVATION.tex'),'validation':str(R/'out'/'EXACT_RESULTS.json')},proof_dependencies=[],review_records=[],status='AUTHOR_PROVED_REPAIR_PENDING_INDEPENDENT_REVIEW',supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A011','A013','A015','A039','A097','A086','A094','B20'])
new['statement_sha256']=statement_hash(new)
source13=BASE/'agents'/'A013'/'runs'/'20261011T221511Z-account05-A013-representation-stability'
original=json.loads((source13/'CLAIMS.json').read_text(encoding='utf-8'))[0]
reviewed=copy.deepcopy(original)
reviewed['review_records'].append({'reviewer':'account05/A012','verdict':'HOLDS_AT_SPECIFIED_SUBCLAIM_SCOPE','scope':'Balanced-core vacuum-separated activation reference with original coefficient 6+2/ln2, and explicitly stated disjoint-reference/balancing iteration only; remaining cover/restriction/reuse clauses NOT ACCEPTED by this review.','method':'Independent geometric-series normalization and exact cross-entropy proof; separate integer-FWHT/Fraction implementation; ten outward rational certificate fixtures','source':str(R/'A013_ACTIVATION_REVIEW.md'),'source_statement_sha256':original['statement_sha256'],'contributor_conflict':'No substantive repair to the reviewed original clause; A012 contributes to the separate refined repair and cannot independently accept that refinement.'})
reviewed['status']='PARTIALLY_INDEPENDENTLY_REVIEWED_LOCAL'
reviewed['review_records'][-1]['source_hash_convention']='Original A013 finalize.py computes SHA256 of UTF-8 exact_statement alone; preserved as source provenance. A012 new repair uses protocol-registry canonical statement+hypotheses JSON digest.'
claims=[new,reviewed];js(R/'CLAIMS.json',claims)
progress=dict(protocol_revision=protocol['revision'],run_id=R.name,stream='B03',packet_id='A012',gap_id='FEI-B03-A012-INITIAL',attempt_id='A012-posterior-erasure-v2',method='Consume/independently review A013 activation clause; exact true-witness posterior and sharp coherent-sector output reference; all-r scalar tail plus rational finite certificates',mathematical_delta='Solved exact balanced control-first posterior/reference transfer: CE=p*c_g+A_r, sharp selector coefficient C_act in (4.536,4.537) at r=3; posterior independent of core tends to two bits. Scoped original A013 activation clause independently accepted locally; arbitrary core and collision payment remain open.',deliverable_status='COMPLETE_LOCAL_ARTIFACT',mathematical_status='ACTIVATION_REPAIR_PROVED_UNREVIEWED_SCOPED_DEPENDENCY_REVIEW_COMPLETE_FULL_FEI_OPEN',claim_versions_used=['A012-HEREDITARY-ACTIVATION-ADMISSION@1 physical-label obstruction; A011 locally accepted that subclaim in its stage-2 review','A013-VACUUM-PROJECTED-COVER-STABILITY@1 activation-only clause independently reconstructed/accepted locally in this stage','A011 control-first coupling and comb-output repair are source interfaces, not unreviewed proof premises'],claims_created_or_changed=['A012-CONTROL-FIRST-POSTERIOR-REPAIR@1','A013-VACUUM-PROJECTED-COVER-STABILITY@1 activation-only partial independent review'],source_artifacts=['REPORT.md','DERIVATION.md','POSTERIOR_ACTIVATION.tex','A013_ACTIVATION_REVIEW.md','out/FROZEN_SPEC.json','code/check_posterior.py','out/EXACT_RESULTS.json','out/SHARP_SELECTOR_CERTIFICATES.json','out/POSTERIOR_FIXTURES.json','out/A013_REVIEW_CERTIFICATES.json','out/SOURCE_RECEIPTS.json'],next_consumers=new['next_consumers'],next_action='A086/A094 review exact posterior/sharp scalar certificates; derive complete compatible reference transfer for two colliding nonconstant children, retaining terminal core and empty-row normalization.',stagnant_substantive_attempts=0,blockers=[],packet_ids=['A012'])
js(R/'PROGRESS.json',progress);js(R/'PACKET_DELTA.json',progress)
paths=[PROTO,BASE/'BOARD.md',BASE/'claude'/'B03'/'STREAM_NOTES.md',source13/'REPORT.md',source13/'CLAIMS.json',source13/'COVER_STABILITY.tex',BASE/'context'/'threshold_paper_38pp.txt']
for run in ['20261011T213831Z-account05-A011-representation-existence','20261011T232009Z-account05-A011-representation-existence']:
    paths+=[BASE/'agents'/'A011'/'runs'/run/x for x in ['REPORT.md','CLAIMS.json']]
paths+=[AGENT/'runs'/'20261011T215648Z-account05-A012-sparse-activation-accounting'/x for x in ['REPORT.md','CLAIMS.json']]
for agent in ['A005','A015','A028']:
    paths+=list((BASE/'agents'/agent/'runs').glob('*/REPORT.md'))
js(R/'out'/'SOURCE_RECEIPTS.json',[dict(path=str(p),bytes=p.stat().st_size,sha256=h(p)) for p in paths])
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A012 stage 2 complete: exact posterior-erased CE=p*c_g+A_r, sharp control coefficient 4.536.. at r=3; 269,139 exact checks; A013 activation-only review HOLDS locally; new repair review pending; FEI OPEN.\nNEXT: A086/A094 audit; derive complete reference transfer for two colliding nonconstant children with terminal conditional core cost and empty-row normalization retained.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp} | {R.name}\nRead board 23:39Z, B03 lead v2, own status and source A013/A011 refinements. Followed lead activation target without redoing coarse repair. Independently accepted only original A013 activation/reference iteration clause (no repair to its proof). Derived exact true physical-leaf posterior independent of balanced core and tending to 2 bits; direct coherent-sector subprobability reference has CE=p*c_g+A_r and sharp selector coefficient 15/4+(49/12)log2(8/7), maximum r=3. Frozen 390 Boolean/1170 reference cases passed 269,139 exact assertions in 12.219 s. Core deficit retained exactly: CE-H=p(c_g-H(g)); arbitrary tensors keep p*t*c_f. New refined repair pending independent review; universal core/collision cost remains open. Local artifacts/receipts saved only in A012.\n')
with (AGENT/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('''
## Stage 2: exact posterior-erased control-first reference

* Balanced fresh activation has a complete subprobability output reference Qvac=(1-p)^2, Qctl=p^2 per nonempty control subset, Qdata(U,T)=p^2 R_g(T). Mass=1-p+p sum R_g; CE=p*c_g+A_r exactly, A_r=2rp(2-p)+L((1-p)^2). The core subprobability penalty is retained: CE-H=p(c_g-H(g)).
* The sharp coefficient A_r/(rp) over integer r>=1 is attained uniquely at r=3: C_act=15/4+(49/12)log2(8/7), in (4.536,4.537). r=1..5 certified by outward rational intervals; r>=6 has c_r<4.5 from ln2>2/3. This is a sharp ideal activation-reference transfer constant, not an optimal universal FEI constant.
* Exact true control-first witness posterior: H(W|S)=D+sum_k2^(-(r-k))B_k-A_r, D=2(1-p), B_k=q_k h2(epsilon_k)+(1-m_k^2)/2, m_k=1-2^(-(k-1)), q_k=(1+m_k^2)/2, epsilon_k=2^(-2(k-1))/(2(1+m_k^2)). W=(physical leaf J, output S), so D-A_r<=posterior<=D and it tends to 2 bits independently of the balanced core.
* A013-VACUUM-PROJECTED-COVER-STABILITY@1 original balanced-activation clause and stated disjoint-reference/balancing iteration independently accepted locally at exactly that subclaim scope. Other cover/restriction clauses not accepted here. No repair was needed to its original proof; the sharp sector generator is a separate refinement.
* Exact pilot n=1,2,3 balanced cores, r=1..5: 78 cores, 390 Boolean cases, 1170 reference cases, 269139 assertions PASS. Integer FWHT/Fraction/prime-log identities and outward atanh-series intervals; signed quotient uses all four corners. No automatic n escalation or heavy compute.
* This output reference does not decode a physical history; ideal cross entropy and one-symbol prefix rounding are different bills. Fresh balanced activation, disjoint tensors and character balancing are covered. General unbalanced restrictions/shared controls/colliding nonconstant children remain unproved. Arbitrary balanced tensors keep their full p*t*c_f core bill.
''')
assert set(progress)=={x.split(' (')[0] for x in protocol['required_per_run']['progress_fields']}
for c in claims:
    assert set(c)==set(protocol['required_per_run']['claim_fields'])
    if c['claim_id']==original['claim_id']:
        assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
    else:
        assert statement_hash(c)==c['statement_sha256']
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
report=(R/'REPORT.md').read_text(encoding='utf-8')
assert all(x in report for x in protocol['required_per_run']['report_fields'])
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert len((AGENT/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
allpaths=[p for p in R.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']+[AGENT/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
for p in allpaths:assert p.stat().st_size<20_000_000
js(R/'out'/'PERSISTENCE_RECEIPTS.json',dict(saved_at_utc=stamp,local_only=True,remote_copy_verified=False,files=[dict(path=str(p),bytes=p.stat().st_size,sha256=h(p)) for p in allpaths]))
print(json.dumps({'status':'PASS','protocol_fields_exact':True,'claim_hashes_valid':True,'delta_identical':True,'two_line_status':True,'files_receipted':len(allpaths),'local_only':True}))
