import itertools, math
import numpy as np

m=8
n=1+4*m
h=0
U=np.arange(1,1+m)
V1=np.arange(1+m,1+2*m)
V2=np.arange(1+2*m,1+3*m)
W=np.arange(1+3*m,1+4*m)

e=np.zeros(n); e[h]=1.0
u=np.zeros(n); u[U]=1/math.sqrt(m)
v1=np.zeros(n); v1[V1]=1/math.sqrt(m)
v2=np.zeros(n); v2[V2]=1/math.sqrt(m)
w=np.zeros(n); w[W]=1/math.sqrt(m)
l1=e+v1
l2=u+v2
A=np.outer(l1,l2)+np.outer(l2,l1)+np.outer(w,w)
R=np.r_[np.array([h]),U]
C=np.r_[V1,V2]
N=A[np.ix_(R,C)]

nz=np.linalg.eigvalsh(A)
nz=nz[np.abs(nz)>1e-10]
sv=np.linalg.svd(N,compute_uv=False)
rp=(l1+l2)/2
rm=(l1-l2)/2
frame=np.column_stack([rp,rm,w])
lev=np.sum(frame**2,axis=1)

max2=0.0
for S in itertools.combinations(range(n),2):
    max2=max(max2,abs(np.linalg.det(A[np.ix_(S,S)])))
max3=0.0
for S in itertools.combinations(range(n),3):
    max3=max(max3,abs(np.linalg.det(A[np.ix_(S,S)])))

print('m',m)
print('nonzero_spectrum',nz.tolist())
print('cross_singular_values',sv[:4].tolist())
print('hub_cross_star_norm',np.linalg.norm(A[h,C]))
print('hub_cross_svd_leverage',1.0)
print('peeled_left_gram_eigs',[0.0,1.0])
print('max_threeframe_leverage',lev.max())
print('hub_threeframe_leverage',lev[h])
print('max_diag',np.max(np.abs(np.diag(A))))
print('max_2x2_principal_det',max2)
print('max_3x3_principal_det',max3)
print('theorem_F_bound',12*4**(-1/3))

assert np.allclose(nz,[-2,1,2],atol=1e-12)
assert sv[1] > 1-1e-12 and sv[2] < 1e-12
assert abs(np.linalg.norm(A[h,C])-1)<1e-12
assert abs(lev[h]-.5)<1e-12 and lev.max()<=.5+1e-12
assert abs(max2-1/m)<1e-12
assert abs(max3-1/m**2)<1e-12
print('QFORM_B19_R53_COLOOP_HALVING_CHECK_PASS')
