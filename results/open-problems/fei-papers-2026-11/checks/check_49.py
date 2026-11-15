import sys
sys.argv = ["x", "18"]
exec(open("check_grammar8.py").read().split("# coverage against")[0].replace("print(r,", "0 and print(r,"))
exec(open("check_mid8.py").read().split("# ---------- 1.")[0])
from math import factorial
# normalized volumes
allv = [(r, v) for r in range(2, 13) for v in vols[r]]
print("distinct reduced (r,vol) 2..12:", len(allv), "all even integral:", all(((v*factorial(r+1)).denominator == 1 and (v*factorial(r+1)).numerator % 2 == 0) for r, v in allv))
allst = [(r, pint(p)) for r in range(2, 13) for p, n in S[r]]
print("all states incl nests 2..12:", len(allst), "distinct (r,vol):", len(set(allst)), "even integral:", all(((v*factorial(r+1)).denominator == 1 and (v*factorial(r+1)).numerator % 2 == 0) for r, v in set(allst)))
for r in range(5, 17):
    print(r, "top3", [str(x) for x in sorted(vols[r], reverse=True)[:3]])
# Hankel parity-mixing subclass: w_r odd only
S2 = {0: set()}; hv = {}
for r in range(1, 19):
    st = set()
    if r >= 3 and r % 2 == 1:
        st.add((fw(r), False))
    for p, _ in S2.get(r - 1, ()):
        st.add(((pint(p),), True))
    for a in range(1, r):
        for p, na in S2[a]:
            for q, nb in S2[r - a]:
                st.add((pmul(p, q), False))
    S2[r] = st
    red = {pint(p) for p, n in st if not n}
    hv[r] = max(red) if red else None
print("Hankel parity-mixing grammar maxima", {r: str(v) for r, v in hv.items()})
# named values
def wv(word): return pint(word)
f2, f3, f4 = fw(2), fw(3), fw(4)
c23 = (F(2,3),)
print("abab cdcd efgefg", pint(pmul(pmul(f2, f2), f3)), "want 13/56")
print("abcabc dede fghfgh", pint(pmul(pmul(f3, f2), f3)), "want 166/945")
print("abcdbcda efghefgh", pint(pmul((pint(f3),), f4)), "want 1/5")
# exhaustive counts
def reduced(pm):
    n = len(pm); return all(pm[i] != (i + 1) % n for i in range(n))
for n in (10, 12, 14):
    d = json.load(open(f"{R}/data/volumes_T{n}.json"))
    red = {k: v for k, v in d["orbits"].items() if reduced(json.loads(k))}
    mx = max(F(v["volume"]) for v in red.values())
    at = [k for k, v in red.items() if F(v["volume"]) == mx]
    print(n, "reduced labelled", sum(v["size"] for v in red.values()), "orbits", len(red), "max", mx, "orbits at max", len(at))
