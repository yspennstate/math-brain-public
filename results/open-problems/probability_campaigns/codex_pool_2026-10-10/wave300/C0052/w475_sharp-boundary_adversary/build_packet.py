"""Build a reviewable packet and concept-only draft; never touch live stores."""
from pathlib import Path
import hashlib
import json
import difflib
import re

ROOT = Path(__file__).resolve().parent
INBOX = Path('~/math-brain-inbox/w475')
def save(name,obj):
    (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

source = json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8-sig'))
source.update({
    'primary_source':{'id':'duminil_copin_ising_potts_2017','title':'Lectures on the Ising and Potts models on the hypercubic lattice',
        'version':'IHES PDF dated 29 June 2017, printed p.94; 101 PDF pages in direct web retrieval',
        'url':'https://www.ihes.fr/~duminil/publi/2017_PIMS.pdf',
        'locator':'Section 7, (7.1)-(7.2), Conjecture 6, Exercise 61',
        'short_quote':'Prove that the three-dimensional Ising model is non-trivial',
        'statement_verification':'direct primary-source web read; signed g and limits recovered',
        'file_hash_verification':'historical intake records a different downloaded PDF hash; not independently rehashed here'},
    'precise_operational_target':{'model':'zero-field nearest-neighbor ferromagnetic Ising on Z^3, free infinite-volume state',
        'regime':'0<beta<beta_c, beta increases to beta_c',
        'signed_coupling':'g(beta)=sum U4(0,x2,x3,x4)/(chi(beta)^2 xi(beta)^3)',
        'chi':'sum_x E_beta[sigma_0 sigma_x]',
        'xi':'(-lim_n n^(-1) log E_beta[sigma_0 sigma_(n e1)])^(-1)',
        'quantifier':'g(beta) does not tend to zero; since g<=0, equivalently some epsilon>0 and beta_n increasing to beta_c have -g(beta_n)>=epsilon',
        'stronger_unproved_routes':['positive full liminf','non-Gaussianity of every critical-field subsequential limit','source-scale uniform endpoint event bound']},
    'prior_work_checks':[
        {'path':'probability_1000_intake_claude_20260907/problems.jsonl:52','result':'attempted_unsolved; historical source says open'},
        {'path':'probability_1000_intake_claude_20260907/attempts.jsonl:42','result':'variance bound unclosed; heuristic cluster independence and scale equivalence need correction'},
        {'path':'probability_1000_attempts_H_20260912; probability_1000_attempts_I_20260914','result':'targeted C0052 search found no exact record'},
        {'path':'prob1000_lean_20260908/RANKED_LIST_2026-09-07_annotated.md:592','result':'attempted_un ranking only; no formal proof receipt'},
        {'path':'other named intake problem/attempt records','result':'targeted C0052 search found no additional exact record'},
        {'path':'~/brain_workers/teams/W0300_O/TEAM_BOARD.md','result':'C0052 absent from listed team tasks'},
        {'path':'~/Big Open problem in probability theory/README.md; ~/Open problem project/solved_register.md','result':'named local solved register concerns other problems; no C0052/Ising hit'},
        {'path':'live_target_receipt.json','result':'exact target card retrieved from canonical population sqlite in read-only mode'},
        {'path':'https://arxiv.org/html/1912.07973','result':'4D Gaussianity and one-sided current sprinkling; no 3D solution'},
        {'path':'https://arxiv.org/abs/2309.05797','result':'2025 revision covers effective dimension >=4, including certain long-range lower-dimensional models; does not settle nearest-neighbor 3D'}],
    'current_openness':'UNKNOWN','status_search_limit':'bounded public-primary and named-local search; no resolution identified, not an exhaustive current-open certification',
    'memory_check':{'recall':'60-second timeout','fallback_slug':'perceptron_proof_open_gaps_fleet_2026_07_12',
        'lesson':'successful finite checks and pipeline labels do not close the hardest parent proof gap'},
    'hardest_remaining_gap':'positive subsequential lower bound for the four-distinct-site Ursell sum divided by chi^2 xi^3 under the exact sourced two-current law',
    'formal_check_receipt':None,'source_check_is_proof':False})
save('SOURCE_STATUS.json',source)

claims=[json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
for row in claims:
    if row['claim_id'] in ('w475-C0052-contact-001','w475-C0052-sprinkling-001'):
        r='R2' if row['claim_id'].endswith('contact-001') else 'R3'
        row.update({'independent_reviewer':'w476','status':'independently checked proof',
            'review_state':'scoped KEEP at ~/brain_workers/w476/REVIEW.jsonl:'+r,
            'review_limit':'named independent reviewer; response-side account/model and frozen-hash attestation unavailable',
            'remaining_gap':'parent distinct-site lower bound remains open; model/account diversity gate not established'})
    row['source']['primary_source_verification']='exact background identities checked; owner derivation is distinct from source verification'
claims.append({'claim_id':'w475-C0052-transitivity-boundary-001','problem_id':'C0052',
    'statement':'For N spins with one perfectly locked component of m spins and N-m independent fair spins, the uniform-weight contact ratio equals [12m^3-22m^2+12m+2(N-m)]/(m^2+N-m)^2. With m=floor(sqrt(3N)), sqrt(N) times this ratio tends to 9sqrt(3)/4. The 12/N bound therefore needs transitivity; the general N^-1/2 decay exponent is optimal over the broader nonnegative-correlation +/-1 field class.',
    'assumptions':['independent components','one locked fair-sign component','uniform weights','mean-zero +/-1 spins'],
    'source':{'type':'owner-own-work','location':'ATTEMPT.md#boundary-of-the-transitive-finite-graph-estimate'},
    'proof_or_counterexample':'Joint cumulants vanish across independent components. In the locked block, -U4=2 for each repeated tuple; their number is m^4-m(m-1)(m-2)(m-3). Isolated spins contribute 2 each. Divide by squared variance and take the asymptotic.',
    'independent_reviewer':'w476; pending','remaining_gap':'Independent referee check; not a translation-invariant critical 3D Ising example',
    'status':'proved special case','review_state':'author-derived; independent review pending','parent_problem_solved':False})
(ROOT/'CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in claims),encoding='utf-8')

owner_source={'source_id':'owner-own-work:w475:C0052-boundaries-2026-10-10',
    'url':(ROOT/'ATTEMPT.md').as_uri(),'revision':'author-derived-2026-10-10; scoped independent reviews recorded separately',
    'license':'owner-own-work','excerpt':None}
entries=[
    {'key':'weighted-contact','namespace':'probability.statmech','logical_name':'ising-weighted-contact-cumulant-delocalization-bound',
     'kind':'concept','title':'DRAFT: repeated-site Ising cumulants vanish for delocalized block weights',
     'statement':'DRAFT concept; author derivation, finite weighted/transitive bound independently kept by w476; broader block extension pending. Let sigma be mean-zero spin-flip-symmetric +/-1 spins, G(x,y)=E sigma_x sigma_y>=0, w_x>=0 finitely supported and nonzero, V=E(sum w_x sigma_x)^2. For q_x=w_x(sum_y w_y G(x,y))/V, sum q_x=1. Let D be the negative fourth-cumulant sum over ordered quadruples with a repeated site, weighted by the four w factors and divided by V^2. Then U4(x,x,y,z)=-2G(x,y)G(x,z), and 0<=D<=12sum q_x^2<=12max q_x<=12||w||_infinity/sqrt(V)<=12||w||_infinity/||w||_2. Uniform weights on a transitive N-site graph give D<=12/N; arbitrary N-site blocks give D<=12/sqrt(N). This removes exact coincidences only and does not prove critical 3D Ising non-triviality.',
     'proof_text':None,'assumptions':['spins +/-1','spin-flip symmetry','G>=0','finite nonnegative nonzero weights'],
     'domain':'probability theory','source':owner_source},
    {'key':'reverse-sprinkling','namespace':'probability.statmech','logical_name':'random-current-reverse-sprinkling-path-obstruction',
     'kind':'concept','title':'DRAFT: no uniform proportional reverse of current sprinkling',
     'statement':'DRAFT concept; special-case proof independently kept by w476; model/account diversity gate unverified. In zero-field ferromagnetic Ising on the path 0,...,3m with uniform beta>0, n1,n2 have source sets {0,m},{2m,3m}; n3,n4 are independent sourceless currents, all four independent. Set p=tanh(beta)^2. The original all-four-connected event in n1+n2 has probability p^m. The independent clusters C(n1+n3,0), C(n2+n4,2m) intersect with probability p^m[1+m(1-p)]. Therefore no graph- and scale-uniform c>0 gives original_probability>=c*sprinkled_probability. The four source distances are comparable to m. This refutes a quantitative reverse bridge only; both probabilities vanish at fixed beta, and the full critical Z^3 conjecture is untouched.',
     'proof_text':None,'assumptions':['finite path','uniform beta>0','zero external field','stated independent current source sets'],
     'domain':'probability theory','source':owner_source}]
target='math:probability.statmech:open-problem-c0052-non-triviality-of-the-scaling-limit-of-the-three-dimensional-ising-mod'
receipt=json.loads((ROOT/'live_target_receipt.json').read_text(encoding='utf-8'))
relations=[]
if any(r['logical_id']==target for r in receipt['targets']):
    relations=[{'from_key':e['key'],'to_existing_logical':target,'kind':'semantic_association',
                'rationale':'Exact verified existing C0052 target concerns critical Ising non-Gaussianity. This scoped obstruction guards a proposed proof route and establishes no solution or refutation of the target.'} for e in entries]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w475','bundle_slug':'c0052-weighted-contact-and-current-bridge-001',
        'entries':entries,'relations':relations}
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
for e in entries:
    assert required<=set(e) and e['kind']=='concept' and e['proof_text'] is None
    assert e['source']['license'].startswith('owner-own-work') and 'DRAFT' in e['statement']
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
assert all(r['kind'] in allowed and r['from_key'] in {e['key'] for e in entries} for r in relations)
save('bundle_001.json',bundle)
INBOX.mkdir(parents=True,exist_ok=True)
assert INBOX.resolve().is_relative_to(Path('~/math-brain-inbox').resolve())
part=INBOX/'bundle_001.part'
destination=INBOX/'bundle_001.json'
assert not destination.exists(), 'Do not overwrite an already submitted draft.'
part.write_text((ROOT/'bundle_001.json').read_text(encoding='utf-8'),encoding='utf-8')
part.replace(destination)

hook={'id':'C0052-w475-01','area':'math','event':'stage-start',
      'cue':r'(?is)(random.current|sourceless.current).{0,180}(sprinkling|sprinkled).{0,100}(lower bound|reverse comparison|non.gaussian)',
      'fire_when':'Propose a lower bound for non-Gaussianity by reversing the upper comparison after adding sourceless currents.',
      'silent_when':'Use sprinkled currents only to upper-bound an intersection probability, or prove the exact sourced-current lower bound directly.',
      'text':'Check the exact sourced-current law and inequality direction. Adding sourceless currents supplies an upper comparison; a lower bound for the enlarged independent clusters needs a proved reverse transfer. On a path the amplification is 1+m(1-tanh(beta)^2).',
      'evidence':'~/brain_workers/w475/bridge_measurements.json: path-sprinkling m=64 amplification=49; ATTEMPT.md; w476 REVIEW.jsonl R3',
      'proposer':'w475'}
assert len(hook['text'])<=300
line=json.dumps(hook,ensure_ascii=False)+'\n'
(ROOT/'HOOK_PROPOSAL.jsonl').write_text(line,encoding='utf-8')
patches=ROOT/'patches'
patches.mkdir(exist_ok=True)
live='~/primary_directive/hooks1000/proposals/probability-w475.jsonl'
diff=''.join(difflib.unified_diff([],line.splitlines(True),fromfile='a/'+live,tofile='b/'+live))
(patches/'01_current_sprinkling_hook.diff').write_text(diff,encoding='utf-8')

peer=Path('~/brain_workers/w474/ATTEMPT.md')
snapshot=peer.read_bytes()
(ROOT/'w474_ATTEMPT_reviewed.md').write_bytes(snapshot)
files=['ATTEMPT.md','CLAIMS.jsonl','SOURCE_STATUS.json','PEER_REVIEW.md','AUDIT_ROWS.jsonl','REPORT.md',
       'measurements.json','bridge_measurements.json','COMPUTE_GATE.json','BRIDGE_COMPUTE_GATE.json',
       'verify_contact.py','verify_bridges.py','bundle_001.json','HOOK_PROPOSAL.jsonl',
       'patches/01_current_sprinkling_hook.diff','w474_ATTEMPT_reviewed.md','live_target_receipt.json']
hashes={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in files}
packet={'worker':'w475','target':'C0052','parent_problem_solved':False,'source_openness':'UNKNOWN',
        'proof_artifact':str(ROOT/'ATTEMPT.md'),'artifact_sha256':hashes,
        'paired_proof_snapshot':{'path':str(ROOT/'w474_ATTEMPT_reviewed.md'),'sha256':hashes['w474_ATTEMPT_reviewed.md'],
            'scope':'w474 L1-L3 and C1; compare with AUDIT_ROWS.jsonl'},
        'independent_review_receipts':{'path':'~/brain_workers/w476/REVIEW.jsonl',
            'keeps':{'R2':'finite weighted/transitive contact bound','R3':'path reverse-sprinkling obstruction'},
            'pending':['general block rate','source-normalized exact count','nontransitive sharpness example'],
            'frozen_hash_bound':False},
        'model_gate':{'author_response_side_evidence':None,'referee_response_side_evidence':None,
                      'different_account_verified':False,'different_model_verified':False,'promotion_allowed':False},
        'measurements':{'cube_checks':10,'bridge_and_boundary_checks':17,'exact_formula_errors':0,
                       'cube_seconds':39.549496500054374,'bridge_seconds':0.08967050001956522,
                       'no_live_recall_improvement_claim':True},
        'brain_output':{'draft':str(destination),'schema_local_check':'PASS: two concept entries, allowed source license and exact existing target ends',
            'submitted':True,'reviewed':'partial scoped mathematical KEEP; deployment/model gates pending',
            'ingested':False,'retrievable':False,'live_store_mutated':False},
        'hook_output':{'proposal':str(ROOT/'HOOK_PROPOSAL.jsonl'),'patch':str(patches/'01_current_sprinkling_hook.diff'),
                       'submitted':False,'applied':False,'reason':'worker write restriction; reviewer applies the ready unified diff'},
        'formal_verification':{'receipt':None,'no_admitted_placeholder':True,'method':'written derivation plus exact finite corroboration; no formal proof claim'},
        'NEXT':'Finish independent checks of later contact extensions; seek a model-specific lower bound for distinct-site exact two-current Ursell mass.'}
save('review_packet.json',packet)
print(json.dumps({'draft_submitted':str(destination),'entries':len(entries),'relations':len(relations),
                  'artifact_sha256':hashes['ATTEMPT.md'],'checks':27,'live_store_mutated':False},indent=2))
