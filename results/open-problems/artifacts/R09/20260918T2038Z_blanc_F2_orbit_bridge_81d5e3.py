#!/usr/bin/env python3
from fractions import Fraction

ORIGIN = None

def opp(q):
    return q ^ 1

def states_F2(d):
    m = 2*d
    S = []
    # (cluster_size, tail_class, delta)
    # tail_class None means b^- = 0; an integer e means b^- = e != 0.
    for delta in range(m):
        S.append((1, ORIGIN, delta))
    for f in range(m):
        # cluster {0,f}, tail 0, head delta; live iff head != f
        for delta in range(m):
            if delta != f:
                S.append((2, ORIGIN, delta))
        # cluster {0,f}, tail f, head f+delta; live iff head != 0, i.e. delta != -f
        for delta in range(m):
            if delta != opp(f):
                S.append((2, f, delta))
    return S

def noncut(A, B):
    # Exact specialization of source (3.2) on |cluster| <= 2:
    # a transition is cut iff B has nonzero tail e and e = -delta(A).
    _, _, da = A
    tb, tailb, _ = B
    return not (tb == 2 and tailb is not ORIGIN and tailb == opp(da))

def mu_weights(d, p):
    m = 2*d
    u = (1-p)**m
    v = p*(1-p)**(2*m-2)
    return u, v

def weight(state, u, v):
    return u if state[0] == 1 else v

def matmul(A, B):
    n = len(A); k = len(B); m = len(B[0])
    out = [[Fraction(0) for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for t in range(k):
            if A[i][t] == 0:
                continue
            a = A[i][t]
            for j in range(m):
                if B[t][j]:
                    out[i][j] += a*B[t][j]
    return out

def check_dimension(d):
    m = 2*d
    p = Fraction(1, 4*d)  # calibration only; theorem in report is algebraic in p
    u, v = mu_weights(d, p)
    S = states_F2(d)
    assert len(S) == m + 2*m*(m-1)

    # Source multiplicities by direction and exact row target counts.
    per_dir = [sum(1 for A in S if A[2] == a) for a in range(m)]
    assert set(per_dir) == {2*m-1}
    target1 = m
    target2 = (m-1)*(2*m-1)
    for A in S:
        c1 = sum(noncut(A,B) and B[0] == 1 for B in S)
        c2 = sum(noncut(A,B) and B[0] == 2 for B in S)
        assert (c1,c2) == (target1,target2)

    # Weighted direction-lumped one-step kernel K.
    K = [[Fraction(0) for _ in range(m)] for _ in range(m)]
    for a in range(m):
        dummy = (1, ORIGIN, a)
        for B in S:
            if noncut(dummy, B):
                K[a][B[2]] += weight(B,u,v)

    G = u + 2*(m-1)*v
    for a in range(m):
        for b in range(m):
            expected = G if a == b else G-v
            assert K[a][b] == expected
    r = m*G - (m-1)*v
    assert all(sum(row) == r for row in K)

    K2 = matmul(K,K)
    Q = m*(G-v)**2 + 2*v*(G-v)
    for a in range(m):
        for b in range(m):
            expected = Q + (v*v if a == b else 0)
            assert K2[a][b] == expected

    # Incoming masses c(B)=sum_A w(A) R(A,B), checked directly.
    cB = []
    for B in S:
        c = sum(weight(A,u,v) for A in S if noncut(A,B))
        if B[0] == 1 or B[1] is ORIGIN:
            assert c == m*G
        else:
            assert c == (m-1)*G
        cB.append(c)

    # Exhaust over direction x endpoint state (all source states with same direction have same row).
    # Ratio = J_F(A,B)/(nu_up_F(A) nu_down_F(B)); endpoint/source weights cancel.
    min_ratio = None
    extremal = []
    for a in range(m):
        for j,B in enumerate(S):
            if B[0] == 1 or B[1] is ORIGIN:
                M = r*r
            else:
                e = B[1]
                M = r*r - K2[a][opp(e)]
            ratio = M/(r*cB[j])
            if min_ratio is None or ratio < min_ratio:
                min_ratio = ratio
                extremal = [(a,j)]
            elif ratio == min_ratio:
                extremal.append((a,j))

    gamma = (G-v)*(m*(G-v)+2*v)/(G*r)
    assert min_ratio == gamma
    assert all(S[j][0] == 2 and S[j][1] is not ORIGIN and S[j][1] == opp(a)
               for a,j in extremal)
    # Per source direction there are exactly m-1 endpoint states in the aligned nonzero-tail class.
    assert len(extremal) == m*(m-1)

    # Strict gaps to the other two ratio classes.
    gamma_H = r/(m*G)
    gamma_L_non = gamma + v*v/(G*(m-1)*r)
    assert gamma_H - gamma == v*v/(G*m*r) > 0
    assert gamma_L_non > gamma

    # Full-chain deterministic two-singleton gateway coefficient from the report.
    gamma_singleton_prefactor = Fraction(m-1,m) * u*u
    assert gamma_singleton_prefactor > 0

    return {
        'd': d, 'm': m, 'states': len(S), 'p': p,
        'gamma': gamma,
        'gamma_H': gamma_H,
        'gamma_L_non': gamma_L_non,
        'extremal_direction_endpoint_pairs': len(extremal),
        'full_chain_gamma_times_chi2': gamma_singleton_prefactor,
    }

def main():
    print('R09 exact F2 bridge-lumping certificate')
    for d in (7,8,9,10):
        z = check_dimension(d)
        print('d', z['d'], 'm', z['m'], 'states', z['states'], 'p', z['p'])
        print('  gamma_F2 =', z['gamma'])
        print('  gamma_F2_decimal = %.15f' % float(z['gamma']))
        print('  gamma_H_minus_min =', z['gamma_H']-z['gamma'])
        print('  gamma_L_non_minus_min =', z['gamma_L_non']-z['gamma'])
        print('  extremal_direction_endpoint_pairs =', z['extremal_direction_endpoint_pairs'])
        print('  full_chain_gamma_singleton * chi^2 =', z['full_chain_gamma_times_chi2'])
    print('ALL_EXACT_CHECKS_PASS')

if __name__ == '__main__':
    main()
