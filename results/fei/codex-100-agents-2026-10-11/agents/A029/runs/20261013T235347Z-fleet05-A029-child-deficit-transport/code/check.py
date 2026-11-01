import argparse,json,time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];ASSERT=0
def ck(v):
    global ASSERT
    ASSERT+=1
    if not v:raise AssertionError(ASSERT)
def pf(v):
    d={};p=2
    while p*p<=v:
        while v%p==0:d[p]=d.get(p,0)+1;v//=p
        p+=1
    if v>1:d[v]=d.get(v,0)+1
    return d
def add(a,b,w=F(1)):
    a=a.copy()
    for p,v in b.items():a[p]=a.get(p,F(0))+w*v
    return {p:v for p,v in a.items() if v}
def scale(a,w):return {p:v*w for p,v in a.items() if v*w}
def walsh(tab):
    a=list(tab);h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):u,v=a[k],a[k+h];a[k]=u+v;a[k+h]=u-v
        h*=2
    return a
@lru_cache(None)
def rec(tab):
    N=len(tab);n=N.bit_length()-1;w=walsh(tab);ck(sum(v*v for v in w)==N*N)
    H={2:F(2*n)}
    for v in w:
        if v:
            for p,e in pf(abs(v)).items():H[p]=H.get(p,F(0))-F(2*e*v*v,N*N)
    H={p:v for p,v in H.items() if v}
    d=[F(sum(tab[x]!=tab[x^(1<<i)] for x in range(N)),N) for i in range(n)]
    ck(sum(d)==F(sum(s.bit_count()*v*v for s,v in enumerate(w)),N*N))
    return H,sum(d),d,w
def seedtab(m,mask):return tuple(1 if mask>>z&1 else -1 for z in range(1<<m))
def root_table(g,m):return tuple(g[y]*(-1 if (x&y).bit_count()%2 else 1) for y in range(1<<m) for x in range(1<<m))
def restrict(tab,state):
    free=[i for i,v in enumerate(state) if v==-1]
    base=sum(v<<i for i,v in enumerate(state) if v!=-1)
    t=tuple(tab[base+sum(((z>>j)&1)<<i for j,i in enumerate(free))] for z in range(1<<len(free)))
    return free,rec(t)
def tree_ledger(tab,m,query):
    leafH={};leafI=F(0);nodeH={};nodeI=F(0);leaves=[];nodes=[]
    def walk(state):
        nonlocal leafH,leafI,nodeH,nodeI
        free,r=restrict(tab,state);H,I,d,_=r;w=F(1,2**(2*m-len(free)));q=query(state)
        if q is None:
            leafH=add(leafH,H,w);leafI+=w*I
            leaves.append({'state':state,'weight':str(w),'H':{str(p):str(v) for p,v in H.items()},'I':str(I)})
            return
        ck(q in free);nodes.append({'state':state,'query':q})
        ch=[]
        for b in range(2):s=list(state);s[q]=b;ch.append(restrict(tab,tuple(s))[1])
        delta=add(add(H,ch[0][0],-F(1,2)),ch[1][0],-F(1,2))
        ck(I-(ch[0][1]+ch[1][1])/2==d[free.index(q)])
        nodeH=add(nodeH,delta,w);nodeI+=w*d[free.index(q)]
        for b in range(2):s=list(state);s[q]=b;walk(tuple(s))
    walk((-1,)*(2*m));H,I,*_=rec(tab)
    ck(add(H,leafH,-1)==nodeH);ck(I-leafI==nodeI)
    return leafH,leafI,nodeH,nodeI,leaves,nodes
def priority(m):
    def query(s):
        first=next((i for i in range(m) if s[i]==1),None)
        if first is None:return next((i for i in range(m) if s[i]==-1),None)
        return next((i+m for i in range(first+1) if s[i+m]==-1),None)
    return query
def compact(s):
    if s[0]==-1:return 0
    if s[0]==1:return 3 if s[3]==-1 else None
    if s[1]==-1:return 1
    if s[1]==1:
        if s[4]==-1:return 4
        return 3 if s[4]==0 and s[3]==-1 else None
    if s[2]==-1:return 2
    return 5 if s[2]==1 and s[5]==-1 else None
def compact_certificate():
    m=3;g=seedtab(3,254);tab=root_table(g,m);Hg,Ig,*_=rec(g)
    ck(Hg=={2:F(4),3:-F(9,8)} and Ig==F(3,4))
    L,I,H,D,leaves,nodes=tree_ledger(tab,m,compact)
    ck(len(leaves)==8 and len(nodes)==7)
    ck(I==F(45,32) and D==F(51,32))
    ck(L=={2:F(25,8),3:-F(9,64)})
    ck(H=={2:F(23,8),3:F(9,64)})
    ratio=scale(H,1/D);ck(ratio=={2:F(92,51),3:F(3,34)})
    terminal=add({2:2*I},L,-1);credit=add({2:2*D},H,-1)
    ck(terminal=={2:-F(5,16),3:F(9,64)});ck(add(terminal,credit)=={})
    ck(3**5<2**8);upper=ratio[2]+ratio[3]*F(8,5);gain=4-upper
    ck(upper==F(496,255));ck(gain==F(524,255)>F(205,100))
    out={'status':'PASS','root_H':6,'root_I':3,'r1':4,'max_depth':4,
      'nodes':nodes,'leaves':leaves,'Pi_I':str(D),'Pi_H':{str(p):str(v) for p,v in H.items()},
      'ratio':{str(p):str(v) for p,v in ratio.items()},'strict_ratio_upper':str(upper),
      'strict_gain_lower':str(gain),'terminal_D2':{str(p):str(v) for p,v in terminal.items()},
      'query_credit':{str(p):str(v) for p,v in credit.items()},
      'prime_log_convention':'p coefficient multiplies log2(p); log2(2)=1',
      'global_optimum_ratio_claimed':False}
    (BASE/'out'/'compact.json').write_text(json.dumps(out,indent=2))
    return out
def main(pilot):
    start=time.monotonic();cases=0;nodecount=0;leafcount=0
    domains=[(3,[254])] if pilot else [(m,range(1<<(1<<m))) for m in (1,2,3)]
    for m,masks in domains:
        p=F(1,2**m)
        for mask in masks:
            g=seedtab(m,mask);tab=root_table(g,m);H0,I0,ds,w=rec(tab)
            ck(H0=={2:F(2*m)} and I0==m)
            ck(all(abs(a)==2**m for a in w));ck(all(di==F(1,2) for di in ds))
            Hg,Ig,*_=rec(g);L,I,H,D,leaves,nodes=tree_ledger(tab,m,priority(m))
            ck(I==m-2+2*p+p*Ig)
            ck(L==add({2:2*(m-2+2*p)},Hg,p))
            ck(D==2-p*(2+Ig)>0)
            ck(H==add({2:4-4*p},Hg,-p))
            # For three arbitrary induction constants, check both signed accounts exactly.
            for K in (F(2),F(4),F(17,3)):
                Dg=add({2:K*Ig},Hg,-1)
                term=add({2:K*I},L,-1);bill=add({2:K*D},H,-1)
                ck(term==add({2:(K-2)*(m-2+2*p)},Dg,p))
                ck(bill==add({2:2*(K-2)-2*p*(K-2)},Dg,-p))
                ck(add(term,bill)==({2:(K-2)*m} if K!=2 else {}))
            cases+=1;nodecount+=len(nodes);leafcount+=len(leaves)
    compact_certificate()
    out={'status':'PASS','pilot':pilot,'priority_cases':cases,'nodes':nodecount,'leaves':leafcount,
      'assertions':ASSERT,'elapsed_seconds':time.monotonic()-start,'cache':rec.cache_info()._asdict(),
      'arithmetic':'Exact prime-log forms and Fraction boundary influences; no floating point'}
    (BASE/'out'/('pilot.json' if pilot else 'checks.json')).write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--pilot',action='store_true');a=p.parse_args();main(a.pilot)
