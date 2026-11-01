from fractions import Fraction

# Exact self-check for P01-P79.  This is not the proof.
# Free-group letters: 1=s1, -1=s1^-1, 2=s2, -2=s2^-1.

def reduce_word(w):
    st = []
    for x in w:
        if st and st[-1] == -x:
            st.pop()
        else:
            st.append(x)
    return tuple(st)


def mul_word(a, b):
    return reduce_word(a + b)


def inv_word(a):
    return tuple(-x for x in reversed(a))


def exp_sum(w):
    return (
        sum(1 if x == 1 else -1 if x == -1 else 0 for x in w),
        sum(1 if x == 2 else -1 if x == -2 else 0 for x in w),
    )


# Lamplighter element = (finite set of toggled lamps, free word).
# Multiplication: (L,w)(M,v)=(L xor w.M, wv).
def translate_lamps(w, lamps):
    return frozenset(mul_word(w, x) for x in lamps)


def lamp_mul(g, h):
    L, w = g
    M, v = h
    return (frozenset(L.symmetric_difference(translate_lamps(w, M))), mul_word(w, v))


e = ()
a = (frozenset({e}), e)
w = reduce_word((1, 1, 2, 2, 2))
wi = inv_word(w)
W = (frozenset(), w)
Wi = (frozenset(), wi)

aw = lamp_mul(a, W)
wa = lamp_mul(W, a)
awi = lamp_mul(a, Wi)
wia = lamp_mul(Wi, a)

assert exp_sum(w) == (2, 3)
assert aw != wa
assert awi != wia
# Terms with quotient word w cannot cancel terms with quotient word w^-1.
assert all(x != y for x in (aw, wa) for y in (awi, wia))

# g=w^-1 a.  Its quotient is the nontrivial free word w^-1.
g = lamp_mul(Wi, a)
assert g[1] == wi and wi

# Finite exact sanity check of the projection argument used in the written proof.
cur = (frozenset(), e)
projs = []
for n in range(1, 11):
    cur = lamp_mul(cur, g)
    projs.append(cur[1])
assert len(set(projs)) == 10
assert all(exp_sum(projs[n - 1]) == (-2 * n, -3 * n) for n in range(1, 11))

# For |z|=1, min |1+r z|^2=(1-r)^2.
for r in (Fraction(1, 2), Fraction(1), Fraction(2)):
    minsq = (1 - r) ** 2
    if r == 1:
        assert minsq == 0
    else:
        assert minsq > 0

print("P79 TWO-OPERATOR EXACT SELF-CHECK")
print(f"reduced word w={w}")
print(f"exponent sums={exp_sum(w)}")
print(f"a*w != w*a: {aw != wa}")
print(f"a*w^-1 != w^-1*a: {awi != wia}")
print(f"quotient(g)=w^-1={g[1]}")
print(f"sample g^n quotient exponent sums n=1..10={[exp_sum(x) for x in projs]}")
print(f"r=1/2 min |1+r z|^2={(1-Fraction(1,2))**2}")
print(f"r=1 critical min |1+r z|^2={(1-Fraction(1))**2}")
print(f"r=2 min |1+r z|^2={(1-Fraction(2))**2}")
print("ALL EXACT SELF-CHECK ASSERTIONS PASSED")
