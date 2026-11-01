from fractions import Fraction

# m=2, critical finite-support law P(X0=0)=4/5, P(X0=2)=1/5.
# X_{n+1}=(X_n^(1)+X_n^(2)-1)_+.
dist = {0: Fraction(4, 5), 2: Fraction(1, 5)}
rows = []
for n in range(3):
    q = 1 - dist.get(0, Fraction(0))
    rows.append(q)
    if n == 2:
        break
    nxt = {}
    for a, pa in dist.items():
        for b, pb in dist.items():
            c = max(a + b - 1, 0)
            nxt[c] = nxt.get(c, Fraction(0)) + pa * pb
    dist = nxt

q0, q1, q2 = rows
assert q0 == Fraction(1, 5)
assert q1 == Fraction(9, 25)
assert q2 == Fraction(113, 625)
r0 = q1 / q0
r1 = q2 / q1
assert r0 == Fraction(9, 5)
assert r1 == Fraction(113, 225)
assert r1 < 1 < r0

for n, q in enumerate(rows):
    print(f"n={n} q={q.numerator}/{q.denominator}")
print(f"q1/q0={r0.numerator}/{r0.denominator}")
print(f"q2/q1={r1.numerator}/{r1.denominator}")
print("PASS: consecutive survival ratios are not monotone or one-sided around 1 at the first two updates.")
