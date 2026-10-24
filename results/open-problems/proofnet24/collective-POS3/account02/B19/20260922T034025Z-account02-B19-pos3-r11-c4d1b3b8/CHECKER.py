from fractions import Fraction
from itertools import combinations

NAMES = ("d","a","b","r1","r2","u")
COVERS = (("d","a"),("d","r1"),("r1","r2"),("r2","u"),("b","u"))

def closure_preds(extra=()):
    pred = {x:set() for x in NAMES}
    for x,y in COVERS + tuple(extra):
        pred[y].add(x)
    changed = True
    while changed:
        changed = False
        for y in NAMES:
            q = set(pred[y])
            for x in tuple(q):
                q |= pred[x]
            if q != pred[y]:
                pred[y] = q
                changed = True
    return pred

def extensions(extra=()):
    pred = closure_preds(extra)
    out = []
    def rec(done, word):
        if len(word) == len(NAMES):
            out.append(tuple(word))
            return
        for x in NAMES:
            if x not in done and pred[x] <= done:
                rec(done | {x}, word + [x])
    rec(set(), [])
    return pred, out

def prob(exts, x, y):
    return Fraction(sum(L.index(x) < L.index(y) for L in exts), len(exts))

pred, exts = extensions()
assert len(exts) == 19

# Width is exactly 3: explicit 3-antichain, and the three chains below cover P.
assert all(x not in pred[y] and y not in pred[x] for x,y in combinations(("a","r1","b"),2))
chains = (("d","a"), ("r1","r2"), ("b","u"))
covered = set(sum((list(c) for c in chains), []))
assert covered == set(NAMES)
for chain in chains:
    for x,y in zip(chain, chain[1:]):
        assert x in pred[y]

expected = {
    ("d","b"): Fraction(15,19),
    ("a","b"): Fraction(6,19),
    ("a","r1"): Fraction(5,19),
    ("a","r2"): Fraction(10,19),
    ("a","u"): Fraction(15,19),
    ("b","r1"): Fraction(9,19),
    ("b","r2"): Fraction(14,19),
}
actual = {}
for i,x in enumerate(NAMES):
    for y in NAMES[i+1:]:
        if x in pred[y] or y in pred[x]:
            continue
        actual[(x,y)] = prob(exts,x,y)
assert actual == expected

# Current majority-late strict-corridor local geometry.
assert pred["b"] < pred["a"] and pred["a"] - pred["b"] == {"d"}
assert prob(exts,"a","b") < Fraction(1,3)
assert prob(exts,"d","b") > Fraction(2,3)
assert prob(exts,"a","u") > Fraction(2,3)
assert "b" in pred["u"] and "a" not in pred["u"] and "u" not in pred["a"]

# Exact two-child conditioning on d || b.
pred_plus, plus = extensions((("d","b"),))
pred_minus, minus = extensions((("b","d"),))
assert len(plus) == 15 and len(minus) == 4
assert set(plus).isdisjoint(set(minus))
assert set(plus) | set(minus) == set(exts)
assert pred_plus["a"] == pred_plus["b"] == {"d"}
assert prob(plus,"a","b") == Fraction(2,5)
assert all(L.index("b") < L.index("a") for L in minus)
gamma = Fraction(len(plus),len(exts))
assert gamma == Fraction(15,19)
assert prob(exts,"a","b") == gamma * prob(plus,"a","b")

print("POS3_MAJORITY_LATE_CONDITIONING_TRAP_PASS")
print("extensions(P)=19 extensions(P+)=15 extensions(P-)=4")
print("width=3 witness={a,r1,b}; chain_cover=(d<a),(r1<r2),(b<u)")
print("Pred(b)=empty Pred(a)={d}; D={d}")
print("P(a<b)=6/19 < 1/3")
print("P(d<b)=15/19 > 2/3")
print("P(a<u)=15/19 > 2/3")
print("P+(a<b)=2/5 in [1/3,2/3]")
print("Law(P)=15/19 Law(P+) + 4/19 Law(P-); P- forces b<a")
print("ALL_INCOMPARABLE_PROBABILITIES")
for k in sorted(actual):
    print(f"{k[0]}<{k[1]} : {actual[k].numerator}/{actual[k].denominator}")
