"""Write local review artifacts only. No submission, integration or messaging."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
read = lambda name: (ROOT/name).read_text(encoding='utf-8')
write_json = lambda name, obj: (ROOT/name).write_text(json.dumps(obj, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
receipt = json.loads(read('DISPLAY_TEST_RECEIPT.json'))
root_url = 'urn:owner-probability-campaign:w382:P0110:'
source = lambda key: {'source_id':'owner-own-work:w382:P0110:'+key,
    'url':root_url+key, 'revision':'draft-2026-10-10',
    'license':'owner-own-work (Codex w382 campaign derivation; independently unreviewed)', 'excerpt':None}
rare_statement = ('For n>=2 let B_n~Bernoulli(n^(-1/2)) and C_n~Bernoulli(n^(-1/4)); no independence is needed. '
    'Set X_n=n^(1/2)(B_n-n^(-1/2)) and D_n=n^(3/4)C_n. The exponential-moment upper endpoints '
    'and variance/expectation lower endpoints are respectively chi_a=1/2, chi_b=1/4, xi_a=3/4, xi_b=1/2. '
    'Thus moment growth alone does not force these pairs to match. This is a scalar example, not iid FPP; independent referee check is pending.')
norm_statement = ('A supporting-sphere direction of a norm does not imply a positive quadratic detour bound in every direction. '
    'For g(x)=||x||_1 on R^2, n a positive multiple of four, v=(n,n), z=(3n/4,n/4), '
    'g(z)+g(v-z)-g(v)=0 while dist(z,[0,v])=n/(2sqrt(2)). '
    'Therefore a bound c dist(z,[0,v])^2/|v|-K with c>0 and finite K cannot hold uniformly in n and direction just from the norm axioms. '
    'This geometry example does not assert that an eligible continuous iid FPP law has this shape. Independent referee check is pending.')
upgrade_statement = ('Let D_n>=0 be random variables, U_n>=0 and V_n>0 deterministic, n>=2. '
    'Assume P(D_n>sqrt(U_n+V_n t))<=exp(-t) for every n and every t>=0, '
    'U_n<=A n^(2tau)log(2+n) and V_n<=B n^(2tau), with fixed A,B>0 and tau>=0. '
    'Then for every r>tau and lambda>0, sup_n E exp(lambda D_n/n^r)<infinity. '
    'An explicit bound is 2 exp(lambda sqrt(U_n)/n^r+lambda^2 V_n/(2n^(2r))). '
    'Applied to the conditional supporting-direction FPP tail, tau=(1+q)/2. This does not give uniformity in other directions or matching lower endpoints. Independent referee check is pending.')
claims = [
    {'id':'w382-P0110-rare-tail-002','kind':'route_counterexample','status':'proved special case',
     'statement':rare_statement,'assumptions':['n>=2','B_n and C_n have the stated Bernoulli marginals','Endpoints use a single scalar sequence, not all FPP displacements'],
     'source':source('rare-tail-obstruction'),'proof_or_counterexample':read('INDEPENDENT_OBSTRUCTION.md'),
     'independent_reviewer':'w383 (pending)','remaining_gap':'Independent referee check; no iid FPP realization or target closure.', 'review_state':'draft'},
    {'id':'w382-P0110-direction-003','kind':'route_counterexample','status':'proved special case',
     'statement':norm_statement,'assumptions':['g is the l1 norm on R^2','n is a positive multiple of four'],
     'source':source('directional-global-obstruction'),
     'proof_or_counterexample':'Both z and v-z have nonnegative coordinates and l1 norm n, while g(v)=2n. The projection of z onto [0,v] is (n/2,n/2); its perpendicular distance is sqrt(2)*n/4. The proposed lower bound grows linearly in n, so no constant subtraction K repairs it.',
     'independent_reviewer':'w383 (pending)','remaining_gap':'Independent referee check; abstract geometry obstruction only.', 'review_state':'draft'},
    {'id':'w382-P0110-exponential-004','kind':'conditional_deduction','status':'sketch',
     'statement':upgrade_statement,
     'assumptions':['All t>=0, not just one polynomial tail threshold','U_n,V_n deterministic','Uniform finite A,B,tau','Strict r>tau'],
     'source':source('conditional-exponential-upgrade'),'proof_or_counterexample':read('CONDITIONAL_EXPONENTIAL_UPGRADE.md'),
     'independent_reviewer':'w383 (pending)','remaining_gap':'Independent referee check; directional and conditional. Does not prove exponent matching.', 'review_state':'draft'},
    {'id':'w382-P0110-audit-005','kind':'peer_proof_audit','status':'proved special case',
     'statement':'Under w381 L1--L5 assumptions (iid positive bounded weights, uniform centered exponential envelope with q>=0, deterministic rounding of a norm-minimizing direction), the terminal-bias identity and finite-scale bound for D(0,v_n) are valid. The cited global KPZ conclusion still needs matching both global upper/lower exponent pairs for one admissible law.',
     'assumptions':['The assumptions and exact constants in w381 ATTEMPT.md L1--L5'],
     'source':{'path':'~/brain_workers/w381/ATTEMPT.md','scope':'L1--L5'},
     'proof_or_counterexample':read('REVIEW.md'),'independent_reviewer':'w382 (independent adversary); w383 final referee pending',
     'remaining_gap':'For the global-KPZ route: matched global exponents for a concrete law. For L3 prose: specify that the farther endpoint is at least L away in an overshoot.',
     'verdict':'KEEP_CONDITIONAL','review_state':'local audit saved; not submitted'},
    {'id':'w382-P0110-recall-006','kind':'measured_retrieval_failure','status':'numerical evidence',
     'statement':'The observed withdrawn FPP obstruction is labeled provisional by the original recall display. Replaying the actual display loops on that memory changes stale-label and unsafe-snippet counts from 1 to 0 each. In 25 synthetic controls, stale labels change 9->0, unsafe snippets 12->0, and 12 active/unavailable controls are unchanged.',
     'assumptions':['Frozen original/candidate code','Actual display-loop replay, not end-to-end recall'],
     'source':{'memory_slug':'the_binding_constraint_is_m_not_l1prime_2026_08_29','report':'DISPLAY_TEST_RECEIPT.json'},
     'proof_or_counterexample':'python -X utf8 verify_recall_display.py; elapsed '+str(receipt['elapsed_seconds'])+' seconds.',
     'independent_reviewer':'claude-4a88bc43 (engineering deployment review pending)',
     'remaining_gap':'Not deployed; no corpus-wide, ranking, or end-to-end recall claim.', 'review_state':'draft'},
]
existing = [json.loads(line) for line in read('CLAIMS.jsonl').splitlines() if line.strip()]
new_ids = {claim['id'] for claim in claims}
with (ROOT/'CLAIMS.jsonl').open('w',encoding='utf-8') as handle:
    for claim in [c for c in existing if c['id'] not in new_ids]+claims:
        handle.write(json.dumps(claim,ensure_ascii=False)+'\n')

entries=[]
def entry(key,kind,title,statement,assumptions):
    entries.append({'key':key,'namespace':'probability.fpp','logical_name':'p0110-'+key,
        'kind':kind,'title':'DRAFT: '+title,'statement':statement,'proof_text':None,
        'assumptions':assumptions,'domain':'probability; proof-method scope','source':source(key)})
entry('sequence-endpoints','definition','Scalar versions of four exponent endpoints',
    'For real centered X_n of finite variance and D_n>=0, n>=2, define chi_a=inf{s: some alpha>0 has sup_n E exp(alpha|X_n|/n^s)<infinity}; chi_b=sup{s: for some N, inf_{n>N} Var(X_n)/n^(2s)>0}; xi_a is the same upper definition with D_n replacing |X_n|; xi_b=sup{s: for some N, inf_{n>N} E D_n/n^s>0}. Infimum/supremum can be extended real. These scalar definitions do not impose the all-displacement uniformity of FPP global exponents.',
    ['n>=2','X_n centered with finite variance','D_n nonnegative with finite expectation'])
entry('moment-only-route','concept','Moment-to-exponential matching route is invalid',
    'The proposed inference from Var(X_n)=Theta(n^(2chi)) and E D_n=Theta(n^xi) to chi_a=chi_b=chi and xi_a=xi_b=xi is false without further tail assumptions. Polynomially rare large deviations can change the exponential upper endpoints while preserving those moment growth laws. This is a refuted abstract route, not an accepted theorem about FPP.',
    ['Upper and lower endpoints as defined in sequence-endpoints','No additional uniform tail premise'])
entry('rare-tail-obstruction','concept','Rare-tail gap between upper and lower endpoints',rare_statement,
    ['Bernoulli marginals specified in the statement','No iid FPP construction claimed','Independent referee check pending'])
entry('directional-global-obstruction','concept','One support direction cannot supply all directions',norm_statement,
    ['Abstract norm geometry','Independent referee check pending'])
entry('conditional-exponential-upgrade','concept','Full Gaussian-form tail gives a larger-scale exponential moment',upgrade_statement,
    ['Full all-t tail','Deterministic U_n,V_n and uniform A,B,tau','Independent referee check pending'])
entry('global-hypothesis-gate','concept','Exact missing premise in the conditional KPZ route',
    'For iid nonnegative nearest-neighbor FPP on Z^d, d>=2, Chatterjee Theorem 1.1 assumes a nearly-gamma law with a moment-generating function near zero. Its upper exponents use uniform exponential moments of |T(0,v)-E T(0,v)|/|v|^s and D(0,v)/|v|^s over all nonzero displacements; its lower exponents use variance and expected segment-deviation lower bounds uniform outside a large ball. The KPZ conclusion requires both upper/lower pairs to match. For P0110 this is a sufficient formalized route, not a supplied law or a consequence of variance growth. Auffinger--Damron removes the nearly-gamma restriction for its conditional relation; it does not remove exponent matching. This node is an owner campaign hypothesis comparison of arXiv:1105.4566 Theorem 1.1 and arXiv:1109.0523 Theorems 2.1--2.2, not a new proof of those published theorems.',
    ['Primary theorem hypotheses retained','A chosen law still needs matching global endpoints'])
relations = [
    {'from_key':'rare-tail-obstruction','to_key':'sequence-endpoints','kind':'depends_on',
     'rationale':'The four exact values in the example use the exponential-upper and moment-lower definitions stated at sequence-endpoints.'},
    {'from_key':'rare-tail-obstruction','to_key':'moment-only-route','kind':'refutes',
     'rationale':'The source end gives chi_a=1/2 versus chi_b=1/4 and xi_a=3/4 versus xi_b=1/2. The target end names the inference that moment growth forces these pairs to match; the explicit mismatches refute that abstract inference.'},
    {'from_key':'directional-global-obstruction','to_key':'global-hypothesis-gate','kind':'semantic_association',
     'rationale':'The source end disproves extending one norm-support direction to every direction from norm axioms. The target end requires upper/lower estimates uniform over all nonzero displacements. This names a scope mismatch, not a new theorem implication.'},
    {'from_key':'conditional-exponential-upgrade','to_key':'global-hypothesis-gate','kind':'semantic_association',
     'rationale':'The source end supplies an upper exponential moment from a full all-t tail. The target end requires upper moments plus matching global lower endpoints, so the directional upgrade leaves that missing premise explicit.'},
    {'from_key':'global-hypothesis-gate','to_existing_logical':'math:probability.core:open-problem-p0110-an-iid-fpp-law-with-proved-kpz-exponent-relation','kind':'semantic_association',
     'rationale':'The existing P0110 card asks for a nondegenerate iid undirected law with well-defined exponents satisfying chi=2xi-1. This draft names the matching-global-exponent premise for one sufficient primary-source route to that exact target.'},
]
(ROOT/'draft_bundle').mkdir(exist_ok=True)
write_json('draft_bundle/bundle_001.json',{'spec':'mathbrain-draft-v1','author_agent':'w382',
    'bundle_slug':'p0110-w382-route-obstructions-and-exponential-upgrade-001','entries':entries,'relations':relations})
write_json('BUNDLE_STATE.json',{'prepared':True,'submitted':False,'reviewed':False,'ingested':False,'retrievable':False,
    'path':'draft_bundle/bundle_001.json','pending_math_reviewer':'w383','pending_integrator':'validating coordinator',
    'placement_note':'Staged inside w382 because the worker brief restricts writes to this folder. The reviewer can place the approved draft in math-brain-inbox/w382. No integrate_drafts.py run.'})

write_json('SOURCE_STATUS.json',{'target':'P0110','worker':'w382','current_openness':'UNKNOWN',
    'historical_status':'attempted_un (ranking 2026-09-07)','exact_statement_recovered':True,
    'intake_statement':'Exhibit a nondegenerate iid undirected FPP law with well-defined fluctuation and wandering exponents satisfying chi=2xi-1.',
    'primary_question':{'url':'https://arxiv.org/pdf/1511.03262','location':'Section 4.3, Eq. (4.19), Question 22; printed pp. 87-88; intake says PDF p.89',
        'quote':'Find a distribution of passage times where (4.19) holds.','equation':'chi=2xi-1',
        'qualification':'The source itself says exponent existence and correct definition are part of the problem.'},
    'primary_theorems_checked':[{'url':'https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n2-p07-p.pdf','theorem':'1.1','requirements':'d>=2, iid nearly-gamma weights, MGF near zero, both global upper/lower exponent pairs match'},
        {'url':'https://arxiv.org/pdf/1109.0523','theorems':'2.1 and 2.2','requirements':'iid nearest-neighbor model with atom at infimum of support <p_c(d); conditional global exponents; matching chi pair (chi>0 for Theorem 2.1), matching both pairs for Theorem 2.2'}],
    'brain_sources_report':'BRAIN_SOURCE_REPORT.json','brain_database_mode':'read-only',
    'independent_derivation_saved_before_paired_proof':True,'paired_proof_read':True,'paired_proof_scope':'w381 L1--L5',
    'prior_work_status':'The math store prior-attempt card explicitly leaves exponent existence and T-to-norm error control unproved. The cited old Codex worktree is absent. Targeted named-intake/attempt searches yielded no additional P0110 closure.',
    'recent_literature_search':'Bounded primary-literature searches through authorized web tool; no claim that a negative search certifies openness.',
    'canonical_store_note':'Read the task-named math-brain-build source store and its export; no claim that a missing default canonical database path was the only canonical location.',
    'formal_check':None,'target_solved':False})

hook={'id':'recall-retraction-w382-01','area':'brain','event':'PostToolUse',
    'cue':'A recalled proof obstruction has a tagged index status that disagrees with author retraction frontmatter',
    'fire_when':'The binding-constraint FPP memory is returned as provisional although its own status is retracted.',
    'silent_when':'Index and frontmatter both identify an active verified note; a body example merely mentions retraction.',
    'text':'Before using a recalled obstruction, honor an author retraction over any index tag. Suppress the withdrawn summary and read the correction. A verified or provisional index label can be stale.',
    'evidence':'the_binding_constraint_is_m_not_l1prime_2026_08_29; DISPLAY_TEST_RECEIPT.json: live row 1->0 stale labels and unsafe snippets; 25 controls.',
    'proposer':'w382'}
(ROOT/'HOOK_PROPOSALS.jsonl').write_text(json.dumps(hook)+'\n',encoding='utf-8')
write_json('LOCAL_TEAM_UPDATES.json',{'sent':False,'reason':'Worker brief forbids outgoing mesh messages and writes outside w382.',
    'claim':'w382 owns independent rare-tail and directional/global scope obstructions; w381 owns terminal-bias supporting-sphere bridge; w383 checks new deductions.',
    'found':'Author-retracted FPP obstruction displayed as provisional; local patch and finite replay provided.',
    'done':'P0110 conditional adversary packet prepared for w383 and claude-4a88bc43.'})
write_json('PROGRESS_EVENT.json',{'posted':False,'agent':'w382','row':'S1.5',
    'event':'w382 P0110: conditional adversary review saved; stale-retraction display 1->0, 25 controls; recall patch and draft nodes staged.',
    'evidence':str(ROOT/'REPORT.md'),'reason':'Local-only worker write constraint; reviewer can post this concrete result.'})
write_json('review_packet.json',{'worker':'w382','target':'P0110','reviewers':['w383','claude-4a88bc43'],
    'math':['SOURCE_STATUS.json','INDEPENDENT_OBSTRUCTION.md','REVIEW.md','CONDITIONAL_EXPONENTIAL_UPGRADE.md','ATTEMPT.md','CLAIMS.jsonl'],
    'brain_change':['patches/01_recall_retracted_tag_override.diff','PATCH_RECEIPT.json','verify_recall_display.py','DISPLAY_TEST_RECEIPT.json'],
    'draft':'draft_bundle/bundle_001.json','states':'BUNDLE_STATE.json',
    'requested_check':'Independently check new scalar obstructions and exponential upgrade; reproduce display and patch-application tests before deploying.'})
print(json.dumps({'claims':len(existing)+len(claims),'draft_entries':len(entries),'draft_relations':len(relations),'submitted':False}))
