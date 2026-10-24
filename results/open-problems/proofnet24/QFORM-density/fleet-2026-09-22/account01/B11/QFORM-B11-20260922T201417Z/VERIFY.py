import math
import numpy as np

for m in range(5, 13):
    rows = [[math.sqrt(3)/2, 0.0, 0.0]]
    for j in range(m):
        th = 2*math.pi*j/m
        rows.append([
            1/(2*math.sqrt(m)),
            math.sqrt(2/m)*math.cos(th),
            math.sqrt(2/m)*math.sin(th),
        ])
    R = np.array(rows)
    err_parseval = np.linalg.norm(R.T@R-np.eye(3), ord=2)
    G = R[1:].T@R[1:]
    Gi2 = np.diag([2.0,1.0,1.0])
    U = R[1:]@Gi2
    err_U = np.linalg.norm(U.T@U-np.eye(3), ord=2)
    lev = np.sum(U*U, axis=1)
    print(m, f"parseval={err_parseval:.3e}", f"U={err_U:.3e}",
          f"lev_min={lev.min():.12f}", f"lev_max={lev.max():.12f}",
          f"3/m={3/m:.12f}")

C1 = 128*2**(1/8)*math.e**(9/8)
C2 = 3*400**(1/3)*2**(7/12)*math.e**(7/12)
alpha = math.sqrt(2/5)
print("C1", C1)
print("C2", C2)
print("m5_branch1", C1*alpha**(-3/4))
print("m5_branch2", C2*alpha**(-5/6))
print("diffuse_bound", 3*math.e*4**(1/3))
print("QFORM_HEAVY_DELETE_DIFFUSE_CHECK_PASS")
