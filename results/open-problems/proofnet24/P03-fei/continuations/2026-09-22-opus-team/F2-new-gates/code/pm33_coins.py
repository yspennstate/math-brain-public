"""Rebuild Numaro's balanced 18-variable g from a two-line description and check the published SHA-256.

Core variables x_0..x_8 are the edges of K_{3,3}: variable i = 3r + c is the edge between left vertex r and right
vertex c.  For a point p = (r, c) let cross(p) = {edges at r} u {edges at c} (5 edges; no perfect matching).
    g(x, y) = TRUE  iff  x contains a perfect matching of K_{3,3},
                    or   x in {cross(p), cross(p) minus the edge p} and y_p = 1   (one coin y_p per point p).
Encoding of the published table: value -1 = TRUE, entry index = x + 512*y, coin j <-> point p = ORDER[j]."""
import itertools, hashlib, sys
import numpy as np

EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
ORDER = [0, 3, 8, 4, 1, 7, 5, 2, 6]          # coin j acts on the cross at point ORDER[j] (i = 3r + c)


def has_pm(x):
    return any(all((x >> (3 * r + s[r])) & 1 for r in range(3)) for s in itertools.permutations(range(3)))


def cross(p):
    r, c = divmod(p, 3)
    return sum(1 << (3 * r + j) for j in range(3)) | sum(1 << (3 * i + c) for i in range(3))


def build():
    T = np.empty((512, 512), dtype=np.int64)
    sites = {}
    for j, p in enumerate(ORDER):
        X = cross(p)
        sites[X] = j
        sites[X ^ (1 << p)] = j
    for y in range(512):
        for x in range(512):
            if has_pm(x):
                T[y, x] = -1
            elif x in sites:
                T[y, x] = -1 if (y >> sites[x]) & 1 else 1
            else:
                T[y, x] = 1
    return T.ravel()


if __name__ == "__main__":
    tab = build()
    sha = hashlib.sha256(",".join(map(str, tab.tolist())).encode()).hexdigest()
    print("sha256 =", sha)
    print("matches the published Numaro table:", sha == EXPECTED_SHA)
    if len(sys.argv) > 1:
        ref = np.load(sys.argv[1]).astype(np.int64)
        print("equal to the stored table:", bool(np.array_equal(ref, tab)))
