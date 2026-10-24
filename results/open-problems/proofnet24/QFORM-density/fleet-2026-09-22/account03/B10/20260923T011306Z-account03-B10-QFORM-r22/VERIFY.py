import itertools, math
import numpy as np

# Deterministic regression for the collinear-bank capped-basis identities.
# This is only a check of the algebra used in REPORT.md, not a proof.

def build_frame(L, proportions):
    proportions = np.asarray(proportions, dtype=float)
    proportions /= proportions.sum()
    alpha = np.sqrt(L * proportions)
    rho = 1.0 - L

    # Complement rows in the basis (r,e1,e2), r=(1,0,0).
    # Two longitudinal rows and two copies of each transverse axis.
    C = np.array([
        [math.sqrt(rho/2.0),0,0],
        [math.sqrt(rho/2.0),0,0],
        [0,1/math.sqrt(2),0],
        [0,1/math.sqrt(2),0],
        [0,0,1/math.sqrt(2)],
        [0,0,1/math.sqrt(2)],
    ])
    B = np.column_stack([alpha, np.zeros((len(alpha),2))])
    R = np.vstack([B,C])
    return alpha,C,R

def entropy_score(alpha2, p):
    return math.exp(sum(pi*math.log(ai/pi) for ai,pi in zip(alpha2,p) if pi>0))

def check_case(L, proportions):
    alpha,C,R = build_frame(L, proportions)
    assert np.max(np.abs(R.T@R-np.eye(3))) < 2e-12
    r=np.array([1.0,0.0,0.0])
    nus={}
    for j,k in itertools.combinations(range(len(C)),2):
        nus[j,k]=np.linalg.det(np.vstack([r,C[j],C[k]]))**2
    assert abs(sum(nus.values())-1) < 2e-12
    q=np.zeros(len(C))
    for (j,k),v in nus.items():
        q[j]+=v; q[k]+=v
    q_direct=np.sum(C[:,1:]**2,axis=1)
    assert np.max(np.abs(q-q_direct)) < 2e-12
    assert np.max(q) <= 0.5 + 2e-12

    a2=alpha**2
    h=float(np.max(a2))
    if h <= L/2 + 1e-12:
        p=a2/L
        target=L
    else:
        i=int(np.argmax(a2)); s=L-h
        p=np.zeros_like(a2); p[i]=0.5
        for j in range(len(a2)):
            if j != i: p[j]=0.5*a2[j]/s
        target=2*math.sqrt(h*s)
    assert abs(p.sum()-1)<2e-12 and np.max(p)<=0.5+2e-12
    Z=entropy_score(a2,p)
    assert abs(Z-target)<2e-12

    # Full product basis distribution w_(i,j,k)=p_i nu_jk.
    # Check marginals and determinant-entropy factorization.
    weights=[]; det2=[]
    for i,pi in enumerate(p):
        for (j,k),nu in nus.items():
            if pi*nu>0:
                weights.append(pi*nu)
                det2.append(a2[i]*nu)
    weights=np.asarray(weights); det2=np.asarray(det2)
    assert abs(weights.sum()-1)<2e-12
    Zfull=math.exp(np.sum(weights*np.log(det2/weights)))
    assert abs(Zfull-target)<2e-12
    return h, float(np.max(q)), Zfull

for L,props,name in [
    (0.9,[0.30,0.25,0.25,0.20],"diffuse-bank"),
    (0.9,[0.70,0.10,0.10,0.10],"clipped-heavy-bank"),
]:
    h,qmax,Z=check_case(L,props)
    print(name, "L=",L,"h=",h,"qmax=",qmax,"Z=",Z)

print("near-endpoint diffuse constant",3*math.e*(8/7)**(1/3))
print("near-endpoint clipped constant",3*math.e*(16/math.sqrt(7))**(1/3))
print("QFORM_B10_NULLRAY_CAPPED_BASIS_CHECK_PASS")
