#!/usr/bin/env python3
import math
import mpmath as mp

DPS=1500
KMAX=2300
TTAIL=60000
SCALE=1000
mp.iv.dps=DPS
Z=mp.iv.mpf([0,0]); O=mp.iv.mpf([1,1]); S=mp.iv.mpf([SCALE,SCALE])

def q(n,d): return mp.iv.mpf([n,n])/d
def dec(s): return mp.iv.mpf([s,s])

def det(M):
    n=len(M)
    if n==1: return M[0][0]
    out=Z
    for j in range(n):
        sub=[row[:j]+row[j+1:] for row in M[1:]]
        term=M[0][j]*det(sub)
        out = out-term if j%2 else out+term
    return out

def poly_mul(A,B):
    out=[Z for _ in range(len(A)+len(B)-1)]
    for i,a in enumerate(A):
        for j,b in enumerate(B): out[i+j]=out[i+j]+a*b
    return out

alpha=q(54861,12500) # 4.38888 exactly
vals=[q(33,5000), q(49,625), O/2, q(576,625), q(4967,5000)]
probs=[q(139,2500), q(1831,10000), q(2613,5000), q(1831,10000), q(139,2500)]
lam=3*alpha/2

pair=[(probs[i]*probs[j], O-vals[i]*vals[j]) for i in range(5) for j in range(5)]
EZ=[O]; pows=[O for _ in pair]
for j in range(1,KMAX+9):
    m=Z
    for idx,(wt,base) in enumerate(pair):
        pows[idx]=pows[idx]*base
        m=m+wt*pows[idx]
    EZ.append(mp.iv.exp(lam*(m-O)))

arr=EZ; mus=[O]; series=Z; allpos=True
for k in range(1,KMAX+9):
    arr=[arr[j+1]-arr[j] for j in range(len(arr)-1)]
    mu=arr[0] if k%2==0 else -arr[0]
    mus.append(mu)
    allpos=allpos and bool(mu.a>0)
    if k<=KMAX: series += mu*mu/k

L=Z
for i in range(5):
    for j in range(5):
        for h in range(5):
            L += probs[i]*probs[j]*probs[h]*mp.iv.log(O-vals[i]*vals[j]*vals[h])
AK=-series-2*alpha*L
muK=mus[KMAX]

# Tilted Q moments m_j = mu_{K+j}/mu_K, then scale Y=1000(1-Q).
mq=[mus[KMAX+j]/muK for j in range(8)]
my=[]
for j in range(8):
    v=Z
    for ell in range(j+1):
        term=mp.iv.mpf([math.comb(j,ell),math.comb(j,ell)])*mq[ell]
        v = v-term if ell%2 else v+term
    my.append((S**j)*v)

# Monic quartic orthogonal to 1,Y,Y^2,Y^3 under the tilted law.
H=[[my[r+c] for c in range(4)] for r in range(4)]
rhs=[-my[r+4] for r in range(4)]
D=det(H)
coef=[] # a0,a1,a2,a3 in Y^4+a3Y^3+a2Y^2+a1Y+a0
for col in range(4):
    M=[[H[r][c] for c in range(4)] for r in range(4)]
    for r in range(4): M[r][col]=rhs[r]
    coef.append(det(M)/D)
a0,a1,a2,a3=coef

def poly(y): return y**4+a3*y**3+a2*y**2+a1*y+a0

# Disjoint certified brackets for the four Y-roots.
br=[
    (dec('0.1160216189968832978010080'),dec('0.1160216189968832978010082')),
    (dec('0.6835582501842503957625136'),dec('0.6835582501842503957625140')),
    (dec('1.8428500366871657771422267'),dec('1.8428500366871657771422273')),
    (dec('3.8702375009266318495968855'),dec('3.8702375009266318495968865')),
]
sg=[]; y=[]
for lo,hi in br:
    plo,phi=poly(lo),poly(hi)
    sg.append((bool(plo.b<0),bool(plo.a>0),bool(phi.b<0),bool(phi.a>0)))
    y.append(mp.iv.mpf([lo.a,hi.b]))
# Expected alternating signs: +-, -+, +-, -+.
root_sign_ok = (sg[0][1] and sg[0][2] and sg[1][0] and sg[1][3] and
                sg[2][1] and sg[2][2] and sg[3][0] and sg[3][3])

# Gaussian weights from the Lagrange basis, using moments 0..3.
w=[]
for i in range(4):
    numpoly=[O]; den=O
    for j in range(4):
        if j==i: continue
        numpoly=poly_mul(numpoly,[-y[j],O])
        den=den*(y[i]-y[j])
    num=Z
    for r,cc in enumerate(numpoly): num += cc*my[r]
    w.append(num/den)

checks={
  'all_mu_positive_1_to_Kplus8': allpos,
  'hankel_det_positive': bool(D.a>0),
  'root_brackets_sign_certified': root_sign_ok,
  'root_intervals_ordered': bool(y[0].b<y[1].a and y[1].b<y[2].a and y[2].b<y[3].a),
  'Y_roots_inside_0_1000': bool(y[0].a>0 and y[3].b<S.a),
  'weights_positive': all(bool(ww.a>0) for ww in w),
}
res=[]
for j in range(8):
    qmom=Z
    for i in range(4): qmom += w[i]*(y[i]**j)
    rr=qmom-my[j]
    res.append(bool(rr.a<=0<=rr.b))
checks['moment_match_0_to_7_interval_contains_zero']=all(res)

# Q-nodes and the finite four-node Gaussian tail lower bound.
x=[O-y[i]/S for i in range(4)]
powx=[O,O,O,O]; tail=Z
for t in range(1,TTAIL+1):
    for i in range(4): powx[i]*=x[i]
    gt=Z
    for i in range(4): gt += w[i]*powx[i]
    tail += gt*gt/(KMAX+t)
TLB=muK*muK*tail
Aup=AK-TLB

mp.iv.dps=80
print('NM13-13 T04 FOUR-NODE GAUSSIAN-TAIL CERTIFICATE')
print('alpha = 54861/12500 = 4.38888')
print('survey support = {33/5000,49/625,1/2,576/625,4967/5000}')
print('survey weights = {139/2500,1831/10000,2613/5000,1831/10000,139/2500}')
print('KMAX =',KMAX); print('TTAIL =',TTAIL); print('interval dps =',DPS)
print('checks =',checks)
print('A_K =',AK)
print('mu_K =',muK)
print('Hankel det =',D)
print('quartic coefficients a0,a1,a2,a3 =',a0,a1,a2,a3)
print('root sign tuples =',sg)
for i in range(4): print('Y%d ='%(i+1),y[i],'; Q%d ='%(i+1),x[i],'; w%d ='%(i+1),w[i])
print('finite Gauss4 tail lower bound =',TLB)
print('A upper bound =',Aup)
print('CERTIFIED_STRUCTURAL_CHECKS =',all(checks.values()))
print('CERTIFIED_A_UPPER_NEGATIVE =',bool(Aup.b<0))
print('CERTIFIED_A_NEGATIVE =',bool(Aup.b<0),'because A <= A_K - finite_Gauss4_tail_LB')
