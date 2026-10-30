import math
import numpy as np

slope=3*2**(1/3)
transverse=3*2**(2/3)
scalar=2**(11/4)*2**(1/4)
partner=3*6**(-1/3)
print('slope_constant',repr(slope))
print('transverse_combined_constant',repr(transverse))
print('scalar_combined_constant',repr(scalar))
print('partner_constant',repr(partner))
assert abs(scalar-8)<1e-12
assert slope<3.78 and transverse<4.763 and partner<1.651

for eps in [0.5,0.1,0.01,1e-4]:
    P=np.array([[0.,0.,eps**-1],[0.,1.,0.],[eps**-1,0.,0.]])
    C=np.array([[1.,0.],[0.,eps],[0.,0.]])
    A=np.block([[P,C],[C.T,np.zeros((2,2))]])
    eig=np.linalg.eigvalsh(A)
    sv=np.linalg.svd(C,compute_uv=False)
    Delta=sv[0]*sv[1]
    a=P@np.array([0.,0.,1.])
    V=Delta**2*np.dot(a,a)
    formula=np.sort(np.array([
        -math.sqrt(1+eps**-2),
        (1-math.sqrt(1+4*eps**2))/2,
        0.,
        (1+math.sqrt(1+4*eps**2))/2,
        math.sqrt(1+eps**-2),
    ]))
    err=np.max(np.abs(eig-formula))
    print('eps',eps,'V',repr(V),'eig_formula_err',repr(err),'third_abs_count',int(np.sum(np.abs(eig)>=1-1e-12)))
    assert abs(V-1)<1e-10
    assert err<1e-10
    assert np.sum(np.abs(eig)>=1-1e-12)>=3

K=np.diag([1.,2.,3.])
Apart=np.block([[np.zeros((3,3)),K],[K,np.zeros((3,3))]])
e=np.linalg.eigvalsh(Apart)
print('partner_spectrum',e.tolist(),'detK',np.linalg.det(K))
assert np.max(np.abs(e-np.array([-3.,-2.,-1.,1.,2.,3.])))<1e-12
assert abs(np.linalg.det(K)-6)<1e-12
print('ALL_CHECKS_PASS')
