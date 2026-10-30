import itertools
import math
import numpy as np

# Regression from REPORT section 6: coordinates (a,b,k,1,2,3).
A=np.zeros((6,6),dtype=float)
for i,j in [(0,3),(1,4),(2,5)]:
    A[i,j]=A[j,i]=1.0

evals=np.linalg.eigvalsh(A)
assert np.allclose(evals,[-1,-1,-1,1,1,1],atol=1e-12)

# Rank-two hub/star data on leaves (k,1,2,3).
P=np.eye(2)
C=np.array([[0.,0.],[1.,0.],[0.,1.],[0.,0.]])
D=np.zeros((4,4),dtype=float)
D[0,3]=D[3,0]=1.0

def e3_cross(M):
    total=0.0
    for rs in itertools.combinations(range(M.shape[0]),3):
        for cs in itertools.combinations(range(M.shape[1]),3):
            total += np.linalg.det(M[np.ix_(rs,cs)])**2
    return total

gamma2=[]
for k in range(4):
    idx=[j for j in range(4) if j!=k]
    Mk=np.vstack([C[idx].T,D[k,idx]])
    gamma2.append(e3_cross(Mk))
assert np.allclose(gamma2,[1,0,0,1],atol=1e-12)
assert abs(sum(gamma2)-2.0)<1e-12

# S={k}, T={1,2,3}.
T=[1,2,3]
B_T=P@C[T].T
Delta=float(np.linalg.det(B_T@B_T.T))
assert abs(Delta-1.0)<1e-12
K=np.vstack([B_T,D[0,T]])
assert np.allclose(K,np.eye(3),atol=1e-12)
assert abs(np.linalg.det(K)-1.0)<1e-12

# Numerical constants stated in REPORT.
rank1_base=4*2**(3/4)*math.e**(1/4)
rank1_local=rank1_base*(25/16)**(1/4)
indef_local=11.463*(400/27)**(1/20)
zero_local=2*math.sqrt(2)*(25/16)**(1/4)
assert rank1_base < 8.638
assert rank1_local < 9.658
assert indef_local < 13.117
assert abs(zero_local-math.sqrt(10))<1e-12

print('eigenvalues=',evals.tolist())
print('Gamma_k^2=',gamma2,'G_*=',sum(gamma2))
print('Delta_T=',Delta,'det K=',float(np.linalg.det(K)))
print('rank1_base=',rank1_base)
print('rank1_local=',rank1_local)
print('indef_local=',indef_local)
print('zero_local=',zero_local)
print('all checks passed')
