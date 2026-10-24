#!/usr/bin/env python3
from math import exp, comb
from collections import defaultdict

def pois_tail_gt(mu,K):
    p=exp(-mu)
    for k in range(1,K+2): p*=mu/k
    return p/(1.0-mu/(K+2))

def candidate(alpha,K):
    mu=1.5*alpha
    pp=[exp(-mu)]
    for k in range(1,K+1): pp.append(pp[-1]*mu/k)
    EZ=0.0; zw=[]
    for z in range(1,K+1):
        w=pp[z]*pp[z]; EZ+=z*w; zw.append((z,z,z*w))
        for m in range(z+1,K+1):
            w=2.0*pp[z]*pp[m]; EZ+=z*w; zw.append((z,m,z*w))
    q=EZ/(2.0*mu); q2=q*q
    pB=q2; pC=2*q*(1-q); pD=(1-q)*(1-q)
    remC=pC/(1-pB); remD=pD/(1-pB)
    joint=[]
    for z,m,num in zw:
        wt=num/EZ
        pS=[comb(z-1,s)*q2**s*(1-q2)**(z-1-s) for s in range(z)]
        pBs=[comb(m,B)*pB**B*(1-pB)**(m-B) for B in range(m+1)]
        for s,ps in enumerate(pS):
            A=1+s
            for B,pb in enumerate(pBs):
                pr=wt*ps*pb
                C=(m-B)*remC; D=(m-B)*remD
                joint.append((A,B,C,D,z,m,pr))
    pt=pois_tail_gt(mu,K)
    palm_tail_prob=(4*mu*pt)/EZ
    return mu,q,EZ,joint,palm_tail_prob

def select(joint,k,keyfn):
    mass=defaultdict(float)
    for A,B,C,D,z,m,p in joint: mass[keyfn(A,B,C,D,m)]+=p
    greater={}; tail=0.0
    for key in reversed(sorted(mass)):
        greater[key]=tail; tail+=mass[key]
    sums=[0.0]*6; sb=defaultdict(float)
    for A,B,C,D,z,m,p in joint:
        key=keyfn(A,B,C,D,m); peq=mass[key]; pgt=greater[key]
        sel=sum(comb(k-1,r)*peq**r*pgt**(k-1-r)/(r+1) for r in range(k))
        w=k*p*sel
        for i,v in enumerate((A,B,C,D,z,m)): sums[i]+=w*v
        sb[(A-1,B)] += w
    A,B,C,D,z,m=sums
    return dict(A=A,B=B,C=C,D=D,Z=z,M=m,net=B-A,sb=sb,mass=sum(sb.values()))

def zero_absorb_prob(desc,root):
    p=0.0
    for _ in range(300):
        new=sum(w*(p**B) for (S,B),w in desc['sb'].items() if S==0)
        if abs(new-p)<1e-16: p=new; break
        p=new
    p_root_one=sum(w*(p**B) for (S,B),w in root['sb'].items() if S==0)
    return p,p_root_one,1-p_root_one

def run(alpha,K,keyfn):
    mu,q,EZ,joint,palm_tail=candidate(alpha,K)
    root=select(joint,3,keyfn); desc=select(joint,2,keyfn)
    r=desc['B']; assert r<1
    fac=root['B']/(1-r)
    tot={x:root[x]+fac*desc[x] for x in ['A','B','C','D','Z','M','net']}
    flips=1+fac; absorb=-tot['net']
    p0,p1,pge2=zero_absorb_prob(desc,root)
    u=alpha*q**3
    return dict(q=q,u=u,palm_tail=palm_tail,root=root,desc=desc,r=r,flips=flips,absorb=absorb,
                load_per_A=flips/absorb,ideal_flip_density=u*flips/absorb,
                M_per_A=tot['M']/absorb,C_per_A=tot['C']/absorb,D_per_A=tot['D']/absorb,
                p0=p0,p1=p1,pge2=pge2,tot=tot)

def show(label,d):
    print(label)
    for k in ['q','u','r','flips','absorb','load_per_A','ideal_flip_density','M_per_A','C_per_A','D_per_A','p0','p1','pge2','palm_tail']:
        print(f'{k}={d[k]:.15g}')
    print(f"root_A={d['root']['A']:.15g} root_B={d['root']['B']:.15g} root_M={d['root']['M']:.15g}")
    print(f"desc_A={d['desc']['A']:.15g} desc_B={d['desc']['B']:.15g} desc_M={d['desc']['M']:.15g}")

KEY_NEW=lambda A,B,C,D,M:(B-A,M,B)
KEY_MINB=lambda A,B,C,D,M:(B,)

print('CONTROLLER_NEW_KEY=(B-A, M, B) lexicographic')
for alpha in (3.52,3.6,4.4898):
    d30=run(alpha,30,KEY_NEW); d35=run(alpha,35,KEY_NEW)
    print(f'\nalpha={alpha}')
    show('NEW_K35',d35)
    stab=max(abs(d30[k]-d35[k]) for k in ['q','r','flips','absorb','load_per_A','M_per_A','C_per_A','D_per_A','pge2'])
    print(f'max_abs_K30_K35_change={stab:.3e}')

print('\nalpha=3.6 comparison_to_minbreak')
new=run(3.6,35,KEY_NEW); old=run(3.6,35,KEY_MINB)
show('MINB_K35',old); show('NEW_K35',new)
print(f"relative_load_per_A_reduction={1-new['load_per_A']/old['load_per_A']:.15g}")
print(f"relative_M_per_A_reduction={1-new['M_per_A']/old['M_per_A']:.15g}")
print(f"relative_C_per_A_reduction={1-new['C_per_A']/old['C_per_A']:.15g}")
print(f"relative_D_per_A_reduction={1-new['D_per_A']/old['D_per_A']:.15g}")
print('ALL_DIAGNOSTICS_COMPLETE')
