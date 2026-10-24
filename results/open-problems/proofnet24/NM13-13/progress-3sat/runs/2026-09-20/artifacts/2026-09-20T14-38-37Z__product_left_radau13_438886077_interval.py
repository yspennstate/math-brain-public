#!/usr/bin/env python3
import math
import mpmath as mp

DPS = 1850
KMAX = 2300
NINT = 13
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
        ss=y[i]
        for j in range(i+1,n): ss=ss-M[i][j]*x[j]
        if contains_zero(M[i][i]): raise RuntimeError(f'back pivot contains zero at {i}')
        x[i]=ss/M[i][i]
    return x,piv

def poly_mul(A,B):
    out=[Z for _ in range(len(A)+len(B)-1)]
    for i,a in enumerate(A):
        for j,b in enumerate(B): out[i+j]=out[i+j]+a*b
    return out

alpha=q(438886077,100000000)  # 4.38886077 exactly
vals=[q(651,100000),q(789,10000),O/2,q(9211,10000),q(99349,100000)]
probs=[q(5581,100000),q(3669,20000),q(13037,25000),q(3669,20000),q(5581,100000)]
lam=3*alpha/2
pair=[(probs[i]*probs[j],O-vals[i]*vals[j]) for i in range(5) for j in range(5)]
NEED=KMAX+2*NINT
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
# Need s_j through j=26 inclusive for the 13-interior-node Radau rule.
sx=[(mus[KMAX+j]/muK)**2 for j in range(2*NINT+1)]

# Y=1000(1-X), with the fixed Radau endpoint X=0 corresponding to Y=1000.
my=[]
for j in range(2*NINT+1):
    v=Z
    for ell in range(j+1):
        term=mp.iv.mpf([math.comb(j,ell),math.comb(j,ell)])*sx[ell]
        v = v-term if ell%2 else v+term
    my.append((S**j)*v)
# Interior nodes are Gaussian nodes for X d sigma = (1-Y/S) d sigma.
t=[my[j]-my[j+1]/S for j in range(2*NINT)]
H=[[t[r+c] for c in range(NINT)] for r in range(NINT)]
rhs=[-t[r+NINT] for r in range(NINT)]
coef,pivots=solve_interval(H,rhs)

def poly(y):
    out=y+coef[NINT-1]
    for j in range(NINT-2,-1,-1): out=out*y+coef[j]
    return out

centers=[
'0.094122924959575790727380599525839660629847596610486822809061323217441674178952467',
'0.33550351611139833695040784476881379573784271717478826232011990388188116674491322',
'0.72940364081132150921676206080326525578112600412038748897984688805136505652318216',
'1.2858362867239552557044300916509543255210711133698187828851696204000293585873927',
'2.01232745391494719753084328308168170278385016344258350461437224708544828782496',
'2.918966401058783851506777838522331695882935082768640217566815636272291709140457',
'4.0192351024302195491246108313955049349263550094226748235082145661456163358600631',
'5.3454205786091935841110986968781267036759418400473119549216226398062685643944024',
'6.9339419408242411345399750749959127228368585005351219275189383953544737793653581',
'8.8377116833368259766907976822285444228261124925385447436313541381438847273881325',
'11.108410941577600074645637183920208086749617290088679100676990228829071687240659',
'13.918021231976696668517471648414866103259923979657240857182233587543484238562752',
'17.754541822608924981602936157103629887860747212402167013067034241111700060207272']
eps=dec('1e-44')
root_signs=[]; y=[]
for cs in centers:
    c=dec(cs); lo,hi=c-eps,c+eps; plo,phi=poly(lo),poly(hi)
    root_signs.append((bool(plo.b<0),bool(plo.a>0),bool(phi.b<0),bool(phi.a>0)))
    y.append(mp.iv.mpf([lo.a,hi.b]))
root_sign_ok=True
for i,(lo_neg,lo_pos,hi_neg,hi_pos) in enumerate(root_signs):
    root_sign_ok = root_sign_ok and ((lo_neg and hi_pos) if i%2==0 else (lo_pos and hi_neg))
ordered=all(bool(y[i].b<y[i+1].a) for i in range(NINT-1)); inside=bool(y[0].a>0 and y[-1].b<S.a)
# Add fixed Radau node Y=S.
nodes=y+[S]
NN=NINT+1
w=[]
for i in range(NN):
    numpoly=[O]; den=O
    for j in range(NN):
        if j==i: continue
        numpoly=poly_mul(numpoly,[-nodes[j],O]); den=den*(nodes[i]-nodes[j])
    num=Z
    for rr,cc in enumerate(numpoly): num += cc*my[rr]
    w.append(num/den)

match=[]
for j in range(NN):
    qmom=Z
    for i in range(NN): qmom += w[i]*(nodes[i]**j)
    rr=qmom-my[j]; match.append(bool(rr.a<=0<=rr.b))
checks={
'all_mu_positive_1_to_Kplus26':allpos,
'all_modified_elimination_pivots_positive':all(bool(pp.a>0) for pp in pivots),
'root_brackets_sign_certified':root_sign_ok,
'interior_root_intervals_ordered':ordered,
'interior_Y_roots_inside_0_1000':inside,
'all_14_weights_positive':all(bool(ww.a>0) for ww in w),
'moment_match_0_to_13_interval_contains_zero':all(match)}

x=[O-y[i]/S for i in range(NINT)]
h=[]
for i in range(NINT):
    xx=x[i]; partial=Z; pp=xx
    for n in range(1,KMAX+1): partial += pp/n; pp*=xx
    hh=(-mp.iv.log(O-xx)-partial)/(xx**KMAX); h.append(hh)
# Endpoint X=0 has h_K(0)=0, so its positive weight contributes zero.
tail=Z
for i in range(NINT): tail += w[i]*h[i]
TLB=muK*muK*tail; Aup=AK-TLB

mp.iv.dps=100
print('NM13-13 T04 DIRECT PRODUCT GAUSS-RADAU14 CERTIFICATE AT 4.38886077')
print('alpha = 438886077/100000000 = 4.38886077')
print('survey support = {651/100000,789/10000,1/2,9211/10000,99349/100000}')
print('survey weights = {5581/100000,3669/20000,13037/25000,3669/20000,5581/100000}')
print('KMAX =',KMAX,'interior_nodes =',NINT,'plus fixed X=0 endpoint; interval dps =',DPS)
print('checks =',checks)
print('A_K =',AK)
print('mu_K =',muK)
print('root sign tuples =',root_signs)
for i in range(NINT): print('Y%d ='%(i+1),y[i],'; X%d ='%(i+1),x[i],'; w%d ='%(i+1),w[i])
print('fixed endpoint Y14=1000; X14=0; w14 =',w[-1])
print('complete direct-product Gauss-Radau14 tail lower bound =',TLB)
print('A upper bound =',Aup)
print('CERTIFIED_STRUCTURAL_CHECKS =',all(checks.values()))
print('CERTIFIED_A_UPPER_NEGATIVE =',bool(Aup.b<0))
print('CERTIFIED_A_NEGATIVE =',bool(Aup.b<0),'because A <= A_K - complete_direct_product_Gauss-Radau14_tail_LB')
