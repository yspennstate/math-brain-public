import itertools
import sympy as sp

r, s = sp.symbols("r s", real=True)
types = {"P": (-1, r), "Q": (r, s), "R": (-1, s)}

target_low = (r+s)/((r+1)*(s+1))
target_high = (1-r)/((s-r)*(s+1))

def common_density(ms):
    i = ms.count("P"); j = ms.count("Q"); k = ms.count("R")
    low = sp.Rational(i,3)/(r+1) + sp.Rational(k,3)/(s+1)
    high = sp.Rational(j,3)/(s-r) + sp.Rational(k,3)/(s+1)
    return sp.factor(low), sp.factor(high)

found_points = set()
found_curves = set()

for ms in itertools.combinations_with_replacement(["P","Q","R"],3):
    low, high = common_density(ms)
    total_endpoint_sum = sp.expand(sum(types[t][0] + types[t][1] for t in ms))
    for ori in itertools.product([0,1], repeat=3):
        p_sum = sp.expand(sum(types[t][o] for t,o in zip(ms,ori)))
        eqs = [
            sp.together(total_endpoint_sum).as_numer_denom()[0],
            sp.together(p_sum).as_numer_denom()[0],
            sp.together(low-target_low).as_numer_denom()[0],
            sp.together(high-target_high).as_numer_denom()[0],
        ]
        A,b = sp.linear_eq_to_matrix(eqs[:2],[r,s])
        if A.row_join(b).rank() != A.rank():
            continue
        rank=A.rank()
        if rank==1:
            sols=sp.solve(eqs[:2],[r,s],dict=True)
            for d in sols:
                rem=[sp.factor(e.subs(d)) for e in eqs[2:]]
                if all(x==0 for x in rem):
                    if d.get(r,None) == 1-s:
                        found_curves.add((ms,ori,"r=1-s"))
                    elif d.get(s,None) == 1-r:
                        found_curves.add((ms,ori,"r=1-s"))
                    else:
                        raise AssertionError(("unexpected curve", ms,ori,d,rem))
        elif rank==2:
            sols=sp.solve(eqs[:2],[r,s],dict=True)
            for d in sols:
                if r not in d or s not in d:
                    continue
                rr=sp.simplify(d[r]); ss=sp.simplify(d[s])
                if any(sp.factor(e.subs({r:rr,s:ss})) != 0 for e in eqs[2:]):
                    continue
                if bool(rr > -1) and bool(rr < 1) and bool(ss > 1) and bool(ss <= 2) and bool(rr < ss):
                    found_points.add((ms,ori,rr,ss))

expected_points = {
    (("P","P","Q"),(0,0,1),sp.Integer(0),sp.Integer(2)),
    (("P","P","Q"),(1,1,0),sp.Integer(0),sp.Integer(2)),
    (("P","P","R"),(0,0,1),sp.Rational(1,2),sp.Integer(2)),
    (("P","P","R"),(1,1,0),sp.Rational(1,2),sp.Integer(2)),
}
expected_curves = {
    (("P","Q","R"),(0,0,1),"r=1-s"),
    (("P","Q","R"),(1,1,0),"r=1-s"),
}
assert found_points == expected_points, (found_points, expected_points)
assert found_curves == expected_curves, (found_curves, expected_curves)

ss = 1-r
alpha=(ss-1)/(ss-r)
beta=(1-r)/(ss-r)
P_low=sp.factor(alpha/(r+1)+beta/(ss+1))
P_high=sp.factor(beta/(ss+1))
C_low=sp.factor(sp.Rational(1,3)/(r+1)+sp.Rational(1,3)/(ss+1))
C_high=sp.factor(sp.Rational(1,3)/(ss-r)+sp.Rational(1,3)/(ss+1))
assert sp.simplify(P_low-C_low)==0
assert sp.simplify(P_high-C_high)==0

alpha0,c,beta0,L=sp.symbols("alpha0 c beta0 L", real=True)
h_left=(beta0-c)/((beta0-alpha0)*(L-alpha0))
h_right=(L-alpha0-beta0+c)/((L-beta0)*(L-alpha0))
assert sp.simplify((h_right-h_left) - (c-alpha0)/((L-beta0)*(beta0-alpha0))) == 0

print("D0008 ALIGNED-SEGMENT EXACT CHECK PASSED")
print("positive-dimensional locus: PQR with r+s=1 (two reverse orientations)")
print("isolated source-domain points: PPQ at (r,s)=(0,2); PPR at (r,s)=(1/2,2)")
print("V-step identity verified: h_right-h_left=(c-alpha)/((L-beta)(beta-alpha))")
