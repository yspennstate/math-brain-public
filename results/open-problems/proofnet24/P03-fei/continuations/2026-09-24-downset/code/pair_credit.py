"""One pair of the biased restriction step, erasure + Jensen-Shannon - credit, against the normalised ratio.

For a coordinate of bias q (sigma^2 = 4q(1-q), tau = sqrt(q/(1-q))) a pair (a, d) of biased coefficients contributes
E(a^2, d^2) + J_q(a, d) = phi(a^2) + phi(d^2) - (1-q) phi((a - tau d)^2) - q phi((a + d/tau)^2), homogeneous of degree 2,
so it equals d^2 Phi_q(s) with s = a/d. The claim tested:
    Phi_q(s) - log2(1/sigma^2) <= C0 + log2(1 + sigma^2 s^2)   for all real s and q in (0, 1),
i.e. the credit log2(1/sigma^2) d^2 pays the Jensen-Shannon part and turns the pair ratio s^2 into sigma^2 s^2.
Printed: the sup of the left minus log2(1 + sigma^2 s^2) over a log grid in q and s (both signs), mpmath 80 digits.
"""
import mpmath as mp
import functools

print = functools.partial(print, flush=True)
mp.mp.dps = 80


def phi(p):
    return mp.mpf(0) if p == 0 else -p * mp.log(p, 2)


def gap(q, s):
    q = mp.mpf(q); s = mp.mpf(s)
    tau = mp.sqrt(q / (1 - q))
    sig2 = 4 * q * (1 - q)
    Phi = phi(s * s) + phi(mp.mpf(1)) - (1 - q) * phi((s - tau) ** 2) - q * phi((s + 1 / tau) ** 2)
    return Phi - mp.log(1 / sig2, 2) - mp.log(1 + sig2 * s * s, 2)


def main():
    qs = [mp.mpf(10) ** (-e) for e in (1, 2, 3, 4, 6, 8, 10, 12, 16)] + [mp.mpf(x) for x in ('0.2', '0.3', '0.4', '0.45', '0.49', '0.5')]
    qs += [1 - x for x in qs if x < mp.mpf('0.5')]
    best = (-mp.inf, None, None)
    for q in qs:
        bq = (-mp.inf, None)
        for e in [x / mp.mpf(8) for x in range(-160, 161)]:
            for sgn in (1, -1):
                s = sgn * mp.mpf(10) ** e
                g = gap(q, s)
                if g > bq[0]:
                    bq = (g, s)
        # refine around the best s
        g0, s0 = bq
        lo, hi = s0 / 3, s0 * 3
        if lo > hi:
            lo, hi = hi, lo
        f = lambda x: -gap(q, x)
        for _ in range(60):
            m1 = lo + (hi - lo) / 3; m2 = hi - (hi - lo) / 3
            if f(m1) < f(m2):
                hi = m2
            else:
                lo = m1
        sr = (lo + hi) / 2
        gr = gap(q, sr)
        if gr > g0:
            bq = (gr, sr)
        print(f"q = {mp.nstr(q, 6):>12}: sup_s gap = {mp.nstr(bq[0], 10)} at s = {mp.nstr(bq[1], 6)}")
        if bq[0] > best[0]:
            best = (bq[0], q, bq[1])
    print(f"overall sup = {mp.nstr(best[0], 12)} at q = {mp.nstr(best[1], 6)}, s = {mp.nstr(best[2], 6)}")
    print(f"reference: log2(e) + 2/ln 2 = {mp.nstr(mp.log(mp.e, 2) + 2 / mp.log(2), 12)}")


if __name__ == "__main__":
    main()
