import numpy as np
for K in (4,6,8,10):
    N=1<<22
    xi=1.0+(np.arange(N)+0.5)/N
    P=np.ones(N)
    for j in range(K+1):
        P*=np.cos(np.pi*xi*1.5**j)**2
    val=2.0**(K+1)*P.sum()/N
    print(K, "fourier-form = %.6f"%val)
