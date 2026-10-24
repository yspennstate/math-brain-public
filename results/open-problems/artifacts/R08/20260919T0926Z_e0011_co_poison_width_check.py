#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache
from math import log10

# Current generated-shield entrance patch from the sound b17_rob Bellman checker.
CEL = ((-2,0),(-2,1),(-1,-1),(-1,0),(-1,1),(-1,2),
       (0,-1),(0,0),(0,1),(0,2),(1,-1),(1,0),(1,1),(1,2),(2,0),(2,1))
FIXED_VAC = {(-2,0),(-2,1),(-1,0),(-1,1),(0,0),(0,1)}
TARGET = {(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1)}
DIRS=((1,0),(-1,0),(0,1),(0,-1))

# Extremal entrance state: exactly the six required entrance vacancies, CO everywhere
# else in this finite patch, and an all-CO adversarial halo outside.
state = {c:(0 if c in FIXED_VAC else 1) for c in CEL}  # 0 vacancy, 1 CO
assert all(v in (0,1) for v in state.values())
assert not all(state[c] == 0 for c in TARGET)  # forward pair is CO
assert {(x,y) for (x,y),v in state.items() if v==0} == FIXED_VAC

# Filling the six vacancies with CO makes the whole finite patch all CO.
poison = dict(state)
for c in FIXED_VAC:
    poison[c]=1
assert all(v==1 for v in poison.values())
assert not all(poison[c]==0 for c in TARGET)

# Exact CTMC first-effective-event recursion for a w x 2 vacant rectangle in an
# all-CO environment. Each vacant site has a CO clock of rate 1/2. Each
# nearest-neighbour edge with two vacant endpoints has an O2 clock of rate 1/4.
# An O2 event is declared failure for the pure-CO poisoning event.
def poison_rect(w):
    coords=tuple((x,y) for x in range(w) for y in range(2))
    idx={c:i for i,c in enumerate(coords)}
    n=len(coords)
    adj=[0]*n
    for i,(x,y) in enumerate(coords):
        for dx,dy in DIRS:
            j=idx.get((x+dx,y+dy))
            if j is not None:
                adj[i] |= 1<<j

    @lru_cache(None)
    def q(mask):
        if mask==0:
            return Fraction(1)
        k=mask.bit_count()
        twice_edges=0
        for i in range(n):
            if (mask>>i)&1:
                twice_edges += (adj[i]&mask).bit_count()
        e=twice_edges//2
        # total effective rate = k/2 + e/4 = (2k+e)/4.
        # A specified CO fill has conditional probability (1/2)/total = 2/(2k+e).
        den=2*k+e
        ans=Fraction(0)
        m=mask
        while m:
            b=m & -m
            ans += Fraction(2,den)*q(mask ^ b)
            m -= b
        return ans

    return q((1<<n)-1), q.cache_info().currsize

vals=[]
for w in range(1,9):
    q,nstates=poison_rect(w)
    vals.append(q)
    print(f'w={w} q={q.numerator}/{q.denominator} decimal={float(q):.15g} states={nstates}')

# Exact checkpoints.
assert vals[0] == Fraction(4,5)
assert vals[1] == Fraction(13,30)
assert vals[2] == Fraction(79066,329175)
assert vals[6] == Fraction(1750406597455503270170325325575179417,
                           77782494778986392703098617947120000000)
assert vals[7] == Fraction(155748783257407943090794606068297776714517311,
                           12509137894535500799375708417886614419687500000)

# The current width-three entrance is far above the allowed 1/64 failure budget.
q3=vals[2]
hit_upper3=1-q3
assert q3 > Fraction(1,64)
assert hit_upper3 < Fraction(63,64)

# The pure-CO poisoning obstruction crosses below 1/64 exactly between widths 7 and 8
# among the computed widths.
assert all(vals[w-1] > Fraction(1,64) for w in range(1,8))
assert vals[7] < Fraction(1,64)
assert all(vals[i+1] < vals[i] for i in range(7))  # finite exact check, not a general theorem

print('PASS exact R08/E0011 all-CO poisoning / width deformation certificate')
print('entrance_fixed_vacancies=', sorted(FIXED_VAC))
print('entrance_target=', sorted(TARGET))
print('current_width=3')
print('q3_exact=', f'{q3.numerator}/{q3.denominator}')
print('q3_decimal=', repr(float(q3)))
print('robust_eventual_hit_upper_from_this_entrance=', f'{hit_upper3.numerator}/{hit_upper3.denominator}')
print('hit_upper_decimal=', repr(float(hit_upper3)))
print('hit_upper_lt_63_over_64_exact=', hit_upper3 < Fraction(63,64))
print('q7_gt_1_over_64_exact=', vals[6] > Fraction(1,64))
print('q8_lt_1_over_64_exact=', vals[7] < Fraction(1,64))
print('first_width_1_to_8_with_q_below_1_over_64=8')
print('log10_q3=', repr(log10(q3.numerator)-log10(q3.denominator)))
print('log10_q8=', repr(log10(vals[7].numerator)-log10(vals[7].denominator)))
