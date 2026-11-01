"""Prepare review artifacts only. Never mutates a live source or store."""
from pathlib import Path
import hashlib
import json
import re
from fractions import Fraction
import math

ROOT = Path(__file__).resolve().parent
def save(name, obj):
    (ROOT/name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
def digest(data):
    return hashlib.sha256(data).hexdigest()

proof_path = ROOT/'PROVED_LEMMAS.md'
proof = proof_path.read_text(encoding='utf-8').replace(
    'Theorem 1.3 (Edelman), and Spielman-Teng ICM survey once retrieved.',
    'Theorem 1.1 (Edelman limiting law) and Theorem 1.3 (universality).')
proof_path.write_text(proof, encoding='utf-8')
parts = re.split(r'^## ', proof, flags=re.M)[1:]
sections = {p.split(':',1)[0]:p.split('\n',1)[1].strip() for p in parts if ':' in p.split('\n',1)[0]}
specs = {
 'L1': ('For n>=2 and iid uniform sign B, P(s_min(B)=0)>=2^(1-n).', ['n>=2','independent uniform {-1,+1} entries']),
 'L2': ('For every nonsingular n by n sign matrix B, n>=2, s_min(B)>=2^(n-1)((n-1)/n^2)^((n-1)/2). Hence for 0<=epsilon<sqrt(n) times this bound, s_min(B)<=epsilon/sqrt(n) if and only if B is singular.', ['n>=2','B has entries in {-1,+1}','nonsingularity only for the positive lower bound']),
 'L3': ('An iid sign n by n B has the same singular-value law as C=[[1,1^T],[1,J-2H]], where H is iid {0,1} of size n-1. det(C)=(-2)^(n-1)det(H). For nonsingular H, C^(-1)=[[1-(1/2)1^T H^(-1)1,(1/2)1^T H^(-1)],[(1/2)H^(-1)1,-(1/2)H^(-1)]].', ['n>=2','all entries of B independent uniform signs','H nonsingular for inverse formula']),
 'L4': ('Let R be real (n-1) by n with full row rank, unit kernel v and orthonormal right singular vectors u_i with squared singular values d_i>0. For any real row x and 0<=t<sqrt(min d_i), s_min([R;x])<=t iff <x,v>^2<=t^2(1+sum_i <x,u_i>^2/(d_i-t^2)).', ['full row rank of R','real Euclidean singular values','0<=t<least positive singular value of R']),
 'L5': ('For every n=2^k, k>=1, a sign Hadamard matrix with its all-ones row removed has all positive singular values sqrt(n) and a flat unit kernel vector, yet an independent iid sign last row makes the square matrix singular with probability binom(n,n/2)/2^n>=1/(n+1). Thus these conditioning and flatness hypotheses alone do not imply a uniform conditional bound epsilon+C exp(-c n).', ['n=2^k, k>=1','R is the displayed deterministic Sylvester Hadamard block','new row independent uniform signs','constants C,c fixed as n varies']),
 'L6': ('For iid sign n by n B, q=2^(n-1), m=binom(n,2), P(B singular)>=1-product_{j=0}^{n-1}(1-j/q)>=m/q-binom(m,2)/q^2. The collision probability is asymptotic to n(n-1)2^(-n), excluding an upper bound C 2^(-n) for fixed C.', ['n>=2','independent uniform sign entries','limit n tends to infinity for asymptotic statement']),
 'C1': ('For real iid standard Gaussian G_n, 1-exp(-t-t^2/2) is the limiting CDF of sqrt(n)s_min(G_n) at fixed t>=0, not a finite-n exact CDF. At n=1 the exact CDF is erf(t/sqrt(2)), with slope sqrt(2/pi) at zero.', ['real standard Gaussian entries','t fixed>=0','n tends to infinity for limiting formula'])
}
rows=[]
for key,(statement,assumptions) in specs.items():
    rows.append({'claim_id':'C0029-w567-'+key,'statement':statement,'assumptions':assumptions,
      'source':('arxiv:0903.0614 Theorem 1.1 equations (1)-(2); own n=1 counterexample' if key=='C1' else 'owner-own-work:w567:C0029; elementary self-contained derivation'),
      'source_quote':('Limiting distributions for gaussian models' if key=='C1' else None),
      'proof':sections[key],'independent_reviewer':'w569 PENDING; no KEEP receipt claimed',
      'remaining_gap':'No parent-conjecture upper-tail estimate follows from this scoped result.',
      'status':'proved special case','formal_check':None})
rows.append({'claim_id':'C0029-w567-GAP','statement':'For iid {0,1} H of size n-1, let C=[[1,1^T],[1,J-2H]]. The desired estimate is P(H singular or ||C^(-1)||_op>=sqrt(n)/epsilon)<=epsilon+C0 exp(-c0 n), for constants C0,c0>0 and all n>=2, 0<epsilon<1, with inverse used only for nonsingular H.',
  'assumptions':['independent uniform {0,1} entries','positive epsilon less than 1'],
  'source':'owner-own-work:w567:C0029; equivalent restatement using L3 of historical target arxiv:2405.20308v2 equation (2)',
  'proof':'L3 proves equivalence to the target, not this upper bound. Determinant divisibility gives only the arithmetic plateau. Bounding the full random bordered inverse without a coefficient loss is the remaining probabilistic obligation.',
  'independent_reviewer':'w569 PENDING','remaining_gap':'The displayed probabilistic bound itself is unproved.','status':'conjecture'})
(ROOT/'CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')

live = Path(r'~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl')
old_line = None
for line_number,line in enumerate(live.open(encoding='utf-8'),1):
    if '"attempt_id": "C0029-A001"' in line:
        old_line=line.rstrip('\n'); break
assert old_line is not None
old = json.loads(old_line)
new=dict(old)
new['key_identity']='Limiting real Gaussian law: for each fixed t>=0, lim_{n->infinity} P(sqrt(n) s_min(G_n)<=t)=1-exp(-t^2/2-t). This is not a finite-n exact law; its limiting slope at zero is 1.'
new['result']="For real Gaussian G_n, Edelman's limiting law gives P(sqrt(n) s_min(G_n)<=t)=1-exp(-t^2/2-t)+o(1) for each fixed t>=0 as n tends to infinity. Its limiting slope at zero is 1; the finite-n law differs, as already seen at n=1, whose CDF is erf(t/sqrt(2)) and slope is sqrt(2/pi). Tao-Vu 2010 hard-edge universality gives a uniform O(n^-c) distributional error under its moment hypotheses, which can yield coefficient one in a polynomial-size t regime but does not by itself cover exponentially small t. This dated attempt made no improvement. Later source update: Sah-Sahasrabudhe-Sawhney arXiv:2405.20308v2, Theorem 1.1, proves (1+O((log n)^(-1/16)))t+exp(-Omega(n)); this still does not supply the exact coefficient-one target. The parent target remains unsolved by this record."
new['correction_source']='https://arxiv.org/pdf/0903.0614 Theorem 1.1 equations (1)-(2); https://arxiv.org/html/2405.20308v2 Theorem 1.1'
new['correction_status']='DRAFT w567 2026-10-10; independent review pending'
new_line=json.dumps(new,ensure_ascii=False,sort_keys=True)
patch_dir=ROOT/'patches'; patch_dir.mkdir(exist_ok=True)
relative='<private-repo>/06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl'
patch=f'--- a/{relative}\n+++ b/{relative}\n@@ -{line_number},1 +{line_number},1 @@\n-{old_line}\n+{new_line}\n'
(patch_dir/'01_c0029_gaussian_limit.diff').write_text(patch,encoding='utf-8')
save('CORRECTED_SOURCE_ROW.json',new)
save('SOURCE_ROW_PRECONDITION.json',{'live_path':str(live),'line':line_number,
    'original_record_utf8_sha256':digest(old_line.encode('utf-8')),
    'replacement_record_utf8_sha256':digest(new_line.encode('utf-8')),
    'apply_root':'~','mathematical_proof':False})

store=json.loads((ROOT/'STORE_C0029_READONLY.json').read_text(encoding='utf-8'))
node=next(n for n in store['nodes'] if n['title'].startswith('Attempt on'))
meta=json.loads(node['metadata_json'])
new_body='ATTEMPT RECORD, corrected draft; mathematical review pending. '+new['result']+' Key identity: '+new['key_identity']+' Obstruction: '+new['obstruction']+'\nRefers to the open problem node open-problem-c0029-spielman-teng-conjecture-on-the-least-singular-value-of-bernoulli-matr\nNo solved claim; result status attempted_unsolved'
save('STORE_CORRECTION.json',{'state':'DRAFT; DO NOT APPLY WITHOUT MATHEMATICAL REVIEW',
    'store_as_read':store['store'],'target_node_id':node['id'],
    'target_logical_id':meta['logical_id'],'expected_revision_digest':meta['revision_digest'],
    'original_body':node['body'],'replacement_body':new_body,
    'reason':'The real Gaussian limit was asserted as a finite-n exact law.',
    'evidence':['C0029-w567-C1','MEASUREMENTS.json','https://arxiv.org/pdf/0903.0614'],
    'keep_attempt_unsolved':True,'independent_review':'PENDING w569',
    'served_model_evidence':'UNAVAILABLE; no promotion gate passed'})

# Exact collision checks use only rational arithmetic and no additional matrix population.
measure=json.loads((ROOT/'MEASUREMENTS.json').read_text(encoding='utf-8'))
collision=[]
for n in [2,4,8,16]:
    q=2**(n-1); m=n*(n-1)//2; no_collision=Fraction(1)
    for j in range(n): no_collision*=1-Fraction(j,q)
    p=1-no_collision; lower=Fraction(m,q)-Fraction(m*(m-1),2*q*q)
    assert lower<=p<=Fraction(m,q)
    collision.append({'n':n,'exact_collision_fraction':str(p),
        'collision_probability':float(p),'ratio_to_2_power_minus_n':float(p*2**n)})
measure['checks']['collision_floor']=collision
measure['source_correction_before_after']={'false_finite_gaussian_identity_fields_before':2,
    'false_finite_gaussian_identity_fields_after':0,
    'scope':'proposed local source row only; live store not changed'}
save('MEASUREMENTS.json',measure)

source=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source.update({'current_openness':'UNKNOWN: 2025 primary result retains 1+o(1); targeted October-2026 primary search found no exact-coefficient resolution, which is not exhaustive.',
 'local_prior_attempt_check':'Only C0029-A001 found in the named intake, H/I attempt and Lean packets by exact-ID/eponym scan. No C0029 assignment on current Team O board.',
 'owner_solved_retired_check':'Top three recall memories and named scars read. The recalled coordinate-submatrix Gaussian result is a different target. Targeted live-store read returned the unsolved C0029 concept and attempted-unsolved record only; no solved/retired certificate found. Absence is not a current-openness proof.',
 'source_record_precondition':'SOURCE_ROW_PRECONDITION.json',
 'live_store_error':'STORE_CORRECTION.json includes exact node/revision precondition and proposed corrected body.',
 'gaussian_law_source':{'url':'https://arxiv.org/pdf/0903.0614','locator':'Theorem 1.1 equations (1)-(2), page 3; Theorem 1.3','short_quote':'Limiting distributions for gaussian models'},
 'recall_seconds':12.61,
 'memory_slugs':['complex_ginibre_average_singular_value_is_decreasing_proved_2026_09_08','open_problem_least_sv_submatrix_2026_07_06','an_authors_own_read_is_not_a_review_and_a_name_is_a_family_of_names_2026_09_03','perceptron_proof_open_gaps_fleet_2026_07_12','proof_steps_need_derived_joint_structure_2026_09_09']})
save('SOURCE_STATUS.json',source)

# Own proofs are campaign work; keep license tag exact. No mathematical parent theorem.
entries=[]
names={'L1':'prescribed-bernoulli-row-proportionality-floor',
 'L2':'arithmetic-singular-value-gap-for-sign-matrices',
 'L3':'sign-matrix-normalization-and-bordered-bernoulli-inverse',
 'L5':'flat-hadamard-kernel-conditional-small-ball-obstruction',
 'L6':'bernoulli-proportional-row-collision-floor',
 'C1':'real-gaussian-least-singular-value-limit-versus-finite-law'}
for key in names:
    statement,assumptions=specs[key]
    proof_text=sections[key] if key!='C1' else None
    if key=='L2':
        proof_text='Using the sign normalization and determinant identity of L3, |det(B)|=2^(n-1)|det(H)|>=2^(n-1) for nonsingular B. Also sum_i s_i^2=n^2. AM-GM on the largest n-1 singular values gives product_{i<n}s_i<=(n^2/(n-1))^((n-1)/2). Divide the determinant product by this bound. The strict-cutoff event equivalence follows immediately.'
    entries.append({'key':key.lower(),'namespace':'probability.random-matrices',
       'logical_name':names[key],'kind':'concept' if key=='C1' else 'lemma',
       'title':names[key].replace('-',' ').capitalize(),
       'statement':statement,'proof_text':proof_text,'assumptions':assumptions,
       'domain':'probability theory and matrix analysis',
       'source':{'source_id':'owner-own-work:w567:C0029:'+key,
           'url':'https://arxiv.org/pdf/0903.0614' if key=='C1' else None,
           'revision':'draft-2026-10-10-review-pending','license':'owner-own-work',
           'excerpt':None}})
relations=[{'from_key':'l2','to_key':'l3','kind':'depends_on',
 'rationale':'L3 gives det(C)=(-2)^(n-1)det(H) with integer H and preserves singular values; L2 combines this divisibility with AM-GM.'},
 {'from_key':'l6','to_key':'l1','kind':'generalizes',
 'rationale':'L1 uses one prescribed proportional-row event. L6 takes the union over all row pairs and derives its exact collision probability.'},
 {'from_key':'c1','to_existing_logical':meta['logical_id'],'kind':'cites',
 'rationale':'C1 corrects only the finite-n exact-law assertion in this attempted-unsolved concept, using the Gaussian limit source and an n=1 counterexample.'}]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w567',
 'bundle_slug':'c0029-arithmetic-route-and-gaussian-limit-correction-w567-001',
 'entries':entries,'relations':relations}
save('DRAFT_BUNDLE.json',bundle)
support=[]
for rel in relations:
    left=next(e for e in entries if e['key']==rel['from_key'])
    right=(next(e for e in entries if e['key']==rel['to_key'])['statement']
           if 'to_key' in rel else node['body'])
    support.append({'relation':rel,'from_statement_quoted':left['statement'],
                    'to_statement_quoted':right,'review_state':'DRAFT'})
(ROOT/'RELATION_SUPPORT.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in support),encoding='utf-8')

hook={'id':'gaussian-limit-w567-01','area':'math','event':'stage-start',
 'cue':'a finite-n random-matrix CDF is called exact using a limiting Gaussian hard-edge formula',
 'fire_when':'C0029-A001 treats 1-exp(-t-t^2/2) as the exact real Gaussian finite-n law',
 'silent_when':'The author states n tends to infinity, retains the finite-n error, or uses the complex Gaussian exact formula with its proper normalization',
 'text':'Before using an exact Gaussian law at finite n, check the source quantifiers and n=1. Real and complex hard-edge laws differ; a limit CDF does not certify a finite-n identity.',
 'evidence':'~/brain_workers/w567/MEASUREMENTS.json gaussian_correction: n=1,t=0.1,error=0.02001980286; memory an_authors_own_read_is_not_a_review_and_a_name_is_a_family_of_names_2026_09_03',
 'proposer':'w567'}
assert len(hook['text'])<=300
hook_line=json.dumps(hook,ensure_ascii=False)+'\n'
(ROOT/'HOOK_PROPOSAL.jsonl').write_text(hook_line,encoding='utf-8')
hook_path='primary_directive/hooks1000/proposals/gaussian-limit-w567.jsonl'
(patch_dir/'02_gaussian_limit_hook.diff').write_text(
    '--- /dev/null\n+++ b/'+hook_path+'\n@@ -0,0 +1,1 @@\n+'+hook_line,encoding='utf-8')

save('BUNDLE_LIFECYCLE.json',{'prepared':True,'submitted':False,'reviewed':False,
 'ingested':False,'retrievable':False,'independent_review':'PENDING w569',
 'served_model_gate':'UNAVAILABLE; not passed','live_store_mutated':False,
 'hook_proposal':'LOCAL unified diff; global write boundary preserved'})
print(json.dumps({'claims':len(rows),'draft_entries':len(entries),
 'relations':len(relations),'patches':2,'source_row_line':line_number,
 'false_finite_identity_fields_before':2,'after':0,
 'live_source_or_store_writes':0}))
