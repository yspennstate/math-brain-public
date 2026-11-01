import itertools, math
import numpy as np

delta=1/100
eps=1e-6
U=np.zeros((6,3))
U[0]=[math.sqrt(1-delta),0,0]
for j in range(5):
    t=2*math.pi*j/5
    U[j+1]=[math.sqrt(delta/5),math.sqrt(2/5)*math.cos(t),math.sqrt(2/5)*math.sin(t)]
V=np.array([[1,2,2],[2,1,-2],[2,-2,1]],dtype=float)/3
M=U@np.diag([eps,2,2])@V.T

triples=list(itertools.combinations(range(6),3))
d2=np.array([np.linalg.det(M[list(S),:])**2 for S in triples])
Z=d2.sum(); P=d2/Z
marg=np.array([sum(P[k] for k,S in enumerate(triples) if i in S) for i in range(6)])
E=np.array([0 in S for S in triples])
p=P[E].sum(); c=0.5
w=np.zeros_like(P)
w[E]=c*P[E]/P[E].sum(); w[~E]=(1-c)*P[~E]/P[~E].sum()
wmarg=np.array([sum(w[k] for k,S in enumerate(triples) if i in S) for i in range(6)])
KL=sum(w[k]*math.log(w[k]/P[k]) for k in range(len(P)) if w[k]>0)
KL_formula=0.5*math.log(1/(4*delta*(1-delta)))
G=Z*math.exp(-KL_formula)
Cvol=3*math.e*G**(-1/6)

k1=eps**2/(eps**2+1/16); k2=64/65
K=U@np.diag([k1,k2,k2])@U.T
theta=k1+128/65
D=4225*(1+16*eps**2)
Cridge=8*3**(-5/8)*math.sqrt(math.e)*math.sqrt(3*theta/(3*theta-4))*D**(-1/(4*theta))/math.sqrt(1/4)

A=np.zeros((10,10)); A[0,0]=1; A[1:7,7:10]=M; A[7:10,1:7]=M.T
b=M[1,0]
Cpartner=63.11383495773493/math.sqrt(abs(b))

print('max|U^TU-I|',np.max(np.abs(U.T@U-np.eye(3))))
print('det V',np.linalg.det(V),'max|V^TV-I|',np.max(np.abs(V.T@V-np.eye(3))))
print('singular values M',np.linalg.svd(M,compute_uv=False))
print('min |physical cross entry|',np.min(np.abs(M)))
print('E3',Z,'expected',16*eps**2)
print('raw row marginals',marg)
print('q=1 optimized row marginals',wmarg)
print('KL numeric',KL,'formula',KL_formula)
print('G',G)
print('optimized volume bound',Cvol)
print('ridge K diagonal',np.diag(K))
print('theta',theta,'D',D,'ridge bound',Cridge)
print('full spectrum',np.linalg.eigvalsh(A))
print('pair coefficient b',b,'partner bound',Cpartner)
print('hierarchy ridge < partner < volume',Cridge<Cpartner<Cvol)
