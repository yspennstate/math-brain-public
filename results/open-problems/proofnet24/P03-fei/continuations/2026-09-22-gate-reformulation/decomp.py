"""Classify k-input gates: DEGENERATE (independent of some input), READONCE (a formula over 2-input gates with
each input used once), GENUINE (neither).  Only GENUINE gates impose a constraint that the arity-2 inequality
does not already imply, so "does a larger fan-in need a larger constant?" is a question about them alone."""
import sys, json

def classify(k):
    n = 1 << k; FULL = (1 << n) - 1
    tab = {}
    for i in range(k):
        a = sum(1 << x for x in range(n) if (x >> i) & 1)
        tab[1 << i] = {a, (~a) & FULL}
    for size in range(2, k + 1):
        for s in range(1, 1 << k):
            if bin(s).count("1") != size:
                continue
            acc = set(); a = (s - 1) & s
            while a:
                b = s ^ a
                if a in tab and b in tab and a < b:
                    for ta in tab[a]:
                        for tb in tab[b]:
                            for t in (ta & tb, ta | tb):
                                acc.add(t); acc.add((~t) & FULL)
                a = (a - 1) & s
            if acc:
                tab[s] = acc
    RO = tab.get((1 << k) - 1, set())
    def degenerate(tt):
        for i in range(k):
            if all((((tt >> x) & 1) == ((tt >> (x ^ (1 << i))) & 1)) for x in range(n)):
                return True
        return False
    return RO, degenerate

if __name__ == "__main__":
    k = int(sys.argv[1]); src = sys.argv[2]
    RO, degenerate = classify(k)
    rows = json.load(open(src, encoding="utf-8"))
    cats = {"DEGENERATE": [], "READONCE": [], "GENUINE": []}
    for D, tt, ps in rows:
        key = "DEGENERATE" if degenerate(tt) else ("READONCE" if tt in RO else "GENUINE")
        cats[key].append((D, tt, ps))
    print("arity %d: %d read-once truth tables out of %d; %d rows from %s" % (k, len(RO), 1 << (1 << k), len(rows), src))
    for name in ("DEGENERATE", "READONCE", "GENUINE"):
        v = cats[name]
        print("  %-11s %6d rows   worst D = %s" % (name, len(v), ("%+.8f" % v[0][0]) if v else "none in this list"))
    g = cats["GENUINE"]
    print("  ten worst GENUINE gates (if any):")
    for D, tt, ps in g[:10]:
        print("     %+.8f  tt=%-8d p=%s" % (D, tt, ["%.5f" % x for x in ps]))
