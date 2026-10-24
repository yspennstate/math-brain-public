#!/usr/bin/env python3
"""
Exact rational certificate for PROB20-07, 2026-09-16T075502Z.

Goal: exclude the remaining negative-real-part complex fixed-point
instability at coefficient floor a=1/12.

All universal branch/cap/upper-bound decisions use fractions.Fraction.
There is no floating-point arithmetic in the proof logic. Decimal output
is display-only after the exact comparisons have completed.
"""
from fractions import Fraction as F
from hashlib import sha256

A = F(1,12)
XLO = F(1,6)
XHI = F(5,9)
DLO = F(219,2000)   # strict rational weakening of sqrt(35)/54
DHI = F(1,6)
ONE = F(1,1)

assert F(35,2916) - DLO*DLO == F(36431,2916000000)
assert F(35,2916) > DLO*DLO

def add(*As):
    return (sum((x[0] for x in As), F(0)),
            sum((x[1] for x in As), F(0)))

def scale(c, X):
    return (c*X[0], c*X[1]) if c >= 0 else (c*X[1], c*X[0])

def sub(X, Y):
    return (X[0]-Y[1], X[1]-Y[0])

def mul(X, Y):
    vals = (X[0]*Y[0], X[0]*Y[1], X[1]*Y[0], X[1]*Y[1])
    return (min(vals), max(vals))

def sq(X):
    l,u = X
    if l <= 0 <= u:
        return (F(0), max(l*l,u*u))
    return (min(l*l,u*u), max(l*l,u*u))

def div(X, Y):
    assert Y[0] > 0
    return mul(X, (1/Y[1], 1/Y[0]))

def U(Xj, Xk):
    # U_jk = x_j/12 + (x_k-1/12)/2 + 3 x_j^2/8
    return add(scale(A,Xj),
               scale(F(1,2), sub(Xk,(A,A))),
               scale(F(3,8), sq(Xj)))

def Fcap(Ui, Vi):
    # F(u,v) = 1/6 + (9u^2 + 2u + 10v - 5)/24
    num = add(scale(9,sq(Ui)), scale(2,Ui), scale(10,Vi), (F(-5),F(-5)))
    return add((F(1,6),F(1,6)), scale(F(1,24),num))

def fmt(q):
    return f"{q.numerator}/{q.denominator}"

def evaluate(box):
    (l1,u1),(l2,u2),(ld,ud) = box
    X1 = (max(l1,XLO), min(u1,XHI))
    X2 = (max(l2,XLO), min(u2,XHI))
    if X1[0] > X1[1] or X2[0] > X2[1]:
        return ("coord", None)

    raw3 = (ONE-u1-u2, ONE-l1-l2)
    X3 = (max(raw3[0],XLO), min(raw3[1],XHI))
    if X3[0] > X3[1]:
        return ("coord", None)

    P = mul(mul(X1,X2),X3)

    caps = [Fcap(X2,X1), Fcap(X3,X2), Fcap(X1,X3)]
    if any(ld > C[1] for C in caps):
        return ("cap", None)

    ud_eff = min(ud, caps[0][1], caps[1][1], caps[2][1], DHI)
    if ld > ud_eff:
        return ("cap", None)
    D = (ld,ud_eff)

    U21 = U(X2,X1)
    U13 = U(X1,X3)
    U32 = U(X3,X2)

    D1 = add(X1, scale(-1,U21), scale(-1,U13), D)
    D2 = add(X2, scale(-1,U21), scale(-1,U32), D)
    D3 = add(X3, scale(-1,U13), scale(-1,U32), D)

    Z1 = div(D1,X1)
    Z2 = div(D2,X2)
    Z3 = div(D3,X3)

    Llow = -1 + max(A,Z1[0]) + max(A,Z2[0]) + max(A,Z3[0])
    real_sq = F(0) if Llow >= 0 else Llow*Llow
    B = real_sq + ud_eff*ud_eff/P[0]
    return ("eval", (B,Llow,ud_eff,P[0]))

def split(box):
    widths = [box[0][1]-box[0][0],
              box[1][1]-box[1][0],
              6*(box[2][1]-box[2][0])]
    k = max(range(3), key=lambda i: widths[i])
    l,u = box[k]
    m = (l+u)/2
    out = []
    for interval in ((l,m),(m,u)):
        child = list(box)
        child[k] = interval
        out.append(tuple(child))
    return out

initial = ((XLO,XHI),(XLO,XHI),(DLO,DHI))
stack = [(initial, "", 0)]
records = []
counts = {"eval":0, "coord":0, "cap":0}
nodes = 0
certified = 0
max_depth = 0
worst = F(0)
worst_path = None

while stack:
    box,path,depth = stack.pop()
    nodes += 1
    max_depth = max(max_depth, depth)
    status,data = evaluate(box)
    counts[status] += 1

    if status == "coord":
        records.append((path,"COORD",""))
        continue
    if status == "cap":
        records.append((path,"CAP",""))
        continue

    B,Llow,du,pmin = data
    if B < 1:
        certified += 1
        if B > worst:
            worst = B
            worst_path = path
        records.append((path,"BOUND",fmt(B)))
        continue

    children = split(box)
    # Push right then left so traversal/certificate order is deterministic.
    stack.append((children[1],path+"R",depth+1))
    stack.append((children[0],path+"L",depth+1))

assert nodes == 5073
assert certified == 1913
assert counts == {"eval":4449, "coord":44, "cap":580}
assert max_depth == 14
assert all(r[1] in ("COORD","CAP","BOUND") for r in records)
assert len(records) == certified + counts["coord"] + counts["cap"]
assert worst < 1

cert_text = "\n".join("\t".join(r) for r in records) + "\n"
digest = sha256(cert_text.encode("utf-8")).hexdigest()

print("ALL EXACT NEGATIVE-REAL COMPLEX-SPECTRUM BOXES CERTIFIED")
print("nodes =", nodes)
print("certified_bound_leaves =", certified)
print("coordinate_prunes =", counts["coord"])
print("circulation_cap_prunes =", counts["cap"])
print("terminal_leaves =", len(records))
print("max_depth =", max_depth)
print("worst_exact_bound =", fmt(worst))
print("worst_decimal_display =", float(worst))
print("worst_path =", worst_path)
print("certificate_sha256 =", digest)
print("rational_d_lower_square_gap =", fmt(F(35,2916)-DLO*DLO))

# Optional explicit certificate materialization when invoked with --certificate PATH.
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 3 and sys.argv[1] == "--certificate":
        with open(sys.argv[2], "w", encoding="utf-8", newline="\n") as f:
            f.write("# path\\tstatus\\texact_upper_bound_if_BOUND\n")
            f.write(cert_text)
