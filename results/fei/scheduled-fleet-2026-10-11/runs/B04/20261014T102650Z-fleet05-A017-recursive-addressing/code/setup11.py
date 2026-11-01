from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1]
v=(R/'code/tree10.py').read_text(encoding='utf8').replace('A017-ten-edit-tree-v1','A017-eleven-edit-tree-v1').replace('edits<=10','edits<=11').replace('min(10,len(K))','min(11,len(K))').replace('min(9,len(K))','min(10,len(K))').replace('F(13,2)','F(34,5)').replace('for s in [1,9,10]','for s in [1,10,11]').replace('tree10_pilot.json','tree11_pilot.json').replace('tree10_validation.json','tree11_validation.json')
(R/'code/tree11.py').write_text(v,encoding='utf8')
p=R/'code/actual5edge.py'
spec=dict(helper='A017-actual-six-control-five-edge-v1',helper_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),family='actual six-control parent with five pivotal selector edges and quadratic five-control children',domain='four quadratic graph cores,32 linear characters,32 translated five-vertex sets{0,1,2,3,4}',pilot_case_count=4,full_case_count=4096,symmetry='none for verification; translation and common character are controls only',arithmetic='direct Boolean edges, integer Walsh and exact integer entropy-product comparisons',memory_estimate_MB=30,max_runtime_seconds=60)
(R/'out/actual5edge_FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf8');print('Eleven-edit checker generated; actual five-edge spec frozen.')
