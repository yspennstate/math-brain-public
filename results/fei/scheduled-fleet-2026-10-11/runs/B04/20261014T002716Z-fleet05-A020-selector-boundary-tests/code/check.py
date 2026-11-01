from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import argparse,json,time,itertools
ROOT=Path(__file__).resolve().parents[1]
def walsh(v):
    v=list(v);h=1
    while h<len(v):
        for i in range(0,len(v),2*h):
            for j in range(i,i+h):a,b=v[j],v[j+h];v[j],v[j+h]=a+b,a-b
        h*=2
    return v
def direct(v):return [sum(a*(-1)**((x&s).bit_count()) for x,a in enumerate(v)) for s in range(len(v))]
def edges(v,i):return Q(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v))
def energy(v):
    w=walsh(v);return sum((Q(w[s]**2*s.bit_count(),len(v)**2) for s in range(len(v))),Q(0))
@lru_cache(None)
def logint(n):
    e=n.bit_length()-1;t=Q(n,1<<e)
    def series(z):
        p=sum((2*z**(2*j+1)/Q(2*j+1) for j in range(40)),Q(0))
        return p,p+2*z**81/(81*(1-z*z))
    l,h=series((t-1)/(t+1));a,b=series(Q(1,3));return l+e*a,h+e*b
def lograt(q):
    a,b=logint(q.numerator);c,d=logint(q.denominator);return a-d,b-c
def entr(weights):
    lo=hi=Q(0)
    for p in weights:
        if p:
            a,b=lograt(1/p);lo+=p*a;hi+=p*b
    return lo,hi
def erasure(p,i):
    lo=hi=Q(0)
    for s in range(len(p)):
        if s>>i&1:continue
        a,b=p[s],p[s|(1<<i)];q=a+b
        if a and b:
            l,h=entr([a/q,b/q]);lo+=q*l;hi+=q*h
    return lo,hi
def ANF_connected(v):
    p=[(1-x)//2 for x in v];n=(len(v)).bit_length()-1
    for i in range(n):
        for s in range(len(v)):
            if s>>i&1:p[s]^=p[s^(1<<i)]
    components=[{i} for i in range(n)]
    for s,a in enumerate(p):
        if a and s:
            variables={i for i in range(n) if s>>i&1};touch=[c for c in components if c&variables]
            merged=set().union(*touch);components=[c for c in components if c not in touch]+[merged]
    return len(components)==1
def family(k,r):
    shared=(1<<k)-1;v=[-1 if (x&shared)==shared and ((x>>k).bit_count()%2) else 1 for x in range(1<<(k+r))]
    return v
def case(k,r):
    delta=Q(1,1<<k);v=family(k,r);N=len(v);w=walsh(v);p=[Q(a*a,N*N) for a in w]
    expected=[];P=(1<<r)-1
    for s in range(N):
        if (s>>k) not in [0,P]:expected.append(Q(0))
        elif s==0:expected.append((1-delta)**2)
        else:expected.append(delta**2)
    assert p==expected and sum(p)==1
    influences=[edges(v,i) for i in range(k+r)]
    assert influences==[delta]*(k+r)
    assert all(sum(p[s] for s in range(N) if s>>i&1)==delta for i in range(k+r))
    assert ANF_connected(v)
    if k+r<=7:assert w==direct(v)
    J=r*delta;loss=k*(r-1)*delta;I=(r+k)*delta
    h=entr(p);l2,h2=logint(2)
    assert h[1] <= 4*I*l2
    # Exact-B at every reached shared-block prefix. All-zero/zero-containing
    # prefixes terminate constant; all-one prefixes are the same smaller core.
    margins=[]
    for ell in range(1,k+1):
        child=family(ell,r);ww=walsh(child);pp=[Q(a*a,len(child)**2) for a in ww]
        d=Q(1,1<<ell);blo,bhi=erasure(pp,0)
        assert bhi<4*d*l2
        margins.append(str(4*d*l2-bhi))
    return dict(k=k,r=r,n=k+r,private_influence=str(J),shared_influence=str(k*delta),total_influence=str(I),minimum_character_owner_loss=str(loss),loss_over_private=str(loss/J),loss_over_total=str(loss/I),entropy_nats_interval=[str(q) for q in h],reference='Q(0)=(1-2^-k)^2; Q(S)=2^-2k on every other set in shared subsets times {empty,all-private}; zero elsewhere',reference_normalized=True,root_connected=True,K4_bad_node_bill='0',K4_prefix_margin_nats_lower=margins)
def orientations():
    count=0
    for k in range(1,5):
        for r in range(1,4):
            d=Q(1,1<<k);minimum=None
            for mask in range(1<<(k*r)):
                loss=Q(0)
                for i in range(k):
                    c=sum((mask>>(j*k+i))&1 for j in range(r))
                    loss+=(r-1)*d+(c-(c%2))*(1-2*d)
                count+=1;minimum=loss if minimum is None else min(minimum,loss)
            assert minimum==k*(r-1)*d
    assert count==5050;return count
def owner_review():
    count=0
    for m0,m1 in itertools.product(range(16),repeat=2):
        raw=[[1-2*((m>>x)&1) for x in range(4)] for m in [m0,m1]]
        g=[];h=[];ds=[];Js=[];ks=[]
        for v in raw:
            a=[v[0],v[2]];b=[v[1],v[3]];d=Q(sum(x!=y for x,y in zip(a,b)),2)
            if d>Q(1,2):b=[-x for x in b];d=1-d
            g.append(a);h.append(b);ds.append(d);Js.append((edges(a,0)+edges(b,0))/2);ks.append(energy([Q(x-y,2) for x,y in zip(a,b)]))
        q=[1-2*d for d in ds];star=(1-q[0]*q[1])/2;J=sum(Js)
        loss=sum(ds)-star;assert 0<=loss<=J-star
        t=[(1-q[1-j])*Js[j]/2+q[1-j]*ks[j] for j in range(2)]
        A=[g[0][x&1]*g[1][x>>1] for x in range(4)];B=[h[0][x&1]*h[1][x>>1] for x in range(4)]
        D=[Q(a-b,2) for a,b in zip(A,B)]
        assert energy(D)==sum(t) and all(0<=a<=b for a,b in zip(t,Js));count+=1
    return dict(cases=count,status='PASS',scope='Independent arbitrary one-bit module pair owner/derivative check; all-r proof reconstructed in REPORT; no author checker imported')
def run(pilot):
    start=time.perf_counter();rows=[]
    domain=itertools.product(range(1,4),range(1,4)) if pilot else itertools.product(range(1,9),range(1,7))
    for k,r in domain:
        if time.perf_counter()-start>(60 if pilot else 120):raise RuntimeError('Frozen deadline')
        rows.append(case(k,r));(ROOT/'out'/('pilot.json' if pilot else 'family.json')).write_text(json.dumps(dict(cases=len(rows),rows=rows,runtime_seconds=time.perf_counter()-start),indent=2))
    if not pilot:
        write=dict(orientations=orientations(),owner_review=owner_review());(ROOT/'out'/'review_and_orientations.json').write_text(json.dumps(write,indent=2))
    print(json.dumps(dict(status='PASS',cases=len(rows),runtime_seconds=time.perf_counter()-start)))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');ap.add_argument('--review-only',action='store_true');args=ap.parse_args()
    if args.review_only:
        out=dict(orientations=orientations(),owner_review=owner_review());(ROOT/'out'/'review_and_orientations.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
    else:run(args.pilot)
