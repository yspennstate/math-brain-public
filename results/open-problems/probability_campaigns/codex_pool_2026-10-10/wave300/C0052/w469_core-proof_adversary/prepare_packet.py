"""Prepare local research artifacts; does not integrate or mutate live data."""
from __future__ import annotations
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

R=Path(__file__).resolve().parent
INTAKE=Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907')
now=datetime.now(timezone.utc).isoformat()
def write_json(name,data):
    (R/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def one_row(path, key, value):
    with path.open(encoding='utf-8') as stream:
        for i,line in enumerate(stream,1):
            row=json.loads(line)
            if row.get(key)==value:
                return i,row
    raise RuntimeError(f'No exact row {value} in {path}')

line,problem=one_row(INTAKE/'problems.jsonl','problem_id','C0052')
source_line,source=one_row(INTAKE/'sources.jsonl','source_id',problem['source_id'])
attempt_line,old_attempt=one_row(INTAKE/'attempts.jsonl','attempt_id','C0052-A001')
status=json.loads((R/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
status.update({'exact_statement_recovered':True,
    'exact_statement':'For the zero-field nearest-neighbor ferromagnetic Ising model on Z^3, with g(beta)=sum U4(0,x2,x3,x4)/(chi(beta)^2 xi(beta)^3) and exponential xi as in (7.2), prove that g(beta) does not tend to zero as beta increases to beta_c. Equivalently, since g<=0, there are epsilon>0 and beta_n increasing to beta_c with -g(beta_n)>=epsilon.',
    'source_locator':problem['locator'], 'intake_statement':problem['statement'],
    'primary_sources':[
      {'url':'https://arxiv.org/abs/1707.00520','author':'Hugo Duminil-Copin','locator':'printed p.94, Conjecture 6, equations (7.1)-(7.2); Exercise 61 on p.95','read_url':'https://www.ihes.fr/~duminil/publi/2017PIMS.pdf','intake_record':str(INTAKE/'sources.jsonl')+f':{source_line}','historical_hash_not_recomputed':source['sha256']},
      {'url':'https://arxiv.org/html/2112.04248v2','author':'Michael Aizenman','locator':'equations (5.9), (5.13), (8.1)-(8.3)','read_state':'relevant passages read'},
      {'url':'https://annals.math.princeton.edu/2021/194-1/p03','authors':['Michael Aizenman','Hugo Duminil-Copin'],'locator':'2021 194(1), pp.163-235','scope':'four-dimensional Gaussian scaling limits, does not solve the three-dimensional target'}],
    'prior_work_checks':{'intake_problem_line':line,'intake_attempt_line':attempt_line,
      'H_and_I_attempt_directories':'Exact C0052 grep returned no matching records',
      'lean_annotated_ranking':'C0052 remains attempted_un in the dated record, line 592',
      'team_O_board':'C0052 not listed; no ownership overwritten',
      'population_export':'Existing C0052 problem and reduction cards are marked unverified',
      'owner_solved_or_retired_status':'No verified disposition found in the inspected target records; canonical checks documented separately; absence is not a novelty certificate'},
    'current_openness':'UNKNOWN','literature_search_scope':'Bounded primary-source search on 2026-10-10 found no verified 3D solution; not an exhaustive current-status certificate',
    'paired_prover_proof_read':True,'independence_receipt':'INDEPENDENT.md hash frozen in VERIFICATION.json before peer proof read',
    'author_model_evidence':{'requested':'gpt-6.1-sol, max reasoning, Fast tier, acc2/proofswarm','served_model':'UNAVAILABLE','response_side_attestation':False},
    'referee_model_evidence':'PENDING; requested settings are not evidence'})
write_json('SOURCE_STATUS.json',status)

claims=[
 {'claim_id':'w469-C0052-CEX-001','statement':'Two independent connected paths with specified pairs of endpoints can have E I=N tending to infinity while P(I>0)=1/N tends to zero, where I counts their common vertices.','assumptions':['Independent uniform corridor labels J,K in {1,...,N}','L=N^2 common vertices in each disjoint corridor','Four distinct source endpoints; only equal labels cause intersection'],'source':'owner-own-work: INDEPENDENT.md; VERIFICATION.json','proof_or_counterexample':'I=N^2 1{J=K}; E I=N, E I^2=N^3, P(I>0)=1/N. Separate binary endpoint fans also give maximum graph degree three.','remaining_gap':'Independent referee check pending; these path laws are not asserted to be Ising current laws.','status':'proved special case'},
 {'claim_id':'w469-C0052-LIMIT-001','statement':'If centered real X_n have E X_n^2=1 and E X_n^4<=3-delta for fixed delta>0, every weak subsequential limit is centered, has variance one and fourth moment at most 3-delta, and is non-Gaussian.','assumptions':['Centered real random variables','Variance one for every n','Uniform positive fourth-moment deficit','Scalar weak subsequential convergence'],'source':'owner-own-work: INDEPENDENT.md, weak-limit lemma','proof_or_counterexample':'The fourth-moment bound gives uniform integrability of first and second moments. Truncating x^4 and then monotone convergence gives the upper bound for the limit fourth moment. Compare with fourth moment three for N(0,1).','remaining_gap':'Independent check pending; no random-distribution tightness or Ising overlap lower bound follows.','status':'sketch'},
 {'claim_id':'w469-C0052-REDUCTION-001','statement':'For a finite free-boundary zero-field ferromagnetic Ising model and weights f_x>=0, let V=E(sum f_x sigma_x)^2>0. Under Q_f(x1,...,x4)=f1 f2 f3 f4 G12 G34/V^2, E X_f^4=3-2 E_Q p, where p is connection of x1 to x3 in the original union of two currents with parity source pairs 12 and 34.','assumptions':['Finite graph, zero field, nonnegative couplings, free boundary','Nonnegative nonzero weights','Source sets are modulo two','Define p arbitrarily, e.g. zero, on zero-Q tuples with unsupported sources'],'source':{'url':'https://arxiv.org/html/2112.04248v2','locator':'(5.13); (5.9) is a different augmented law'},'proof_or_counterexample':'Sum -U4=2 G12 G34 p with the four weights; each of the three pair-products sums to V^2. Q has total mass one. Finite chain verification covers all 4^4 endpoint tuples at three couplings.','remaining_gap':'A scale-independent lower bound on E_Q p for actual critical 3D currents is unproved; connection to the source near-critical g requires cutoff and normalization control.','status':'sketch'},
 {'claim_id':'w469-C0052-LAW-001','statement':'On the three-edge Ising path 0-1-2-3 at parameter t>0, a current with sources {0,1} hits vertex 2 with probability 1-sech(t), whereas that source component after one independent sourceless augmentation hits 2 with probability tanh(t)^2. The standard two-point hitting identity cannot be used as an equality for the bare current.','assumptions':['Finite path, free boundary, zero field','Positive coupling parameter t','Current weights product t^n/n! subject to source parity'],'source':'owner-own-work: VERIFICATION.json and ATTEMPT.md; primary law attribution Aizenman (5.9)','proof_or_counterexample':'The bridge edge is even. Its conditional probability of zero is 1/cosh(t); two independent even currents both vanish with probability sech(t)^2. At t=0.1 the probabilities are 0.004979251046773414 and 0.009933709152560035.','remaining_gap':'Independent reviewer pending; no dimension-specific estimate claimed.','status':'proved special case'},
 {'claim_id':'w469-C0052-TREE-001','statement':'For finite ferromagnetic trees at zero field and free boundary, original two-source-current connection q and meeting r of the independently sourceless-augmented source components satisfy q >= (e/4) r^2. The constant is asymptotically sharp among paths.','assumptions':['Finite connected tree','Source-pair current measures exist','Four independent currents with source pairs ab,cd,empty,empty','No cyclic-graph transfer'],'source':'owner-own-work: TREE_NONLINEAR.md; derived after reading and independently checking w468 TREE_OBSTRUCTION.md','proof_or_counterexample':'If source paths meet, q=r=1. Otherwise q=product p_i and r=q(1+sum(1-p_i)); 1-p_i<=-log p_i and max_(x>=0)(1+x)e^(-x/2)=2/sqrt(e) give the bound. Paths p_i=e^(-1/m) approach equality.','remaining_gap':'w470 independent check pending; analogous inequality on the full critical Z^3 lattice is unproved.','status':'proved special case'},
 {'claim_id':'w469-C0052-SOURCE-002','statement':'The original source definition asks g(beta) not to tend to zero; it is equivalent to a nonzero limsup of -g, not by definition to an infimum over every scale and unspecified source placement of a current intersection probability.','assumptions':['g as in Duminil-Copin equations (7.1)-(7.2)','g<=0','No theorem equating unspecified pointwise and integrated criteria is assumed'],'source':{'url':'https://www.ihes.fr/~duminil/publi/2017PIMS.pdf','locator':'printed p.94, (7.1)-(7.2), Conjecture 6','quote':'If g(β) tends to 0 as β ↗ βc, the field is said to be trivial.'},'proof_or_counterexample':'Negating the limit-to-zero criterion gives epsilon and a sequence approaching beta_c. The weighted-current formula must retain the endpoint sum and chi^2 xi^3 normalization; a pointwise infimum is an additional, stronger route requiring proof.','remaining_gap':'Mathematical source correction and reviewer check pending; source text alone does not prove a 3D result.','status':'sketch'},
 {'claim_id':'w469-C0052-PEER-AUDIT-001','statement':'w468-C0052-L1 and L2 finite-path formulas are correct with the finite-tree assumptions and have no demonstrated extension to critical Z^3.','assumptions':['Exact finite-tree statements in w468 TREE_OBSTRUCTION.md as read','Graph-uniform linear comparison is the claim refuted'],'source':'~/brain_workers/w468/TREE_OBSTRUCTION.md','proof_or_counterexample':'Separate edge parity factorization and first-closed-edge derivation in REVIEW_W468.md reproduce q=p^m and r=[1+m(1-p)]p^m, and bare/augmented hit ratio (1+sech t)^(-m).','remaining_gap':'w470 is the designated referee; served-model/different-model gate unavailable.','status':'independently checked proof','verdict':'KEEP limited to finite-tree formulas; not a parent-problem solution'}]
for row in claims:
    row.update({'target':'C0052','independent_reviewer':'w470 requested; pending' if row['claim_id']!='w469-C0052-PEER-AUDIT-001' else 'w469 independent derivation; w470 referee pending','review_state':'unreviewed' if row['claim_id']!='w469-C0052-PEER-AUDIT-001' else 'scoped adversarial KEEP','recorded_utc':now})
existing={}
with (R/'CLAIMS.jsonl').open(encoding='utf-8') as stream:
    for text in stream:
        if text.strip():
            row=json.loads(text)
            existing[row['claim_id']]=row
with (R/'CLAIMS.jsonl').open('a',encoding='utf-8') as stream:
    for row in claims:
        if row['claim_id'] not in existing:
            stream.write(json.dumps(row,ensure_ascii=False)+'\n')

def entry(key,name,title,statement,assumptions,artifact):
    return {'key':key,'namespace':'probability.statmech','logical_name':name,'kind':'concept',
      'title':title,'statement':'DRAFT; independent mathematical review pending. '+statement,
      'proof_text':None,'assumptions':assumptions,'domain':'probability theory',
      'source':{'source_id':'owner-proofswarm-w469:'+key,'url':'local:brain_workers/w469/'+artifact,
                'revision':'campaign-draft-2026-10-10','license':'owner-own-work','excerpt':None}}
selected=[claims[0],claims[1],claims[2],claims[4],claims[5]]
entries=[entry('corridor','independent-connected-path-large-mean-small-intersection',
              'Large expected overlap does not force intersection',selected[0]['statement']+' In the explicit corridor construction E I=N, E I^2=N^3, P(I>0)=1/N; the graph can have maximum degree three.',selected[0]['assumptions'],'INDEPENDENT.md'),
         entry('limit','uniform-fourth-moment-deficit-nongaussian-weak-limit',
              'A fourth-moment deficit survives weak convergence',selected[1]['statement']+' Fourth-moment equality under the limit is unnecessary; second-moment uniform integrability and a truncated fourth-moment bound suffice.',selected[1]['assumptions'],'INDEPENDENT.md'),
         entry('weighted','ising-original-current-weighted-fourth-moment-criterion',
              'The original-current weighted fourth-moment criterion',selected[2]['statement']+' A uniform positive E_Q p gives a scalar fourth-moment deficit. Its 3D lower bound remains unproved.',selected[2]['assumptions'],'ATTEMPT.md'),
         entry('nonlinear','finite-tree-original-augmented-current-quadratic-comparison',
              'A quadratic current comparison on finite trees',selected[3]['statement']+' This rules out treating failure of a linear comparison as failure of every quantitative transfer; the full cyclic Z^3 case remains unproved.',selected[3]['assumptions'],'TREE_NONLINEAR.md'),
         entry('source-criterion','ising-three-dimensional-nontriviality-source-quantifiers',
              'C0052 source quantifiers and normalization',selected[4]['statement']+' For zero-field nearest-neighbor Ising on Z^3, g=sum U4(0,x2,x3,x4)/(chi^2 xi^3)<=0, with xi the exponential correlation length. The original goal is a sequence beta_n increasing to beta_c with -g(beta_n)>=epsilon>0; uniqueness or all-subsequence non-Gaussianity is not supplied by this definition.',selected[4]['assumptions'],'SOURCE_STATUS.json')]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w469','bundle_slug':'c0052-current-law-and-nongaussianity-audit-w469','entries':entries,
  'relations':[
    {'from_key':'weighted','to_key':'limit','kind':'depends_on','rationale':'The weighted criterion yields E X^4=3-2 E_Q p; the weak-limit lemma turns a uniform deficit into non-Gaussianity.'},
    {'from_key':'weighted','to_key':'corridor','kind':'cites','rationale':'The corridor example supplies E I=N but P(I>0)=1/N, showing why an expected-count lower bound alone cannot prove the required E_Q p floor.'},
    {'from_key':'nonlinear','to_key':'weighted','kind':'analogous_to','rationale':'The finite-tree q>=e*r^2/4 comparison addresses transferring an augmented meeting lower bound to original-current connection; no cyclic-lattice transfer is claimed.'},
    {'from_key':'source-criterion','to_existing_logical':'math:probability.statmech:ising-3d-nontriviality-reduces-to-current-intersection-lower-bound','kind':'cites','rationale':'Existing unverified card asserts equivalence to inf over scales L. This draft records the source nonzero-limsup criterion, exact normalization, and the missing endpoint/cutoff argument.'}]}
write_json('bundle_001.json',bundle)

keys={e['key'] for e in entries}
assert len(keys)==len(entries) and len(entries)<=200
for e in entries:
    assert e['kind']=='concept' and e['proof_text'] is None
    assert e['source']['license'].startswith('owner-own-work')
    assert 'DRAFT' in e['statement'] and e['assumptions']
for rel in bundle['relations']:
    assert rel['from_key'] in keys
    if 'to_key' in rel:
        assert rel['to_key'] in keys
    assert rel['kind'] in {'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
write_json('BUNDLE_VALIDATION.json',{'schema_checks':'PASS','entries':len(entries),'relations':len(bundle['relations']),'proof_promotion':False,'mathematical_proof_receipt':False,'integrator_run':False})

patch_dir=R/'patches'
patch_dir.mkdir(exist_ok=True)
raw=INTAKE/'brain_bundle_C001.json'
old_line=None
with raw.open(encoding='utf-8') as stream:
    for lineno,text in enumerate(stream,1):
        if 'equivalent to inf over scales' in text and 'statement' in text:
            old_line=text
            break
if old_line is None:
    raise RuntimeError('Exact original over-claim line not found; do not guess a patch')
replacement='PRIVATE REDUCTION, author-recorded; proposed mathematical correction, independent check pending. In Duminil-Copin (2017), (7.1)-(7.2), Conjecture 6, three-dimensional non-triviality means g(beta) does not tend to zero as beta increases to beta_c, equivalently limsup(-g)>0. The original two-current switching identity expresses -U4=2 G12 G34 P(original source connection); the integrated endpoint sum and normalization chi^2 xi^3 must be retained. A uniform lower bound for suitably weighted original-current connection is a sufficient route after its normalization/cutoff argument is proved. An unspecified infimum over all scales and endpoint placements is not a supplied equivalence. The two-point lower bound, exact current law, and scale-independent second-moment or nonclumping estimate remain proof obligations. Numerical cluster dimensions and added sourceless currents alone do not discharge them. No proof of C0052 is claimed.'
indent=old_line[:old_line.index('"statement"')]
comma=',' if old_line.rstrip().endswith(',') else ''
new_line=indent+'"statement": '+json.dumps(replacement,ensure_ascii=False)+comma+'\n'
live=str(raw).replace('\\','/')
patch='--- a/'+live+'\n+++ b/'+live+f'\n@@ -{lineno},1 +{lineno},1 @@\n-'+old_line+'+'+new_line
(patch_dir/'01_c0052_source_criterion.diff').write_text(patch,encoding='utf-8')
(patch_dir/'source_line_before.txt').write_text(old_line,encoding='utf-8')
(patch_dir/'source_line_after.txt').write_text(new_line,encoding='utf-8')
json.loads('{'+new_line.strip().rstrip(',')+'}')
write_json('PATCH_CHECK.json',{'target_file':live,'target_line':lineno,'expected_old_line_sha256':hashlib.sha256(old_line.encode()).hexdigest(),'before_unsupported_equivalence_count':old_line.count('equivalent to inf over scales'),'after_unsupported_equivalence_count':new_line.count('equivalent to inf over scales'),'syntax':'PASS','scope':'one proposed source statement; applying this does not update the live canonical store or certify mathematics'})

hook={'id':'current-law-w469-01','area':'math','event':'stage-start',
  'cue':'A random-current non-Gaussianity proof replaces the original two-current connection by augmented cluster meeting, or asserts a positive overlap probability from a growing expected count alone',
  'fire_when':'Finite Ising chain t=0.1: bare hit 0.004979251046773414 is replaced by augmented identity 0.009933709152560035; or E I=N is used to force P(I>0)>=c in the corridor example',
  'silent_when':'The proof states the exact original current law and proves a valid second-moment/nonclumping estimate or quantitative comparison, or labels that bound as an open input',
  'text':'Check the exact current law and bound direction. A growing expected overlap can coexist with vanishing intersection probability. Adding sourceless currents changes the hitting law; supply the comparison and a scale-independent nonclumping estimate.',
  'evidence':'~/brain_workers/w469/VERIFICATION.json; INDEPENDENT.md; memory slug proof_steps_need_derived_joint_structure_2026_09_09',
  'proposer':'w469'}
assert len(hook['text'])<=300
(R/'HOOK_PROPOSALS.jsonl').write_text(json.dumps(hook,ensure_ascii=False)+'\n',encoding='utf-8')
write_json('BUNDLE_STATE.json',{'prepared':True,'submitted':False,'reviewed':False,'ingested':False,'retrievable':False,'reviewer':'w470','source_tag':'owner-own-work','live_store_mutation':False})
files=['INDEPENDENT.md','ATTEMPT.md','TREE_NONLINEAR.md','REVIEW_W468.md','CLAIMS.jsonl','SOURCE_STATUS.json','VERIFICATION.json','TREE_VERIFICATION.json','bundle_001.json','BUNDLE_VALIDATION.json','PATCH_CHECK.json','patches/01_c0052_source_criterion.diff','HOOK_PROPOSALS.jsonl']
packet={'target':'C0052','author':'w469','referee':'w470','integration_contact':'codex-01a12190',
  'status':'REVIEW_READY_DRAFT','parent_problem_solved':False,'hardest_remaining_input':'A scale-independent original-current weighted-connection floor for the actual critical/near-critical 3D lattice, with the endpoint/cutoff normalization proved.',
  'served_model_evidence':'UNAVAILABLE; requested model settings are not evidence',
  'different_model_gate':'NOT_PASSED','required_reviews':['w469 weak-limit reduction','w469 finite-tree nonlinear comparison','C0052 source-quantifier correction'],
  'peer_scope':'w468 finite-tree formulas independently reproduced; w470 referee gate pending',
  'artifacts':[{'path':str(R/f),'sha256':hashlib.sha256((R/f).read_bytes()).hexdigest()} for f in files if (R/f).exists()]}
write_json('REVIEW_PACKET.json',packet)
print(json.dumps({'claims_added_or_present':len(claims),'draft_entries':len(entries),'relations':len(bundle['relations']),'patch_target_line':lineno,'all_theorem_promotion_disabled':True}))
