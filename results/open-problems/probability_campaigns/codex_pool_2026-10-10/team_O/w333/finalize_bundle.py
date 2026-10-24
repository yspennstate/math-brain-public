import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
path=ROOT/'bundles/bundle_001.json'
bundle=json.loads(path.read_text(encoding='utf-8'))
cards=json.loads((ROOT/'evidence/store_cards.json').read_text(encoding='utf-8'))
edges=[json.loads(line) for line in (ROOT/'edges.jsonl').read_text(encoding='utf-8').splitlines()]
for entry in bundle['entries']:
    entry['namespace']='probability.openproblems'
    if entry['key']=='rotation-strong-convergence-reduction':
        entry['statement']=entry['statement'].split(' Combining it')[0]+' The cached Fang--Jiang--Lin--Xu paper, arXiv:1210.4771v1, Theorem 12.2, identifies the Brown measure of u+v in this canonical tracial representation as Haar measure on the unit circle. Every finite sum U_j+V_j has empirical eigenvalue measure delta_0. This gives a candidate counterexample to the implication from arbitrary strong convergence to Brown-measure convergence, pending independent review and with no novelty claim. It does not address independent Ginibre ensembles or a free limiting family.'
        entry['proof_text']=entry['proof_text'].split(' The Brown-measure assertion')[0]+' The cached paper uses the canonical irrational-rotation pair in its tracial GNS von Neumann algebra, and Theorem 12.2 includes the coefficient lambda=1. Its established Brown measure is Haar on the unit circle, different from the finite delta_0 measures. The full construction therefore has no remaining unidentified source dependency in this local check; it still requires an independent full proof audit.'
    if entry['key']=='poisson-extinction-duality-rate-identity':
        entry['proof_text']=entry['proof_text'].split(' A hypercube proof')[0]+' A hypercube proof still needs uniform exploration and dependence estimates. The cached survey specifies epsilon=o(1) and epsilon>>2^(-d/3). It says Hulshof--Nachmias established the subcritical order Theta_P(epsilon^(-2) log(epsilon^3 2^d)), while the sharp leading constant remained missing in that revision. This local cached-source statement is not a certification of present openness.'

# C0153 has no matched problem card in the selected store queries. Link the
# proved obstruction to the actual local-weak-convergence technique card.
fk_key='random-cluster-finite-energy-boundary-obstruction'
tech=next(c for c in cards['C0153'] if 'Local Weak Convergence and the Objective Method' in c['title'])
quote=tech['body'].split('\n')[0][:500]
entry=next(e for e in bundle['entries'] if e['key']==fk_key)
bundle['relations'].append({'from_key':fk_key,'to_existing_logical':tech['metadata']['logical_id'],'kind':'semantic_association','rationale':''})
edges.append({'from_key':fk_key,'to_existing_logical':tech['metadata']['logical_id'],'kind':'semantic_association','new_end_quote':entry['statement'],'existing_end_quote':quote,'existing_node_id':tech['id'],'audit_status':'PENDING w347'})

ledger=Path('~/Downloads/Probability_1000_20h_20260906/problems.jsonl')
with ledger.open(encoding='utf-8-sig') as f:
    matches=[{'path':ledger.as_posix(),'line':n,'record':json.loads(line)} for n,line in enumerate(f,1) if '"P0476"' in line]
assert len(matches)==1
held=matches[0]
assert held['record']['result_status']=='held' and held['record']['current_status']=='unverified'
(ROOT/'evidence/C0011_held_source.json').write_text(json.dumps(held,indent=2)+'\n',encoding='utf-8')
key='torus-local-time-level-set-held-status'
statement='The 2026-09-07 local campaign row P0476, originating as C0011, records result_status=held and current_status=unverified. Its stated reason is that later wired-boundary local-time results do not directly match the torus with inverse-origin-local-time clock. The revision of Biskup\'s notes after Problem 16.11 cites an Abe--Biskup intermediate-level-set result in a different parametrization. That update alone is not a verified exact-domain resolution of the torus problem. A store heading saying "Resolved or excluded" must not be used as a proof that this exact problem was solved.'
bundle['entries'].append({'key':key,'namespace':'probability.openproblems','logical_name':key,'kind':'concept','title':'C0011 torus level-set status is held, not a verified resolution','statement':statement,'proof_text':None,'assumptions':[],'domain':'probability','source':{'source_id':'owner:w333:c0011-held-source-status','url':(ROOT/'evidence/C0011_held_source.json').as_uri(),'revision':'2026-10-10-read-of-2026-09-07-record','license':'owner-own-work','excerpt':None}})
resolved=next(c for c in cards['C0011'] if c['title'].startswith('Resolved:'))
quote=resolved['body'].split('\n')[0][:500]
bundle['relations'].append({'from_key':key,'to_existing_logical':resolved['metadata']['logical_id'],'kind':'semantic_association','rationale':''})
edges.append({'from_key':key,'to_existing_logical':resolved['metadata']['logical_id'],'kind':'semantic_association','new_end_quote':statement,'existing_end_quote':quote,'existing_node_id':resolved['id'],'audit_status':'PENDING w347'})
by_key={e['key']:e for e in bundle['entries']}
for edge in edges:
    edge['new_end_quote']=by_key[edge['from_key']]['statement']
for relation in bundle['relations']:
    if 'to_key' in relation:
        relation['rationale']='New end: "'+by_key[relation['from_key']]['statement']+'" Dependency end: "'+by_key[relation['to_key']]['statement']+'"'
    else:
        edge=next(e for e in edges if e['from_key']==relation['from_key'] and e['to_existing_logical']==relation['to_existing_logical'])
        relation['rationale']='New end: "'+edge['new_end_quote']+'" Existing end: "'+edge['existing_end_quote']+'" The relation applies to this stated reduction, status distinction, or quoted step; no audited open-problem solution is asserted.'
part=path.with_suffix('.part')
part.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
part.replace(path)
(ROOT/'edges.jsonl').write_text(''.join(json.dumps(e,ensure_ascii=False)+'\n' for e in edges),encoding='utf-8')

# Keep evidence pointers and short quotes; do not redistribute pages of papers.
excerpts=json.loads((ROOT/'evidence/source_excerpts.json').read_text(encoding='utf-8'))
for row in excerpts:
    row['anchors']=[e['anchor'] for e in row['excerpts']]
    row.pop('excerpts')
    if row['label']=='P0189-brown':
        row['short_quote']='Theorem 12.2. The Brown measure of u + λv is the Haar measure on the unit circle'
    if row['label']=='C0070':
        row['note']='The cached revision distinguishes known subcritical order from its missing sharp leading constant; epsilon=o(1) is part of the stated range.'
    if row['label']=='C0011':
        row['note']='Problem 16.11 concerns the torus and inverse-origin-local-time clock. The revision update points to Abe--Biskup; compare the domain and clock before calling it a full resolution.'
(ROOT/'evidence/source_excerpts.json').write_text(json.dumps(excerpts,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

proof=ROOT/'proofs/P0189.md'
text=proof.read_text(encoding='utf-8')
text=text.replace('full counterexample remains a candidate pending the cited Brown-measure theorem and w347\'s independent KEEP','full counterexample remains a candidate pending w347\'s independent KEEP')
text+='\nCached-source check, 2026-10-10: Fang--Jiang--Lin--Xu, arXiv:1210.4771v1, Theorem 12.2 explicitly includes lambda=1 and gives Haar Brown measure on the unit circle. The paper uses the canonical irrational-rotation pair in its tracial GNS representation. The source dependency has now been checked locally; the full candidate is still unaudited. The survey scope and source pointers are in evidence/source_excerpts.json.\n'
proof.write_text(text,encoding='utf-8')
proof=ROOT/'proofs/C0070.md'
text=proof.read_text(encoding='utf-8')
text+='\nSource scope check: the cached survey requires epsilon=o(1), epsilon>>2^(-d/3); the known subcritical Theta order does not supply its sharp leading constant in that revision. No current-literature certification is claimed.\n'
proof.write_text(text,encoding='utf-8')
row={'row_id':'S1.O.w333.c0011-held-status','problem_id':'C0011','result_type':'source-status correction','label':'source record checked; audit pending','statement':statement,'source_path':ledger.as_posix(),'source_line':held['line'],'source_quote':held['record']['exclusion_reason'],'entry_key':key,'audit_status':'PENDING w347'}
with (ROOT/'results.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(row)+'\n')
print('Final bundle:',len(bundle['entries']),'entries;',len(bundle['relations']),'relations;',len(edges),'quoted existing edges')
