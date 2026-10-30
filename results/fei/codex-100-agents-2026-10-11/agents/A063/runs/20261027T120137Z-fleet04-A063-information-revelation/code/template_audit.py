"""Frozen exact v1, widths <=(2,2), all physical cuts/orders/outcomes, no resets."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import math, json, time, hashlib, argparse
R=Path(__file__).resolve().parents[1]; START=time.monotonic(); L=512
checks=queries=0
def ck(b,msg):
    global checks
    checks+=1
    if not b: raise AssertionError(msg)
    if time.monotonic()-START>60: raise RuntimeError('frozen runtime limit exceeded')
@lru_cache(None)
def law(tab):
    a=list(tab); h=1
    while h<len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return tuple(F(x*x,len(a)**2) for x in a)
def exp_log_sum(weights,arguments):
    value=F(1)
    for w,v in zip(weights,arguments):
        if w:
            ck(v>0 and (L*w).denominator==1,'positive log and exact exponent')
            value*=v**int(L*w)
    return value
def kp(p,q): return exp_log_sum(p,[a/b if a else F(1) for a,b in zip(p,q)])
def hp(p): return exp_log_sum(p,[1/a if a else F(1) for a in p])
def insert(t,i,b): return (t&((1<<i)-1))|((t>>i)<<(i+1))|(b<<i)
def restrict(tab,i,b): return tuple(tab[insert(t,i,b)] for t in range(len(tab)//2))
def sqrtq(x):
    a,b=math.isqrt(x.numerator),math.isqrt(x.denominator)
    ck(a*a==x.numerator and b*b==x.denominator,'physical average exact rational root')
    return F(a,b)
def transition(tab,ref,i):
    p=law(tab); N=len(tab)//2
    pb=tuple(p[insert(t,i,0)]+p[insert(t,i,1)] for t in range(N))
    qb=tuple(ref[insert(t,i,0)]+ref[insert(t,i,1)] for t in range(N))
    out=[]; masses=[]
    for b in (0,1):
        child=restrict(tab,i,b); pc=law(child)
        raw=tuple(qb[t]*(pc[t]/(2*pb[t]) if pb[t] else F(1,2)) for t in range(N))
        mass=sum(raw); ck(mass>0,'positive actual reference branch')
        out.append((child,tuple(x/mass for x in raw))); masses.append(mass)
    ck(sum(masses)==1,'complete normalized reference outcomes')
    erasure=kp(p,ref)/kp(pb,qb); outcome=kp((F(1,2),F(1,2)),masses)
    ck(erasure>=1 and outcome>=1,'nonnegative E and O separately')
    ck(kp(p,ref)**2==(erasure*outcome)**2*math.prod(kp(law(t),q) for t,q in out),'full E/O/K chain')
    ck(hp(p)**2>=math.prod(hp(law(t)) for t,q in out),'physical Fourier-entropy supermartingale')
    return out,erasure*outcome,masses
@lru_cache(maxsize=12000)
def budget(tab,ref):
    global queries
    p=law(tab); ck(sum(ref)==1 and all(ref[i]>0 for i,a in enumerate(p) if a),'supported normalized inherited source')
    stop=kp(p,ref)*hp(p); best=stop
    for i in range(len(tab).bit_length()-1):
        queries+=1; out,fee,_=transition(tab,ref,i)
        value=fee*sqrtq(math.prod(budget(t,q) for t,q in out))
        ck(value<=stop,'all adaptive stopped continuations <= current full CE')
        best=max(best,value)
    return best
def family(a,b):
    d=1+a+b; U=((1<<a)-1)<<1; V=((1<<b)-1)<<(a+1)
    tab=tuple((-1)**((x&1)*((x&U).bit_count()%2)*((x&V).bit_count()%2)) for x in range(1<<d))
    masks={z0^z1^z2 for z0 in (0,1) for z1 in (0,U) for z2 in (0,V)}
    ref=tuple(F(1,2) if t==0 else F(1,14) if t in masks else F(0) for t in range(1<<d))
    return tab,ref,masks
def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--pilot',action='store_true'); args=parser.parse_args()
    widths=[(1,1)] if args.pilot else [(1,1),(1,2),(2,1),(2,2)]
    ck(14**28<2**107,'positive original reserve >1/64')
    ck(3**3<2**5,'original product same4I root obstruction')
    rows=[]
    for a,b in widths:
        tab,ref,masks=family(a,b); p=law(tab); d=1+a+b
        ck(p[0]==F(9,16) and all(p[t]==(F(1,16) if t in masks else 0) for t in range(1,1<<d)),'actual eight-atom Boolean spectrum')
        influences=tuple(sum(v for t,v in enumerate(p) if t>>i&1) for i in range(d))
        ck(influences==(F(1,4),)*d,'all original physical spectral influences')
        product=tuple(math.prod(v if t>>i&1 else 1-v for i,v in enumerate(influences)) for t in range(1<<d))
        original_ce=kp(p,ref)*hp(p)
        ck(original_ce==F(2**288*14**224),'explicit original template invoice')
        ck(kp(p,product)*hp(p)>2**(L*3*d//4),'product fails original oldquarter at root')
        ck(budget(tab,ref)==original_ce,'every physical query policy and stopping cut paid')
        out,fee,pi=transition(tab,ref,0)
        ck(pi==[F(16,35),F(19,35)],'actual selector reference outcome mismatch')
        sparse=out[1]; sp=law(sparse[0]); sr=sparse[1]
        ck(sr[0]==F(4,19) and sorted(v for t,v in enumerate(sr) if t)!=[],'non-source-equal sparse incoming law')
        ck(all(sr[t]==F(5,19) for t in range(1,len(sr)) if sp[t]),'three sparse inherited nonvacuum atoms')
        ck(sr!=sp and kp(sp,sr)>1,'positive inherited sparse source KL')
        if a+b>2:
            ck(F(2**(L*(a+b-2)))/kp(sp,sr)>1,'positive optional sparse product-admission bill deferred')
        rows.append({'widths':[a,b],'original_I':str(F(d,4)),'selector_pi':[str(v) for v in pi],
                     'rank_deficient_non_source_equal':a+b>2,'all_cuts_paid':True})
    result={'status':'PASS','assertions':checks,'query_states':queries,'states':budget.cache_info().currsize,
            'cases':rows,'elapsed_seconds':time.monotonic()-START,
            'arithmetic':'Fraction, integer Walsh, exact rational exponentiated CE/KL; no floating log decisions',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (R/'out').mkdir(exist_ok=True)
    (R/'out'/('pilot.json' if args.pilot else 'main.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__': main()
