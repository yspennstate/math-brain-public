from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];old=R.parent/'20261014T014813Z-account05-A017-recursive-addressing'
v=(old/'code/validate6.py').read_text(encoding='utf8')
v=v.replace('A017-six-edit-tree-v1','A017-eight-edit-tree-v1').replace('edits<=6','edits<=8')
v=v.replace('min(6,len(K))','min(8,len(K))')
v=v.replace('4+U.log_interval(6)[0]','7')
v=v.replace("i=active[0] if active else polar[0];nodes+=1;B=U.erasure(sp,n,i)","""if not active and n==5 and edits==7 and polar:
  good=[j for j in polar if inf[j]>=F(3,16)]
  if not good:
   # Verify the actual algebraic terminal in unchanged physical coordinates.
   req(all(inf[j]==F(1,16) for j in polar),'all-weak lattice')
   W=U.fwht(g);req(sorted(w*w for w in W)==[4]*31+[900],'actual point-defect character spectrum')
   nonnegative(U.LF(4*sum(inf)).add(H,-1),'collapsed retained terminal')
   leaves+=1;return F(0),sum(inf)
  i=good[0]
 else:i=active[0] if active else polar[0]
 nodes+=1;B=U.erasure(sp,n,i)""")
# Add the two mandatory fixtures and include exactly seven-edit prefixes too.
v=v.replace('tuple(K[:min(3,len(K))])','tuple(K[:min(7,len(K))])')
v=v.replace('def tree(g,b,labels,ids,Q):',"""def fixtures():
 E=(7,11,15,19,23,27,31)
 return [(5,[],U.poly_code(5,[(0,1),(1,2),(3,4)]),E),(5,[],U.poly_code(5,[(0,1)]),E)]

def tree(g,b,labels,ids,Q):""")
v=v.replace('for c in configs(a.pilot):root(*c);roots+=1','for c in list(configs(a.pilot))+fixtures():root(*c);roots+=1')
v=v.replace('min(6,1<<n)','min(8,1<<n)').replace('range(1,16),5','range(1,16),7').replace('for s in [4,5,6]','for s in [7,8]')
v=v.replace('tree6_pilot.json','tree8_pilot.json').replace('tree6_validation.json','tree8_validation.json')
v=v.replace('pilot_roots=sum(1 for x in configs(True))','pilot_roots=sum(1 for x in configs(True))+2').replace('full_roots=sum(1 for x in configs())','full_roots=sum(1 for x in configs())+2')
(R/'code/tree8.py').write_text(v,encoding='utf8')
for name in ['critical.py','ternary.py','seven.py']:
 (R/'code'/name).write_bytes((old/'code'/name).read_bytes())
def spec(name,**kw):
 p=R/'code'/name
 data=dict(helper=name,helper_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),arithmetic='integer Walsh, rational edge energies, exact prime-log forms with proved rational log enclosures; no floating verdict',memory_estimate_MB=100,max_runtime_seconds=180,symmetry='explicitly stated only; no physical influence relabeling',**kw)
 (R/'out'/(p.stem+'_FROZEN_SPEC.json')).write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
spec('collapse.py',family='all rank-two quadratic all-weak seven-edit cases on five physical controls, all radical cosets, omitted points and allowed linear parts',domain='155 polar matrices, 4 cosets of size 8, 8 omissions, all linear parts on zero polar rows',pilot_case_count=640,full_case_count=13120,max_pilot_runtime_seconds=60)
spec('critical.py',family='generic D4 selected Boolean coordinate with one pivotal edge',domain='128 normalized three-bit child tables',case_count=128)
spec('ternary.py',family='generic D5 selected Boolean coordinate with two pivotal edges',domain='3^7 ternary projected child tables',case_count=2187)
spec('seven.py',family='unchanged fixed-order seven-edit obstruction and repaired order',domain='one five-control fixture, two physical policies',case_count=2)
print('Setup and four frozen specs saved. Tree counts must be frozen after --plan before execution.')
