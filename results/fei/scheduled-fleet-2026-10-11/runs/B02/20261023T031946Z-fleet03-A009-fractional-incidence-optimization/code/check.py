"""Frozen exact validation; no floating-point mathematical decisions."""
from fractions import Fraction as F
from math import comb, prod
from pathlib import Path
import json, time, sys

ROOT=Path(__file__).resolve().parents[1]
(ROOT/'out').mkdir(exist_ok=True)
START=time.monotonic()
COUNTS={}
def ck(v,k):
    assert v,k
    COUNTS[k]=COUNTS.get(k,0)+1
    if time.monotonic()-START>59: raise RuntimeError('frozen runtime reached')

def subsets(mask):
    x=mask
    while x:
        yield x
        x=(x-1)&mask

def bits(x):
    while x:
        v=x&-x
        yield v.bit_length()-1
        x-=v

def transform(v):
    w=v[:]; h=1
    while h<len(w):
        for i in range(0,len(w),2*h):
            for j in range(i,i+h):
                x,y=w[j],w[j+h]; w[j],w[j+h]=x+y,x-y
        h*=2
    return w

def data(a,b,H):
    n=a+b; full=(1<<b)-1
    hn=[sum(1<<j for ii,j in H if ii==i) for i in range(a)]
    hr=[sum(1<<i for i,jj in H if jj==j) for j in range(b)]
    d=max([x.bit_count() for x in hn+hr])
    E=set()
    for i in range(a):
        for Y in subsets(hn[i]):
            common=(1<<a)-1
            for j in bits(Y): common &=hr[j]
            for X in subsets(common):
                if X&-X==1<<i: E.add(X|(Y<<a))
    e=len(E)
    bd=sum((x^(1<<k)) not in E for x in E for k in range(n))
    J=F(2*bd,1<<n)
    cross=sum((x&((1<<a)-1)).bit_count()==1 for x in E)+sum((x>>a).bit_count()==1 for x in E)
    I0=2*a*F(1,1<<a)*(1-F(1,1<<b))+2*b*F(1,1<<b)*(1-F(1,1<<a))
    I=I0+F(2*bd-4*cross,1<<n)
    ck(J<=F(2*n*e,1<<n),'boundary_count')
    if d: ck(e<=a*((1<<d)-1)*(1<<(d-1)),'anchored_biclique_count')
    else: ck(e==0,'zero_deletion')
    if d<=2:
        c4=sum(1 for i in range(a) for k in range(i+1,a) if (hn[i]&hn[k]).bit_count()==2)
        ck(e==len(H)+sum(x.bit_count()==2 for x in hn+hr)+c4,'degree_two_count')
    if a>=4 and 2*d<=a:
        ck(I>=2*a*F(1,1<<a)*(1-F(1,1<<(b-d))),'sole_left_pivotal')
        ck(J*b/I<=F(b*b*(1<<(2*d)),1<<b)/(1-F(1,1<<(b-d))),'general_payment_algebra')
    if n<=16:
        vals=[]; actual_E=set()
        for x in range(1<<n):
            X=x&((1<<a)-1); Y=x>>a
            true=any(Y&(full^hn[i]) for i in bits(X))
            vals.append(1 if true else -1)
            if X and Y and not true: actual_E.add(x)
        ck(E==actual_E,'direct_exception_set')
        W=transform(vals)
        ck(sum(w*w for w in W)==(1<<n)**2,'parseval')
        ck(I==F(sum(k.bit_count()*w*w for k,w in enumerate(W)),(1<<n)**2),'physical_spectral_I')
        DV=transform([-2 if x in E else 0 for x in range(1<<n)])
        ck(J==F(sum(k.bit_count()*w*w for k,w in enumerate(DV)),(1<<n)**2),'physical_spectral_J')
        physical=F(sum(vals[x]!=vals[x^(1<<k)] for x in range(1<<n) for k in range(n)),1<<n)
        ck(I==physical,'direct_flip_I')
    return {'a':a,'b':b,'d':d,'deleted_edges':len(H),'exception_points':e,'I':str(I),'J':str(J)}

def forest(a,b,H):
    edges=[(i,a+j) for i in range(a) for j in range(b) if (i,j) not in H]
    if not edges: return
    n=a+b; lam=F(1,b)
    for A in range(1,1<<n):
        owned={}
        for v in bits(A):
            incident=[i for i,e in enumerate(edges) if v in e]
            if not incident: break
            owned.setdefault(incident[0],set()).add(v)
        else:
            es=sorted(owned); N=len(es)
            arc=[[i!=j and bool(owned[es[i]] &set(edges[es[j]])) for j in range(N)] for i in range(N)]
            reach=[[i==j or arc[i][j] for j in range(N)] for i in range(N)]
            for k in range(N):
                for i in range(N):
                    for j in range(N): reach[i][j] |= reach[i][k] and reach[k][j]
            comps=[]; unseen=set(range(N))
            while unseen:
                i=min(unseen); c={j for j in unseen if reach[i][j] and reach[j][i]}
                comps.append(c); unseen-=c
            roots=[min(c) for c in comps if not any(arc[i][j] for i in range(N) if i not in c for j in c)]
            reached=set(roots); queue=roots[:]; children=[0]*N
            for i in queue:
                for j in range(N):
                    if arc[i][j] and j not in reached:
                        reached.add(j); queue.append(j); children[i]+=1
            ck(len(reached)==N,'queue_reaches_all')
            numerator=lam**N*F(1,4)**len(roots)
            for i,e in enumerate(es):
                s=len(owned[e]); c=children[i]
                numerator/=s*(s+1)*comb(2,s)*(c+1)*(c+2)*comb(s+c-1,c)
            ck(numerator >=(lam/72)**A.bit_count(),'actual_forest_mass_72')
            if A>>a==0:
                count=prod(sum(i in e for e in edges) for i in bits(A))
                mass=F(count,1)*(lam/32)**A.bit_count()
                ck(mass==prod(F(sum(i in e for e in edges),32*b) for i in bits(A)),'left_partition_sum')
            elif A&((1<<a)-1)==0:
                count=prod(sum(i in e for e in edges) for i in bits(A))
                mass=F(count,1)*(lam/32)**A.bit_count()
                ck(mass==prod(F(sum(i in e for e in edges),32*b) for i in bits(A)),'right_partition_sum')

def small():
    rows=[]
    for a,b in [(2,2),(2,3),(3,3)]:
        for mask in range(1<<(a*b)):
            H={(i,j) for i in range(a) for j in range(b) if mask>>(i*b+j)&1}
            if max([sum(ii==i for ii,j in H) for i in range(a)]+[sum(jj==j for i,jj in H) for j in range(b)])>2: continue
            rows.append(data(a,b,H)); forest(a,b,H)
    ck(len(rows)==330,'small_graph_count')
    return rows

def extras():
    fixtures=[(4,4,{(i,i) for i in range(4)}|{(i,(i+1)%4) for i in range(4)})]
    for a,k in [(8,2),(12,3),(16,4),(32,4)]:
        fixtures.append((a,a,{(i,j) for i in range(a) for j in range(a) if i//k==j//k}))
    fixtures.append((4,8,{(i,j) for i in range(2) for j in range(2)}))
    rows=[data(*f) for f in fixtures]
    for r,k in zip(rows[1:5],[2,3,4,4]):
        ck(r['exception_points']==r['a']//k*((1<<k)-1)**2,'independent_block_count')
    ck(72**4<2**25,'log72_constant')
    ck(F(91,8)+F(72,7)==F(1213,56)<22,'quarter_final_constant')
    ck(F(91,8)+F(8,3)==F(337,24)<15,'tail_final_constant')
    ck(F(25,4)+F(9,8)+28==F(283,8)<36,'source_large_constant')
    ck(F(25,4)+F(9,8)+F(304,9)==F(2963,72)<42,'source_small_constant')
    for a in range(4,129):
        for b in range(a,129):
            for d in range(a//2+1):
                B=F(b*b*(1<<(2*d)),1<<b); den=1-F(1,1<<(b-d))
                if 4*d<=a: ck(2*B/den<=F(72,7),'quarter_scalar')
                if a*a*(1<<(2*d))<=1<<a: ck(2*B/den<=F(8,3),'tail_scalar')
    for b in range(4,257):
        ck(F(b**4,1<<b)<=F(81,4),'parity_scalar')
        if b>=5: ck((b+2)**2<=2*b*b,'parity_induction')
    return rows

def obstruction():
    rows=[]
    for m in range(2,129):
        u=F(1,1<<m); I=8*m*u*u*(1-u)*(2-u); J=8*m*u*u*(1-u)
        ck(J/I==1/(2-u) and J/I>F(1,2),'obstruction_ratio')
        if m<=4:
            a=2*m; H={(i,j) for i in range(a) for j in range(a) if i//m==j//m}
            r=data(a,a,H)
            ck(F(r['I'])==I and F(r['J'])==J,'obstruction_actual_boolean')
            rows.append(r)
    return rows

if __name__=='__main__':
    mode=sys.argv[1]
    result={'helper':'A009-growing-deleted-degree-v1','mode':mode}
    if mode=='pilot': result['graphs']=small()
    elif mode=='full': result['graphs']=small(); result['fixtures']=extras(); result['obstruction']=obstruction()
    else: raise ValueError(mode)
    result.update(counts=COUNTS,total_checks=sum(COUNTS.values()),elapsed_seconds=time.monotonic()-START,status='PASS')
    (ROOT/'out'/f'{mode}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['graphs','fixtures','obstruction']}))
