"""Persist A041 protocol-exact claim/progress files and local receipts."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json

root=Path(__file__).resolve().parents[1]
agent=root.parents[1]
protocol_path=Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
protocol=json.loads(protocol_path.read_text(encoding='utf-8-sig'))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def save(name,data):
    (root/name).write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
def claim(cid,statement,hypotheses,proof,consumers,refutes=()):
    obj={'claim_id':cid,'version':1,'exact_statement':statement,
         'hypotheses':hypotheses,
         'statement_sha256':hashlib.sha256(json.dumps(
             {'statement':statement,'hypotheses':hypotheses},
             sort_keys=True,separators=(',',':')).encode('utf-8')).hexdigest(),
         'contributors':['fleet05/A041'],
         'proof_source':{'path':str(root/proof),'sha256':sha(root/proof)},
         'proof_dependencies':[],
         'review_records':[],
         'status':'AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
         'supersedes':[],'refutes':list(refutes),'first_unproved_line':None,
         'next_consumers':consumers}
    assert set(obj)==set(protocol['required_per_run']['claim_fields'])
    return obj

claims=[claim('A041-BIASED-WEIGHT-BAND-MULTISCALE-RANK',
    'For every finite increasing weighted threshold f=2*1{sum w_j X_j>=t}-1 with arbitrary positive real weights and independent interior Bernoulli(q_j) inputs, every i with pivotal probability rho_i>0, and every integer r>=1, let d_i be the pivotal interval indicator, nu_i(B)=dhat_i(B)^2/rho_i in the orthonormal product Fourier basis, U_i,r={j!=i:w_j>=w_i/r}, L_i,r=2 sum_{j in U_i,r} min(q_j,1-q_j), and K_i,r(B)=|B intersect U_i,r|. For 0<epsilon<=1, E_nu_i (1-epsilon)^K_i,r <= min(1,r/sqrt(epsilon L_i,r)). With r_k=2^k and pi_k=1/[(k+1)(k+2)], put R_i(B)=sup_{k>=0} pi_k^2 L_i,r_k/[4^k(K_i,r_k(B)+1)]. Then Pr_nu_i(ln^+ R_i>u)<=min(1,sqrt(2e)*exp(-u/2)) for u>=0, E_nu_i ln^+ R_i<=3+ln 2, and sum_i sum_{S containing i} fhat_mu(S)^2 ln^+ R_i(S without i)<=(3+ln 2) I_mu(f). A zero L gives score zero and noise upper bound one. Signed weights are oriented and zero weights/deterministic inputs contracted. This is a rank payment in natural units, not a corrected FEI+ theorem.',
    ['actual Boolean weighted threshold','arbitrary finite arity and real threshold',
     'independent product input law; endpoints contracted','orthonormal product Fourier basis',
     'natural logarithms; scale prior fixed before sampling'],
    'WEIGHTED_THRESHOLD_REPLACEMENT.tex',
    ['A042','A044','A045','A068','A084','A090','A091','B20']),
    claim('A041-BOOLEAN-ONE-BIT-ENDPOINT-TAX-LOWER-BOUND',
    'Let X~Ber(p), Y~Ber(1/4) be independent and f=1-2XY. For the physical reveal A={X}, let M=H(S_X|S_Y) under the squared orthonormal product Fourier law and J=H(S_Y)-E_X H(spectrum(f_X)), in bits. Then lim_{p downarrow 0}(J-M)/[p log_2(1/p)]=1/2. Therefore every scalar tau(p) making J<=M+tau(p) valid for all Boolean functions, all product measures, and one-bit physical reveals satisfies liminf_{p downarrow 0} tau(p)/[p log_2(1/p)]>=1/2; no fixed finite O(p) correction is sufficient. No optimality of coefficient one or composition payment is asserted.',
    ['actual Boolean two-input sign AND','independent p in (0,1), fixed q=1/4',
     'one-coordinate physical reveal','orthonormal product Fourier basis','entropy in bits'],
    'ENDPOINT_TAX_LOWER_BOUND.tex',['A042','A045','A090','A091','B09','B13','B20'],
    ['Universal scalar one-bit uncertainty correction tau(p)<=K*p for fixed finite K'])]
save('CLAIMS.json',claims)

progress={
    'protocol_revision':'2026-10-11-execution-v2',
    'run_id':root.name,'stream':'B09','packet_id':'A041',
    'gap_id':'G-BIASED-LTF','attempt_id':'A041-BIASED-LTF-01-PIVOTAL-WEIGHT-BANDS',
    'method':'Biased fair-activation refresh, bounded-height pivotal fibers, normalized dyadic scale prior; actual Boolean endpoint expansion',
    'mathematical_delta':'Proved arity/weight/bias-independent multiscale pivotal spectral-rank payment (3+ln 2) I in nats, surviving all recovered controls. Proved actual Boolean endpoint tax lower coefficient 1/2 in bits, repairing the unsupported O(p)-impossibility inference. Higher-degree corrected entropy versus Delta remains unpaid.',
    'deliverable_status':'COMPLETE_LOCAL_REVIEW_PENDING',
    'mathematical_status':'AUXILIARY_REPLACEMENT_AND_ENDPOINT_LOWER_BOUND_PROVED; WEIGHTED_FEIPLUS_AND_FULL_FEI_OPEN',
    'claim_versions_used':[],
    'claims_created_or_changed':[{'claim_id':c['claim_id'],'version':1} for c in claims],
    'source_artifacts':['REPORT.md','WEIGHTED_THRESHOLD_REPLACEMENT.tex','ENDPOINT_TAX_LOWER_BOUND.tex',
        'WEIGHTED_GUARD_LEDGER.md','out/SOURCE_RECEIPTS.json','out/EXACT_VALIDATION.json',
        'out/ENDPOINT_VALIDATION.json'],
    'next_consumers':['A042','A044','A045','A068','A084','A090','A091','B20'],
    'next_action':'A091 reconstructs the refresh/tail/prior proof and A090 the endpoint expansion; build a normalized higher-degree spectral reference retaining variance normalization and near-dictator costs.',
    'stagnant_substantive_attempts':0,
    'blockers':[],
    'packet_ids':['A041']}
# Protocol lists "packet_ids (one primary ID, for compatibility)" as a
# documented field label; the compatibility instruction specifies packet_ids.
progress_fields={k.split(' (',1)[0] for k in protocol['required_per_run']['progress_fields']}
assert set(progress)==progress_fields
save('PROGRESS.json',progress)
save('PACKET_DELTA.json',progress)
assert (root/'PROGRESS.json').read_bytes()==(root/'PACKET_DELTA.json').read_bytes()

(agent/'STATUS.md').write_text(
    'STATE: A041 stage complete locally: multiscale biased-weight rank bound and Boolean endpoint tax lower coefficient 1/2 proved; 253 exact cases/42,189 assertions; independent review pending; weighted FEI+ and full FEI OPEN.\n'
    'NEXT: A091/A090 review the two claims; construct a normalized higher-degree spectral reference paying I-Var, with explicit near-dictator and variance normalization costs.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write('\n2026-10-12: Proved bounded-height biased pivotal refresh and normalized all-dyadic-scale spectral rank payment <=(3+ln2)I nats. Exact 253-case Fraction pilot passed 42,189 assertions in 1.149s; independent physical kernels checked on designated small cases. Derived actual AND endpoint J-M~(1/2)p log2(1/p), repairing B09 section 5(4); six rational-interval endpoint checks passed in 0.013s. Saved proofs, guard ledger, protocol-exact claims/progress and receipts. Higher-degree corrected entropy payment by Delta remains open. Two complete claims pending independent review.\n')
(agent/'LEARNED.md').write_text(
    '# A041 durable mathematics\n\n'
    '* Product-biased corrected entropy is sum_{S!=empty} P(S) log2(v_S/P(S)); physical influence is v_i*rho_i, not rho_i. Deterministic inputs must be contracted.\n'
    '* A width-w_i pivotal interval has fiber height <=r on coordinates w_j>=w_i/r, for arbitrary positive real weights. Refresh fair mass L=2 sum min(q_j,1-q_j) yields E_nu(1-epsilon)^K<=min(1,r/sqrt(epsilon L)).\n'
    '* The dyadic-scale score sup_k pi_k^2 L_k/[4^k(K_k+1)], pi_k=1/[(k+1)(k+2)], has expected positive natural logarithm <=3+ln2. A sample-dependent scale choice is valid only after retaining its prior square; the tail union sums pi_k, not one per scale.\n'
    '* This pays rank cost by I, not by Delta=I-Var. Singleton corrected entropy is <=4 Delta nats; high-degree corrected entropy remains the exact unpaid term. No weighted FEI+ proof follows without its normalized reference and near-dictator treatment.\n'
    '* All three recovered weighted guards concern physical event-conditioned TC or a coefficient-one pivotal normalization. They do not refute spectral erasure or larger pivotal-credit multipliers. The rank scores vanish on the two-branch rare controls.\n'
    '* Actual f=1-2XY, q_Y=1/4 fixed, p_X->0: (J-M)/[p_X log2(1/p_X)]->1/2. This proves necessity of a logarithmic endpoint tax; the upper-tax asymptotic alone could not prove that. The optimal scalar coefficient remains between 1/2 and 1 given the recovered upper bound.\n'
    '* Exact rational log interval division must use all four numerator/positive-denominator corners when the numerator can be negative. Finite checks do not replace the analytic all-bias/all-weight proof.\n',encoding='utf-8')
receipts=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
        assert p.stat().st_size<20*1024*1024
        receipts.append({'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':sha(p)})
for p in (agent/'STATUS.md',agent/'WORKLOG.md',agent/'LEARNED.md'):
    receipts.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
save('out/PERSISTENCE_RECEIPTS.json',{'saved_at_utc':datetime.now(timezone.utc).isoformat(),
    'protocol_fields_checked':True,'claim_count':2,'progress_delta_identical':True,
    'local_only':True,'artifacts':receipts})
print(json.dumps({'status':'PASS','claim_count':2,'claims_fields':len(claims[0]),
    'progress_fields':len(progress),'progress_delta_identical':True,
    'receipt_count':len(receipts),'largest_bytes':max(r['bytes'] for r in receipts)},indent=2))
