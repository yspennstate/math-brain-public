import json,time,hashlib
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
def factors(m):
    d={};p=2
    while p*p<=m:
        while m%p==0:d[p]=d.get(p,0)+1;m//=p
        p+=1
    if m>1:d[m]=d.get(m,0)+1
    return d
F={m:factors(m) for m in range(1,513)}
def vector(sq,i):
    bit=1<<i;D=sum(x for s,x in enumerate(sq) if s&bit)
    c=Counter({2:-8*D,3:9*D,5:-5*D})
    for s,u in enumerate(sq):
        if s&bit:continue
        v=sq[s|bit]
        if not u or not v:continue
        for m,mul in ((u+v,2*(u+v)),(u,-2*u),(v,-2*v)):
            for p,e in F[m].items():c[p]+=mul*e
    return D,{p:e for p,e in c.items() if e}
def sign(c):
    lhs=rhs=1
    for p,e in c.items():
        if e>0:lhs*=p**e
        else:rhs*=p**(-e)
    return (lhs>rhs)-(lhs<rhs)
def run(n):
    N=1<<n;old=0;a=[N]+[0]*(N-1);chosen=bytearray();eq_cases=[];checks=0
    signs=[[(-1)**((s&x).bit_count()%2) for s in range(N)] for x in range(N)]
    t=time.perf_counter()
    for k in range(1<<(N-1)):
        g=k^(k>>1)
        if k:
            x=(g^old).bit_length();delta=-2 if g&(1<<(x-1)) else 2
            a=[u+delta*v for u,v in zip(a,signs[x])]
        old=g;sq=[x*x for x in a]
        assert sum(sq)==N*N;checks+=1
        outcomes=[]
        for i in range(n):
            D,c=vector(sq,i)
            if D:outcomes.append((sign(c),i));checks+=1
        if not outcomes:chosen.append(255);continue
        acceptable=[i for s,i in outcomes if s<=0]
        assert acceptable,(n,k,g,outcomes)
        chosen.append(acceptable[0])
        if min(s for s,i in outcomes)==0:eq_cases.append({'gray_index':k,'truth_mask':g})
    path=ROOT/'out'/f'selection_n{n}.bin';path.write_bytes(chosen)
    return {'n':n,'cases':len(chosen),'exact_checks':checks,'sharp_cases':len(eq_cases),'first_sharp_cases':eq_cases[:8], 'selection_sha256':hashlib.sha256(chosen).hexdigest(),'elapsed_seconds':time.perf_counter()-t}
if __name__=='__main__':
    (ROOT/'out').mkdir(exist_ok=True);t=time.perf_counter();results=[]
    for n in [1,2,3,4]:
        r=run(n);results.append(r);print(json.dumps(r),flush=True)
        (ROOT/'out'/'exact_partial.json').write_text(json.dumps(results,indent=2))
    # 2*Kstar < 107/20 iff 160+100 log5-180 log3 <107.
    assert 2**53*5**100<3**180
    out={'status':'PASS','target':'B_i <= Kstar I_i','Kstar_symbolic':'4+(5/2)log2(5)-(9/2)log2(3)','rational_upper_bound':'107/40','rational_upper_bound_integer_certificate':'2^53 * 5^100 < 3^180','results':results,'elapsed_seconds':time.perf_counter()-t}
    (ROOT/'FINITE_INEQUALITY_CERTIFICATE.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
