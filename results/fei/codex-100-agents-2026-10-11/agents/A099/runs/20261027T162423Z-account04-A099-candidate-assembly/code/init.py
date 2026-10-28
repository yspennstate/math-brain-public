from pathlib import Path
import json,hashlib,shutil
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1];A=R.parents[1]
OLD=A/'runs/20261026T233346Z-account04-A099-candidate-assembly'
ROOT=A.parents[1]
for n in ['out','out/sources']:(R/n).mkdir(parents=True,exist_ok=True)
def put(n,d):(R/n).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
receipts=[]
def pin(p,copy=False):
 raw=p.read_bytes();s=raw.decode('utf-8-sig')
 receipts.append(dict(path=str(p),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
 if copy:(R/'out/sources'/(p.parent.name+'-'+p.name)).write_bytes(raw)
 return s
protocol=Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json')
pin(protocol);pin(ROOT/'BOARD.md');pin(ROOT/'claude/B20/STREAM_NOTES.md');pin(A/'STATUS.md')
sources=[('A012','20261027T062634Z-account04-A012-sparse-activation-accounting',['DERIVATION.md','CLAIMS.json','REPORT.md']),('A097','20261027T092641Z-account04-A097-cross-route-transfer',['PROOF.md','CLAIMS.json','REPORT.md']),('A093','20261027T124307Z-account04-A093-literature-and-priority',['DERIVATION.md','CLAIMS.json']),('A098','20261027T125558Z-account04-A098-resource-reallocation',['REVIEW.md','CLAIMS.json']),('A011','20261027T025625Z-account04-A011-representation-existence',['DERIVATION.md','CLAIMS.json']),('A094','20261026T232939Z-account04-A094-proof-chain-challenger',['REPORT.md']),('A100','20261027T023227Z-account04-A100-release-and-continuation-ledger',['REVIEW.md'])]
for a,run,names in sources:
 for name in names:pin(ROOT/'agents'/a/'runs'/run/name,True)
for src,dst in [('CANDIDATE_MANUSCRIPT.tex','out/BASELINE_v11.tex'),('CLAIMS.json','out/BASELINE_CLAIMS.json'),('out/PROOF_DEPENDENCIES.json','out/BASELINE_DAG.json'),('code/exact.py','code/exact.py')]:
 shutil.copyfile(OLD/src,R/dst)
put('out/SOURCE_RECEIPTS.json',receipts)
put('out/FROZEN_SPEC.json',dict(helper_version='A099-v12 direct literal Walsh + prior prime-log utilities',family='All labelled Boolean tables n<=3, literal physical children, covering references matched and matched/uniform mixture; full profile updates; explicit affine tilts and high-moment AND2 tensors; AND3 forward-handoff witness',pilot_domain='all labelled n<=2 and n4 moment fixture',main_domain='all labelled n<=3, all coordinates, two reference recipes, update parameters0,1/2,1; full adaptive trees n<=2; moment n4,6,8,10; all16 labelled AND3 translations/signs x3 queries x2 children',case_count='278 truth tables; 804 physical coordinate choices x2 references;44 fixed outcome-adaptive trees;4 analytic-family fixtures;48 AND3 queries',symmetry='none; AND3 translations and output signs explicit',arithmetic='Fraction, literal integer Walsh, exact prime-log identities, outward rational log bounds',memory_MB=140,pilot_seconds=55,max_runtime_seconds=55,automatic_dimension_escalation=False,scope='Finite checks accompany finite analytic identities and all-dimensional family formulas; no FEI supplier proved'))
put('out/CHECKPOINT.json',dict(timestamp=datetime.now(timezone.utc).isoformat(),state='SOURCES_PINNED_SPEC_FROZEN',next='Reconstruct affine/projection fee identities and nonfree forward handoff; test exact full tree ledger'))
(A/'STATUS.md').write_text('STATE: A099 v12 in progress: sources pinned; full query-KL/affine-fee ledger and AND3 forward-handoff cost selected;full FEI OPEN.\nNEXT: Independently reconstruct exact full-bill identity, certify bounded cases and high-moment guard, then integrate source without claiming initial O(I) supplier.\n',encoding='utf-8')
print('Saved',len(receipts),'source receipts and frozen specification')
