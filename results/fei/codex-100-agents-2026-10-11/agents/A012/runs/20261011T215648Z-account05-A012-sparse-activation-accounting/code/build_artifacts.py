from pathlib import Path
import json,hashlib,datetime

RUN=Path(__file__).resolve().parents[1]
AGENT=RUN.parents[1]
run_id=RUN.name
def write(path,obj):
    path.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
claims=[]
def claim(cid,statement,hypotheses,dependencies):
    obj=dict(claim_id=cid,version=1,exact_statement=statement,hypotheses=hypotheses,
      statement_sha256=hashlib.sha256(json.dumps({'statement':statement,'hypotheses':hypotheses},sort_keys=True,separators=(',',':')).encode()).hexdigest(),
      contributors=['account05/A012'],proof_source={'path':str(RUN/'HIDDEN_CORE_TEST.md'),'deliverable':str(RUN/'ACTIVATION_ADMISSION.tex')},
      proof_dependencies=dependencies,review_records=[],status='AUTHOR_PROVED_PENDING_INDEPENDENT_REVIEW',
      supersedes=[],refutes=[],first_unproved_line=None,next_consumers=['A011','A013','A086','A094'])
    claims.append(obj)
claim('A012-HEREDITARY-ACTIVATION-REFLECTION',
 'For any Boolean function class C containing constants and literals and closed under sign reversal, physical coordinate restrictions, disjoint Boolean products and point activation on fresh controls, for every Boolean f and integers t,r>=1, membership of f in C is equivalent to membership of g_t=z*product_{j=1}^t f(x^(j)) and equivalent to membership of 1+A_r(g_t-1).',
 ['Uniform cubes of arbitrary finite dimension','Fresh independent blocks and sign z','A_r is a single-point indicator on r fresh controls','All five class hypotheses are required'],[])
claim('A012-AUDITED-READONCE-ADMISSION',
 'Let R consist of Boolean signs with finite globally read-once AND/OR/parity/negation formula certificates, literal or constant leaves and no opaque Boolean leaves. R is closed under restrictions, sign reversal, disjoint substitution, disjoint products, balancing and point activation on fresh controls. Every f in R satisfies corrected product-biased E(f)<=C0*(I(f)-Var(f)), C0=2+4/ln(2), and H(f)<=C0*I(f) for uniform original inputs. The balanced three-bit multiplexer M(x,y,z)=(1+x)y/2+(1-x)z/2 and all its activated balanced tensor powers are outside R. Overlapping OR substitution does not preserve R.',
 ['Each original input label occurs at most once globally','Arbitrary finite gate fan-in and depth','Product inputs for corrected E; uniform inputs for H/I','Delete deterministic children before dividing by child variance'],
 ['A012-HEREDITARY-ACTIVATION-REFLECTION@1','Elementary gate and composition identities reconstructed in HIDDEN_CORE_TEST.md; threshold paper 38pp Proposition 7.1 and Lemma 7.5 are source attribution'])
# Bundle the tightly dependent reflection, class certificate and exclusion
# in one review record instead of opening separate broad candidates.
combined=claims[0]
combined['claim_id']='A012-HEREDITARY-ACTIVATION-ADMISSION'
combined['exact_statement'] += ' Furthermore, '+claims[1]['exact_statement']
combined['exact_statement'] += ' For the control-first r-bit point activation of a fresh literal y, with p=2^(-r), the expected control depth D=2(1-p), I_sel=rp, I=p(r+1), and the uncompressed two-bits-per-query transcript has cost/I=4(2^r-1)/(r+1), tending to infinity. Every exact finite spectral witness W retaining its physical leaf label satisfies H(W|S)>=D-H(F)>=2(1-p)-4rp-2p*log2(e), whose displayed lower bound tends to two bits.'
combined['hypotheses'] += claims[1]['hypotheses']
combined['statement_sha256']=hashlib.sha256(json.dumps({'statement':combined['exact_statement'],'hypotheses':combined['hypotheses']},sort_keys=True,separators=(',',':')).encode()).hexdigest()
combined['proof_dependencies']=[]
claims=[combined]
write(RUN/'CLAIMS.json',claims)
progress=dict(protocol_revision='2026-10-11-execution-v2',run_id=run_id,stream='B03',packet_id='A012',gap_id='FEI-B03-A012-INITIAL',attempt_id='A012-hereditary-admission-v1',method='Exact activation atom ledger; hereditary restriction extraction; audited disjoint formula composition; complete labelled three-bit membership enumeration; physical-label entropy lower bound',mathematical_delta='Proved exact class-membership reflection through activated balanced tensors; explicit proper admission class with a self-contained constant <8 proof and excluded multiplexer family. Consumed A011: activated literal makes uncompressed transcript cost/I unbounded, with posterior entropy lower bound tending to two bits; universal overlap payment remains open.',deliverable_status='COMPLETE_LOCAL_ARTIFACT_PENDING_INDEPENDENT_REVIEW',mathematical_status='RESTRICTED_ADMISSION_PROVED_UNREVIEWED_FULL_FEI_OPEN',claim_versions_used=['Threshold38pp Proposition7.1 Lemma7.5 Proposition8.9 Corollary8.10; recovered baseline, fully reconstructed','A011-BOUNDARY-RETAINING-SELECTOR-TRANSCRIPT@1; unreviewed source interface consumed, not a proof premise'],claims_created_or_changed=[x['claim_id']+'@1' for x in claims],source_artifacts=['REPORT.md','HIDDEN_CORE_TEST.md','ACTIVATION_ADMISSION.tex','out/FROZEN_SPEC.json','code/validate.py','out/validation.json','out/three_bit_admitted.json','out/mux_certificate.json','out/SOURCE_RECEIPTS.json'],next_consumers=['A011','A013','A002','A005','A021','A086','A094'],next_action='Review bundled admission proof and posterior lower bound; A011 optimize complete low-boundary code on activated y retaining H(W|S), then stress-test activated balanced tensor cores.',stagnant_substantive_attempts=0,blockers=[{'kind':'ADVISORY_SOURCE_MISSING','path':r'~\brain_workers\FEI100_20261011\claude\B03\STREAM_NOTES.md','impact':'Lead direction unavailable; independent packet proof and local persistence completed'}],packet_ids=['A012'])
write(RUN/'PROGRESS.json',progress);write(RUN/'PACKET_DELTA.json',progress)
base=Path(r'~\mop_fei100\reports\fei-2026-10-11')
sup=Path(r'~\mop_fei100\research_pushes\2026-10-11-full-fei-100-agents')
ctx=Path(r'~\brain_workers\FEI100_20261011\context')
paths=[base/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','AGENT_ASSIGNMENTS.json','FEI_100_agent_research_plan.tex','source_material/reductions/paper/forests.tex']]
paths += [sup/x for x in ['CAMPAIGN.md','CLAIMS.md','COUNTEREXAMPLES.md','SEED_LEMMAS.md','NATIVE_MAPPING.md','sources/LOG_ALLOCATION_CURATED.md','sources/ROUTE_MAP_CURATED.md','sources/OVERLAPPING_PRODUCT_NOTE.md']]
paths += list(ctx.glob('*.txt'))
paths += list((base/'runs').rglob('REPORT.md'))
paths += [Path(r'~\brain_workers\FEI100_20261011\BOARD.md')]
paths += [Path(r'~\brain_workers\FEI100_20261011\agents\A011\runs\20261011T213831Z-account05-A011-representation-existence')/x for x in ['REPORT.md','CLAIMS.json']]
write(RUN/'out'/'SOURCE_RECEIPTS.json',[dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in paths])
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
(AGENT/'STATUS.md').write_text('STATE: A012 complete: hereditary admission plus activated-literal transcript cost/I divergence and posterior lower bound tending to 2 bits; 5,268 exact checks; one bundled claim awaits review; FEI OPEN. B03 notes absent.\nNEXT: A086/A094 review; A011 erase the full physical-label posterior cost on activated y, then test the repaired complete code on activated balanced tensor cores.\n',encoding='utf-8')
with (AGENT/'WORKLOG.md').open('a',encoding='utf-8') as f:
    f.write(f'\n{stamp} | {run_id}\nRead protocol, campaign/board/source interfaces; missing B03 lead notes recorded. Reconstructed exact balanced/general activation ledger; proved hereditary admission reflection. Supplied a globally audited read-once AND/OR/parity certificate class with source-complete constant <8 proof and analytic multiplexer exclusion. Frozen exact three-bit pilot passed 5,268 assertions, 768 activations, 152 admitted tables, 912 restrictions. New A011 report consumed: control-first activated y has D=2(1-p), uncompressed cost/I=4(2^r-1)/(r+1) diverging; any witness retaining the physical leaf label has H(W|S)>=D-H(F), tending in lower bound to 2 bits. Results bundled into one review record to retain B03 cap with A011. Universal C020 remains open. Local artifacts saved; independent review, adoption and remote copying pending.\n')
(AGENT/'LEARNED.md').write_text('''# Durable A012 facts

* Exact point activation: p=2^-r, mu=Eg, a=1-mu, v=1-mu^2; I(1+A_r(g-1))=pI(g)+rpa. For balanced g, H=pH(g)+2rp(2-p)+L((1-p)^2), L(q)=qlog2(1/q).
* General entropy ledger: H=L((1-pa)^2)+(p-p^2)a^2log2(1/(p^2a^2))+p[H(g)-L(mu^2)]+2rpv, with continuous zero terms. Never erase the selector/control entropy.
* Rarity and small I alone retain the optimal full FEI constant via fresh balanced tensor powers and r_t=ceil(2log2(t+1)). This is source baseline, not a new theorem.
* For a sign/restriction/disjoint-product/fresh-activation closed class containing constants and literals, f, its fresh balanced tensor and its point activation have exactly equivalent membership. Restrict the controls, all but one tensor block, and the fresh sign to extract f. This is a necessary admission audit.
* Audited globally read-once AND/OR/parity formulas with literal/constant leaves satisfy product-biased corrected E <= (2+4/ln2)(I-Var), hence uniform H <= (2+4/ln2)I <8. Gate constants and disjoint composition are recovered baseline and reconstructed in the run. Closure holds for restrictions, disjoint substitution/product, balancing and arbitrarily rare fresh point activation.
* Three-bit multiplexer M=(1+x)y/2+(1-x)z/2 has H=2, I=3/2, all influences 1/2 and is outside that class. Its activations and activated balanced tensors are outside by restriction reflection. It is an easy FEI function, not a conjecture counterexample.
* Overlap destroys this class: M=OR(AND(x,y),AND(-x,z)). A local read-once claim cannot bypass the repeated x. Universal representations need a proved complete reuse/witness cost, which this stage does not supply.
* A011 dependency consumed: control-first r-bit activation of y has D=2(1-p), I_sel=rp and I=p(r+1). Its uncompressed transcript cost/I=4(2^r-1)/(r+1) diverges even though this core is already certified. Any exact witness retaining the physical leaf label has H(W|S)>=D-H(F)>=2(1-p)-4rp-2p log2(e), tending in lower bound to 2 bits. The necessary repair is posterior erasure, not a new leaf-class theorem. This does not refute other representations or FEI.
* Exact frozen n=3 enumeration found 152/256 read-once class members and verified 768 activations plus 912 restrictions; 5,268 Fraction/integer assertions passed. Analytic proofs provide all-dimensional conclusions. B03 lead notes were unavailable at the supplied path.
'''.replace('\n+','\n'),encoding='utf-8')
receipt_paths=[p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']+[AGENT/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
write(RUN/'out'/'PERSISTENCE_RECEIPTS.json',dict(saved_at_utc=stamp,local_only=True,remote_mirror_verified=False,files=[dict(path=str(p),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in receipt_paths]))
print(json.dumps({'claims':len(claims),'mandatory_files_saved':True,'receipt_files':len(receipt_paths),'local_only':True}))
