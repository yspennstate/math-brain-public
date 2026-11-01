from fractions import Fraction as F
from itertools import product
from math import factorial, log, exp

# Frozen certificate parameters.
A = F(1903,1000)
B = F(2837,1000)
r = F(4999,1000)
u = F(5,1)          # 1+s
s = u-1
q = r/u
c = F(63039,100000)
rho = F(361,200)
beta_hat = F(249,250)

# Directions E,W,N,S.
dirs = ((1,0),(-1,0),(0,1),(0,-1))
w = (A,1/A,B,1/B)

# Four-step words whose five visited vertices are distinct.
states=[]
for word in product(range(4), repeat=4):
    x=y=0
    seen={(0,0)}
    ok=True
    for d in word:
        dx,dy=dirs[d]; x+=dx; y+=dy
        if (x,y) in seen:
            ok=False; break
        seen.add((x,y))
    if ok:
        states.append(word)
idx={word:i for i,word in enumerate(states)}
trans=[[] for _ in states]
for i,word in enumerate(states):
    for d in range(4):
        nw=word[1:]+(d,)
        if nw in idx:
            trans[i].append((idx[nw],d))

# Hard-coded positive Collatz vector, generated once numerically but verified below only by exact arithmetic.
zint=[12492429, 12996418, 5078240, 12484340, 8188922, 13003834, 12003664, 1090773, 5570659, 12492429, 12996418, 4963551, 8396815, 12870535, 12484340, 8259451, 13003834, 12492429, 12135396, 5078240, 8396815, 2947622, 12003664, 5774021, 5570659, 8396815, 12870535, 2947622, 12134266, 8259451, 13003834, 5114929, 5774021, 5570659, 12492429, 12996418, 8396815, 12870535, 1000000, 12484340, 8259451, 13003834, 12492429, 5078240, 8396815, 8250147, 2947622, 12003664, 5774021, 5570659, 12492429, 12996418, 5078240, 12484340, 8188922, 13003834, 12003664, 5570659, 8396815, 12870535, 2947622, 12134266, 8259451, 13003834, 5774021, 5570659, 12492429, 12996418, 4963551, 8396815, 12870535, 1000000, 12484340, 8259451, 13003834, 12492429, 12996418, 5078240, 12484340, 13003834, 12003664, 1090773, 5570659, 8396815, 12870535, 2947622, 8259451, 13003834, 5114929, 5774021, 5570659, 12492429, 12135396, 5078240, 8396815, 8250147, 2947622, 12003664, 5774021, 5570659]
assert len(states)==100 and len(zint)==100
assert sum(len(t) for t in trans)==284
zmin=min(zint)
z=[F(v,zmin) for v in zint]
assert min(z)==1

ratios=[]
for i,ls in enumerate(trans):
    lhs=sum(w[d]*z[j] for j,d in ls)
    ratios.append(lhs/z[i])
max_ratio=max(ratios)
max_i=ratios.index(max_ratio)
assert max_ratio < r

# Initial vector a_s = tilted weight of the first four directions.
a=[]
for word in states:
    ww=F(1)
    for d in word:
        ww*=w[d]
    a.append(ww)
K4=sum(ai*zi for ai,zi in zip(a,z))/(r**4)

# Cover startup lengths 1,2,3 with the same K.
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
            total+=ww
    return total
startup=[]
for m in (1,2,3):
    W=saw_weight_sum(m)
    startup.append((m,W,W/(r**m)))
K=max([K4]+[x[2] for x in startup])
assert K==K4
C=K/(1-q)

# Exact short-word negation test: every genuine SAW through length 9 has each 4-window in S4.
# This is only a self-check; the general inclusion is proved symbolically in the report.
short_saw_count=0
for m in range(4,10):
    for word in product(range(4), repeat=m):
        x=y=0; seen={(0,0)}; ok=True
        for d in word:
            dx,dy=dirs[d]; x+=dx; y+=dy
            if (x,y) in seen:
                ok=False; break
            seen.add((x,y))
        if not ok:
            continue
        short_saw_count+=1
        for j in range(m-3):
            assert word[j:j+4] in idx

# Exact upper bound on beta(rho)^200.
# beta = A^{-1} B^{-rho} exp(sc) q^{1+rho}; multiplying exponent by 200 clears rho's denominator.
x=F(200)*s*c          # = 800 c = 504.312
k=1024
y=x/k
N=24
T=sum((y**j)/factorial(j) for j in range(N+1))
first=(y**(N+1))/factorial(N+1)
# For j>=N+1, successive Taylor-term ratio <= y/(N+2), so this is a rigorous upper bound on e^y.
U=T+first/(1-y/F(N+2,1))
exp_x_upper=U**k
beta200_upper=(A**(-200))*(B**(-361))*exp_x_upper*(q**561)
assert beta200_upper < beta_hat**200

# P04 length-8 exact axis input and the new reflected-triangle defect.
A8=F(4688722489067361283750127182134186345695457354381617699,
     7437921710332085596529852377779940412620800000000000000)
delta=2*(c-A8)
assert delta>0

# Finite expected residual: for an divisible by 4,
# E R/(an) >= delta - 2 c C beta_hat^(an).
Nfinite=5552
finite_margin=delta-2*c*C*(beta_hat**Nfinite)
prev_margin=delta-2*c*C*(beta_hat**(Nfinite-4))
assert Nfinite % 4 == 0
assert finite_margin>0
assert prev_margin<=0

print('PROB10-10 exact four-step local-SAW cone certificate')
print('states =',len(states),'transitions =',sum(len(t) for t in trans))
print('zmin =',zmin,'zmax =',max(zint))
print('max_Mz_over_z_index =',max_i)
print('max_Mz_over_z =',max_ratio)
print('r =',r,'slack =',r-max_ratio)
for m,W,km in startup:
    print(f'm={m} weighted_SAW_sum={W} normalized={km}')
print('K =',K)
print('q =',q)
print('C =',C)
print('short_SAW_windows_checked =',short_saw_count)
print('rho0 =',rho,'=',float(rho))
print('c =',c,'=',float(c))
print('beta_hat =',beta_hat,'=',float(beta_hat))
print('beta200_upper_float =',float(beta200_upper))
print('beta_hat_200_float =',float(beta_hat**200))
print('beta200_upper < beta_hat^200 =',beta200_upper < beta_hat**200)
print('A8 =',A8)
print('delta =',delta,'=',float(delta))
print('finite_scale_an =',Nfinite)
print('finite_margin_float =',float(finite_margin))
print('finite_margin_num_bits =',finite_margin.numerator.bit_length(),'den_bits =',finite_margin.denominator.bit_length())
print('previous_multiple4_margin_float =',float(prev_margin))
print('previous_margin_num_bits =',prev_margin.numerator.bit_length(),'den_bits =',prev_margin.denominator.bit_length())
print('ALL_EXACT_CHECKS_PASS = True')
