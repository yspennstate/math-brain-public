"""Independent direct-character reconstruction; exact rational prime-log equalities."""
from pathlib import Path
from fractions import Fraction as F
import json, time, sys

RUN = Path(__file__).resolve().parents[1]
START = time.monotonic()
COUNT = 0

def check(ok):
    global COUNT
    COUNT += 1
    assert ok, COUNT
    assert time.monotonic() - START < 55, 'frozen runtime exceeded'

def logq(q):
    assert q > 0
    d = {}
    for value, sign in [(q.numerator, 1), (q.denominator, -1)]:
        p = 2
        while p*p <= value:
            while value % p == 0:
                d[p] = d.get(p, 0)+sign
                value //= p
            p += 1
        if value > 1:
            d[value] = d.get(value, 0)+sign
    return {p: F(a) for p,a in d.items() if a}

def add(*terms):
    ans = {}
    for d in terms:
        for p,a in d.items(): ans[p] = ans.get(p,F(0))+a
    return {p:a for p,a in ans.items() if a}

def scale(a,d): return {p:a*b for p,b in d.items() if a*b}

def ce(p,q):
    return add(*(scale(-a,logq(b)) for a,b in zip(p,q) if a))

def entropy(p): return ce(p,p)

def kl(p,q): return add(ce(p,q),scale(-1,entropy(p)))

def spec(f):
    N = len(f)
    return [F(sum(v * (-1 if (s & x).bit_count()%2 else 1)
                  for x,v in enumerate(f)), N)**2 for s in range(N)]

def insert(x,j,bit): return (x & ((1<<j)-1)) | ((x>>j)<<(j+1)) | (bit<<j)

def restrict(f,j,bit): return [f[insert(x,j,bit)] for x in range(len(f)//2)]

def marginal(p,j): return [p[insert(t,j,0)]+p[insert(t,j,1)] for t in range(len(p)//2)]

def query(f,q,j,reset=False):
    p=spec(f);m=marginal(p,j);v=marginal(q,j)
    children=[restrict(f,j,b) for b in range(2)]
    pc=[spec(h) for h in children]
    check(sum(p)==sum(q)==sum(v)==1)
    check(all((pc[0][t]+pc[1][t])/2==m[t] for t in range(len(m))))
    check(all(not a or b>0 for child in pc for a,b in zip(child,v)))
    B=add(entropy(p),scale(-1,entropy(m)))
    R=add(kl(p,q),scale(-1,kl(m,v)))
    # Independent fiber disintegration, including reference-only fibers.
    direct={}
    for t,mt in enumerate(m):
        if mt:
            cp=[p[insert(t,j,b)]/mt for b in range(2)]
            cq=[q[insert(t,j,b)]/v[t] for b in range(2)]
            check(sum(cp)==sum(cq)==1)
            direct=add(direct,scale(mt,kl(cp,cq)))
    check(R==direct)
    terminal=scale(F(1,2),add(*(ce(child,v) for child in pc)))
    check(ce(p,q)==add(B,terminal,R))
    J=add(entropy(m),scale(F(-1,2),add(*(entropy(child) for child in pc))))
    check(add(kl(p,q),scale(F(-1,2),add(*(kl(child,v) for child in pc))))==add(R,scale(-1,J)))
    if reset:
        fresh=[]
        for b,child in enumerate(pc):
            # Mixed true/uniform: all support retained, never zero normalization.
            fresh.append([(a+F(1,len(child)))/2 for a in child])
        Z=scale(F(1,2),add(*(
            add(*(scale(a,logq(old/new)) for a,old,new in zip(child,v,qq) if a))
            for child,qq in zip(pc,fresh))))
        newcost=scale(F(1,2),add(*(ce(child,qq) for child,qq in zip(pc,fresh))))
        check(newcost==add(terminal,Z))
        # RS2 as prime-log identity, with a nonzero already-booked debit.
        A={2:F(19)};d={2:F(3)}
        U=add(A,scale(-1,d),scale(-1,ce(p,q)))
        lhs=add(A,scale(-1,d),scale(-1,B),scale(-1,newcost))
        check(lhs==add(U,R,scale(-1,Z)))
    return children,v,B,R

def history(f,q,depth=0):
    if len(f)==1 or (depth>0 and f[0]==1):
        return {},{},ce(spec(f),q),1
    n=(len(f)).bit_length()-1
    j=(depth+int(f[0]<0))%n
    child,v,B,R=query(f,q,j)
    results=[history(h,v,depth+1) for h in child]
    bs=add(B,scale(F(1,2),add(*(x[0] for x in results))))
    rs=add(R,scale(F(1,2),add(*(x[1] for x in results))))
    ts=scale(F(1,2),add(*(x[2] for x in results)))
    check(ce(spec(f),q)==add(bs,rs,ts))
    return bs,rs,ts,sum(x[3] for x in results)

def main():
    pilot='--pilot' in sys.argv
    roots=queries=histories=leaves=0
    for n in range(1, 3 if pilot else 4):
        N=1<<n
        for word in range(1<<N):
            f=[1 if word>>x&1 else -1 for x in range(N)]
            p=spec(f)
            models=[p,[F(1,N)]*N,[F(2*(x+1),N*(N+1)) for x in range(N)]]
            for q in models:
                roots+=1
                for j in range(n):
                    query(f,q,j,reset=True);queries+=1
                b,r,t,L=history(f,q);histories+=1;leaves+=L
                check(ce(p,q)==add(b,r,t))
    f=[1,1,1,1,-1,1,1,1];p=spec(f)
    check(p==[F(9,16)]+[F(1,16)]*7)
    h=restrict(f,0,1);v=marginal(p,0)
    check(h==[1]*4)
    check(v==[F(5,8)]+[F(1,8)]*3)
    check(ce(spec(h),v)==logq(F(8,5)))
    # Countercheck a tempting omitted-entropy KL telescope on a constant child.
    _,_,B,R=query(f,p,0)
    check(kl(p,p)=={} and R=={})
    check(any(kl(spec(restrict(f,0,b)),v) for b in range(2)))
    # Full terminal tensor cost stays additive, including off-true-support mass.
    terminals=0
    for word in range(16):
        h=[1 if word>>x&1 else -1 for x in range(4)];ph=spec(h);rh=[F(1,4)]*4
        for q in [p,[F(1,8)]*8]:
            joint=[a*b for a in p for b in ph];qr=[a*b for a in q for b in rh]
            check(ce(joint,qr)==add(ce(p,q),ce(ph,rh)))
            terminals+=1
    out={'status':'PASS','pilot':pilot,'roots_and_references':roots,'single_queries':queries,
         'adaptive_histories':histories,'terminal_leaves':leaves,'tensor_cases':terminals,
         'exact_assertions':COUNT,'arithmetic':'Fraction and exact prime-log vectors; no floating sign',
         'seconds':time.monotonic()-START,'scope':'finite algebraic identities; Gibbs sign proved analytically; no universal FEI certificate'}
    (RUN/'out'/('PILOT.json' if pilot else 'EXACT_TRANSPORT.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out))

if __name__=='__main__':main()
