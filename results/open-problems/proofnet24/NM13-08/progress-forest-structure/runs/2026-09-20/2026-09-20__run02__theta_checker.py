#!/usr/bin/env python3
from itertools import combinations

def enum_counts(n, edges, terminals=None):
    m = len(edges)
    Z = 0
    Ze = [0]*m
    Zef = [[0]*m for _ in range(m)]
    D = C = 0
    for mask in range(1 << m):
        parent = list(range(n))
        rank = [0]*n
        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a
        def union(a,b):
            a,b = find(a),find(b)
            if a == b:
                return False
            if rank[a] < rank[b]:
                a,b = b,a
            parent[b] = a
            if rank[a] == rank[b]:
                rank[a] += 1
            return True
        bits = []
        ok = True
        for i,(u,v) in enumerate(edges):
            if (mask >> i) & 1:
                if not union(u,v):
                    ok = False
                    break
                bits.append(i)
        if not ok:
            continue
        Z += 1
        for i in bits:
            Ze[i] += 1
        for a in range(len(bits)):
            for b in range(a+1, len(bits)):
                i,j = bits[a],bits[b]
                Zef[i][j] += 1
                Zef[j][i] += 1
        if terminals is not None:
            if find(terminals[0]) == find(terminals[1]):
                C += 1
            else:
                D += 1
    return {"Z":Z,"Ze":Ze,"Zef":Zef,"D":D,"C":C}

def rayleigh_summary(st):
    vals = []
    Z,Ze,Zef = st["Z"],st["Ze"],st["Zef"]
    for i in range(len(Ze)):
        for j in range(i+1,len(Ze)):
            vals.append((Ze[i]*Ze[j]-Z*Zef[i][j],i,j))
    return min(vals), sum(v[0] < 0 for v in vals), len(vals)

def wheel4_edges():
    return [(0,1),(0,2),(0,3),(0,4),(1,2),(2,3),(3,4),(4,1)]

# Transparent theta gadget for ell=2: r=2^2-1=3 internally disjoint 2-edge paths.
A_edges = [(0,2),(2,1),(0,3),(3,1),(0,4),(4,1)]
Ast = enum_counts(5, A_edges, terminals=(0,1))
assert (Ast["D"],Ast["C"],Ast["Z"]) == (27,27,54)
print("A_theta_l2 D=%d C=%d Z=%d" % (Ast["D"],Ast["C"],Ast["Z"]))

# Completion by the port edge g=01 is series-parallel and is checked exactly at unit weights.
Kst = enum_counts(5, A_edges+[(0,1)])
kmin,kneg,kpairs = rayleigh_summary(Kst)
assert Kst["Z"] == 81 and kneg == 0
print("K_theta_l2 Z=%d pair_count=%d negative=%d min_delta=%d" %
      (Kst["Z"],kpairs,kneg,kmin[0]))

# Core wheel W4 and one theta substitution.
W = wheel4_edges()
Wst = enum_counts(5,W)
wmin,wneg,wpairs = rayleigh_summary(Wst)
assert Wst["Z"] == 134 and wneg == 0
print("W4 Z=%d pair_count=%d negative=%d min_delta=%d" %
      (Wst["Z"],wpairs,wneg,wmin[0]))

# Replace spoke (0,1) by three 2-edge paths through fresh vertices 5,6,7.
G_edges = W[1:] + [(0,5),(5,1),(0,6),(6,1),(0,7),(7,1)]
Gst = enum_counts(8,G_edges)
gmin,gneg,gpairs = rayleigh_summary(Gst)
assert Gst["Z"] == Ast["D"] * Wst["Z"] == 3618
assert gneg == 0
print("W4_theta_l2 n=8 m=13 Z=%d pair_count=%d negative=%d min_delta=%d" %
      (Gst["Z"],gpairs,gneg,gmin[0]))
print("partition_scale Z_G=%d D_A*Z_W4=%d" % (Gst["Z"],Ast["D"]*Wst["Z"]))

# Core-core Rayleigh differences must scale by D_A^2=729.
for a in range(7):
    for b in range(a+1,7):
        oldi,oldj = a+1,b+1
        dW = Wst["Ze"][oldi]*Wst["Ze"][oldj] - Wst["Z"]*Wst["Zef"][oldi][oldj]
        dG = Gst["Ze"][a]*Gst["Ze"][b] - Gst["Z"]*Gst["Zef"][a][b]
        assert dG == Ast["D"]**2 * dW
print("core_core_scale_exact=True factor=%d" % (Ast["D"]**2))

# Closed-form transparent theta counts for ell=2,...,7:
# one ell-edge path has (D,C)=(2^ell-1,1); r=2^ell-1 parallel copies have
# D=(2^ell-1)^r and C=r(2^ell-1)^(r-1)=D.
for ell in range(2,8):
    d = 2**ell - 1
    r = d
    D = d**r
    C = r*d**(r-1)
    assert D == C
    print("theta_formula ell=%d branches=%d transparent=True D_digits=%d" %
          (ell,r,len(str(D))))

print("ALL_EXACT_CHECKS_PASS")
