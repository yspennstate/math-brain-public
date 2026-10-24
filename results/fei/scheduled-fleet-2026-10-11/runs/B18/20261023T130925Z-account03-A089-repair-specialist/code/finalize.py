"""Persist source-bound review, sharpened theorem and exact receipts, A089 v1."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,datetime
import audit as a
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parents[1]
ALL=BASE.parents[1]
def save(path,obj):
    path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def claim_digest(c):
    legacy=c['claim_id']=='A071-POSITIVE-OUTER-CORRECTION-ENVELOPE-FAILS'
    key='statement' if legacy else 'exact_statement'
    return hashlib.sha256(json.dumps({key:c['exact_statement'],'hypotheses':c['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=legacy).encode('utf-8')).hexdigest()
def serial(v):return {str(p):str(c) for p,c in v.items()}
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def append(path,text):
    with path.open('a',encoding='utf-8',newline='\n') as f:f.write(text)
validation=load(ROOT/'out/VALIDATION.json');assert validation['status']=='PASS'
source72=ALL/'agents/A072/runs/20261023T120900Z-account03-A072-exact-walsh-engine'
source71=ALL/'agents/A071/runs/20261023T113913Z-account03-A071-search-space-design'
claims72=load(source72/'CLAIMS.json');claims71=load(source71/'CLAIMS.json')
s72=next(c for c in claims72 if c['claim_id']=='A072-SIGNED-COMPOSITION-DRIFT-COHERENT-ENVELOPE')
s71=next(c for c in claims71 if c['claim_id']=='A071-POSITIVE-OUTER-CORRECTION-ENVELOPE-FAILS')
for c in [s71,s72]:assert claim_digest(c)==c['statement_sha256']
save(ROOT/'out/HASH_CONVENTION.json',{'A071':'UTF8 SHA256 sorted compact JSON keys statement,hypotheses; ensure_ascii=True','A072_and_A089':'UTF8 SHA256 sorted compact JSON keys exact_statement,hypotheses; ensure_ascii=False','source_hashes_retained':[s71['statement_sha256'],s72['statement_sha256']],'initial_checker_error':'Assumed hash of statement text alone; source finalizers establish their correct documented conventions. No source defect.'})
h=tuple(1 if x==7 else -1 for x in range(8))
point=lambda n:tuple(-1 if x==0 else 1 for x in range(1<<n))
gs=[point(3),point(2),point(2)]
expected=[{2:F(57,8),3:-F(1431,1024),7:-F(3087,2048)},
          {2:F(53,8),3:-F(1701,512),5:-F(25,512)},
          {2:F(3),3:-F(27,16)}]
witness=[]
for name,gg,exp in zip(['parent','child0','child1'],[gs,[point(2),point(2),point(2)],[(1,1,1,1),point(2),point(2)]],expected):
    C=a.correction(h,gg);assert C==exp
    assert a.interval(C)[0]>0
    t=a.compose(h,gg)
    witness.append({'state':name,'physical_bits':len(t).bit_length()-1,'pivotal_weights':[str(v) for v in a.qs(h,gg)],'total_influence':str(a.data(t)[2]),'correction_exact_log_vector':serial(C),'correction_interval_scaled_2pow192':a.interval(C)})
assert [x['total_influence'] for x in witness]==['111/64','27/16','3/2']
save(ROOT/'out/WITNESS.json',{'status':'PASS','full_children_dummies_retained':True,'states':witness,'universal_K_extension':'All restrictions of each g_m, m<=3, are constants or g_l with H<=3I by 3^9>2^14; backward hull induction proves rho_K=0 for every real K>=3.'})
sources=[]
for p in [source72/'PROOF.md',source72/'REPORT.md',source72/'CLAIMS.json',source72/'code/finalize.py',source71/'PROOF.md',source71/'REPORT.md',source71/'CLAIMS.json',source71/'code/finalize.py',ALL/'BOARD.md',ALL/'claude/B18/STREAM_NOTES.md']:
    sources.append({'path':str(p),'sha256':digest(p),'usage':'source-bound proof review' if 'A07' in str(p) else 'dispatch context'})
save(ROOT/'out/SOURCES.json',sources)
for c in [s71,s72]:
    c['review_records'].append({'reviewer':'A089','independent_reviewer':True,'verdict':'HOLDS_UNCHANGED_SCOPE','method':'Independent algebraic reconstruction; no peer code imports. Integer whole-cube characters and separate FWHT, direct edges, canonical rational prime-log vectors; 4096 four-bit compositions,16384 query rows; exact seven-bit source formulas and integer signs.','evidence':str(ROOT/'PROOF.md')+'; out/VALIDATION.json; out/WITNESS.json','scope':'Original source version unchanged. A089 sharpened coefficient is a separate contributed claim, not independently accepted here.'})
    c['status']='INDEPENDENTLY_ACCEPTED_UNCHANGED_SCOPE'
    c['proof_source'].append(str(ROOT/'PROOF.md'))
statement='For every finite Boolean outer gate h and disjoint finite Boolean inner functions g_j on independent uniform physical bits, including constants and dummies, fix the original partition under restriction, put F=h(g), q_j equal to the true pivotal probabilities, and C=H(F)-sum_j q_j H(g_j), with base2 squared-Fourier entropy. For a physical query i in block j let mu=E g_j, t=ghat_j({i}) and d=Inf_i(g_j). Then mean C_child-C_parent <= q_j*(abs(t)*(abs(mu)+abs(t))+2*d)/ln2 <= (3/ln2)*Inf_i(F) <= (9/2)*Inf_i(F). For kappa=3/ln2 or9/2, C+kappa I(F) is nonnegative and full-query superharmonic. For every K>=0, adding sum_j q_j rho_K(g_j), where rho_K is the complete inner stopping hull of (H-KI)_+, gives a nonnegative full-query superharmonic majorant A_K of (H(F)-K I(F))_+. Actually supplied credit at least A_K can be propagated with conditional-mean-conserved old nonnegative credit owners and old signed debit labels, both full children and spent outside donors preserved. The coefficient is sufficient, not claimed optimal. No dimension-independent initial price is asserted: singleton physical cores give A_K=H(F)+kappa I(F), whose influence payment is FEI-equivalent.'
new={'claim_id':'A089-SHARPENED-SIGNED-COMPOSITION-RESERVE','version':1,'exact_statement':statement,'hypotheses':['uniform independent physical bits; entropy in bits; all finite arities and dimensions','fixed disjoint partition under every physical restriction; constants and dummies retained','K>=0 and complete finite stopping hulls','any historical reserve must be actually supplied by the same unused original owners; admission changes no partition; repartitioning needs its own comparison'],'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A089'],'proof_source':['PROOF.md sections2-5','code/audit.py','out/VALIDATION.json','out/WITNESS.json'],'proof_dependencies':['A072-SIGNED-COMPOSITION-DRIFT-COHERENT-ENVELOPE@1 exact identity, independently reconstructed unchanged in PROOF.md section3','Boolean restriction means mu+t,mu-t lie in[-1,1]; elementary log inequalities and finite backward induction proved here'],'review_records':[{'reviewer':'A089','independent_reviewer':False,'verdict':'ANALYTIC_PROOF_AND_EXACT_FINITE_VALIDATION_PASS','scope':'All-dimensional proof plus fixed finite controls; independent review of new3/ln2 coefficient remains pending'}],'status':'PROVED_LOCALLY_EXTERNAL_REVIEW_PENDING','supersedes':[],'refutes':[],'first_unproved_line':'Pay the initial A_K from O(I) of SAME actually unused original owners for arbitrary Boolean functions; identity partition is FEI-equivalent.','next_consumers':['A071','A072','A074','A075','A092','B18','B20']}
new['exact_statement']+=' Moreover, for every such fixed partition and K>=0, H(F)+(kappa-K)*I(F)<=A_K<=H(F)+kappa*I(F): the inner savings H(g_j)-rho_K(g_j) lie in[0,K*I(g_j)]. Thus dimension-independent initial influence funding at any fixed K is FEI-equivalent for arbitrary choices of partition, not only singleton cores.'
new['statement_sha256']=claim_digest(new)
save(ROOT/'CLAIMS.json',[s71,s72,new])
progress={'protocol_revision':'2026-10-11-execution-v2','run_id':ROOT.name,'stream':'B18','packet_id':'A089','gap_id':'G-R-MISMATCH','attempt_id':'A089-stage10-sharp-signed-reserve','method':'Consume A071 counterexample and independently reconstruct A072 signed erasure drift; exploit Boolean restriction-mean triangle to reduce the universal reserve.','mathematical_delta':'Independently accepts A071 witness and A0724/ln2 theorem unchanged; proves new universal3/ln2 drift and rational9/2 coherent owner-preserving envelope,25% less analytic reserve. Initial price remains FEI-equivalent.','deliverable_status':'COMPLETE_LOCAL_ARTIFACTS_CHECKED; SUPERVISOR_MIRROR_UNVERIFIED','mathematical_status':'SHARPENED_COHERENCE_PROVED_LOCALLY_EXTERNAL_REVIEW_PENDING; FULL_FEI_OPEN','claim_versions_used':['A071-POSITIVE-OUTER-CORRECTION-ENVELOPE-FAILS@1','A072-SIGNED-COMPOSITION-DRIFT-COHERENT-ENVELOPE@1'],'claims_created_or_changed':['A089-SHARPENED-SIGNED-COMPOSITION-RESERVE@1','A071-POSITIVE-OUTER-CORRECTION-ENVELOPE-FAILS@1 review only','A072-SIGNED-COMPOSITION-DRIFT-COHERENT-ENVELOPE@1 review only'],'source_artifacts':sources,'next_consumers':new['next_consumers'],'next_action':'A072/A074 independently review the3/ln2 triangle bound; A075 test whether any non-singleton partition supplies the initial signed correction and inner hulls from the same unused influence owners, explicitly comparing against the singleton FEI-equivalent specialization.','stagnant_substantive_attempts':0,'blockers':['Universal initial bank funding remains unproved; not a coherence obstruction.','Independent review of new coefficient and supervisor mirror verification pending.','Brain self-care degraded/unverified: personal model99.7h, state-of-mind84.2h,dream35.0h stale at stage wake; not mathematical premises.'],'packet_ids':['A089']}
save(ROOT/'PROGRESS.json',progress)
(ROOT/'PACKET_DELTA.json').write_bytes((ROOT/'PROGRESS.json').read_bytes())
report='''# A089 stage10: a smaller universal signed-composition reserve

## exact target, quantifiers, hypotheses and units

For every finite Boolean disjoint composition, every physical query and all subsequent restrictions of its fixed original partition, repair the false C_plus+sum(q inner hull) envelope while preserving full functions, old owner labels and both children. Entropy is in bits. New theorem: signed C drift is at most3/ln2 times queried physical influence; rational9/2 suffices. Constants and dummies are included. Initial FEI funding remains OPEN.

## sources actually read, revisions and theorem locators

Current BOARD snapshot13:08UTC and B18 STREAM_NOTES v2 were read with own stage9 STATUS. The stale original lex-family assignment is already closed; protocol dispatch consumes the new objection. A071 stage20 PROOF/REPORT and A072 stage20 PROOF/REPORT were read in full; CLAIMS bind exact statements. Their locators and SHA256 receipts are in out/SOURCES.json. Source versions A071-POSITIVE-OUTER-CORRECTION-ENVELOPE-FAILS@1 and A072-SIGNED-COMPOSITION-DRIFT-COHERENT-ENVELOPE@1 are accepted unchanged in this local independent review. The source A071 vacuum theorem is not used or accepted here. No peer code was imported or run.

## complete derivation or exact first unsupported line

PROOF.md is the complete derivation. Section1 keeps the failed statement, seven-bit witness and all-real K>=3 hull argument visible. Sections2-3 rederive erasure, Jensen-Shannon signs and the exceptional row. Boolean restriction means imply abs(mu)+abs(t)<=1. Hence ln2*Phi(mu^2,t^2)<=abs(t)*(abs(mu)+abs(t))<=d, while ln2*J_i(g)<=2d. The exact signed identity therefore yields3/ln2 instead of4/ln2. Backward induction proves nonnegative coherence of C+kappa I and its full inner-hull extension; Section5 gives conservative old-owner propagation with zero-total cases. Neither a positive part on C nor a new outside donor is introduced. A rational9/2 reserve releases81/128 against the witness drift G in(0.107184,0.107185).

First unsupported universal line: fund the initial whole bank from O(I) of the SAME unused original owners. For EVERY partition and every fixed K, H+(kappa-K)I<=A_K<=H+kappa I, since0<=H(g)-rho_K(g)<=K I(g). Thus nontrivial partitions also retain the FEI-equivalent initial price. No coefficient optimality, initial payment, repartitioning transfer or full FEI resolution is asserted.

## executed validation with domain, arithmetic, commands and outputs

Frozen out/FROZEN_SPEC.json preceded the search. Command: python -B -X utf8 code/audit.py from this run (or use the absolute script path). It passed4096 compositions of all16 Boolean two-bit gates with every ordered pair of all16 two-bit cores,16384 physical query rows,153 rational nonnegative triangle points of denominator16, and all seven witness queries. No symmetry quotient or dimension escalation. Runtime31.8105176 seconds; planned memory90MB, under the300MB memok threshold. Actual peak memory was not measured. Integer direct character sums and independent FWHT agree, direct edges match Fourier influences, coefficient restrictions match exactly, and canonical rational prime-log vectors prove entropy and signed drift identities exactly. Signs use outward192-bit logs with80-term atanh tail plus five integer-power checks. PROOF.md supplies the continuum/all-dimensional argument; finite tests are not its proof.

Command: python -B -X utf8 code/finalize.py verifies all three exact witness correction formulas, their strict signs and total influences111/64,27/16,3/2, with both six-free-bit children retained. out/VALIDATION.json and out/WITNESS.json contain exact certificates and scale conventions. Existing logs use own earlier arithmetic helper; peer code is not a validation dependency.

## proof dependencies and changed downstream conclusions

A071 refutes A089 stage9 NEXT proposal, not its conditional rerouting theorem. The failed proposal is withdrawn in rolling STATUS and explicitly annotated in LEARNED; its original immutable stage9 files remain untouched. A072's original statement and SHA256 are preserved, with an independent acceptance record. Source finalizers were read solely to verify their distinct statement-plus-hypotheses hash conventions; the initial bare-statement hash assumption was corrected, and out/HASH_CONVENTION.json records this. No source digest defect exists. A089 contributes the separate3/ln2 improvement,25% below the source4/ln2 analytic reserve; rational9/2 replaces6. The new theorem awaits independent review. Its all-partition savings sandwich strengthens the source's honest unpaid initial-price line. No claimed universal H/I bound results.

## one next mathematical action and independent reviewer

A072/A074: independently review the Boolean triangle improvement. A075: examine initial payment by a nontrivial fixed partition using the SAME unused influence stock, and identify exactly what goes beyond the singleton FEI-equivalent price. This initial-payment test is the next mathematical action; further finite gate searches do not resolve it. Named consumers are handoff destinations, not claims that messages were sent or work assigned.

## actual persistence receipts or precise save blocker

All artifacts are confined to A089. out/PERSISTENCE.json records byte hashes for the proof, required four protocol files, code and certificates. The persistence validator checks exact schema fields, source statement digests, PROGRESS/PACKET_DELTA equality, all files under20MB, and two-line STATUS. Local persistence is checked; supervisor GitHub/brain mirrors and downstream adoption are unverified. No shared tree or other agent folder was modified. No job remains running. Session brain self-care is degraded/unverified: stale personal model99.7h, state-of-mind84.2h and dream35.0h were reported at wake, and are excluded from mathematical reasoning. Compute telemetry was stale; only the bounded31.8s pilot ran, with no large job, worker launch or process survey.

**Universal bridge:** This stage moves C019 stopping-tree coherence and the fixed-partition C024 history-transfer interface by reducing the universal signed-correction drift reserve from4/ln2 to3/ln2, with a fully rational9/2 substitute for6 and preserved old-owner accounting. The whole-set/initial influence price is still unpaid; singleton cores expose exactly H+kappa I. The shortest route to full FEI is now to prove or refute initial payment for arbitrary functions using nontrivial partitions and the same unused owners, rather than searching another isolated gate class or treating superharmonicity as free starting capital.
'''
(ROOT/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
(BASE/'STATUS.md').write_text('STATE: A089 stage10 complete locally: A071 failure and A072 drift accepted unchanged; new3/ln2 drift,9/2 reserve and all-partition initial-price sandwich proved; external review pending; FEI OPEN.\nNEXT: A072/A074 review coefficient and savings bound; A075 target initial same-owner bank payment, FEI-equivalent for EVERY partition at fixed K, rather than more coherence or gate cases.\n',encoding='utf-8',newline='\n')
append(BASE/'WORKLOG.md','\n2026-10-23 stage10 (20261023T130925Z): Consumed A071 stage20 refutation of stage9 NEXT; independently accepted its literal7bit witness and A072 stage20 signed identity unchanged. Boolean restriction means give abs(mu)+abs(t)<=1, sharpening exceptional Phi to d/ln2 and universal drift to3/ln2 (rational9/2 reserve). Exact4096 compositions/16384 rows/153 scalar points and witness pass in31.81s. Initial same-owner bank payment remains FEI-equivalent for EVERY partition at fixed K by H+(kappa-K)I<=A_K<=H+kappa I; new coefficient awaits A072/A074 review. Source hashes verified with their original distinct canonical JSON conventions after correcting my bare-text hash assumption. No running jobs; supervisor mirror unverified.\n')
append(BASE/'LEARNED.md','\n2026-10-23 stage10: CORRECTION TO stage9 NEXT (original immutable run preserved): C_plus+sum(q inner hull) is false as a universal full-query envelope. Literal AND(OR3,OR2,OR2), queried in OR3, has positive drift G in(0.107184,0.107185) for every K>=3 while all inner hulls vanish. Use SIGNED C with an actually supplied reserve. Durable new bound: Boolean means mu+t and mu-t in[-1,1] imply abs(mu)+abs(t)<=1. Natural Phi(mu^2,t^2)<=abs(t)*(abs(mu)+abs(t))<=Inf_i(g), by ln(1+x)<=x and ln(1+s^2)<=s. Combined with the exact signed erasure identity and JS<=2Inf/ln2 yields universal drift<=3Inf(full)/ln2. Thus C+(3/ln2)I, or C+(9/2)I, is nonnegative and full-query coherent. Source A0724/ln2 theorem accepted unchanged; A089 improvement awaits independent review. This is25% less analytic reserve, not an FEI constant. Stronger price diagnosis: H is superharmonic, so0<=rho_K<=H and rho_K>=H-KI. Inner savings satisfy0<=H-rho_K<=KI, whence H+(kappa-K)I<=A_K<=H+kappa I for EVERY partition. At fixed K, initial O(I) funding is FEI-equivalent even if the partition is chosen separately for each function.\n')
# Annotate the corrected rolling entry itself, so an excerpt cannot resurrect it.
learned=BASE/'LEARNED.md'
with learned.open('r',encoding='utf-8',newline='') as f:old=f.read()
needle='outerC_plus+sum(q_j*inner_hull)'
if needle in old:
    old=old.replace(needle,needle+' [WITHDRAWN: A071 stage20 literal7bit witness; use stage10 signed reserve, initial price still unpaid]')
    with learned.open('w',encoding='utf-8',newline='') as f:f.write(old)
protocol=load(Path(r'~\mop_fei100\reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))
cf=set(protocol['required_per_run']['claim_fields']);pf=set(protocol['required_per_run']['progress_fields']);pf.remove('packet_ids (one primary ID, for compatibility)');pf.add('packet_ids')
assert all(set(c)==cf for c in load(ROOT/'CLAIMS.json'))
assert set(load(ROOT/'PROGRESS.json'))==pf
assert (ROOT/'PROGRESS.json').read_bytes()==(ROOT/'PACKET_DELTA.json').read_bytes()
assert len((BASE/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
for c in load(ROOT/'CLAIMS.json'):assert claim_digest(c)==c['statement_sha256']
files=[p for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
receipt={'status':'PASS','local_only':True,'mirrors_verified':False,'schema_checks':'PASS','four_protocol_files':'PASS','packet_delta_exact_copy':True,'rolling_status_lines':2,'files':[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in files],'rolling':[{'path':str(p),'bytes':p.stat().st_size,'sha256':digest(p)} for p in [BASE/'STATUS.md',BASE/'WORKLOG.md',BASE/'LEARNED.md']]}
save(ROOT/'out/PERSISTENCE.json',receipt)
readback=load(ROOT/'out/PERSISTENCE.json')
assert all(digest(ROOT/item['path'])==item['sha256'] for item in readback['files'])
assert all(digest(Path(item['path']))==item['sha256'] for item in readback['rolling'])
print(json.dumps({'status':'PASS','source_reviews':2,'new_claim':new['claim_id'],'local_files_hashed':len(files),'rolling_files_hashed':3,'validation':validation['status'],'witness':'PASS','schemas':'PASS','full_FEI':'OPEN','external_review':'PENDING','mirrors':'UNVERIFIED'}))
