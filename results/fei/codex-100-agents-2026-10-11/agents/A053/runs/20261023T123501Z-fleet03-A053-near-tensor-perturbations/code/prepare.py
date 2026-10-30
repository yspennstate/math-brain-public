from pathlib import Path
import json,hashlib,shutil
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1]
(RUN/'out').mkdir(exist_ok=True)
old=ROOT/'runs/20261023T064432Z-fleet03-A053-near-tensor-perturbations/code/arithmetic.py'
shutil.copyfile(old,RUN/'code/arithmetic.py')
indsource=ROOT/'runs/20261023T064432Z-fleet03-A053-near-tensor-perturbations/code/independent.py'
header=indsource.read_text(encoding='utf-8').split('roots=cuts=0')[0]
assert 'def verify' not in header and 'def ent' in header
(RUN/'code/independent_arithmetic.py').write_text(header,encoding='utf-8',newline='\n')
spec={'family':'All n3 signed-character seeds and every edit set size0..3; fixed n6 and n9 triple-coded point-defect seeds with specified edits','domain':{'n3_seed_count':16,'n3_edit_sets_per_seed':93,'n6_edits':[[0],[0,1],[0,7],[0,63],[0,1,2],[0,1,7],[0,1,2,3],[0,7,56,63],list(range(8))],'n9_edits':[[0],[0,1],[0,7],[0,1,2],[0,7,56],list(range(8))]},'symmetry':'none; all labelled seed/edit choices retained','arithmetic':'integer Walsh and edges, exact Fraction, rational atanh24 log intervals','helper_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'memory_estimate_MB':80,'maximum_runtime_seconds':55,'pilot':'n3 all16 signed characters, edit sets0..2','automatic_dimension_escalation':False,'new_predicates':['seed-dependent Cauchy lower influence','seed-independent off-anchor coefficient <=actual queried influence','linear37R/4 payment','same-bank gain at10R','branch boundary n+1=4R'],'independent':'separate direct characters and own atanh32 helper on all n3 signed-character edits1..3 plus frozen n6/n9 fixtures; estimated80MB/55seconds'}
(RUN/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8',newline='\n')
compute=Path(r'~\.claude\compute\compute_state.json')
if compute.exists():
 d=json.loads(compute.read_text(encoding='utf-8-sig'))
 (RUN/'out/COMPUTE_BEFORE.json').write_text(json.dumps({'observed_utc':__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),'snapshot':d},indent=2)+'\n',encoding='utf-8',newline='\n')
 print('compute snapshot timestamp',d.get('ts'),'not assumed fresh')
log=Path(r'~\.claude\compute\governor.log')
if log.exists():
 with log.open('rb') as f:
  f.seek(max(0,log.stat().st_size-3000))
  tail=f.read().decode('utf-8',errors='replace')
 (RUN/'out/GOVERNOR_TAIL.txt').write_text(tail,encoding='utf-8',newline='\n')
checkpoint={'state':'proof saved and search frozen','next':'pilot then full linear-branch checks and separate replay','administrative_blocker':'checklist working T-20261023-452 failed: checklist lock held too long; no lock touched','wake':'degraded: owner model99h,state83.6h,dream34.3h stale; personal context/consolidation not premises'}
(RUN/'out/CHECKPOINT.json').write_text(json.dumps(checkpoint,indent=2)+'\n',encoding='utf-8',newline='\n')
(ROOT/'STATUS.md').write_text('STATE: Stage20 proof saved: candidate linear37R/4 critical-radius payment;branch certificates next;prior quadratic theorem unchanged;FEI OPEN.\nNEXT: Validate sparse-derivative lower influence and independent-seed edge cancellation, retaining original complete-child bank.\n',encoding='utf-8',newline='\n')
print('proof checkpoint and frozen search saved')
