from pathlib import Path
from datetime import datetime,timezone
import hashlib,json

run=Path(__file__).resolve().parents[1]; agent=run.parents[1]
root=Path(r'~\brain_workers\FEI100_20261011')
repo=Path(r'~\mop_fei100\reports\fei-2026-10-11')
supp=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
up=root/'agents'/'A012'/'runs'/'20261011T234525Z-fleet05-A012-sparse-activation-accounting'
major=root/'agents'/'A006'/'runs'/'20261011T231903Z-fleet05-A006-posterior-forest-optimization'
proto=json.loads((repo/'EXECUTION_PROTOCOL.json').read_text())
now=datetime.now(timezone.utc).isoformat()
sha=lambda b:hashlib.sha256(b).hexdigest()
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

old=json.loads((up/'CLAIMS.json').read_text(encoding='utf-8'))[0]
assert old['claim_id']=='A012-CONTROL-FIRST-POSTERIOR-REPAIR' and old['version']==1
old['review_records']=old['review_records']+[{
 'reviewer':'A015/fleet05','verdict':'ACCEPT_AT_ORIGINAL_STATED_SCOPE_NO_REPAIR',
 'source':str(run/'A012_REVIEW.md'),'source_statement_sha256':old['statement_sha256'],
 'method':'Independent actual-child Fourier recursion for full (physical leaf, output) law; exact entropy in a formal log-prime basis; complete subprobability generator and all-r coefficient reconstruction',
 'validation':str(run/'out'/'EXACT_RESULTS.json'),'reviewer_contributed_repair':False,
 'scope':'Entire original balanced-core control-first repair, sharp constant, exact posterior and explicitly disjoint reference/balancing iteration; not shared-control/collision transfer or original queue-infimum payment',
 'timestamp_utc':now}]
old['status']='INDEPENDENTLY_RECONSTRUCTED_AT_ORIGINAL_SCOPE_LOCAL_ADOPTION_PENDING'

statement=('For any nonconstant Boolean f on n>=1 declared uniform coordinates, its N positive full-cell conjunctions '
 'with pi=2^-n, weights lambda_l=1/N and a common rank order have conditioned exactly-one-root probability '
 'eta=pi/((1+pi/N)^N-1), with exp(-pi)<=eta<=1. Summing their identical one-root/no-child subset laws '
 'cancels both gate labels and root rarity up to -log2 eta. A globally uniform common permutation prior gives '
 'the complete nonempty subprobability R_sym(A)=eta/[2*s*(s+1)*binom(n,s)], s=|A|>=1, of mass eta*n/[2*(n+1)]. '
 'For every probability law P on subsets, the infimum of CE(P,Q) over exchangeable subprobabilities Q is '
 'H(|S|)+E log2 binom(n,|S|), whose exact excess over H(P) is sum_s W_s D(P(.|s)||Uniform_s). '
 'For the actual balanced Boolean family M_r=y+A_r(z-y), r>=1,p=2^-r,n=r+2, every coordinate is relevant, '
 'I=1+r*p, H=(1-p)^2 log2(1/(1-p)^2)+2*r*(2*p-p^2)->0, and W_1=(1-p)^2+p^2. '
 'Every exchangeable reference has CE/I>=W_1 log2(r+2)/(1+r*p)->infinity; its best CE is log2(r+2)+o(1). '
 'The explicit ordered full-minterm one-root reference with y ranked first and exponent-two subset weights '
 'has CE<(639/80)*I<8*I for all r. For a balanced regular core with a desirability order, the same '
 'mandatory-one-gate exponent-two reference has mass n/[2*(n+1)] and c_g<=K_ord*I(g), '
 'K_ord=3+log2(6)+3*log2(e)<101/10, by the stated regular rank mean. '
 'The accepted A012 fresh-activation output construction transfers it with full mass 1-p+p*z and '
 'CE=p*c_g+A_r<=K_ord I(F), retaining D(P_F||Q_F)=p D(P_g||R_g). '
 'The exponent-two ordered reference is explicitly modified from the original exponent-6/5 PI-J law; '
 'this refutes only a universal exchangeable-reference payment, not FEI or an arbitrary function-adapted posterior reference.')
claim={
 'claim_id':'A015-CONDITIONED-MINTERM-LOCATION-BARRIER','version':1,'exact_statement':statement,
 'hypotheses':['Uniform finite Boolean cubes; entropy, CE and all log quantities in bits',
               'All full-cell supports have the same declared coordinate set and a common chosen order',
               'Exactly-one-root/no-child finite-run subreference conditioned on nonempty initial roots',
               'Exchangeable means invariant under all permutations of physical coordinates',
               'Exponent two for the explicit rational ordered-cost repair; the averaged subset identity holds for any exponent >1',
               'Balanced core and fresh independent controls for activation; regular rank mean is a source-bound input only for the stated grouped-gate application',
               'Ideal complete subprobability cross entropy; failure mass retained and single-sample integer-code rounding separate'],
 'statement_sha256':sha(statement.encode()),'contributors':['A015/fleet05'],
 'proof_source':{'path':str(run/'REPORT.md'),'locators':'complete derivation Sections 2--7',
                 'validation':['out/EXACT_RESULTS.json','out/TRANSFER_RESULTS.json']},
 'proof_dependencies':[{'claim_id':'A012-CONTROL-FIRST-POSTERIOR-REPAIR','version':1,
                        'source':str(up/'DERIVATION.md'),'status':'INDEPENDENTLY_ACCEPTED_IN_THIS_STAGE',
                        'scope':'Only the final balanced-core reference-transfer application'},
                       {'source':str(supp/'baseline'/'current-threshold-paper.tex'),
                        'sha256':sha((supp/'baseline'/'current-threshold-paper.tex').read_bytes()),
                        'locator':'lem:ranktail and one-regular-gate derivative-law rank expectation',
                        'status':'SOURCE_COMPLETE_BASELINE_READ','scope':'Only grouped regular-core CE bound'}],
 'review_records':[],'status':'AUTHOR_PROVED_SCOPED_MECHANISM_DIAGNOSTIC_REVIEW_PENDING',
 'supersedes':[],
 'refutes':['Every balanced Boolean spectrum has an exchangeable complete output subprobability reference with CE<=K I for one absolute K',
            'Root/name erasure followed by exchangeable size coding is sufficient for universal influence-paid complete cost'],
 'first_unproved_line':None,'next_consumers':['A011','A012','A013','A006','B03','A086','A094','B20']}
claims=[old,claim]
for c in claims:assert set(c)==set(proto['required_per_run']['claim_fields'])
save(run/'CLAIMS.json',claims)

next_action=('Consume A006\'s actual-forest/determinant output construction and test retention of dominant physical-coordinate '
             'information on rare-switch prime tables and their nonconstant-child generalization, retaining conditional core CE. '
             'A086/A094 review the root conditioning, fixed order prior and exchangeable-location obstruction; do not repeat known-class baseline calculations.')
progress={
 'protocol_revision':proto['revision'],'run_id':run.name,'stream':'B03','packet_id':'A015',
 'gap_id':'G-J-COST','attempt_id':'A015-posterior-location-stage2',
 'method':'Independent A012 actual-child witness reconstruction; conditioned full-minterm root summation; exact exchangeable-reference variational optimization; explicit ordered rational repair and grouped-gate transfer',
 'mathematical_delta':'A012 v1 repair independently accepted locally. Full-minterm conditioning cancels labels and root rarity up to eta, but exchangeable-reference infimum/I diverges on all-relevant rare Boolean switches; explicit ordered repair CE<639/80 I and grouped majority reference transfer retain failure/core cost.',
 'deliverable_status':'COMPLETE_LOCAL_SOURCE_BOUND_HANDOFF','mathematical_status':'SCOPED_MECHANISM_RESOLVED_NEW_DIAGNOSTIC_REVIEW_PENDING_FULL_FEI_OPEN',
 'claim_versions_used':['A012-CONTROL-FIRST-POSTERIOR-REPAIR@1 (independently reconstructed whole original claim)',
                        'A006-MAJORITY-PRIME-IMPLICANT-POSTERIOR-PAYMENT@1 (pending; duplication guard, not proof premise)',
                        'A015-FIXED-SCALE-MINTERM-BARRIER@1 (preserved component scope)',
                        'Threshold current source lem:ranktail (grouped regular-core application)',
                        'forests.tex root conditioning interface (independently derived root sum)'],
 'claims_created_or_changed':['A012-CONTROL-FIRST-POSTERIOR-REPAIR@1: independent original-scope review added',
                              'A015-CONDITIONED-MINTERM-LOCATION-BARRIER@1: new scoped diagnostic'],
 'source_artifacts':['REPORT.md','A012_REVIEW.md','NOTES.md','code/check.py','code/transfer.py',
                     'out/FROZEN_SPEC.json','out/TRANSFER_SPEC.json','out/PILOT_FAILURE.json',
                     'out/EXACT_RESULTS.json','out/TRANSFER_RESULTS.json','out/SOURCES.json'],
 'next_consumers':['A011','A012','A013','A006','B03','A086','A094','B20'],
 'next_action':next_action,'stagnant_substantive_attempts':0,
 'blockers':['Universal function-adapted support/order/posterior cost payment remains unproved',
             'New A015 diagnostic independent review and supervisor registry/mirror adoption pending; no local save blocker'],
 'packet_ids':['A015']}
assert set(progress)=={x.split(' (')[0] for x in proto['required_per_run']['progress_fields']}
save(run/'PROGRESS.json',progress);save(run/'PACKET_DELTA.json',progress)
for field in proto['required_per_run']['report_fields']:assert '## '+field in (run/'REPORT.md').read_text(encoding='utf-8')

paths=[(repo/'EXECUTION_PROTOCOL.json','Full protocol reread'),
       (root/'BOARD.md','Stage-start 04:39 UTC snapshot'),
       (root/'claude'/'B03'/'STREAM_NOTES.md','Full lead v2'),
       (root/'claude'/'B02'/'STREAM_NOTES.md','Full lead v2; single-order tribes duplication guard'),
       (up/'DERIVATION.md','Full original A012 v1 proof Sections 1--5'),(up/'CLAIMS.json','Full original claim and exact version'),
       (major/'REPORT.md','Full majority posterior source and construction'),(major/'CLAIMS.json','Pending exact source version; not proof premise'),
       (root/'agents'/'A013'/'runs'/'20261012T010150Z-fleet05-A013-representation-stability'/'GENERAL_RESET.md','Full minterm reset source'),
       (root/'agents'/'A013'/'runs'/'20261012T010150Z-fleet05-A013-representation-stability'/'DERIVATION.md','Full averaged bent reserve source'),
       (repo/'source_material'/'reductions'/'paper'/'forests.tex','Complete root/conditioning/finite forest interfaces'),
       (supp/'baseline'/'current-threshold-paper.tex','Rank tail/mean, normalizer and derivative-law expectation at exact locators'),
       (agent/'runs'/'20261011T225533Z-fleet05-A015-minterm-barrier-analysis'/'REPORT.md','Own prior stage preserved; context from saved conclusions')]
save(run/'out'/'SOURCES.json',[{'path':str(p),'sha256':sha(p.read_bytes()),'bytes':p.stat().st_size,'read_scope':scope} for p,scope in paths])

(agent/'STATUS.md').write_text('STATE: A015 stage 2 complete: A012 repair independently accepted; conditioned minterm roots cancel, exchangeable-location obstruction and ordered <8I repair proved; 21,051 exact checks PASS; new review pending; FEI OPEN.\nNEXT: A086/A094 review; consume A006 actual-forest output transfer on rare-switch prime tables with physical location information and conditional core CE retained.\n',encoding='utf-8')
with (agent/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(now+': Stage 2 read updated board/B03 v2 and consumed A012 repair, A006 majority posterior, A013 reset and B02 single-gate guard. Independently accepted A012 whole original v1 with no repair. Root conditioning cancels full-minterm label and rarity in one-root sums up to eta. Exact exchangeable-reference optimum has an unbounded physical-location bill on all-relevant rare switches; an ordered exponent-two reference costs <639/80 I. Pilot serialization failure preserved, repaired with outward rational rounding; successful 20,956 assertions in 0.7232003 s plus 95 grouped-majority activation transfer assertions in 0.2911084 s. Protocol artifacts saved locally, no shared write/mirror/adoption claim.\n')
with (agent/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write('Conditioning strengthens the prior unconditioned full-minterm refund: eta=pi/((1+pi/N)^N-1), exp(-pi)<=eta<=1. One-root multiplicity cancels both names and root rarity up to -log eta; subset locations are still unpaid.\n')
    f.write('Best exchangeable complete reference CE is H(|S|)+E log2 binom(n,|S|); excess over H is degree-conditioned location divergence. All-relevant M_r=y+A_r(z-y) has I=1+r2^-r,H->0,W1->1, so every exchangeable reference CE/I diverges like log r. A function-aware common order y first with rational exponent-two weights gives complete CE<639/80 I.\n')
    f.write('A012-CONTROL-FIRST-POSTERIOR-REPAIR@1 independently reconstructed by A015 at whole original balanced-core scope: mass 1-p+pz, CE=p c_g+A_r, D_F=p D_g, exact physical-label posterior tends to two bits, sharp selector coefficient at r3 in (4.536,4.537). Explicit regular core reference mass n/[2(n+1)] transfers without discarding failure/core CE. Shared-control or arbitrary core reference payment remains open.\n')

assert json.loads((run/'out'/'EXACT_RESULTS.json').read_text())['exact_assertions']==20956
assert json.loads((run/'out'/'TRANSFER_RESULTS.json').read_text())['exact_assertions']==95
assert (run/'PROGRESS.json').read_bytes()==(run/'PACKET_DELTA.json').read_bytes()
files=[p for p in run.rglob('*') if p.is_file() and p.name!='RECEIPTS.json']+[agent/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
assert all(p.stat().st_size<20*1024*1024 for p in files)
save(run/'out'/'RECEIPTS.json',{'saved_at_utc':now,'scope':'Local byte/hash readback only',
 'claims_protocol_exact_fields':True,'progress_protocol_exact_fields':True,'report_required_fields_present':True,
 'packet_delta_byte_equal_progress':True,'A012_independent_original_scope_review':True,
 'new_A015_independent_review':False,'supervisor_adoption':False,'remote_mirror_verified':False,
 'files':[{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p.read_bytes())} for p in files]})
print(json.dumps({'status':'PASS','exact_assertions':21051,'files_hashed':len(files),
                  'A012_review':'ACCEPT_AT_ORIGINAL_SCOPE_NO_REPAIR','new_A015_review':'PENDING',
                  'protocol_fields':'EXACT_MATCH','remote_mirror_verified':False},indent=2))
