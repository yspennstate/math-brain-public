"""Exact determinant/decoder identities and numerical complete curvature for X065."""
from pathlib import Path
import itertools
import json
import sympy as s
import mpmath as mp

mp.mp.dps = 80
R = s.Rational
I2, I4 = s.eye(2), s.eye(4)
S = s.Matrix([[0,1,2,3],[-1,0,4,5],[-2,-4,0,6],[-3,-5,-6,0]])
t = R(1,1024)
Q = (I4-t*S)*(I4+t*S).inv()
W,V = Q[:,:2],Q[:,2:]
eta = sum(1-W[j,j]**2 for j in range(2))
rates = [R(1,2),R(1,2**40)]
labels = list(itertools.product([0,1],repeat=2))
weights = [s.prod(rates[j] if z[j] else 1-rates[j] for j in range(2)) for z in labels]
sets = [tuple(j for j in range(4) if mask>>j&1) for mask in range(16)]
M = s.Matrix([[R(2,5),s.I/20],[-s.I/20,R(1,2)]])
directions = {
    'definite':s.Matrix([[R(1,10),R(1,40)],[R(1,40),R(1,8)]]),
    'indefinite':s.Matrix([[R(1,10),s.I/30],[-s.I/30,-R(1,10)]]),
}
exact,numerical = 0,0
def ck(value,num=False):
    global exact,numerical
    assert bool(value)
    numerical += int(num)
    exact += int(not num)

def rat(x):
    return s.factor(s.cancel(s.expand_complex(x)))

def realmp(x):
    return mp.mpf(str(s.N(s.re(x),90)))

def volume(C,T):
    if C.cols != len(T):
        return s.Integer(0)
    if not T:
        return s.Integer(1)
    d=C[list(T),:].det()
    return rat(d*s.conjugate(d))

def middle(C,T):
    if len(T)!=C.cols+1:
        return s.zeros(1,2)
    return s.Matrix([[C.row_join(V[:,j])[list(T),:].det() for j in range(2)]])

flag_data=[]
for z in labels:
    C=W[:,[j for j in range(2) if z[j]]]
    flag_data.append([(volume(C,T),middle(C,T),volume(C.row_join(V),T)) for T in sets])

def conditional_jets(data,E):
    d=rat(M.det())
    d0=rat((I2-M).det())
    dd=rat(s.trace(M.adjugate()*E))
    d0d=rat(-s.trace((I2-M).adjugate()*E))
    delta=rat(E.det())
    B=M-d*I2
    Bd=E-dd*I2
    result=[]
    for alpha,e,beta in data:
        norm=rat((e*e.H)[0])
        p=rat(d0*alpha+(e*B*e.H)[0]+d*beta)
        pd=rat(d0d*alpha+(e*Bd*e.H)[0]+dd*beta)
        pdd=rat(2*delta*(alpha+beta-norm))
        result.append((p,pd,pdd))
    return result

def atom(K,T):
    A=s.Matrix.hstack(*[K[:,j] if j in T else (I4-K)[:,j] for j in range(4)])
    return rat(A.det())

def direct_jets(K,A):
    result=[]
    for T in sets:
        p,plus,minus=atom(K,T),atom(K+A,T),atom(K-A,T)
        result.append((p,rat((plus-minus)/2),rat(plus+minus-2*p)))
    return result

def entropy_jets(jets):
    fi=mp.mpf(0)
    acc=mp.mpf(0)
    for p,pd,pdd in jets:
        if p:
            fi+=realmp(pd)**2/realmp(p)
            acc+=realmp(pdd)*mp.log(realmp(p))
        else:
            ck(pd==0 and pdd==0)
    return fi,-fi-acc

ck(Q.T*Q==I4)
ck(eta<=R(224,1024**2))
ck(eta<R(1,4096))
ck(all(V[[i,j],:].det()!=0 for i in range(4) for j in range(i)))
PV=V*V.T
ck(all(PV[i,j]!=0 for i in range(4) for j in range(i)))
ck(M*directions['definite']!=directions['definite']*M)
for N in [M,M+directions['definite']]:
    ck((N-I2/4).det()>0 and (N-I2/4)[0,0]>0)
    ck((3*I2/4-N).det()>0 and (3*I2/4-N)[0,0]>0)
Bg=W*s.diag(*rates)*W.T
K=Bg+V*M*V.T
results={}

for name,E in directions.items():
    latent=[conditional_jets(data,E) for data in flag_data]
    measured=direct_jets(K,V*E*V.T)
    for jets in latent:
        ck(sum(q[0] for q in jets)==1)
        ck(sum(q[1] for q in jets)==0)
        ck(sum(q[2] for q in jets)==0)
    for x in range(16):
        for j in range(3):
            ck(measured[x][j]==rat(sum(weights[z]*latent[z][x][j] for z in range(4))))
    epsilon=rat(sum(weights[z]*latent[z][x][0] for z in range(4) for x,T in enumerate(sets)
                    if labels[z]!=(int(0 in T),int(1 in T))))
    ck(epsilon<=eta)
    for j in range(2):
        actual_error=rat(sum(weights[z]*latent[z][x][0] for z in range(4) for x,T in enumerate(sets)
                            if labels[z][j]!=int(j in T)))
        rj=1-W[j,j]**2
        bj=sum(rates[k]*W[j,k]**2 for k in range(2) if k!=j)+(V*M*V.T)[j,j]
        ck(actual_error==rat(rates[j]*rj+(1-2*rates[j])*bj))
        ck(actual_error<=rj)

    fi,hess=entropy_jets(measured)
    latent_stats=[entropy_jets(jets) for jets in latent]
    average_hess=sum(realmp(w)*v[1] for w,v in zip(weights,latent_stats))
    joint_fi=sum(realmp(w)*v[0] for w,v in zip(weights,latent_stats))
    loss=joint_fi-fi
    correction,posterior_correction,posterior_entropy=mp.mpf(0),mp.mpf(0),mp.mpf(0)
    for z,w in enumerate(weights):
        for x,(p,pd,pdd) in enumerate(latent[z]):
            if p:
                ratio=realmp(p)/realmp(measured[x][0])
                log_post=mp.log(realmp(w)*ratio)
                correction+=realmp(w*pdd)*mp.log(ratio)
                posterior_correction+=realmp(w*pdd)*log_post
                posterior_entropy-=realmp(w*p)*log_post
                ck(abs(pdd)<=32*abs(E.det())*p)
                if E.det()>0:
                    ck(abs(pd)<=4*s.trace(E)*p)
    identity_error=abs(hess-average_hess-loss-correction)
    ck(identity_error<mp.mpf('1e-65'),True)
    ck(abs(correction-posterior_correction)<mp.mpf('1e-65'),True)
    ep=realmp(epsilon)
    fano=-ep*mp.log(ep)-(1-ep)*mp.log(1-ep)+ep*mp.log(3)
    ck(posterior_entropy<=fano,True)
    rbound=32*realmp(abs(E.det()))*posterior_entropy
    ck(abs(correction)<=rbound,True)
    if E.det()>0:
        loss_bound=64*ep*realmp(s.trace(E))**2
        ck(loss<=loss_bound,True)
        lower=mp.mpf(5)/8*realmp(s.trace(E))**2
        ck(-hess>=lower,True)
    else:
        lower,loss_bound=fi,None
        ck(-hess>=fi,True)
    results[name]={
        'minus_hessian':str(-hess),'entire_fisher':str(fi),'conditional_average_minus_hessian':str(-average_hess),
        'posterior_fisher_loss':str(loss),'signed_log_correction':str(correction),
        'posterior_entropy':str(posterior_entropy),'fano_bound':str(fano),
        'classification_error':str(ep),'score_loss_bound':str(loss_bound),'absolute_log_bound':str(rbound),
        'proved_lower_bound':str(lower),'complete_identity_error':str(identity_error),
    }

L=K*(I4-K).inv()
detR=rat(L.det()/s.prod(L[j,j] for j in range(4)))
ck(detR<R(1,16))
hz=-sum(realmp(w)*mp.log(realmp(w)) for w in weights)
ck(hz>=mp.log(2),True)
results.update({
    'exact_assertions':exact,'high_precision_assertions':numerical,
    'eta_exact':str(eta),'eta_decimal':str(realmp(eta)),
    'background_rates':[str(x) for x in rates],
    'prior_label_entropy':str(hz),'odds_correlation_determinant':str(realmp(detR)),
    'scope':'Finite algebra checks. Universal signs and all-rate theorem are proved analytically in agents/X065.md.',
})
Path(__file__).with_name('certificate.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
