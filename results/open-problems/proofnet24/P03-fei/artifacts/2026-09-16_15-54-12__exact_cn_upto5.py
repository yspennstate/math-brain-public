#!/usr/bin/env python3
"""Exact certificate for FEI finite optima C_n, n<=5.

Normalization:
  f:{-1,1}^n -> {-1,1}, uniform Fourier-Walsh coefficients,
  H = sum p_S log_2(1/p_S), p_S = hat f(S)^2,
  I = sum_i Pr[f(x) != f(x^i)].

The checker uses only Python integer arithmetic for all comparisons deciding the
optimum. Decimal values are printed only after the exact decision.
"""
from itertools import combinations
from math import log2


def char_sign(s, x):
    return -1 if ((s & x).bit_count() & 1) else 1


def exact_profile_from_minority(n, A):
    """Return (P,Q) encoding H/I exactly for f=1-2 1_A.

    Set N=2^n and a_S=|W_S|/2, where W_S=sum_x f(x) chi_S(x).
    Then
      P=prod_{a_S>0} a_S^(a_S^2),
      Q=sum_S |S| a_S^2,
      H/I = (K_n - 2 log_2 P)/Q,
      K_n = N^2(n-1)/2.
    """
    N = 1 << n
    half = N // 2
    k = len(A)
    aa = [half - k]
    for s in range(1, N):
        aa.append(abs(sum(char_sign(s, x) for x in A)))
    assert sum(a*a for a in aa) == N*N//4
    Q = sum(s.bit_count() * aa[s] * aa[s] for s in range(N))
    P = 1
    for a in aa:
        if a > 1:
            P *= pow(a, a*a)
    return P, Q, tuple(aa)


def exact_cmp_ratio(P1, Q1, P2, Q2, n):
    """Compare r1=(K-2log2 P1)/Q1 with r2 exactly.

    Returns +1 if r1>r2, 0 if equal, -1 if r1<r2.
    Integer comparison follows by exponentiating base 2 after cross-multiplying:
      r1 >= r2 iff 2^{K(Q2-Q1)} P2^{2Q1} >= P1^{2Q2}.
    """
    assert Q1 > 0 and Q2 > 0 and P1 > 0 and P2 > 0
    N = 1 << n
    K = N*N*(n-1)//2
    D = K*(Q2-Q1)
    if D >= 0:
        left = (1 << D) * pow(P2, 2*Q1)
        right = pow(P1, 2*Q2)
    else:
        left = pow(P2, 2*Q1)
        right = (1 << (-D)) * pow(P1, 2*Q2)
    return (left > right) - (left < right)


def ratio_decimal(P, Q, n):
    N = 1 << n
    K = N*N*(n-1)//2
    return (K - 2*log2(P))/Q


def enumerate_translated_representatives(n, max_k=None):
    """Exhaust all minority sets A with 0 in A and 1<=|A|<=max_k.

    Output negation lets us assume |A|<=2^{n-1}. Translation lets us assume
    0 in A. We keep the exact minimum P at each Q because, for fixed Q, H/I
    is strictly decreasing in P.
    """
    N = 1 << n
    if max_k is None:
        max_k = N//2
    data = {}
    count = 0
    for k in range(1, max_k+1):
        minP_by_Q = {}
        count_k = 0
        for rest in combinations(range(1, N), k-1):
            A = (0,) + rest
            P,Q,_ = exact_profile_from_minority(n, A)
            old = minP_by_Q.get(Q)
            if old is None or P < old:
                minP_by_Q[Q] = P
            count_k += 1
        data[k] = minP_by_Q
        count += count_k
    return data, count


def candidate_one_point(n):
    return exact_profile_from_minority(n, (0,))[:2]


def certify_enumeration(n, max_k=None):
    data,count = enumerate_translated_representatives(n, max_k)
    Pc,Qc = candidate_one_point(n)
    equal_states = []
    strict_fail = []
    for k,d in data.items():
        for Q,P in d.items():
            c = exact_cmp_ratio(Pc,Qc,P,Q,n)
            if c < 0:
                strict_fail.append((k,Q))
            elif c == 0:
                equal_states.append((k,Q,P))
    assert not strict_fail
    return data,count,equal_states


def relaxed_n5(k):
    """Arithmetic relaxation for n=5 and minority size k.

    For S!=empty, a_S=|sum_{x in A} chi_S(x)| has same parity as k and lies
    between 0 and k. Parseval fixes sum_{S!=empty} a_S^2=k(32-k).
    There are degree multiplicities 5,10,10,5,1. For a genuine Boolean set,
    Q=sum |S|a_S^2=16*|edge boundary(A)|, so Q is divisible by 16.

    DP minimizes exact P=prod a_S^(a_S^2) for every (square-sum,Q), hence
    maximizes H for that Q over a superset of realizable Walsh profiles.
    """
    assert 1 <= k <= 16
    degrees = [1]*5 + [2]*10 + [3]*10 + [4]*5 + [5]
    target = k*(32-k)
    allowed = list(range(k&1, k+1, 2))
    opts = [(a,a*a,(pow(a,a*a) if a>1 else 1)) for a in allowed]
    dp = {(0,0):1}
    for idx,d in enumerate(degrees):
        nd = {}
        remaining = len(degrees)-idx-1
        min_sq = opts[0][1]
        max_sq = opts[-1][1]
        for (sq,q),P in dp.items():
            for a,a2,fac in opts:
                sq2 = sq+a2
                if sq2 > target: continue
                if sq2 + remaining*min_sq > target: continue
                if sq2 + remaining*max_sq < target: continue
                q2 = q+d*a2
                P2 = P*fac
                key = (sq2,q2)
                old = nd.get(key)
                if old is None or P2 < old:
                    nd[key] = P2
        dp = nd
    a0 = 16-k
    cfac = pow(a0,a0*a0) if a0>1 else 1
    finals = {}
    for (sq,q),P in dp.items():
        if sq == target and q%16 == 0:
            finals[q] = P*cfac
    assert finals
    return finals


def certify_n5_tail(Pc,Qc):
    table = []
    for k in range(7,17):
        finals = relaxed_n5(k)
        best = None
        for Q,P in finals.items():
            c = exact_cmp_ratio(Pc,Qc,P,Q,5)
            assert c > 0, ("relaxation beat/tied candidate",k,Q)
            r = ratio_decimal(P,Q,5)
            if best is None or r > best[0]:
                best = (r,Q,P.bit_length())
        table.append((k,len(finals),best[1],best[0],best[2]))
    return table


def exact_formula_string(n):
    if n == 1:
        return "0"
    a = (1 << (n-1))-1
    from fractions import Fraction
    A = Fraction((1<<n)*(n-1), n)
    B = Fraction(2*a*a, n*(1<<(n-1)))
    if a == 1:
        return str(A)
    return f"{A} - ({B})*log2({a})"


def main():
    print("EXACT FEI FINITE-CONSTANT CERTIFICATE n<=5")
    print("All optimum decisions below are exact integer comparisons; decimals are display only.")
    print()
    totals = {}
    for n in range(1,5):
        data,count,eq = certify_enumeration(n)
        Pc,Qc = candidate_one_point(n)
        assert eq == [(1,Qc,Pc)], (n,eq)
        totals[n] = count
        print(f"n={n}: translated/output-folded representatives exhaustively checked = {count}")
        print(f"  C_{n} = {exact_formula_string(n)}")
        print(f"  decimal = {ratio_decimal(Pc,Qc,n):.15f}")
        if n == 1:
            print("  extremizers = both nonconstant 1-bit Boolean functions (2 functions)")
        else:
            print(f"  extremizers = one-point defects and complements, exactly {2*(1<<n)} functions")
        print(f"  equality state after folding/translation: k=1, Q={Qc}; all other exact states strict")
    print()
    data5,count5,eq5 = certify_enumeration(5,max_k=6)
    Pc,Qc = candidate_one_point(5)
    assert eq5 == [(1,Qc,Pc)], eq5
    tail = certify_n5_tail(Pc,Qc)
    print(f"n=5: exact translated enumeration for k=1..6 checked = {count5} subsets")
    for k in range(1,7):
        best = max((ratio_decimal(P,Q,5),Q) for Q,P in data5[k].items())
        print(f"  actual k={k}: Q-states={len(data5[k])}, display max ratio={best[0]:.15f}, at Q={best[1]}")
    print("  k=7..16: exact arithmetic relaxation (superset of realizable Walsh profiles)")
    for k,nstates,Q,r,bits in tail:
        print(f"    k={k}: final Q-states={nstates}, display relaxed max={r:.15f}, Q={Q}, P_bits={bits}, EXACTLY below C_5")
    print(f"  C_5 = {exact_formula_string(5)}")
    print(f"  decimal = {ratio_decimal(Pc,Qc,5):.15f}")
    print(f"  extremizers = one-point defects and complements, exactly {2*(1<<5)} functions")
    print("  equality after output-folding/translation occurs only at k=1")
    print()
    print("COVERAGE COUNTS")
    print("  n<=4 exhaustive folded/translated counts:", totals)
    print("  n=5 actual k<=6 count:", count5)
    print("  n=5 k>=7 covered by exact DP relaxation, not sampling")
    print("CERTIFICATE STATUS: PASS")

if __name__ == '__main__':
    main()
