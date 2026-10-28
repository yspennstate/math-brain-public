from pathlib import Path
import json, hashlib, datetime

A=Path(__file__).resolve().parents[3]
R=Path(__file__).resolve().parents[1]
HOME=Path('~')
B=HOME/'brain_workers/FEI100_20261011'
CAN=HOME/'mop_fei100/reports/fei-2026-10-11'
SUP=HOME/'mop_fei100/research_pushes/2026-10-11-full-fei-100-agents'
SRC=B/'agents/A032/runs/20261023T141525Z-account03-A032-boolean-phase-realizability'
OLD=A/'runs/20261023T130748Z-account03-A079-correlated-auxiliaries'
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,value):
    (R/name).parent.mkdir(parents=True,exist_ok=True)
    (R/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def text(name,value):(R/name).write_text(value,encoding='utf-8')

protocol=json.loads((CAN/'EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'))
sources=[CAN/n for n in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex']]
sources += [SUP/n for n in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md']]
sources += sorted((SUP/'sources').glob('*'))
sources += sorted((B/'context').glob('*.txt'))
sources += [B/'BOARD.md',B/'claude/B16/STREAM_NOTES.md',SRC/'PROOF.md',SRC/'REPORT.md',SRC/'CLAIMS.json',OLD/'PROOF.md',OLD/'REPORT.md']
manifest=[];excerpts=[]
for p in sources:
    if not p.is_file():continue
    raw=p.read_bytes()
    try:body=raw.decode('utf-8');enc='utf-8'
    except UnicodeDecodeError:body=raw.decode('cp1252');enc='cp1252'
    mode='current direct proof source' if p.parent==SRC else 'current coordination/protocol or targeted baseline intake'
    manifest.append({'path':str(p),'sha256':sha(p),'bytes':len(raw),'encoding':enc,'mode':mode})
    lines=body.splitlines()
    selected=[]
    for i,line in enumerate(lines):
        if any(t in line.lower() for t in ['a079','g-phase-cond','conditional auxiliary','shared-data','conditional entropy','b16','c024']):
            selected.append(f'{i+1}: {line[:350]}')
    excerpts.append(str(p)+'\n'+'\n'.join(selected[:14])+'\n')
write('out/SOURCE_MANIFEST.json',manifest)
text('out/INTAKE_EXCERPTS.md','\n'.join(excerpts))

scalar=json.loads((R/'out/scalar.json').read_text(encoding='utf-8'))
ind=json.loads((R/'out/independent.json').read_text(encoding='utf-8'))
cert=next(x for x in scalar['records'] if x['a']==7)
assert cert['coefficients']==ind['independent_coefficients']
assert cert['ordered_cone_coefficients']==ind['cone_coefficients']
assert cert['positive_cone_certificate'] and ind['status']=='PASS'
assert len(cert['coefficients'])==85
write('out/FORMAL_RECEIPT.json',{
 'statement':'example : (8 * (10:Nat)^9 + ((10:Nat)^3 + 11^3)^3)^5 > 4 * (3 * (10:Nat)^5 + 11^5)^9 := by norm_num',
 'memok':'OK: physical free5.5GB (need4.0), commit free19.7GB (need8.0)',
 'wrapper_result':'RUNTIME_UNVERIFIED in15.6s; Compute admission held (hung window or under3000MB free); no new compiler process',
 'source_sha256':'2ed4479ec6b20e13ab2d136b53a7ec262f5bafdd89aeacccf0b7f1ceac69dbe4',
 'exit_code':1,'translation_fidelity':'UNVERIFIED','formal_theorem_claimed':False,
 'note':'The wrapper makes a fresh admission decision after memok; the observations have different times. No compiler launched.'})

source_claims=json.loads((SRC/'CLAIMS.json').read_text(encoding='utf-8'))
reviewed=next(c for c in source_claims if c['claim_id']=='A032-ISOSPECTRAL-CORE-BOUNDED-MIXTURE-OBSTRUCTION')
assert reviewed['version']==2
assert reviewed['statement_sha256']==hashlib.sha256(reviewed['exact_statement'].encode('utf-8')).hexdigest()
reviewed['review_records'].append({'reviewer':'A079','at':NOW,'verdict':'HOLDS_AT_STATED_SCOPE_WITHOUT_REPAIR','source':str(R/'PROOF.md'),'proof_sha256':sha(R/'PROOF.md'),'method':'Independent degree6 scalar identity, Holder and posterior KL reconstruction; new7/4 certificate independently reconstructs and strengthens coefficient2; actual full physical handoff verified without author code'})
reviewed['status']='INDEPENDENT_LOCAL_RECONSTRUCTION_HOLDS_REMOTE_ADOPTION_UNVERIFIED'
statement=('Let P(000)=9/16 and P(s)=1/16 on the other seven labels, the squared Fourier spectrum of the Boolean3-bit point defect, and P_r=P^tensor r for every integer r>=0. For every law R on3r bits, sum_i D(R_i||Bernoulli(1/4))<=(7/4)D(R||P_r). Consequently, for EVERY complete normalized coordinate-product mixture Q=sum_j w_j product_i q_ji with at most M positive components, the exact posterior joint L=P_r(X)w_j product_i q_ji(X_i)/Q(X) satisfies D(P_r||Q)+(3/4)I_L(X;J)>=r*tau, tau=2-(9/8)log2(3), and D>=max(0,r*tau-(3/4)H_L(J))>=max(0,r*tau-(3/4)log2 M). Infinite divergence is allowed as trivial case. The coefficient5/3 in the contraction is FALSE by the explicit rational tilted posterior R(s)=P(s)*1000^(3-|s|)*1331^|s|/(A/16), A=8*1000^3+(1000+1331)^3; the exact positive polynomial witness is recorded. The contraction optimum is strictly above5/3 and at most7/4, with no exact optimum claimed. For the original four-bit complementary controller and h=z1*z2*z3*g_r, both full physical z1 children have zero erasure/JS/singleton/phase refunds; target core replacement costs beta times mean full KL, beta3/8, and therefore bill+(3 beta/4)mean posterior information>=beta*r*tau. Actual influence23/8+9r/32, full conditional auxiliary entropy c_aux+beta H(g_r), and physical auxiliary influence beta(3+3r/4) are retained. Targets are necessary only in the DECLARED class. No arbitrary-core initial price, automatic descendant contraction, full FEI theorem or FEI counterfamily follows. All units bits; author proof with independently reconstructed exact certificates, not Lean-checked.')
new={
 'claim_id':'A079-DEFECT-CORE-LATENT-CAPACITY','version':1,'exact_statement':statement,
 'hypotheses':['P_r is the tensor of the actual Boolean three-bit defect spectrum; no arbitrary spectral source substitution','Q is a COMPLETE normalized mixture of coordinate products, with finite posterior alphabet and finite divergence or trivial infinite case','Posterior information/entropy under L, not free mixture-prior labels','Complete original controller vacuum, BOTH physical children, all old debits and original unused-account ownership retained','No universally mandatory product target, no initially cheap arbitrary-core source, no descendant application without source hypotheses'],
 'statement_sha256':hashlib.sha256(statement.encode('utf-8')).hexdigest(),'contributors':['A079'],
 'proof_source':{'path':str(R/'PROOF.md'),'sha256':sha(R/'PROOF.md'),'certificates':['out/scalar.json','out/independent.json'],'formal_verification':'NOT_CLAIMED; required wrapper held compute admission'},
 'proof_dependencies':[],'review_records':[],'status':'AUTHOR_PROOF_EXACT_CERTIFICATES_EXTERNAL_REVIEW_PENDING',
 'supersedes':[],'refutes':[{'statement':'Contraction coefficient5/3 suffices for every law R relative to this defect spectrum','witness':'PROOF.md section3; out/independent.json endpoint_positive_integer','scope':'Strictly strengthens A032 lower guard; A032@2 remains true'}],
 'first_unproved_line':None,'next_consumers':['A032','A033','A094','A096','A097','B16','B20']}
claims=[reviewed,new]
expected=set(protocol['required_per_run']['claim_fields'])
for c in claims:assert set(c)==expected
write('CLAIMS.json',claims)

gap='G-PHASE-COND'
next_action='A032/A033/A094 independently reconstruct the degree84 two-cone certificate and entropy dual; then construct an influence-priced ORIGINAL arbitrary-core compatible reference closed under physical inherited marginals, with all old debits and both full terminals. Do not optimize another isolated scalar constant instead of paying that source.'
progress={
 'protocol_revision':protocol['revision'],'run_id':R.name,'stream':'B16','packet_id':'A079','gap_id':gap,
 'attempt_id':'A079-stage11-degree84-cone-certificate','method':'Exact homogeneous polynomial positivity on two ordered cones; independent multinomial reconstruction; entropy dual and complete actual Boolean physical handoff',
 'mathematical_delta':'Same unduplicated Boolean defect family: contraction2 ->7/4; posterior-information/logM penalty1 ->3/4. Exact rational dual witness strictly refutes endpoint5/3. Independently accepts A032@2 without repair. Universal FEI improvement0.',
 'deliverable_status':'COMPLETE_LOCAL','mathematical_status':'RESTRICTED_ALL_R_AUTHOR_PROOF_EXACT_CERTIFICATES; NEW_REVIEW_PENDING; FULL_FEI_OPEN',
 'claim_versions_used':[{'claim_id':reviewed['claim_id'],'version':2,'statement_sha256':reviewed['statement_sha256'],'scope':'Independently reviewed predecessor; new theorem self-contained'}],
 'claims_created_or_changed':[{'claim_id':new['claim_id'],'version':1,'action':'new quantitative strengthening'},{'claim_id':reviewed['claim_id'],'version':2,'action':'independent HOLDS record'}],
 'source_artifacts':['PROOF.md','FROZEN_SPEC.json','FROZEN_VALIDATION.json','out/scalar.json','out/independent.json','out/SOURCE_MANIFEST.json','out/FORMAL_RECEIPT.json'],
 'next_consumers':['A032','A033','A094','A096','A097','B16','B20'],'next_action':next_action,
 'stagnant_substantive_attempts':0,
 'blockers':['Universal initial arbitrary-core influence price and useful REQUIRED compatible class remain unpaid','External review and supervisor mirror/adoption unverified','Lean wrapper held fresh admission; no compiler certificate','Brain wake warns stale personal/state/dream notes; not mathematical premises'],
 'packet_ids':['A079']}
required=set(protocol['required_per_run']['progress_fields']);required.remove('packet_ids (one primary ID, for compatibility)');required.add('packet_ids')
assert set(progress)==required
write('PROGRESS.json',progress);write('PACKET_DELTA.json',progress)

report=f'''# exact target, quantifiers, hypotheses and units

For EVERY r>=0, sharpen the retained latent-information capacity charge for the SAME actual Boolean tensor of three-bit defects. For every complete coordinate-product mixture Q, prove D(P_r||Q)+(3/4)I_L(X;J)>=r*tau, tau=2-(9/8)log2(3), and retain conditional auxiliary entropy, complete phase-realization influence, BOTH physical children and all original-account debits. Units: bits. Full FEI remains OPEN. Rung: author proof with independently reconstructed exact certificates; external review pending, NOT Lean-checked.

# sources actually read, revisions and theorem locators

Execution protocol execution-v2 read in full; current BOARD Oct26 23:00, own STATUS/LEARNED and stage10 proof/report, B16 lead v2; A032 run20261023T141525Z PROOF sections1--5 and exact claim@2. The source statement hash is verified and its proof reconstructed without importing author code. Required canonical/supplemental campaign files, plan, source inventory and four paper versions are source-pinned in out/SOURCE_MANIFEST.json; current baseline intake is targeted, with earlier full-paper recovery inherited rather than claimed re-audited. No unseen paper theorem or external literature result is used. The broad math-brain query returned weak unrelated matches and supplied no premise. Current direct stage invocation authorizes continuation after historical campaign dates; no schedule or deadline was altered.

# complete derivation or exact first unsupported line

PROOF.md gives a degree84 exact nonnegative polynomial certificate on BOTH ordered scalar cones. Holder and a KL variational dual yield contraction7/4, improving A032's2. Exact posterior KL decomposition then lowers the information/cardinality coefficient from1 to3/4 for the SAME unduplicated Boolean family. The endpoint5/3 also fails: an explicit rational tilt gives the positive integer witness {ind['endpoint_positive_integer']}. This is an entropy-dual probability-law witness, not a falsely claimed Boolean counterexample. Conditional auxiliary entropy is c_aux+(3/8)H(g), auxiliary influence (3/8)(3+I(g)); full influence and all controller vacuum costs remain. A032@2 independently HOLDS without repair; its theorem is strengthened, not refuted.

FIRST UNSUPPORTED UNIVERSAL LINE: an initial dimension-independent influence price for a useful arbitrary-core reference family closed under physical inherited marginals, or a genuinely REQUIRED compatible handoff paid from its ACTUAL same unused original allowance. The scalar source must still be P_r when used; arbitrary history-conditioning does not license renewal. No universal constant or FEI disproof follows.

# executed validation with domain, arithmetic, commands and outputs

Both frozen specifications precede their respective jobs. Commands: python -B -X utf8 code/scalar.py, then code/independent.py. Scalar pilot: exactly p5/3 and7/4, BOTH ordered cones, degree45/84 and seven fixed evaluations each; integer coefficients prove7/4 on the whole nonnegative quadrant and refute5/3 at10,11. This is not floating evidence. Independent implementation uses direct multinomial coefficients and Horner translation; exact arrays match the convolution certificate. Final independent validation: {ind['exact_assertions']} exact assertions PASS in {ind['seconds']:.6f}s. It includes r1,2 truth/Walsh spectra and independent physical edge sums, two full parents of1024/8192 points, BOTH children for each, six complete core target laws and twelve full terminal transactions, plus complete conditional entropy/influence identities. Prime-log vectors validate exact CE/KL identities;36-term outward rational atanh bounds certify finite strict signs. The analytical dual supplies every r and every finite mixture, without finite extrapolation.

The first independent pass had10143 assertions PASS; the final pass adds explicit conditional entropy and physical energy identities on the SAME frozen domain. Counts are not pooled. Exact equality, zero scalar inputs, absent posterior components, nonzero normalizers, finite-support KL, infinite target charge and r0 are treated in the proof. No automatic dimension increase, GPU, remote job or detached work. Memory estimates30/60MB; observed peak unmeasured. All substantive checks run under55s. Required memok returned0 (physical5.5GB, commit19.7GB), but the subsequent Lean wrapper made a fresh admission decision and held before starting a compiler. RUNTIME_UNVERIFIED is saved, and supplies no formal theorem.

# proof dependencies and changed downstream conclusions

The new proof is self-contained, and retains the source-bound A032@2 statement/hash with independent A079 HOLDS record. The exact controller handoff is reconstructed directly, including BOTH full terminals; no initially cheap source or unidentified numeric reserve is assumed. New all-r coefficient and strict5/3 exclusion await external review. The new candidate is one strengthening of the existing capacity mechanism, not another broad FEI closure claim. All downstream product-mixture accounts for this source may use3/4 posterior-information charge after accepting the new proof. Arbitrary-core source pricing is unchanged.

# one next mathematical action and independent reviewer

{next_action}

# actual persistence receipts or precise save blocker

Four exact-schema protocol files, complete proof, frozen specs, code, exact coefficient arrays, Boolean results, source receipts and formal-held receipt are saved in this run. Rolling STATUS/WORKLOG/LEARNED are current. out/LOCAL_PERSISTENCE.json records local hashes, sizes, statement hashes, exact schema checks and equality of PROGRESS/PACKET_DELTA. Supervisor copying, independent external review, remote mirrors and downstream adoption remain unverified. No git, mail, brain writes, shared research mutation, other-agent writes, trading/GPU work or deletion. The required wake completed with stale owner-context/state/dream warnings disclosed before relying on them; none supplies a mathematical premise. The compute advisory reports disk distress; all work here stays small. No research job is left running.

# Universal bridge

This stage advances the retained capacity side of C020 whole-reference witness cost and C024 history transfer inside C019: for the SAME actual unduplicated Boolean defect tensor, an exact all-r theorem lowers the necessary product-mixture information charge by25 percent, from beta*I_L to(3 beta/4)*I_L, or the cardinality loss from beta*log M to(3 beta/4)*log M, while keeping complete conditional entropy and actual phase energy. Universal FEI improvement is zero. The missing universal bridge is an influence-priced ORIGINAL arbitrary-core source closed under inherited physical marginals, or a necessary compatible handoff paid from the SAME genuinely unused original owner. NEXT targets that source after independent certificate review; another optional reset or merely optimizing this fixed scalar coefficient cannot settle full FEI.
'''
text('REPORT.md',report)

status='STATE: Stage11 saved: A032@2 independently HOLDS; new all-r defect contraction7/4 (was2), latent penalty3/4 (was1), endpoint5/3 FALSE;11575 exact checks PASS; new review pending; FEI OPEN.\nNEXT: A032/A033/A094 review exact cone certificate/entropy dual; fund ORIGINAL arbitrary-core compatible reference closed under physical marginals from SAME unused influence; no latent-credit renewal.\n'
(A/'STATUS.md').write_text(status,encoding='utf-8')
with (A/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{NOW} {R.name}: independently reconstructed A032@2. Degree84 two-cone positivity proves contraction7/4 and latent-capacity coefficient3/4 for SAME unduplicated defect spectra, all r; exact rational dual witness excludes endpoint5/3. Independent final11575 assertions/0.557s PASS, actual full physical parents/children and conditional entropy/influence retained. New proof awaits external review; full FEI/initial arbitrary-core source OPEN. Lean wrapper held compute admission; no compiler. No research left running.\n')
with (A/'LEARNED.md').open('a',encoding='utf-8') as f:
    f.write(f'\n## {NOW} Stage11: exact scalar contraction improvement\nFor P(000)=9/16,P(other)=1/16 and P_r=P^tensor r, sum_i D(R_i||mu)<=(7/4)D(R||P_r) for ANY law R. Exact degree84 polynomial16(3u^7+v^7)^12-[8u^12+(u^4+v^4)^3]^7 is nonnegative on BOTH ordered cones, independently reconstructed. Thus ANY complete coordinate-product mixture has D(P_r||Q)+(3/4)I_L(X;J)>=r*tau and D>=max(0,r*tau-(3/4)log M), tau2-(9/8)log3. A032@2 coefficient2 remains true and is independently accepted. Endpoint5/3 is strictly FALSE (not just coefficients below it): rational tilt with x1000,y1331 gives explicit positive integer certificate. Optimal contraction lies strictly above5/3 and at most7/4. Conditional auxiliary entropy c_aux+beta H(g), actual auxiliary energy beta(3+I(g)), BOTH terminals and complete vacuum costs remain. No arbitrary history reapplication, optional-conversion necessity, universal source price or FEI conclusion follows. Final11575 exact checks PASS; Lean runtime unverified. Further scalar optimization is not the universal NEXT; initial original arbitrary-core source remains unpaid.\n')

assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for c in claims:assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
files=[]
for p in sorted(R.rglob('*')):
    if p.is_file() and p.name!='LOCAL_PERSISTENCE.json':
        assert p.stat().st_size<20*1024*1024
        files.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':sha(p)})
write('out/LOCAL_PERSISTENCE.json',{'at':NOW,'status':'PASS_LOCAL_ONLY','protocol_schema_checks':True,'statement_hash_checks':True,'independent_coefficient_match':True,'progress_delta_byte_equal':True,'status_two_lines':True,'all_files_under20MB':True,'files':files,'external_review':'PENDING','supervisor_mirror':'UNVERIFIED'})
print(json.dumps({'status':'PASS_LOCAL','files':len(files),'claims':len(claims),'assertions':ind['exact_assertions'],'run':str(R)}))
