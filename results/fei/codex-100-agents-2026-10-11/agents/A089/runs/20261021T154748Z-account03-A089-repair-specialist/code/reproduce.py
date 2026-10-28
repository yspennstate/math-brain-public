"""Independent A+gB packet spectrum; direct DFT, no mixed-bias outer helper."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json,time
from arithmetic import Q,log2,scale,plus,ceildiv
ROOT=Path(__file__).resolve().parents[1]
tests=0
def ck(x):
    global tests
    assert x;tests+=1
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def C(x):return scale((Q,Q),F(x))
def avg(xs):
    z=(0,0)
    for x in xs:z=plus(z,x)
    return scale(z,F(1,len(xs)))
def mul(a,b):
    v=[x*y for x in a for y in b];return min(v)//Q,ceildiv(max(v),Q)
def div(a,b):
    ck(b[0]>0);v=[F(x*Q,y) for x in a for y in b]
    return min(v).__floor__(),max(v).__ceil__()
def ent(ps):
    z=(0,0)
    for p in ps:
        ck(p>=0)
        if p:z=plus(z,scale(log2(1/p),p))
    return z
def dft(t):
    return [sum(F(v*(-1 if (x&s).bit_count()%2 else 1),len(t)) for x,v in enumerate(t)) for s in range(len(t))]
def child(t,i,b):
    return tuple(t[(x%2**i)+2**(i+1)*(x//2**i)+2**i*b] for x in range(len(t)//2))
G=tuple(-1 if x<3 else 1 for x in range(64))
H=tuple(-1 if x in {0,1,2,4,8,16,32,6,17,40} else 1 for x in range(64))
J=tuple(-H[x^1] for x in range(64))
@lru_cache(None)
def core(t):
    co=dft(t);ps=[x*x for x in co];ck(sum(ps)==1)
    I=sum(F(s.bit_count())*p for s,p in enumerate(ps))
    n=(len(t)-1).bit_length()
    edges=[F(sum(t[x]!=t[x^2**i] for x in range(len(t))),len(t)) for i in range(n)]
    ck(sum(edges)==I)
    return co[0],ent(ps),I,edges
mu,hg,ig,_=core(G);v=1-mu*mu
ag=dft([F(J[2*x]+J[2*x+1],2) for x in range(32)])
bg=dft([F(J[2*x]-J[2*x+1],2) for x in range(32)])
AB=[]
for T in range(32):
    aa=sum(ag[U]*mu**((U^T).bit_count()) for U in range(32) if U&T==T)
    bb=sum(bg[U]*mu**((U^T).bit_count()) for U in range(32) if U&T==T)
    AB.append((T,aa,bb,v**T.bit_count()))
q=sum(w*b*b for T,a,b,w in AB)
ck(q>0)
hcond=scale(sub(hg,ent([v,1-v])),1/v)
icond=ig/v
@lru_cache(None)
def profile(t):
    m,h,I,ds=core(t);vv=1-m*m
    empty=[w*(a+m*b)**2 for T,a,b,w in AB]
    active=[w*b*b*vv for T,a,b,w in AB]
    ck(sum(empty+active)==1)
    totalH=ent(empty+active)
    otherweight=sum((empty[j]+active[j])*T.bit_count() for j,(T,a,b,w) in enumerate(AB))
    totalH=plus(totalH,scale(hcond,otherweight))
    totalH=plus(totalH,scale(sub(h,ent([vv,1-vv])),q))
    totalI=otherweight*icond+q*I
    U=scale(sub(C(4*I),h),q);S=sub(C(4*totalI),totalH);M=sub(S,U)
    return {'H':totalH,'I':totalI,'U':U,'M':M,'S':S,'d':ds,'truth':t}
def query(p,i):
    cs=[profile(child(p['truth'],i,b)) for b in [0,1]]
    dd=q*p['d'][i];ck(p['I']-(cs[0]['I']+cs[1]['I'])/2==dd)
    return cs,sub(sub(p['H'],avg([x['H'] for x in cs])),C(4*dd))
def overlap(x,y):ck(x[0]<=y[1] and y[0]<=x[1])
def main():
    start=time.perf_counter();root=profile(G);first,e1=query(root,2);second,e2=query(first[0],0)
    old=scale(e1,F(2));B2=avg([x['U'] for x in second]);total=plus(old,e2)
    records=json.loads((ROOT/'out/REPAIRED_CASES.json').read_text(encoding='utf-8'));checked=[]
    for row in records:
        b=row['second_bit'];i=[1,3,4,5].index(row['third_original_coordinate']);p=second[b]
        incoming=mul(div(total,B2),p['U']);children,e=query(p,i);T=plus(incoming,e)
        Vs=[];Ws=[]
        for k,c in enumerate(children):
            M=c['M'];V=sub(c['U'],(max(0,-M[1]),max(0,-M[0])))
            W=(max(0,M[0]),max(0,M[1]));ck(V[0]>=0);ck(W[0]>=0)
            overlap(V,row['corrected_selected_V'][k]);overlap(W,row['other_positive_W'][k]);Vs.append(V);Ws.append(W)
        B=avg(Vs);W=avg(Ws);need=sub(T,B);tau=(max(0,need[0]),max(0,need[1]))
        overlap(T,row['old_plus_new_T']);overlap(tau,row['minimal_transfer_tau']);ck(sub(W,tau)[0]>0)
        if b==0:
            ck(need[0]>0);ratio=div(tau,W);ck(ratio[0]*4>Q);ck(ratio[1]*50<13*Q)
        else:ck(need[1]<0)
        checked.append({'b':b,'i':row['third_original_coordinate'],'T':T,'tau':tau,'B':B,'W':W})
    out={'version':'A-plus-gB-direct-DFT-v1','independent_cases':len(checked),'exact_assertions':tests,
      'runtime_seconds':time.perf_counter()-start,'failed':0,'cases':checked}
    ck(out['runtime_seconds']<55)
    (ROOT/'out/INDEPENDENT_REPRODUCTION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
if __name__=='__main__':main()
