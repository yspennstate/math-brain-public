import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parent
INBOX=Path('~/math-brain-inbox/w552')
source={'source_id':'owner-probability300-C0047-w552-v1:nb-obstruction',
        'url':(ROOT/'NB_ROUTE_OBSTRUCTION.md').as_uri(),'revision':'author-draft-2026-10-10-v1',
        'license':'owner-own-work (campaign route obstruction, independent review pending)','excerpt':None}

def entry(key,name,title,statement):
    return {'key':key,'namespace':'probability.percolation','logical_name':name,'kind':'concept',
            'title':title,'statement':statement,'proof_text':None,
            'assumptions':['Independent Bernoulli bond percolation','Fixed simple Cayley graph of C3*C2 with generators a,a inverse,s'],
            'domain':'probability theory: nonamenable percolation','source':source.copy()}

entries=[
entry('graph','cyclic-three-free-product-cyclic-two-tree-of-triangles-graph',
      'Draft graph model: C3*C2 tree of triangles',
      'DRAFT, independent review pending. The free product Gamma=C3*C2, with a of order 3 and s of order 2, has simple undirected Cayley graph for S={a,a inverse,s}. It is 3-regular. The a-cosets are triangles, every vertex has one s-bridge, and contracting triangles yields the 3-regular tree. For any finite nonempty vertex set K, |boundary_E K|>=|K|/3+2, so the graph is nonamenable. The proof uses free-product normal form and the forest count on occupied quotient blocks.'),
entry('shortcut','refuted-universal-nonbacktracking-critical-threshold-shortcut',
      'REFUTED route: nonamenability universally supplies pc beta<1',
      'REFUTED ROUTE PROPOSAL, NOT AN ACCEPTED THEOREM. For a d-regular nonamenable Cayley graph, let b=d-1, alpha=||A||_2 and beta=sqrt(b) if alpha<=2sqrt(b), otherwise beta=(alpha+sqrt(alpha squared-4b))/2. The proposed universal shortcut p_c beta<1 is false. Its use as an extra sufficient hypothesis in a conditional operator bound remains valid. The fixed C3*C2 tree-of-triangles graph instead has p_c beta>1.'),
entry('obstruction','tree-of-triangles-counterexample-universal-nonbacktracking-input',
      'Draft author proof: obstruction to the universal nonbacktracking shortcut',
      'UNREVIEWED AUTHOR PROOF, novelty not asserted. On the 3-regular Cayley graph of C3*C2 with S={a,a inverse,s}, Bernoulli bond percolation explores disjoint triangle blocks with nonroot offspring mean m(p)=2p(p+p squared-p cubed). At p=3/5 this mean is 558/625<1, so p_c>3/5. Constant-on-triangle test vectors give alpha=||A||_2>=2+2sqrt(2)/3. The nonbacktracking root beta=(alpha+sqrt(alpha squared-8))/2 is greater than 5/3, because z+2/z at z=5/3 is 43/15<2+2sqrt(2)/3. Hence p_c beta>1. A closed bridge separates independent surviving half-tree clusters with positive probability for p_c<p<1, yielding p_u=1. This refutes the extra universal spectral shortcut and is a special case of C0047, not a counterexample to it.'),
]
bundle={'spec':'mathbrain-draft-v1','author_agent':'w552',
        'bundle_slug':'c0047-refuted-universal-nonbacktracking-shortcut-v1','entries':entries,
        'relations':[
            {'from_key':'obstruction','to_key':'shortcut','kind':'refutes','rationale':'The shortcut requires p_c beta<1 on every nonamenable Cayley graph; this fixed nonamenable graph has p_c beta>1.'},
            {'from_key':'obstruction','to_key':'graph','kind':'depends_on','rationale':'The exact triangle/bridge graph structure gives the block branching law and adjacency test vectors.'}]}
serialized=json.dumps(bundle,ensure_ascii=False,indent=2)+'\n'
(ROOT/'brain_draft'/'bundle_002.json').write_text(serialized,encoding='utf-8')
final=INBOX/'bundle_002.json'
if final.exists():
    assert final.read_text(encoding='utf-8')==serialized, 'existing bundle differs; preserve it'
else:
    part=INBOX/'bundle_002.json.part'
    part.write_text(serialized,encoding='utf-8')
    part.rename(final)

status=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
status['target_status']='public-resolution-claim-unverified'
status['current_openness']='UNKNOWN'
status['public_resolution_claim']={
    'family':214,'date_in_manuscript_path':'2026-09-24',
    'overview_url':'https://github.com/openai/math/blob/main/overview.tex',
    'manuscript_url':'https://github.com/openai/math/blob/main/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf',
    'claimed_scope':'Every infinite connected locally finite nonamenable quasi-transitive graph; Bernoulli bond; pc<p2to2<=pu.',
    'source_claim_verified':True,'mathematical_proof_verified_by_w552':False,'formal_receipt':False,
    'comparator_url':'https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/BenjaminiSchramm.lean',
    'comparator_note':'full_main, critical_laws and cayley_main have sorry placeholders; this challenge file is not evidence about a separate library proof.',
    'effect':'August 2026 conjectural status is historical only. No current-openness or novelty certification.'}
status['route_obstruction']={'claim_id':'w552-C0047-OB1','route':'nonamenability universally implies pc beta<1',
                             'status':'refuted by author special case; independent check pending',
                             'parent_conjecture_refuted':False}
status['store_snapshot']={'path':str(ROOT/'STORE_SNAPSHOT.json'),'store_mode':'ro',
                         'targeted_rows':2,'live_edits':False}
status['mathematical_feedback']=[{'from':'w553','claims':['L1','L2','L3 conditional only'],
                                'verdict_reported':'KEEP','evidence_pointer':'~/brain_workers/w553/PROVER_AUDIT.md',
                                'evidence_type':'peer mesh message read at 07:10 UTC; not rereviewed',
                                'served_model_receipt':'UNKNOWN','formal_referee_w554':'pending'}]
status['peer_boundaries']={'w555':'cuts/block-branching; overlapping normalization correction noted',
                           'w559':'independent triangle family; our added scope is pc beta obstruction, no duplicate enumeration',
                           'w561':'independently saved Russo/BK continuation; overlapping baseline reduction noted'}
(ROOT/'SOURCE_STATUS.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

files=['STATEMENT.md','ATTEMPT.md','NONBACKTRACKING_LEMMA.md','NB_ROUTE_OBSTRUCTION.md','CLAIMS.jsonl',
       'SOURCE_STATUS.json','PRIOR_DIGEST.md','PRIOR_RECORDS.json','STORE_SNAPSHOT.json','validate.py',
       'VALIDATION.json','COMPUTE_GATE.json','validate_obstruction.py','OBSTRUCTION_VALIDATION.json',
       'OBSTRUCTION_GATE.json','REPORT.md','REVIEW.md','brain_draft/bundle_001.json','brain_draft/bundle_002.json',
       'HOOK_PROPOSAL.jsonl','HOOK_CONTROLS.json']
hashes=[{'path':str(ROOT/f),'sha256':hashlib.sha256((ROOT/f).read_bytes()).hexdigest()} for f in files]
inboxes=[{'path':str(INBOX/f),'sha256':hashlib.sha256((INBOX/f).read_bytes()).hexdigest()} for f in ['bundle_001.json','bundle_002.json']]
packet=json.loads((ROOT/'REVIEW_PACKET.json').read_text(encoding='utf-8'))
packet.update({'packet_id':'w552-C0047-critical-operator-v2','created_utc':datetime.now(timezone.utc).isoformat(),
               'claim_ids':[json.loads(l)['claim_id'] for l in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines()],
               'scoped_keep_candidates':['L1','L2','L3 conditional only','L4 with strict input','TREE special case','CORR1 normalization','OB1 route counterexample only'],
               'file_hashes':hashes,'inbox_drafts':inboxes,'public_resolution_claim':status['public_resolution_claim'],
               'mathematical_feedback':status['mathematical_feedback'],
               'NEXT':'w554 independently check seven scoped mathematical claims; preserve the general critical-norm and public-resolution proof/model gates.'})
(ROOT/'REVIEW_PACKET.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
summary={'packet':str(ROOT/'REVIEW_PACKET.json'),'packet_sha256':hashlib.sha256((ROOT/'REVIEW_PACKET.json').read_bytes()).hexdigest(),
         'claims':len(packet['claim_ids']),'draft_entries':10,'inbox_drafts':inboxes,'review_state':'PENDING',
         'mathematical_feedback':'w553 KEEP L1-L3 conditional; served-model receipt UNKNOWN',
         'target_solved':False,'current_openness':'UNKNOWN'}
(ROOT/'DELIVERY_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary))
