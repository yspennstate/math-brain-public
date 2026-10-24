"""Finite identity checks for X037; the universal proof is in agents/X037.md."""
import itertools,json,pathlib
import sympy as S
import numpy as np
out=pathlib.Path(__file__).with_name('results.json')
r,s,T=S.symbols('r s T', positive=True)
A=4*(1-s)/(1-r)+16*s*s/(1-r*s)+T*(1-s)/r
D=4*(1-r)/(1-s)+16*r*r/(1-r*s)+T*(1-r)/s
B=4+16*r*s/(1-r*s)-2*T
D0=64*(r-s)**2/((1-r)*(1-s)*(1-r*s))
L=4*(1/r+1/s+2)+16*(r+s+2*r*s)/(1-r*s)
assert S.factor(A*D-B*B-D0-L*T-T*T*((1-r)*(1-s)/(r*s)-4))==0
q=(r-s)**2/((1-r*r)*(1-s*s))
assert S.factor(D0-64*q*(1+r)*(1+s)/(1-r*s))==0
assert S.factor((1-r*s)**2/((1-r*r)*(1-s*s))-(1+q))==0

R=S.Rational; ii=S.I
U=S.Matrix([[R(3,5),R(4,5)],[-R(4,5),R(3,5)]])
V=S.Matrix([[R(5,13),12*ii/13],[12*ii/13,R(5,13)]])
aa=R(9999,10000);bb=R(3,5)
assert U*U.H==S.eye(2) and V*V.H==S.eye(2)
C=U*S.diag(aa,bb)*V
loop=S.simplify(C[0,0]*C[1,1]*S.conjugate(C[0,1]*C[1,0]))
assert S.im(loop)!=0
E=S.Matrix([[R(1,9)+ii/7,R(1,11)-2*ii/13],[-R(2,17)+ii/19,R(3,23)+ii/29]])
K=S.eye(4)/2
K[:2,2:]=C/2;K[2:,:2]=C.H/2
AH=S.zeros(4);AH[:2,2:]=E/2;AH[2:,:2]=E.H/2
pjets={};count=[[S.Integer(0)]*3 for _ in range(5)]
for bits in itertools.product([0,1],repeat=4):
 M=K-S.diag(*[1-b for b in bits]);inv=M.inv();W=inv*AH
 p=S.simplify((-1)**(4-sum(bits))*M.det())
 p1=S.simplify(p*S.trace(W));p2=S.simplify(p*(S.trace(W)**2-S.trace(W*W)))
 assert p>0 and S.im(p1)==0 and S.im(p2)==0
 pjets[bits]=(p,p1,p2)
 for j,value in enumerate((p,p1,p2)):count[sum(bits)][j]+=value
assert [S.simplify(sum(count[k][j] for k in range(5))) for j in range(3)]==[1,0,0]

u=S.symbols('u',real=True)
Ct=C+u*E
norm2=S.expand(S.trace(Ct.H*Ct))
det2=S.expand(Ct.det()*S.conjugate(Ct.det()))
pc=(1-norm2+det2)/16;mc=(1-det2)/4
for k,poly in [(0,pc),(4,pc),(1,mc),(3,mc),(2,1-2*pc-2*mc)]:
 for j in range(3):assert S.simplify(count[k][j]-S.diff(poly,u,j).subs(u,0))==0

# Exact spin-density jets, including the determinant acceleration.
w=[S.expand(Ct[i,j]*S.conjugate(Ct[i,j])) for i,j in [(0,0),(0,1),(1,0),(1,1)]]
for bits,jet in pjets.items():
 spin=[2*b-1 for b in bits];eta=np.prod(spin).item();tu=-spin[0]*spin[2];tv=-spin[0]*spin[3]
 atom=(1+eta*det2+(w[0]+eta*w[3])*tu+(w[1]+eta*w[2])*tv)/16
 for j in range(3):assert S.simplify(jet[j]-S.diff(atom,u,j).subs(u,0))==0

rh=aa*aa;sh=bb*bb;dh=rh*sh
w0=[S.simplify(v.subs(u,0)) for v in w]
a,b,c,e=w0;x=a+e-b-c;y=a+b-c-e;z=a+c-b-e
Pm=((1-dh)**2-y*y)*((1-dh)**2-z*z)
Pp=((1+dh)**2-(rh+sh)**2)*((1+dh)**2-x*x)
Rtau=S.factor(Pm/Pp)
exp_upper=S.factor((1-dh)**2/((1-rh*rh)*(1-sh*sh)))
assert Rtau>0 and Rtau<=exp_upper
assert S.simplify(y*y+4*dh-x*x-4*abs(C[0,0]*S.conjugate(C[0,1])-C[1,0]*S.conjugate(C[1,1]))**2)==0
assert S.simplify(z*z+4*dh-x*x-4*abs(C[0,0]*S.conjugate(C[1,0])-C[0,1]*S.conjugate(C[1,1]))**2)==0
assert Rtau>64 # e^4 < (11/4)^4 < 64, so tau > 8.
eta=2*rh/(1+rh)+2*sh/(1+sh);p=count[0][0]
assert eta>R(3,2) and 1-2*p>R(3,4) # X026's old certificate fails.

Eh=U.H*E*V.H;h=S.re(Eh[0,0]);k=S.re(Eh[1,1])
Pr=(-(1-sh)*h*h-(1-rh)*k*k+4*aa*bb*h*k)/8
N=((1-sh)*S.im(Eh[0,0])**2+(1-rh)*S.im(Eh[1,1])**2+abs(Eh[0,1])**2+abs(Eh[1,0])**2+2*aa*bb*S.re(Eh[0,1]*Eh[1,0]))/8
assert S.simplify(count[0][2]-Pr+N)==0

# Independently evaluate the full zero-diagonal Hessian from mixed determinants.
Kn=np.array(K,dtype=complex);En=[]
for i in range(4):
 for j in range(i+1,4):
  for value in [1,1j]:
   F=np.zeros((4,4),complex);F[i,j]=value;F[j,i]=np.conjugate(value);En.append(F)
Hess=np.zeros((12,12));Fisher=np.zeros_like(Hess)
for bits,(ps,_,_) in pjets.items():
 Mn=Kn-np.diag(1-np.array(bits));Qn=np.linalg.inv(Mn);Wn=np.array([Qn@F for F in En]);tr=np.trace(Wn,axis1=1,axis2=2).real
 pn=float(ps);pg=pn*tr;ph=pn*(np.outer(tr,tr)-np.einsum('aij,bji->ab',Wn,Wn).real)
 Fisher+=np.outer(pg,pg)/pn;Hess-=np.outer(pg,pg)/pn+np.log(pn)*ph

results={'status':'PASS','exact_checks':['two-dimensional determinant polynomial','spectral-log ratio identity','unitary spectral feasibility','all 16 atom first and second jets','all five count first and second jets','spin-atom first and second jets','two modulus-square cancellations','rational spectral tau upper bound','witness outside X026 certificate','full determinant residual identity'],
'witness':{'C':str(C),'cycle_product':str(loop),'r':str(rh),'s':str(sh),'tau':float(2*S.log(Rtau)),'tau_upper':float(2*S.log(exp_upper)),'eta':float(eta),'old_X026_left_ratio':float(S.log(Rtau)*(1-1/eta)*(1-2*p)),'largest_12d_entropy_hessian_eigenvalue':float(np.linalg.eigvalsh(Hess)[-1]),'numerics_role':'corroboration only; theorem proved analytically'},'exp_tau_half':str(Rtau)}
out.write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
