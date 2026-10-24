from fractions import Fraction as F
from itertools import product
from math import factorial

# PROB10-10 six-local-SAW exact certificate.
# Floating point is used only to GENERATE a candidate positive vector.
# Every promoted transfer-matrix inequality and every sign is then rechecked
# exactly with Fraction arithmetic.

A=F(1939,1000)
B=F(2795,1000)
r=F(623,125)
nu=F(997,200)
s=nu-1
q=r/nu
c=F(6083,10000)
rho=F(857,500)
beta_hat=F(9997,10000)

dirs=((1,0),(-1,0),(0,1),(0,-1))
w=(A,1/A,B,1/B)
wf=tuple(float(x) for x in w)

# States: six steps whose seven visited vertices are all distinct.
states=[]
for word in product(range(4), repeat=6):
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
assert len(states)==780
assert sum(len(t) for t in trans)==2172

# Deterministic floating power iteration to propose z; exact verification follows.
zf=[1.0]*len(states)
for iteration in range(200):
    nz=[sum(wf[d]*zf[j] for j,d in ls) for ls in trans]
    mn=min(nz)
    nz=[v/mn for v in nz]
    err=max(abs(nz[i]/zf[i]-1.0) for i in range(len(zf)))
    zf=nz
    if err < 1e-14:
        break
zint=[int(round(v*10**9)) for v in zf]
zmin=min(zint)
z=[F(v,zmin) for v in zint]
assert zmin>0

ratios=[]
for i,ls in enumerate(trans):
    lhs=sum(w[d]*z[j] for j,d in ls)
    ratios.append(lhs/z[i])
max_ratio=max(ratios)
max_i=ratios.index(max_ratio)
assert max_ratio < r

# Total tilted weight bound L_m <= K r^m.
avec=[]
for word in states:
    ww=F(1)
    for d in word:
        ww*=w[d]
    avec.append(ww)
K6=sum(ai*zi for ai,zi in zip(avec,z))/(r**6)

def saw_weight_sum(m):
    total=F(0)
    def rec(x,y,seen,depth,ww):
        nonlocal total
        if depth==m:
            total+=ww
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
for m in range(1,6):
    W=saw_weight_sum(m)
    startup.append((m,W,W/(r**m)))
K=max([K6]+[t[2] for t in startup])
assert K==K6
C=K/(1-q)

# Finite negation test. The theorem uses the direct global-SAW inclusion proof;
# this enumeration is only a sanity check.
short_saw_count=0
def check_short_saws(m):
    global short_saw_count
    word=[]
    def rec(x,y,seen,depth):
        global short_saw_count
        if depth==m:
            short_saw_count+=1
            tup=tuple(word)
            for j in range(m-5):
                assert tup[j:j+6] in idx
            return
        for d,(dx,dy) in enumerate(dirs):
            nx,ny=x+dx,y+dy
            if (nx,ny) in seen:
                continue
            seen.add((nx,ny)); word.append(d)
            rec(nx,ny,seen,depth+1)
            word.pop(); seen.remove((nx,ny))
    rec(0,0,{(0,0)},0)
for m in range(6,11):
    check_short_saws(m)
assert short_saw_count==69236

# Exact rational upper certificate for beta(rho)^500.
# beta=A^-1 B^-rho exp(sc) q^(1+rho), rho=857/500.
x=F(500)*s*c
split=2048
y=x/split
N=24
T=sum((y**j)/factorial(j) for j in range(N+1))
first=(y**(N+1))/factorial(N+1)
assert y/F(N+2,1) < 1
U=T+first/(1-y/F(N+2,1))
# e^y < U by bounding the positive Taylor tail geometrically.
exp_x_upper=U**split
beta500_upper=(A**(-500))*(B**(-857))*exp_x_upper*(q**1357)
assert beta500_upper < beta_hat**500

# P04 six-column carry-lane axis theorem, consumed input.
a6=F(57444100690415803497507130042889304438078500562657949173917,
     94434081367035184054991164646261870153788595690449920000000)
piC=F(2095562334665629616215085932452515,
      5682936976425472344119584785039011)
piO=1-piC
delta=2*(c-a6)
assert delta>0

# For m=an divisible by 3:
# E R/m >= delta - 2 c C beta_hat^m - piO/m.
mfinite=200001
assert mfinite%3==0
finite_margin=delta-2*c*C*(beta_hat**mfinite)-piO/F(mfinite)
assert finite_margin>0

mprev=197382
assert mprev%3==0
prev_margin=delta-2*c*C*(beta_hat**mprev)-piO/F(mprev)
assert prev_margin<0

print("PROB10-10 exact six-local-SAW cone certificate")
print("power_iterations =",iteration+1)
print("states =",len(states),"transitions =",sum(len(t) for t in trans))
print("zmin =",zmin,"zmax =",max(zint))
print("max_Mz_over_z_index =",max_i)
print("max_Mz_over_z =",max_ratio)
print("r =",r,"slack =",r-max_ratio)
for m,W,km in startup:
    print("startup",m,"normalized =",km)
print("K =",K)
print("short_SAW_windows_checked =",short_saw_count)
print("q =",q)
print("C_float =",float(C))
print("c =",c,"float =",float(c))
print("rho0 =",rho,"float =",float(rho))
print("beta_hat =",beta_hat,"float =",float(beta_hat))
print("beta500_upper_float =",float(beta500_upper))
print("beta_hat_500_float =",float(beta_hat**500))
print("beta500_upper < beta_hat^500 =",beta500_upper < beta_hat**500)
print("a6_float =",float(a6))
print("delta =",delta)
print("delta_float =",float(delta))
print("piO_float =",float(piO))
print("finite_scale_m =",mfinite)
print("finite_margin_float =",float(finite_margin))
print("finite_margin_num_bits =",finite_margin.numerator.bit_length(),
      "den_bits =",finite_margin.denominator.bit_length())
print("previous_scale_m =",mprev)
print("previous_margin_float =",float(prev_margin))
print("ALL_EXACT_CHECKS_PASS = True")
