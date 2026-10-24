import numpy as np
import math

def adj2(G):
    return np.array([[G[1,1], -G[0,1]],[-G[1,0], G[0,0]]], float)

m = 16
th = 2*np.pi*np.arange(m)/m
Z = np.column_stack((np.cos(th), np.sin(th)))/np.sqrt(m)
G = Z.T @ Z
assert np.linalg.norm(G - 0.5*np.eye(2)) < 1e-12
assert np.max(np.sum(Z*Z,axis=1)) <= 1/16 + 1e-12

q = np.array([0.6,-0.4])
raw = np.array([1,-1,2,-2,3,-3,4,-4,5,-5,6,-6,7,-7,8,-8.],float)
e = raw - Z @ np.linalg.solve(G,Z.T@raw)
e *= math.sqrt(0.05)/np.linalg.norm(e)
a = Z@q + e
u = float(a@a)
v = Z.T@a
delta = u - float(v@np.linalg.solve(G,v))
assert abs(delta-0.05) < 1e-12

K = np.block([[np.array([[u]]),v[None,:]],[v[:,None],G]])
c = 0.75
H = K.copy(); H[0,0] += c
assert abs(np.linalg.det(K) - delta*np.linalg.det(G)) < 1e-12
assert abs(np.linalg.det(H) - (c+delta)*np.linalg.det(G)) < 1e-12
h = c*np.linalg.inv(H)[0,0]
assert abs(h-c/(c+delta)) < 1e-12

Ki=np.linalg.inv(K); Gi=np.linalg.inv(G)
errs=[]
for i in range(m):
    r=np.r_[a[i],Z[i]]
    lhs=float(r@Ki@r)
    rhs=e[i]**2/delta + float(Z[i]@Gi@Z[i])
    errs.append(abs(lhs-rhs))
assert max(errs)<1e-11

spikes=np.flatnonzero(e*e>delta/4)
assert len(spikes)<=3
Grem=G-Z[spikes].T@Z[spikes]
assert np.linalg.eigvalsh(Grem).min()>=1/16-1e-12

agraph=Z@q
ug=float(agraph@agraph); vg=Z.T@agraph
Kg=np.block([[np.array([[ug]]),vg[None,:]],[vg[:,None],G]])
Hg=Kg.copy(); Hg[0,0]+=c
assert np.linalg.matrix_rank(Kg,tol=1e-10)==2
assert abs(c*np.linalg.inv(Hg)[0,0]-1.0)<1e-12
assert abs(np.linalg.det(Hg)-c*np.linalg.det(G))<1e-12

for zi in Z:
    assert float(zi@adj2(0.75*np.eye(2))@zi)<=3/64+1e-12

C0=3*(2**(2/3))*math.e**(2/3)
graph_const=C0*(32**(1/3))
assert graph_const<29.448

print('detK_factorization',np.linalg.det(K),delta*np.linalg.det(G))
print('heavy_leverage',h,c/(c+delta))
print('max_leverage_identity_error',max(errs))
print('static_spike_count',len(spikes))
print('graph_endpoint_constant',graph_const)
print('QFORM_BANK_REGRESSION_CHECK_PASS')
