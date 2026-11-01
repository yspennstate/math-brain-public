from pathlib import Path
from fractions import Fraction as F
import arithmetic as A
import json,sys,time
RUN=Path(__file__).resolve().parents[1]
def add(*xs):
    z=(F(0),F(0))
    for x in xs:z=A.add(z,x)
    return z
def zero(x):A.ck(x[0]<=0<=x[1])
def H(v):
    p=A.law(v);return A.ce(p,p)
def D(v,q):return A.sub(A.ce(A.law(v),q),H(v))
def embed(q,b,r):
    return q+[F(0)]*(len(q)*((1<<(b+r))-1))
def floor(g,R,b,r=1):
    a=(len(g)-1).bit_length();n=a+b;rho=F(1,1<<(n+r));beta=6*rho
    base=[g[x&((1<<a)-1)] for x in range(1<<(n+r))];base[0]*=-1
    P=A.law(base);q=[sum(P[x+(u<<n)] for u in range(1<<r)) for x in range(1<<n)]
    Rpad=R+[F(0)]*((1<<n)-len(R))
    data=[(x+beta/F(1<<n))/(1+beta) for x in Rpad]
    Q=[data[x&((1<<n)-1)]*p/q[x&((1<<n)-1)] for x,p in enumerate(P)]
    A.ck(sum(Q)==(sum(R)+beta)/(1+beta));A.ck(all(not p or qq>0 for p,qq in zip(P,Q)))
    if n==0:A.ck(data[0]>=R[0])
    return base,Q
def source_children(g,R,i):
    s=sum(R);vv,qq=A.inherit(g,[x/s for x in R],i,True)
    QQ=[[s*x for x in q] for q in qq]
    A.ck(all(sum(q)==s for q in QQ))
    contraction=A.sub(D(g,R),A.scale(add(*(D(v,q) for v,q in zip(vv,QQ))),F(1,2)))
    A.ck(contraction[1]>=0)
    return vv,QQ
def tree(g,b,variant,reverse):
    a=(len(g)-1).bit_length();p=A.law(g);s=F(1) if variant==0 else F(1,2)
    R=p if variant==0 else [(x+F(1,len(p)))/4 for x in p]
    A.ck(sum(R)==s);I=A.total(g);c=A.ce(p,R);C0=F((c[1]/I).__ceil__());K=4*C0+15
    v,Q=floor(g,R,b);I0=A.total(v);hroot=H(v);Croot=A.ce(A.law(v),Q)
    dp=sum(g[0]!=g[1<<i] for i in range(a));rho=F(1,1<<(a+b+1));E=2*rho*dp;G=2*rho*(a+b-dp+1)
    A.ck(I0==I+G-E);A.ck(E<=I/8)
    leaves=[];reach=F(1);signed=(F(0),F(0));entropy=(F(0),F(0));rows=[];source=g;model=R;pad=b
    def record(kind,depth):
        terms=[(rr,D(vv,qq),A.ce(A.law(vv),qq)) for rr,vv,qq in leaves]+[(reach,D(v,Q),A.ce(A.law(v),Q))]
        endpoint=add(hroot,*(A.scale(d,rr) for rr,d,_ in terms))
        zero(A.sub(endpoint,add(Croot,signed)))
        zero(A.sub(endpoint,add(entropy,*(A.scale(cc,rr) for rr,_,cc in terms))))
        # Retain stronger root and padding structure, and actual quantitative source factor.
        if kind in ['root','final']:
            upper=2*c[1]+30*rho*(a+b+1)
        elif kind=='padding':upper=F(3,2)*c[1]+F(61,8)*I
        else:upper=F(5,2)*c[1]+F(15,2)*I
        A.ck(endpoint[1]<=upper);A.ck(K*I0-endpoint[1]>=(C0+F(11,2))*I)
        U=(C0+F(37,8))*I
        A.ck(K*I0-endpoint[1]-U>=F(7,8)*I)
        A.ck(K*I0-endpoint[1]-(C0+1)*I>=F(7,8)*I)
        rows.append({'kind':kind,'depth':depth,'source_bits':(len(source)-1).bit_length(),'full_ledger_interval':[str(x) for x in endpoint],'complete_reference_mass':str(sum(Q)),'margin_after_larger_U_lower':str(K*I0-endpoint[1]-U)})
    record('root',0)
    def step(i,children,newmodels):
        nonlocal v,Q,reach,signed,entropy
        actual=[A.restrict(v,i,j) for j in [0,1]]
        A.ck(actual==children)
        dv=D(v,Q);ds=[D(x,q) for x,q in zip(children,newmodels)]
        signed=add(signed,A.scale(A.sub(A.scale(add(*ds),F(1,2)),dv),reach))
        entropy=add(entropy,A.scale(A.sub(H(v),A.scale(add(*(H(x) for x in children)),F(1,2))),reach))
        A.ck(A.total(v)==A.inf(v,i)+(A.total(children[0])+A.total(children[1]))/2)
        leaves.append((reach/2,children[1],newmodels[1]));v,Q=children[0],newmodels[0];reach/=2
    for j in range(b):
        pad-=1;active,fresh=floor(source,model,pad)
        off=[source[x&((1<<a)-1)] for x in range(1<<(a+pad+1))]
        step(a,[active,off],[fresh,embed(model,pad,1)])
        record('padding',j+1)
    for k in range(1,a+1):
        i=(len(source)-1).bit_length()-1 if reverse else 0
        gg,rr=source_children(source,model,i)
        active,fresh=floor(gg[0],rr[0],0)
        off=gg[1]+gg[1]
        step(i,[active,off],[fresh,embed(rr[1],0,1)])
        source,model=gg[0],rr[0]
        if k==a:
            A.ck(len(model)==1 and model[0]==s)
            A.ck(D(v,Q)[1]<=-A.lg(s)[0]+F(1,1<<50))
        record('final' if k==a else 'source',k)
    return {'a':a,'source_table':g,'b':b,'reference_variant':variant,'source_mass':str(s),'reverse_source_order':reverse,'C0':str(C0),'Ig':str(I),'frontiers':rows}
mode=sys.argv[1];start=time.perf_counter()
small=[[1,-1],[-1,1]]+[[1 if mask&(1<<x) else -1 for x in range(4)] for mask in range(1,15)]
sources=small+[[1 if x else -1 for x in range(8)],[(-1)**x.bit_count() for x in range(8)],[1 if x.bit_count()>=2 else -1 for x in range(8)]]
if mode=='pilot':sources=[[1,-1],[-1,1,1,1]]
rows=[]
for g in sources:
    for b in ([2] if mode=='pilot' else [2,3]):
        for variant in [0,1]:
            for rev in ([False] if mode=='pilot' or len(g)==2 else [False,True]):rows.append(tree(g,b,variant,rev))
out={'status':'PASS','mode':mode,'ordered_trees':len(rows),'frontiers':sum(len(z['frontiers']) for z in rows),'assertions':A.checks,'seconds':time.perf_counter()-start,'rows':rows}
(RUN/'out'/f'{mode.upper()}_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
