import json,time
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path
from check_phase import walsh
ROOT=Path(__file__).resolve().parents[1]

def add(v,key,w):
    if key>1 and w:v[key]+=w
def vec_entropy(nums,den):
    v=defaultdict(Q)
    for p in nums:
        if p:
            add(v,den,Q(p,den));add(v,p,-Q(p,den))
    return v
def merge(*parts):
    out=defaultdict(Q)
    for scale,vec in parts:
        for k,v in vec.items():out[k]+=scale*v
    return {k:v for k,v in out.items() if v}
def entropy(f):
    N=len(f);W=walsh(f)
    return vec_entropy([v*v for v in W],N*N)
def influence(f):
    W=walsh(f);N=len(f)
    return Q(sum(s.bit_count()*v*v for s,v in enumerate(W)),N*N)
def faces(f):
    N=len(f);n=N.bit_length()-1;odd=0
    for i in range(n):
        for j in range(i):
            for x in range(N):
                if not(x>>i&1) and not(x>>j&1):
                    odd+=f[x]*f[x^(1<<i)]*f[x^(1<<j)]*f[x^(1<<i)^(1<<j)]==-1
    return Q(2*odd,N)
def split(f,i):
    g=[];h=[];n=len(f).bit_length()-1
    for z in range(1<<(n-1)):
        x=(z&((1<<i)-1))|((z>>i)<<(i+1))
        g.append(f[x]);h.append(f[x|(1<<i)])
    return g,h

def tree(f,order):
    start=time.monotonic();Wtotal=Q(0);dtotal=Q(0)
    btotal={};jtotal={};credits={};nodes=0;assertions=0
    def visit(f,labels,w):
        nonlocal Wtotal,dtotal,btotal,jtotal,credits,nodes,assertions
        if len(f)==1:return
        i=labels.index(next(j for j in order if j in labels));g,h=split(f,i)
        N=len(g);A=[(x+y)//2 for x,y in zip(g,h)];V=[(x-y)//2 for x,y in zip(g,h)]
        U=walsh(A);Z=walsh(V)
        real=[x*x for x in U];imag=[x*x for x in Z];q=[a+b for a,b in zip(real,imag)]
        Hpacket=vec_entropy(q,N*N)
        # Conditional spectral entropy from entropy difference, independently of phase formal-log checker.
        B=merge((1,entropy(f)),(-1,Hpacket))
        JS=merge((1,Hpacket),(-Q(1,2),entropy(g)),(-Q(1,2),entropy(h)))
        delta=merge((1,entropy(f)),(-Q(1,2),entropy(g)),(-Q(1,2),entropy(h)))
        assert merge((1,B),(1,JS))==delta;assertions+=1
        d=Q(sum(v*v for v in V),N);phasebill=influence([x*y for x,y in zip(g,h)])/2
        assert faces(f)==phasebill+(faces(g)+faces(h))/2;assertions+=1
        assert influence(f)==d+(influence(g)+influence(h))/2;assertions+=1
        Wtotal+=w*phasebill;dtotal+=w*d
        btotal=merge((1,btotal),(w,B));jtotal=merge((1,jtotal),(w,JS))
        # R+M+sigma = phasebill + log2(e)d - B; track log2(e) coefficient separately.
        credits=merge((1,credits),(-w,B));nodes+=1
        childlabels=[j for z,j in enumerate(labels) if z!=i]
        visit(g,childlabels,w/2);visit(h,childlabels,w/2)
    n=len(f).bit_length()-1
    visit(f,list(range(n)),Q(1))
    assert Wtotal==faces(f);assertions+=1
    assert dtotal==influence(f);assertions+=1
    assert merge((1,btotal),(1,jtotal))==dict(entropy(f));assertions+=1
    # In (5), tree credit is Wtotal + log2(e)dtotal + credits. Both first terms cancel exactly.
    assert merge((-1,credits),(1,jtotal))==dict(entropy(f));assertions+=1
    assert Wtotal+Q(0)==faces(f)
    return {'order':order,'nodes':nodes,'assertions':assertions,'I':str(dtotal),'Q_odd':str(Wtotal),
            'Q_sum':str(2*Wtotal),'runtime_seconds':time.monotonic()-start,
            'certificate':'exact formal logarithms and rational scalar credit cancellation; no float signs'}

def main():
    start=time.monotonic();cases=[]
    for r in [2,4]:
        n=2*r;mask=(1<<r)-1
        def b(z):
            x=z&mask;y=z>>r;My=y^(mask if y.bit_count()%2 else 0)
            return -1 if (x&My).bit_count()%2 else 1
        f=[b(z) for z in range(1<<n)]
        for order in [list(range(n)),list(reversed(range(n)))]:
            cases.append({'family':'dense_bent','r':r,**tree(f,order)})
    for m in [2,4,6]:
        n=m+1
        def b(z):return -1 if sum(((z>>(2*j))&1)*((z>>(2*j+1))&1) for j in range(m//2))%2 else 1
        f=[b(z>>1)*(-1 if (z&1) and not(z>>1) else 1) for z in range(1<<n)]
        for order in [list(range(n)),list(reversed(range(n)))]:
            cases.append({'family':'bent_point_selector','m':m,**tree(f,order)})
        if time.monotonic()-start>58:raise RuntimeError('Frozen 60-second cap')
    result={'cases':cases,'total_cases':len(cases),'assertions':sum(c['assertions'] for c in cases),'runtime_seconds':time.monotonic()-start}
    (ROOT/'out/tree_validation.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
if __name__=='__main__':main()
