import itertools, math, numpy as np

rng=np.random.default_rng(20260923)

def proj_span(cols, dim):
    M=np.column_stack(cols)
    U,s,_=np.linalg.svd(M, full_matrices=False)
    rank=np.sum(s>1e-10)
    if rank==0:
        return np.zeros((dim,dim))
    U=U[:,:rank]
    return U@U.T

def perp_vec(v):
    vv=float(v@v)
    return np.eye(len(v)) if vv<1e-14 else np.eye(len(v))-np.outer(v,v)/vv

def wedge2(x,y):
    return math.sqrt(max(float((x@x)*(y@y)-(x@y)**2),0.0))

def E3(M):
    lam=np.linalg.svd(M,compute_uv=False)**2
    return sum(float(np.prod(c)) for c in itertools.combinations(lam,3))

count=0
max_wedge_scaled_error=0.0
max_schur_projection_error=0.0
min_E3_minus_bound_U=float('inf')
min_E3_minus_bound_V=float('inf')

for _ in range(2000):
    m=int(rng.integers(2,7)); n=int(rng.integers(2,7))
    d,e,a=rng.normal(size=3)
    delta=d*e-a*a
    if abs(delta)<0.05:
        continue
    u,c=rng.normal(size=(2,m)); r,v=rng.normal(size=(2,n))
    N=rng.normal(size=(m,n))
    P=np.array([[d,a],[a,e]])
    T=N-np.column_stack([u,c])@np.linalg.inv(P)@np.vstack([r,v])
    xi=a*u-d*c; eta=a*v-e*r
    chi=a*c-e*u; zeta=a*r-d*v

    max_wedge_scaled_error=max(
        max_wedge_scaled_error,
        abs(wedge2(xi,chi)-abs(delta)*wedge2(u,c))/(1+abs(delta)*wedge2(u,c)),
        abs(wedge2(eta,zeta)-abs(delta)*wedge2(r,v))/(1+abs(delta)*wedge2(r,v)))

    PU=proj_span([u,c],m); PV=proj_span([r,v],n)
    PUc=np.eye(m)-PU; PVc=np.eye(n)-PV
    max_schur_projection_error=max(
        max_schur_projection_error,
        float(np.linalg.norm(PUc@(T-N))),
        float(np.linalg.norm((T-N)@PVc)))

    Pxi=perp_vec(xi); Peta=perp_vec(eta)
    qU=Pxi@chi; qV=Peta@zeta
    FU=float(np.linalg.norm(PUc@T@Peta,'fro'))
    FV=float(np.linalg.norm(Pxi@T@PVc,'fro'))
    MU=np.column_stack([u,c,N]); MV=np.vstack([r,v,N])
    boundU=float((xi@xi)*(qU@qU)/(delta*delta)*FU*FU)
    boundV=float((eta@eta)*(qV@qV)/(delta*delta)*FV*FV)
    slackU=E3(MU)-boundU; slackV=E3(MV)-boundV
    min_E3_minus_bound_U=min(min_E3_minus_bound_U,slackU)
    min_E3_minus_bound_V=min(min_E3_minus_bound_V,slackV)
    if slackU < -1e-8 or slackV < -1e-8:
        raise AssertionError((slackU,slackV))
    count+=1

print('instances',count)
print('max_wedge_scaled_error',max_wedge_scaled_error)
print('max_schur_projection_error',max_schur_projection_error)
print('min_E3_minus_bound_U',min_E3_minus_bound_U)
print('min_E3_minus_bound_V',min_E3_minus_bound_V)
print('C_q43',9*math.sqrt(3)*math.e/2)
print('C_q43_theta_half',9*math.sqrt(3)*math.e/2*48**(1/6))
print('C_partner_hybrid',5*math.exp(0.9)*3**(11/20)*2**(-1/30))
print('STATUS PASS')
