from pathlib import Path
import json,time,hashlib
p=Path(__file__).with_name('check_flat.py')
exec(compile(p.read_text(encoding='utf-8').split('cases=0;coords=0')[0],str(p),'exec'))
start=time.monotonic();checks=0;functions=queries=fibers=0
for n in range(4):
 N=1<<n
 for code in range(1<<N):
  v=tuple(1 if code>>x&1 else -1 for x in range(N));functions+=1
  a=tuple(Q(sum(v[x]*((-1)**((x&s).bit_count()%2)) for x in range(N)),N) for s in range(N))
  for i in range(n):
   d=sum(a[s]**2 for s in range(N) if s>>i&1)
   eq(d,Q(sum(v[x]!=v[x^(1<<i)] for x in range(N)),N))
   direct=add(*(L(a[s],a[s^(1<<i)]) for s in range(N) if not s>>i&1))
   eq(direct,erasure(v,i));queries+=1
   for T in range(N):
    if T>>i&1:continue
    aa,b=a[T],a[T^(1<<i)];A=1-d-aa*aa;D=d-b*b
    le(Q(0),A);le(Q(0),D);le(abs(b),d)
    C=sum(abs(a[s]*a[s^(1<<i)]) for s in range(N) if s!=T and not s>>i&1)
    le(C*C,A*D)
    rest=add(direct,sc(L(aa,b),-1));le(sign(add(rest,const(-2*C))),0)
    fibers+=1
  if time.monotonic()-start>60:raise TimeoutError('frozen cap')
eq(functions,278);eq(queries,804);eq(fibers,3140)
f=compose((-1,1),(-1,1));_,_,_,_,B=split(f,0)
eq(sign(B),1)
a=tuple(Q(x,len(f)) for x in fwht(f));d=sum(a[s]**2 for s in range(len(f)) if s&1)
eq((1-d-a[0]**2)*(d-a[1]**2)>0,True)
out={'status':'PASS','functions':functions,'coordinate_queries':queries,'distinguished_fibers':fibers,'positive_controls':1,'exact_assertions':checks,'runtime_seconds':time.monotonic()-start,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'flat_helper_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'sqrt_arithmetic':'Cauchy bound checked by squaring exact nonnegative rational half energies; no approximate square roots'}
save('WITNESS.json',out);print(json.dumps(out))
