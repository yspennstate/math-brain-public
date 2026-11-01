#!/usr/bin/env python3
from fractions import Fraction
from functools import lru_cache

THRESHOLD = Fraction(3753, 6250)  # 2*(3753/12500)=0.60048

def exact_square_fpp(m):
    """Exact E T((0,0),(m,m)) for iid Exp(1) edges in the finite square [0,m]^2.

    CTMC infection recursion.  If S is the infected set and b(S) is the number
    of boundary edges, the next infection occurs after Exp(b(S)); an outside
    vertex v is next with probability (# boundary edges S--v)/b(S).
    """
    verts = [(i,j) for i in range(m+1) for j in range(m+1)]
    idx = {v:k for k,v in enumerate(verts)}
    s = idx[(0,0)]
    t = idx[(m,m)]
    adj = [[] for _ in verts]
    for (i,j),k in idx.items():
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            w=(i+di,j+dj)
            if w in idx:
                adj[k].append(idx[w])

    @lru_cache(None)
    def E(mask):
        if (mask >> t) & 1:
            return Fraction(0,1)
        rates = {}
        total = 0
        for u in range(len(verts)):
            if (mask >> u) & 1:
                for v in adj[u]:
                    if not ((mask >> v) & 1):
                        rates[v] = rates.get(v,0) + 1
                        total += 1
        ans = Fraction(1,total)
        for v,r in rates.items():
            ans += Fraction(r,total) * E(mask | (1<<v))
        return ans

    val = E(1<<s)
    return val, E.cache_info().currsize

def l1_ball_count(L):
    return sum(
        1
        for x in range(-L,L+1)
        for y in range(-L,L+1)
        for z in range(-L,L+1)
        if abs(x)+abs(y)+abs(z) <= L
    )

def audit_r09_passage_l1():
    # R09 formula V_L=(4L^3+6L^2+8L+3)/3.
    checked=[]
    for L in range(1,21):
        exact=l1_ball_count(L)
        formula=(4*L**3+6*L**2+8*L+3)//3
        assert exact == formula
        checked.append((L, exact))

    # On s in [1/10,1/2], s(1-s) >= 9/100, hence
    # Psi'(s)=1/(2 sqrt(s(1-s))) <= 5/3.
    # Exact squared check:
    # (5/3)^2 * 4*(9/100) = 1.
    assert Fraction(25,9) * 4 * Fraction(9,100) == 1
    return checked

def main():
    expected = {
        1: Fraction(5,4),
        2: Fraction(30757,14400),
        3: Fraction(5675443731448268047,1935723847680000000),
    }
    print("R08 stuck recovery: exact finite square-block diagonal computation")
    print("threshold_for_gap", THRESHOLD, float(THRESHOLD))
    for m in (1,2,3):
        val,states = exact_square_fpp(m)
        assert val == expected[m]
        normalized = val / m
        assert normalized > THRESHOLD
        print("m",m,
              "E_T",val,
              "E_T_over_m",normalized,
              "decimal",float(normalized),
              "states",states,
              "beats_threshold",False)
    print("Conclusion: no m<=3 full-square independent-block certificate reaches 0.60048.")

    checked = audit_r09_passage_l1()
    print("R09-PASSAGE-L1 l1-ball formula exact checks", len(checked),
          "L_range", checked[0][0], checked[-1][0])
    print("R09-PASSAGE-L1 derivative_bound_exact", "PASS")
    print("ALL_EXACT_CHECKS_PASS")

if __name__ == "__main__":
    main()
