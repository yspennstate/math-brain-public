from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import comb,factorial
import json,time,sys
R=Path(__file__).resolve().parents[1]
start=time.monotonic(); counts={}
def ck(v,k):
    assert v,k
    counts[k]=counts.get(k,0)+1
    if time.monotonic()-start>55:raise RuntimeError('frozen runtime limit')
def fwht(v):
    a=v[:];h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h];a[j]=x+y;a[j+h]=x-y
        h*=2
    return a
def influence(v,n):
    return F(sum(v[x]!=v[x^(1<<i)] for x in range(1<<n) for i in range(n)),1<<n)
def spectral(v):
    w=fwht(v);den=len(v)**2
    return w,F(sum(i.bit_count()*x*x for i,x in enumerate(w)),den)
def graph_case(m,H):
    n=4*m;mask=(1<<m)-1;t=F(1,1<<m)
    hv=[int(any((z>>i&1) and (z>>(m+j)&1) for i,j in H)) for z in range(1<<(2*m))]
    p=F(sum(hv),len(hv));ih=influence(hv,2*m)
    old=[];new=[];delta=[];direct=[]
    for z in range(1<<n):
        l1=z&mask;r1=z>>m&mask;l2=z>>(2*m)&mask;r2=z>>(3*m)&mask
        f=bool(l1 and r1 or l2 and r2);g=bool(f or hv[l1|(r2<<m)])
        old.append(2*int(f)-1);new.append(2*int(g)-1);delta.append(2*int(g)-2*int(f))
        direct.append(2*hv[l1|(r2<<m)] if not r1 and not l2 else 0)
    ck(delta==direct,'actual_joint_cylinder')
    w0,i0=spectral(old);w1,i1=spectral(new);dw,energy=spectral(delta)
    ck(i0==influence(old,n) and i1==influence(new,n),'physical_spectral_influences')
    ck(all(c==b-a for a,b,c in zip(w0,w1,dw)),'spectral_perturbation')
    ck(sum(x*x for x in dw)==(1<<n)**2*4*t*t*p,'total_delta_energy')
    ck(energy==t*t*(4*m*p+ih),'degree_delta_energy')
    ck(i0==8*m*t*t*(1-t)*(2-t),'old_influence')
    ck(i1==i0+t*t*(ih-4*m*p),'new_influence_identity')
    ck(i1>=F(13,2)*m*t*t and i0/i1<=F(21,13),'joint_influence_bounds')
    ck(F(sum(x==-1 for x in new),len(new))== (2*t-t*t)**2-t*t*p,'actual_false_probability')
    v1=1-F(sum(new),len(new))**2
    ck(v1<=16*t*t,'variance_bound')
    ebound=4*t*t*p*(F(3*m,8)+6)+6*energy
    ck(ebound<=F(99,2)*m*t*t,'joint_occupation_bound')
    normalizer=v1*(F(3*m,16)+F(6,m))
    ck(normalizer<=F(54,13)*i1,'single_normalizer_bound')
    cert=2*F(71,8)*i0+2*ebound+normalizer
    ck(cert<49*i1,'complete_cost_upper_certificate')
    if len(H)==1:
        ck(i1==i0-(m-1)*t*t,'source_connector_physical_identity')
        ck(i1>=F(19,2)*m*t*t and i0/i1<=F(21,19),'source_connector_bounds')
    return dict(m=m,k=len(H),p=str(p),Ih=str(ih),I0=str(i0),I1=str(i1),delta_energy=str(energy),occupation_upper=str(ebound),complete_cost_upper_ratio=str(cert/i1))
def root_maps(m):
    collisions=0;histories=set()
    for partners in product(range(m),repeat=2*m):
        bad=any(partners[i]==j and partners[m+j]==i for i in range(m) for j in range(m))
        if bad:continue
        collisions+=1
        owned=[]
        for i in range(m):owned.append(((i,partners[i]),i))
        for j in range(m):owned.append(((partners[m+j],j),m+j))
        ck(len({e for e,v in owned})==2*m,'distinct_actual_root_gates')
        key=tuple(sorted(owned))
        ck(key not in histories,'distinct_actual_run_identity');histories.add(key)
        probability=(F(1,2*m)/32)**(2*m)
        ck(probability==F(1,(64*m)**(2*m)),'original_root_probability')
    expected=sum((-1)**k*comb(m,k)**2*factorial(k)*m**(2*m-2*k) for k in range(m+1))
    ck(collisions==expected,'root_maps_vs_inclusion_exclusion')
    ck(F(collisions,m**(2*m))>=F(1,8),'root_maps_lower_probability')
    return dict(m=m,total_maps=m**(2*m),collision_free=collisions)
def scalar_checks():
    for m in range(2,65):
        for s in range(m+1):
            for t in range(m+1):
                num=sum((-1)**k*comb(s,k)*comb(t,k)*factorial(k)*m**(s+t-2*k) for k in range(min(s,t)+1))
                ck(8*num>=m**(s+t),'all_selected_sizes_collision_bound')
        mu2=F((m-1)**2,2*m*m);mu3=F((m-1)**2*(m-2)**2,6*m**4)
        ck(mu2-mu3>=F(1,8),'third_bonferroni_uniform')
    ck(F(71,4)*F(21,13)+F(198,13)+F(54,13)==F(2499,52)<49,'final_constant')
    ck(F(1491,76)+F(91,38)+F(9,32)==F(13555,608)<23,'source_connector_constant')
    for m in range(2,257):
        t=F(1,1<<m)
        ck(3*m<=2*(1<<m),'source_log_induction')
        ck(F(32,13*m)*(F(3*m,16)+F(6,m))<=F(54,13),'normalizer_scalar')
        for k in range(1,m+1):
            lam=F(1,2*m)
            actual=m**(k-1)*(lam/48)*(lam/32)**(k-1)
            ck(actual==F(2,3*m)*F(1,64)**k,'source_double_root_numerator')
    for r in range(2,65):
        for m in range(2,65):
            u=F(1,1<<m);q=2*u-u*u
            i=r*q**(r-1)*4*m*u*(1-u);v=4*q**r*(1-q**r)
            ck(v/i<=F(7,3*r*m),'source_all_posterior_scaling')
            ck(m*u<=F(1,2),'source_component_occupation')
def component_projection():
    # All196 ordered signed nonconstant two-bit pairs; no source helper imports.
    fs=[[2*((mask>>x)&1)-1 for x in range(4)] for mask in range(1,15)]
    for a in fs:
        wa,ia=spectral(a);qa=F(a.count(-1),4)
        for b in fs:
            wb,ib=spectral(b);qb=F(b.count(-1),4)
            vals=[1 if a[x&3]==1 or b[x>>2]==1 else -1 for x in range(16)]
            w,i=spectral(vals)
            ck(i==qb*ia+qa*ib,'signed_component_influence')
            for s in range(1,4):
                ck(F(sum(w[s|(t<<2)]**2 for t in range(4)),256)==qb*F(wa[s]**2,16),'signed_component_marginal_left')
                ck(F(sum(w[t|(s<<2)]**2 for t in range(4)),256)==qa*F(wb[s]**2,16),'signed_component_marginal_right')
if __name__=='__main__':
    mode=sys.argv[1];rows=[]
    maps=[root_maps(2)]
    for mask in range(16):rows.append(graph_case(2,{(i,j) for i in range(2) for j in range(2) if mask>>(2*i+j)&1}))
    if mode=='full':
        maps.append(root_maps(3));component_projection();scalar_checks()
        for m in [3,4]:
            complete={(i,j) for i in range(m) for j in range(m)}
            fixtures=[complete,{(i,i) for i in range(m)},{(0,j) for j in range(m)},{(i,i) for i in range(m)}|{(i,(i+1)%m) for i in range(m)}]
            if m==3:fixtures=[set(),{(0,0)}]+fixtures
            for h in fixtures:rows.append(graph_case(m,h))
    result=dict(helper='A009-joint-connectors-v1',mode=mode,status='PASS',graphs=rows,root_maps=maps,counts=counts,total_checks=sum(counts.values()),elapsed_seconds=time.monotonic()-start)
    (R/'out'/f'{mode}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['graphs','root_maps']}))
