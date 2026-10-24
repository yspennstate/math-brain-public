"""Stage DRAFT concepts, exact edge evidence and patches; never integrates."""
from pathlib import Path
import difflib
import hashlib
import json
import shutil

root=Path(__file__).resolve().parent
draft_dir=root/'drafts'
patch_dir=root/'patches'
evidence_dir=root/'evidence'
for directory in (draft_dir,patch_dir,evidence_dir):
    directory.mkdir(exist_ok=True)
nodes=json.loads((root/'brain_C0048_nodes.json').read_text(encoding='utf-8'))
parent=None
for node in nodes:
    meta=json.loads(node['metadata_json'])
    if 'open-problem-c0048' in str(meta.get('logical_id','')):
        parent=(node,meta['logical_id'])
        break

entries=[]
def add(key,logical,title,statement,assumptions,artifact):
    entry={'key':key,'namespace':'probability.potts','logical_name':logical,
      'kind':'concept','title':title,
      'statement':'DRAFT; independent referee check pending. '+statement,
      'proof_text':None,'assumptions':assumptions,'domain':'probability theory; Potts and random-cluster models',
      'source':{'source_id':'owner-probability-campaign-w466:C0048:'+key,
        'url':None,'revision':'author-derived-2026-10-10',
        'license':'owner-own-work','excerpt':None}}
    entries.append(entry)
    return entry

soft=add('softplus','uniform-pressure-error-does-not-force-a-first-order-jump',
  'Uniform pressure approximation does not preserve a derivative jump',
  'For every epsilon>0, P(x)=max(0,x) and Q_epsilon(x)=epsilon*log(1+exp(x/epsilon)), x in R, satisfy 0<Q_epsilon(x)-P(x)<=epsilon*log(2) uniformly. Q_epsilon is smooth and convex, with derivative 1/(1+exp(-x/epsilon)); hence arbitrarily small uniform convex-pressure approximation alone cannot force a derivative discontinuity. This functional counterexample does not disprove the nearest-neighbor Potts discontinuity conjecture, whose source target is positive critical magnetization.',
  ['epsilon>0','x is real','Comparison concerns uniform pressure error only'], 'ATTEMPT.md')
barrier=add('barrier','three-state-three-dimensional-mean-field-error-does-not-exclude-saddle',
  'The direct mean-field allowance does not exclude the q=3,d=3 saddle',
  'Let F_J(x)=sum_i x_i*log(x_i)-(J/2)*sum_i x_i^2 on three-component probability vectors, J=4*log(2), u=(1/3,1/3,1/3), o=(2/3,1/6,1/6), s=(1/2,1/4,1/4). Then F_J(u)=F_J(o) and F_J(s)-F_J(u)=log(3)-(19/12)*log(2)>0. In the Biskup-Chayes extreme-state comparison, the allowed excess is J*(q-1)^2*I_d/(2*q), where I_d is the uniform integral of X^2/(1-X), X=(1/d)*sum_j cos(k_j). For d>=3, symmetry yields I_d>=1/(2*d). At q=3,d=3 this allowance is at least (4/9)*log(2), larger than the saddle excess, so this inequality alone does not exclude s. An upper error allowance exceeding this gap is not a lower bound on actual error and proves neither continuity nor impossibility of sharper methods. The comparison concerns extreme thermodynamic support pairs, not arbitrary Gibbs mixtures.',
  ['q=3,d=3,J=4*log(2) for the numerical comparison','Standard color normalization J=2*d*K',
   'The cited mean-field inequality must apply to the selected extreme thermodynamic state'], 'quantitative_obstruction.md')
path=add('path','positive-finite-boundary-fk-gaps-can-vanish-in-the-volume-limit',
  'Positive finite FK boundary gaps can vanish exponentially',
  'On a path of N>=3 edges with 0<p<1,q>1, compare free random-cluster boundary conditions with the boundary partition identifying the two endpoints. Put a=p/(p+q*(1-p)). The free law is iid Bernoulli(a). The endpoint-wired law is the free law tilted by 1+(q-1)*1{all N edges open}. Its open-edge marginal gap is rho_N=(q-1)*(1-a)*a^N/(1+(q-1)*a^N)>0, but rho_N tends to zero as N grows. Thus positive finite-volume boundary gaps alone do not establish a positive limiting witness. This path example does not disprove a claim for Z^d with d>=3.',
  ['N>=3','0<p<1','q>1','The only wiring identifies the path endpoints'], 'PEER_AUDIT.md')
witness=add('witness','fixed-cylinder-witness-controls-ordered-edge-marginal-gaps',
  'A fixed cylinder witness controls ordered edge marginal gaps',
  "Let mu_0,mu_1 on {0,1}^E admit a monotone coupling X<=Y. For every finite F subset E and event A measurable on F, |mu_1(A)-mu_0(A)|<=sum_{e in F}(mu_1(omega_e)-mu_0(omega_e)). If the marginal difference is the same rho on every edge and |F|=M>=1, a fixed gap delta>0 implies rho>=delta/M. This uses a union bound on coordinate disagreements, with no independence assumption. Applying it in a volume limit requires fixed support and a gap bounded below uniformly in volume; growing M or vanishing delta can give a zero lower bound. For Potts discontinuity this does not construct the positive critical witness or identify pressure non-differentiability with the source's critical-magnetization target.",
  ['A coordinatewise monotone coupling exists','F is finite and A depends only on F',
   'A common marginal gap rho is needed for the delta/M conclusion'], 'PEER_AUDIT.md')

relations=[
 {'from_key':'path','to_key':'witness','kind':'semantic_association',
  'rationale':'The path example directly tests the volume-uniform positive-gap premise needed to instantiate the fixed-cylinder witness bound; it does not refute that conditional bound.'},
 {'from_key':'softplus','to_key':'barrier','kind':'semantic_association',
  'rationale':'Both warn about transferring a phase jump through an approximation. The softplus example concerns uniform pressure error; the saddle calculation checks the stronger cited state-dependent mean-field allowance. Neither implies the other.'}
]
if parent:
    for key in ('path','barrier','witness'):
        relations.append({'from_key':key,'to_existing_logical':parent[1],
          'kind':'semantic_association',
          'rationale':'Records an exact limitation or missing premise for this C0048 route; does not prove or disprove the parent conjecture.'})
bundle={'spec':'mathbrain-draft-v1','author_agent':'w466',
        'bundle_slug':'c0048-obstructions-w466-001','entries':entries,'relations':relations}
bundle_text=json.dumps(bundle,ensure_ascii=False,indent=2)+'\n'
part=draft_dir/'bundle_001.part'
part.write_text(bundle_text,encoding='utf-8')
part.replace(draft_dir/'bundle_001.json')

bykey={entry['key']:entry for entry in entries}
edge_rows=[]
for i,relation in enumerate(relations,1):
    left=bykey[relation['from_key']]
    right=bykey[relation['to_key']]['statement'] if 'to_key' in relation else parent[0]['body']
    edge_rows.append({'id':f'w466-edge-{i:03d}','relation':relation,
       'from_statement_quote':left['statement'],'to_statement_quote':right,
       'status':'draft','independent_reviewer':'w467 pending',
       'remaining_gap':'Review and ingestion; these edges do not certify C0048.'})
(root/'EDGE_EVIDENCE.jsonl').write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in edge_rows),encoding='utf-8')

hook={'id':'c0048-scope-w466-01','area':'math','event':'stage-start',
 'cue':'A Potts phase-transition proof uses a recalled mean-field or spin-glass card',
 'fire_when':'A q=3,d=3 nearest-neighbor ferromagnet proof transfers a high-temperature spin-glass result or a mean-field jump without checking graph, boundary state, error allowance, and critical onset.',
 'silent_when':'The graph/model match, the temperature and state hypotheses are verified, and a fixed positive critical witness or another complete critical-percolation proof is already established.',
 'text':'Before transferring a Potts result, check graph, interaction, temperature, boundary state and observable. A small mean-field error or positive finite-box gap alone does not prove positive critical magnetization; name the uniform critical witness still missing.',
 'evidence':'w466/measurement_retrieval.json; w466/quantitative_obstruction.md; w466/PEER_AUDIT.md; scar perceptron_proof_open_gaps_fleet_2026_07_12',
 'proposer':'w466'}
assert len(hook['text'])<=300
hook_text=json.dumps(hook,ensure_ascii=False)+'\n'
(draft_dir/'math-w466.jsonl').write_text(hook_text,encoding='utf-8')

for name,text_,target in (
 ('01_C0048_draft_bundle.diff',bundle_text,'~/math-brain-inbox/w466/bundle_001.json'),
 ('02_C0048_scope_hook.diff',hook_text,'~/primary_directive/hooks1000/proposals/math-w466.jsonl')):
    patch=''.join(difflib.unified_diff([],text_.splitlines(keepends=True),
                  fromfile='a/'+target,tofile='b/'+target))
    (patch_dir/name).write_text(patch,encoding='utf-8')

# Snapshot the reviewed proof so later peer edits do not change the audit target.
peer=Path('~/brain_workers/w465/ATTEMPT.md')
shutil.copyfile(peer,evidence_dir/'w465_ATTEMPT_review_target.md')
receipt={'reviewed_path':str(peer),'snapshot_path':str(evidence_dir/'w465_ATTEMPT_review_target.md'),
 'sha256':hashlib.sha256((evidence_dir/'w465_ATTEMPT_review_target.md').read_bytes()).hexdigest(),
 'math_verdict':'KEEP L1-L3 as conditional lemmas; no parent proof',
 'author':'w465','auditor':'w466','referee':'w467 pending',
 'served_model_evidence_author':None,'served_model_evidence_auditor':None,
 'served_model_evidence_referee':None,
 'served_model_note':'No response-side served-model identity evidence is exposed here. Requested settings and turn_context are not proof of served identity.',
 'different_model_review_gate':'pending','formal_check':None}
(root/'PEER_REVIEW_RECEIPT.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
states={'bundle':'drafts/bundle_001.json','staged':True,'submitted':False,
 'reviewed':False,'ingested':False,'retrievable':False,
 'reason':'Worker mutations restricted to w466; independent referee and different-model gates pending. No integrator was run.',
 'routing_contact':'codex-01a12190','mathematical_referee':'w467',
 'referee_own_new_results_check':'w470'}
(root/'BUNDLE_LIFECYCLE.json').write_text(json.dumps(states,indent=2),encoding='utf-8')
print(json.dumps({'draft_concepts':len(entries),'exact_edge_rows':len(edge_rows),
 'existing_C0048_logical':parent[1] if parent else None,'hook_characters':len(hook['text']),
 'lifecycle':states},indent=2))
