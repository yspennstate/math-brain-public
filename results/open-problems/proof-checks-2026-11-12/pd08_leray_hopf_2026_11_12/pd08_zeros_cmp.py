# Compares the roots in the authors' data/bessel_zeros.mat (dumped to text by pd08_mat_dump.py)
# with our own roots of the eigenvalue equations (6.3), (6.4), family by family and l by l.
# usage: python pd08_zeros_cmp.py <prefix of the text dumps>
import sys, math
import numpy as np
from scipy.special import jv, jvp
from scipy.optimize import brentq

def load(p):
    rows = {}
    for line in open(p):
        w = line.split()
        rows[int(w[0])] = [float(x) for x in w[1:]]
    return rows

def fz1(x, nu):
    return x * jvp(nu, x) - 0.5 * jv(nu, x)
def fy1(x, nu, a, b, c):
    J = jv(nu, x)
    return (x * x - a) * (x * jvp(nu, x) - 1.5 * J) + (x * x - b) * (x * x - c) * J
def args_of(fam, l):
    nu = l + 0.5
    if fam == "Z":
        return fz1, (nu,)
    return fy1, (nu, l * (l - 1) * (l + 2), l * (l - 1), (l - 1) * (l + 2))

XMAX = 100.0
R0 = 32.0
h = 0.004
r = np.arange(0.05, XMAX, h)
def our_roots(fam, l):
    f, a = args_of(fam, l)
    v = f(r, *a)
    idx = np.nonzero(np.sign(v[1:]) * np.sign(v[:-1]) < 0)[0]
    return [brentq(f, r[i], r[i + 1], args=a, xtol=1e-12) for i in idx]

pre = sys.argv[1]
theirs = {"Y": load(pre + "_Y_zeros.txt"), "Z": load(pre + "_Z_zeros.txt")}
print("rows in the file: Y %d, Z %d" % (len(theirs["Y"]), len(theirs["Z"])))

# which l does row i hold?  try l = i + 1 and l = i on the rows that have roots
for fam in "YZ":
    for off in (1, 0):
        good = tot = 0
        for i, xs in theirs[fam].items():
            l = i + off
            if l < 1 or not xs:
                continue
            f, a = args_of(fam, l)
            for x in xs[:3]:
                tot += 1
                good += f(x - 1e-6, *a) * f(x + 1e-6, *a) < 0
        print("  family %s, row i read as l = i + %d: %d of %d sampled entries are roots" % (fam, off, good, tot))

tot_file = tot_ours = 0
worst = 0.0
bad_rows = []
cnt = {"Y": {}, "Z": {}}
maxfile = 0.0
for fam in "YZ":
    for i in sorted(theirs[fam]):
        l = i + 1
        xs = sorted(theirs[fam][i])
        ours = our_roots(fam, l)
        cnt[fam][l] = len(ours)
        tot_file += len(xs); tot_ours += len(ours)
        if xs:
            maxfile = max(maxfile, xs[-1])
        if len(xs) != len(ours):
            bad_rows.append((fam, l, len(xs), len(ours)))
            continue
        for x, y in zip(xs, ours):
            worst = max(worst, abs(x - y))
print("entries in the file %d, our roots below %.0f for the same l: %d" % (tot_file, XMAX, tot_ours))
print("largest entry in the file %.6f (scaled eigenvalue %.6f); cutoff 100 is scaled %.6f" % (maxfile, (maxfile / R0) ** 2, (XMAX / R0) ** 2))
print("rows where the counts differ: %d %s" % (len(bad_rows), bad_rows[:8]))
print("largest |their root - our root| over matched rows: %.3e" % worst)
lmax = max(l for fam in "YZ" for l, n in cnt[fam].items() if n)
extra = sum(len(our_roots(fam, l)) for fam in "YZ" for l in range(len(theirs[fam]) + 1, len(theirs[fam]) + 4))
print("largest l with a root below 100: %d; our roots below 100 for the three l beyond the file's rows: %d" % (lmax, extra))
Ye = sum(n for l, n in cnt["Y"].items() if l % 2 == 0); Yo = sum(n for l, n in cnt["Y"].items() if l % 2 == 1)
Ze = sum(n for l, n in cnt["Z"].items() if l % 2 == 0); Zo = sum(n for l, n in cnt["Z"].items() if l % 2 == 1)
print("below 100: Y even l %d, Y odd l %d, Z even l %d, Z odd l %d" % (Ye, Yo, Ze, Zo))
print("class of U (Y even l, Z odd l): %d   paper N = 1257" % (Ye + Zo))
print("class of v (Y odd l, Z even l): %d, with the zero mode %d   paper N = 1260" % (Yo + Ze, Yo + Ze + 1))
