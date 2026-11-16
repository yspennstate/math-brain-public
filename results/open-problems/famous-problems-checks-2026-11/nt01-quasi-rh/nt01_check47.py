# Test of identity (4.7) of Lemma 4.1 through its equivalent form. Given (4.1), G(ab) = G(a)G(b)R(a,b) on the
# whole ray class group, identity (4.7), chi_a(-1) conj(G(a)) G(b) R(a,b) = G(b a^-1), is equivalent to
#     R(a, a) = chi_a(-1),
# where R(a, a) means R(a, a') for any a' in the ray class of a that is prime to a, and
# R(a, a') = chi_a'(a) / chi_a(a'). The paper fixes the modulus only as "sufficiently large"; this script tries
# several moduli M and, for each primary prime a of norm <= 200, every primary prime a' != a with a' = a (mod M)
# of norm <= 2500. A modulus is good when the ratio never depends on a' and always equals chi_a(-1).
import io, os, sys
here = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(here, "nt01_check.py"), encoding="utf-8").read()
exec(src[:src.index("TOL = 1e-8")])          # the arithmetic and the class Elt, without the main run
TOL = 1e-8

def close(x, y):
    return abs(x - y) < TOL

small = primary_primes(200)
big = primary_primes(2500)
print(f"primes a: {len(small)}; candidate primes a': {len(big)}", flush=True)
for M in (1, 2, 3, 4, 6, 9, 12, 24, 36):
    tot = ok = 0; pm = 0; a_seen = set(); a_const = 0
    for a in small:
        ea = Elt([a]); target = ea.chi((-1, 0)); vals = set()
        for b in big:
            if b == a or norm(b) == norm(a) and b == conj(a) and False:
                continue
            if (b[0] - a[0]) % M or (b[1] - a[1]) % M:
                continue
            eb = Elt([b])
            ca = eb.chi(a); cb = ea.chi(b)
            if ca == 0 or cb == 0:
                continue
            R = ca / cb
            tot += 1
            pm += 1 if (close(R, 1) or close(R, -1)) else 0
            ok += 1 if close(R, target) else 0
            vals.add(round(R.real))
            a_seen.add(a)
        if len(vals) == 1:
            a_const += 1
    print(f"  modulus {M}: pairs {tot}; R = +-1 on {pm}; R(a,a') = chi_a(-1) on {ok}; a with a constant value: {a_const} of {len(a_seen)}", flush=True)
neg = sum(1 for a in small if close(Elt([a]).chi((-1, 0)), -1))
print(f"chi_a(-1) = -1 for {neg} of the {len(small)} primes a, so the sign is exercised", flush=True)
