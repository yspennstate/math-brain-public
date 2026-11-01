"""Real negative control: inject a fault into the recursion and confirm the
brute-force comparison TRIPS. A control that cannot fail is decoration."""
import random, importlib
import ro, control

def patched_analyse_drop_h2(t):
    """FAULT: drop the h2(V) correction in the composition."""
    k = t[0]
    if k == 'const': return (float(t[1]), 0.0, 0.0)
    if k == 'lit':   return (0.5, 1.0, 0.0)
    a, b = t[1], t[2]
    pa, Ia, Ha = patched_analyse_drop_h2(a)
    pb, Ib, Hb = patched_analyse_drop_h2(b)
    if pa in (0.0,1.0) or pb in (0.0,1.0):
        return patched_analyse_drop_h2(ro.simplify(t))
    if k == 'and': p, q = pa, pb
    else:          p, q = 1-pa, 1-pb
    Ht, It_a, It_b = ro.ht_and(p, q)
    I = q*Ia + p*Ib
    H = q*Ha + p*Hb + Ht            # <-- the h2 terms removed
    out_p = p*q if k == 'and' else 1-p*q
    return (out_p, I, H)

if __name__ == '__main__':
    random.seed(11)
    worst_true = 0.0; worst_fault = 0.0; tripped = 0; total = 0
    for n in range(3, 10):
        for _ in range(30):
            t = control.rand_tree(list(range(n)))
            _, _, Hb = control.brute(t, n)
            _, _, Hr = ro.analyse(t)
            _, _, Hf = patched_analyse_drop_h2(t)
            worst_true = max(worst_true, abs(Hr-Hb))
            worst_fault = max(worst_fault, abs(Hf-Hb))
            total += 1
            if abs(Hf-Hb) > 1e-9: tripped += 1
    print("FAULT INJECTION (h2 correction removed from the composition):")
    print("  trees tested            : %d" % total)
    print("  true recursion worst err: %.3e   (must be ~0)" % worst_true)
    print("  faulted recursion worst : %.3e   (must be large)" % worst_fault)
    print("  control tripped on      : %d of %d trees" % (tripped, total))
    print("  VERDICT: %s" % ("the check CAN fail -> the pass means something"
                             if tripped > 0.5*total and worst_true < 1e-9 else "CONTROL IS VACUOUS"))
