from pathlib import Path
from fractions import Fraction as F
import json,time,sys
R=Path(__file__).resolve().parents[1];start=time.monotonic();counts={}
def ck(v,k):
    assert v,k
    counts[k]=counts.get(k,0)+1
    if time.monotonic()-start>55:raise RuntimeError('frozen cap')
def fwht(v):
    a=v[:];h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h];a[j]=x+y;a[j+h]=x-y
        h*=2
    return a
def infl(v,n):return F(sum(v[x]!=v[x^(1<<i)] for x in range(1<<n) for i in range(n)),1<<n)
def spec(v):
    w=fwht(v)
    return w,F(sum(i.bit_count()*x*x for i,x in enumerate(w)),len(v)**2)
def case(m,H,K):
    n=4*m;mask=(1<<m)-1;t=F(1,1<<m)
    h=[int(any((x>>i&1) and (x>>(m+j)&1) for i,j in H)) for x in range(1<<(2*m))]
    k=[int(any((x>>i&1) and (x>>(m+j)&1) for i,j in K)) for x in range(1<<(2*m))]
    P=F(sum(h)+sum(k),len(h));J=infl(h,2*m)+infl(k,2*m)
    old=[];new=[];d=[];d1=[];d2=[]
    for x in range(1<<n):
        l=x&mask;r=x>>m&mask;u=x>>(2*m)&mask;v=x>>(3*m)&mask
        a=bool(l and r or u and v)
        z1=2*h[l|(v<<m)] if not r and not u else 0
        z2=2*k[u|(r<<m)] if not v and not l else 0
        b=bool(a or h[l|(v<<m)] or k[u|(r<<m)])
        old.append(2*int(a)-1);new.append(2*int(b)-1)
        d.append(2*int(b)-2*int(a));d1.append(z1);d2.append(z2)
    ck(all(c==a+b for a,b,c in zip(d1,d2,d)),'joint_actual_cylinders')
    ck(not any(a and b for a,b in zip(d1,d2)),'disjoint_changed_supports')
    w0,i0=spec(old);w1,i1=spec(new);wd,en=spec(d);wa,ea=spec(d1);wb,eb=spec(d2)
    ck(i0==infl(old,n) and i1==infl(new,n),'direct_flip_vs_Walsh')
    ck(sum(i.bit_count()*a*b for i,(a,b) in enumerate(zip(wa,wb)))==0,'exact_Dirichlet_cross_zero')
    ck(en==ea+eb==t*t*(4*m*P+J),'joint_energy_identity')
    ck(sum(a*a for a in wd)==len(d)**2*4*t*t*P,'joint_total_mass')
    ck(i1==i0+t*t*(J-4*m*P),'actual_influence_change')
    ck(i0==8*m*t*t*(1-t)*(2-t),'old_influence')
    q=F(new.count(-1),len(new));v1=4*q*(1-q)
    ck(q==(2*t-t*t)**2-t*t*P,'false_probability')
    ck(P<=2*(1-t)**2,'both_free_sides_nonempty')
    ck(i1>=8*m*t*t*(1-t)>=6*m*t*t and i0/i1<2,'influence_floor')
    occupation=4*t*t*P*(F(3*m,8)+6)+6*en
    ck(occupation<=99*m*t*t,'complete_joint_occupation')
    normalizer=v1*(F(3*m,8)+F(6,m))
    ck(normalizer<=5*i1,'one_root_increment')
    cert=2*F(71,8)*i0+2*occupation+normalizer
    ck(cert<F(147,2)*i1,'final_complete_cost_certificate')
    return dict(m=m,k12=len(H),k21=len(K),P=str(P),J=str(J),I0=str(i0),I1=str(i1),occupation_upper=str(occupation),cost_upper_ratio=str(cert/i1))
mode=sys.argv[1];rows=[]
graphs=[{(i,j) for i in range(2) for j in range(2) if mask>>(2*i+j)&1} for mask in range(16)]
for h in graphs:
    for k in graphs:rows.append(case(2,h,k))
if mode=='full':
    for m in [3,4]:
        complete={(i,j) for i in range(m) for j in range(m)};diag={(i,i) for i in range(m)}
        row={(0,j) for j in range(m)};col={(i,0) for i in range(m)}
        cycle=diag|{(i,(i+1)%m) for i in range(m)}
        fixtures=[(complete,complete),(diag,diag if m==3 else {(i,(i+1)%m) for i in range(m)}),(row,col),(cycle,{(j,i) for i,j in cycle} if m==3 else cycle)]
        if m==3:fixtures=[(set(),set()),({(0,0)},{(0,0)})]+fixtures
        for h,k in fixtures:rows.append(case(m,h,k))
    for m in range(2,257):
        t=F(1,1<<m)
        ck(8*(1-t)>=6,'all_m_floor_scalar')
        ck(1+F(16,m*m)<=5,'all_m_root_scalar')
    ck(2*F(71,8)*2+F(2*99,6)+5==F(147,2)<74,'all_m_final_constant')
result=dict(helper='A009-bidirectional-connectors-v1',status='PASS',mode=mode,graphs=rows,counts=counts,total_checks=sum(counts.values()),elapsed_seconds=time.monotonic()-start)
(R/'out'/f'{mode}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='graphs'}))
