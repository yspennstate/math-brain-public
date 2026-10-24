import math
import numpy as np
from math import comb, factorial
from scipy.optimize import root
from scipy.special import logsumexp

GAMMA=4.4898
M=23

def qeq(q):
    return q-(1.0-math.exp(-1.5*GAMMA*q*q))
lo,hi=.9,1.0
for _ in range(200):
    mid=(lo+hi)/2
    if qeq(lo)*qeq(mid)<=0: hi=mid
    else: lo=mid
q=(lo+hi)/2
a=1.5*GAMMA*q*q

def delta_b(i,j):
    if i<j or j<1: return 0.0
    return math.exp(-2*a+(i+j)*math.log(a)-math.lgamma(i+1)-math.lgamma(j+1))*(2.0 if i>j else 1.0)

lambda_p=lambda_n=0.0
for i in range(1,100):
    for j in range(1,i+1):
        dd=delta_b(i,j); lambda_p+=i*dd; lambda_n+=j*dd
gamma_b=(lambda_p+lambda_n)/3.0
light=[]; light_p=light_n=0.0
for i in range(1,M+1):
    for j in range(1,i+1):
        dd=delta_b(i,j); light.append((i,j,dd)); light_p+=i*dd; light_n+=j*dd
h_ps=lambda_p-light_p; h_ns=lambda_n-light_n
gamma_k=[comb(3,k)*lambda_p**k*lambda_n**(3-k)/(lambda_p+lambda_n)**3*gamma_b for k in range(4)]

def clause_states(K):
    out=[]
    for ps in range(4):
        for ns in range(4-ps):
            for pu in range(4-ps-ns):
                nu=3-ps-ns-pu
                if ps+ns<1 or ps+pu!=K: continue
                ns1=ns if ps+ns==1 else 0
                ns2=0 if ps+ns==1 else ns
                zeros=sum(int(z==0) for z in (ps,ns,pu,nu))
                out.append((ps,ns1,ns2,2.0/factorial(zeros)))
    return out
CSTATES=[clause_states(k) for k in range(4)]
assert sum(map(len,CSTATES))==16

def variable_A_mean_cov(theta):
    t=np.asarray(theta,float)
    A=h_ps*t[0]+h_ns*logsumexp(t[1:])
    pn=np.exp(t[1:]-logsumexp(t[1:]))
    mean=np.array([h_ps,h_ns*pn[0],h_ns*pn[1]])
    cov=np.zeros((3,3)); ss=pn[0]*pn[1]
    cov[1,1]+=h_ns*ss; cov[2,2]+=h_ns*ss; cov[1,2]-=h_ns*ss; cov[2,1]-=h_ns*ss
    for i,j,dd in light:
        states=[np.array([float(i),0.,0.])]; logw=[i*t[0]]
        for k in range(1,j+1):
            states.append(np.array([0.,float(k),float(j-k)]))
            logw.append(math.log(comb(j,k))+k*t[1]+(j-k)*t[2])
        lz=logsumexp(logw); A+=dd*lz
        p=np.exp(np.asarray(logw)-lz); Y=np.stack(states); mm=(p[:,None]*Y).sum(0)
        mean+=dd*mm
        cov+=dd*(p[:,None,None]*(Y-mm)[:,:,None]*(Y-mm)[:,None,:]).sum(0)
    return A,mean,cov

def clause_A_mean_cov(theta):
    t=np.asarray(theta,float); A=0.0; mean=np.zeros(3); cov=np.zeros((3,3))
    for K in range(4):
        states=[]; logw=[]
        for ps,n1,n2,base in CSTATES[K]:
            states.append(np.array([float(ps),float(n1),float(n2)]))
            logw.append(math.log(base)+ps*t[0]+n1*t[1]+n2*t[2])
        lz=logsumexp(logw); A+=gamma_k[K]*lz
        p=np.exp(np.asarray(logw)-lz); Y=np.stack(states); mm=(p[:,None]*Y).sum(0)
        mean+=gamma_k[K]*mm
        cov+=gamma_k[K]*(p[:,None,None]*(Y-mm)[:,:,None]*(Y-mm)[:,None,:]).sum(0)
    return A,mean,cov

def copy_y(nu,mu):
    nps,n1,n2=nu; mps,m1,m2=mu
    return np.array([lambda_p*nps*mps/(1+nps*mps),
                     lambda_n*n1*m1/(1+n1*m1+n2*m2),
                     lambda_n*n2*m2/(1+n1*m1+n2*m2)])

def stationarity(logx):
    z=np.exp(logx); y=copy_y(z[:3],z[3:])
    return np.r_[variable_A_mean_cov(logx[:3])[1]-y, clause_A_mean_cov(logx[3:])[1]-y]

x0=np.log([1.2782018,0.33277280,0.95336927,1.9972796,0.45029358,0.33794030])
sol=root(stationarity,x0,method='hybr',tol=1e-12)
assert sol.success and np.linalg.norm(stationarity(sol.x),np.inf)<1e-10
z=np.exp(sol.x); tv0=sol.x[:3]; tc0=sol.x[3:]; y0=copy_y(z[:3],z[3:])

def solve_mean(fun,y,guess):
    rr=root(lambda th:fun(th)[1]-y,guess,method='hybr',tol=1e-12)
    assert rr.success and np.linalg.norm(fun(rr.x)[1]-y,np.inf)<1e-9
    return rr.x

def Kfun(y):
    u,v,w=y; rem=lambda_n-v-w
    assert min(u,lambda_p-u,v,w,rem)>0
    return u*math.log(u)+(lambda_p-u)*math.log(lambda_p-u)+v*math.log(v)+w*math.log(w)+rem*math.log(rem)

def Hcopy(y):
    u,v,w=y; rem=lambda_n-v-w
    return np.array([[1/u+1/(lambda_p-u),0,0],[0,1/v+1/rem,1/rem],[0,1/rem,1/w+1/rem]])

def eval_y(y,gV,gC):
    tv=solve_mean(variable_A_mean_cov,y,gV); tc=solve_mean(clause_A_mean_cov,y,gC)
    AV,mV,SV=variable_A_mean_cov(tv); AC,mC,SC=clause_A_mean_cov(tc)
    phi=Kfun(y)+AV-tv@y+AC-tc@y
    H=Hcopy(y)-np.linalg.inv(SV)-np.linalg.inv(SC)
    return phi,tv,tc,SV,SC,H

phi0,tv0,tc0,SV0,SC0,H0=eval_y(y0,tv0,tc0)
assert np.max(np.linalg.eigvalsh(H0))<0

# Route A: blockwise Bhatia-Davis at the actual Gibbs mean, then
# (x^T Sigma x)(x^T Sigma^{-1}x) >= ||x||^4.
xdir=np.array([-1.,10.,-6.])
def bd_variable(theta):
    t=np.asarray(theta); B=actual=0.0
    p=np.exp(t[1:]-logsumexp(t[1:])); vals=np.array([xdir[1],xdir[2]]); mm=float(p@vals)
    B+=h_ns*(vals.max()-mm)*(mm-vals.min()); actual+=h_ns*np.sum(p*(vals-mm)**2)
    for i,j,dd in light:
        states=[np.array([float(i),0.,0.])]; logw=[i*t[0]]
        for k in range(1,j+1):
            states.append(np.array([0.,float(k),float(j-k)])); logw.append(math.log(comb(j,k))+k*t[1]+(j-k)*t[2])
        lz=logsumexp(logw); p=np.exp(np.asarray(logw)-lz); Y=np.stack(states); vals=Y@xdir; mm=float(p@vals)
        B+=dd*(vals.max()-mm)*(mm-vals.min()); actual+=dd*np.sum(p*(vals-mm)**2)
    return B,actual

def bd_clause(theta):
    t=np.asarray(theta); B=actual=0.0
    for K in range(4):
        states=[]; logw=[]
        for ps,n1,n2,base in CSTATES[K]:
            states.append(np.array([float(ps),float(n1),float(n2)])); logw.append(math.log(base)+ps*t[0]+n1*t[1]+n2*t[2])
        lz=logsumexp(logw); p=np.exp(np.asarray(logw)-lz); Y=np.stack(states); vals=Y@xdir; mm=float(p@vals)
        B+=gamma_k[K]*(vals.max()-mm)*(mm-vals.min()); actual+=gamma_k[K]*np.sum(p*(vals-mm)**2)
    return B,actual
BV,actV=bd_variable(tv0); BC,actC=bd_clause(tc0)
norm4=float((xdir@xdir)**2)
bd_inverse_lb=norm4/BV+norm4/BC
copy_curvature=float(xdir@Hcopy(y0)@xdir)
actual_inverse=float(xdir@np.linalg.inv(SV0)@xdir+xdir@np.linalg.inv(SC0)@xdir)
assert bd_inverse_lb<copy_curvature<actual_inverse

# Route B/C: explicit ray through a direction where global Hessian concavity fails.
d=np.array([-0.67804166,0.60629724,-0.41552757]); d/=np.linalg.norm(d)
ray=[]; gv=tv0.copy(); gc=tc0.copy()
for tt in [0.,.25,.5,1.,1.5,2.,2.5,2.7]:
    ph,gv,gc,SV,SC,H=eval_y(y0+tt*d,gv,gc)
    ray.append((tt,ph-phi0,float(np.max(np.linalg.eigvalsh(H)))))
lo,hi=.5,1.0
for _ in range(45):
    mid=(lo+hi)/2
    ph,tv,tc,SV,SC,H=eval_y(y0+mid*d,tv0,tc0)
    if np.max(np.linalg.eigvalsh(H))<=0: lo=mid
    else: hi=mid
cross=(lo+hi)/2
phcross,tv,tc,SV,SC,H=eval_y(y0+cross*d,tv0,tc0)

def dual_U(y,tv,tc):
    AV=variable_A_mean_cov(tv)[0]; AC=clause_A_mean_cov(tc)[0]
    return Kfun(y)+AV-tv@y+AC-tc@y

segments=[(.25,.5),(.5,1.),(1.,1.5),(1.5,2.),(2.,2.5),(2.5,2.7)]
segment_certs=[]; gv=tv0.copy(); gc=tc0.copy()
for aa,bb in segments:
    cc=(aa+bb)/2; ph,gv,gc,SV,SC,H=eval_y(y0+cc*d,gv,gc)
    ups=[dual_U(y0+tt*d,gv,gc)-phi0 for tt in (aa,bb)]
    segment_certs.append((aa,bb,max(ups),ups[0],ups[1]))
assert all(row[2]<0 for row in segment_certs)

# A genuine 3D simplex centered where H is already indefinite.  By the theorem
# artifact, negative dual upper values at its four vertices exclude its continuum.
c=y0+d
phc,tvc,tcc,SVc,SCc,Hc=eval_y(c,tv0,tc0)
tetdirs=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)/math.sqrt(3)
r=.15
verts=[c+r*ee for ee in tetdirs]
tet_ups=[dual_U(vv,tvc,tcc)-phi0 for vv in verts]
assert np.max(np.linalg.eigvalsh(Hc))>0 and max(tet_ups)<0

print('PROB10_04_GLOBAL_ANNULUS_DUAL_SIMPLEX_DIAGNOSTIC')
print('NUMERICAL_DIAGNOSTIC_ONLY_NOT_INTERVAL_ENDPOINT')
print('q = %.16g'%q); print('lambda_p = %.16g'%lambda_p); print('lambda_n = %.16g'%lambda_n)
print('y0 =',' '.join('%.16g'%v for v in y0)); print('phi0_tilde = %.16g'%phi0)
print('eig_H0 =',' '.join('%.16g'%v for v in np.linalg.eigvalsh(H0)))
print('BD_DIRECTION = -1 10 -6')
print('BD_variable_upper = %.16g'%BV); print('BD_clause_upper = %.16g'%BC)
print('actual_variable_variance = %.16g'%actV); print('actual_clause_variance = %.16g'%actC)
print('BD_Cauchy_inverse_lower = %.16g'%bd_inverse_lb); print('copy_direction_curvature = %.16g'%copy_curvature)
print('actual_inverse_curvature = %.16g'%actual_inverse)
print('MEAN_DEPENDENT_SCALAR_BD_SHORTCUT_FAILS =',bd_inverse_lb<copy_curvature)
for tt,gap,eig in ray: print('RAY t=%.2f phi_gap=% .16g max_hessian_eig=% .16g'%(tt,gap,eig))
print('HESSIAN_SIGN_CROSS_t = %.16g'%cross); print('HESSIAN_SIGN_CROSS_phi_gap = %.16g'%(phcross-phi0))
for aa,bb,ub,u0,u1 in segment_certs:
    print('SEGMENT [%.2f,%.2f] dual_upper_gap=% .16g endpoints=(% .16g,% .16g)'%(aa,bb,ub,u0,u1))
print('TETRA_center_t = 1.0 radius = %.16g'%r)
print('TETRA_center_max_hessian_eig = %.16g'%np.max(np.linalg.eigvalsh(Hc)))
for i,(vv,up) in enumerate(zip(verts,tet_ups)):
    print('TETRA_VERTEX_%d y=%s dual_upper_gap=% .16g'%(i,' '.join('%.16g'%x for x in vv),up))
print('TETRA_whole_simplex_dual_upper_gap = %.16g'%max(tet_ups))
print('SEGMENT_DUAL_CERTIFICATES_NEGATIVE =',all(row[2]<0 for row in segment_certs))
print('INDEFINITE_TETRA_DUAL_CERTIFICATE_NEGATIVE =',max(tet_ups)<0 and np.max(np.linalg.eigvalsh(Hc))>0)
print('DIAGNOSTIC_CHECKS_PASS = True')
