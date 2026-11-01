import itertools, math
import numpy as np

rng=np.random.default_rng(310031)
trials=3000
viol=0
diff_r=diff_c=double=0
max_mix=0.0
min_currency=float('inf')
min_double=float('inf')
for _ in range(trials):
    m=n=6
    B=rng.normal(size=(m,n))
    rowpairs=list(itertools.combinations(range(1,m),2))
    colpairs=list(itertools.combinations(range(1,n),2))
    terms=[]; J=0.0
    for R2 in rowpairs:
        for T2 in colpairs:
            d=float(np.linalg.det(B[np.ix_((0,)+R2,(0,)+T2)]))
            w=d*d; terms.append((R2,T2,w)); J+=w
    qr=np.zeros(m); qc=np.zeros(n)
    for R2,T2,w in terms:
        for h in R2: qr[h]+=w/J
        for k in T2: qc[k]+=w/J
    dr=qr[1:].max()<=0.6+1e-12
    dc=qc[1:].max()<=0.6+1e-12
    diff_r+=int(dr); diff_c+=int(dc)
    if dr:
        mix=np.zeros(m); mix[0]=0.5; mix[1:]=(5.0/6.0)*qr[1:]
        max_mix=max(max_mix,float(mix.max()))
        if mix.max()>0.5000000001: viol+=1
        rho2=float(B[0]@B[0])
        eta={R:0.0 for R in rowpairs}
        for R2,T2,w in terms: eta[R2]+=w/J
        H=0.0; avg=0.0
        for R,e in eta.items():
            if e==0: continue
            D=0.0
            for U in itertools.combinations(range(n),2):
                d=float(np.linalg.det(B[np.ix_(R,U)])); D+=d*d
            H-=e*math.log(e); avg+=e*math.log(D)
        Knu=math.exp(H+avg)
        ratio=Knu/(J/rho2)
        min_currency=min(min_currency,ratio)
        if ratio<1-1e-9: viol+=1
    if (not dr) and (not dc):
        double+=1
        h=1+int(np.argmax(qr[1:])); k=1+int(np.argmax(qc[1:]))
        G=sum(w for R,T,w in terms if h in R and k in T)
        ratio=G/J; min_double=min(min_double,ratio)
        if ratio<=0.2-1e-12: viol+=1

M=2**(2/3)*math.sqrt(3)
C_density=26*math.sqrt(math.e)*M**(-3/13)
C_half=(30/7)*2**(9/10)*3**(-1/20)*math.exp(13/60)
C_partner=2**(5/3)*3**(1/4)*math.exp(1/4)
print('trials',trials)
print('diffuse_rows',diff_r,'diffuse_cols',diff_c,'double_cases',double)
print('violations',viol)
print('max_mixed_row_marginal',max_mix)
print('min_Knu_over_J_rho2',min_currency)
print('min_double_anchor_ratio',min_double)
print('C_density',C_density)
print('C_half_riesz',C_half)
print('C_partner_hybrid',C_partner)
print('C_partner_after_G_gt_Z15',C_partner*15**(1/8))
