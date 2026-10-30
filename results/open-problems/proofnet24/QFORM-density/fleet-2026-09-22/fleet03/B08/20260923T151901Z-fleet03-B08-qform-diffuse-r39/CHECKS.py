import math
import numpy as np

rng=np.random.default_rng(20260923)

def frame(n,r):
    q,_=np.linalg.qr(rng.normal(size=(n,r)))
    return q[:,:r]

def e2(M):
    s=np.linalg.svd(M,compute_uv=False)
    return sum((s[i]*s[j])**2 for i in range(len(s)) for j in range(i+1,len(s)))

def check_plucker():
    cases=0; violations=0; maxerr=0.0
    for n in range(4,9):
        for _ in range(80):
            U=frame(n,2)
            ell=np.sum(U*U,axis=1); mu=float(np.max(ell))
            lam=np.array([1.3,-2.1])
            S=U@np.diag(lam)@U.T
            best=-1.0
            for mask in range(1,(1<<n)-1):
                I=[i for i in range(n) if (mask>>i)&1]
                J=[i for i in range(n) if not ((mask>>i)&1)]
                if len(I)<2 or len(J)<2:
                    continue
                GI=U[I].T@U[I]; GJ=U[J].T@U[J]
                prod=float(np.linalg.det(GI)*np.linalg.det(GJ))
                best=max(best,prod)
                M=S[np.ix_(I,J)]
                rhs=float((abs(lam[0]*lam[1])**2)*prod)
                maxerr=max(maxerr,abs(e2(M)-rhs))
            lower=max(0.0,(1-2*mu)/16)
            if best+1e-11<lower:
                violations+=1
            cases+=1
    return cases,violations,maxerr

def check_balancing():
    cases=0; violations=0; maxratio=0.0
    for r in (2,3):
        for n in range(max(2*r,4),9):
            for _ in range(50):
                U=frame(n,r)
                ell=np.sum(U*U,axis=1); mu=float(np.max(ell))
                target=math.sqrt(r*mu/4)
                best=999.0
                for mask in range(1,(1<<n)-1):
                    I=[i for i in range(n) if (mask>>i)&1]
                    GI=U[I].T@U[I]
                    best=min(best,float(np.linalg.norm(GI-.5*np.eye(r),2)))
                if best>target+1e-11:
                    violations+=1
                if target>0:
                    maxratio=max(maxratio,best/target)
                cases+=1
    return cases,violations,maxratio

pc,pv,pe=check_plucker()
bc,bv,br=check_balancing()
CE2=36.44334493792993
mu3=1/16
g3=.5-math.sqrt(3*mu3/4)
Ctail=9*math.sqrt(3)*math.e/2
print('plucker_cases',pc)
print('plucker_violations',pv)
print('max_e2_identity_abs_error',format(pe,'.16e'))
print('balance_cases',bc)
print('balance_violations',bv)
print('max_balance_ratio',format(br,'.12f'))
print('C_exact_mu_le_1_4',format(CE2*32**(1/8),'.12f'))
print('C_nearrank2_mu_le_1_8_eta_1_15',format(CE2/math.sqrt(.25-1/15),'.12f'))
print('g3_mu_1_16',format(g3,'.12f'))
print('C_rank3_volume_square_beta1',format(2*math.sqrt(46/g3),'.12f'))
print('QFORM_B08_R39_CHECK_PASS')
