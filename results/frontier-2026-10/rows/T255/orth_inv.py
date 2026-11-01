import numpy as np
rng=np.random.default_rng(1)
def Sig(L,m,c,k):
    P=np.eye(m)-np.ones((m,m))/m; K=L.T@P@L; dirs=[]
    for i in range(m):
        for j in range(i,m):
            E=np.zeros((m,m)); E[i,j]=E[j,i]=1.0
            s=np.sqrt(2.0) if i==j else 1.0   # GOE: diag var 2, offdiag var 1
            dirs.append(np.sqrt(c)*s*(E if i!=j else E/1.0)/ (1 if i!=j else 1))
    for a in range(m):
        for b in range(m):
            N=np.zeros((m,m)); N[a,b]=1.0; dirs.append(k*(N@K+K@N.T))
    S=np.zeros((m*m,m*m))
    for G in dirs:
        x=(L@G@L.T).ravel(); S+=np.outer(x,x)
    return S
worst=0
for m in (2,3,4,5):
    for _ in range(20):
        A=rng.normal(size=(m,m)); V=A@A.T+0.1*np.eye(m); L=np.linalg.cholesky(V)
        O,_=np.linalg.qr(rng.normal(size=(m,m)))
        S1=Sig(L,m,0.7,0.3); S2=Sig(L@O,m,0.7,0.3)
        worst=max(worst,np.abs(S1-S2).max()/np.abs(S1).max())
print("max rel gap", worst)
