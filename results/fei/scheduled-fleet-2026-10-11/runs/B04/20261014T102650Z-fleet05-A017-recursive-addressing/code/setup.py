from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];old=R.parent/'20261014T043353Z-fleet05-A017-recursive-addressing'
v=(old/'code/tree8.py').read_text(encoding='utf8')
v=v.replace('A017-eight-edit-tree-v1','A017-ten-edit-tree-v1').replace('edits<=8','edits<=10').replace('min(7,len(K))','min(9,len(K))').replace('min(8,len(K))','min(10,len(K))')
start=v.index(' if not active and n==5 and edits==7 and polar:');end=v.index(' nodes+=1;B=U.erasure',start)
v=v[:start]+''' if not active and n<=5:
  i=max(range(n),key=lambda j:inf[j])
 else:i=active[0] if active else polar[0]
'''+v[end:]
# Affine masks of <=10 points on D>=6 pay13/2; every actual phase on D<=5 pays K by good-coordinate recursion.
v=v.replace("if not active and (not edits or not polar):","if not active and (not edits or (not polar and n>=6) or n==0):")
v=v.replace("U.LF((7)*sum(inf))","U.LF(F(13,2)*sum(inf))")
v=v.replace("(4+2/U.LN2[1])*spent+(7)*terminal","(4+2/U.LN2[1])*(spent+terminal)")
start=v.index('def leafconfigs(');end=v.index('def main():',start)
v=v[:start]+'''def leafconfigs(pilot=False):
 for n in [6] if pilot else [6,7,8]:
  for s in [1,9,10]:yield n,tuple(range(s))
'''+v[end:]
v=v.replace("U.LF((7)*worst)","U.LF(F(13,2)*worst)").replace('tree8_pilot.json','tree10_pilot.json').replace('tree8_validation.json','tree10_validation.json')
(R/'code/tree10.py').write_text(v,encoding='utf8')
for name in ['critical.py','ternary.py','seven.py']:(R/'code'/name).write_bytes((old/'code'/name).read_bytes())
def spec(name,**kw):
 p=R/'code'/name
 data=dict(helper=name,helper_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),arithmetic='integer Walsh, rational edges, exact prime-log forms with proved rational bounds or integer power comparisons; no floating verdict',memory_estimate_MB=100,max_runtime_seconds=180,symmetry='explicit normalization only; no physical influence relabeling',**kw)
 (R/'out'/(p.stem+'_FROZEN_SPEC.json')).write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
spec('five.py',family='all normalized five-control phases with coordinate0 having one pivotal edge',domain='a on four controls, a(0)=1, other15 signs arbitrary; b flips only0; chosen coordinate maximizes actual physical influence',pilot_case_count=256,full_case_count=32768,max_pilot_runtime_seconds=60)
spec('critical.py',family='generic four-control one-edge selected coordinate',domain='128 normalized three-bit child tables',case_count=128)
spec('ternary.py',family='generic five-control two-edge selected coordinate',domain='3^7 projected ternary child tables',case_count=2187)
spec('seven.py',family='preserved actual fixed-order seven-edit obstruction and repair',domain='one five-control fixture, two original physical policies',case_count=2)
print('Checkers copied/generated; four frozen specs saved. Freeze tree counts after --plan before execution.')
