# ap_9ck against ap_9c and k33c: same inputs, generators and classes as ap_9c; every k33c class is a union of ap_9ck
# classes (so every k33c function is an ap_9ck function); the edge list is the k33c one.
# usage: python3 test_ap9ck.py CODEDIR
import sys
sys.path.insert(0, sys.argv[1])
import sym_search as S

m1, g1, e1 = S.struct("ap_9c")
m2, g2, e2 = S.struct("ap_9ck")
m3, g3, e3 = S.struct("k33c")
print("same m and generators as ap_9c:", m1 == m2 and [list(a) for a in g1] == [list(b) for b in g2])
print("edge list equals k33c:", [tuple(x) for x in e2] == [tuple(x) for x in e3], "ap_9c edges:", e1)
r2, c2, s2 = S.orbits(m2, g2)
r3, c3, s3 = S.orbits(m3, g3)
print("classes ap_9ck %d k33c %d" % (len(r2), len(r3)))
# c2[x], c3[x]: class index of input x.  k33c classes must be unions of ap_9ck classes.
img = {}
ok = True
for x in range(1 << m2):
    a, b = int(c2[x]), int(c3[x])
    if img.setdefault(a, b) != b:
        ok = False; break
print("every ap_9ck class lies in one k33c class:", ok, "classes mapped", len(img))
