import math, random

KAPPA = 7.0/800.0
C1 = math.e*math.sqrt(math.pi)/(2.0*math.sqrt(2.0))*math.gamma(0.25)/math.gamma(0.75)
V0 = KAPPA/32.0
BOUND0 = 8.0*C1/KAPPA

def inv2(A):
    a,b=A[0]
    c,d=A[1]
    det=a*d-b*c
    return [[d/det,-b/det],[-c/det,a/det]]

def mv(A,x):
    return [sum(A[i][k]*x[k] for k in range(len(x))) for i in range(len(A))]

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def add2(A,B):
    return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def det3(M):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def spd(rng):
    a=rng.uniform(-2,2); b=rng.uniform(-2,2); c=rng.uniform(-2,2); d=rng.uniform(-2,2)
    return [[a*a+b*b+KAPPA, a*c+b*d],
            [a*c+b*d, c*c+d*d+KAPPA]]

rng=random.Random(130229)
max_parallel_err=0.0
max_det_err=0.0
min_det_margin=float("inf")
for _ in range(5000):
    G1=spd(rng); G2=spd(rng)
    w1=[rng.uniform(-2,2),rng.uniform(-2,2)]
    w2=[rng.uniform(-2,2),rng.uniform(-2,2)]
    rho1=rng.random(); rho2=rng.random()

    h1=mv(G1,w1); h2=mv(G2,w2)
    tau1=dot(w1,h1)+rho1
    tau2=dot(w2,h2)+rho2
    G=add2(G1,G2)
    h=[h1[0]+h2[0],h1[1]+h2[1]]
    tau=tau1+tau2
    rho=tau-dot(h,mv(inv2(G),h))

    P=inv2(add2(inv2(G1),inv2(G2)))
    dw=[w1[0]-w2[0],w1[1]-w2[1]]
    rhs=rho1+rho2+dot(dw,mv(P,dw))
    max_parallel_err=max(max_parallel_err,abs(rho-rhs))

    S=[[tau,h[0],h[1]],[h[0],G[0][0],G[0][1]],[h[1],G[1][0],G[1][1]]]
    detS=det3(S)
    max_det_err=max(max_det_err,abs(detS-det2(G)*rho))
    V=rho1+rho2+(KAPPA/2.0)*dot(dw,dw)
    margin=detS-4.0*KAPPA*KAPPA*V
    min_det_margin=min(min_det_margin,margin)
    if margin < -1e-9:
        raise AssertionError(("det lower bound", margin))

assert abs((4*KAPPA*KAPPA*V0)**(1/3)-KAPPA/2) < 1e-14
assert abs(C1*6400.0/7.0-BOUND0) < 1e-12
print("QFORM_B13_R19_CHECK_PASS")
print("samples=5000")
print("max_parallel_identity_error=%.3e" % max_parallel_err)
print("max_schur_det_identity_error=%.3e" % max_det_err)
print("min_det_lower_bound_margin=%.3e" % min_det_margin)
print("kappa=%.12g" % KAPPA)
print("C1=%.15g" % C1)
print("V0=%.15g" % V0)
print("threshold_bound=%.15g" % BOUND0)
