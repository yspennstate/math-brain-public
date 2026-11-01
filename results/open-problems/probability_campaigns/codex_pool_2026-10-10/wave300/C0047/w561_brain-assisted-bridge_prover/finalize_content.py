from pathlib import Path
import json

root=Path(__file__).resolve().parent
rows=[json.loads(s) for s in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if s]
for row in rows:
    row['peer_review_receipt']={'reviewer':'w562','verdict':'scoped KEEP reported','path':'~/brain_workers/w562/AUDIT_W561.md',
        'message_time':'2026-10-10T07:21:00Z','response_side_served_model':'UNKNOWN','named_referee_gate':'w563 pending'}
    if row['id'].endswith('L05'):
        row['statement']='For an infinite connected countable vertex-transitive simple graph of bounded degree, independent Bernoulli bond percolation satisfies pc<pu if pc<1/a, with a=||A||2->2>=1. On a d-regular graph this condition is pc*d*rho<1 with rho the normalized random-walk spectral radius.'
        row['assumptions']=['Infinite connected countable vertex-transitive simple graph','Uniformly bounded degree','Independent Bernoulli bond law','a=||A||2->2>=1','pc*a<1']
(root/'CLAIMS.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')
failure=json.loads((root/'RETRIEVAL_FAILURE.json').read_text(encoding='utf-8'))
failure['observed_bounded_fallback']={'seconds':json.loads((root/'BRAIN_RETRIEVAL.json').read_text(encoding='utf-8'))['seconds'],
    'completed_target_cards':2,'method':'read-only targeted title SQL; not the same retrieval engine as the timed-out general recall'}
failure['repair_state']='Bounded fallback observed; numeric normalization guard is an unmeasured code proposal, microchecks held at two fresh CPU gates.'
(root/'RETRIEVAL_FAILURE.json').write_text(json.dumps(failure,indent=2),encoding='utf-8')
with (root/'STATUS.md').open('a',encoding='utf-8') as f:
    f.write('2026-10-10: STUCK: two microcheck gates refused at CPU 88.1% and 86.0%; did not weaken the limit or run the experiments. Proceeded with analytic proofs and clearly unmeasured guard proposal. Scoped KEEP receipt from independent adversary w562 recorded; official w563/model gates still pending.\n')
    f.write('2026-10-10: First DRAFT bundle and narrow hook proposal submitted; schema/dependency and fire/silent controls passed. Revision 2 makes the connected/nonzero-adjacency assumptions in L05 explicit, corrects the formal declaration namespace, and records superseded drafts without deleting them.\n')
