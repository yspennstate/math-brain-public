#!/usr/bin/env python3
import math
import mpmath as mp
DPS=1300; KMAX=2300; R=11; TAUR=4; SCALE=1000
STEP_STR='0.000005'; TMAX_STR='0.02'
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
        c=dec(cs); lo=c-eps; hi=c+eps; plo=poly(lo); phi=poly(hi)
        tup=(bool(plo.b<0),bool(plo.a>0),bool(phi.b<0),bool(phi.a>0)); tuples.append(tup)
        roots.append(mp.iv.mpf([lo.a,hi.b])); left_neg=((degree-i)%2==1)
        ok=ok and ((tup[0] and tup[3]) if left_neg else (tup[1] and tup[2]))
    return roots,tuples,ok

# Exact rational candidate: new symmetric seven-support survey.
alpha=q(219443029,50000000)  # 4.38886058
vals=[q(651,100000), q(1,50), q(789,10000), O/2, q(9211,10000), q(49,50), q(99349,100000)]
probs=[q(5581,100000), q(1,2500), q(3661,20000), q(13037,25000), q(3661,20000), q(1,2500), q(5581,100000)]
lam=3*alpha/2
pair=[(probs[i]*probs[j],O-vals[i]*vals[j]) for i in range(7) for j in range(7)]
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
    mu=arr[0] if k%2==0 else -arr[0]; mus.append(mu); allpos=allpos and bool(mu.a>0)
    if k<=KMAX: series += mu*mu/k
L=Z
for i in range(7):
    for j in range(7):
        for h in range(7): L += probs[i]*probs[j]*probs[h]*mp.iv.log(O-vals[i]*vals[j]*vals[h])
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
H=[[wm[a+b] for b in range(R)] for a in range(R)]; rhs=[-wm[a+R] for a in range(R)]
coef,pivots=solve_interval(H,rhs)
def pbase(y):
    out=y+coef[R-1]
    for j in range(R-2,-1,-1): out=out*y+coef[j]
    return out
base_centers=[
'0.10945230970444828799365700993145067815133175989442332866488881513837089476677114929380801847587924086050824509',
'0.39164736452289324730442498037967145045354693068984473734397530661554269928949555261729091361158270731314017682',
'0.85543199077964376565834013522924530087552522698534880761753209816079087120436047731515592793289909403651221092',
'1.5147846641730207169853003791168303685743148514495337312050520453800076771192215383178077509109830677905417347',
'2.3808559956730869919326607729592851481524199850939280661518335004112059710908440104219251510678639187554019504',
'3.4755321071839910220492114551229205025121533269997446832537538904252441704608771304715194740855048368276969901',
'4.8311022189789416422256603045956791264782171469565105738110747382379757480064389996774479933060136088890558376',
'6.4987992382518455009999002058689056142413233328155018994697661462584117117761085196017695973662813309998066458',
'8.5563086502875851102393423728915329217824573261665921296855729986784697265696898162589916335890660149390124014',
'11.156420316415735428798277776680046731050159080815643351877339543398841380536860342184986447675140546199722296',
'14.693828941647125332110496390198277030058811833811448098155763698958042105997964578055220499058914188109865305']
eps=dec('1e-24')
yb,base_signs,base_sign_ok=signs_for_roots(pbase,base_centers,R,eps)
base_ordered=all(bool(yb[i].b<yb[i+1].a) for i in range(R-1)); base_inside=bool(yb[0].a>0 and yb[-1].b<S.a)
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
baseTLB=muK*muK*baseQ; baseAup=AK-baseTLB
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
Ht=[[tmy[a+b] for b in range(TAUR)] for a in range(TAUR)]; rhst=[-tmy[a+TAUR] for a in range(TAUR)]
tcoef,tpivots=solve_interval(Ht,rhst)
def ptau(y):
    out=y+tcoef[TAUR-1]
    for j in range(TAUR-2,-1,-1): out=out*y+tcoef[j]
    return out
tau_centers=[
'0.86450456669877897596550911191722259032144629362508711686520151962453082773266604183880363442158582831317556298',
'6.9379516992407308453137543011999039996630295452588795000203914744892365760180051368006892037706873655964615053',
'15.705724442649733013500678183847151211322646386624663832019810352968701183156885319899797173928908144326164211',
'20.459771938954566788077404698332065593744023154101987553250397846730803057928319509052792769991355832204225909']
yt,tau_signs,tau_sign_ok=signs_for_roots(ptau,tau_centers,TAUR,eps)
tau_ordered=all(bool(yt[i].b<yt[i+1].a) for i in range(TAUR-1)); tau_inside=bool(yt[0].a>0 and yt[-1].b<S.a)
zt=[O-y/S for y in yt]; vt=lagrange_weights(yt,tmy)
tmatch=[]
for j in range(TAUR):
    qm=Z
    for i in range(TAUR): qm += vt[i]*(yt[i]**j)
    rr=qm-tmy[j]; tmatch.append(bool(rr.a<=0<=rr.b))
h=dec(STEP_STR); M=int(mp.mpf(TMAX_STR)/mp.mpf(STEP_STR)); qstep=mp.iv.exp(-h); qN=mp.iv.exp(-(KMAX+2*R+1)*h); u=qstep; un=qN
G=[Z for _ in range(TAUR)]
for jj in range(1,M+1):
    den=O
    for xx in xb: den *= (O-xx*u)*(O-xx*u)
    base=un/den
    for a in range(TAUR): G[a] += h*base/(O-zt[a]*u)
    u*=qstep; un*=qN
corr_inner=Z
for a in range(TAUR): corr_inner += vt[a]*G[a]
corrLB=muK*muK*Nx*corr_inner; totalTLB=baseTLB+corrLB; Aup=AK-totalTLB
checks={
'all_mu_positive_1_to_Kplus30':allpos,
'base_hankel_pivots_positive':all(bool(pp.a>0) for pp in pivots),
'base_root_sign_brackets':base_sign_ok,'base_roots_ordered':base_ordered,'base_roots_inside':base_inside,
'base_interior_weights_positive':all(bool(w.a>0) for w in wb),'base_endpoint_weight_square_positive':bool(w0sq.a>0),
'Ny_positive':bool(Ny.a>0),'Nx_positive':bool(Nx.a>0),
'tau_hankel_pivots_positive':all(bool(pp.a>0) for pp in tpivots),'tau_root_sign_brackets':tau_sign_ok,
'tau_roots_ordered':tau_ordered,'tau_roots_inside':tau_inside,'tau_weights_positive':all(bool(v.a>0) for v in vt),
'tau_moment_match_0_to_3':all(tmatch),'riemann_grid_positive':all(bool(g.a>0) for g in G)}
mp.iv.dps=100
print('NM13-06 T04 SEVEN-SUPPORT NESTED RADAU11+TAUGAUSS4 CERTIFICATE AT 4.38886058')
print('alpha = 219443029/50000000 = 4.38886058')
print('support = {651/100000,1/50,789/10000,1/2,9211/10000,49/50,99349/100000}')
print('weights = {5581/100000,1/2500,3661/20000,13037/25000,3661/20000,1/2500,5581/100000}')
print('KMAX =',KMAX,'BASE_RADAU_INTERIOR =',R,'TAU_GAUSS_NODES =',TAUR,'interval dps =',DPS)
print('checks =',checks)
print('A_K =',AK); print('mu_K =',muK); print('Nx =',Nx)
print('base left-Radau11 tail lower bound =',baseTLB)
print('base A upper before nested correction =',baseAup)
print('nested Markov error correction lower bound =',corrLB)
print('total tail lower bound =',totalTLB)
print('A upper bound =',Aup)
print('CERTIFIED_STRUCTURAL_CHECKS =',all(checks.values()))
print('CERTIFIED_A_UPPER_NEGATIVE =',bool(Aup.b<0))
print('CERTIFIED_A_NEGATIVE =',bool(Aup.b<0),'because A <= A_K - base_Radau11_tail_LB - nested_Markov_error_LB')
