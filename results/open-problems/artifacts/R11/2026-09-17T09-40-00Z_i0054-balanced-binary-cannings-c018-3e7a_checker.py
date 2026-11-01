from fractions import Fraction

CHECKS = 0

def check(cond, msg):
    global CHECKS
    if not cond:
        raise AssertionError(msg)
    CHECKS += 1

def matchings(items, odd_singleton=False):
    items = tuple(items)
    if not items:
        yield ()
        return
    if odd_singleton:
        for s in items:
            rest = tuple(x for x in items if x != s)
            for m in matchings(rest, False):
                yield ((s,),) + m
        return
    first = items[0]
    for j in range(1, len(items)):
        second = items[j]
        rest = items[1:j] + items[j+1:]
        for m in matchings(rest, False):
            yield ((first, second),) + m

def contains_pair(m, a, b):
    target = {a,b}
    return any(len(block)==2 and set(block)==target for block in m)

def p_h_fixed_pairs(N, h):
    den = 1
    if N % 2 == 0:
        for t in range(h):
            den *= N - (2*t + 1)
    else:
        for t in range(h):
            den *= N - 2*t
    return Fraction(1, den)

def cN(N):
    return Fraction(1, N-1 if N % 2 == 0 else N)

# 1. Exact matching/near-matching probabilities, N=3,...,9.
for N in range(3,10):
    ms = list(matchings(range(N), odd_singleton=(N%2==1)))
    for h in range(1, N//2 + 1):
        fav = sum(all(contains_pair(m, 2*t, 2*t+1) for t in range(h)) for m in ms)
        check(Fraction(fav, len(ms)) == p_h_fixed_pairs(N,h),
              f"matching formula failed N={N}, h={h}")

# 2. Two specified pair-collisions are O(c_N^2), with sharp checked ratio 3.
max_ratio = Fraction(0)
for N in range(4,101):
    p2 = p_h_fixed_pairs(N,2)
    c = cN(N)
    ratio = p2/(c*c)
    max_ratio = max(max_ratio, ratio)
    check(ratio <= 3, f"pair-collision ratio > 3 at N={N}")

# 3. Deterministic family multiset has total N and maximum family size 2.
for N in range(3,101):
    if N % 2 == 0:
        fam = [2]*(N//2) + [0]*(N//2)
    else:
        fam = [2]*((N-1)//2) + [1] + [0]*((N-1)//2)
    check(sum(fam)==N and max(fam)==2,
          f"family multiset failed N={N}")

# 4. Exact N=3 first-visible-root witness.
N = 3
delta = Fraction(1,3)
c = cN(3)
u = delta*c/2
a = 1-u
L = c*a*a/(1-(1-c)*a*a)
p_none = a**3 * L
p_deg3 = 3*u*u*a + u**3 + 2*u*a*a*(1-L)
p_deg2 = 1-p_none-p_deg3
cond3 = p_deg3/(1-p_none)
cond2 = p_deg2/(1-p_none)

check(c == Fraction(1,3), "N=3 c")
check(delta == Fraction(1,3), "N=3 delta")
check(u == Fraction(1,18), "N=3 mark probability")
check(L == Fraction(289,394), "N=3 two-lineage no-mark transform")
check(p_none == Fraction(1419857,2297808), "N=3 no visible refinement")
check(p_deg2 == Fraction(265591,765936), "N=3 raw degree 2")
check(p_deg3 == Fraction(40589,1148904), "N=3 raw degree 3")
check(cond3 == Fraction(81178,877951), "N=3 conditional degree 3")
check(cond2 == Fraction(796773,877951), "N=3 conditional degree 2")

# 5. Frozen-convention comparison with retained N=3 witnesses C001--C017.
previous = [
    Fraction(0), Fraction(1,10), Fraction(1,22), Fraction(1,6),
    Fraction(1,728), Fraction(1,7), Fraction(1,71), Fraction(1,71),
    Fraction(0), Fraction(0), Fraction(2,105),
    Fraction(21521,4909716), Fraction(35,1296), Fraction(14,2201),
    Fraction(2,17), Fraction(40589,352998), Fraction(70135,515173),
]
for idx, old in enumerate(previous, start=1):
    check(cond3 != old, f"C018 witness collides with retained C{idx:03d} witness")

check(p_none+p_deg2+p_deg3 == 1, "raw N=3 law does not sum to one")

print("R11 I0054 C018 balanced-binary Cannings exact checker")
print("matching-formula checks: PASS")
print("higher-collision O(c_N^2) checks through N=100: PASS")
print("family size <=2 / no triple ancestral merger in one generation: PASS")
print(f"N=3 c_N={c} delta_N={delta} mark_u={u}")
print(f"N=3 P(no visible refinement)={p_none}")
print(f"N=3 P(raw degree-2)={p_deg2}")
print(f"N=3 P(raw degree-3)={p_deg3}")
print(f"N=3 P(first visible root degree=3)={cond3}")
print(f"N=3 P(first visible root degree=2)={cond2}")
print("comparison against retained C001-C017 N=3 witnesses: PASS")
print(f"max checked p(two specified pair collisions)/c_N^2 through N=100 = {max_ratio}")
print(f"TOTAL_EXACT_CHECKS={CHECKS}")
print("ALL_EXACT_CHECKS_PASS")
