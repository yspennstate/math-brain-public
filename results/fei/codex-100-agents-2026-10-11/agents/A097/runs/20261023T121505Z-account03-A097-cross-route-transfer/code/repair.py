from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];p=R/'code/check.py';data=p.read_bytes()
(R/'out/check_v1.py.txt').write_bytes(data);(R/'out/FROZEN_SPEC_v1.json').write_bytes((R/'out/FROZEN_SPEC.json').read_bytes())
t=data.decode('utf-8');t=t.replace('import json,time,sys,hashlib','import json,time,sys,hashlib\nfrom math import lcm')
t=t.replace('def lg(q):',"def nonnegative(e):\n if not e:return True\n den=lcm(*(v.denominator for v in e.values()));left=right=1\n for p,v in e.items():\n  k=int(v*den)\n  if k>0:left*=p**k\n  else:right*=p**(-k)\n return left>=right\ndef lg(q):")
t=t.replace('expected_delta={2:F(-3,16),3:F(9,32),5:F(-3,16)}','expected_delta={3:F(9,32),5:F(-3,16)}')
t=t.replace('# The occupancy is exactly0 here (same occupied orientations in qnew), hence the post query is fully paid.\n    ok(occ=={})','# The last-bit case can have positive occupancy KL; certify its sign exactly, without discarding it.\n    ok(nonnegative(occ))')
t=t.replace('ok(sum(q)==1);ok(kl(p,q)==add(lg(a/ell),lg((t-a)/(t-ell)),(t-a)/a) if False else True)','ok(sum(q)==1)')
assert t!=data.decode('utf-8');p.write_text(t,encoding='utf-8',newline='')
spec=json.loads((R/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'));spec['helper_version']='A097-floor-admission-same-owner-v2';spec['helper_sha256']=hashlib.sha256(p.read_bytes()).hexdigest();spec['revision_reason']='Correct expected prime-log map; remove unwarranted zero-occupancy assumption in last-bit continuation, certify actual nonnegative KL instead; theorem unchanged'
(R/'out/FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
failure={'attempt':'v1 pilot','result':'FAIL at assertion291 before main','first_failing_line':'kl(pp,qnew)==expected_delta','cause':'Expected map incorrectly included an extra -3/16 log2(2); exact stated cost is(3/32)log2(27/25)','additional_pre-main_audit_fix':'Post-conversion occupancy may be positive for L1; replace false checker equality with exact integer-power nonnegative-KL certificate; analytic proof already uses -D_occ<=0','preserved':['out/check_v1.py.txt','out/FROZEN_SPEC_v1.json'],'proof_or_scope_changed':False}
(R/'out/INITIAL_FAILURE.json').write_text(json.dumps(failure,indent=2)+'\n',encoding='utf-8')
own=R.parents[1];(own/'STATUS.md').write_text('STATE: A097 stage20 active: floor-class minimum cost derived; arbitrary-depth isospectral same-original35/4 bank retains>77/32 after old quarter; v1 checker error preserved; exact validation pending; FEI OPEN.\nNEXT: Validate repaired fixed pilot/main and independent full physical witness; save scoped admission theorem and exact initial-source gap.\n',encoding='utf-8')
print(json.dumps({'frozen_revision':'v2','failure_preserved':True,'theorem_changed':False}))
