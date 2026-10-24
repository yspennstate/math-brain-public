import math
import itertools
from fractions import Fraction
import numpy as np
from math import comb, factorial
from scipy.optimize import root, linprog
from scipy.special import logsumexp
from scipy.spatial import ConvexHull

# PROB10-04 tangent-bank / arrangement diagnostic.
# Floating part is diagnostic only and is NOT an interval-certified threshold endpoint.
# An exact rational toy check validates the finite arrangement combinatorics separately.

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

def eval_y(y,gV,gC):
    tv=solve_mean(variable_A_mean_cov,y,gV); tc=solve_mean(clause_A_mean_cov,y,gC)
    AV=variable_A_mean_cov(tv)[0]; AC=clause_A_mean_cov(tc)[0]
    phi=Kfun(y)+AV-tv@y+AC-tc@y
    return phi,tv,tc,AV,AC

phi0,tv0,tc0,AV0,AC0=eval_y(y0,tv0,tc0)
d=np.array([-0.67804166,0.60629724,-0.41552757]); d/=np.linalg.norm(d)

# ---------- Exact rational micro-check of arrangement geometry ----------
# R=[0,1], K=x^2, L1=0, L2=1-2x. The lower-envelope cells meet at x=1/2.
# Exact surrogate values at the only required candidates 0,1/2,1 are 0,1/4,0.
rx=[Fraction(0),Fraction(1,2),Fraction(1)]
def toyK(x): return x*x
def toyL1(x): return Fraction(0)
def toyL2(x): return Fraction(1)-2*x
toyvals=[toyK(x)+min(toyL1(x),toyL2(x)) for x in rx]
assert toyvals==[Fraction(0),Fraction(1,4),Fraction(0)]
assert max(toyvals)==Fraction(1,4)

# ---------- Tangent bank on inherited difficult ray ----------
bank_centers=[.25,.5,1.0,1.5,2.0,2.5,2.7]
bank=[]
gv=tv0.copy(); gc=tc0.copy()
for cc in bank_centers:
    ph,gv,gc,AV,AC=eval_y(y0+cc*d,gv,gc)
    # L_j(t)=intercept+slope*t along y0+t d.
    intercept=AV+AC-(gv+gc)@y0
    slope=-(gv+gc)@d
    bank.append((cc,intercept,slope,gv.copy(),gc.copy(),AV,AC,ph))

# Route A: global mixture LP over the two segment endpoints.
za=y0+.25*d; zb=y0+2.7*d
Kends=np.array([Kfun(za),Kfun(zb)])
Tends=np.array([[inter+slope*.25,inter+slope*2.7] for _,inter,slope,*_ in bank])
# primal: max K.lambda + s, s<=T_j.lambda, lambda in Delta_2
cvec=np.array([-Kends[0],-Kends[1],-1.])
A_ub=np.column_stack([-Tends,np.ones(len(bank))])
res=linprog(cvec,A_ub=A_ub,b_ub=np.zeros(len(bank)),
            A_eq=np.array([[1.,1.,0.]]),b_eq=np.array([1.]),
            bounds=[(0,None),(0,None),(None,None)],method='highs')
assert res.success
mixture_gap=-res.fun-phi0
assert mixture_gap>0

# Route B in 1D: exact lower-envelope arrangement candidate list = endpoints +
# active tangent intersections. Testing all pair intersections is conservative and contains all active ones.
pts={.25,2.7}
for i in range(len(bank)):
    for j in range(i+1,len(bank)):
        ai,bi=bank[i][1],bank[i][2]
        aj,bj=bank[j][1],bank[j][2]
        if abs(bi-bj)>1e-14:
            tt=(aj-ai)/(bi-bj)
            if .25<tt<2.7: pts.add(float(tt))
pts=sorted(pts)
ray_candidates=[]
for tt in pts:
    yy=y0+tt*d
    vals=[inter+slope*tt for _,inter,slope,*_ in bank]
    jj=int(np.argmin(vals))
    sg=Kfun(yy)+vals[jj]-phi0
    ray_candidates.append((tt,sg,jj))
ray_max=max(ray_candidates,key=lambda x:x[1])
assert ray_max[1]<0

# Bregman/KL tangent identity at y(t=1.2), tangent center c(t=1.0).
# Use the already computed bank center 1.0 and independently solve at 1.2.
center1=[row for row in bank if abs(row[0]-1.0)<1e-12][0]
_,_,_,tv_c,tc_c,AV_c,AC_c,_=center1
ph_y,tv_y,tc_y,AV_y,AC_y=eval_y(y0+1.2*d,tv_c,tc_c)
y_y=y0+1.2*d
entropy_y=(AV_y-tv_y@y_y)+(AC_y-tc_y@y_y)
tangent_y=(AV_c-tv_c@y_y)+(AC_c-tc_c@y_y)
DV=AV_c-AV_y-variable_A_mean_cov(tv_y)[1]@(tv_c-tv_y)
DC=AC_c-AC_y-clause_A_mean_cov(tc_y)[1]@(tc_c-tc_y)
kl_identity_error=abs((tangent_y-entropy_y)-(DV+DC))
assert DV>=-1e-12 and DC>=-1e-12 and kl_identity_error<1e-10

# ---------- 3D indefinite tetrahedron from preceding run ----------
c=y0+d
tetdirs=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)/math.sqrt(3)
r=.15
verts=[c+r*ee for ee in tetdirs]
# tangent bank = tetra center plus four vertices
tet_bank=[]
gv=tv0.copy(); gc=tc0.copy()
for yy in [c]+verts:
    ph,gv,gc,AV,AC=eval_y(yy,gv,gc)
    tet_bank.append((AV+AC,-(gv+gc).copy(),yy.copy(),ph))
# old one-tangent simplex bound from center tangent
old_center_c,old_center_g,_,_=tet_bank[0]
old_one_tangent_gap=max(Kfun(v)+old_center_c+old_center_g@v-phi0 for v in verts)
assert old_one_tangent_gap<0

# Enumerate every cell extreme point from 3 active hyperplanes.
hull=ConvexHull(np.array(verts))
Areg=hull.equations[:,:3]; breg=hull.equations[:,3]
arr_candidates=[]
for j,(cj,gj,_,_) in enumerate(tet_bank):
    A=[]; b=[]; labels=[]
    for ii in range(len(Areg)):
        A.append(Areg[ii]); b.append(breg[ii]); labels.append(('facet',ii))
    for k,(ck,gk,_,_) in enumerate(tet_bank):
        if k==j: continue
        A.append(gj-gk); b.append(cj-ck); labels.append(('tan',k))
    A=np.asarray(A); b=np.asarray(b)
    for inds in itertools.combinations(range(len(A)),3):
        MM=A[list(inds)]
        if abs(np.linalg.det(MM))<1e-10: continue
        xx=np.linalg.solve(MM,-b[list(inds)])
        if np.max(A@xx+b)<=1e-8:
            val=Kfun(xx)+cj+gj@xx-phi0
            arr_candidates.append((val,j,xx,tuple(labels[ii] for ii in inds)))
assert arr_candidates
arr_max=max(arr_candidates,key=lambda z:z[0])
assert arr_max[0]<0
assert arr_max[0] <= old_one_tangent_gap + 1e-10

print('PROB10_04_TANGENT_ARRANGEMENT_DIAGNOSTIC')
print('FLOATING_DIAGNOSTIC_ONLY_NOT_INTERVAL_THRESHOLD_ENDPOINT')
print('EXACT_TOY_ARRANGEMENT_VALUES =',*[str(x) for x in toyvals])
print('EXACT_TOY_ARRANGEMENT_MAX =',str(max(toyvals)))
print('q = %.16g'%q)
print('lambda_p = %.16g'%lambda_p)
print('lambda_n = %.16g'%lambda_n)
print('y0 =',' '.join('%.16g'%v for v in y0))
print('phi0_tilde = %.16g'%phi0)
print('RAY_BANK_CENTERS =',' '.join('%.2f'%x for x in bank_centers))
print('ROUTE_A_GLOBAL_MIXTURE_LP_GAP = %.16g'%mixture_gap)
print('ROUTE_A_GLOBAL_MIXTURE_FAILS =',mixture_gap>0)
print('RAY_PAIR_INTERSECTION_CANDIDATE_COUNT =',len(pts))
print('ROUTE_B_RAY_ARRANGEMENT_MAX_t = %.16g'%ray_max[0])
print('ROUTE_B_RAY_ARRANGEMENT_MAX_GAP = %.16g'%ray_max[1])
print('ROUTE_B_RAY_ARRANGEMENT_CERTIFIES =',ray_max[1]<0)
print('KL_BREGMAN_DV = %.16g'%DV)
print('KL_BREGMAN_DC = %.16g'%DC)
print('KL_BREGMAN_IDENTITY_ERROR = %.16g'%kl_identity_error)
print('KL_BREGMAN_IDENTITY_CHECK =',kl_identity_error<1e-10 and DV>=-1e-12 and DC>=-1e-12)
print('TETRA_OLD_ONE_TANGENT_GAP = %.16g'%old_one_tangent_gap)
print('TETRA_ARRANGEMENT_FEASIBLE_CANDIDATES =',len(arr_candidates))
print('TETRA_ARRANGEMENT_MAX_GAP = %.16g'%arr_max[0])
print('TETRA_ARRANGEMENT_MAX_CELL =',arr_max[1])
print('TETRA_ARRANGEMENT_MAX_POINT =',' '.join('%.16g'%v for v in arr_max[2]))
print('TETRA_ARRANGEMENT_CERTIFIES =',arr_max[0]<0)
print('TETRA_ARRANGEMENT_IMPROVEMENT = %.16g'%(old_one_tangent_gap-arr_max[0]))
print('ALL_TANGENT_ARRANGEMENT_DIAGNOSTIC_CHECKS_PASS = True')
