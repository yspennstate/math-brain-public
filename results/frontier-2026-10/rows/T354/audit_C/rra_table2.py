"""Intercept test on rra_runs.txt: gap(d) = exact - prediction at the same beta2 (the K-form); fit gap = g0 + g1 d on
beta2 0.9995 and 0.999. The prediction is right to this order when g0 = 0 (gap/d flat); a wrong O(1) term leaves g0 != 0."""
import re, collections
rows = collections.defaultdict(dict)
pat = re.compile(r"RRA eps (\S+) a (\[.*?\]) b .*? beta1 (\S+) beta2 (\S+) nodes (\d+):.*?\(x\*/x0-1\)/d (\S+)\s+guess (\S+)\s+withr1 (\S+)")
for line in open("rra_runs.txt", encoding="utf-8"):
    m = pat.search(line)
    if m:
        eps, a, b1, b2, nodes, val, guess, w = m.groups()
        if int(nodes) == 160:
            rows[(a, float(eps), float(b1))][float(b2)] = (float(val), float(guess), float(w))
print("| a | eps | beta1 | withr1 limit | g0 vs withr1 | g1 vs withr1 | g0 vs guess | gap/d vs guess at 0.9995 / 0.999 / 0.998 |")
print("|---|---|---|---|---|---|---|---|")
for key in sorted(rows):
    r = rows[key]
    d1, d2 = 0.0005, 0.001
    def fit(i):
        G1, G2 = r[1 - d1][0] - r[1 - d1][i], r[1 - d2][0] - r[1 - d2][i]
        g1 = (G2 - G1) / (d2 - d1)
        return G1 - g1 * d1, g1
    w0, w1 = fit(2)
    q0, _ = fit(1)
    gg = " / ".join("%.1f" % ((r[b][0] - r[b][1]) / (1 - b)) for b in sorted(r, reverse=True))
    print("| %s | %g | %g | %.6f | %+.1e | %.2f | %+.1e | %s |" % (key[0], key[1], key[2], r[1 - d1][2], w0, w1, q0, gg))

print()
print("three-point fit gap = g0 + g1 d + g2 d^2 (beta2 0.9995, 0.999, 0.998), against withr1:")
import numpy as np
for key in sorted(rows):
    r = rows[key]
    ds = np.array([0.0005, 0.001, 0.002])
    G = np.array([r[1 - d][0] - r[1 - d][2] for d in ds])
    g0, g1, g2 = np.linalg.solve(np.vander(ds, 3, increasing=True), G)
    print("  %s eps %g beta1 %g: g0 %+.1e g1 %.3f g2 %.1f" % (key[0], key[1], key[2], g0, g1, g2))
