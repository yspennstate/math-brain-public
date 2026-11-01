from fractions import Fraction
import itertools, math
import numpy as np
import sympy as sp

e = sp.symbols('e', positive=True)
k=9
N=-10*(2*sp.eye(k)+sp.ones(k,k))
for a,b in [(2,6),(3,6),(4,7),(5,7)]:
    N[a,b] += -10*e
    N[b,a] += -10*e
pairs=list(itertools.combinations(range(k),2))
D2=0
for R in pairs:
    for T in pairs:
        if set(R).isdisjoint(T):
            D2 += sp.det(N.extract(R,T))**2
assert sp.factor(D2)==160000*e**2*(e**2+4*e+20)

c=Fraction(199,200)
ef=Fraction(1,16)
Z3=8*c*c*ef**4
assert Z3==Fraction(39601,327680000)
s2Z=4*c*c*ef**4
assert s2Z==Fraction(39601,655360000)
D2f=160000*ef**2*(ef**2+4*ef+20)
assert D2f==Fraction(3240625,256)

# build the full target matrix at e=1/16 and audit spectrum
B=np.array([[3.,1.],[1.,-3.]])
v=np.array([.1,.2])
C=np.ones((9,1))@v.reshape(1,2)
S=2*np.eye(9)+np.ones((9,9))
D0=S+C@np.linalg.inv(B)@C.T
E=np.zeros((9,9))
for a,b in [(2,6),(3,6),(4,7),(5,7)]: E[a,b]=E[b,a]=1/16
A=np.block([[B,C.T],[C,D0+E]])
lam=np.linalg.eigvalsh(A)
assert np.min(np.abs(lam))>1

# natural 6x3 crossing and ridge gate
c0=199/200; ee=1/16
u=np.array([c0,c0,c0])
M=np.vstack([u,u,u+[ee,0,0],u+[ee,0,0],u+[0,ee,0],u+[0,ee,0]])
assert np.linalg.matrix_rank(M)==3
assert abs(np.linalg.det(M.T@M)-float(Z3))<1e-15
g=ee**8
K=M@np.linalg.inv(M.T@M+g*np.eye(3))@M.T
theta=float(np.trace(K)); mx=float(np.diag(K).max())
assert mx<.5 and theta>2
sgn,logD=np.linalg.slogdet(np.eye(3)+(M.T@M)/g)
Br=math.e/(math.sqrt(2)*math.sqrt(g))*theta/(theta-2)*math.exp(-logD/(2*theta))
BD=6*math.sqrt(math.e)*float(Z3)**(-1/6)
CPF=3*2**(7/6)*math.e**(1/3)
B55=CPF*float(s2Z)**(-1/6)
B52=8*2**(7/12)*(1+math.pi)*float(D2f)**(-1/12)
BA=3*math.sqrt(math.pi)
assert BA < B52 < Br < BD < B55
print('D2=',sp.factor(D2))
print('Z3=',Z3,float(Z3))
print('s2Z=',s2Z,float(s2Z))
print('D2(e=1/16)=',D2f,float(D2f))
print('eig=',[float(x) for x in lam])
print('theta=',theta,'maxlev=',mx,'ridge=',Br)
print('A=',BA,'r52=',B52,'D=',BD,'r55=',B55)
print('QFORM_B04_R22_COHERENT_TETRAD_COLLAR_CHECK_PASS')
