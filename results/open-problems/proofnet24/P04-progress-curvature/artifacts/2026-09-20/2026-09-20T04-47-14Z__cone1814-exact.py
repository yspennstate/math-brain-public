from fractions import Fraction as F
from functools import lru_cache

# Exact L=8, width-three ladder infection recursion.
L=8
ys=(-1,0,1)
verts=[(x,y) for x in range(L+1) for y in ys]
idx={v:i for i,v in enumerate(verts)}
N=len(verts)
neigh=[[] for _ in range(N)]
for i,(x,y) in enumerate(verts):
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        v=(x+dx,y+dy)
        if v in idx:
            neigh[i].append(idx[v])
source=idx[(0,0)]
target=idx[(L,0)]
states=0

@lru_cache(None)
def E(mask):
    global states
    states += 1
    if (mask >> target) & 1:
        return F(0)
    rates={}
    boundary=0
    mm=mask
    while mm:
        bit=mm & -mm
        i=bit.bit_length()-1
        mm -= bit
        for j in neigh[i]:
            if not ((mask >> j) & 1):
                boundary += 1
                rates[j]=rates.get(j,0)+1
    ans=F(1,boundary)
    for j,mult in rates.items():
        ans += F(mult,boundary)*E(mask | (1<<j))
    return ans

EM8=E(1<<source)
a8=EM8/F(8)

# Reuse and reverify the exact non-backtracking certificate from the current
# canonical T10 cone route, but retune the lower threshold and cone slope.
A=F(189,100)
B=F(291,100)
w=[A,1/A,B,1/B]
z=[F(2095936,10**6),F(1469509,10**6),F(2181303,10**6),F(1)]
r=F(5083,1000)
s=F(1021,250)
c=F(63039,100000)
rho=F(907,500)
beta_hat=F(24994,25000)
rev=(1,0,3,2)
ratios=[]
for i in range(4):
    mz=sum((w[j]*z[j] for j in range(4) if j != rev[i]),F(0))
    ratios.append(mz/z[i])
    assert mz <= r*z[i]
assert min(z) >= 1
q=r/(1+s)
assert q == F(5083,5084)
K=sum((w[i]*z[i] for i in range(4)),F(0))/r
C=K/(1-q)
assert K == F(20954749844641,9318663900000)
assert C == F(26633487052538711,2329665975000)

# Rigorous rational upper bound on exp(x), x=s*c, from a degree-20 Taylor sum
# plus a geometric bound on the positive tail.
x=s*c
Ntay=20
term=F(1)
Ebar=term
for k in range(1,Ntay+1):
    term *= x/F(k)
    Ebar += term
term21=term*x/F(Ntay+1)
ratio_tail=x/F(Ntay+2)
assert ratio_tail < 1
Ebar += term21/(1-ratio_tail)
# e^x < Ebar.  Since rho=907/500,
# beta(rho)^500 = A^-500 B^-907 e^(500 x) q^1407.
U=(A**(-500))*(B**(-907))*(Ebar**500)*(q**1407)
assert U < beta_hat**500
assert beta_hat < 1

delta=2*(c-a8)
assert delta > F(0)
assert delta > F(1,100000)
finite_n=90000
finite_error=2*c*C*(beta_hat**finite_n)
finite_margin=delta-finite_error
assert finite_n % 4 == 0
assert finite_margin > F(1,100000)

print('ALL_EXACT_CHECKS_PASS')
print('ladder_vertices=',N)
print('ladder_states=',states)
print('E_M8=',EM8)
print('a8=',a8)
print('a8_decimal=',float(a8))
print('rho=',rho,'rho_decimal=',float(rho))
print('c=',c,'c_decimal=',float(c))
print('delta=',delta)
print('delta_decimal=',float(delta))
print('delta_gt_1e-5=',delta>F(1,100000))
print('finite_n=',finite_n)
print('finite_error_at_a1=',float(finite_error))
print('finite_margin_at_a1=',float(finite_margin))
print('finite_margin_gt_1e-5=',finite_margin>F(1,100000))
print('q=',q,'q_decimal=',float(q))
print('K=',K,'K_decimal=',float(K))
print('C=',C,'C_decimal=',float(C))
print('beta_hat=',beta_hat,'beta_hat_decimal=',float(beta_hat))
print('exp_taylor_degree=',Ntay)
print('U_lt_beta_hat_pow_500=',U < beta_hat**500)
print('U_decimal=',float(U))
print('component_ratios=',','.join(str(v) for v in ratios))
