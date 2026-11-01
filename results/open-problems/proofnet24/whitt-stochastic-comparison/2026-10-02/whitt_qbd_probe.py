import numpy as np

def model(lam,p,ms,ml):
    D=np.zeros((3,3)); M=np.zeros(3)
    for i in range(3):
        M[i]=lam+i*ms+(2-i)*ml
        D[i,i]+=i*ms*p+(2-i)*ml*(1-p)
        if i: D[i,i-1]+=i*ms*(1-p)
        if i<2:D[i,i+1]+=(2-i)*ml*p
    R=np.zeros((3,3))
    for k in range(10000):
        S=(lam*np.eye(3)+R@R@D)/M
        if np.max(abs(S-R))<1e-16:break
        R=S
    H=np.zeros((6,6))
    H[0,0]=-lam;H[0,1]=lam*p;H[0,2]=lam*(1-p)
    H[1,0]=ms;H[1,1]=-(lam+ms);H[1,5]=lam*p;H[1,4]=lam*(1-p)
    H[2,0]=ml;H[2,2]=-(lam+ml);H[2,4]=lam*p;H[2,3]=lam*(1-p)
    H[3:,3:]=-np.diag(M)+R@D
    H[3,2]=2*ml;H[4,1]=ml;H[4,2]=ms;H[5,1]=2*ms
    x=np.linalg.solve(-H[1:,1:].T,H[0,1:])
    assert min(x)>0
    print('empty-residual',H[0,0]+x@H[1:,0])
    busy=x[2:]@np.linalg.solve(np.eye(3)-R,np.ones(3))
    idle=1+x[:2].sum()
    print('Pdelay',busy/(busy+idle),'x',x,'R',R)
    J=np.zeros((9,9))
    for j in range(9):
        E=np.zeros((3,3));E.flat[j]=1
        J[:,j]=((R@E+E@R)@D/M).ravel()
    d=np.linalg.solve(np.eye(9)-J,np.ones(9)).reshape(3,3)
    return R,d

if __name__=='__main__':
    for args in [(1.1,3/7,5,5/8),(1.1*11/14,3/11,2.5,5/8)]:
        R,d=model(*args)
        print('CENTER',[[round(float(v)*10**12) for v in row]for row in R])
        print('DIRECTION',[[round(float(v)*1000)for v in row]for row in d])
