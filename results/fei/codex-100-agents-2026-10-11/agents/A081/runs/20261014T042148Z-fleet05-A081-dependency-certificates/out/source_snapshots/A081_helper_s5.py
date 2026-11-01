from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json, time, sys
R=Path(__file__).resolve().parents[1]
checks=0
def ck(v):
    global checks
    checks+=1
    assert v,checks
def factors(n):
    ans={};p=2
    while p*p<=n:
        while n%p==0:ans[p]=ans.get(p,0)+1;n//=p
        p+=1
    if n>1:ans[n]=ans.get(n,0)+1
    return ans
def addlog(ans,q,c):
    for n,s in ((q.numerator,1),(q.denominator,-1)):
        for p,k in factors(n).items():ans[p]+=s*k*c
def clean(a):return {p:c for p,c in a.items() if c}
def kl(mu,ref):
    ans=defaultdict(F)
    for k,v in mu.items():
        if v:ck(ref[k]>0);addlog(ans,v/ref[k],v)
    return clean(ans)
def scaled(a,c):return clean({p:v*c for p,v in a.items()})
def minus(a,b):
    out=defaultdict(F,a)
    for p,v in b.items():out[p]-=v
    return clean(out)
def spectrum(table):
    N=len(table)
    return [F(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(table)),N) for s in range(N)]
def push(law,part):
    out=defaultdict(F)
    for k,v in law.items():out[part(k)]+=v
    return dict(out)
def encode(a):return {str(p):str(v) for p,v in a.items()}
start=time.perf_counter();pilot='--pilot' in sys.argv
gates=[(r,m) for r in (1,2) for m in range(1<<(1<<r))]+[(3,m) for m in (1,7,105,150)]
cores=[4] if pilot else [4,6]
if pilot:gates=[(2,7)]
rows=0;cases=0;positive=0;witness=None
for d in cores:
    delta=F(1,1<<d);t=F(1,1<<(d//2))
    b=[-1 if sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(d//2))%2 else 1 for y in range(1<<d)]
    bs=spectrum(b);sig=[int(v/t) for v in bs];ck(all(s in (-1,1) for s in sig))
    for r,m in gates:
        gt=[1 if (m>>x)&1 else -1 for x in range(1<<r)];a=spectrum(gt)
        table=[gt[z>>d] if z% (1<<d)==0 else b[z% (1<<d)] for z in range(1<<(d+r))]
        hat=spectrum(table);p=[v*v for v in hat];ck(sum(p)==1)
        for z in range(len(p)):
            core=z% (1<<d);V=z>>d
            ck(hat[z]==(sig[core]*t if V==0 else 0)+delta*(a[V]-(1 if V==0 else 0)))
        influences=[F(sum(table[z]!=table[z^(1<<j)] for z in range(len(table))),len(table)) for j in range(d+r)]
        coreinf=F(1,2)+delta*(1-a[0])
        ck(all(e==coreinf for e in influences[:d]))
        gate_bound=F(0)
        for i in range(r):
            E=sum(a[V]**2 for V in range(1<<r) if (V>>i)&1);e=delta*E
            ck(influences[d+i]==e)
            if not e:continue
            rows+=1
            keys=[z for z in range(len(p)) if not (z>>(d+i))&1]
            mu={z:p[z|(1<<(d+i))]/e for z in keys};ref={z:p[z]+p[z|(1<<(d+i))] for z in keys}
            ck(sum(mu.values())==sum(ref.values())==1)
            full=kl(mu,ref)
            signed=lambda z:(z>>d,sig[z%(1<<d)])
            mask=lambda z:z>>d
            ck(full==kl(push(mu,signed),push(ref,signed)))
            coarse=kl(push(mu,mask),push(ref,mask));loss=scaled(minus(full,coarse),e)
            rho=1-delta+delta*(a[0]**2+a[1<<i]**2)
            D0=defaultdict(F);cvals=[]
            for s in (-1,1):
                N=((1<<d)+s*(1<<(d//2)))//2
                c=(s+t*(a[0]-1))**2+delta*a[1<<i]**2;cvals.append(c)
                ck(c>=F(1,4));ck(rho<=1);ck(rho/c<=4)
                addlog(D0,rho/c,N*delta)
            ck(sum(F(((1<<d)+s*(1<<(d//2)))//2)*delta*c for s,c in zip((-1,1),cvals))==rho)
            ck(loss==scaled(clean(D0),delta*a[1<<i]**2))
            gate_bound+=2*delta*a[1<<i]**2
            positive+=bool(loss)
            if d==4 and r==2 and m==7 and i==0:
                children=[[table[z] for z in range(len(table)) if ((z&1)==bit)] for bit in (0,1)]
                childI=[]
                for child in children:
                    I=sum(F(sum(child[x]!=child[x^(1<<j)] for x in range(len(child))),len(child)) for j in range(d+r-1))
                    childI.append(I);ck(12*I>=d+r-1)
                ck(bool(loss));ck(cvals[0]!=cvals[1])
                witness={'d':d,'r':r,'gate_positive_table_mask':m,'gate_row':i,'loss_prime_log_coefficients':encode(loss),'core_influence':str(coreinf),'child_influences':list(map(str,childI)),'C':12,'child_dimension':d+r-1,'complete_subprobability_reference':'Q_b=P_b*2^(H_b-12 I_b)','CE_b':'12 I_b exactly','unused_child_surplus':'0 exactly','lost_refund':'strictly positive by unequal conditional laws and KL equality case'}
        ck(gate_bound<=2*delta);ck(2*delta<=coreinf/4);cases+=1
out={'status':'PASS','helper_version':'A081-signed-partition-v1','pilot':pilot,'cases':cases,'relevant_gate_rows':rows,'positive_exact_losses':positive,'assertions':checks,'runtime_seconds':time.perf_counter()-start,'arithmetic':'direct integer character sums, Fraction, exact prime-log coefficient identities; analytic KL equality and log-ratio upper bound','owner_availability_witness':witness}
(R/'out'/('PILOT.json' if pilot else 'EXACT_SIGNED_PARTITION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
