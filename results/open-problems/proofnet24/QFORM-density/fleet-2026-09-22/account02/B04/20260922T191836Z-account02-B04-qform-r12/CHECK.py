import numpy as np
p=11/4
H=.5*np.array([[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]],float)
B=H@np.diag([6/5,3/5,1/20,1/50])@H.T
C=H@np.diag([1/10,-1/12,1/20,-1/25])@H.T
A=np.zeros((9,9)); A[0,0]=1; A[1:5,1:5]=C; A[1:5,5:9]=B; A[5:9,1:5]=B
cp=lambda r: 2*r*((r-1)/(r-2))**((r-1)/r)
print('B=',B)
print('C=',C)
print('eig(A)=',np.linalg.eigvalsh(A))
print('opnorm(B)=',np.linalg.svd(B,compute_uv=False)[0])
print('Cp(11/4)=',cp(p))
print('bound(11/4)=',cp(p)*(6/5)**(-(p-1)/p))
print('Cp(3)=',cp(3.0))
print('bound(3)=',cp(3.0)*(6/5)**(-2/3))
