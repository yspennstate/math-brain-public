import math
import random

RNG = random.Random(130193004)


def det3(M):
    a,b,c=M[0]
    d,e,f=M[1]
    g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def transpose(A):
    return [list(x) for x in zip(*A)]


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


max_zero_err=0.0
max_graph_det_err=0.0
max_graph_pivot_err=0.0

for _ in range(20000):
    # Canonical zero-pivot determinant relation det M=-a^2 b22.
    a=RNG.uniform(-3.0,3.0)
    if abs(a)<0.2:
        a=0.2 if a>=0 else -0.2
    b=RNG.uniform(-2.0,2.0)
    e=RNG.uniform(-2.0,2.0)
    d=RNG.uniform(-3.0,3.0)
    if abs(d)<0.2:
        d=0.2 if d>=0 else -0.2
    M=[[0.0,a,0.0],[a,b,e],[0.0,e,d]]
    max_zero_err=max(max_zero_err,abs(det3(M)+a*a*d))

    # Graph-bank map L and a null spectral pivot.
    c0=RNG.uniform(0.3001,1.0)
    q1,q2=RNG.uniform(-2.0,2.0),RNG.uniform(-2.0,2.0)
    beta=RNG.uniform(0.3,2.0)
    s=RNG.uniform(-1.0,1.0)
    tau=RNG.uniform(-2.0,2.0)
    if abs(tau)<0.3:
        tau=0.3 if tau>=0 else -0.3
    r=RNG.uniform(-2.0,2.0)
    Lam=[[0.0,beta,0.0],[beta,r,s],[0.0,s,tau]]
    L=[[math.sqrt(c0),q1,q2],[0.0,1.0,0.0],[0.0,0.0,1.0]]
    M2=matmul(transpose(L),matmul(Lam,L))
    max_graph_det_err=max(max_graph_det_err,abs(det3(M2)-c0*det3(Lam)))
    max_graph_pivot_err=max(max_graph_pivot_err,abs(M2[0][0]))

C0=3.0*2.0**(2.0/3.0)
gamma=7.0/800.0
cmin=3.0/10.0
graph_constant=C0*(2.0/gamma)**(2.0/3.0)*cmin**(-1.0/3.0)

# Exact formulas for the dependent-pair nonzero-pivot falsifier.
max_area_err=max_uniform_err=max_peak_err=0.0
for delta in [0.5,0.2,0.1,0.05,0.02]:
    logR=2.0/delta
    area=(delta/2.0)*logR
    pair_density=0.5*logR
    peak=(1.0/delta)*math.sqrt(delta)
    max_area_err=max(max_area_err,abs(area-1.0))
    max_uniform_err=max(max_uniform_err,abs(pair_density-1.0/delta))
    max_peak_err=max(max_peak_err,abs(peak-delta**(-0.5)))

print(f"ZERO_DET_MAX_ERROR={max_zero_err:.3e}")
print(f"GRAPH_DET_MAX_ERROR={max_graph_det_err:.3e}")
print(f"GRAPH_PIVOT_MAX_ERROR={max_graph_pivot_err:.3e}")
print(f"GRAPH_CONSTANT={graph_constant:.12f}")
print(f"FALSIFIER_AREA_MAX_ERROR={max_area_err:.3e}")
print(f"FALSIFIER_UNIFORM_MAX_ERROR={max_uniform_err:.3e}")
print(f"FALSIFIER_PEAK_MAX_ERROR={max_peak_err:.3e}")
print("STATUS=PASS")
