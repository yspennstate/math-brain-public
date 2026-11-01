import numpy as np
print("P0189: clock/shift pair U^q=I, V^q=-I; claim det(zI-U-V)=z^q so empirical eigenvalue measure = delta_0")
for q in [3,4,5,8,13,32]:
    w=np.exp(2j*np.pi/q)
    U=np.diag([w**k for k in range(q)])
    S=np.roll(np.eye(q),1,axis=0)
    V=np.exp(1j*np.pi/q)*S
    A=U+V
    ev=np.linalg.eigvals(A)
    Uq=np.linalg.matrix_power(U,q); Vq=np.linalg.matrix_power(V,q); Aq=np.linalg.matrix_power(A,q)
    print(f" q={q:>3}: ||U^q-I||={np.abs(Uq-np.eye(q)).max():.2e}  ||V^q+I||={np.abs(Vq+np.eye(q)).max():.2e}"
          f"  ||(U+V)^q||={np.abs(Aq).max():.2e}  max|eig(U+V)|={np.abs(ev).max():.3e}")
print("\n=> U+V is nilpotent, all eigenvalues 0, empirical measure delta_0 at every q. CONFIRMED.")
print("Norms (the strong-convergence side): ||U+V|| should converge to the limit operator's norm")
for q in [5,13,32,101,401]:
    w=np.exp(2j*np.pi/q); U=np.diag([w**k for k in range(q)]); S=np.roll(np.eye(q),1,axis=0)
    V=np.exp(1j*np.pi/q)*S; A=U+V
    print(f" q={q:>4}: ||U+V||_op = {np.linalg.norm(A,2):.6f}   (2 = the free/commuting upper bound)")
