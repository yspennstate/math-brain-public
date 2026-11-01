"""Assemble review artifacts; never writes the live store or original sources."""
from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parent
INBOX=Path('~/math-brain-inbox/w559')
ORIGINAL=Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907')
HOOK=Path('~/primary_directive/hooks1000/proposals/math-w559.jsonl')
now=datetime.now(timezone.utc).isoformat()

def write_json(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        while chunk:=f.read(65536):
            h.update(chunk)
    return 'sha256:'+h.hexdigest()

def append_unique(path,rows,key):
    existing=set()
    if path.exists():
        existing={json.loads(line)[key] for line in path.read_text(encoding='utf-8').splitlines() if line.strip()}
    with path.open('a',encoding='utf-8',newline='\n') as out:
        for row in rows:
            if row[key] not in existing:
                out.write(json.dumps(row,ensure_ascii=False)+'\n')
                existing.add(row[key])

measure=json.loads((ROOT/'MEASUREMENTS.json').read_text(encoding='utf-8'))
parallel=json.loads((ROOT/'MEASUREMENTS_PARALLEL.json').read_text(encoding='utf-8'))
assert measure['status']==parallel['status']=='PASS'
store=json.loads((ROOT/'STORE_C0047_SNAPSHOT.json').read_text(encoding='utf-8'))
attempt=next(r for r in store if r['title'].startswith('Attempt on '))
target=next(r for r in store if r['title'].startswith('Open problem: '))
attempt_logical=json.loads(attempt['metadata_json'])['logical_id']
target_logical=json.loads(target['metadata_json'])['logical_id']

# Bind the adversarial verdict to the original mathematical proof, not a review.
peer=Path('~/brain_workers/w558/ATTEMPT.md')
peer_bytes=peer.read_bytes()
peer_hash='sha256:'+hashlib.sha256(peer_bytes).hexdigest()
(ROOT/'review_inputs').mkdir(exist_ok=True)
(ROOT/'review_inputs/w558_ATTEMPT.md').write_bytes(peer_bytes)
audit={
    'audit_id':'w559-C0047-w558-adversarial-001','auditor':'w559','author':'w558',
    'proof_path':str(peer),'proof_sha256':peer_hash,
    'independent_derivation_path':str(ROOT/'ATTEMPT.md'),
    'independent_derivation_sha256':digest(ROOT/'ATTEMPT.md'),
    'independent_derivation_created_utc':datetime.fromtimestamp((ROOT/'ATTEMPT.md').stat().st_ctime,timezone.utc).isoformat(),
    'first_paired_proof_read':'After ATTEMPT.md was saved; see native tool trace and STATUS.md',
    'verdict':'KEEP scoped free-product family; no general-Cayley extension',
    'checked':['Fresh horizontal factor clusters are finite for p<1 by disjoint closed finite-width cuts',
               'Exactly 2K_N-1 unused b-edges lead to distinct fresh factor lines; the incoming edge is excluded',
               'The quotient of the ordinary F_2 tree by connected a-lines is a tree, also after adding a-power edges inside lines',
               'Closed b-bridges isolate edge-disjoint infinite branch clusters for alpha_N<p<1',
               'Spanning T_4 gives edge expansion >=2; a-line intervals approach expansion 2',
               'Rayleigh lower bound N/(N+1)-N/(2L) and split-adjacency upper bound (N-1+sqrt(3))/(N+1)',
               'Strict alpha_N<1/3 for N>=2 follows by pointwise addition of +/-2 indicators, without independence of those indicators',
               'N=1 and p=0,alpha_N,1 boundary cases are treated correctly'],
    'separate_derivation':'Explore alternating a-factor and b-factor clusters. Their two-type offspring means are chi_N-1 and chi_Z-1=2p/(1-p). Disjoint free-product cosets make offspring independent. The critical product (chi_N-1)*2p/(1-p)=1 is exactly p(2chi_N-1)=1; finite nondegenerate offspring laws imply critical extinction. This independently recovers the principal critical equation.',
    'minimal_missing_premise':'A generalization needs a tree of disjoint unexplored factor cosets and finite separating bridge cuts. Nonamenability by itself does not supply either premise.',
    'counterexample_to_stronger_bridge':'The separately derived simple C_2*C_3 triangle graph has 3*rho*p_c>1.26 although p_c<p_u=1. It disproves universal satisfaction of the sufficient spectral inequality, not C0047.',
    'remaining_gap':'Required referee w560 remains pending; author/referee response-side served-model evidence and different-model gate are unverified. No parent-problem solution or store promotion.',
    'new_result_by_referee':False,'status':'proved special case','parent_problem_solved':False,
    'created_utc':now
}
write_json(ROOT/'AUDIT_W558.json',audit)
(ROOT/'AUDIT_W558.md').write_text(
    'w558 adversarial verdict: KEEP within the stated F_2 power-generator family.\n\n'
    'The principal branching step survives: each new a-line has an independent horizontal cluster K_N and exactly 2K_N-1 fresh outgoing b-edges. An independent two-type factor-cluster derivation gives (chi_N-1)*2p/(1-p)=1, equivalent to p(2chi_N-1)=1. The critical, root, and p=1 boundary cases are accounted for.\n\n'
    'The missing premise for a wider theorem is the tree of disjoint factor cosets together with finite bridge separators. The separately derived C_2*C_3 simple graph refutes universal satisfaction of d*rho*p_c<1. No counterexample was found inside w558\'s stated family; no extension to all prescribed Cayley graphs is kept.\n\n'
    f'Proof snapshot: review_inputs/w558_ATTEMPT.md, {peer_hash}. Required referee: w560; served-model/account gate unverified.\n',encoding='utf-8')

model_note=(
    'C_2 multiplicity boundary — source and model receipt\n\n'
    'The independent ATTEMPT.md fixes a simple undirected Cayley graph: the order-two generator contributes one a-edge per vertex. Its critical equation is 2p^2+2p^3-2p^4=1 and p_c=0.6372776105... .\n\n'
    'Kozakova, Critical Percolation of Free Product of Groups, arXiv:math/0611668v3, section 1.1, defines Cayley edges with the quote "with the appropriate multiplicity". Section 5 reports the modular-group polynomial 2p^5-6p^4+2p^3+4p^2-1 and threshold 0.5199... . These numbers must not be imported into the simple-graph packet.\n\n'
    'Model interpretation (an inference from the stated cyclic-factor model and polynomial): replace every a-edge by two independent parallel bonds, each open with probability p. The probability that the pair connects its endpoints is r=1-(1-p)^2=2p-p^2. The same triangle exploration has mean r*2(p+p^2-p^3)=4p^2+2p^3-6p^4+2p^5, exactly the polynomial in that source. This is a different Bernoulli bond model on a multigraph. Merging the parallel pair while preserving its original parameter p changes the threshold. Merging it with effective parameter r preserves connectivity but makes the simple graph anisotropic.\n\n'
    f'Fresh gated check: all 128 local configurations agree with that polynomial; threshold display {parallel["pc_decimal_display_only"]}; exact rational bracket 0.51<p_c<0.53. Runtime {parallel["elapsed_seconds"]}s. This supplements the simple-graph derivation and does not revise it.\n\n'
    'Primary source: https://arxiv.org/html/math/0611668v3 . Source interpretation and both infinite-graph statements require w560 review; no numerical discrepancy is called a refutation of the paper.\n'
)
(ROOT/'MODEL_CONVENTIONS.md').write_text(model_note,encoding='utf-8')

corrected=(
    'AUDIT CORRECTION (w559, 2026-10-10; independent review pending) of the 2026-09-07 C0047-A001 spectral route. '
    'For independent Bernoulli bond percolation on an infinite connected d-regular simple Cayley graph G, let rho=||A_G||/d denote the normalized simple-random-walk spectral radius. '
    'Benjamini-Schramm 1996, Theorem 4, printed p.76 (bond extension in section 2), and Juschenko-Nagnibeda 2015, Theorem 2, give the sufficient condition d*rho*p_c(G)<1 for p_c(G)<p_u(G). '
    'The original p_c<1/rho quotation omitted d and is not that criterion: it is automatic when rho<1 and p_c<=1. '
    'Nonamenability does not imply the repaired criterion for a prescribed generating set. In the simple Cayley graph C_2*C_3 with generators {a,b,b^-1}, p_c=q is the root of 2q^2+2q^3-2q^4=1 in (0.63,0.64), p_u=1, and ||A||>=2, so d*rho*p_c>1.26. '
    'This counterexample refutes only the stronger universal spectral bridge. An existence theorem for a favorable generating multiset does not establish the result for every prescribed simple generating set. '
    'The parent conjecture is not solved by this packet; current 2026 openness is UNKNOWN because a recent public full-result claim has not received a mathematical or comparator proof check here.'
)

# Patch exactly the one named statement in each source; no source file mutation.
patches=[]
inputs=[]
for name in ('brain_bundle_C004.json','brain_bundle_C004b.json'):
    path=ORIGINAL/name
    in_target=False
    located=None
    with path.open(encoding='utf-8') as f:
        for lineno,line in enumerate(f,1):
            if '"logical_name": "attempt-c0047-' in line:
                in_target=True
            if in_target and line.lstrip().startswith('"statement":'):
                located=(lineno,line.rstrip('\r\n'))
                break
    assert located is not None
    lineno,old=located
    indent=old[:len(old)-len(old.lstrip())]
    new=indent+'"statement": '+json.dumps(corrected,ensure_ascii=False)+','
    assert json.loads(old.split(': ',1)[1].rstrip(',')) in attempt['body']
    assert json.loads(new.split(': ',1)[1].rstrip(','))==corrected
    live=path.as_posix()
    patches.append(f'--- a/{live}\n+++ b/{live}\n@@ -{lineno},1 +{lineno},1 @@\n-{old}\n+{new}\n')
    inputs.append({'path':live,'sha256':digest(path),'line':lineno,'old_statement_line':old,'new_statement_line':new})
(ROOT/'patches').mkdir(exist_ok=True)
(ROOT/'patches/01_c0047_spectral_normalization.diff').write_text(''.join(patches),encoding='utf-8')
write_json(ROOT/'PATCH_INPUTS.json',inputs)
store_correction={'spec':'store-correction-proposal-v1','author':'w559','target_id':attempt['id'],
                  'target_logical_id':attempt_logical,'expected_node_digest':attempt['digest'],
                  'expected_revision_digest':json.loads(attempt['metadata_json'])['revision_digest'],
                  'old_body':attempt['body'],'proposed_statement':corrected,
                  'source_quote':'ρ(G)kp < 1','source_locator':'Benjamini-Schramm 1996 Theorem 4, printed p.76',
                  'source_url':'https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/978/978-3321-1-PB.pdf',
                  'required_action':'Integrator creates a reviewed superseding revision and preserves the historical node; never direct-write SQLite or reuse its digest.',
                  'reviewer':'w560 (pending)','submitted':False,'reviewed':False,'ingested':False,'retrievable':False}
write_json(ROOT/'STORE_CORRECTION.json',store_correction)

def own_source(slug):
    return {'source_id':'owner-own-work:'+slug,'url':'urn:owner-own-work:w559:'+slug,
            'revision':'author-checked-20261010-draft-v1','license':'owner-own-work (campaign derivation; independent review pending)','excerpt':None}

def concept(key,logical,title,statement,assumptions,source):
    return {'key':key,'namespace':'probability.percolation','logical_name':logical,'kind':'concept',
            'title':title,'statement':statement,'proof_text':None,'assumptions':assumptions,
            'domain':'probability theory','source':source}

entries=[
    concept('spectral-criterion','benjamini-schramm-sufficient-spectral-criterion-normalized-srw',
            'Benjamini-Schramm spectral criterion with explicit normalization',
            'KNOWN SUFFICIENT CRITERION; source audit pending. For independent Bernoulli bond percolation on an infinite connected d-regular simple Cayley graph G, write rho=||A_G||/d for simple random walk. If d*rho*p_c(G)<1, then p_c(G)<p_u(G). The condition is sufficient and cannot be inferred from nonamenability alone for the prescribed generators.',
            ['Infinite connected locally finite d-regular simple Cayley graph','Independent Bernoulli bond percolation','rho is the normalized simple-random-walk spectral radius'],
            {'source_id':'doi:10.1214/ECP.v1-978:theorem-4','url':store_correction['source_url'],
             'revision':'published-1996-as-read-20261010-theorem-4','license':'cc-by-3.0','excerpt':None}),
    concept('false-bridge','false-universal-nonamenability-spectral-criterion-bridge',
            'False universal spectral bridge for prescribed Cayley generators',
            'FALSE AUXILIARY CLAIM, recorded for refutation: every infinite connected nonamenable d-regular simple Cayley graph with independent Bernoulli bond percolation satisfies d*rho*p_c<1, where rho=||A||/d. This is stronger than the nonuniqueness conjecture and fails on the explicitly specified simple C_2*C_3 graph.',
            ['This entry records a false proposed bridge, not an accepted theorem','rho=||A||/d'],own_source('false-spectral-bridge')),
    concept('triangle-boundary','simple-c2-free-c3-bond-threshold-and-spectral-obstruction',
            'Simple C_2*C_3 triangle-block boundary and spectral obstruction',
            'DRAFT AUTHOR PROOF; independent review pending; no novelty claim. Let G be the simple undirected Cayley graph of <a,b | a^2=b^3=1> with the symmetric generating set {a,b,b^-1}. Each unordered a-edge appears once. In iid Bernoulli bond percolation, p_c=q, the unique root in (0,1) of 2q^2+2q^3-2q^4=1, with 0.63<q<0.64, and p_u=1. No infinite cluster exists at p<=q; for each fixed q<p<1 there are almost surely infinitely many; at p=1 there is one. The edge Cheeger constant is 1/3. For rho=||A||/3, the triangle Rayleigh bound gives 3*rho*p_c>=2q>1.26. This refutes universal satisfaction of the sufficient spectral criterion while proving this special case of nonuniqueness.',
            ['Simple undirected graph: one a-edge, not two parallel a-bonds','Independent common-p bond edges','Fixed-p almost-sure assertions','w560 independent infinite-graph proof review pending'],own_source('triangle-block-boundary')),
    concept('source-correction','c0047-a001-normalized-spectral-source-correction',
            'C0047-A001 source normalization correction',corrected,
            ['A correction to the unreviewed 2026-09-07 attempt record','Canonical historical node is preserved','No full-conjecture solution or current-openness certification'],own_source('c0047-source-correction')),
    concept('multiplicity','c2-order-two-bond-edge-multiplicity-threshold-boundary',
            'Order-two Cayley edge multiplicity changes bond thresholds',
            'DRAFT AUTHOR MODEL CHECK; independent review pending. In the simple C_2*C_3 triangle graph with one a-edge per unordered pair, the forward branching mean is 2p^2+2p^3-2p^4. Replacing every a-edge by two independent parallel Bernoulli(p) bonds changes its connection probability to 2p-p^2 and the branching mean to 4p^2+2p^3-6p^4+2p^5. Its critical equation is 2p^5-6p^4+2p^3+4p^2-1=0, with root in (0.51,0.53), rather than the simple-graph root in (0.63,0.64). These polynomials are checked by 32 and 128 exact local configurations respectively. Kozakova 2008 reports the latter polynomial with Cayley edge multiplicity; that published number must not be transplanted into the simple graph at the same p.',
            ['Independent bond model, not site percolation','Parallel bonds are distinct random variables','Published-model interpretation is identified as an inference in MODEL_CONVENTIONS.md'],own_source('order-two-multiplicity-boundary'))
]
relations=[
    {'from_key':'triangle-boundary','to_key':'false-bridge','kind':'refutes','rationale':'The triangle graph is nonamenable but 3*rho*p_c>1.26, so the stated universal inequality fails.'},
    {'from_key':'triangle-boundary','to_key':'spectral-criterion','kind':'semantic_association','rationale':'The special case has a nonuniqueness phase despite failing this sufficient criterion.'},
    {'from_key':'source-correction','to_key':'spectral-criterion','kind':'cites','rationale':'The corrected attempt records the primary theorem with its missing degree factor restored.'},
    {'from_key':'source-correction','to_existing_logical':attempt_logical,'kind':'semantic_association','rationale':'Corrects the exact normalized-SRW criterion quotation in this historical attempt; it does not refute the parent conjecture.'},
    {'from_key':'triangle-boundary','to_existing_logical':target_logical,'kind':'specializes','rationale':'The prescribed simple C_2*C_3 Cayley graph is one nonamenable group/generating-set instance of the universally quantified target.'},
    {'from_key':'multiplicity','to_key':'triangle-boundary','kind':'semantic_association','rationale':'Distinguishes the single-a-edge graph from a parallel-a-bond model on the same vertices.'}
]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w559','bundle_slug':'c0047-triangle-boundary-source-correction-w559-001','entries':entries,'relations':relations}
write_json(ROOT/'bundle_001.json',bundle)
INBOX.mkdir(exist_ok=True)
destination=INBOX/'bundle_001.json'
if not destination.exists():
    part=INBOX/'bundle_001.part'
    assert not part.exists(),'Do not overwrite an in-flight draft'
    write_json(part,bundle)
    part.rename(destination)
else:
    assert destination.read_bytes()==(ROOT/'bundle_001.json').read_bytes(),'Existing submitted draft differs; preserve it'

by_key={e['key']:e for e in entries}
external={attempt_logical:attempt,target_logical:target}
edge_rows=[]
for i,rel in enumerate(relations,1):
    other=rel.get('to_key') or rel['to_existing_logical']
    end_statement=by_key[other]['statement'] if other in by_key else external[other]['body']
    edge_rows.append({'edge_id':f'w559-C0047-edge-{i:03d}','kind':rel['kind'],
                     'from':rel['from_key'],'from_statement_quote':by_key[rel['from_key']]['statement'],
                     'to':other,'to_statement_quote':end_statement,'rationale':rel['rationale'],
                     'reviewer':'w560 (pending)','status':'DRAFT','ingested':False})
append_unique(ROOT/'RELATION_EVIDENCE.jsonl',edge_rows,'edge_id')

hooks=[
    {'id':'math-w559-01','area':'math','event':'PreToolUse',
     'cue':'bond_percolation && normalized_SRW_rho && inverse_rho_criterion && degree_factor_absent',
     'fire_when':'C0047-A001 quotes p_c<1/rho with rho defined as normalized simple random walk.',
     'silent_when':'rho is explicitly the unnormalized adjacency norm, or d*rho*p_c<1 is already checked.',
     'text':'For normalized simple-random-walk rho on a d-regular Cayley graph, the sufficient criterion is d*rho*p_c<1. Check the degree factor; nonamenability alone need not satisfy the repaired criterion.',
     'evidence':str(ROOT/'ATTEMPT.md')+' section 4; MEASUREMENTS.json: 32 exact states, corrected product>1.26', 'proposer':'w559'},
    {'id':'math-w559-02','area':'math','event':'PreToolUse',
     'cue':'bond_percolation && order_two_generator && edge_multiplicity_unspecified',
     'fire_when':'The 0.5199 C_2*C_3 threshold is copied into the simple one-a-edge graph.',
     'silent_when':'Site percolation, or the single-edge/parallel-bond convention and effective bond parameter are explicit.',
     'text':'For an order-two Cayley generator, check one undirected edge versus two parallel bonds. A parallel Bernoulli(p) pair connects with 2p-p^2; merging it at the same p changes p_c.',
     'evidence':str(ROOT/'MODEL_CONVENTIONS.md')+'; MEASUREMENTS_PARALLEL.json: 128 states and the quintic polynomial', 'proposer':'w559'}
]
assert all(len(h['text'])<=300 for h in hooks)
append_unique(ROOT/'HOOK_PROPOSALS.jsonl',hooks,'id')
append_unique(HOOK,hooks,'id')
write_json(ROOT/'HOOK_CONTROLS.json',{'proposed_only':True,'implemented':False,'controls':[
    {'hook':'math-w559-01','fire':'normalized SRW rho and degree factor omitted','silent':'adjacency norm rho or degree factor present'},
    {'hook':'math-w559-02','fire':'bond + C_2 factor + unspecified multiplicity','silent':'site or explicit single/parallel bond convention'}],
    'evidence':'Model witnesses are measured; hook firing precision has not been measured in live traffic.'})

append_unique(ROOT/'CLAIMS.jsonl',[
    {'claim_id':'w559-C0047-audit-001','exact_statement':'Within w558\'s specified F_2 power-generator family, the iid factor-line branching reduction p(2chi_N(p)-1)=1, p_u=1, and explicit spectral bounds pass the adversarial mathematical check. This KEEP has no general-Cayley scope.',
     'assumptions':['Exact family and proof snapshot named in AUDIT_W558.json','Free-product normal forms and disjoint factor edges'],
     'source':{'path':str(peer),'sha256':peer_hash},'proof_or_counterexample':audit['separate_derivation'],
     'independent_reviewer':'w559 adversary; required w560 referee pending','remaining_gap':audit['remaining_gap'],
     'status':'proved special case','verdict':'KEEP scoped family only','parent_problem_solved':False},
    {'claim_id':'w559-C0047-multiplicity-001','exact_statement':'Single-a-edge and parallel-a-bond C_2*C_3 models have different critical polynomials: 2p^2+2p^3-2p^4-1 and 2p^5-6p^4+2p^3+4p^2-1 respectively.',
     'assumptions':['Independent bonds','Parallel pair is two distinct Bernoulli(p) variables','Same triangle-block geometry'],
     'source':{'source_id':'owner-own-work:w559-order-two-multiplicity-check','path':str(ROOT/'MODEL_CONVENTIONS.md'),
               'primary_url':'https://arxiv.org/html/math/0611668v3','source_quote':'with the appropriate multiplicity'},
     'proof_or_counterexample':'A single bond connects with p; a parallel pair with 2p-p^2. Exact 32/128-state enumerations independently recover the two branching means.',
     'independent_reviewer':'w560 (pending)','remaining_gap':'Source interpretation and infinite-graph proof check pending; no published-paper refutation.',
     'status':'proved special case','parent_problem_solved':False}], 'claim_id')

status=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
status.update({'primary_statement':'For every infinite finitely generated group and every prescribed finite symmetric simple generating set, iid Bernoulli bond p_c<p_u iff the group is nonamenable; current openness UNKNOWN.',
               'primary_sources':[{'url':store_correction['source_url'],'locator':'Sections 2 and 4, Conjecture 6 and Theorem 4','read':True},
                                  {'url':'https://arxiv.org/html/1206.2183v3','locator':'Conjecture 1 and Theorems 2 and 4','read':True},
                                  {'url':'https://arxiv.org/html/math/0611668v3','locator':'Theorem 1, Cayley multiplicity convention, section 5','read':True}],
               'recent_claim':{'url':'https://raw.githubusercontent.com/openai/math/main/lean/docs/214.md',
                               'paper':'Nonuniqueness of percolation on nonamenable quasi-transitive graphs, September 24, 2026',
                               'claimed_scope':'Full bond nonuniqueness including every prescribed finite symmetric Cayley generating set',
                               'verification_status':'PUBLISHED_CLAIM_UNVERIFIED',
                               'comparator_template':'ComparatorChallenges/BenjaminiSchramm.lean contains sorry placeholders as comparison statements; not a proof receipt and not evidence against the actual solution module',
                               'solution_module':'OAI.Probability.BenjaminiSchramm.Main',
                               'theorem_names':['OAI.Percolation.BenjaminiSchramm.full_main','OAI.Percolation.BenjaminiSchramm.cayley_main','OAI.Percolation.BenjaminiSchramm.critical_laws'],
                               'permitted_axioms':['propext','Quot.sound','Classical.choice'],'enable_nanoda':False,
                               'comparator_run':False,'actual_trusted_axioms':None,'mathematical_proof_audit':False},
               'prior_scoped_checks':['Exact C0047 ranking, problem and attempt records; two draft duplicates carry the same missing-degree statement',
                                      'Named H/I attempt directories: no C0047/Benjamini-Schramm match found',
                                      'Other named intake directories: D0061 is the broader prior statement; no current-status certification',
                                      'Annotated Lean list: attempted_un, no proof receipt',
                                      'Team O board: no C0047 row; peers own distinct regular-tree/F_2 and triangle-block lanes',
                                      'Population store read-only: exact old open-problem and attempt nodes captured; no live data changed'],
               'owner_solved_retired_check':'Only the named percolation-relevant paths and records were scoped; no exhaustive owner archive audit. No novelty claim.',
               'recall':{'status':'TIMEOUT_60S','fallback_memory_slug':'perceptron_proof_open_gaps_fleet_2026_07_12','read':True},
               'submitted':True,'submitted_path':str(destination),'reviewed':False,'ingested':False,'retrievable':False,
               'submission_kind':'DRAFT concepts only; no live store integration run','updated_utc':now})
write_json(ROOT/'SOURCE_STATUS.json',status)

report=(
    'C0047: one live-source normalization correction, with a disjoint exact boundary check.\n\n'
    'The live attempt card quotes p_c<1/rho for normalized simple random walk. The cited sufficient criterion is d*rho*p_c<1. The missing degree is present in two intake source duplicates and the current population-store node. STORE_CORRECTION.json binds a proposed superseding revision to that exact node and its digest. The historical record remains available.\n\n'
    'ATTEMPT.md independently derives the simple C_2*C_3 triangle-block case before the paired proof was read: p_c is the quartic root 0.6372776105..., p_u=1, edge Cheeger constant 1/3, and d*rho*p_c>1.26. This defeats a universal spectral bridge. AUDIT_W558.json keeps the paired F_2 power-generator result within its stated family and identifies the missing disjoint-factor/bridge premise for an extension.\n\n'
    f'Measurement: python -X utf8 verify_boundary.py passed all 32 configurations and 7 rational parameters in {measure["elapsed_seconds"]}s. On this witness the old unscaled test accepts, while the corrected sufficient test rejects: 1 mistaken criterion certification before, 0 after. This measures a source-correctness check, not general recall performance.\n\n'
    f'A distinct multiplicity check, python -X utf8 verify_parallel_convention.py, passed 128 configurations in {parallel["elapsed_seconds"]}s. The parallel-a-bond variant has the published quintic root {parallel["pc_decimal_display_only"][:14]}... rather than the simple-graph quartic root. MODEL_CONVENTIONS.md labels the source-model interpretation as an inference.\n\n'
    'The inbox draft contains five concepts and six relations with both ends quoted in RELATION_EVIDENCE.jsonl. No unreviewed result is a theorem node. The two hook proposals carry measured witnesses, fire cases and silence cases; they are proposed only.\n\n'
    'Apply: the reviewer applies patches/01_c0047_spectral_normalization.diff to the two absolute live source paths named in its headers after checking PATCH_INPUTS.json hashes, then uses the canonical integrator to create the superseding store revision specified in STORE_CORRECTION.json; do not patch SQLite or promote the DRAFT without review.\n\n'
    'Risks and limits: w560\'s independent proof check and author/referee response-side served-model evidence remain pending. A September 2026 public full-result claim was found; current openness stays UNKNOWN because neither its mathematical proof nor its comparator execution was audited here. Comparator templates with sorry are not receipts and do not discredit the solution module. No parent-problem solved or novelty claim is made. Submitted, reviewed, ingested and retrievable are separate fields; ingestion/retrieval effects are unmeasured.\n\n'
    'NEXT: w560 checks the frozen infinite-graph proof and model conventions; codex-01a12190 coordinates reviewed source correction and draft ingestion with the served-model gate intact.\n'
)
(ROOT/'REPORT.md').write_text(report,encoding='utf-8')
review=(
    'C0047 review packet — w559\n\n'
    'Requested decision: KEEP or FIX the source normalization correction and independently check the C_2*C_3 block-tree proof. Required referee: w560. Independent referee for new results originated by w560: w563.\n\n'
    'Read ATTEMPT.md for the proof saved before paired-proof exposure; MEASUREMENTS.json for exact finite algebra; MODEL_CONVENTIONS.md and MEASUREMENTS_PARALLEL.json for single versus parallel bonds; AUDIT_W558.json for the bounded paired-proof verdict. File integrity hashes are in ARTIFACT_HASHES.json and are not mathematical certificates or store manifests.\n\n'
    'The decisive checks are (a) free-product normal forms make triangle contraction T_3, (b) outgoing triangle/bridge edge sets are disjoint, (c) the bounded critical process dies out, (d) off-ray branch events are independent and closed bridges isolate their infinite clusters, and (e) a triangle-supported Rayleigh quotient equals 2. For the parallel convention the link probability is 2p-p^2, not p.\n\n'
    f'Live correction target: {attempt["id"]}, digest {attempt["digest"]}. Read STORE_CORRECTION.json for the full old statement and proposed replacement. Archival textual patch covers exactly two one-line source duplicates and writes neither source on this run.\n\n'
    f'Submission: {destination}. Five concept entries; six allowed relations. No integrator run. The source correction is also found independently by w558; integration should deduplicate it while retaining both checks.\n\n'
    'Scope: a sharp special case and auxiliary-bridge obstruction, with no solution of the universally quantified target. Current openness UNKNOWN. Author system family is GPT-6; requested gpt-6.1-sol is not response-side served identity evidence. Different-model/account gates remain unverified and cannot be waived by KEEP.\n\n'
    'NEXT: obtain w560\'s artifact-bound mathematical verdict; integration separately verifies served evidence and preserves historical node provenance.\n'
)
(ROOT/'REVIEW_PACKET.md').write_text(review,encoding='utf-8')

required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
allowed_relations={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
for e in entries:
    assert required<=e.keys()
    assert e['kind']=='concept' and e['proof_text'] is None
    assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['logical_name'])
    assert e['source']['license'].lower().startswith(('owner-own-work','cc-by'))
for rel in relations:
    assert rel['kind'] in allowed_relations and rel['from_key'] in by_key
    assert rel.get('to_key') in by_key or rel.get('to_existing_logical') in external
assert len(entries)<=200
assert destination.read_bytes()==(ROOT/'bundle_001.json').read_bytes()
validation={'status':'PASS','entries':len(entries),'relations':len(relations),'all_entries_concepts':True,
            'source_patch_hunks':len(inputs),'source_mutations':0,'store_mutations':0,
            'draft_submitted':True,'formal_proof_receipt':False,'math_review_pending':True,
            'hook_proposals':len(hooks),'ingested':False,'retrievable':False,'checked_utc':now}
write_json(ROOT/'PACKET_VALIDATION.json',validation)

# These are requested review-integrity file hashes only. The integrator owns all
# bundle/store cryptographic ceremony, canonical digests, seals and manifests.
hash_paths=[ROOT/name for name in ('ATTEMPT.md','CLAIMS.jsonl','SOURCE_STATUS.json','MEASUREMENTS.json',
    'MEASUREMENTS_PARALLEL.json','MODEL_CONVENTIONS.md','AUDIT_W558.json','STORE_CORRECTION.json',
    'PATCH_INPUTS.json','REVIEW_PACKET.md','REPORT.md','bundle_001.json','RELATION_EVIDENCE.jsonl',
    'HOOK_PROPOSALS.jsonl','PACKET_VALIDATION.json')]+[ROOT/'patches/01_c0047_spectral_normalization.diff',destination]
write_json(ROOT/'ARTIFACT_HASHES.json',{'purpose':'review file integrity only; not a store manifest or proof certificate',
                                     'files':[{'path':str(p),'sha256':digest(p),'bytes':p.stat().st_size} for p in hash_paths]})
(ROOT/'STATUS.md').write_text('STATE: WORKING\nNEXT: Verify packet hashes and send final review/integration notices; then set NEEDS_REVIEW.\n\n'
    +f'{now}: Five DRAFT concepts / six supported relations submitted under the explicitly authorized w559 inbox. Exact 32/128-state checks PASS. Two source-diff hunks and one digest-bound live-card correction saved; no store/source mutation. Two measured hook proposals appended. w558 scoped adversarial KEEP saved. Required w560 proof check and served-model evidence are pending.\n',encoding='utf-8')
print(json.dumps({'packet':str(ROOT/'REVIEW_PACKET.md'),'bundle':str(destination),'validation':validation,
                  'independent_proof_sha256':digest(ROOT/'ATTEMPT.md'),'bundle_sha256':digest(destination),
                  'paired_proof_sha256':peer_hash},indent=2))
