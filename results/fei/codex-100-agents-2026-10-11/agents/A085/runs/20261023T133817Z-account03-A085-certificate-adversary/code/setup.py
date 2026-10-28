from pathlib import Path
import hashlib,json,shutil
R=Path(__file__).resolve().parents[1]
(R/'out').mkdir(exist_ok=True)
old=R.parent/'20261023T112613Z-account03-A085-certificate-adversary'/'code'
for name in ('algebra.py','log_intervals.py'):
    shutil.copyfile(old/name,R/'code'/name)
spec={'helper_version':'A085-floor-adversary-v1','files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (R/'code').glob('*.py')},'family':'A097 original complementary controller, equal-sign three-bit defect core, disjoint parity blocks, both signs; separate finite probability projection algebra','pilot':'full wrappers L=1, both signs; endpoint algebra and fixed dyadic floor k=1..64','main':'full wrappers L=1,2 both signs (4 roots); all first-block histories (8 query nodes,12 converted leaves,24 post-query full children); seed-only L=3,4 all first-block histories; 64 fixed dyadic floors per sign and old booking 0,1/4; projection grid r in {0,1/4,1/2}, a in quarter units up to 1-r, ell in eighth units from a to 1-r','symmetry':'none; all labelled prefix outcomes retained','arithmetic':'integer FWHT crosschecked with independently expanded signed polynomial and direct character controller; physical pivotal counts; Fraction complete laws; exact prime-log identities and 100-bit outward dyadic atanh(40 terms) bounds','memory_MB':140,'runtime_seconds':55,'no_automatic_dimension_escalation':True,'formal_verification':'NOT_CLAIMED'}
(R/'out'/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
print('Frozen spec saved before evaluation')
