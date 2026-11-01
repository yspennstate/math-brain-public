import itertools, math
import numpy as np

rng=np.random.default_rng(20260923)
max_row=max_spec=max_two=0.0
min_three=float('inf')
viol=0
for _ in range(500):
    M=rng.normal(size=(6,7))
    U,s,Vt=np.linalg.svd(M,full_matrices=False)
    x=s*s
    i=int(rng.integers(0,6))
    w=M[i]
    rows=[r for r in range(6) if r!=i]
    Prow=np.outer(w,w)/(w@w)
    C=M[rows]@(np.eye(7)-Prow)
    G=C@C.T
    e2=0.5*((np.trace(G))**2-np.trace(G@G))
    Ji=0.0
    for ab in itertools.combinations(rows,2):
        B=M[[i,*ab],:]
        Ji+=np.linalg.det(B@B.T)
    rhs=(w@w)*e2
    max_row=max(max_row,abs(Ji-rhs)/max(1.0,abs(Ji),abs(rhs)))

    # Spectral incident identity.
    Jspec=0.0
    for p,q,r in itertools.combinations(range(len(s)),3):
        Jspec += x[p]*x[q]*x[r]*(U[i,p]**2+U[i,q]**2+U[i,r]**2)
    max_spec=max(max_spec,abs(Ji-Jspec)/max(1.0,abs(Ji),abs(Jspec)))

    # Pick the largest natural two-volume residual row marginal and check second descent.
    H=[]
    for a in range(len(rows)):
        H.append(sum(np.linalg.det(C[[a,b]]@C[[a,b]].T) for b in range(len(rows)) if b!=a))
    a=int(np.argmax(H)); k=rows[a]
    P=M[[i,k],:]
    PP=P@P.T
    if np.linalg.det(PP)>1e-12:
        Proj=P.T@np.linalg.inv(PP)@P
        rest=[r for r in range(6) if r not in (i,k)]
        C2=M[rest]@(np.eye(7)-Proj)
        Hik=sum(np.linalg.det(M[[i,k,l],:]@M[[i,k,l],:].T) for l in rest)
        rhs2=np.linalg.det(PP)*np.sum(C2*C2)
        max_two=max(max_two,abs(Hik-rhs2)/max(1.0,abs(Hik),abs(rhs2)))
        if np.sum(C2*C2)>1e-12:
            lidx=int(np.argmax(np.sum(C2*C2,axis=1)))
            l=rest[lidx]
            lhs3=np.linalg.det(M[[i,k,l],:]@M[[i,k,l],:].T)
            rhs3=np.linalg.det(PP)*np.sum(C2[lidx]**2)
            ratio=lhs3/rhs3 if rhs3>1e-12 else 1.0
            min_three=min(min_three,ratio)
            if abs(lhs3-rhs3)>1e-8*max(1.0,abs(lhs3),abs(rhs3)):
                viol+=1

c3=11907/16384
Z0=63/(2**20)*c3**3
C12=3*2**(7/6)*math.exp(1/3)
C21=3*2**(5/6)
CE3=3*2**(4/3)*math.exp(1/3)
print({
    'seed':20260923,
    'trials':500,
    'max_row_anchor_relative_error':max_row,
    'max_spectral_incident_relative_error':max_spec,
    'max_two_row_descent_relative_error':max_two,
    'min_three_row_gram_ratio':min_three,
    'violations':viol,
    'C12':C12,
    'C21':C21,
    'C_E3':CE3,
    'L1_E3_constant':2*math.pi*CE3,
    'Z0':Z0,
    'strongcut_density_constant':CE3*Z0**(-1/6),
    'strongcut_L1_constant':2*math.pi*CE3*Z0**(-1/6),
})
