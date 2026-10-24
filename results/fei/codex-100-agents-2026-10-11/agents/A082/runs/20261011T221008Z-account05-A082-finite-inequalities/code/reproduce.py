"""Independent butterfly Walsh and outward fixed-denominator log bounds."""
import json,time,hashlib
from pathlib import Path
from fractions import Fraction as Q
ROOT=Path(__file__).resolve().parents[1]
SCALE=1<<100
def ln_interval(r):
    z=(r-1)/(r+1);term=z;v=Q(0)
    for j in range(40):v+=term/Q(2*j+1);term*=z*z
    return 2*v,2*v+2*term/(81*(1-z*z))
L2,U2=ln_interval(Q(2))
def log_interval(m):
    k=m.bit_length()-1;l,u=ln_interval(Q(m,1<<k))
    lo=Q(k)+l/U2;hi=Q(k)+u/L2
    return (lo*SCALE).__floor__(),(hi*SCALE).__ceil__()
def factor(m):
    out=[]
    for p in range(2,m+1):
        if m%p:continue
        e=0
        while m%p==0:m//=p;e+=1
        out.append((p,e))
        if m==1:break
    return out
logs={p:log_interval(p) for p in range(2,513) if factor(p)==[(p,1)]}
def transform(vals):
    a=vals[:]
    for level in range((len(a)).bit_length()-1):
        b=1<<level
        for start in range(0,len(a),b*2):
            left=a[start:start+b];right=a[start+b:start+2*b]
            a[start:start+b]=[x+y for x,y in zip(left,right)]
            a[start+b:start+2*b]=[x-y for x,y in zip(left,right)]
    return a
def diff_vector(squares,bit,D):
    v={2:-8*D,3:9*D,5:-5*D}
    for s in range(len(squares)):
        if s&bit:continue
        a,b=squares[s],squares[s|bit]
        if a==0 or b==0:continue
        for m,c in [(a+b,2*(a+b)),(a,-2*a),(b,-2*b)]:
            for p,e in factor(m):v[p]=v.get(p,0)+c*e
    return {p:c for p,c in v.items() if c}
def run(n):
    N=1<<n;chosen=(ROOT/'out'/f'selection_n{n}.bin').read_bytes()
    assert len(chosen)==1<<(N-1)
    strict=equal=constant=0;max_upper=None;t=time.perf_counter()
    for k,i in enumerate(chosen):
        g=k^(k>>1);vals=[1]+[-1 if g&(1<<(x-1)) else 1 for x in range(1,N)]
        a=transform(vals);squares=[x*x for x in a]
        assert sum(squares)==N*N
        if i==255:
            assert all(x==vals[0] for x in vals);constant+=1;continue
        assert i<n;bit=1<<i
        boundary=sum(vals[x]!=vals[x^bit] for x in range(N));D=N*boundary
        assert D>0 and D==sum(squares[s] for s in range(N) if s&bit)
        v=diff_vector(squares,bit,D)
        if not v:equal+=1;continue
        upper=sum(c*(logs[p][1] if c>0 else logs[p][0]) for p,c in v.items())
        assert upper<0,(n,k,i,v,upper)
        strict+=1;max_upper=upper if max_upper is None else max(max_upper,upper)
    return {'n':n,'cases':len(chosen),'strict_selected':strict,'equal_selected':equal,'constants':constant,'maximum_strict_difference_upper_numerator':max_upper,'log_denominator':str(SCALE),'selection_sha256':hashlib.sha256(chosen).hexdigest(),'elapsed_seconds':time.perf_counter()-t}
if __name__=='__main__':
    t=time.perf_counter();out={'status':'PASS','method':'independent physical boundaries + butterfly + rational intervals','log_terms':40,'log_rounding_denominator':str(SCALE),'results':[]}
    for n in [1,2,3,4]:
        r=run(n);out['results'].append(r);print(json.dumps(r),flush=True)
    out['elapsed_seconds']=time.perf_counter()-t
    (ROOT/'out'/'independent_reproduction.json').write_text(json.dumps(out,indent=2))
