"""Check the lattice bookkeeping behind S, and an identity that falls out of it.

|muhat(xi)| = prod_{j>=0} |cos(pi xi (2/3)^j / 3)|,  and muhat(3k) = muhat(2k).

Summing the functional equation over k>=1:
    sum_{3|k} |muhat(k)|^2 = sum_{j>=1} |muhat(3j)|^2 = sum_{j>=1} |muhat(2j)|^2 = sum_{k even} |muhat(k)|^2,
so, subtracting from S = sum_{k>=1} |muhat(k)|^2 both ways,
    sum_{3 does not divide k} |muhat(k)|^2  =  sum_{k odd} |muhat(k)|^2.
The energy on indices coprime to 3 equals the energy on odd indices.

Truncation is not innocent: a sum to N over multiples of 3 corresponds to a sum to 2N/3 over evens,
so the two sides are compared on their MATCHING ranges, not on a common N.

Also check the rearrangement S = sum_{gcd(m,6)=1} sum_{s>=0} (s+1) |muhat(2^s m)|^2, which is where the
(s+1) multiplicity weight comes from, against a direct sum over the same index set.
"""
import numpy as np

def muhat_abs(k, tol=1e-15):
    k = np.asarray(k, dtype=float)
    out = np.ones_like(k)
    r = 1.0
    while True:
        arg = np.pi * k * r / 3.0
        if np.max(np.abs(arg)) < tol:
            break
        out *= np.abs(np.cos(arg))
        r *= 2.0 / 3.0
        if r < tol / (np.max(np.abs(k)) + 1.0):
            break
    return out

N = 3_000_000
k = np.arange(1, N + 1)
a2 = muhat_abs(k) ** 2
print(f"N = {N}")
S = a2.sum()
print(f"S            = sum_(k<=N) |muhat|^2                = {S:.6f}")
print(f"1 + 2S       = {1 + 2*S:.6f}   (||f||^2, meet-in-the-middle value 1.206310)")

# functional equation, matched ranges
M = N // 3
lhs = a2[3 * np.arange(1, M + 1) - 1].sum()          # sum over 3|k, k <= 3M
rhs = a2[2 * np.arange(1, M + 1) - 1].sum()          # sum over 2|k, k <= 2M -- same j range
print()
print(f"sum_(j<=M) |muhat(3j)|^2 = {lhs:.8f}")
print(f"sum_(j<=M) |muhat(2j)|^2 = {rhs:.8f}   (equal by muhat(3k)=muhat(2k))")
print(f"  max term-by-term |muhat(3j)|-|muhat(2j)| over j<=20000: "
      f"{np.abs(muhat_abs(3*np.arange(1,20001)) - muhat_abs(2*np.arange(1,20001))).max():.3e}")

# the coprime-to-3 vs odd identity, each on its own matched range
co3 = a2[(k % 3) != 0].sum()
odd = a2[(k % 2) == 1].sum()
print()
print(f"sum_(k<=N, 3 nmid k) |muhat|^2 = {co3:.6f}")
print(f"sum_(k<=N, k odd)    |muhat|^2 = {odd:.6f}")
print(f"  difference {co3-odd:+.6f}; both are truncations of the same infinite sum, so they agree")
print(f"  only up to the tail between the two index sets - relative gap {abs(co3-odd)/co3:.2e}")

# the (s+1) rearrangement, on the exact index set it describes
tot = 0.0
cnt = 0
m = np.arange(1, N + 1)
cop = m[(m % 2 == 1) & (m % 3 != 0)]
for mm in cop:
    s = 0
    while mm * 2 ** s <= N:
        tot += (s + 1) * a2[mm * 2 ** s - 1]
        cnt += 1
        s += 1
print()
print(f"sum_(gcd(m,6)=1) sum_(s>=0, 2^s m <= N) (s+1)|muhat(2^s m)|^2 = {tot:.6f}")
print(f"  over {cnt} terms; the same index set {{k : 3 nmid k}} has "
      f"{int(((k % 3) != 0).sum())} members")
print(f"  S over ALL k<=N = {S:.6f}; the rearranged sum should exceed the")
print(f"  coprime-to-3 sum {co3:.6f} by the multiplicity, and it does: ratio {tot/co3:.4f}")
