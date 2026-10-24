from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import factorial

# P04 T10 exact certificate.
# Part I: a six-column, three-row directed-east / vertical-undirected block.
KBLK = 6
verts = [(x,r) for x in range(KBLK+1) for r in range(3)]
idx = {v:i for i,v in enumerate(verts)}
out = [[] for _ in verts]
for x in range(KBLK):
    # Vertical physical edges in departure columns only; both orientations are allowed.
    for r in (0,1):
        a,b = idx[(x,r)],idx[(x,r+1)]
        out[a].append(b); out[b].append(a)
    # Physical horizontal edges are used only eastward by the policy.
    for r in range(3):
        out[idx[(x,r)]].append(idx[(x+1,r)])
targets = [idx[(KBLK,r)] for r in range(3)]

def absorption(start_lane):
    states = 0
    @lru_cache(None)
    def rec(mask):
        nonlocal states
        states += 1
        for j,t in enumerate(targets):
            if (mask >> t) & 1:
                p = [F(0),F(0),F(0)]
                p[j] = F(1)
                return F(0), tuple(p)
        rates = {}
        total = 0
        mm = mask
        while mm:
            bit = mm & -mm
            i = bit.bit_length()-1
            mm -= bit
            for j in out[i]:
                if not ((mask >> j) & 1):
                    rates[j] = rates.get(j,0)+1
                    total += 1
        assert total > 0
        et = F(1,total)
        ps = [F(0),F(0),F(0)]
        for j,mult in rates.items():
            ej,pj = rec(mask | (1 << j))
            w = F(mult,total)
            et += w*ej
            for q in range(3):
                ps[q] += w*pj[q]
        return et,tuple(ps)
    ans = rec(1 << idx[(0,start_lane)])
    return ans,states

((gO,pO),statesO) = absorption(0)
((gC,pC),statesC) = absorption(1)
assert sum(pO,F(0)) == 1 and sum(pC,F(0)) == 1
# Reflection gives the same gO and center-hit probability from the lower outer lane.
pOC = pO[1]
pCC = pC[1]
lam = pCC-pOC
assert 0 < lam < 1
assert gC < gO
piC = pOC/(pOC + 1-pCC)
piO = 1-piC
assert 0 < piC < 1
abar = (piC*gC + piO*gO)/KBLK
# From a center start the C/O chain has C-mass piC + piO*lam^j,
# so each expected block reward is at most the stationary mean because gC<gO.
# A terminal outer lane is repaired to center by one fresh Exp(1) vertical edge;
# its expected correction is at most piO.

# Compare with the preceding P04 length-8 fixed-end ladder bound.
A8 = F(4688722489067361283750127182134186345695457354381617699,
       7437921710332085596529852377779940412620800000000000000)
assert abar < A8

# Part II: exact reuse/reverification of the canonical 4-local-SAW path-count certificate.
A = F(1903,1000)
B = F(2837,1000)
r = F(4999,1000)
u = F(5,1)  # 1+s
s = u-1
q = r/u
assert q == F(4999,5000)
dirs = ((1,0),(-1,0),(0,1),(0,-1))
w = (A,1/A,B,1/B)

states=[]
for word in product(range(4), repeat=4):
    x=y=0; seen={(0,0)}; ok=True
    for d in word:
        dx,dy=dirs[d]; x+=dx; y+=dy
        if (x,y) in seen:
            ok=False; break
        seen.add((x,y))
    if ok:
        states.append(word)
Sidx={word:i for i,word in enumerate(states)}
trans=[[] for _ in states]
for i,word in enumerate(states):
    for d in range(4):
        nw=word[1:]+(d,)
        if nw in Sidx:
            trans[i].append((Sidx[nw],d))

zint=[12492429,12996418,5078240,12484340,8188922,13003834,12003664,1090773,5570659,12492429,12996418,4963551,8396815,12870535,12484340,8259451,13003834,12492429,12135396,5078240,8396815,2947622,12003664,5774021,5570659,8396815,12870535,2947622,12134266,8259451,13003834,5114929,5774021,5570659,12492429,12996418,8396815,12870535,1000000,12484340,8259451,13003834,12492429,5078240,8396815,8250147,2947622,12003664,5774021,5570659,12492429,12996418,5078240,12484340,8188922,13003834,12003664,5570659,8396815,12870535,2947622,12134266,8259451,13003834,5774021,5570659,12492429,12996418,4963551,8396815,12870535,1000000,12484340,8259451,13003834,12492429,12996418,5078240,12484340,13003834,12003664,1090773,5570659,8396815,12870535,2947622,8259451,13003834,5114929,5774021,5570659,12492429,12135396,5078240,8396815,8250147,2947622,12003664,5774021,5570659]
assert len(states)==100 and len(zint)==100
assert sum(len(t) for t in trans)==284
zmin=min(zint)
z=[F(v,zmin) for v in zint]
ratios=[]
for i,ls in enumerate(trans):
    lhs=sum((w[d]*z[j] for j,d in ls),F(0))
    ratios.append(lhs/z[i])
max_ratio=max(ratios)
assert max_ratio < r

a=[]
for word in states:
    ww=F(1)
    for d in word:
        ww*=w[d]
    a.append(ww)
K4=sum(ai*zi for ai,zi in zip(a,z))/(r**4)

def saw_weight_sum(m):
    total=F(0)
    for word in product(range(4), repeat=m):
        x=y=0; seen={(0,0)}; ok=True; ww=F(1)
        for d in word:
            dx,dy=dirs[d]; x+=dx; y+=dy
            if (x,y) in seen:
                ok=False; break
            seen.add((x,y)); ww*=w[d]
        if ok:
            total += ww
    return total
startup=[]
for m0 in (1,2,3):
    W=saw_weight_sum(m0)
    startup.append((m0,W,W/(r**m0)))
K=max([K4]+[x[2] for x in startup])
assert K==K4
C=K/(1-q)
assert C == F(35548730504621175912805033436058585575537199210,
              530548441769990085527241493316853229845841)

# Part III: retune the lower-tail compiler to the stronger axis policy.
c = F(1901,3125)       # 0.60832
rho = F(429,250)        # 1.716
beta_hat = F(24999,25000)  # 0.99996
assert abar < c
assert rho < F(361,200)     # genuine enlargement beyond the current 1.805 cone

# beta(rho)^250 = A^-250 B^-429 exp(250*s*c) q^(250+429).
# Rigorous upper bound on exp(x): split x into 2048 equal pieces; for each
# piece use a degree-24 Taylor polynomial plus geometric domination of the tail.
x = F(250)*s*c
kscale = 2048
y = x/F(kscale)
Nt = 24
T = sum((y**j)/F(factorial(j)) for j in range(Nt+1))
first = y**(Nt+1)/F(factorial(Nt+1))
ratio_tail = y/F(Nt+2)
assert ratio_tail < 1
U = T + first/(1-ratio_tail)
exp_x_upper = U**kscale
beta250_upper = (A**(-250))*(B**(-429))*exp_x_upper*(q**679)
assert beta250_upper < beta_hat**250
assert beta_hat < 1

# Infinite-volume reflected strict-triangle defect.
delta = 2*(c-abar)
assert delta > F(0)
assert delta > F(4,100000)   # > 4e-5

# Explicit finite residual budget.  Let m=an.  If 3|m, then 2m is a multiple
# of the 6-column block length.  The axis upper bound contributes piO/m.
# Since beta_hat=(1-1/25000), beta_hat^m <= exp(-m/25000).
# At m=550002 (divisible by 3), lower-bound exp(m/25000) by its positive
# degree-80 Taylor polynomial.
mfinite = 550002
assert mfinite % 3 == 0
xe = F(mfinite,25000)
Elow = sum((xe**j)/F(factorial(j)) for j in range(81))
finite_error_upper = 2*c*C/Elow + piO/F(mfinite)
finite_margin_lower = delta-finite_error_upper
assert finite_margin_lower > F(1,100000)

print('P04 T10 exact strip-6 Markov / cone-1.716 certificate')
print('ALL_EXACT_CHECKS_PASS = True')
print('block_width =',KBLK)
print('block_states_outer =',statesO)
print('block_states_center =',statesC)
print('gO =',gO,'=',float(gO))
print('gC =',gC,'=',float(gC))
print('pOC =',pOC,'=',float(pOC))
print('pCC =',pCC,'=',float(pCC))
print('lambda =',lam,'=',float(lam))
print('piC =',piC,'=',float(piC))
print('piO =',piO,'=',float(piO))
print('axis_policy_bound =',abar,'=',float(abar))
print('previous_A8 =',A8,'=',float(A8))
print('axis_improvement =',A8-abar,'=',float(A8-abar))
print('local_SAW_states =',len(states),'transitions =',sum(len(t) for t in trans))
print('max_Mz_over_z =',max_ratio,'=',float(max_ratio))
print('C =',C,'=',float(C))
print('c =',c,'=',float(c))
print('rho =',rho,'=',float(rho))
print('beta_hat =',beta_hat,'=',float(beta_hat))
print('beta250_upper_float =',float(beta250_upper))
print('beta_hat_250_float =',float(beta_hat**250))
print('delta =',delta,'=',float(delta))
print('finite_m =',mfinite)
print('finite_error_upper =',finite_error_upper,'=',float(finite_error_upper))
print('finite_margin_lower =',finite_margin_lower,'=',float(finite_margin_lower))
