"""Independent exact law audit; no upstream numerical helper imported."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,hashlib,math,sys
RUN=Path(__file__).resolve().parents[1]
def save(name,obj):
    (RUN/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
pilot='--pilot' in sys.argv
spec={'helper_version':'A081-independent-law-audit-v1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'family':'All labelled signs on n=0,1,2 plus fixed n=3 masks 1,7,105,150; finite physical stopping trees and fresh-parity tensor point activations','domain':{'seeds':26,'tree_policies':['one singleton then stop','adaptive up to two singleton queries','one full physical block'],'leaf_modes':['actual','half actual plus half uniform','same smooth law scaled by 1/3','history-dependent smooth subprobability'],'activation_seeds':22,'tensor_m':[1,2],'parity_ell':[2,3],'controls_k':[1,2]},'case_count':{'trees':312,'activations':176,'debt_sign_witness':1},'pilot_domain':'all n<=1 seeds, same tree/reference modes; activations n<=1,m=1,ell=2,k=1','symmetry':'none','arithmetic':'Integer direct character sums (no FWHT), Fraction probabilities/influence, exact prime-log coefficient dictionaries; no numerical logarithms','memory_estimate_MB':64,'maximum_runtime_seconds':60,'automatic_dimension_increase':False}
save('FROZEN_SPEC.json',spec)
start=time.perf_counter(); checks=0
def check(cond):
    global checks
    assert cond
    checks+=1
    if time.perf_counter()-start>60:raise RuntimeError('Frozen runtime cap')
@lru_cache(None)
def factors(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0:out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def add(a,b,scale=F(1)):
    c=dict(a)
    for p,v in b.items():c[p]=c.get(p,F(0))+scale*v
    return {p:v for p,v in c.items() if v}
def log(q,scale=F(1)):
    q=F(q); assert q>0
    return add({p:scale*v for p,v in factors(q.numerator).items()},{p:scale*v for p,v in factors(q.denominator).items()},F(-1))
def ce(p,q):
    ans={}
    for s,mass in enumerate(p):
        if mass:ans=add(ans,log(q[s],-mass))
    return ans
def ent(p):return ce(p,p)
def kl(p,q):return add(ce(p,q),ent(p),F(-1))
def phi(a,b):
    if not a or not b:return {}
    return add(add(log(a,-a),log(b,-b)),log(a+b,a+b))
def walsh(vals):
    N=len(vals)
    return [F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(vals)),N) for s in range(N)]
def spectrum(vals):return [a*a for a in walsh(vals)]
def infl(p):return sum(F(s.bit_count())*v for s,v in enumerate(p))
def bi(p,i,ell=0):
    ans={}
    for s,a in enumerate(p):
        if not s&(1<<i) and s.bit_count()>=ell:ans=add(ans,phi(a,p[s|(1<<i)]))
    return ans
def agg(p,ell=0):
    ans={}
    for i in range((len(p)-1).bit_length()):ans=add(ans,bi(p,i,ell))
    return ans
def physical_inf(vals,i):return F(sum(vals[x]!=vals[x^(1<<i)] for x in range(len(vals))),len(vals))
def restrict(vals,A,y):
    n=(len(vals)-1).bit_length(); C=[i for i in range(n) if i not in A]; out=[]
    for z in range(1<<len(C)):
        x=sum(((z>>j)&1)<<i for j,i in enumerate(C))+sum(((y>>j)&1)<<i for j,i in enumerate(A))
        out.append(vals[x])
    return out
def split_index(s,A,n):
    C=[i for i in range(n) if i not in A]
    return sum(((s>>i)&1)<<j for j,i in enumerate(A)),sum(((s>>i)&1)<<j for j,i in enumerate(C))
def tree(vals,policy,mode,depth=0,path=()):
    n=(len(vals)-1).bit_length(); P=spectrum(vals)
    check(sum(P)==1)
    stop=n==0 or (policy==0 and depth>=1) or (policy==1 and depth>=2) or (policy==2 and depth>=1)
    if stop:
        smooth=[(v+F(1,len(P)))/2 for v in P]
        Q=P if mode==0 else smooth
        scale=F(1,3) if mode==2 else (F(2+(sum(path)%2),4) if mode==3 else F(1))
        Q=[scale*v for v in Q]
        return {'P':P,'Q':Q,'B':{},'J':{},'K':{},'terminalCE':ce(P,Q),'terminalKL':kl(P,Q),'terminalH':ent(P),'removed':F(0),'terminalI':infl(P),'leaves':1}
    if policy==2:A=list(range(n))
    elif policy==0:A=[0]
    else:A=[max(range(n),key=lambda i:(physical_inf(vals,i),-i))]
    children=[tree(restrict(vals,A,y),policy,mode,depth+1,path+(y,)) for y in range(1<<len(A))]
    M=len(children); size=len(children[0]['P'])
    q=[sum(c['P'][t] for c in children)/M for t in range(size)]
    r=[sum(c['Q'][t] for c in children)/M for t in range(size)]
    Q=[F(0)]*len(P)
    for s,mass in enumerate(P):
        u,t=split_index(s,A,n)
        if q[t]:Q[s]=mass*r[t]/q[t]
        elif u==0:Q[s]=r[t] # declared zero-true-fiber kernel: point mass U=0
    check(sum(Q)==sum(sum(c['Q']) for c in children)/M)
    check(all(Q[s]>0 for s,mass in enumerate(P) if mass))
    blockB=add(ent(P),ent(q),F(-1))
    blockJ=ent(q); localK={}
    for c in children:blockJ=add(blockJ,ent(c['P']),F(-1,M))
    for t,mass in enumerate(q):
        if mass:
            kp=[c['P'][t]/(M*mass) for c in children];kq=[c['Q'][t]/(M*r[t]) for c in children]
            check(sum(kp)==sum(kq)==1)
            localK=add(localK,kl(kp,kq),mass)
    averageCE={};averageKL={}
    for c in children:
        averageCE=add(averageCE,ce(c['P'],c['Q']),F(1,M));averageKL=add(averageKL,kl(c['P'],c['Q']),F(1,M))
    check(ce(P,Q)==add(add(add(blockB,blockJ),averageCE),localK,F(-1)))
    check(kl(P,Q)==add(averageKL,localK,F(-1)))
    result={'P':P,'Q':Q,'B':blockB,'J':blockJ,'K':localK,'terminalCE':{},'terminalKL':{},'terminalH':{},'removed':sum(physical_inf(vals,i) for i in A),'terminalI':F(0),'leaves':0}
    for c in children:
        for label in ['B','J','K','terminalCE','terminalKL','terminalH']:result[label]=add(result[label],c[label],F(1,M))
        result['removed']+=c['removed']/M;result['terminalI']+=c['terminalI']/M;result['leaves']+=c['leaves']
    check(ce(P,Q)==add(add(add(result['B'],result['J']),result['terminalCE']),result['K'],F(-1)))
    check(result['K']==add(result['terminalKL'],kl(P,Q),F(-1)))
    check(infl(P)==result['removed']+result['terminalI'])
    check(ent(P)==add(add(result['B'],result['J']),result['terminalH']))
    return result
seeds=[(n,mask,[(-1 if (mask>>x)&1 else 1) for x in range(1<<n)]) for n in range(3) for mask in range(1<<(1<<n))]
extra=[(3,mask,[(-1 if (mask>>x)&1 else 1) for x in range(8)]) for mask in [1,7,105,150]]
treecases=0; nonzeroK=0; positiveTerminal=0
for n,mask,vals in (seeds[:6] if pilot else seeds+extra):
    for policy in range(3):
        results=[tree(vals,policy,mode) for mode in range(4)]
        for result in results:
            treecases+=1
            if result['K']:nonzeroK+=1
            if result['terminalH']:positiveTerminal+=1
        check(results[0]['K']=={})
        check(results[1]['K']==results[2]['K'])
        check(ce(results[0]['P'],results[2]['Q'])==add(ce(results[0]['P'],results[1]['Q']),log(F(3))))
activationcases=0
domain=seeds[:6] if pilot else seeds
for n,mask,seed in domain:
    for m in ([1] if pilot else [1,2]):
        for ell in ([2] if pilot else [2,3]):
            for k in ([1] if pilot else [1,2]):
                d=m*n+ell;N=d+k;core=[]
                for x in range(1<<d):
                    v=-1 if (x>>(m*n)).bit_count()%2 else 1
                    for j in range(m):v*=seed[(x>>(j*n))&((1<<n)-1)]
                    core.append(v)
                vals=[core[x&((1<<d)-1)] if x>>d==0 else 1 for x in range(1<<N)]
                P=spectrum(vals);pseed=spectrum(seed);q=F(1,1<<k)
                check(sum(P)==1);check(infl(P)==q*(m*infl(pseed)+ell+k))
                data={}
                for i in range(d):data=add(data,bi(P,i))
                check(data==add({},agg(pseed),q*m))
                target=add({},agg(pseed),q*m)
                count=sum(math.comb(k-1,r) for r in range(ell,k))
                target=add(target,log(F(2),k*q+2*k*q*q*count))
                check(agg(P,ell)==target)
                check(agg(P,2)==add(add({},agg(pseed),q*m),log(F(2),2*k*q*(1-k*q))))
                for i in range(m*n,d):check(bi(P,i)=={} and physical_inf(vals,i)==q)
                activationcases+=1
                if not pilot:check(N<=9)
# Tiny exact sign witness: parent and both children satisfy H<=2I, slack still has wrong drift.
vals=[-1,1,1,1]; P=spectrum(vals); children=[spectrum(restrict(vals,[0],y)) for y in range(2)]
check(ent(P)=={2:F(2)} and infl(P)==1)
check([ent(c) for c in children]==[{},{}])
d=physical_inf(vals,0);Q0=2*infl(P)-2;Qchild=sum(2*infl(c) for c in children)/2
check(d==F(1,2) and Q0==0 and Qchild==1)
check(2>2*d+Q0-Qchild)
out={'status':'PASS','pilot':pilot,'assertions':checks,'tree_cases':treecases,'nonzero_credit_cases':nonzeroK,'nonzero_terminal_entropy_cases':positiveTerminal,'activation_cases':activationcases,'runtime_seconds':time.perf_counter()-start,'maximum_activation_dimension':9 if not pilot else 4,'debt_sign_witness':{'truth_table':vals,'C':2,'H':2,'I':1,'queried_influence':'1/2','entropy_drop':2,'root_slack':0,'average_child_slack':1,'claimed_debt_RHS':0},'hash_convention':{'graph':'canonical JSON statement+hypotheses','statement_only':'SHA256 UTF8 exact_statement; external receipts distinguish this explicitly'},'semantic_scope':'Independent analytic proof supplies all-dimensional quantifiers, not finite extrapolation.'}
save('PILOT.json' if pilot else 'EXACT_AUDIT.json',out);print(json.dumps(out,indent=2))
