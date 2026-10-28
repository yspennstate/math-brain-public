from pathlib import Path
import json,math,time
R=Path(__file__).resolve().parents[1];t0=time.perf_counter();maxratio=(0,None);minimum=(1e9,None)
def fw(a):
 a=list(a);h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
for phase in range(65536):
 a=fw([1-2*((phase>>s)&1) for s in range(16)]);p=[x*x/256 for x in a]
 H=-sum(x*math.log2(x) for x in p if x);I=sum(x*j.bit_count() for j,x in enumerate(p));gap=4*I-H
 if I and H/I>maxratio[0]:maxratio=(H/I,phase)
 if gap<minimum[0] and I:minimum=(gap,phase)
 assert time.perf_counter()-t0<55
out={'status':'NUMERICAL_EVIDENCE_ONLY','cases':65536,'max_H_over_I':maxratio,'minimum_nonconstant_4I_minus_H':minimum,'seconds':time.perf_counter()-t0}
(R/'out').mkdir(exist_ok=True);(R/'out/PILOT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
