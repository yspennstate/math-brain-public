from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, permutations
import json,sys,time
R=Path(__file__).resolve().parents[1]
SRC=R.parents[2]/'A012'/'runs'/'20261023T010946Z-fleet03-A012-sparse-activation-accounting'
O=1<<64;CHECKS=0
def ck(v):
    global CHECKS
    assert v,CHECKS;CHECKS+=1
def save(n,d):
    (R/'out').mkdir(exist_ok=True)
    (R/'out'/n).write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
def ch(s,t):return 1-2*((s&t).bit_count()%2)
def fw(v):
    a=list(v);h=1
    while h<len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a
@lru_cache(maxsize=10000)
def ln(z):
    assert 1<=z<=2
    u=(z-1)/(z+1);w=u;sm=F(0)
    for j in range(32):sm+=2*w/(2*j+1);w*=u*u
    return sm,sm+2*w/(65*(1-u*u))
LL,LH=ln(F(2))
@lru_cache(maxsize=10000)
def loghi(n,d):
    x=F(n,d);assert x>=1;k=0
    while x>=2:x/=2;k+=1
    hi=ln(x)[1]/LL+k;q=hi*O
    return -(-q.numerator//q.denominator)
def seed(job,D):
    high={0:(),1:(1,),2:(1,2),3:(0,),4:(0,1)}[job]
    lo=[D//2 if j in high else 0 for j in range(8)]
    return tuple(lo),tuple(x+D//2 for x in lo)
def cover(job):
    start=time.perf_counter();before=CHECKS
    d=json.loads((SRC/'out'/f'CONTINUUM_{job}.json').read_text(encoding='utf-8'))
    ck(d['status']=='PASS' and not d['unresolved'] and d['denominator']==128)
    D=128;nodes={};c=[-1]+[1]*7;a=fw(c)
    M=[[c[s]*ch(s,t) for s in range(8)] for t in range(8)]
    for label in ('leaves','pruned','splits'):
        for lo,hi,v in d[label]:
            key=tuple(lo),tuple(hi);ck(key not in nodes);ck(len(lo)==len(hi)==8)
            ck(all(0<=lo[j]<hi[j]<=D for j in range(8)));nodes[key]=(label,v)
    todo=[seed(job,D)];seen=set();mingap=None;corners=0
    while todo:
        key=todo.pop();ck(key in nodes and key not in seen);seen.add(key);lo,hi=key;kind,v=nodes[key]
        if kind=='splits':
            ck(0<=v<8 and hi[v]-lo[v]>=2);mid=(hi[v]+lo[v])//2
            l=list(lo);h=list(hi);l[v]=h[v]=mid;todo.extend([(lo,tuple(h)),(tuple(l),hi)]);continue
        if kind=='pruned':
            ck((v=='rare' and 4*sum(hi)<=D) or (v=='moderate' and 3*sum(lo)>=4*D));continue
        sl=[]
        for t in range(8):
            b=sum(M[t][s]*(lo[s]+hi[s]) for s in range(8));aa=(2*D*a[t]-b)**2;bb=b*b
            r=F(1,4096) if not bb else F(4095,4096) if not aa else F(bb,aa+bb)
            lam=loghi(r.denominator,r.denominator-r.numerator);mu=loghi(r.denominator,r.numerator)
            ck(lam+mu>=2*O);sl.append((lam,mu))
        mx=None
        # Normalized corner probabilities; direct character sums, no author Gray recurrence.
        for bits in product((0,1),repeat=8):
            q=[hi[j] if bits[j] else lo[j] for j in range(8)];val=-16*D*O*sum(q)
            for t,(lam,mu) in enumerate(sl):
                b=sum(M[t][s]*q[s] for s in range(8))
                val+=lam*(D*a[t]-b)**2+(mu-2*O)*b*b
            mx=val if mx is None else max(mx,val);corners+=1
        ck(mx<0);gap=F(-mx,64*D*D*O);mingap=gap if mingap is None else min(mingap,gap)
        if time.perf_counter()-start>50:raise RuntimeError('50s cap; no PASS')
    ck(seen==set(nodes))
    save(f'COVER_{job}.json',dict(status='PASS',job=job,checks=CHECKS-before,nodes=len(nodes),leaves=len(d['leaves']),analytic=len(d['pruned']),corners=corners,min_gap=str(mingap),seconds=time.perf_counter()-start,arithmetic='exact Fraction32-term atanh with rational remainder;64-bit outward weights;direct256 corners'))
    print(json.dumps(dict(status='PASS',job=job,checks=CHECKS-before,seconds=time.perf_counter()-start)),flush=True)
    ln.cache_clear();loghi.cache_clear()
def classify():
    before=CHECKS;start=time.perf_counter();gl=[];types={};mult=[0]*5;moderate=0
    for u,v,w in permutations(range(1,8),3):
        im=[(u if s&1 else 0)^(v if s&2 else 0)^(w if s&4 else 0) for s in range(8)]
        if len(set(im))==8:gl.append(im)
    ck(len(gl)==168)
    for m in range(256):
        c=[1-2*((m>>s)&1) for s in range(8)];a=fw(c);nz=sum(x!=0 for x in a)
        ck(nz in (1,4,8));types[nz]=types.get(nz,0)+1
        if nz==8:
            witnesses=[(t,w,sg) for t in range(8) for w in range(8) for sg in (-1,1) if all(c[s]==sg*ch(s,t)*(-1 if s==w else 1) for s in range(8))]
            ck(len(witnesses)==1);ck(sorted(abs(x) for x in a)==[2]*7+[6])
    ck(types=={1:16,4:112,8:128})
    for flags in product((0,1),repeat=8):
        if sum(flags)>=3:ck(F(sum(flags),16)>F(1,6));moderate+=1;continue
        job=sum(flags[1:]) if not flags[0] else 3+sum(flags[1:]);target=seed(job,2)[0]
        ck(any(all(flags[im[s]]==target[s] for s in range(8)) for im in gl));mult[job]+=1
    ck(mult==[1,7,21,1,7] and moderate==219)
    lo,hi=ln(F(2));ck(lo>F(2,3) and hi<F(7,10));ck(F(5,4)**3<2)
    # e>1+1+1/2>9/4, so sqrt(e)*ln2>1. No rounded transcendental input.
    ck(F(1)+1+F(1,2)>F(9,4));ck(F(48,7)<4+2/hi)
    save('CLASSIFICATION.json',dict(status='PASS',checks=CHECKS-before,phase_counts=types,seed_multiplicities=mult,GL_maps=len(gl),moderate=moderate,seconds=time.perf_counter()-start))
@lru_cache(maxsize=20000)
def factors(n):
    out=[];p=2
    while p*p<=n:
        k=0
        while n%p==0:n//=p;k+=1
        if k:out.append((p,k))
        p+=1
    if n>1:out.append((n,1))
    return out
def logadd(out,w,x):
    if not w:return
    assert x>0
    for sign,n in ((1,x.numerator),(-1,x.denominator)):
        for p,k in factors(n):out[p]=out.get(p,F(0))+sign*k*w
def clean(a):return {p:v for p,v in a.items() if v}
def phi(a,b):
    o={}
    if a:logadd(o,a,(a+b)/a)
    if b:logadd(o,b,(a+b)/b)
    return clean(o)
def linear(*terms):
    o={}
    for w,s in terms:
        for p,v in s.items():o[p]=o.get(p,F(0))+w*v
    return clean(o)
def spec(v):return [F(x*x,len(v)**2) for x in fw(v)]
def B(p):
    n=len(p)//2;o={}
    for j in range(n):o=linear((1,o),(1,phi(p[j],p[j+n])))
    return o
def kl(p,q):
    o={}
    for x,y in zip(p,q):
        if x:ck(y>0);logadd(o,x,x/y)
    return clean(o)
def formula(c,q):
    n=len(c);a=[F(v,n) for v in fw(c)];b=[v/n for v in fw([c[j]*q[j] for j in range(n)])]
    d=sum(q)/n;o={2:2*d}
    for x,y in zip(a,b):
        if x:o=linear((1,o),(1,phi((x-y)**2,y*y)),(1,{2:-2*y*y}))
    return clean(o),a,b
def rank(seq):
    basis={}
    for x in seq:
        while x:
            j=x.bit_length()-1
            if j in basis:x^=basis[j]
            else:basis[j]=x;break
    return len(basis)
def affdim(v):
    s=[j for j,a in enumerate(fw(v)) if a]
    return rank([j^s[0] for j in s])
def fixtures():
    before=CHECKS;start=time.perf_counter();cases=0;updates=0
    phases=[0,1,2,3,4,5,6,7,16,17,18,19,20,21,22,23]
    for t,L in [(4,[1,6,12]),(5,[7,14,28]),(6,[1,22,45])]:
        n=2**t;ck(rank(L)==3)
        labels=[sum(((s&k).bit_count()%2)<<j for j,k in enumerate(L)) for s in range(n)]
        for m in phases:
            g=[1-2*((m>>s)&1) for s in range(8)]
            for shift in (0,1):
                c=[ch(s,shift)*g[labels[s]] for s in range(n)]
                for policy in range(4):
                    masks=[0 if policy==0 else 15 if policy==1 else (11*s+7*(s>>2)+3)&15 if policy==2 else (s^(s>>1)^5)&15 for s in range(n)]
                    q=[F(x.bit_count(),4) for x in masks];d=sum(q)/n
                    h=[c[s]*(1-2*((masks[s]>>v)&1)) for v in range(4) for s in range(n)]
                    p=spec(c*4+h);ph=spec(h);pg=spec(c*4);siga,a,b=formula(c,q)
                    ck(B(p)==siga);ck(sum(p[4*n:])==d)
                    ck(sum(x*i.bit_count() for i,x in enumerate(p))==(sum(x*i.bit_count() for i,x in enumerate(pg))+sum(x*i.bit_count() for i,x in enumerate(ph)))/2+d)
                    bar=[sum(q[s] for s in range(n) if labels[s]==y)/F(n,8) for y in range(8)]
                    ck(formula(g,bar)[0]==siga)
                    for u in range(8):
                        idx=shift
                        for j in range(3):
                            if u>>j&1:idx^=L[j]
                        ck(a[idx]==F(fw(g)[u],8))
                        ck(b[idx]==fw([g[y]*bar[y] for y in range(8)])[u]/8)
                    rho=sum(ph[n:]);rh=ph[:n]+[(x+rho/F(3*n))/2 for x in ph[n:]];Q=p[:]
                    for j in range(n,4*n):Q[j]=Q[j+4*n]=rh[j]/4
                    ck(sum(Q)==sum(rh)==1);ck(kl(p,Q)==linear((F(1,2),kl(ph,rh))))
                    # New exact physical quotient update law, both rank cases.
                    for i in range(t):
                        ei=1<<i;inside=rank(L+[ei])==3
                        alpha=next((u for u in range(8) if (L[0] if u&1 else 0)^(L[1] if u&2 else 0)^(L[2] if u&4 else 0)==ei),None)
                        ck(inside==(alpha is not None))
                        theta=[sum(q[s]*ch(s,ei) for s in range(n) if labels[s]==y)/F(n,8) for y in range(8)]
                        for val in range(2):
                            ss=[s for s in range(n) if ((s>>i)&1)==val];seen=sorted(set(labels[s] for s in ss))
                            ck(len(seen)==(4 if inside else 8));counts=[sum(labels[s]==y for s in ss) for y in seen];ck(len(set(counts))==1)
                            ck(affdim([c[s] for s in ss])<=3)
                            for y in seen:
                                actual=sum(q[s] for s in ss if labels[s]==y)/counts[0]
                                if inside:ck(ch(y,alpha)==(-1)**val);ck(actual==bar[y])
                                else:ck(actual==bar[y]+(-1)**val*theta[y])
                                updates+=1
                    cases+=1
                    if time.perf_counter()-start>50:raise RuntimeError('50s cap; no PASS')
    # Stale quotient counterexample: rank is retained but the row profile changes.
    L=[9,2,4];n=16;labels=[sum(((s&k).bit_count()%2)<<j for j,k in enumerate(L)) for s in range(n)]
    c=[-1 if labels[s]==0 else 1 for s in range(n)];h=[c[s]*(-ch(s,8)) for s in range(n)]
    ck(B(spec(c+h))=={2:F(1)})
    for v in range(2):
        cc=[c[s] for s in range(n) if (s>>3)&1==v];hh=[h[s] for s in range(n) if (s>>3)&1==v]
        ck(B(spec(cc+hh))=={});ck(affdim(cc)==3)
    save('FIXTURES.json',dict(status='PASS',checks=CHECKS-before,cases=cases,physical_row_update_checks=updates,seconds=time.perf_counter()-start,stale_quotient='parent B=1;both physical children B=0;affine rank3 retained',arithmetic='integer Walsh;Fraction;exact rational prime-log signatures'))
def transport():
    start=time.perf_counter();before=CHECKS;cases=0;rows=0
    for L in ([1],[3,6],[1,6,12],[1,2,4,8]):
        r=len(L);ck(rank(L)==r)
        W={0}
        for l in L:W|={x^l for x in list(W)}
        labels=[sum(((s&k).bit_count()%2)<<j for j,k in enumerate(L)) for s in range(16)]
        for policy in range(6):
            profiles=[[F(0)]*16,[F(1)]*16,
                [F(((11*s+7*(s>>2)+3)&15).bit_count(),4) for s in range(16)],
                [F(s&1) for s in range(16)],[F((s>>3)&1) for s in range(16)],
                [F(((s^(s>>1)^5)&15).bit_count(),4) for s in range(16)]]
            q=profiles[policy]
            for assignment in product((-1,0,1),repeat=4):
                A=sum((assignment[j]>=0)<<j for j in range(4));a=sum((assignment[j]==1)<<j for j in range(4));size=A.bit_count()
                subsets=[k for k in range(16) if k&~A==0];t=rank([w for w in W if w&~A==0])
                projected=[l&~A for l in L];ck(rank(projected)==r-t)
                ss=[s for s in range(16) if s&A==a];ys=sorted(set(labels[s] for s in ss));ck(len(ys)==2**(r-t))
                count=len(ss)//len(ys);ck(all(sum(labels[s]==y for s in ss)==count for y in ys))
                for y in range(2**r):
                    fiber=[s for s in range(16) if labels[s]==y];sub=[s for s in ss if labels[s]==y]
                    denom=F(len(sub),len(fiber));ck(denom in (0,F(1,2**(size-t))))
                    if not sub:continue
                    # All moments are from the SAME incoming profile q, no renewed source.
                    num=sum((-1)**((a&k).bit_count()%2)*sum(q[s]*ch(s,k) for s in fiber)/len(fiber) for k in subsets)
                    expected=num/F(2**t);actual=sum(q[s] for s in sub)/len(sub)
                    ck(expected==actual and 0<=actual<=1);rows+=1
                # Full-label cells: compatible fibers survive with the exact new density.
                pi=F(1,2**r);newpi=F(count,len(ss));ck(newpi==pi*2**t)
                positive=[y for y in range(2**r) if y.bit_count()%2==0];N=len(positive);Np=sum(y in positive for y in ys)
                ck(Np<=N)
                if 0<Np<len(ys):
                    oldroot=pi/(N+pi);newroot=newpi/(Np+newpi);ck(0<oldroot<=newroot<1)
                cases+=1
                if time.perf_counter()-start>50:raise RuntimeError('50s cap; no PASS')
    save('BLOCK_TRANSPORT.json',dict(status='PASS',checks=CHECKS-before,cases=cases,conditional_rows=rows,seconds=time.perf_counter()-start,arithmetic='Fraction conditional probabilities,GF2 ranks,exact Boolean-event Fourier expansion',meaning='Profile/label/root metadata only; no cost-free canonical reset or terminal-bank payment inferred'))
if __name__=='__main__':
    if sys.argv[1]=='cover':
        for j in map(int,sys.argv[2:]):cover(j)
    elif sys.argv[1]=='classify':classify();print(json.dumps({'status':'PASS','checks':CHECKS}))
    elif sys.argv[1]=='transport':transport();print(json.dumps({'status':'PASS','checks':CHECKS}))
    else:fixtures();print(json.dumps({'status':'PASS','checks':CHECKS}))
