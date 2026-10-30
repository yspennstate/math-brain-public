from pathlib import Path
from fractions import Fraction as Q
import json,time,hashlib

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out';OUT.mkdir(exist_ok=True)
spec={'helper':'A041-overlap-v1','family':'actual two-weight threshold 2*1{w N_A+N_B>=t}-1','domain':{'group_sizes':[[2,2],[2,3],[3,2],[3,3]],'weights':['1/2','1','2','3'],'thresholds':'all positive half-integers through max score','bias_profiles':['all 1/2','all 1/4','all 3/4','periodic 1/4,1/2,3/4']},'case_count':840,'symmetry':'none; labeled product biases','arithmetic':'Fraction, exact rational','memory_estimate_MB':100,'maximum_runtime_seconds':60,'targets':['Z_star<=D','pointwise K_star>=P','sum min(K_A,K_B)>=M'],'source':'own stage5 function definitions only; source hash pinned below'}
src=ROOT.parent/'20261014T083216Z-fleet05-A041-weighted-threshold-fei/code/check_stage.py'
source=src.read_text(encoding='utf-8');spec['source_sha256']=hashlib.sha256(source.encode()).hexdigest()
(OUT/'FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
namespace={'__file__':str(__file__)}
exec(compile(source.split('parser=')[0],str(src),'exec'),namespace)
transform=namespace['transform'];reference=namespace['reference']
start=time.monotonic();rows=[];counter={};maximum=(Q(0),None);checks=0
for h,b in ((2,2),(2,3),(3,2),(3,3)):
 for w in (Q(1,2),Q(1),Q(2),Q(3)):
  n=h+b
  profiles=[(Q(1,2),)*n,(Q(1,4),)*n,(Q(3,4),)*n,tuple((Q(1,4),Q(1,2),Q(3,4))[i%3] for i in range(n))]
  for p in profiles:
   for j in range(1,int(2*(w*h+b))+1):
    t=Q(j,2);vals=[2*int(w*(x&((1<<h)-1)).bit_count()+(x>>h).bit_count()>=t)-1 for x in range(1<<n)]
    _,P,v=transform(vals,p);KA,JA=reference(vals,p,h,'A');KB,JB=reference(vals,p,h,'B')
    mixed=lambda s:bool(s&((1<<h)-1)) and bool(s>>h)
    M=sum(z for s,z in enumerate(P) if mixed(s));D=sum((s.bit_count()-1)*z for s,z in enumerate(P) if mixed(s))
    K=[max(a,c) for a,c in zip(KA,KB)];Z=sum(K);overlap=sum(min(a,c) for a,c in zip(KA,KB))
    assert Z<=D+M and M<=D;checks+=2
    rec={'h':h,'b':b,'w':str(w),'t':str(t),'p':list(map(str,p)),'M':str(M),'D':str(D),'Z':str(Z),'overlap':str(overlap),'P':list(map(str,P)),'K_A':list(map(str,KA)),'K_B':list(map(str,KB))}
    if D and Z/D>maximum[0]:maximum=(Z/D,rec)
    for name,bad in [('Z_le_D',Z>D),('K_ge_P',any(K[s]<P[s] for s in range(len(P)) if mixed(s))),('overlap_ge_M',overlap<M)]:
     if bad and name not in counter:counter[name]=rec
    if len(rows)<10:rows.append(rec)
    if time.monotonic()-start>60:raise RuntimeError('frozen 60-second cap')
count=0
for h,b in ((2,2),(2,3),(3,2),(3,3)):
 for w in (Q(1,2),Q(1),Q(2),Q(3)):count+=4*int(2*(w*h+b))
result={'helper':spec['helper'],'cases':count,'assertions':checks,'runtime_seconds':time.monotonic()-start,'max_Z_over_D':str(maximum[0]),'max_fixture':maximum[1],'counterexamples':counter,'sample':rows}
(OUT/'OVERLAP_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('max_fixture','counterexamples','sample')}))
print('counterexamples',list(counter))
