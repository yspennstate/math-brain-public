import math
import numpy as np

h=(2*math.sqrt(2)-1)/1572864
C0=462.4798790835328

def core_coeff(m,theta=0.5):
    return 8*C0*math.sqrt(theta)/(m*math.sqrt(math.comb(m,2))) - ((m-1)/8+h/128)

print('h', format(h,'.17g'))
print('coeff_m31', format(core_coeff(31),'.17g'))
print('coeff_m32', format(core_coeff(32),'.17g'))
sigma=core_coeff(31)*h
cap=2*math.sqrt(6*math.pi*62)/sigma
print('sigma_m31', format(sigma,'.17g'))
print('density_cap_m31', format(cap,'.17g'))

for N in (4,8,16):
    J=np.ones((N,N))/N
    Z=np.zeros((N,N))
    K=np.block([[J,Z],[Z,J]])
    s=np.linalg.svd(K,compute_uv=False)
    omega=(np.linalg.norm(J,'fro')**2)*(np.linalg.norm(J,'fro')**2)
    S=np.block([[np.zeros((2*N,2*N)),K],[K.T,np.zeros((2*N,2*N))]])
    eig=np.linalg.eigvalsh(S)
    nz=eig[np.abs(eig)>1e-9]
    print('N',N,'s',np.round(s[:4],12).tolist(),'omega',round(omega,12),
          'nz',np.round(nz,12).tolist(),'entry',1/N)
print('STATUS=PASS')
