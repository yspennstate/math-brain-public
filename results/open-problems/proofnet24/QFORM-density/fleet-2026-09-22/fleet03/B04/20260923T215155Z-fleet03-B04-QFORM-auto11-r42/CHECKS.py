import itertools, math, json

H = [
    [1, 1, 1, 1],
    [1,-1, 1,-1],
    [1, 1,-1,-1],
    [1,-1,-1, 1],
]

def det3(a):
    return (
        a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
    )

HHt = [[sum(H[i][k]*H[j][k] for k in range(4)) for j in range(4)] for i in range(4)]
assert HHt == [[4 if i == j else 0 for j in range(4)] for i in range(4)]

mins = []
for R in itertools.combinations(range(4), 3):
    for C in itertools.combinations(range(4), 3):
        a = [[H[r][c] for c in C] for r in R]
        mins.append((R, C, det3(a)))
assert {abs(d) for _,_,d in mins} == {4}
E3 = sum(d*d for _,_,d in mins)
assert E3 == 256
incident = [sum(d*d for R,_,d in mins if i in R) for i in range(4)]
assert incident == [192,192,192,192]

def D(h):
    return 3*math.e/(math.sqrt(2*h)*(3-4*h))

def Hbranch(h):
    return 3*2**(4/3)*h**(-1/6)

lo, hi = 0.5, 0.75-1e-15
for _ in range(200):
    mid = (lo+hi)/2
    if D(mid) < Hbranch(mid):
        lo = mid
    else:
        hi = mid
h_star = (lo+hi)/2
C_star = max(D(h_star), Hbranch(h_star))
assert abs(D(h_star)-Hbranch(h_star)) < 1e-12
assert abs(h_star-0.5115590081942362) < 2e-15
assert abs(C_star-8.453021225528177) < 2e-12

delta = 47045881/(12*10**18)
C_inc = 3*2**(4/3)
partner_incident = C_inc*delta**(-1/6)
partner_global = C_star*delta**(-1/6)
example_bound = C_inc*192**(-1/6)
assert partner_incident < 602.012
assert partner_global < 673.166
assert example_bound < 3.147346

# A0=[[0,H],[H^T,0]] has eigenvalues +/-2 because HH^T=4I.
# diag(J4/8,J4/8) has operator norm 1/2, so Weyl leaves every
# eigenvalue at distance at least 3/2 from zero.
weyl_min_abs_lower_bound = 2-0.5
assert weyl_min_abs_lower_bound == 1.5

print(json.dumps({
    "status": "PASS",
    "HHt": HHt,
    "minor_abs_values": sorted({abs(d) for _,_,d in mins}),
    "E3": E3,
    "incident_J": incident,
    "h_star": h_star,
    "C_star": C_star,
    "delta": delta,
    "partner_incident_bound": partner_incident,
    "partner_global_bound": partner_global,
    "explicit_example_bound": example_bound,
    "weyl_min_abs_lower_bound": weyl_min_abs_lower_bound,
}, indent=2))
