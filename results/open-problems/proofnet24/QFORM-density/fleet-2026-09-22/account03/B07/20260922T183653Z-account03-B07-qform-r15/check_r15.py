import itertools, math
import numpy as np

# Deterministic sanity checker for the two explicit PSD-contraction examples
# in REPORT.md. This is not used as a proof of the universal theorem.

def build(ell,m,g):
    d=(1-ell)*m+g
    s2=ell*d-g
    s=math.sqrt(s2)
    K=np.zeros((5,5))
    K[:2,:2]=[[ell,s],[s,d]]
    rem=(3-np.trace(K[:2,:2]))/3
    for q in range(2,5): K[q,q]=rem
    assert min(np.linalg.eigvalsh(K))>-1e-12
    assert max(np.linalg.eigvalsh(K))<1-1e-12
    assert abs(np.trace(K)-3)<1e-12
    L=K@np.linalg.inv(np.eye(5)-K)
    D=np.linalg.det(np.eye(5)+L)
    probs={}
    for r in range(6):
        for S in itertools.combinations(range(5),r):
            det=1.0 if r==0 else np.linalg.det(L[np.ix_(S,S)])
            probs[S]=det/D
    return K,probs

def stats(K,probs):
    both=sum(p for S,p in probs.items() if 0 in S and 1 in S)
    none=sum(p for S,p in probs.items() if 0 not in S and 1 not in S)
    xor=sum(p for S,p in probs.items() if ((0 in S) ^ (1 in S)))
    bank=sum(p for S,p in probs.items() if 0 in S and 1 in S and 3<=len(S)<=5)
    return both,none,xor,bank,np.linalg.eigvalsh(K[:2,:2])

for name,g in [('area',1/10),('replacement',1/25)]:
    K,p=build(4/5,3/5,g)
    print(name, stats(K,p))

cstar=(31/64-math.exp(-1))/16
print('cstar',repr(cstar))
print('mu_plus_floor',(7+math.sqrt(33))/16)
print('mu_minus_ceiling',(7-math.sqrt(33))/16)
print('reverse_exclusion_floor',11/13)
