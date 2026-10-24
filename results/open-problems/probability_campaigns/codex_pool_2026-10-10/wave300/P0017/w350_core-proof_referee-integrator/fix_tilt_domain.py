"""Apply the final domain correction to local reports and the unsubmitted .part only."""
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parent
BASE=Path('~')
def load(path):return json.loads(path.read_text(encoding='utf-8-sig'))
def save(path,data):path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def jsonl(path):return [json.loads(s) for s in path.read_text(encoding='utf-8-sig').splitlines() if s.strip()]
def save_rows(path,rows):path.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')

reviews=jsonl(ROOT/'reviews'/'w348_verdicts.jsonl')
if not any(r['id']=='w350-R348-L4-original' for r in reviews):
    for r in reviews:
        if r['id']=='w350-R348-L4':
            r['id']='w350-R348-L4-original';r['verdict']='FIX'
            r['finding']='Finite fourth moments alone do not define exponential tilts near zero. The covariance operator identity is valid, but its identification as D^2F_f(0)/2 requires a local exponential moment.'
            r['corrected_statement']='Define U_2f=0.5 E[f(XX^T-I)] under finite fourth moments. It has the stated quadratic-variance dual norm. If the law additionally has exponential moments near zero, U_2 is the tilt derivative T_2.'
            r['independent_reproduction']='reviews/L4_DOMAIN_FIX.md gives a centered isotropic polynomial-tail law of finite fourth moment with divergent MGF at every nonzero real tilt, and proves the repaired derivative domain using Cauchy-Schwarz.'
    reviews.append({'id':'w350-R348-L4-corrected','subject':'w348 current ATTEMPT.md L4, repaired algebraic statement','verdict':'KEEP','reviewer':'w350','exact_scope':'Centered isotropic law with finite fourth moments for U_2; add a local exponential moment only for the equality U_2=T_2.','independent_reproduction':'Hilbert duality proves the algebraic identity under fourth moments. For |z|<epsilon/4, the extra E exp(epsilon|X|)<infinity and Cauchy-Schwarz justify numerator derivatives for every L2 f. Quotient differentiation then gives D^2F_f(0)/2=U_2. The current author artifact separates these two assertions.','remaining_gap':'No uniform quadratic variance upper bound is derived. This is a corrected auxiliary statement, not a full-target proof.'})
save_rows(ROOT/'reviews'/'w348_verdicts.jsonl',reviews)

other=jsonl(ROOT/'reviews'/'w349_verdicts.jsonl')
extras=[
 {'id':'w350-R349-C009','subject':'w349-C009 sharp equality witness','verdict':'KEEP','reviewer':'w350','exact_scope':'1<=p<=q, dim H>=2; extended passive W is nonzero.','independent_reproduction':'The coefficient witness and kth finite difference were independently derived in reviews/w348_independent.md before paired proof access; 35 p,q pairs and 925 components check the exact block-reversal identity.','remaining_gap':'The equality witness is not alone an upper-bound proof; that upper bound is separately checked as w348 L1.'},
 {'id':'w350-R349-C010','subject':'w349-C010 finite-fourth-moment tilt-domain counterexample','verdict':'KEEP','reviewer':'w350','exact_scope':'R density 5 r^-6 for r>=1, independent fair sign S, X=sqrt(3/5) S R. It is a counterexample to the general moment-only domain assertion, not a log-concave example.','independent_reproduction':'Integral_1^infinity 5r^(k-6)dr=5/(5-k) for k<5. Symmetry gives mean 0; scaling gives variance (3/5)*(5/3)=1 and fourth moment (9/25)*5=9/5. For any z!=0, the half with matching sign has an exponential integral against r^-6 and diverges.','remaining_gap':'The covariance-operator norm identity remains valid; the parent log-concave route has exponential moments.'}
]
known={r['id'] for r in other}
other.extend(r for r in extras if r['id'] not in known)
save_rows(ROOT/'reviews'/'w349_verdicts.jsonl',other)
all_reviews=reviews+other
counts={v:sum(r['verdict']==v for r in all_reviews) for v in ['KEEP','FIX','DROP']}
assert counts=={'KEEP':13,'FIX':1,'DROP':0}

bundle_path=ROOT/'drafts'/'bundle_002.json'
bundle=load(bundle_path)
quad=next(e for e in bundle['entries'] if e['key']=='quadratic-duality')
quad['logical_name']='quadratic-moment-operator-and-tilt-derivative-duality'
quad['title']='Quadratic moment operator, variance duality and the tilt domain'
quad['statement']='Let mu be centered and isotropic in R^n with finite fourth moments. Define the bounded quadratic-moment operator U_2 f=(1/2)E[f(X)(XX^T-I)]. Its L^2-to-Hilbert-Schmidt norm equals (1/2)sup_{A=A^T,||A||_HS=1}sqrt(Var_mu(X^TAX)). If mu additionally satisfies E exp(epsilon|X|)<infinity for some epsilon>0, then F_f(z)=E[f(X)e^(z.X)]/E[e^(z.X)] is defined near zero for every L^2 f and U_2 f=(1/2)D^2F_f(0). The local exponential moment is needed for this derivative identification and is automatic for log-concave laws; no uniform radius is asserted.'
quad['assumptions']=['Centered isotropic probability law','Finite fourth moments for the algebraic U_2 identity','Local exponential moment only for identification with a tilt derivative','Ordered-index Hilbert-Schmidt norm']
quad['proof_text']='Pair U_2 f with an HS-unit symmetric A. The functional is half the covariance with X^TAX, and its L2 norm is half the standard deviation. Interchanging the two suprema proves the identity; a normalized centered quadratic attains every nonzero-variance functional norm. Antisymmetric matrices pair to zero. Under E exp(epsilon|X|)<infinity, for |z|<epsilon/4 Cauchy-Schwarz bounds derivatives using E[|X|^4 exp(2|z||X|)]<infinity. Differentiate the quotient twice: mean zero removes the first-order denominator terms, covariance I gives D^2F_f(0)=E[f(XX^T-I)]. Finite fourth moments alone do not define the quotient, as independently checked polynomial-tail counterexamples show.'
quad['source']['revision']='2026-10-10-domain-repaired-reviewed-by-w350'
save(bundle_path,bundle)
held=BASE/'math-brain-inbox'/'w350'/'bundle_002.part'
assert not (BASE/'math-brain-inbox'/'w350'/'bundle_002.json').exists(),'Reviewer bundle must stay unsubmitted'
save(held,bundle)

claims=jsonl(ROOT/'CLAIMS.jsonl')
for r in claims:
    if r['id']=='w350-reviewed-quadratic-duality':
        r['statement']=quad['statement'];r['assumptions']=quad['assumptions'];r['proof_or_counterexample']=quad['proof_text'];r['source']=quad['source']
        r['remaining_gap']='Original moment-only derivative identification was FIX. The repaired U_2 statement is checked; local exponential moments are necessary for the derivative version. Statement review and second-account audit pending; no parent solution.'
save_rows(ROOT/'CLAIMS.jsonl',claims)

edges=jsonl(ROOT/'RELATIONS.jsonl')
for r in edges:
    if r.get('to_key')=='quadratic-duality':r['to_statement_quote']=quad['statement']
    if r.get('from_key')=='quadratic-duality':r['from_statement_quote']=quad['statement']
save_rows(ROOT/'RELATIONS.jsonl',edges)

source=load(ROOT/'SOURCE_STATUS.json')
source['recent_primary_claims'][1]['authors']=['Z. Song','X. Zhang']
source['auxiliary_statement_correction']='w348 original L4 confused a fourth-moment covariance operator with a locally defined tilt derivative. Current repaired L4 separates U_2 from T_2 and requires exponential moments for their identification. This correction does not challenge the parent log-concave target.'
save(ROOT/'SOURCE_STATUS.json',source)

for rel in ['w348/ATTEMPT.md','w349/CLAIMS.jsonl']:
    data=(BASE/'brain_workers'/rel).read_bytes()
    p=ROOT/'reviews'/('snapshot_corrected_'+rel.replace('/','_'))
    p.write_bytes(data)
    prov={'source':str(BASE/'brain_workers'/rel),'snapshot':str(p),'sha256':hashlib.sha256(data).hexdigest(),'scope':'Current corrected statements; original snapshot preserved separately. Hash is not proof.'}
    save(p.with_suffix('.provenance.json'),prov)

states=load(ROOT/'BUNDLE_STATES.json')
states['bundle_002']['reviewed']='Current four peer lemma statements independently reproduced by w350. Original L4 derivative generality required FIX; current U_2 statement is repaired. Second-account and statement review remain pending.'
save(ROOT/'BUNDLE_STATES.json',states)
packet=load(ROOT/'REVIEW_PACKET.json')
packet['verdicts']=all_reviews;packet['verdict_counts']=counts;packet['bundle_states']=states
packet['domain_correction']='reviews/L4_DOMAIN_FIX.md; original L4 FIX, current repaired L4 KEEP, w349-C010 counterexample KEEP. No unsubmitted lemma draft was ingested by this worker.'
save(ROOT/'REVIEW_PACKET.json',packet)
before=load(ROOT/'measurements'/'before_after.json')
before['peer_KEEP_count']=13;before['peer_FIX_count']=1
before['domain_correction']='Finite fourth moments define U_2. Local exponential moments are needed to identify it with the derivative T_2.'
save(ROOT/'measurements'/'before_after.json',before)

(ROOT/'REVIEW_PACKET.md').write_text('P0017 review packet, w350, 2026-10-10\n\nThirteen scoped KEEP verdicts and one historical FIX are in reviews/w348_verdicts.jsonl and reviews/w349_verdicts.jsonl. They cover current w348 L1-L4, w349 C001-C007, C009 and C010. C008 is an explicitly unproved input and is not counted as a proof. Original L4 needed FIX: finite fourth moments define a quadratic-moment operator U_2 but do not define exponential tilt derivatives near zero. The current author statement separates these claims and adds the exponential-moment condition. reviews/L4_DOMAIN_FIX.md contains the independent reproduction and counterexample.\n\nThe tensor recovery bound and sharpness were independently rederived before reading the paired proof. The product-exponential support decomposition is checked only under explicit independence. Posterior factorization strictness was independently proved without certifying the peers quadrature value. The conditional weighted reduction keeps (W) explicit.\n\nOwn Claims A-B are written in ATTEMPT.md and requested from w353. Their cards remain concept drafts. Universal all-function retention, the general all-degree Taylor bound and (W) remain unproved in this packet. Recent primary papers report full KLS resolution; their full proofs are not certified here.\n\nSix concept/definition entries are queued. Four reviewed lemma entries remain .part, with the domain repair applied, for author-deduplication and another account review. No live store was opened for writing. No source hash or finite check is called a formal proof receipt.\n\nNEXT: Independently audit Claims A-B adjoint/domain steps and the corrected U_2/T_2 statement before promotion; retain all-function VR as the explicit full-target input.\n',encoding='utf-8')

(ROOT/'REPORT.md').write_text('P0017 has October primary papers reporting full KLS resolution, while the read-only brain probe found two historical September cards. SOURCE_STATUS.json records the original Conjecture 30, current claims, assumptions and opposite psi conventions. Complete current proof validity remains unverified in this packet.\n\nI returned 13 scoped KEEP verdicts and one historical FIX. The original general L4 tilt claim was missing exponential moments; I corrected my earlier KEEP. Its covariance operator U_2 is valid under fourth moments, and equals the tilt derivative T_2 only with the additional local exponential moment. The author has repaired that statement. The counterexample and corrected proof are in reviews/L4_DOMAIN_FIX.md.\n\nThe tensor recovery constant for p=d,q=2d is binom(2d,d), versus the displayed 4^d bound: at d=5, 1024 becomes 252, a ratio of 4.06349. This sharpening was already supported by the source proof; novelty is not claimed. python -X utf8 check_math.py passed 35 sharpness pairs, 925 components, 140 block-symmetric fixtures, 9 coordinate enumerations, 100 Gaussian calibrations, 16 Wick dimensions and one negative control in 0.116479 seconds. The optional Gram test was skipped at fresh host CPU 86.7257%, above the 85% gate. The product proof was checked mathematically.\n\nSix concept/definition cards are submitted in math-brain-inbox/w350/bundle_001.json. Four corrected peer lemma cards are held as bundle_002.part. w348 already queued its original bundle; use the verdicts there to avoid duplicate nodes. BUNDLE_STATES.json separates prepared, submitted, reviewed, ingested and retrievable. Integration and retrieval are unverified; no live store was written by this worker. Own bridge review from w353 is pending.\n\nApply: the validating coordinator reviews and integrates accepted entries; the global hook patch is patches/01_stale_status_hook.diff. Worker-folder restrictions leave the hook and progress post staged in drafts/math-w350.jsonl and PROGRESS_PENDING.json.\n\nThe remaining mathematical risk is the all-function input. Tensor symmetry, product examples and unweighted covariance averages do not establish it. NEXT: audit Claims A-B and the corrected derivative domain, then the universal retention/weighted-covariance input.\n',encoding='utf-8')
progress=load(ROOT/'PROGRESS_PENDING.json')
progress['event']='P0017: 13 scoped KEEP and 1 historical FIX; corrected tilt domain; tensor and product proofs checked; Gaussian-retention draft queued; full-target input explicit.'
save(ROOT/'PROGRESS_PENDING.json',progress)
# This is a report of the permitted recall, retaining only the job-relevant hit.
(ROOT/'context'/'recall_P0017.txt').write_text('Recall completed successfully. Relevant first hit: open_problem_repo_survey_famous_tracks_all_open_af449ii_now_refuted_with_two_audits_2026_09_18 (verified historical survey). It reports KLS open/partial or retired on 2026-09-18, which cannot certify status after the October claims. Out-of-scope recall summaries were not followed and are excluded from this report. Prescribed proof scars are cited separately.\n',encoding='utf-8')
print(json.dumps({'status':'CORRECTED','verdict_counts':counts,'domain':'U_2 under fourth moments; T_2 identification additionally needs exponential moments','held_bundle_submitted':False}),flush=True)
