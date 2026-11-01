#!/usr/bin/env python3
import math
import mpmath as mp

DPS = 850
KMAX = 2300
NGAUSS = 9
SCALE = 1000
mp.iv.dps = DPS
Z = mp.iv.mpf([0,0]); O = mp.iv.mpf([1,1]); S = mp.iv.mpf([SCALE,SCALE])

def q(n,d): return mp.iv.mpf([n,n]) / d
def dec(s): return mp.iv.mpf([s,s])
def contains_zero(x): return bool(x.a <= 0 <= x.b)

def solve_interval(A,b):
    n=len(A); M=[[A[i][j] for j in range(n)] for i in range(n)]; y=[b[i] for i in range(n)]; piv=[]
    for k in range(n):
        p=M[k][k]
        if contains_zero(p): raise RuntimeError(f'interval pivot contains zero at {k}: {p}')
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

# Exact density and reoptimized symmetric five-support survey.
alpha=q(87777273,20000000)  # 4.38886365 exactly
vals=[q(651,100000),q(789,10000),O/2,q(9211,10000),q(99349,100000)]
probs=[q(5581,100000),q(3669,20000),q(13037,25000),q(3669,20000),q(5581,100000)]
lam=3*alpha/2

pair=[(probs[i]*probs[j],O-vals[i]*vals[j]) for i in range(5) for j in range(5)]
NEED=KMAX+2*NGAUSS
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
sx=[(mus[KMAX+j]/muK)**2 for j in range(2*NGAUSS)]

my=[]
for j in range(2*NGAUSS):
    v=Z
    for ell in range(j+1):
        term=mp.iv.mpf([math.comb(j,ell),math.comb(j,ell)])*sx[ell]
        v = v-term if ell%2 else v+term
    my.append((S**j)*v)

H=[[my[r+c] for c in range(NGAUSS)] for r in range(NGAUSS)]
rhs=[-my[r+NGAUSS] for r in range(NGAUSS)]
coef,pivots=solve_interval(H,rhs)

def poly(y):
    out=y+coef[8]
    for j in range(7,-1,-1): out=out*y+coef[j]
    return out

centers=[
'0.131239748998705310871097632993544620002285995860196773446534',
'0.471276280223515105656435616537291480422960692044523845581034',
'1.035671956561800228896854635018261971788558611831932602070736',
'1.845570772633228183411675616791574548060457420942227874312423',
'2.924620088058113529062198296228252104119864586553062264363468',
'4.315174912541120770679441961776356161499944001830245067575829',
'6.101880847411103547925052642144956615448221403796162760352950',
'8.428636265813766904813942820710774463480986520212159245211756',
'11.688126678314728446338414928474215036939109999277834295617640']
eps=dec('1e-24')
root_signs=[]; y=[]
for cs in centers:
    c=dec(cs); lo,hi=c-eps,c+eps; plo,phi=poly(lo),poly(hi)
    root_signs.append((bool(plo.b<0),bool(plo.a>0),bool(phi.b<0),bool(phi.a>0)))
    y.append(mp.iv.mpf([lo.a,hi.b]))
root_sign_ok=True
for i,(lo_neg,lo_pos,hi_neg,hi_pos) in enumerate(root_signs):
    root_sign_ok = root_sign_ok and ((lo_neg and hi_pos) if i%2==0 else (lo_pos and hi_neg))
ordered=all(bool(y[i].b<y[i+1].a) for i in range(NGAUSS-1)); inside=bool(y[0].a>0 and y[-1].b<S.a)

w=[]
for i in range(NGAUSS):
    numpoly=[O]; den=O
    for j in range(NGAUSS):
        if j==i: continue
        numpoly=poly_mul(numpoly,[-y[j],O]); den=den*(y[i]-y[j])
    num=Z
    for rr,cc in enumerate(numpoly): num += cc*my[rr]
    w.append(num/den)

match=[]
for j in range(NGAUSS):
    qmom=Z
    for i in range(NGAUSS): qmom += w[i]*(y[i]**j)
    rr=qmom-my[j]; match.append(bool(rr.a<=0<=rr.b))
checks={
'all_mu_positive_1_to_Kplus18':allpos,
'all_elimination_pivots_positive':all(bool(pp.a>0) for pp in pivots),
'root_brackets_sign_certified':root_sign_ok,
'root_intervals_ordered':ordered,
'Y_roots_inside_0_1000':inside,
'weights_positive':all(bool(ww.a>0) for ww in w),
'moment_match_0_to_8_interval_contains_zero':all(match)}

x=[O-y[i]/S for i in range(NGAUSS)]; h=[]
for i in range(NGAUSS):
    xx=x[i]; partial=Z; pp=xx
    for n in range(1,KMAX+1): partial += pp/n; pp*=xx
    hh=(-mp.iv.log(O-xx)-partial)/(xx**KMAX); h.append(hh)
tail=Z
for i in range(NGAUSS): tail += w[i]*h[i]
TLB=muK*muK*tail; Aup=AK-TLB

mp.iv.dps=90
print('NM13-13 T04 REOPTIMIZED DIRECT PRODUCT GAUSS9 CERTIFICATE AT 4.38886365')
print('alpha = 87777273/20000000 = 4.38886365')
print('survey support = {651/100000,789/10000,1/2,9211/10000,99349/100000}')
print('survey weights = {5581/100000,3669/20000,13037/25000,3669/20000,5581/100000}')
print('KMAX =',KMAX,'NGAUSS =',NGAUSS,'interval dps =',DPS)
print('checks =',checks)
print('A_K =',AK)
print('mu_K =',muK)
print('root sign tuples =',root_signs)
for i in range(NGAUSS): print('Y%d ='%(i+1),y[i],'; X%d ='%(i+1),x[i],'; w%d ='%(i+1),w[i])
print('complete direct-product Gauss9 tail lower bound =',TLB)
print('A upper bound =',Aup)
print('CERTIFIED_STRUCTURAL_CHECKS =',all(checks.values()))
print('CERTIFIED_A_UPPER_NEGATIVE =',bool(Aup.b<0))
print('CERTIFIED_A_NEGATIVE =',bool(Aup.b<0),'because A <= A_K - complete_direct_product_Gauss9_tail_LB')
