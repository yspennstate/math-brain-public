from exact import *
import exact as eng

def sub(x,y):return combine((1,x),(-1,y))
def kl(p,q):return sub(ce(p,q),entropy(p))
def complete_ce(p,q):
    mass=sum(q);check(0<mass<=1)
    return combine((1,ce(p,[x/mass for x in q])),(-1,logq(mass)))

def inherit(v,q,j):
    p=spectrum(v);m=marginal(p,j);r=marginal(q,j);s=sum(q)
    ps=[spectrum(restrict(v,j,b)) for b in (0,1)]
    raw=[[R*x/y if y else R for x,y,R in zip(child,m,r)] for child in ps]
    Z=[sum(x) for x in raw];check(all(x>0 for x in Z))
    qs=[[s*x/z for x in row] for row,z in zip(raw,Z)]
    check((Z[0]+Z[1])/2==s)
    check(all(sum(x)==s for x in qs))
    return ps,qs,Z

v0=[1]+[-1]*7
q0=[F(x,256) for x in [144,1,1,1,106,1,1,1]]
q1=[F(x,256) for x in [144,80,15,13,1,1,1,1]]
transactions=0;child_checks=0;paths=0;zero_fibers=0
for truth in range(256):
    v=[1 if truth>>z&1 else -1 for z in range(8)];p=spectrum(v)
    for j in range(3):
        m=marginal(p,j);children=[restrict(v,j,b) for b in (0,1)]
        for s in [F(1),F(1,2)]:
            a=[s*x for x in q0];b=[s*x for x in q1]
            ps,qa,Z0=inherit(v,a,j);_,qb,Z1=inherit(v,b,j)
            for lam in [F(1,4),F(1,2),F(3,4)]:
                mix=[(1-lam)*x+lam*y for x,y in zip(a,b)]
                _,qm,Zm=inherit(v,mix,j)
                for k in (0,1):
                    lc=lam*Z1[k]/((1-lam)*Z0[k]+lam*Z1[k])
                    check(qm[k]==[(1-lc)*x+lc*y for x,y in zip(qa[k],qb[k])])
                    # The advertised likelihood corridor is an exact equivalence.
                    for c in [F(1,4),F(1,2)]:check((lc>=c)==(Z1[k]/Z0[k]>=c*(1-lam)/(lam*(1-c))))
                    child_checks+=1
                decr=combine((1,entropy(p)),(-F(1,2),entropy(ps[0])),(-F(1,2),entropy(ps[1])))
                inc=combine((1,decr),(F(1,2),complete_ce(ps[0],qm[0])),(F(1,2),complete_ce(ps[1],qm[1])),(-1,complete_ce(p,mix)))
                rm=marginal(mix,j)
                rho=sub(kl(p,[x/s for x in mix]),kl(m,[x/s for x in rm]))
                norm=combine((F(1,2),logq(Zm[0]/s)),(F(1,2),logq(Zm[1]/s)))
                check(not combine((1,inc),(1,rho),(-1,norm)))
                check(not inc or bounds(inc)[1]<=0)
                check(not rho or bounds(rho)[0]>=0)
                zero_fibers+=sum(x==0 for x in m)
                transactions+=1
            check(time.perf_counter()-start<55)
    # Two successive queries on one common physical history, retained mass1/2.
    vv=v;qs=[[x/2 for x in q0],[x/2 for x in q1]];lm=F(1,4)
    mix=[(1-lm)*x+lm*y for x,y in zip(qs[0],qs[1])];L=[F(1),F(1)]
    for outcome in (truth%2,(truth//2)%2):
        _,c0,z0=inherit(vv,qs[0],0);_,c1,z1=inherit(vv,qs[1],0);_,cm,zm=inherit(vv,mix,0)
        L[0]*=z0[outcome]/F(1,2);L[1]*=z1[outcome]/F(1,2)
        lc=lm*L[1]/((1-lm)*L[0]+lm*L[1])
        check(cm[outcome]==[(1-lc)*x+lc*y for x,y in zip(c0[outcome],c1[outcome])])
        vv=restrict(vv,0,outcome);qs=[c0[outcome],c1[outcome]];mix=cm[outcome]
    paths+=1

# Exact source witness and a free mass/vacuum-preserving floor repair.
ps,a,Z0=inherit(v0,q0,0);_,b,Z1=inherit(v0,q1,0)
mix=[F(3,4)*x+F(1,4)*y for x,y in zip(q0,q1)]
_,c,Zm=inherit(v0,mix,0)
P=ps[0];q=c[0];target=b[0]
check(P==[F(1,4)]*4 and c[0][1]==F(85,1242))
lc=F(1,4)*Z1[0]/Zm[0];check(lc==F(32,207))
check(q[1]<target[1]/4 and target[1]/4==F(35,384))
M=[x/(1-q[0]) for x in q[1:]];T=[x/(1-target[0]) for x in target[1:]]
pi=[F(1,3)]*3
check(M[0]/T[0]==F(272,2555))
check(T==[F(7,8),F(1,16),F(1,16)])
check(min(x/y for x,y in zip(pi,T))==F(8,21))
repair=[q[0]]+[(1-q[0])*x for x in pi]
check(sum(repair)==sum(q) and repair[0]==q[0])
check(all(x>=y/4 for x,y in zip(repair,target)))
check(all(x>=y/4 for x,y in zip(pi,T)))
tax=sub(complete_ce(P,repair),complete_ce(P,q))
expected=combine((-F(3,4),kl(pi,M)))
check(not sub(tax,expected) and bounds(tax)[1]<0)
# Same full owner: retain the complementary physical terminal unchanged.
old_bill=combine((F(1,2),complete_ce(ps[0],c[0])),(F(1,2),complete_ce(ps[1],c[1])))
new_bill=combine((F(1,2),complete_ce(ps[0],repair)),(F(1,2),complete_ce(ps[1],c[1])))
check(not combine((1,new_bill),(-1,old_bill),(-F(1,2),tax)))
check(bounds(sub(old_bill,new_bill))[0]>F(1,4))

out={'status':'PASS','assertions':eng.assertions,'parent_transactions':transactions,'child_mixture_checks':child_checks,'two_query_paths':paths,'actual_zero_fibers_retained':zero_fibers,'elapsed_seconds':time.perf_counter()-start,'witness':{'lambda_child':str(lc),'old_child':[str(x) for x in q],'target_child':[str(x) for x in target],'actual_child':[str(x) for x in P],'conditional_target':[str(x) for x in T],'old_conditional_ratio':str(M[0]/T[0]),'repaired_conditional_floor':str(F(8,21)),'repair_child':[str(x) for x in repair],'repair_signed_tax':display(tax),'global_original_owner_release':display(sub(old_bill,new_bill))},'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'helper_sha256':hashlib.sha256(Path(eng.__file__).read_bytes()).hexdigest()}
(run/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='')
print(json.dumps(out,indent=2))
