import math, mpmath as mp
DPS=1300; KMAX=2300; R=11; TAUR=4; SCALE=1000
STEP_STR='0.000005'; TMAX_STR='0.02'
mp.iv.dps=DPS
Z=mp.iv.mpf([0,0]); O=mp.iv.mpf([1,1]); S=mp.iv.mpf([SCALE,SCALE])
def q(n,d): return mp.iv.mpf([n,n])/d
def dec(s): return mp.iv.mpf([s,s])
def contains_zero(x): return bool(x.a <= 0 <= x.b)
def solve_interval(A,b):
    n=len(A); M=[[A[i][j] for j in range(n)] for i in range(n)]; y=[b[i] for i in range(n)]
    piv=[]
    for k in range(n):
        p=M[k][k]
        if contains_zero(p): raise RuntimeError(('pivot',k,p))
        piv.append(p)
        for i in range(k+1,n):
            f=M[i][k]/p; M[i][k]=Z
            for j in range(k+1,n): M[i][j]-=f*M[k][j]
            y[i]-=f*y[k]
    x=[Z]*n
    for i in range(n-1,-1,-1):
        s=y[i]
        for j in range(i+1,n): s-=M[i][j]*x[j]
        x[i]=s/M[i][i]
    return x,piv
def poly_mul(A,B):
    out=[Z]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B): out[i+j]+=a*b
    return out
def lagrange_weights(nodes,moments):
    out=[]
    for i in range(len(nodes)):
        numpoly=[O]; den=O
        for j in range(len(nodes)):
            if j==i: continue
            numpoly=poly_mul(numpoly,[-nodes[j],O]); den*=nodes[i]-nodes[j]
        num=Z
        for rr,cc in enumerate(numpoly): num += cc*moments[rr]
        out.append(num/den)
    return out
def signs_for_roots(poly,centers,degree,eps):
    roots=[]; ok=True
    for i,cs in enumerate(centers):
        c=dec(cs); lo=c-eps; hi=c+eps; plo=poly(lo); phi=poly(hi)
        left_neg=((degree-i)%2==1)
        ok = ok and ((bool(plo.b<0) and bool(phi.a>0)) if left_neg else (bool(plo.a>0) and bool(phi.b<0)))
        roots.append(mp.iv.mpf([lo.a,hi.b]))
    return roots,ok

alpha=q(109721469,25000000)
vals=[q(7,200000), q(651,100000), q(789,10000), O/2, q(9211,10000), q(99349,100000), q(199993,200000)]
probs=[q(147,100000), q(2717,50000), q(3669,20000), q(13037,25000), q(3669,20000), q(2717,50000), q(147,100000)]
lam=3*alpha/2
pair=[(probs[i]*probs[j],O-vals[i]*vals[j]) for i in range(7) for j in range(7)]
NEED=KMAX+30
EZ=[O]; pows=[O for _ in pair]
for jj in range(1,NEED+1):
    m=Z
    for idx,(wt,base) in enumerate(pair):
        pows[idx]*=base; m+=wt*pows[idx]
    EZ.append(mp.iv.exp(lam*(m-O)))
arr=EZ; mus=[O]; series=Z; allpos=True
for k in range(1,NEED+1):
    arr=[arr[j+1]-arr[j] for j in range(len(arr)-1)]
    mu=arr[0] if k%2==0 else -arr[0]
    mus.append(mu); allpos=allpos and bool(mu.a>0)
    if k<=KMAX: series += mu*mu/k
L=Z
for i in range(7):
  for j in range(7):
    for h3 in range(7):
      L += probs[i]*probs[j]*probs[h3]*mp.iv.log(O-vals[i]*vals[j]*vals[h3])
AK=-series-2*alpha*L; muK=mus[KMAX]
sx=[(mus[KMAX+j]/muK)**2 for j in range(31)]
my=[]
for j in range(31):
    v=Z
    for ell in range(j+1):
        term=mp.iv.mpf([math.comb(j,ell),math.comb(j,ell)])*sx[ell]
        v = v-term if ell%2 else v+term
    my.append((S**j)*v)
wm=[my[j]-my[j+1]/S for j in range(30)]
H=[[wm[a+b] for b in range(R)] for a in range(R)]; rhs=[-wm[a+R] for a in range(R)]
coef,pivots=solve_interval(H,rhs)
def pbase(y):
    out=y+coef[R-1]
    for j in range(R-2,-1,-1): out=out*y+coef[j]
    return out
base_centers=[
'0.10811434877041591547197332520229392481333811647909509658066325131739346177722031',
'0.38961179433949103180935168130769110476075892251509127722205349682222078469488787',
'0.85302815455684441825894440315507826468710197003218042883300620638164339796885793',
'1.5119803451375556786014789860579987654304266751392532521241821390094546699078513',
'2.3775412673697419072807377974951765316939608008841864226598943438319679235359591',
'3.4718031374428377697474403581744441193193995221031368344417466847956425223872879',
'4.8273085501311171722752344538559720987468493099499172037697259702885065062329339',
'6.4951967385949401030992584945005508803889755669985057656501843057253621640875252',
'8.5533446620142581089650546391336420351601118097037908429385336533121173291915833',
'11.154004044320008822388762833852666608277622814441372286069054520846004895936782',
'14.691646845338102885031685000732982545933957606637073818366948166487519471668833']
eps=dec('1e-24'); yb,base_sign_ok=signs_for_roots(pbase,base_centers,R,eps)
base_ordered=all(bool(yb[i].b<yb[i+1].a) for i in range(R-1)); base_inside=bool(yb[0].a>0 and yb[-1].b<S.a)
xb=[O-y/S for y in yb]
wb=[]
for i in range(R):
    numpoly=[O]; den=O
    for j in range(R):
        if j==i: continue
        numpoly=poly_mul(numpoly,[-yb[j],O]); den*=yb[i]-yb[j]
    numpoly=poly_mul(numpoly,[-S,O]); den*=yb[i]-S
    num=Z
    for rr,cc in enumerate(numpoly): num += cc*my[rr]
    wb.append(num/den)
pc=list(coef)+[O]
hb=[]
for xx in xb:
    partial=Z; pp=xx
    for n in range(1,KMAX+1): partial += pp/n; pp*=xx
    hb.append((-mp.iv.log(O-xx)-partial)/(xx**KMAX))
baseQ=Z
for i in range(R): baseQ += wb[i]*hb[i]
baseTLB=muK*muK*baseQ
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
'0.86397294947911821346911520415749922672046726384574218996895963447287793020577349',
'6.9369437416031674176432126947052890027564081798420640256511109181401958048285061',
'15.704055446327097514316042091997184245469176286312034946225319888611583247031691',
'20.458368694345474673903928232710450230798065015507329864387747125874955899694237']
yt,tau_sign_ok=signs_for_roots(ptau,tau_centers,TAUR,eps)
tau_ordered=all(bool(yt[i].b<yt[i+1].a) for i in range(TAUR-1)); tau_inside=bool(yt[0].a>0 and yt[-1].b<S.a)
zt=[O-y/S for y in yt]; vt=lagrange_weights(yt,tmy)
tmatch=[]
for j in range(TAUR):
    qm=Z
    for i in range(TAUR): qm += vt[i]*(yt[i]**j)
    rr=qm-tmy[j]; tmatch.append(bool(rr.a<=0<=rr.b))

# Cellwise tangent lower bound.  For
# f_z(t)=exp(-N t)/[prod_i(1-x_i exp(-t))^2 (1-z exp(-t))],
# D_z(t)=-f'_z(t)/f_z(t)=N+2 sum_i x_i u/(1-x_i u)+z u/(1-z u).
# Convexity gives int_{b-h}^b f >= h f(b) - h^2 f'(b)/2
# = h f(b)(1+h D_z(b)/2).  This is applied separately to every cell/node.
h=dec(STEP_STR); M=int(mp.mpf(TMAX_STR)/mp.mpf(STEP_STR))
qstep=mp.iv.exp(-h); qN=mp.iv.exp(-(KMAX+2*R+1)*h)
u=qstep; un=qN; Nconst=mp.iv.mpf([KMAX+2*R+1,KMAX+2*R+1])
Gold=[Z for _ in range(TAUR)]; Gtan=[Z for _ in range(TAUR)]
minD=None
for jj in range(1,M+1):
    den=O; dcommon=Nconst
    for xx in xb:
        fac=O-xx*u
        den *= fac*fac
        dcommon += 2*xx*u/fac
    base=un/den
    for a in range(TAUR):
        facz=O-zt[a]*u
        fr=base/facz
        D=dcommon+zt[a]*u/facz
        Gold[a] += h*fr
        Gtan[a] += h*fr*(O+h*D/2)
        if minD is None or D.a < minD.a: minD=D
    u*=qstep; un*=qN
corr_old_inner=Z; corr_tan_inner=Z
for a in range(TAUR):
    corr_old_inner += vt[a]*Gold[a]
    corr_tan_inner += vt[a]*Gtan[a]
corr_old=muK*muK*Nx*corr_old_inner
corr_tan=muK*muK*Nx*corr_tan_inner
Aup_old=AK-baseTLB-corr_old
Aup_tan=AK-baseTLB-corr_tan

# One-sided density transfer.  For this survey s_min=1-(199993/200000)^2,
# and the companion proof certifies -log(s_min)<48/5, whence
# A(alpha-delta,nu)-A(alpha,nu) <= (144/5) delta.
delta=q(1,2500000000)  # 4e-10
penalty=q(144,5)*delta
Aup_alpha1=Aup_tan+penalty
alpha1=alpha-delta
checks={
'all_mu_positive':allpos,
'base_hankel_pivots_positive':all(bool(pp.a>0) for pp in pivots),
'base_root_sign_brackets':base_sign_ok,'base_roots_ordered':base_ordered,'base_roots_inside':base_inside,
'base_weights_positive':all(bool(w.a>0) for w in wb),
'Ny_positive':bool(Ny.a>0),'Nx_positive':bool(Nx.a>0),
'tau_hankel_pivots_positive':all(bool(pp.a>0) for pp in tpivots),
'tau_root_sign_brackets':tau_sign_ok,'tau_roots_ordered':tau_ordered,'tau_roots_inside':tau_inside,
'tau_weights_positive':all(bool(v.a>0) for v in vt),'tau_moment_match_0_to_3':all(tmatch),
'cell_D_positive':bool(minD.a>0),'corr_tangent_gt_old':bool((corr_tan-corr_old).a>0),
'Aup_tangent_negative':bool(Aup_tan.b<0),'Aup_alpha1_negative':bool(Aup_alpha1.b<0)
}
mp.iv.dps=100
print('NM13-06 T04 CELLWISE-TANGENT NESTED RADAU CERTIFICATE')
print('alpha0 =',alpha)
print('alpha1 =',alpha1)
print('delta =',delta,'penalty =',penalty)
print('checks =',checks)
print('minimum cellwise D interval =',minD)
print('old nested correction =',corr_old)
print('cellwise tangent correction =',corr_tan)
print('correction gain =',corr_tan-corr_old)
print('old A upper =',Aup_old)
print('cellwise tangent A upper at alpha0 =',Aup_tan)
print('transferred A upper at alpha1 =',Aup_alpha1)
print('CERTIFIED_STRUCTURAL_CHECKS =',all(checks.values()))
print('CERTIFIED_A_ALPHA1_NEGATIVE =',bool(Aup_alpha1.b<0))
