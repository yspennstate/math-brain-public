from fractions import Fraction as F
from itertools import product

# PROB10-10: retitled ten-local self-avoidance dual certificate.
# Floating arithmetic proposes the positive Collatz vector only.
# Every promoted inequality is rechecked with exact Fraction arithmetic.

dirs=((1,0),(-1,0),(0,1),(0,-1))
A=F(247,125)             # 1.976
B=F(2767,1000)           # 2.767
r=F(24934561,5000000)    # 4.9869122
a9=F(13247968739227,22500000000000)
pbar=F(631541,1000000)

# Closed cone and lower-tail parameters.
rho0=F(8187,5000)        # 1.6374
c=a9+F(1,125000)         # strict lower-tail level above axis cap
eps=F(3,100000)
s=r-1+eps
q=r/(1+s)
beta_hat=F(99997,100000)
w=(A,1/A,B,1/B)
wf=tuple(float(x) for x in w)

# Ten-step locally self-avoiding states.
states=[]
for word in product(range(4), repeat=10):
    x=y=0
    seen={(0,0)}
    ok=True
    for d in word:
        dx,dy=dirs[d]
        x+=dx; y+=dy
        if (x,y) in seen:
            ok=False
            break
        seen.add((x,y))
    if ok:
        states.append(word)

idx={word:i for i,word in enumerate(states)}
trans=[[] for _ in states]
for i,word in enumerate(states):
    for d in range(4):
        nw=word[1:]+(d,)
        j=idx.get(nw)
        if j is not None:
            trans[i].append((j,d))

assert len(states)==44100
assert sum(len(ls) for ls in trans)==120292
assert sum(1 for ls in trans if not ls)==200

# Deterministic floating proposal for a positive Collatz vector.
zfloat=[1.0]*len(states)
tiny=1e-14
for _ in range(100):
    nz=[sum(wf[d]*zfloat[j] for j,d in ls) for ls in trans]
    mx=max(nz)
    floor=tiny*mx
    nz=[v if v>=floor else floor for v in nz]
    mn=min(nz)
    zfloat=[v/mn for v in nz]
z=[max(1,int(round(v))) for v in zfloat]
assert min(z)>=1

# Authoritative exact transfer verification.
max_ratio=F(0)
max_i=-1
for i,ls in enumerate(trans):
    lhs=sum((w[d]*z[j] for j,d in ls),F(0))
    ratio_i=lhs/F(z[i])
    if ratio_i>max_ratio:
        max_ratio=ratio_i
        max_i=i
assert max_ratio < r

# All-length prefactor L_m <= K r^m.
sumaz=F(0)
for word,zi in zip(states,z):
    ww=F(1)
    for d in word:
        ww*=w[d]
    sumaz += ww*zi
K10=sumaz/(r**10)

def saw_weight_sum(m):
    total=F(0)
    def rec(x,y,seen,depth,ww):
        nonlocal total
        if depth==m:
            total += ww
            return
        for d,(dx,dy) in enumerate(dirs):
            nx,ny=x+dx,y+dy
            if (nx,ny) in seen:
                continue
            seen.add((nx,ny))
            rec(nx,ny,seen,depth+1,ww*w[d])
            seen.remove((nx,ny))
    rec(0,0,{(0,0)},0,F(1))
    return total

startup=[]
for m in range(1,10):
    W=saw_weight_sum(m)
    startup.append((m,W/(r**m)))
K=max([K10]+[v for _,v in startup])
assert K==K10
C=K/(1-q)

# Rigorous logarithm bounds for x>1.
# log x = 2 sum z^(2k+1)/(2k+1), z=(x-1)/(x+1).
def log_bounds_gt1(x,N):
    assert x>1
    z0=(x-1)/(x+1)
    L=F(0)
    for k in range(N+1):
        L += F(2)*z0**(2*k+1)/F(2*k+1)
    tail=F(2)*z0**(2*N+3)/(F(2*N+3)*(1-z0*z0))
    return L,L+tail

LA_L,LA_U=log_bounds_gt1(A,18)
LB_L,LB_U=log_bounds_gt1(B,18)
LQ_L,LQ_U=log_bounds_gt1(1/q,3)

# Critical slope rho*=(((r-1)a9)-log A)/log B.
num_L=(r-1)*a9-LA_U
num_U=(r-1)*a9-LA_L
rho_star_L=num_L/LB_U
rho_star_U=num_U/LB_L
assert rho_star_L>0
assert rho_star_L < rho_star_U < rho0

# Closed-cone lower-tail sign.
# log beta = sc - log A - rho log B - (1+rho)log(1/q).
logbeta_upper=s*c-LA_L-rho0*LB_L-(1+rho0)*LQ_L
LBH_L,LBH_U=log_bounds_gt1(1/beta_hat,4)
log_beta_hat_lower=-LBH_U
assert logbeta_upper < log_beta_hat_lower < 0

delta=2*(c-a9)
assert delta==F(1,62500)

# Explicit finite-to-infinite error for horizontal scale M divisible by 9:
# err(M)=2*c*C*beta_hat^M + sqrt(2*pbar/(9*M)).
# This is a rigorous displayed bound; no finite M is needed for the
# infinite-volume theorem. The square-root term comes from P04 strip-9
# endpoint repair E|S_N| <= sqrt(N*pbar), with N=2M/9.
assert q<1 and beta_hat<1 and pbar<1

print("PROB10-10 retitled ten-local dual exact certificate")
print("states =",len(states),"transitions =",sum(len(ls) for ls in trans),
      "dead_ends =",sum(1 for ls in trans if not ls))
print("A =",A,"B =",B)
print("z_min =",min(z),"z_max =",max(z))
print("max_Mz_over_z_index =",max_i)
print("max_Mz_over_z =",max_ratio)
print("r =",r,"exact_slack =",r-max_ratio)
for m,v in startup:
    print("startup",m,"normalized_float =",float(v))
print("K_float =",float(K))
print("C_float =",float(C))
print("a9_float =",float(a9))
print("pbar_float =",float(pbar))
print("rho_star_lower_float =",float(rho_star_L))
print("rho_star_upper_float =",float(rho_star_U))
print("rho_star_width_float =",float(rho_star_U-rho_star_L))
print("rho0 =",rho0,"rho0_float =",float(rho0))
print("c_float =",float(c))
print("s_float =",float(s),"q_float =",float(q))
print("logbeta_upper_float =",float(logbeta_upper))
print("log_beta_hat_lower_float =",float(log_beta_hat_lower))
print("delta =",delta,"delta_float =",float(delta))
print("finite_error_formula = 2*c*C*(99997/100000)^M + sqrt(2*pbar/(9*M)), for 9|M")
print("ALL_EXACT_CHECKS_PASS = True")
