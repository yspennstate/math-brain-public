"""early_tag_v1: exact closed spectra versus independent physical truth tables."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from itertools import product
import sys, json, time, hashlib
sys.dont_write_bytecode=True
import kernel as K
ROOT=Path(__file__).resolve().parents[1]
PRICES=[F(4),F(32609,5000),F(8)]

def entropy(items,den):
    assert den>0 and den&(den-1)==0
    mult=Counter()
    for a,c in items: mult[abs(a)]+=c
    K.check(sum(a*a*c for a,c in mult.items())==den*den)
    e=den.bit_length()-1;lo=hi=2*e*K.SCALE;sym={2:F(2*e)}
    for a,c in mult.items():
        if not a or not c:continue
        l,h=K.log_bounds(a);w=F(2*a*a*c,den*den)
        lo-=K.ceil(w*h);hi-=K.floor(w*l)
        for p,v in K.factors(a).items():sym[p]=sym.get(p,F(0))-w*v
    return (lo,hi),{p:v for p,v in sym.items() if v}

def sadd(a,b,scale=F(1)):
    d=dict(a)
    for p,v in b.items():d[p]=d.get(p,F(0))+scale*v
    return {p:v for p,v in d.items() if v}

def es(k):
    N=1<<k;r=1<<(k//2);np=(N+r)//2;nm=(N-r)//2
    return [(r-1,np),(r+1,nm),(1,N)],N

def os(j):
    N=1<<j;r=1<<(j//2);np=(N+r)//2;nm=(N-r)//2
    return [(2*r-1,np),(2*r+1,nm),(1,3*N)],2*N

def bent(x,k):return sum(((x>>i)&1)*((x>>(i+1))&1) for i in range(0,k,2))%2

def reserve(D,C,d,q):return K.pos(K.add(K.sub(D,K.exact(C*d)),K.half(q)))

def raw_profile(k,odd=False):
    # dummy is first coordinate, so the exceptional mate query is physically first.
    n=k+1+int(odd);ans=[]
    for z in range(1<<n):
        if odd:y=z&1;x=(z>>1)&((1<<k)-1);w=(z>>(k+1))&1;edit=(x==0 and y==0)
        else:x=z&((1<<k)-1);w=(z>>k)&1;edit=(x==0)
        ans.append(bent(x,k)^(w and edit))
    return bytes(ans)

def raw_seed(choices):
    free=[i for i,c in enumerate(choices) if c is None];out=[]
    for z in range(1<<len(free)):
        bits=[c for c in choices]
        for j,i in enumerate(free):bits[i]=(z>>j)&1
        out.append(int(sum(bits)>=2))
    return bytes(out)

def compare_raw(items,den,truth):
    expected=Counter()
    for a,c in items:
        if c:expected[abs(a)]+=c
    expected.pop(0,None)
    actual=Counter(abs(v)*den//len(truth) for v in K.walsh(truth) if v)
    K.check(all(v*den%len(truth)==0 for v in K.walsh(truth)))
    K.check(expected==actual)

def main():
    start=time.monotonic();pilot='--pilot' in sys.argv
    widths=[2,4] if pilot else [2,4,6,8,10,12]
    rows=[];seedrows=0;qe={0:tuple((0,0) for _ in PRICES)}
    for j in range(0,max(widths)+1,2):
        ho,_=entropy(*os(j));hm,_=entropy(*es(j))
        D=K.sub(ho,K.half(K.add(hm,K.exact(F(j)))))
        qo=tuple(reserve(D,C,F(1,2*(1<<j)),q) for C,q in zip(PRICES,qe[j]))
        if j>=2:
            K.check(ho[0]>F(3*j-2,3)*K.SCALE)
            K.check(D[1]<F(15,16)*K.SCALE)
            K.check(all(q[1]<=F(15,16)*K.SCALE for C,q in zip(PRICES,qo) if C>=6))
        if j+2<=max(widths):
            k=j+2;he,_=entropy(*es(k));de=K.sub(he,K.half(K.add(ho,K.exact(F(j)))))
            qe[k]=tuple(reserve(de,C,F(1,2)+F(1,1<<k),q) for C,q in zip(PRICES,qo))
            K.check(all(q==(0,0) for C,q in zip(PRICES,qe[k]) if C>=6))
        if j not in widths:continue
        k=j;N=1<<k;r=1<<(k//2);np=(N+r)//2;nm=(N-r)//2
        ei,ed=es(k);oi,od=os(k)
        compare_raw(ei,ed,raw_profile(k));compare_raw(oi,od,raw_profile(k,True))
        if k<=6:
            tt=raw_profile(k)
            rt=K.tree(tt,list(range(k+1)),'control-first',['data']*(k+1))
            for actual,compressed in zip(rt['Q_scaled'],qe[k]):
                K.check(max(actual[0],compressed[0])<=min(actual[1],compressed[1]))
        for odd,tt in [(False,raw_profile(k)),(True,raw_profile(k,True))]:
            _,ct=K.stats(tt);actual=F(2*ct[0],len(tt));K.check(actual==(F(1,2*N) if odd else F(1,2)+F(1,N)))
        if k>=6:K.check(hm[1]<(F(k)+F(15,128))*K.SCALE)
        if k==4:K.check(hm[1]<(F(k)+F(11,32))*K.SCALE)
        if j>=4:K.check(ho[0]>(F(j)-F(1,2))*K.SCALE)
        if j==2:K.check(ho[0]>2*K.SCALE)
        K.check((r-1)**2+1>F(N,4))
        hv,_=entropy([(r-2,np),(r+2,nm)],N)
        dw=K.sub(hm,K.half(K.add(K.exact(F(k)),hv)))
        eps=[K.sub(K.add(dw,K.exact(F(2,N))),K.exact(C*F(5,2*N))) for C in PRICES]
        for C,ep in zip(PRICES,eps):K.check(F(ep[0],K.SCALE)>F(1,N)*(k-F(5,2)*C))
        if k==10:K.check(F(eps[1][0],K.SCALE)>F(1,100000))
        for choices in product([None,0,1],repeat=3):
            a=raw_seed(choices);aw=K.walsh(a);L=len(a);ha,sa=entropy([(abs(v),1) for v in aw],L)
            # Fresh tag: the A and aB sectors are disjoint, including empty seed.
            hidden=[((r-1)*L,np),((r+1)*L,nm)]+[(abs(z),N) for z in aw]
            hf,sf=entropy(hidden,N*L);_,sm=entropy(ei,N)
            K.check(sf==sadd(sm,sa,F(1,N)))
            for sign in [-1,1]:
                child=[((r-1)*L+sign*aw[0],np),((-r-1)*L+sign*aw[0],nm)]+[(abs(z),N) for z in aw[1:]]
                hc,sc=entropy(child,N*L)
                if k<=4:
                    raw=bytes(bent(x,k)^int(x==0 and ((1-sign*(1-2*a[z]))//2)) for z in range(L) for x in range(N))
                    compare_raw(child,N*L,raw)
                K.check(hc[0]>=0)
            seedrows+=1
        rows.append({'k':k,'Dtag':dw,'epsilon':eps,'profile_reserves':qe[k],'Hprofile':hm,'Hodd':ho})
        K.stats.cache_clear();K.children.cache_clear()
        K.check(time.monotonic()-start<55)
    result={'helper':'early_tag_v1','scale':str(K.SCALE),'prices':[str(C) for C in PRICES],'roots':len(rows)*3,'partial_seed_histories':seedrows,'rows':rows,'assertions':K.ASSERTIONS,'seconds':time.monotonic()-start,'rigor':'integer Walsh, Fraction logarithm enclosures, symbolic prime-log identities; finite verification only'}
    (ROOT/'out'/('PILOT.json' if pilot else 'EXACT.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['roots','partial_seed_histories','assertions','seconds']}))

if __name__=='__main__':main()
