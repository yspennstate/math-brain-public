#!/usr/bin/env python3
import math
import mpmath as mp

DPS=1300
KMAX=2300
R=11
TAUR=4
SCALE=1000
STEP_STR='0.000005'
TMAX_STR='0.02'
mp.iv.dps=DPS
Z=mp.iv.mpf([0,0]); O=mp.iv.mpf([1,1]); S=mp.iv.mpf([SCALE,SCALE])

def q(n,d): return mp.iv.mpf([n,n])/d
def dec(s): return mp.iv.mpf([s,s])
def contains_zero(x): return bool(x.a <= 0 <= x.b)

def solve_interval(A,b):
    n=len(A); M=[[A[i][j] for j in range(n)] for i in range(n)]; y=[b[i] for i in range(n)]; piv=[]
    for k in range(n):
        p=M[k][k]
        if contains_zero(p): raise RuntimeError(f'pivot contains zero at {k}: {p}')
        piv.append(p)
        for i in range(k+1,n):
            f=M[i][k]/p; M[i][k]=Z
            for j in range(k+1,n): M[i][j]=M[i][j]-f*M[k][j]
            y[i]=y[i]-f*y[k]
    x=[Z for _ in range(n)]
    for i in range(n-1,-1,-1):
        s=y[i]
        for j in range(i+1,n): s=s-M[i][j]*x[j]
        if contains_zero(M[i][i]): raise RuntimeError(f'back pivot contains zero at {i}')
        x[i]=s/M[i][i]
    return x,piv

def poly_mul(A,B):
    out=[Z for _ in range(len(A)+len(B)-1)]
    for i,a in enumerate(A):
        for j,b in enumerate(B): out[i+j]=out[i+j]+a*b
    return out

def lagrange_weights(nodes,moments):
    n=len(nodes); out=[]
    for i in range(n):
        numpoly=[O]; den=O
        for j in range(n):
            if j==i: continue
            numpoly=poly_mul(numpoly,[-nodes[j],O]); den=den*(nodes[i]-nodes[j])
        num=Z
        for rr,cc in enumerate(numpoly): num += cc*moments[rr]
        out.append(num/den)
    return out

def signs_for_roots(poly,centers,degree,eps):
    roots=[]; tuples=[]; ok=True
    for i,cs in enumerate(centers):
        c=dec(cs); lo=c-eps; hi=c+eps
        plo=poly(lo); phi=poly(hi)
        tup=(bool(plo.b<0),bool(plo.a>0),bool(phi.b<0),bool(phi.a>0))
        tuples.append(tup)
        roots.append(mp.iv.mpf([lo.a,hi.b]))
        left_neg=((degree-i)%2==1)
        if left_neg:
            ok=ok and tup[0] and tup[3]
        else:
            ok=ok and tup[1] and tup[2]
    return roots,tuples,ok

alpha=q(2743038,625000)
vals=[q(651,100000),q(789,10000),O/2,q(9211,10000),q(99349,100000)]
probs=[q(5581,100000),q(3669,20000),q(13037,25000),q(3669,20000),q(5581,100000)]
lam=3*alpha/2
pair=[(probs[i]*probs[j],O-vals[i]*vals[j]) for i in range(5) for j in range(5)]
NEED=KMAX+30
EZ=[O]; pows=[O for _ in pair]
for jj in range(1,NEED+1):
    m=Z
    for idx,(wt,base) in enumerate(pair):
        pows[idx]=pows[idx]*base; m=m+wt*pows[idx]
    EZ.append(mp.iv.exp(lam*(m-O)))
arr=EZ; mus=[O]; series=Z; allpos=True
for k in range(1,NEED+1):
    arr=[arr[j+1]-arr[j] for j in range(len(arr)-1)]
    mu=arr[0] if k%2==0 else -arr[0]
    mus.append(mu); allpos=allpos and bool(mu.a>0)
    if k<=KMAX: series += mu*mu/k
L=Z
for i in range(5):
    for j in range(5):
        for h in range(5):
            L += probs[i]*probs[j]*probs[h]*mp.iv.log(O-vals[i]*vals[j]*vals[h])
AK=-series-2*alpha*L; muK=mus[KMAX]
sx=[(mus[KMAX+j]/muK)**2 for j in range(31)]
my=[]
for j in range(31):
    v=Z
    for ell in range(j+1):
        term=mp.iv.mpf([math.comb(j,ell),math.comb(j,ell)])*sx[ell]
        v=v-term if ell%2 else v+term
    my.append((S**j)*v)
wm=[my[j]-my[j+1]/S for j in range(30)]
H=[[wm[a+b] for b in range(R)] for a in range(R)]
rhs=[-wm[a+R] for a in range(R)]
coef,pivots=solve_interval(H,rhs)

def pbase(y):
    out=y+coef[R-1]
    for j in range(R-2,-1,-1): out=out*y+coef[j]
    return out
base_centers=[
'0.1095949740980931770687836320141025039643846866225158787598237885512325043414529306412440049856897659',
'0.3919257891640474546918537564450615214019980468569503532290606365021454289580471969734839706315396109',
'0.8558306864792507828446710767502847445159935686482875514646815303322637651942071549212595948648155077',
'1.515313613895239180853207307220905664955385487468426855156002723027455272660760920751709145509838511',
'2.381501191730155663714226110140517878391988602643296704902652654245962815056479923119458177736709221',
'3.476283222402723491323938874267081371759412178986493453809201253592111123933585318376049395070406576',
'4.831991734441718096573314769444115498673197951506915804052116109845720485937188210055317171123657604',
'6.499828690359182483422662719749883612351773642153519416137076375105681139913476152412728213373867915',
'8.557502859947763136836725748815817516612392303357517172098711746440909459502732673324074556243488565',
'11.1576584568528318087907825837468833962608843570045444271315023562274669838130485896668698236377315',
'14.6950831096777683062233542920507338377898344935742992305030358553039530695862340781589895091658517']
eps=dec('1e-24')
yb,base_signs,base_sign_ok=signs_for_roots(pbase,base_centers,R,eps)
base_ordered=all(bool(yb[i].b<yb[i+1].a) for i in range(R-1))
base_inside=bool(yb[0].a>0 and yb[-1].b<S.a)
xb=[O-y/S for y in yb]
wb=[]
for i in range(R):
    numpoly=[O]; den=O
    for j in range(R):
        if j==i: continue
        numpoly=poly_mul(numpoly,[-yb[j],O]); den=den*(yb[i]-yb[j])
    numpoly=poly_mul(numpoly,[-S,O]); den=den*(yb[i]-S)
    num=Z
    for rr,cc in enumerate(numpoly): num += cc*my[rr]
    wb.append(num/den)
pc=list(coef)+[O]
num0=Z
for i,ci in enumerate(pc):
    for j,cj in enumerate(pc): num0 += ci*cj*my[i+j]
pS=pbase(S); w0sq=num0/(pS*pS)
hb=[]
for xx in xb:
    partial=Z; pp=xx
    for n in range(1,KMAX+1): partial += pp/n; pp*=xx
    hb.append((-mp.iv.log(O-xx)-partial)/(xx**KMAX))
baseQ=Z
for i in range(R): baseQ += wb[i]*hb[i]
baseTLB=muK*muK*baseQ
baseAup=AK-baseTLB
Ny=Z
for i,ci in enumerate(pc):
    for j,cj in enumerate(pc): Ny += ci*cj*wm[i+j]
Nx=Ny/(S**(2*R))
tmy=[]
for qj in range(2*TAUR):
    num=Z
    for i,ci in enumerate(pc):
        for j,cj in enumerate(pc): num += ci*cj*wm[i+j+qj]
    tmy.append(num/Ny)
Ht=[[tmy[a+b] for b in range(TAUR)] for a in range(TAUR)]
rhst=[-tmy[a+TAUR] for a in range(TAUR)]
tcoef,tpivots=solve_interval(Ht,rhst)

def ptau(y):
    out=y+tcoef[TAUR-1]
    for j in range(TAUR-2,-1,-1): out=out*y+tcoef[j]
    return out

tau_centers=[
'0.8645893105563788129129737832977869627589834853213845698473911263898545907128210739355979963428621296',
'6.93817115902672689650563890798069965841698348112977008757895538391111996209734946869628552737253702',
'15.70694118964636714563179203331569909072109252813460257378523591500034534340734202261577606504750179',
'20.46106344947113584307642872536957238334583861862377454385345782739103401089488735968852542787450777']
yt,tau_signs,tau_sign_ok=signs_for_roots(ptau,tau_centers,TAUR,eps)
tau_ordered=all(bool(yt[i].b<yt[i+1].a) for i in range(TAUR-1))
tau_inside=bool(yt[0].a>0 and yt[-1].b<S.a)
zt=[O-y/S for y in yt]
vt=lagrange_weights(yt,tmy)
tmatch=[]
for j in range(TAUR):
    qm=Z
    for i in range(TAUR): qm += vt[i]*(yt[i]**j)
    rr=qmom-my[j] if False else qm-tmy[j]
    tmatch.append(bool(rr.a<=0<=rr.b))
h=dec(STEP_STR); Tmax=dec(TMAX_STR); M=int(mp.mpf(TMAX_STR)/mp.mpf(STEP_STR))
qstep=mp.iv.exp(-h)
qN=mp.iv.exp(-(KMAX+2*R+1)*h)
u=qstep; un=qN
G=[Z for _ in range(TAUR)]
for jj in range(1,M+1):
    den=O
    for xx in xb:
        den *= (O-xx*u)*(O-xx*u)
    base=un/den
    for a in range(TAUR):
        G[a] += h*base/(O-zt[a]*u)
    u*=qstep; un*=qN
corr_inner=Z
for a in range(TAUR): corr_inner += vt[a]*G[a]
corrLB=muK*muK*Nx*corr_inner
totalTLB=baseTLB+corrLB
Aup=AK-totalTLB
checks={
'all_mu_positive_1_to_Kplus30':allpos,
'base_hankel_pivots_positive':all(bool(pp.a>0) for pp in pivots),
'base_root_sign_brackets':base_sign_ok,
'base_roots_ordered':base_ordered,
'base_roots_inside':base_inside,
'base_interior_weights_positive':all(bool(w.a>0) for w in wb),
'base_endpoint_weight_square_positive':bool(w0sq.a>0),
'Ny_positive':bool(Ny.a>0),
'Nx_positive':bool(Nx.a>0),
'tau_hankel_pivots_positive':all(bool(pp.a>0) for pp in tpivots),
'tau_root_sign_brackets':tau_sign_ok,
'tau_roots_ordered':tau_ordered,
'tau_roots_inside':tau_inside,
'tau_weights_positive':all(bool(v.a>0) for v in vt),
'tau_moment_match_0_to_3':all(tmatch),
'riemann_grid_positive':all(bool(g.a>0) for g in G)}
mp.iv.dps=100
print('NM13-13 T04 NESTED RADAU11 + TAU-GAUSS4 MARKOV-ERROR CERTIFICATE AT 4.3888608')
print('alpha = 2743038/625000 = 4.3888608')
print('KMAX =',KMAX,'BASE_RADAU_INTERIOR =',R,'TAU_GAUSS_NODES =',TAUR,'interval dps =',DPS)
print('right-Riemann step =',STEP_STR,'Tmax =',TMAX_STR,'M =',M)
print('checks =',checks)
print('A_K =',AK)
print('mu_K =',muK)
print('Ny =',Ny)
print('Nx =',Nx)
print('base left-Radau11 tail lower bound =',baseTLB)
print('base A upper before nested correction =',baseAup)
print('nested Markov error correction lower bound =',corrLB)
print('total tail lower bound =',totalTLB)
print('A upper bound =',Aup)
print('CERTIFIED_STRUCTURAL_CHECKS =',all(checks.values()))
print('CERTIFIED_A_UPPER_NEGATIVE =',bool(Aup.b<0))
print('CERTIFIED_A_NEGATIVE =',bool(Aup.b<0),'because A <= A_K - base_Radau11_tail_LB - nested_Markov_error_LB')
