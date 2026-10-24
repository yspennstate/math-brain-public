import itertools
import math

zs=[-0.4,0.1,0.6,0.9]
aa=[0.7,1.2,0.5,0.8]
q0=(1.0,0.0,1.0)
t0=(0.0,1.0,0.0)
qpi=(-1.0,0.0,1.0)

def det3(M):
    (a,b,c),(d,e,f),(g,h,i)=M
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def row(z,a):
    return tuple(a*(q0[j]+2*z*t0[j]+z*z*qpi[j]) for j in range(3))

rows=[row(z,a) for z,a in zip(zs,aa)]
H=[[sum(u[i]*u[j] for u in rows) for j in range(3)] for i in range(3)]
direct=det3(H)
W=sum(a*a for a in aa)
p=[a*a/W for a in aa]
Ez=sum(w*z for w,z in zip(p,zs))
Ez2=sum(w*z*z for w,z in zip(p,zs))
Ez3=sum(w*z**3 for w,z in zip(p,zs))
var=Ez2-Ez*Ez
beta=(Ez3-Ez*Ez2)/var
alpha=Ez2-beta*Ez
res=sum(w*(z*z-alpha-beta*z)**2 for w,z in zip(p,zs))
reg=16*W**3*var*res
vand=0.0
for i,j,k in itertools.combinations(range(len(zs)),3):
    V=(zs[j]-zs[i])*(zs[k]-zs[i])*(zs[k]-zs[j])
    vand += 16*(aa[i]*aa[j]*aa[k])**2*V**2

tol=1e-11
assert abs(direct-reg)<tol
assert abs(direct-vand)<tol
partner_eta_bound=8*math.sqrt(2*math.pi)
assert partner_eta_bound<20.054
print(f"direct_det={direct:.15f}")
print(f"regression_rhs={reg:.15f}")
print(f"vandermonde_rhs={vand:.15f}")
print(f"var={var:.15f} residual={res:.15f}")
print(f"partner_eta_1_16_bound={partner_eta_bound:.15f}")
print("QFORM_B11_NULL_ARC_MOMENT_GRAM_CHECK_PASS")
