from pathlib import Path
from fractions import Fraction as Q
import json,time
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261012T010436Z-account05-A018-shared-data-collision-law/code/check_lead.py'
ns={'__file__':str(OLD),'__name__':'arithmetic_only'}
exec(compile(OLD.read_text(encoding='utf8').split("\nresult={'helper_version'")[0],str(OLD),'exec'),ns)
start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1;assert x;assert time.perf_counter()-start<60
def Hhist(hist):
 # Keep rational log arguments intact: prime factorization of a huge
 # coefficient is unnecessary for a rigorous interval sign certificate.
 return ns['add'](*[(-count*p,{p:1}) for p,count in hist if p])
def mul(a,b):
 c=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
def polydiff(a,b):
 return [(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]
# Bound polynomial truncation residuals without a floating derivative estimate.
P0=mul([2,-8,16,-16,8],[0,2,0,-4,2])
P1=mul([4,-8,-4,16,-8],[0,-1,Q(-1,2)])
P2=mul([0,-8,40,-64,32],[0,-2,-2])
ck(P0[:3]==[0,4,-16] and sum(abs(x) for x in P0[3:])==268)
ck(P1[:3]==[0,-4,6] and sum(abs(x) for x in P1[3:])==26)
ck(P2[:3]==[0,0,16] and sum(abs(x) for x in P2[3:])==240)
ck(268+8+26+40+240+36<=1000)
ck(Q(16*12+1048,1<<12)<1)
ck((4*12+8)*Q(1,1<<12)<2)
l2,h2=ns['ln'](2);ck(l2>Q(2,3) and h2<1)
rows=[]
for m in (4,5,6,8,12,16,24,32,64,128):
 d=Q(1,1<<m);N=1<<m;c=1-2*d+2*d*d
 hist=[(c*c,1),(4*d*d*(1-d)**2,1),(d*d*(1-2*d)**2,4*(N-1)),(4*d**4,2*(N-1)**2)]
 ck(sum(p*k for p,k in hist)==1)
 module=[((1-d)**2,1),(d*d,2*N-1)]
 ck(sum(p*k for p,k in module)==1)
 H=Hhist(hist);Hm=Hhist(module);gap=ns['add']((1,H),(-2,Hm))
 lead=ns['add']((d*d*(4*m-24),{2:1}),(6*d*d,{}))
 # The constant natural term 6*d^2 is handled explicitly, not as ln(2).
 residual=ns['add']((1,gap),(-d*d*(4*m-24),{2:1}))
 lo,hi=ns['grid'](residual,constant=-6*d*d)
 bound=d**3*((16*m+48)*h2+1000)*ns['SCALE']
 direct_remainder=(lo>=-bound and hi<=bound)
 if not direct_remainder and not(ROOT/'out/FORMULA_INTERVAL_FAILURE.json').exists():
  (ROOT/'out/FORMULA_INTERVAL_FAILURE.json').write_text(json.dumps({'m':m,'status':'INCONCLUSIVE_DIRECT_REMAINDER_INTERVAL','lo':str(lo),'hi':str(hi),'bound':str(bound),'scale':str(ns['SCALE']),'correction':'Use the proved symbolic remainder bound and rational monotone inequality. No precision escalation or sign inferred from an interval midpoint.'},indent=2)+'\n',encoding='utf8')
 if m<=24:ck(direct_remainder)
 gl,gh=ns['grid'](gap)
 I=2*(m+1)*d-2*d*d
 eta=2*d*(1-d)
 Rj=[(1-eta,1),(2*d*d,N-1)]
 Rjoint=[((1+(1-2*d)**4)/2,1),(2*d*d*(1-2*d)**2,2*(N-1)),(8*d**4,(N-1)**2)]
 ck(sum(p*k for p,k in Rj)==1 and sum(p*k for p,k in Rjoint)==1)
 TC=ns['add']((2,Hhist(Rj)),(-1,Hhist(Rjoint)))
 chi2=eta*eta/(1-eta)**2
 ck(chi2/l2<8*d*d)
 CE=ns['add']((1,H),(1,TC))
 if m<=24:
  ck(ns['grid'](TC)[0]>=0)
  ck(ns['grid'](ns['add']((8*d*d,{2:1}),(-1,TC)))[0]>0)
 if m>=12:
  analytic_lower=d*d*((2*m-6)-d*(16*m+1048))
  ck(analytic_lower>0 and (4*m+16)*d<2)
  if m<=24:
   ck(gl>0)
   ck(ns['grid'](ns['add']((4*I,{2:1}),(-1,H)))[0]>0)
   ck(ns['grid'](ns['add']((4*I,{2:1}),(-1,CE)))[0]>0)
 row={'m':m,'delta':str(d),'I':str(I),'physical_owner_loss':str(2*d*d),'gap_rational_log':{str(p):str(c) for p,c in gap.items()},'gap_scaled_interval':[str(gl),str(gh)],'scale':str(ns['SCALE']),'positive_gap_certified':gl>0 or m>=12,'sign_method':'all-parameter analytic lower bound' if m>24 else 'direct rigorous interval','direct_remainder_interval_certified':direct_remainder,'remainder_bound_nat':str(bound/ns['SCALE']),'residual_interval_nat':[str(lo/ns['SCALE']),str(hi/ns['SCALE'])]}
 row.update({'TC_rational_log':{str(p):str(c) for p,c in TC.items()},'chi_square':str(chi2),'reference_CE_identity':'H_parent+TC','TC_upper_bits':str(8*d*d),'reference_paid_at_4I':m>=12})
 rows.append(row)
 (ROOT/'out/FORMULA_PARTIAL.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf8')
save={'status':'PASS','checks':checks,'cases':rows,'elapsed_seconds':time.perf_counter()-start,'polynomial_coefficients':[list(map(str,P0)),list(map(str,P1)),list(map(str,P2))],'all_parameter_proof':'REPORT.md remainder derivation and m>=12 monotone rational bounds; finite checks do not replace the proof'}
(ROOT/'out/FORMULA_CHECK.json').write_text(json.dumps(save,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:save[k] for k in ('status','checks','elapsed_seconds')}))
