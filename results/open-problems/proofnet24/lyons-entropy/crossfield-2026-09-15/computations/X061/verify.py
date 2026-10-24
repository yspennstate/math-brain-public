"""Exact algebra and high-precision checks for X061; signs are proved in text."""
from pathlib import Path
import json
import itertools
import sympy as s
import mpmath as mp

mp.mp.dps = 80
R = s.Rational
I4 = s.eye(4)
h = s.Matrix([1, 2, 3, 4])
g = s.Matrix([2, -1, 1, 3])
Q = (I4-2*g*g.T/15)*(I4 - h*h.T/15)
W, V = Q[:, :2], Q[:, 2:]
assert Q.T*Q == I4
rates = [1-R(1,1024), R(1,2048)]
M = s.Matrix([[R(2,5), s.I/20],[-s.I/20,R(1,2)]])
directions = {
    "definite": s.Matrix([[R(1,10),R(1,40)],[R(1,40),R(1,8)]]),
    "indefinite": s.Matrix([[R(1,10),s.I/30],[-s.I/30,-R(1,10)]]),
}
subsets = [tuple(j for j in range(4) if (mask>>j)&1) for mask in range(16)]
labels = list(itertools.product([0,1], repeat=2))
weights = [s.prod(rates[j] if z[j] else 1-rates[j] for j in range(2)) for z in labels]
backgrounds = [sum((W[:,j]*W[:,j].T for j in range(2) if z[j]), s.zeros(4)) for z in labels]
Bg = W*s.diag(*rates)*W.T
checks = 1
numerical_checks = 0

def ck(v, numerical=False):
    global checks, numerical_checks
    assert bool(v)
    checks += 1
    numerical_checks += int(numerical)

def atom(K, S):
    return s.factor(s.Matrix.hstack(*[K[:,j] if j in S else (I4-K)[:,j] for j in range(4)]).det())

def jet(K, A, S):
    p = atom(K,S)
    plus, minus = atom(K+A,S), atom(K-A,S)
    return (p, s.factor((plus-minus)/2), s.factor(plus+minus-2*p))

def f(x):
    return mp.mpf(str(s.N(s.re(x),90)))

def ent_curv(jets):
    fi = mp.mpf(0)
    accel = mp.mpf(0)
    for p,d,dd in jets:
        if p:
            fi += f(d)**2/f(p)
            accel += f(dd)*mp.log(f(p))
        else:
            ck(d==0 and dd==0)
    return fi,accel, -fi-accel

def minor_mass(C,S):
    if len(S)!=C.cols:
        return s.Integer(0)
    if not S:
        return s.Integer(1)
    d = C[list(S),:].det()
    return s.factor(d*s.conjugate(d))

P = V*V.T
seen={0}
for _ in range(4):
    seen.update(j for j in range(4) if any(P[i,j]!=0 for i in tuple(seen)))
ck(len(seen)==4)
ck(all(V[[i,j],:].det()!=0 for i in range(4) for j in range(i)))
ck(M*directions['definite'] != directions['definite']*M)
for N in [M, M+directions['definite']]:
    ck((N-s.eye(2)/4).det()>0 and (N-s.eye(2)/4)[0,0]>0)
    ck((3*s.eye(2)/4-N).det()>0 and (3*s.eye(2)/4-N)[0,0]>0)

results={}
for name,E in directions.items():
    A=V*E*V.T
    delta=s.factor(E.det())
    latent=[]
    for z,B in zip(labels,backgrounds):
        C=W[:,[j for j in range(2) if z[j]]]
        jets=[jet(B+V*M*V.T,A,S) for S in subsets]
        ck(sum(p for p,d,dd in jets)==1)
        ck(sum(d for p,d,dd in jets)==0)
        ck(sum(dd for p,d,dd in jets)==0)
        for S,(p,d,dd) in zip(subsets,jets):
            c=minor_mass(C,S)+minor_mass(C.row_join(V),S)
            c-=minor_mass(C.row_join(V[:,0]),S)+minor_mass(C.row_join(V[:,1]),S)
            ck(dd==2*delta*c)
            if p:
                ck(d*d <= 32*s.trace(E*E)*p*p)
                ck(abs(dd)<=32*abs(delta)*p)
                if delta>0:
                    ck(abs(d)<=4*s.trace(E)*p)
        latent.append(jets)
    measured=[jet(Bg+V*M*V.T,A,S) for S in subsets]
    for x in range(16):
        for j in range(3):
            ck(measured[x][j]==sum(weights[z]*latent[z][x][j] for z in range(4)))
    stats=[ent_curv(j) for j in latent]
    fi,accel,hess=ent_curv(measured)
    fi_joint=sum(f(w)*v[0] for w,v in zip(weights,stats))
    latent_hess=sum(f(w)*v[2] for w,v in zip(weights,stats))
    correction=mp.mpf(0)
    posterior_correction=mp.mpf(0)
    posterior_entropy=mp.mpf(0)
    for z,w in enumerate(weights):
        for x,(p,d,dd) in enumerate(latent[z]):
            if p:
                correction += f(w)*f(dd)*mp.log(f(p)/f(measured[x][0]))
                posterior_log=mp.log(f(w)*f(p)/f(measured[x][0]))
                posterior_correction += f(w)*f(dd)*posterior_log
                posterior_entropy -= f(w)*f(p)*posterior_log
    loss=fi_joint-fi
    err=abs(hess-latent_hess-loss-correction)
    ck(err<mp.mpf('1e-70'), numerical=True)
    tau=1-max(weights)
    hz=-sum(f(w)*mp.log(f(w)) for w in weights)
    log_bound=32*f(abs(delta))*hz
    ck(abs(correction)<=log_bound, numerical=True)
    ck(abs(correction-posterior_correction)<mp.mpf('1e-70'), numerical=True)
    ck(abs(correction)<=32*f(abs(delta))*posterior_entropy, numerical=True)
    if delta>0:
        score_bound=64*f(tau)*f(s.trace(E))**2
        ck(loss<=score_bound, numerical=True)
        proved=mp.mpf(5)/12*f(s.trace(E))**2
        ck(-hess>=proved, numerical=True)
    else:
        score_bound=None
        proved=fi
        ck(-hess>=fi, numerical=True)
    results[name]={
        'minus_hessian':str(-hess), 'entire_fisher':str(fi),
        'posterior_score_loss':str(loss), 'signed_log_correction':str(correction),
        'score_loss_bound':str(score_bound), 'absolute_log_bound':str(log_bound),
        'posterior_entropy':str(posterior_entropy),
        'identity_error':str(err), 'proved_lower_bound':str(proved),
    }

K=Bg+V*M*V.T
L=K*(I4-K).inv()
detR=s.factor(L.det()/s.prod(L[j,j] for j in range(4)))
ck(detR<R(1,16))
ck(4*(1-max(weights))+R(1,64)<R(3,128))
results['exact_assertions']=checks-numerical_checks
results['high_precision_assertions']=numerical_checks
results['odds_correlation_determinant']=str(detR)
results['background_rates']=[str(x) for x in rates]
results['scope']='Finite algebra checks; universal inequalities are proved in agents/X061.md.'
Path(__file__).with_name('certificate.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
