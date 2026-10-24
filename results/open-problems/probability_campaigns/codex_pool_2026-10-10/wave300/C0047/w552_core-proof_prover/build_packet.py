from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
UTC = datetime.now(timezone.utc).isoformat()
INBOX = Path('~/math-brain-inbox/w552')


def own_source(key, filename):
    return {'source_id': 'owner-probability300-C0047-w552-v1:' + key,
            'url': (ROOT / filename).as_uri(), 'revision': 'author-draft-2026-10-10-v1',
            'license': 'owner-own-work (campaign author proof, independent review pending)',
            'excerpt': None}


def entry(key, name, title, statement, assumptions, filename):
    return {'key': key, 'namespace': 'probability.percolation', 'logical_name': name,
            'kind': 'concept', 'title': title, 'statement': statement, 'proof_text': None,
            'assumptions': assumptions, 'domain': 'probability theory: Bernoulli bond percolation',
            'source': own_source(key, filename)}


common = ['Independent Bernoulli bond percolation', 'Simple undirected graph']
entries = [
    entry('target', 'benjamini-schramm-bond-conjecture-fixed-generating-set-scope',
          'C0047: universal fixed-generating-set bond conjecture (current openness UNKNOWN)',
          'CONJECTURE, NOT PROVED HERE. For every infinite finitely generated group Gamma and every fixed finite symmetric generating set S excluding the identity, let G be its simple undirected Cayley graph. For independent Bernoulli bond percolation, p_c is the infimum of p with an infinite cluster almost surely, and p_u is the infimum of p with exactly one infinite cluster almost surely. The assertion is p_c(G)<p_u(G) if and only if Gamma is nonamenable. Existence of a favorable S does not settle the universal assertion. The amenable direction is known. October 2026 current openness is UNKNOWN in this bounded source check; no novelty claim is made.',
          common + ['Arbitrary fixed finite symmetric generating set'], 'STATEMENT.md'),
    entry('gap', 'critical-two-point-uniform-finite-volume-norm-gap',
          'Unproved universal critical operator input for C0047',
          'UNPROVED INPUT. On an infinite connected bounded-degree nonamenable Cayley graph G, define T_pc^F(x,y) as the probability of connection inside the finite connected free-boundary subgraph F at the ambient critical parameter p_c(G). The proposed input is M_c(G)=sup_F ||T_pc^F||_2<infinity, with one bound uniform in all F. Individual finite-volume finiteness is automatic and does not imply this input. This is a stronger sufficient route to p_c<p_u; equivalence to the full conjecture is not claimed.',
          common + ['Infinite connected bounded-degree Cayley graph', 'Free boundary on F'], 'ATTEMPT.md'),
    entry('russo', 'finite-volume-russo-bk-two-point-norm-bootstrap',
          'Draft author proof: finite-volume Russo/BK norm bootstrap',
          'UNREVIEWED AUTHOR PROOF, DRAFT. Let F be a finite connected free-boundary subgraph of a bounded-degree graph G and alpha=||A_G||_2. For 0<p_0<=q<=1 with alpha ||T_p0^F||_2(q-p_0)<1, the Bernoulli bond two-point kernel satisfies ||T_q^F||_2<=||T_p0^F||_2/[1-alpha ||T_p0^F||_2(q-p_0)]. Russo and BK on F with one edge deleted give entrywise T prime<=T A_F T; the nonnegative Perron vector gives m prime<=alpha m squared. No cluster-exploration independence or Loewner domination is asserted.',
          common + ['Finite connected free-boundary F', '0<p_0<=q<=1', 'Strict denominator positivity'], 'ATTEMPT.md'),
    entry('conditional', 'critical-two-point-norm-explicit-nonuniqueness-margin',
          'Draft conditional reduction: explicit positive nonuniqueness margin',
          'UNREVIEWED AUTHOR PROOF, CONDITIONAL. Let G be an infinite connected bounded-degree Cayley graph with 0<p_c<1. Assume the uniform bound sup_F ||T_pc^F||_2<=M<infinity, where F is finite connected with free boundary, and let alpha=||A_G||_2. Then p_u>=p_c+eta>p_c, with eta=min{(1-p_c)/2,1/(2 alpha M)}. The bootstrap bounds the full T_q by 2M throughout this interval. Almost-sure uniqueness would force T_q(x,y)>=theta(q)^2, contradicting quadratic forms on n vertices. The uniform critical input remains unproved in general.',
          common + ['Infinite connected bounded-degree Cayley graph', '0<p_c<1', 'UNPROVED IN GENERAL: uniform critical norm M<infinity'], 'ATTEMPT.md'),
    entry('nb', 'nonbacktracking-resolvent-sufficient-two-point-operator-bound',
          'Draft author proof: nonbacktracking operator criterion',
          'UNREVIEWED AUTHOR PROOF, DRAFT; novelty not asserted. Let G be an infinite connected simple d-regular graph, d>=3, b=d-1 and alpha=||A||_2. Put beta=sqrt(b) if alpha<=2sqrt(b), and beta=(alpha+sqrt(alpha squared-4b))/2 otherwise. For Bernoulli bond percolation and 0<=p<1/beta, ||T_p||_2<=(1-p squared)/(1+b p squared-alpha p). Nonbacktracking walk matrices have B_2=A squared-dI and B_n=A B_n-1-b B_n-2 for n>=3. Their norm-convergent series is (1-p squared)(I-pA+b p squared I) inverse. For Cayley graphs, p_c beta<1 is sufficient for a critical uniform norm bound, but is not derived from nonamenability alone.',
          common + ['Infinite connected d-regular graph, d>=3', 'Strict p beta<1'], 'NONBACKTRACKING_LEMMA.md'),
    entry('tree', 'regular-tree-critical-two-point-operator-norm-calibration',
          'Draft author proof: regular-tree critical two-point norm',
          'UNREVIEWED AUTHOR PROOF OF A KNOWN SPECIAL CASE. On the infinite d-regular tree, d>=3 and b=d-1, Bernoulli bond percolation has p_c=1/b, ||A||_2=2sqrt(b), and ||T_pc||_2=(1-b to the power -2)/(1-b to the power -1/2) squared<infinity. Tree simple paths make the nonbacktracking series exact. The coarse condition p_c||A||<1 holds only for d>=6, while the nonbacktracking sufficient condition p_c sqrt(b)<1 holds for all d>=3. This is an analytic infinite-family statement; finite checks only evaluate its constants.',
          common + ['Infinite d-regular tree, d>=3'], 'NONBACKTRACKING_LEMMA.md'),
    entry('normalization', 'percolation-spectral-radius-normalization-c0047-attempt-correction',
          'Draft correction: normalize the spectral input in C0047-A001',
          'DRAFT AUTHOR CORRECTION, independent review pending. If rho=||A/d||_2 is the simple-random-walk radius on a nonamenable d-regular Cayley graph, then 0<rho<1 and p_c<=1, so p_c<1/rho is automatic. It cannot be the difficult input of the elementary path/operator route. That route uses alpha=||A||_2=d rho and the SUFFICIENT condition p_c d rho<1. This sufficient condition is not necessary: on the 3-regular tree p_c alpha=sqrt(2)>1 but the critical two-point norm is finite. The correction diagnoses the normalization ambiguity in C0047-A001, not a counterexample to C0047.',
          common + ['Nonamenable d-regular Cayley graph', 'rho=||A/d||_2; Kesten characterization rho<1'], 'PRIOR_DIGEST.md'),
]
relations = [
    {'from_key':'gap','to_key':'target','kind':'cites','rationale':'The unproved uniform critical norm is a sufficient route to the stated universal bond conjecture; it is not the target itself.'},
    {'from_key':'conditional','to_key':'russo','kind':'depends_on','rationale':'The explicit eta uses the displayed finite-volume norm bootstrap with alpha and M.'},
    {'from_key':'conditional','to_key':'gap','kind':'depends_on','rationale':'The conditional reduction explicitly assumes the exact uniform bound whose universal proof is still missing.'},
    {'from_key':'nb','to_key':'gap','kind':'semantic_association','rationale':'The strict extra condition p_c beta<1 yields a finite critical norm but is not supplied by nonamenability alone.'},
    {'from_key':'tree','to_key':'nb','kind':'specializes','rationale':'On a regular tree alpha=2sqrt(d-1), beta=sqrt(d-1), and the nonbacktracking path bound is exact.'},
    {'from_key':'normalization','to_existing_logical':'math:probability.statmech:attempt-c0047-benjamini-schramm-conjecture-p-c-p-u-if-and-only-if-the-group-is-non-a','kind':'cites','rationale':'C0047-A001 uses normalized simple-random-walk rho in its tentative reciprocal-radius criterion; the draft correction specifies the missing degree factor without deleting the historical attempt.'},
]
bundle = {'spec':'mathbrain-draft-v1','author_agent':'w552',
          'bundle_slug':'c0047-critical-operator-proof-gap-and-spectral-correction-v1',
          'entries':entries,'relations':relations}
serialized = json.dumps(bundle,ensure_ascii=False,indent=2) + '\n'
(ROOT/'brain_draft').mkdir(exist_ok=True)
(ROOT/'brain_draft'/'bundle_001.json').write_text(serialized,encoding='utf-8')
INBOX.mkdir(exist_ok=True)
part = INBOX/'bundle_001.json.part'
part.write_text(serialized,encoding='utf-8')
part.rename(INBOX/'bundle_001.json')

status_path = ROOT/'SOURCE_STATUS.json'
status = json.loads(status_path.read_text(encoding='utf-8'))
status['intake_primary'] = {'source_id':'duminil_copin_icm_2018','url':'https://arxiv.org/pdf/1712.04651',
                            'revision':'1712.04651v1','location':'Conjecture 2, printed p.4',
                            'source_record_pdf_sha256':'d46fd63bd798736d1a463aade6e4c04f365da2e45d05d956a1812ec9c55950f2',
                            'hash_status':'prior intake metadata, not independently rehashed by w552'}
status['prior_attempt_check'] = 'Exact C0047 and C0047-A001 rows preserved in PRIOR_RECORDS.json; bounded H/I and Lean searches found no proof theorem.'
status['owner_solved_retired_check'] = 'Named percolation project README explicitly unfinished; June proof_strategy has an unproved global escape bridge. Its solved-register note excludes percolation from that local solved register. Bounded check, not exhaustive October clearance.'
status['adjacent_recent_paper'] = {'url':'https://arxiv.org/pdf/2609.07768', 'revision':'2609.07768v1',
                                 'finding':'Introduction Remark 1.5 discussion concerns pc<1, BS96 Question 2, not the pc<pu conjecture.'}
status['promotion'] = {'prepared':True,'submitted':True,'reviewed':False,'ingested':False,'retrievable':False,
                       'submission_meaning':'Complete concept-only DRAFT staged in the explicitly authorized inbox; mathematical/model gates pending.'}
status['statement_first_delivery'] = {'to':'w553','message_id':'msg-76ee3bde2c','method':'direct mesh after team_comm team routing failed'}
status_path.write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

hook = {'id':'spectral-normalization-w552-01','area':'math','event':'stage-start',
        'cue':r'(?i)\b(?:p_c|pc)\s*<\s*1\s*/\s*(?:rho|ρ)',
        'fire_when':'C0047-A001 proposes pc<1/rho where rho is the spectral radius of simple random walk.',
        'silent_when':'An explicit sufficient condition pc*d*rho<1 uses rho=||A/d||, with the universal proof gap preserved.',
        'text':'Before using a reciprocal spectral-radius criterion in percolation, fix the normalization: rho=||A/d|| and alpha=d*rho. On a nonamenable Cayley graph pc<1/rho is automatic. The elementary path bound instead needs pc*alpha<1, a sufficient extra input.',
        'evidence':'~/brain_workers/w552/CLAIMS.jsonl w552-C0047-CORR1; PRIOR_RECORDS.json C0047-A001; VALIDATION.json tree comparison 5/8 to 8/8',
        'proposer':'w552'}
assert len(hook['text']) <= 300
assert re.search(hook['cue'],hook['fire_when']) and not re.search(hook['cue'],hook['silent_when'])
hook_text = json.dumps(hook,ensure_ascii=False)+'\n'
(ROOT/'HOOK_PROPOSAL.jsonl').write_text(hook_text,encoding='utf-8')
hook_path = Path('~/primary_directive/hooks1000/proposals/math-w552.jsonl')
existing = hook_path.read_text(encoding='utf-8') if hook_path.exists() else ''
if hook['id'] not in existing:
    with hook_path.open('a',encoding='utf-8') as handle:
        handle.write(hook_text)
(ROOT/'HOOK_CONTROLS.json').write_text(json.dumps({'fire':True,'silent':True,'hook_id':hook['id'],
         'measurement':'Python re.search on the two explicit controls; a proposal, not an installed hook'},indent=2),encoding='utf-8')

files = ['STATEMENT.md','ATTEMPT.md','NONBACKTRACKING_LEMMA.md','CLAIMS.jsonl','SOURCE_STATUS.json',
         'PRIOR_DIGEST.md','PRIOR_RECORDS.json','validate.py','VALIDATION.json','COMPUTE_GATE.json',
         'REPORT.md','REVIEW.md','brain_draft/bundle_001.json','HOOK_PROPOSAL.jsonl','HOOK_CONTROLS.json']
hashes = [{'path':str(ROOT/f),'sha256':hashlib.sha256((ROOT/f).read_bytes()).hexdigest()} for f in files]
packet = {'packet_id':'w552-C0047-critical-operator-v1','created_utc':UTC,'author':'w552',
          'adversary':'w553','referee':'w554','independent_referee_for_referee_new_results':'w557',
          'target':'C0047','target_solved':False,'current_openness':'UNKNOWN','claim_ids':[
              json.loads(line)['claim_id'] for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()],
          'review_state':'PENDING','scoped_keep_candidates':['L1','L2','L3 conditional only','L4 with strict input','TREE special case','CORR1 normalization'],
          'single_hardest_remaining_gap':status['single_hardest_gap'],
          'served_model_evidence':status['served_model_evidence'],
          'validation':{'path':str(ROOT/'VALIDATION.json'),'status':'PASS','formal_certificate':False,
                        'infinite_uniform_bound_certificate':False},
          'brain_state':status['promotion'],'inbox_draft':str(INBOX/'bundle_001.json'),
          'inbox_sha256':hashlib.sha256((INBOX/'bundle_001.json').read_bytes()).hexdigest(),
          'file_hashes':hashes,'hash_warning':'Byte integrity only; not a mathematical proof or served-model attestation.',
          'NEXT':'w554 independently check the six scoped mathematical claims; preserve the unproved universal input and model gates.'}
(ROOT/'REVIEW_PACKET.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'packet':str(ROOT/'REVIEW_PACKET.json'),'draft':str(INBOX/'bundle_001.json'),
                  'entries':len(entries),'relations':len(relations),'claims':len(packet['claim_ids']),
                  'concept_only':all(e['kind']=='concept' for e in entries),'reviewed':False,
                  'ingested':False,'hook':str(hook_path)}))
