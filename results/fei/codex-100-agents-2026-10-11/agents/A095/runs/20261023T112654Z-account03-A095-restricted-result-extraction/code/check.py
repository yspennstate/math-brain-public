from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import importlib.util, hashlib, json, sys, time

RUN=Path(__file__).resolve().parents[1]
OWN=RUN.parents[1]
HELPER=OWN/'runs/20261021T180853Z-account03-A095-restricted-result-extraction/code/check.py'
sp=importlib.util.spec_from_file_location('own_arithmetic',HELPER)
A=importlib.util.module_from_spec(sp);sp.loader.exec_module(A)
START=time.perf_counter();COUNT=0
def ck(x):
    global COUNT
    assert x
    COUNT+=1
    if time.perf_counter()-START>55: raise RuntimeError('frozen 55-second guard')
def add(x,y):return x[0]+y[0],x[1]+y[1]
def sub(x,y):return x[0]-y[1],x[1]-y[0]
def mul(q,x):return q*x[0],q*x[1]
def total(xs):
    z=(F(0),F(0))
    for x in xs:z=add(z,x)
    return z
def outward(x):
    den=2**70
    return [str(F((x[0]*den).__floor__(),den)),str(F((x[1]*den).__ceil__(),den))]
def rounded(x):
    den=2**80
    return F((x[0]*den).__floor__(),den),F((x[1]*den).__ceil__(),den)
@lru_cache(maxsize=256)
def spectrum(v):return tuple(a*a for a in A.walsh(v))
@lru_cache(maxsize=256)
def ce(P,Q):
    g={}
    for p,q in zip(P,Q):
        if p:
            ck(q>0);g[q]=g.get(q,F(0))+p
    z=(F(0),F(0))
    for q,p in g.items():z=rounded(add(z,mul(p,A.log2(1/q))))
    return z
@lru_cache(maxsize=256)
def entropy(v):return ce(spectrum(v),spectrum(v))
def source(w):
    return tuple((-1 if x&((1<<w)-1)==0 else 1)*(-1 if x>>w==0 else 1) for x in range(1<<(w+2)))
def pointed(g,m):
    k=len(g).bit_length()-1
    v=[g[x&((1<<k)-1)] for x in range(1<<(k+m+1))]
    ck(v[0]==1);v[0]=-1
    return tuple(v)
def canonical(g,m):
    v=pointed(g,m);P=spectrum(g);k=len(g).bit_length()-1
    eps=F(1,1<<(k+m));s=sum(p>0 for p in P);W=2*eps-s*eps*eps
    Q=tuple((1-W)*P[x] if x<len(P) and P[x] else eps*eps for x in range(len(v)))
    ck(sum(Q)==1)
    return v,Q
def floor(w,m):
    g=source(w);v=pointed(g,m);P=spectrum(v);Pg=spectrum(g)
    N=len(v)//2;delta=F(1,N);beta=3*delta
    q=F(2,1<<w)
    explicit=tuple((1-q if s&((1<<w)-1)==0 else -q)*(F(1,2) if s>>w==0 else F(-1,2)) for s in range(len(g)))
    ck(tuple(A.walsh(g))==explicit)
    for s,a in enumerate(A.walsh(v)):ck(a==(explicit[s] if s<len(g) else F(0))-delta)
    ck(sum(P[N:])==delta)
    M=[((Pg[s] if s<len(Pg) else F(0))+beta/N)/(1+beta) for s in range(N)]
    marg=[P[s]+P[s+N] for s in range(N)]
    ck(min(marg)>0);Q=tuple(M[s%N]*P[s]/marg[s%N] for s in range(len(v)))
    ck(sum(Q)==1)
    return g,v,Q,delta

def history(w,m,d,eta):
    g,v,Q,delta=floor(w,m);Ig=A.influence(g);If=A.influence(v)
    G=(m+1)*delta;E=(w+2)*delta;B=G+E;c=entropy(g)
    ck(Ig==1+w*F(2,1<<w));ck(If==Ig+G-E);ck(E<=Ig/8);ck(c[1]<4*Ig)
    root=ce(spectrum(v),Q);ck(root[1]<=2*c[0]+15*B)
    ck(31*If-root[1]>=F(69,4)*Ig+16*G)
    U=F(69,8)*Ig;labels=tuple(range(w+3+m))
    leaves=[(F(1),v,Q,labels)];release=(F(0),F(0));signed=(F(0),F(0));complete_release=(F(0),F(0))
    positive_upper=F(0);fresh_upper=F(0);charges=[];frontiers=0
    def verify():
        nonlocal frontiers
        ck(sum(x[0] for x in leaves)==1)
        terminals=total(mul(p,ce(spectrum(z),qq)) for p,z,qq,l in leaves)
        ledger=add(release,terminals)
        full=add(complete_release,terminals)
        full_identity=sub(full,add(root,signed));ck(full_identity[0]<=0<=full_identity[1])
        ck(sub(full,ledger)[1]>=0)
        ck(full[1]<=root[1]+fresh_upper+F(1,1<<55))
        ck(31*If-U-full[1]>F(47,8)*Ig+16*G)
        div=total(mul(p,sub(ce(spectrum(z),qq),entropy(z))) for p,z,qq,l in leaves)
        equivalent=add(entropy(v),div);dif=sub(ledger,equivalent)
        ck(dif[0]<=0<=dif[1])
        ck(ledger[1]<=root[1]+fresh_upper+F(1,1<<55))
        ck(31*If-U-ledger[1]>F(47,8)*Ig+16*G)
        frontiers+=1
    def query(j,label):
        nonlocal release,complete_release
        p,z,qq,ll=leaves[j];i=ll.index(label)
        zs,qs=A.transport(z,qq,i);zs=[tuple(x) for x in zs];qs=[tuple(x) for x in qs]
        Hloss=sub(entropy(z),mul(F(1,2),add(entropy(zs[0]),entropy(zs[1]))))
        ck(Hloss[1]>=0)
        Dpar=sub(ce(spectrum(z),qq),entropy(z))
        Dav=mul(F(1,2),total(sub(ce(spectrum(zs[b]),qs[b]),entropy(zs[b])) for b in (0,1)))
        ck(sub(Dpar,Dav)[1]>=0)
        complete_loss=sub(ce(spectrum(z),qq),mul(F(1,2),total(ce(spectrum(zs[b]),qs[b]) for b in (0,1))))
        ck(complete_loss[1]>=0)
        complete_release=add(complete_release,mul(p,complete_loss))
        release=add(release,mul(p,Hloss));nl=ll[:i]+ll[i+1:]
        leaves[j:j+1]=[(p/2,zs[b],qs[b],nl) for b in (0,1)]
        verify()
        return j
    def reset(j,newQ,name):
        nonlocal signed,positive_upper,fresh_upper
        p,z,old,ll=leaves[j];P=spectrum(z)
        fresh=ce(P,newQ);oldce=ce(P,old);e=mul(p,sub(fresh,oldce))
        before=total(mul(a,ce(spectrum(b),c)) for a,b,c,l in leaves)
        leaves[j]=(p,z,newQ,ll)
        after=total(mul(a,ce(spectrum(b),c)) for a,b,c,l in leaves)
        identity=sub(sub(after,before),e);ck(identity[0]<=0<=identity[1])
        signed=add(signed,e);positive_upper+=max(F(0),e[1]);fresh_upper+=p*fresh[1]
        if name=='first_narrow_actual_floor_handoff' and d==0 and eta==F(1,4):ck(e[0]>0)
        charges.append({'name':name,'reach':str(p),'actual_signed_charge':outward(e),'fresh_reached_ce':outward(mul(p,fresh))})
        verify()
    verify()
    # Unique edited zero path; every one sibling stays with its actual reference.
    for j in range(d):query(0,j)
    t=w-d;rho=F(1,1<<d)
    query(0,w)
    g1=tuple((-1 if x&((1<<t)-1)==0 else 1)*(-1 if x>>t==0 else 1) for x in range(1<<(t+1)))
    cv,q1=canonical(g1,m);ck(cv==leaves[0][1])
    q1=tuple((1-eta)*a+eta/F(len(q1)) for a in q1)
    reset(0,q1,'first_narrow_actual_floor_handoff')
    ck(F(1,2)*rho*ce(spectrum(cv),q1)[1]<F(5,4))
    query(0,w+1)
    g2=tuple(1 if x==0 else -1 for x in range(1<<t))
    cv,q2=canonical(g2,m);ck(cv==leaves[0][1]);reset(0,q2,'second_narrow')
    ck(rho/4*ce(spectrum(cv),q2)[1]<F(1,2))
    for j in range(1,t+1):
        query(0,d+j-1);g3=tuple(1 if x==0 else -1 for x in range(1<<(t-j)))
        cv,q3=canonical(g3,m);ck(cv==leaves[0][1]);ck(ce(spectrum(cv),q3)[1]<4)
        reset(0,q3,'remaining_wide_'+str(j))
    ck(fresh_upper<F(11,4));ck(positive_upper<F(11,4))
    # A subsequent actual padding query has no reset; controls remain in its full bill.
    query(0,w+2)
    return {'w':w,'m':m,'d':d,'eta':str(eta),'frontiers':frontiers,'resets':len(charges),'actual_charges':charges,'sum_positive_upper':outward((positive_upper,positive_upper)),'sum_fresh_upper':outward((fresh_upper,fresh_upper)),'source_I':str(Ig),'full_I':str(If),'old_U':str(U),'guaranteed_reserve':str(F(47,8)*Ig+16*G)}

def main():
    pilot='pilot' in sys.argv
    domain=[(4,2,0,F(1,4))] if pilot else [(w,m,d,e) for w in (4,5) for m in (2,3) for d in range(w+1) for e in (F(0),F(1,4))]
    batch=None
    if '--batch' in sys.argv:
        batch=int(sys.argv[sys.argv.index('--batch')+1]);wm=[(4,2),(4,3),(5,2),(5,3)][batch]
        domain=[x for x in domain if x[:2]==wm]
    records=[history(*x) for x in domain]
    result={'status':'PASS','histories':len(records),'assertions':COUNT+A.NCHK,'frontiers':sum(x['frontiers'] for x in records),'resets':sum(x['resets'] for x in records),'runtime_seconds':time.perf_counter()-START,'helper_path':str(HELPER),'helper_sha256':hashlib.sha256(HELPER.read_bytes()).hexdigest(),'records':records,'scope':'finite exact reconstruction; all-dimensional extension is DERIVATION sections1-4'}
    name='PILOT.json' if pilot else ('BATCH_'+str(batch)+'.json' if batch is not None else 'EXACT_RESULTS.json')
    (RUN/'out'/name).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='records'}))
if __name__=='__main__':main()
