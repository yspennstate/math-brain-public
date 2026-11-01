"""Record the newly delivered peer kernel audit and revision metadata."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parent
peer=Path('~/brain_workers/w468/ATTEMPT.md')
snapshot=root/'PEER_KERNEL_AS_READ.md'
snapshot.write_bytes(peer.read_bytes())
claim={'claim_id':'w469-C0052-PEER-KERNEL-AUDIT-001','target':'C0052',
 'statement':'Under w468\'s explicitly stated subcritical sourced-current assumptions, equations (A)-(G) in ATTEMPT.md give valid endpoint-average and original-single-current first/second-moment reductions. UCM m2<=C m1^2 remains an unproved sufficient input; no C0052 proof is supplied.',
 'assumptions':['Homogeneous zero-field nearest-neighbor Ising on Z^3 at 0<beta<beta_c','Finite susceptibility, exponential xi>=1 and the subcritical sourced-current switching construction','Independent endpoint draws X,W; Y uniform in the specified box','Condition on Y before using independence of the two components','Keep joint two-hit kernel k2 and diagonal terms'],
 'source':{'path':str(peer),'as_read_copy':str(snapshot),'sha256':hashlib.sha256(snapshot.read_bytes()).hexdigest()},
 'proof_or_counterexample':'Independent derivations in REVIEW_W468.md: -g=2xi^(-3)sum_y Q_y; Q_B>=m1^2/m2; m1,m2 are the stated kernel convolutions; k_aug=G and G/chi<=k<=G. N^2>=N implies UCM requires m1>=1/C, whereas the trivial endpoint coincidence only guarantees 1/|B|.',
 'independent_reviewer':'w469 scoped adversarial check; designated referee w470 pending',
 'remaining_gap':'A dimension-specific original-current occupation floor and joint two-hit/nonclumping estimate proving UCM, or a weaker positive subsequence. No different-model gate or new infinite-volume construction is certified.',
 'status':'independently checked proof','review_state':'KEEP conditional reduction only; UCM unproved','recorded_utc':datetime.now(timezone.utc).isoformat()}
known={json.loads(line)['claim_id'] for line in (root/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()}
if claim['claim_id'] not in known:
    with (root/'CLAIMS.jsonl').open('a',encoding='utf-8') as stream:
        stream.write(json.dumps(claim,ensure_ascii=False)+'\n')
packet_path=root/'REVIEW_PACKET.json'
packet=json.loads(packet_path.read_text(encoding='utf-8'))
packet['peer_scope']='w468 finite-tree laws and new original-current kernel equations (A)-(G) independently checked as conditional reductions. UCM unproved; designated w470 referee pending.'
packet['hardest_remaining_input']='UCM (or a positive subsequence): prove m2<=C m1^2 for original unaugmented source-component overlap at xi_exp scale, including a nonvanishing occupation estimate; source normalization and joint conditioning are explicit.'
for name in ['PEER_KERNEL_AS_READ.md','fix_source_patch.py','revise_review.py','check_handoff.py']:
    path=root/name
    if not any(Path(item['path'])==path for item in packet['artifacts']):
        packet['artifacts'].append({'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
packet_path.write_text(json.dumps(packet,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report_path=root/'REPORT.md'
report=report_path.read_text(encoding='utf-8')
note='The updated w468 original-current kernel reduction (A)-(G) was also independently checked. Its UCM input m2<=C m1^2 remains unproved. A necessary consequence m1>=1/C shows why the trivial 1/|B| endpoint contribution is insufficient. The paired packet preserves joint two-hit probabilities and conditions on Y correctly.\n\n'
if note not in report:
    report_path.write_text(report.replace('Measured with',note+'Measured with'),encoding='utf-8')
print(json.dumps({'kernel_verdict':'KEEP conditional reduction','UCM':'UNPROVED','claim_added':claim['claim_id'],'snapshot_sha256':claim['source']['sha256']}))
