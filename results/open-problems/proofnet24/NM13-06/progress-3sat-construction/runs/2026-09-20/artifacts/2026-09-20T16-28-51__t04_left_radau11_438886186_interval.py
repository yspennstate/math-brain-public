#!/usr/bin/env python3
import math
import mpmath as mp

DPS=1200
KMAX=2300
R=11
SCALE=1000
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

# exact density 4.38886186
alpha=q(219443093,50000000)
vals=[q(651,100000),q(789,10000),O/2,q(9211,10000),q(99349,100000)]
probs=[q(5581,100000),q(3669,20000),q(13037,25000),q(3669,20000),q(5581,100000)]
lam=3*alpha/2
pair=[(probs[i]*probs[j],O-vals[i]*vals[j]) for i in range(5) for j in range(5)]
NEED=KMAX+2*R
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
# moments s_j = E_sigma X^j through 22
sx=[(mus[KMAX+j]/muK)**2 for j in range(2*R+1)]
# Y=1000(1-X) moments through 22
my=[]
for j in range(2*R+1):
    v=Z
    for ell in range(j+1):
        term=mp.iv.mpf([math.comb(j,ell),math.comb(j,ell)])*sx[ell]
        v=v-term if ell%2 else v+term
    my.append((S**j)*v)
# modified moments for X d sigma = (1-Y/S)d sigma, through degree 21
wm=[my[j]-my[j+1]/S for j in range(2*R)]
H=[[wm[a+b] for b in range(R)] for a in range(R)]
rhs=[-wm[a+R] for a in range(R)]
coef,pivots=solve_interval(H,rhs)

def poly(y):
    out=y+coef[R-1]
    for j in range(R-2,-1,-1): out=out*y+coef[j]
    return out

centers=[
'0.109594959303078360596274984802917468395074669565982532644686287954368528666817808601562373',
'0.391925757928106897982051890664122406150434900283090566567916438053786196467175036962766681',
'0.855830641134928515353591748264366801956011252625248289850658945290136099386100835191228815',
'1.51531355243956371273902257652499615789090431395710220312153892921298821081747458944220328',
'2.38150111370518937519656345591112346800397548906753307143463025557642556629930088985756346',
'3.47628312867028793640800038358117239394734244976055145425178399296337012461394723381105023',
'4.83199162884917728755860357988838229780097274642058198459880902500305887839518749734286125',
'6.49982857425328860932282606521831160512329375993533470386558218651335367301797129798166857',
'8.55750273765813334153067072418176114331539207984483781082243092088075842854708564662317638',
'11.157658322146437498864299827380883317562311494875170437718775297582678390990721661267294',
'14.6950829645385979547385213771843071821723617613466271050180416236916843428437336835337831']
eps=dec('1e-24')
y=[]; root_signs=[]
for cs in centers:
    c=dec(cs); lo=c-eps; hi=c+eps
    plo=poly(lo); phi=poly(hi)
    root_signs.append((bool(plo.b<0),bool(plo.a>0),bool(phi.b<0),bool(phi.a>0)))
    y.append(mp.iv.mpf([lo.a,hi.b]))
root_sign_ok=True
for i,(lo_neg,lo_pos,hi_neg,hi_pos) in enumerate(root_signs):
    root_sign_ok = root_sign_ok and ((lo_neg and hi_pos) if i%2==0 else (lo_pos and hi_neg))
ordered=all(bool(y[i].b<y[i+1].a) for i in range(R-1))
inside=bool(y[0].a>0 and y[-1].b<S.a)
# Interior Radau weights: Lagrange basis over the 11 interior nodes plus endpoint Y=S.
w=[]
for i in range(R):
    numpoly=[O]; den=O
    for j in range(R):
        if j==i: continue
        numpoly=poly_mul(numpoly,[-y[j],O]); den=den*(y[i]-y[j])
    numpoly=poly_mul(numpoly,[-S,O]); den=den*(y[i]-S)
    num=Z
    for rr,cc in enumerate(numpoly): num += cc*my[rr]
    w.append(num/den)
w0=O
for ww in w: w0=w0-ww
# Independent positive endpoint-weight formula from Radau exactness on l_0^2:
# l_0(Y)=p(Y)/p(S), where p is the monic interior-node polynomial.
pc=list(coef)+[O]
num0=Z
for i,ci in enumerate(pc):
    for j,cj in enumerate(pc): num0 += ci*cj*my[i+j]
pS=poly(S)
w0sq=num0/(pS*pS)
# moment sanity through degree 11 (includes endpoint for degree 0+)
match=[]
for j in range(R+1):
    qmom=w0*(S**j)
    for i in range(R): qmom += w[i]*(y[i]**j)
    rr=qmom-my[j]; match.append(bool(rr.a<=0<=rr.b))
checks={
'all_mu_positive_1_to_Kplus22':allpos,
'all_modified_hankel_pivots_positive':all(bool(pp.a>0) for pp in pivots),
'root_brackets_sign_certified':root_sign_ok,
'root_intervals_ordered':ordered,
'Y_roots_inside_0_1000':inside,
'interior_weights_positive':all(bool(ww.a>0) for ww in w),
'endpoint_weight_square_formula_positive':bool(w0sq.a>0),
'moment_match_0_to_11_interval_contains_zero':all(match)}
# Tail lower bound. Endpoint X=0 contributes h_K(0)=0 exactly.
x=[O-y[i]/S for i in range(R)]
h=[]
for i in range(R):
    xx=x[i]; partial=Z; pp=xx
    for n in range(1,KMAX+1): partial += pp/n; pp*=xx
    hh=(-mp.iv.log(O-xx)-partial)/(xx**KMAX); h.append(hh)
tail=Z
for i in range(R): tail += w[i]*h[i]
TLB=muK*muK*tail; Aup=AK-TLB
mp.iv.dps=100
print('NM13-06 T04 LEFT-RADAU11 COMPLETE-TAIL CERTIFICATE AT 4.38886186')
print('alpha = 219443093/50000000 = 4.38886186')
print('KMAX =',KMAX,'RADAU_INTERIOR =',R,'interval dps =',DPS)
print('checks =',checks)
print('A_K =',AK)
print('mu_K =',muK)
print('root sign tuples =',root_signs)
for i in range(R): print('Y%d ='%(i+1),y[i],'; X%d ='%(i+1),x[i],'; w%d ='%(i+1),w[i])
print('endpoint Y=1000 / X=0 subtraction enclosure =',w0)
print('endpoint weight positive square-formula enclosure =',w0sq)
print('complete left-Radau11 tail lower bound =',TLB)
print('A upper bound =',Aup)
print('CERTIFIED_STRUCTURAL_CHECKS =',all(checks.values()))
print('CERTIFIED_A_UPPER_NEGATIVE =',bool(Aup.b<0))
print('CERTIFIED_A_NEGATIVE =',bool(Aup.b<0),'because A <= A_K - complete_left_Radau11_tail_LB')
