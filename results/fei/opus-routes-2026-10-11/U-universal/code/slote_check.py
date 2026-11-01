"""Check, on small cases, the anticommuting-assembly identity behind Slote's quantum FEI counterexample:
A = sum_l P_l (x) B_l with pairwise anticommuting Pauli P_l and commuting diagonal B_l, sum B_l^2 = I  =>  A^2 = I.
Also compute the classical analogue's failure: the 'relaxed row family' with only the pointwise norm identity."""
import numpy as np, itertools
I2=np.eye(2); X=np.array([[0,1],[1,0]]); Y=np.array([[0,-1j],[1j,0]]); Z=np.diag([1,-1])
def kron(*ms):
    out=np.array([[1]])
    for m in ms: out=np.kron(out,m)
    return out
# r=1: F_1 = {X, Y, Z} on 1 qubit, L = largest power of 2 less than 3 -> 2: use {X, Z}
P=[X,Z]; L=2
# k=1 block of L=2 qubits: G(x)=H Diag(x) 1, B_l = sum_a H[l,a] Z_a
H=np.array([[1,1],[1,-1]])
Za=[kron(Z,I2),kron(I2,Z)]
B=[sum(H[l,a]*Za[a] for a in range(L)) for l in range(L)]
S=sum(b@b for b in B); print('sum B^2 = c*I ?', np.allclose(S, S[0,0]*np.eye(4)), S[0,0])
M=sum(np.kron(P[l],B[l]) for l in range(L)); A=M/np.sqrt(S[0,0])
print('A^2 = I ?', np.allclose(A@A, np.eye(8)))
# Pauli coefficients of A
paulis={'I':I2,'X':X,'Y':Y,'Z':Z}
coef={}
for lab in itertools.product('IXYZ',repeat=3):
    Pm=kron(*[paulis[c] for c in lab]); c=np.trace(Pm.conj().T@A).real/8
    if abs(c)>1e-12: coef[''.join(lab)]=c
print(coef)
p=np.array(list(coef.values()))**2; Hs=-(p*np.log2(p)).sum()
Iq=sum(sum(ch!='I' for ch in k)*v**2 for k,v in coef.items())
print('quantum H, I =',Hs,Iq)
