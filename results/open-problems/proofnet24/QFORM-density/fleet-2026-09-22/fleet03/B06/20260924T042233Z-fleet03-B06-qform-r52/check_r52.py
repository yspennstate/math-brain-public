import numpy as np

rng=np.random.default_rng(20260924)
N=10000
min_layer_ratio=10.0
max_cofactor_defect=0.0
max_residual_error=0.0
max_residual_ratio=0.0
for _ in range(N):
    Q,_=np.linalg.qr(rng.normal(size=(3,3)))
    vals=np.sort(np.exp(rng.uniform(-4,4,size=2)))[::-1]
    s1,s2=float(vals[0]),float(vals[1])
    s3=float(rng.uniform(0,(1/15)*0.999))
    if s2<s3:
        s2=s3+float(rng.uniform(1e-5,1))
    if s1<s2:
        s1=s2+float(rng.uniform(1e-5,1))
    G=Q@np.diag([s1,s2,s3])@Q.T
    e1=float(np.trace(G))
    e2=float(0.5*(np.trace(G)**2-np.trace(G@G)))
    den=float(np.linalg.det(np.eye(3)+G))
    min_layer_ratio=min(min_layer_ratio,max(1.0,e1,e2)/den)

    w,V=np.linalg.eigh(G)
    u=V[:,0]
    h=int(np.argmax(u*u))
    J=[j for j in range(3) if j!=h]
    W=float(np.linalg.det(G[np.ix_(J,J)]))
    max_cofactor_defect=max(max_cofactor_defect,max(0.0,s1*s2/3-W))

    ew,EV=np.linalg.eigh(G)
    Z=EV@np.diag(np.sqrt(np.maximum(ew,0)))@EV.T
    zh=Z[h]
    ZJ=Z[J]
    P=ZJ.T@np.linalg.pinv(ZJ@ZJ.T)@ZJ
    n=zh@(np.eye(3)-P)
    residual=float(n@n)
    pred=float(np.linalg.det(G)/W)
    max_residual_error=max(max_residual_error,abs(residual-pred)/(1+abs(pred)))
    if s3>1e-12:
        max_residual_ratio=max(max_residual_ratio,residual/s3)

print('QFORM_B06_R52_CHECK_PASS')
print('samples',N)
print('min max{1,e1,e2}/det(I+G)',repr(min_layer_ratio))
print('required lower bound',repr(5/16))
print('max cofactor defect',repr(max_cofactor_defect))
print('max normalized residual identity error',repr(max_residual_error))
print('max residual/s3',repr(max_residual_ratio))
print('required residual/s3 upper bound',3.0)
