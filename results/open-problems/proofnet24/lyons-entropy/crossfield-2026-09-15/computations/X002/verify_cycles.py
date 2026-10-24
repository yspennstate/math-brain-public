"""Exact checks of angular cycle expansion and bridge removal, independently of logs."""
from itertools import combinations, permutations, product
from pathlib import Path
import json
import sympy as s
from verify_transport import atom_jet


def marginal(K, keep, x):
    M = K.extract(keep, keep) - s.diag(*[1 - x[j] for j in keep])
    return s.simplify((-1)**sum(1 - x[j] for j in keep) * M.det())


def div_complement(K, U, x):
    keep = [j for j in range(K.rows) if j not in U]
    return s.prod(2*x[j]-1 for j in U) * marginal(K, keep, x)


def simple_cycles(K, S):
    n = K.rows
    for m in range(3, n+1):
        for U in combinations(range(n), m):
            for tail in permutations(U[1:]):
                C = (U[0],) + tail
                if C[1] > C[-1]:
                    continue
                E = list(zip(C, C[1:]+C[:1]))
                if all(K[i,j] != 0 or S[i,j] != 0 for i,j in E):
                    yield C, E


def cycle_check():
    K = s.diag(s.Rational(2,5),s.Rational(9,20),s.Rational(11,20),s.Rational(3,5))
    S = s.zeros(4)
    for i,j in combinations(range(4),2):
        K[i,j] = K[j,i] = s.Rational((-1)**(i+j),30+3*i+j)
        S[i,j] = s.Rational(i+2*j+1,15)
        S[j,i] = -S[i,j]
    # A missing base edge is deliberately moved: union support is necessary.
    K[0,3] = K[3,0] = 0
    cycles = list(simple_cycles(K,S))
    cycle_data = []
    for C,E in cycles:
        R = 0
        for a,b in combinations(range(len(E)),2):
            other = s.prod(K[i,j] for g,(i,j) in enumerate(E) if g not in (a,b))
            R += S[E[a][0],E[a][1]] * S[E[b][0],E[b][1]] * other
        cycle_data.append((C,s.simplify(R)))
    for x in product([0,1],repeat=4):
        p,dp,ddp = atom_jet(K,s.I*S,x)
        assert p > 0 and dp == 0
        expansion = -2*sum(S[i,j]**2*div_complement(K,[i,j],x)
                           for i,j in combinations(range(4),2))
        expansion -= 4*sum((-1)**(len(C)-1)*R*div_complement(K,C,x)
                           for C,R in cycle_data)
        assert s.simplify(expansion-ddp) == 0
    return {"exact_cycle_acceleration": "PASS", "number_of_simple_cycles":len(cycles),
            "includes_zero_base_moving_edge":True,
            "cycle_coefficients":[{"cycle":list(C),"R":str(R)} for C,R in cycle_data]}


def bridge_check():
    K = s.diag(s.Rational(2,5),s.Rational(9,20),s.Rational(11,20),s.Rational(3,5))
    edges = {(0,1):s.Rational(1,25)+s.I/40,
             (0,2):s.Rational(-1,35)+s.I/45,
             (1,2):s.Rational(1,30)-s.I/50,
             (2,3):s.Rational(1,24)+s.I/32}
    A = s.diag(s.Rational(1,7),s.Rational(-1,6),s.Rational(1,5),s.Rational(-1,4))
    for (i,j),k in edges.items():
        K[i,j],K[j,i] = k,s.conjugate(k)
        A[i,j] = s.Rational(i-j,17) + s.I*s.Rational(i+j+1,19)
        A[j,i] = s.conjugate(A[i,j])
    e=(2,3)
    r=s.re(s.simplify(A[e[0],e[1]]/K[e[0],e[1]]))
    theta=s.im(s.simplify(A[e[0],e[1]]/K[e[0],e[1]]))
    B=A.copy()
    B[2,3]=r*K[2,3]
    B[3,2]=s.conjugate(B[2,3])
    coefficient=2*theta**2*K[2,3]*K[3,2]
    for x in product([0,1],repeat=4):
        p,dp,ddp=atom_jet(K,A,x)
        pB,dpB,ddpB=atom_jet(K,B,x)
        assert p>0 and p==pB and dp==dpB
        assert s.simplify(ddp-ddpB+coefficient*div_complement(K,e,x))==0
    return {"exact_bridge_first_and_second_jets":"PASS",
            "complex_cyclic_block":True,"bridge":[2,3],
            "radial_ratio":str(r),"angular_ratio":str(theta),
            "negative_square_coefficient_before_W":str(s.simplify(coefficient))}


if __name__=="__main__":
    results={"cycle_expansion":cycle_check(),"bridge_removal":bridge_check()}
    Path(__file__).with_name("cycle_results.json").write_text(json.dumps(results,indent=2)+"\n")
    print(json.dumps(results,indent=2))
