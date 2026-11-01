from fractions import Fraction as F
from itertools import permutations
from math import factorial

print("HARD7-03 exact local-minimum triple-slack certificate")

A_VARS = (-1,0,1)

def A3(t):
    return F(2) * (
        F(2268) - F(4408)*t + F(3748)*t**2 - F(1918)*t**3
        + F(652)*t**4 - F(143)*t**5 + F(18)*t**6 - t**7
    ) / ((F(3)-t)**4 * (F(2)-t)**3 * (F(1)-t)**3)

def M2(z,t):
    z = abs(z)
    if z == 2:
        return F(1)/(F(1)-t)**2
    if z == 1:
        return F(2)/((F(1)-t)**2*(F(2)-t))
    if z == 0:
        return F(6)/((F(1)-t)**2*(F(2)-t)*(F(3)-t))
    raise ValueError(z)

def pair_correction(t):
    return F(8)/(F(2)-t) * (M2(0,t)+M2(1,t)+M2(2,t))

def kappa(t):
    return t/((F(2)-t)*(F(3)-t))

def ordered_exp_integral(c):
    c1,c2,c3 = c
    r1 = F(3) - (c1+c2+c3)
    r2 = F(2) - (c2+c3)
    r3 = F(1) - c3
    assert r1 > 0 and r2 > 0 and r3 > 0
    return F(1)/(r1*r2*r3)

def weighted_target_max(t,bases,target):
    labels = list(bases)
    competitors = [j for j in labels if j != target]
    total = F(0)
    for perm in permutations(A_VARS):
        rank = {var:i for i,var in enumerate(perm)}
        br = {label:max(rank[v] for v in subset) for label,subset in bases.items()}
        M = max(br.values())
        for mask in range(1 << len(competitors)):
            S = [competitors[k] for k in range(len(competitors)) if (mask >> k) & 1]
            q = F(1)-t+len(S)
            c = [F(0),F(0),F(0)]
            c[br[target]] += 1
            for j in S:
                c[br[j]] += 1
            c[M] -= q
            term = ordered_exp_integral(c)/q
            total += -term if len(S) % 2 else term
    return total

def interval_integral(c,q,Lrank,Urank=None):
    if Urank is not None and Urank <= Lrank:
        return F(0)
    cL = list(c)
    cL[Lrank] -= q
    ans = ordered_exp_integral(cL)/q
    if Urank is not None:
        cU = list(c)
        cU[Urank] -= q
        ans -= ordered_exp_integral(cU)/q
    return ans

def weighted_chain(t,bases,upper,target,lowers):
    total = F(0)
    for perm in permutations(A_VARS):
        rank = {var:i for i,var in enumerate(perm)}
        br = {label:max(rank[v] for v in subset) for label,subset in bases.items()}
        Lrank = max([br[target]] + [br[l] for l in lowers])
        Urank = br[upper]
        for mask in range(1 << len(lowers)):
            S = [lowers[k] for k in range(len(lowers)) if (mask >> k) & 1]
            sign = -1 if len(S) % 2 else 1
            c = [F(0),F(0),F(0)]
            c[br[target]] += 1
            for l in S:
                c[br[l]] += 1
            q1 = F(1)-t+len(S)
            total += sign * interval_integral(c,q1,Lrank,Urank)
            c2 = list(c)
            c2[Urank] += 1
            q2 = q1 + 1
            total += sign * interval_integral(c2,q2,max(Lrank,Urank),None)
    return total

BASES_ALL = {
    -2:{-1},
    -1:{-1,0},
     0:{-1,0,1},
     1:{0,1},
     2:{1},
}

theta = F(5871,10000)
a = F(18543,6250)
old_L = F(3125,37092)

M2loc = weighted_target_max(theta,{2:{1},1:{0,1}},2)
M2closed = (F(3)-F(2)*theta)/((F(1)-theta)**2*(F(2)-theta)**3)
assert M2loc == M2closed

M1_target = weighted_target_max(theta,{0:{-1,0,1},1:{0,1},2:{1}},1)
M1_chain = weighted_chain(theta,BASES_ALL,upper=-1,target=2,lowers=[0,1])
M1loc = M1_target + M1_chain

M0_target = weighted_target_max(theta,{-1:{-1,0},0:{-1,0,1},1:{0,1}},0)
M0_chain_right = weighted_chain(theta,BASES_ALL,upper=2,target=-1,lowers=[0,1])
M0_chain_left = weighted_chain(theta,BASES_ALL,upper=-2,target=1,lowers=[-1,0])
assert M0_chain_right == M0_chain_left
M0loc = M0_target + M0_chain_right + M0_chain_left

W1dom = weighted_target_max(theta,{
    1:{0,1}, -1:{-1,0}, 0:{-1,0,1}, 2:{1}
},1)
W0dom = weighted_target_max(theta,{
    0:{-1,0,1}, -2:{-1}, -1:{-1,0}, 1:{0,1}, 2:{1}
},0)
assert M1loc > W1dom
assert M0loc > W0dom

H_dom = kappa(theta)*(F(2)*M2loc + F(2)*W1dom + W0dom)
H_loc = kappa(theta)*(F(2)*M2loc + F(2)*M1loc + M0loc)
assert H_loc > H_dom

U4 = (F(3)*A3(theta) - pair_correction(theta) - H_loc)/(F(1)-theta)

x = F(4)*theta*a
S24 = sum(x**k/F(factorial(k),1) for k in range(25))
margin = S24-U4
assert margin > 0

new_L = F(1)/(F(4)*a)
assert new_L == F(3125,37086)
assert new_L > old_L

print(f"theta = {theta}")
print(f"a = {a}")
print(f"M2loc = {M2loc}")
print(f"M1_target = {M1_target}")
print(f"M1_chain = {M1_chain}")
print(f"M1loc = {M1loc}")
print(f"M0_target = {M0_target}")
print(f"M0_chain_right = {M0_chain_right}")
print(f"M0_chain_left = {M0_chain_left}")
print(f"M0loc = {M0loc}")
print(f"W1dom = {W1dom}")
print(f"W0dom = {W0dom}")
print(f"H_dom = {H_dom}")
print(f"H_loc = {H_loc}")
print(f"H_gain = {H_loc-H_dom}")
print(f"U4 = {U4}")
print(f"U4_float = {float(U4):.15f}")
print(f"x = {x}")
print(f"S24_minus_U4 = {margin}")
print(f"S24_minus_U4_float = {float(margin):.15f}")
print(f"old_L = {old_L}")
print(f"new_L = {new_L}")
print(f"metric_gain = {new_L-old_L}")
print(f"new_L_float = {float(new_L):.15f}")
print("ALL_EXACT_CHECKS_PASS = True")
