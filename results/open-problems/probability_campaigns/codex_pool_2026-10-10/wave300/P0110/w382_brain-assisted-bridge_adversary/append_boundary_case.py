"""Save the newly found exact boundary case to the local packet only."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
claim={'id':'w382-P0110-small-displacement-007','kind':'hypothesis_counterexample',
    'status':'proved special case',
    'statement':'For d>=2 and weights in [a,b] with 0<a<=b<3a, every geodesic between adjacent vertices is the direct edge, so D(0,e_1)=0. Consequently inf_{v!=0} E D(0,v)/|v|^s=0 for every real s. Thus Uniform[1,2] fails the literally printed Auffinger--Damron Eq. (2.2) lower wandering premise over all nonzero displacements; this finite obstruction does not refute Chatterjee\'s lower premise outside a large ball.',
    'assumptions':['Nearest-neighbor lattice Z^d, d>=2','Every edge weight lies in [a,b]','0<a<=b<3a','D is distance to the endpoint segment, maximized over minimizing paths'],
    'source':{'url':'https://arxiv.org/pdf/1109.0523','location':'Eq. (2.2), PDF page 4','own_derivation':'SMALL_DISPLACEMENT_OBSTRUCTION.md','license':'owner-own-work (campaign boundary-case deduction)'},
    'proof_or_counterexample':(ROOT/'SMALL_DISPLACEMENT_OBSTRUCTION.md').read_text(encoding='utf-8'),
    'independent_reviewer':'w383 (pending)',
    'remaining_gap':'Independent referee check; no asymptotic exponent matching has been shown. Do not silently modify a published theorem\'s assumptions.',
    'review_state':'draft'}
existing=[json.loads(line) for line in (ROOT/'CLAIMS.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
if claim['id'] not in {row['id'] for row in existing}:
    with (ROOT/'CLAIMS.jsonl').open('a',encoding='utf-8') as handle: handle.write(json.dumps(claim,ensure_ascii=False)+'\n')
source_status=json.loads((ROOT/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source_status['printed_AD_lower_bound_caveat']='SMALL_DISPLACEMENT_OBSTRUCTION.md: all-nonzero Eq. (2.2) fails for Uniform[1,2] because D(0,e_1)=0; Chatterjee (A4) uses sufficiently large displacements.'
(ROOT/'SOURCE_STATUS.json').write_text(json.dumps(source_status,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
path=ROOT/'draft_bundle'/'bundle_001.json'
bundle=json.loads(path.read_text(encoding='utf-8'))
gate=next(entry for entry in bundle['entries'] if entry['key']=='global-hypothesis-gate')
addition=' Important convention boundary (independent referee check pending): Auffinger--Damron Eq. (2.2) as printed uses all nonzero displacements. With edge support [a,b], b<3a, adjacent vertices have only the direct edge as a geodesic, so D(0,e_1)=0 and the printed lower wandering premise fails. This includes Uniform[1,2]. Chatterjee\'s outside-large-ball lower convention avoids this finite obstruction; asymptotic matching is still needed.'
if addition not in gate['statement']: gate['statement']+=addition
part=path.with_suffix('.part')
part.write_text(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
part.replace(path)
packet=json.loads((ROOT/'review_packet.json').read_text(encoding='utf-8'))
if 'SMALL_DISPLACEMENT_OBSTRUCTION.md' not in packet['math']: packet['math'].append('SMALL_DISPLACEMENT_OBSTRUCTION.md')
(ROOT/'review_packet.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'boundary_claim_saved':True,'new_theorem_promoted':False}))
