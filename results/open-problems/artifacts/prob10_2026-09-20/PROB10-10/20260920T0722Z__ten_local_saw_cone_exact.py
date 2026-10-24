from fractions import Fraction as F
from itertools import product
from math import factorial

# PROB10-10 ten-local-SAW exact certificate.
# Floating arithmetic is used ONLY to propose a positive integer Collatz vector.
# Every promoted transfer inequality, logarithmic comparison, and final sign
# is rechecked below with exact Fraction arithmetic.

dirs=((1,0),(-1,0),(0,1),(0,-1))
A=F(3889,2000)      # 1.9445
B=F(27893,10000)    # 2.7893
r=F(1993,400)       # 4.9825
s=F(398251,100000)  # 3.98251 > r-1
q=r/(1+s)
c=F(121,200)        # 0.605
rho=F(1701,1000)    # 1.701
beta_hat=F(2499,2500) # 0.9996
w=(A,1/A,B,1/B)
wf=tuple(float(x) for x in w)

# 10-step locally self-avoiding states: all 11 window vertices distinct.
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

# Deterministic floating proposal.  Trap states are kept positive by a tiny
# floor.  Exact rational verification below is authoritative.
zfloat=[1.0]*len(states)
eps=1e-14
for iteration in range(100):
    nz=[sum(wf[d]*zfloat[j] for j,d in ls) for ls in trans]
    mx=max(nz)
    floor=eps*mx
    nz=[v if v>=floor else floor for v in nz]
    mn=min(nz)
    zfloat=[v/mn for v in nz]
z=[max(1,int(round(v))) for v in zfloat]
assert min(z)>=1

max_ratio=F(0)
max_i=-1
for i,ls in enumerate(trans):
    lhs=sum((w[d]*z[j] for j,d in ls),F(0))
    ratio_i=lhs/F(z[i])
    if ratio_i>max_ratio:
        max_ratio=ratio_i
        max_i=i
assert max_ratio < r

# L_m <= K r^m. For m>=10 use the Collatz vector.
sumaz=F(0)
for word,zi in zip(states,z):
    ww=F(1)
    for d in word:
        ww*=w[d]
    sumaz += ww*zi
K10=sumaz/(r**10)

# For m<10, enumerate genuine SAWs exactly; these are the only startup cases
# relevant to the endpoint count.
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

# Rigorous logarithm bounds for x>1:
# log x = 2 sum_{k>=0} z^(2k+1)/(2k+1), z=(x-1)/(x+1).
# The lower bound is the partial sum; the positive tail is bounded
# geometrically by replacing every later denominator by the first omitted one.
def log_bounds_gt1(x,N):
    assert x>1
    z0=(x-1)/(x+1)
    L=F(0)
    for k in range(N+1):
        L += F(2)*z0**(2*k+1)/F(2*k+1)
    tail=F(2)*z0**(2*N+3)/(F(2*N+3)*(1-z0*z0))
    return L,L+tail

LA_L,LA_U=log_bounds_gt1(A,14)
LB_L,LB_U=log_bounds_gt1(B,14)
LQ_L,LQ_U=log_bounds_gt1(1/q,2)
# log beta = sc - log A - rho log B - (1+rho) log(1/q).
logbeta_upper=s*c-LA_L-rho*LB_L-(1+rho)*LQ_L

LBH_L,LBH_U=log_bounds_gt1(1/beta_hat,3)
log_beta_hat_lower=-LBH_U
assert logbeta_upper < log_beta_hat_lower

# Consumed P04 seven-column carry-lane theorem.
a7=F(49279440150576815510877201378785240485589858515856075374192914164647729263797,
     81456881928364919725453017902788824118878214603726702705992953229312000000000)
piO=F(40379780780386028600356821383956979806106624,
      63945812674576825594122899689798242883976669)
delta=2*(c-a7)
assert delta>0

# Explicit finite-to-infinite residual at m=an, requiring 7|m so the
# consumed seven-column axis block tiles the length 2m.
mfinite=140000
assert mfinite%7==0
finite_margin=delta-2*c*C*(beta_hat**mfinite)-piO/F(mfinite)
assert finite_margin>0

# A nearby smaller multiple is still negative, to show the scale check is
# non-vacuous rather than a sign typo.
mfail=138600
assert mfail%7==0
fail_margin=delta-2*c*C*(beta_hat**mfail)-piO/F(mfail)
assert fail_margin<0

print("PROB10-10 ten-local-SAW cone certificate")
print("states =",len(states),"transitions =",sum(len(ls) for ls in trans),"dead_ends =",sum(1 for ls in trans if not ls))
print("z_min =",min(z),"z_max =",max(z))
print("max_Mz_over_z_index =",max_i)
print("max_Mz_over_z =",max_ratio)
print("r =",r,"exact_slack =",r-max_ratio)
for m,v in startup:
    print("startup",m,"normalized_float =",float(v))
print("K_float =",float(K))
print("K_num_bits =",K.numerator.bit_length(),"K_den_bits =",K.denominator.bit_length())
print("q =",q,"q_float =",float(q))
print("rho0 =",rho,"rho0_float =",float(rho))
print("c =",c,"c_float =",float(c))
print("logbeta_upper_float =",float(logbeta_upper))
print("log_beta_hat_lower_float =",float(log_beta_hat_lower))
print("logbeta_upper < log(beta_hat)_lower =",logbeta_upper < log_beta_hat_lower)
print("a7_float =",float(a7))
print("delta =",delta)
print("delta_float =",float(delta))
print("C_float =",float(C))
print("piO_float =",float(piO))
print("finite_scale_m =",mfinite)
print("finite_margin_float =",float(finite_margin))
print("finite_margin_num_bits =",finite_margin.numerator.bit_length(),"den_bits =",finite_margin.denominator.bit_length())
print("negative_test_m =",mfail)
print("negative_test_margin_float =",float(fail_margin))
print("ALL_EXACT_CHECKS_PASS = True")
