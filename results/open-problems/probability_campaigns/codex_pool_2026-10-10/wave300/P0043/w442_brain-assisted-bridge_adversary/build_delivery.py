"""Prepare local diffs and concept-only mathematical drafts for review."""
import difflib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
claims = [json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line]
claims[0]['remaining_gap'] = 'Exact restricted target recovered; only the referee check is pending. This refutes the unqualified formulation, not the p_c<1 conjecture.'
(ROOT/'CLAIMS.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False)+'\n' for row in claims), encoding='utf-8')

def entry(key, name, title, statement, assumptions, kind='concept'):
    return {'key':key, 'namespace':'probability.percolation.audit', 'logical_name':name,
            'kind':kind, 'title':title, 'statement':statement, 'proof_text':None,
            'assumptions':assumptions, 'domain':'Bernoulli bond percolation / proof auditing',
            'source':{'source_id':'owner:P0043:w442:'+key,
                      'url':'~/brain_workers/w442/ATTEMPT.md',
                      'revision':'draft-pending-independent-referee-2026-10-10',
                      'license':'owner-own-work', 'excerpt':None}}

entries = [
 entry('rooted-expansion','rooted-edge-expansion-notation-w442', 'Rooted asymptotic edge expansion',
       'For an infinite connected locally finite graph H rooted at o, define iota_*(H,o)=liminf_{n->infinity} inf{ |boundary_H(S)|/|S| : S is a finite connected vertex set containing o and |S|>=n }. The boundary counts H-edges having exactly one endpoint in S.',
       ['H infinite, connected and locally finite','o a vertex of H'], 'definition'),
 entry('endpoint','infinite-path-critical-endpoint-obstruction-draft-w442', 'Critical endpoint obstruction on the infinite path (draft)',
       'Draft deduction awaiting referee w443: '+claims[0]['statement'], claims[0]['assumptions']),
 entry('continuity-countermodel','finite-radius-continuity-quantifier-countermodel-draft-w442', 'Finite continuity does not give one common lower parameter (draft)',
       'Draft deduction awaiting referee w443: '+claims[1]['statement'], claims[1]['assumptions']),
 entry('subexponential-obstruction','subexponential-subgraph-anchored-expansion-obstruction-draft-w442', 'Subexponential ambient growth forbids positive anchored expansion (draft)',
       'Draft deduction awaiting referee w443: '+claims[2]['statement']+' Here iota_*(H,o) is the liminf, as n tends to infinity, of the infimum of |boundary_H(S)|/|S| over finite connected H-vertex sets S containing o with |S|>=n; boundary_H counts H-edges with exactly one endpoint in S.', claims[2]['assumptions']),
 entry('finite-continuity-route','finite-continuity-uniform-parameter-route-audit-w442', 'Refuted generic finite-continuity inference',
       'Audited candidate inference, false for abstract arrays: if f_n:[0,1]->[0,1] is continuous and increasing in its parameter, decreasing with n, and inf_n f_n(a)>0 for a in (0,1), then some q<a has inf_n f_n(q)>0. The failure is the exchange of for-every-scale/there-exists-parameter with there-exists-parameter/for-every-scale. This is not asserted as a valid theorem.',
       ['abstract arrays of functions','no graph-specific premise added']),
 entry('anchored-route','positive-anchored-expansion-critical-cluster-route-audit-w442', 'Impossible anchored-expansion premise on subexponential graphs',
       'Audited proposed bridge: a hypothetical infinite Bernoulli critical cluster H inside a bounded-degree graph G of subexponential volume growth has positive anchored edge expansion. This proposed premise is impossible: for any infinite connected subgraph H containing o, iota_*(H,o)=0 when limsup_r |B_G(o,r)|^(1/r)=1. Its failure obstructs that sufficient-condition route; it does not prove the critical cluster finite.',
       ['bounded-degree subexponential ambient graph','a hypothetical infinite connected subgraph']),
 entry('exploration-gap','finite-exploration-domination-criticality-bridge-gap-w442', 'Finite exploration domination leaves a uniform-history bridge',
       'A retrieved unverified concept card for arXiv:2304.12110 describes finite-edge stochastic domination from a conditional next-edge probability bound holding after every positive-probability exploration history. A marginal probability bound is weaker. To apply such a finite comparison in an infinite critical-cluster argument, one must supply the precise exploration, every-history bound, a percolating comparison object, and the limit argument. These are missing premises, not consequences of the stored paper title or an empty structured conditions list. Primary lemma transcription and applicability are still under review.',
       ['this is an audit of a retrieved concept card, not a promotion to theorem','finite exploration histories must be specified'])
]
relations = [
 {'from_key':'subexponential-obstruction','to_key':'rooted-expansion','kind':'depends_on','rationale':'The obstruction uses exactly the rooted edge-boundary constant defined at the target end.'},
 {'from_key':'subexponential-obstruction','to_key':'anchored-route','kind':'refutes','rationale':'The source end gives iota_*=0 for every infinite connected subgraph in this graph class; the candidate premise requires iota_*>0 in the same class.'},
 {'from_key':'continuity-countermodel','to_key':'finite-continuity-route','kind':'refutes','rationale':'The source end has inf_n f_n(a)=1 and inf_n f_n(q)=0 for every q<a, satisfying the candidate hypotheses and contradicting its conclusion.'},
 {'from_key':'exploration-gap','to_existing_logical':'math:harvest.arxiv.owner-math:arxiv-2304-12110-lemma-7-72467d','kind':'cites','rationale':'The existing end requires the lower conditional edge probability after every eligible positive-probability exploration history; the audit end identifies those hypotheses as a missing bridge. The existing card is unverified concept material.'}
]
bundle = {'spec':'mathbrain-draft-v1','author_agent':'w442','bundle_slug':'probability-percolation-p0043-adversary-w442-001','entries':entries,'relations':relations}
(ROOT/'DRAFT_BUNDLE.json').write_text(json.dumps(bundle, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

by_key = {row['key']:row for row in entries}
card = json.loads((ROOT/'BRIDGE_CARD.json').read_text(encoding='utf-8'))['hits'][0]
edges = []
for relation in relations:
    target = by_key[relation['to_key']]['statement'] if 'to_key' in relation else card['body']
    edges.append({**relation,'from_quote':by_key[relation['from_key']]['statement'],'to_quote':target,
                  'status':'draft','independent_reviewer':'w443 (pending)'})
(ROOT/'EDGES.jsonl').write_text(''.join(json.dumps(row, ensure_ascii=False)+'\n' for row in edges), encoding='utf-8')

hook = {'id':'p0043-w442-01','area':'math','event':'stage-start',
        'cue':'proof proposes positive anchored expansion for an infinite critical cluster in a bounded-degree subexponential ambient graph',
        'fire_when':'a P0043 route on Z^3 asserts positive anchored expansion in order to survive independent thinning',
        'silent_when':'positive expansion is an explicit conditional premise on an exponential-growth graph, without a transfer to subexponential graphs',
        'text':'Positive anchored expansion forces exponential ball growth in bounded degree. Every infinite connected subgraph of a subexponential ambient graph has anchored expansion zero. Check this before using thinning as a criticality bridge.',
        'evidence':'~/brain_workers/w442/CLAIMS.jsonl w442-C003; ATTEMPT.md independent ball-growth derivation; referee pending',
        'proposer':'w442'}
(ROOT/'hook_proposal.jsonl').write_text(json.dumps(hook)+'\n', encoding='utf-8')
patch_dir = ROOT/'patches'
patch_dir.mkdir(exist_ok=True)
for name, local, live in [
 ('01_math_source_fallback.diff','math_source_fallback.py','.claude/dreaming/math_source_fallback.py'),
 ('02_anchored_expansion_hook.diff','hook_proposal.jsonl','primary_directive/hooks1000/proposals/math-w442.jsonl')]:
    text = (ROOT/local).read_text(encoding='utf-8').splitlines(keepends=True)
    patch = ''.join(difflib.unified_diff([],text,fromfile='a/'+live,tofile='b/'+live))
    (patch_dir/name).write_text(patch, encoding='utf-8')
(ROOT/'patch_check').mkdir(exist_ok=True)

source = json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source['primary_sources'][1].update(
    checked='Scope note, comparator, comparator JSON and actual Main.lean theorem inspected. Main theorem has the intended graph hypotheses. Dependencies and trusted axioms were not kernel-checked.',
    solution_module='OAI.Probability.CriticalPercolation.Main',
    theorem_name='OAI.CriticalPercolation.BondGraph.no_percolation_at_criticality',
    permitted_axioms_in_comparator=['propext','Quot.sound','Classical.choice'],
    actual_axiom_receipt=False,
    note='The comparator statement has sorry by design; this does not establish a defect in the separate actual solution.')
source['primary_sources'].append({'url':'https://github.com/openai/math/blob/main/preprints/No-percolation-at-criticality-on-quasi-transitive-graphs-September-24-2026/paper.pdf',
    'locator':'Theorem 1.1, page 2','checked':'downloaded exact target statement; 42-page proof not certified',
    'local_file':'sources/quasi_transitive_claim.pdf','status':'claimed resolution requiring verification','mathematical_proof_receipt':False})
source['owner_solved_retired_check']='Read the relevant C0084 prior attempt and targeted percolation references in the named owner folder. No owner full-proof/retirement receipt for P0043 was recovered; no exhaustive exclusion is claimed.'
source['next']='Referee checks C003 and the paired bridge packet; no repeated open-status search is needed for this deliverable.'
(ROOT/'SOURCE_STATUS.json').write_text(json.dumps(source,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'prepared_entries':len(entries),'draft_relations':len(relations),'patches':2,'submitted':False}))
