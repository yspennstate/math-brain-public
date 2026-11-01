#!/usr/bin/env python3
import mpmath as mp
DPS=1450; KMAX=2300; TTAIL=60000
mp.iv.dps=DPS
Z=mp.iv.mpf([0,0]); O=mp.iv.mpf([1,1])
def q(n,d): return mp.iv.mpf([n,n])/d
def dec(s): return mp.iv.mpf([s,s])
alpha=q(43889,10000)
vals=[q(33,5000), q(49,625), O/2, q(576,625), q(4967,5000)]
probs=[q(139,2500), q(1831,10000), q(2613,5000), q(1831,10000), q(139,2500)]
lam=3*alpha/2
pair=[(probs[i]*probs[j], O-vals[i]*vals[j]) for i in range(5) for j in range(5)]
EZ=[O]; pows=[O for _ in pair]
for j in range(1,KMAX+6):
    m=Z
    for idx,(wt,base) in enumerate(pair):
        pows[idx]=pows[idx]*base; m=m+wt*pows[idx]
    EZ.append(mp.iv.exp(lam*(m-O)))
arr=EZ; mus=[O]; series=Z; allpos=True
for k in range(1,KMAX+6):
    arr=[arr[j+1]-arr[j] for j in range(len(arr)-1)]
    mu=arr[0] if k%2==0 else -arr[0]
    mus.append(mu); allpos=allpos and bool(mu.a>0)
    if k<=KMAX: series += mu*mu/k
L=Z
for i in range(5):
 for j in range(5):
  for h in range(5): L += probs[i]*probs[j]*probs[h]*mp.iv.log(O-vals[i]*vals[j]*vals[h])
AK=-series-2*alpha*L
muK=mus[KMAX]; m=[mus[KMAX+j]/muK for j in range(6)]

def det3(M):
    return M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1]) - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0]) + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
H=[[m[0],m[1],m[2]],[m[1],m[2],m[3]],[m[2],m[3],m[4]]]
rhs=[-m[3],-m[4],-m[5]]
D=det3(H)
Mc=[[rhs[r],H[r][1],H[r][2]] for r in range(3)]
Mb=[[H[r][0],rhs[r],H[r][2]] for r in range(3)]
Ma=[[H[r][0],H[r][1],rhs[r]] for r in range(3)]
c=det3(Mc)/D; b=det3(Mb)/D; a=det3(Ma)/D

def poly(x): return x*x*x+a*x*x+b*x+c
br=[(dec('0.9974372408462504946316604'),dec('0.9974372408462504946316606')),
    (dec('0.9990969679342048040980063'),dec('0.9990969679342048040980065')),
    (dec('0.9998509116033566906217556'),dec('0.9998509116033566906217559'))]
sg=[]
for lo,hi in br:
    plo,phi=poly(lo),poly(hi)
    sg.append((bool(plo.b<0),bool(plo.a>0),bool(phi.b<0),bool(phi.a>0)))
root_sign_ok = sg[0][0] and sg[0][3] and sg[1][1] and sg[1][2] and sg[2][0] and sg[2][3]
x=[mp.iv.mpf([lo.a,hi.b]) for lo,hi in br]
w=[]
for i in range(3):
    js=[j for j in range(3) if j!=i]; j,k=js
    num=m[2]-(x[j]+x[k])*m[1]+x[j]*x[k]
    den=(x[i]-x[j])*(x[i]-x[k])
    w.append(num/den)
checks={
 'all_mu_positive':allpos,
 'hankel_det_positive':bool(D.a>0),
 'root_brackets_sign_certified':root_sign_ok,
 'root_intervals_ordered': bool(x[0].b<x[1].a and x[1].b<x[2].a),
 'roots_inside_unit':bool(x[0].a>0 and x[2].b<1),
 'weights_positive':all(bool(ww.a>0) for ww in w),
}
res=[]
for j in range(6):
    qmom=sum(w[i]*(x[i]**j) for i in range(3))
    rr=qmom-m[j]
    res.append(bool(rr.a<=0<=rr.b))
checks['moment_match_0_to_5_interval_contains_zero']=all(res)
powx=[O,O,O]; tail=Z
for t in range(1,TTAIL+1):
    for i in range(3): powx[i]*=x[i]
    gt=w[0]*powx[0]+w[1]*powx[1]+w[2]*powx[2]
    tail += gt*gt/(KMAX+t)
TLB=muK*muK*tail
Aup=AK-TLB
mp.iv.dps=80
print('NM13-13 T04 THREE-NODE GAUSSIAN-TAIL CERTIFICATE')
print('alpha = 43889/10000 = 4.3889')
print('survey support = {33/5000,49/625,1/2,576/625,4967/5000}')
print('survey weights = {139/2500,1831/10000,2613/5000,1831/10000,139/2500}')
print('KMAX =',KMAX); print('TTAIL =',TTAIL); print('interval dps =',DPS)
print('checks =',checks)
print('A_K =',AK); print('mu_K =',muK); print('Hankel det =',D)
print('c,b,a =',c,b,a)
print('root sign tuples =',sg)
for i in range(3): print('x%d ='%(i+1),x[i])
for i in range(3): print('w%d ='%(i+1),w[i])
print('finite Gauss3 tail lower bound =',TLB)
print('A upper bound =',Aup)
print('CERTIFIED_STRUCTURAL_CHECKS =',all(checks.values()))
print('CERTIFIED_A_UPPER_NEGATIVE =',bool(Aup.b<0))
print('CERTIFIED_A_NEGATIVE =',bool(Aup.b<0),'because A <= A_K - finite_Gauss3_tail_LB')
