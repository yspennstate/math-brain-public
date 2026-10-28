from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];(R/'out').mkdir(exist_ok=True)
spec={'helper_version':'A097-floor-admission-same-owner-v1','helper_sha256':hashlib.sha256((R/'code/check.py').read_bytes()).hexdigest(),'family':'actual G_sigma,L with A079 four-bit complementary controller, g=-1 at equal3-sign inputs, each seed coordinate replaced by disjoint L-parity block','domain':'pilot L1/both signs; primary FIXED L1,2,3/both signs; reveal complete first block then fixed1/6 floor conversion on ALL leaves and one actual second-block-bit query','case_count':{'pilot_roots':2,'main_roots':6,'main_zero_credit_query_nodes':22,'main_converted_frontier_leaves':28,'main_post_conversion_children':56,'rational_floor_cases':18},'symmetry':'none; all physical outcome branches retained','arithmetic':'integer FWHT and independent direct physical pivotal edges, Fraction full normalized laws, exact prime-log CE/KL identities; integer 25<27<50 certifies positive cost<3/32','memory_estimate_MB':90,'max_runtime_seconds':45,'runtime_guard':'checked every assertion','automatic_dimension_escalation':False}
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
base=R.parents[3];paths=[base/'BOARD.md',base/'claude/B20/STREAM_NOTES.md',base/'agents/A097/STATUS.md']
for who,rid in [('A085','20261023T112613Z-account03-A085-certificate-adversary'),('A083','20261023T070041Z-account03-A083-formal-core'),('A079','20261023T105923Z-account03-A079-correlated-auxiliaries'),('A090','20261023T112633Z-account03-A090-independent-reconstruction')]:
 p=base/'agents'/who/'runs'/rid;paths.extend(x for x in p.iterdir() if x.name in ['PROOF.md','REPORT.md','CLAIMS.json'])
camp=Path('math-open-problems/reports/fei-2026-10-11');paths.extend(camp/x for x in ['EXECUTION_PROTOCOL.json','README.md','CURRENT_STATUS.md','CLAIM_REGISTRY.json','OBSTRUCTION_REGISTRY.json','PACKET_STATUS.json','STREAM_NEXT_ACTIONS.json','FEI_100_agent_research_plan.tex'])
records=[]
for p in paths:
 data=p.read_bytes();text=data.decode('utf-8-sig');records.append({'path':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'lines':len(text.splitlines())})
(R/'out/SOURCES.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
(R/'out/CHECKPOINT.md').write_text('Stage20: exact floor I-projection and SAME original35/4 payer derived; >77/32 remains after old quarter. NEXT: fixed pilot/main and independent direct physical reproduction. Necessity is declared recipe-class admission only; full FEI OPEN.\n',encoding='utf-8')
print(json.dumps({'frozen':True,'sources':len(records),'class_requirement':'same1/6 coherent point-source recipe as A083, relaxed to one likelihood floor'}))
