from fractions import Fraction

# Regression verifier for account04/B20 POS3 shallow-run localization.
# This is finite verification only; the universal theorem is proved analytically in REPORT.md.

def transitive_closure(n, rels):
    reach = [[False]*n for _ in range(n)]
    for a,b in rels:
        reach[a][b] = True
    for k in range(n):
        for i in range(n):
            if reach[i][k]:
                for j in range(n):
                    if reach[k][j]:
                        reach[i][j] = True
    return {(i,j) for i in range(n) for j in range(n) if reach[i][j]}

def linear_extensions(n, rels):
    preds=[set() for _ in range(n)]
    for a,b in rels:
        preds[b].add(a)
    out=[]
    def rec(seq, rem):
        if not rem:
            out.append(tuple(seq))
            return
        avail=sorted(v for v in rem if preds[v].isdisjoint(rem))
        for v in avail:
            rec(seq+[v], rem-{v})
    rec([], set(range(n)))
    return out

# account01/B19 r12 Simpson example:
# Q has S={0,1,2,3}, T={4,5,6}, and relations
# 0<2<3<5, 1<6, 4<6. Restoring c=7 imposes c<4,c<5.
S={0,1,2,3}
T={4,5,6}
q_rels=transitive_closure(7, {(0,2),(2,3),(3,5),(1,6),(4,6)})
LQ=linear_extensions(7,q_rels)
assert len(LQ)==70

def kappa(tau):
    k=0
    for z in tau:
        if z in S:
            k += 1
        else:
            break
    return k

ks=[kappa(t) for t in LQ]
lift_count=sum(k+1 for k in ks)
assert lift_count==203
M=Fraction(lift_count,len(LQ))

# Exact first-element insertion identity:
# Under a full extension of P, conditionally on tau, c has kappa(tau)+1 legal gaps.
# G is its insertion-gap index.
G_counts={}
for tau,k in zip(LQ,ks):
    for g in range(k+1):
        G_counts[g]=G_counts.get(g,0)+1
assert sum(G_counts.values())==203

for h in range(1,8):
    lhs=Fraction(sum(v for g,v in G_counts.items() if g>=h), lift_count)
    rhs=Fraction(sum(max(k-h+1,0) for k in ks), len(LQ))/M
    assert lhs==rhs, (h,lhs,rhs)

# Reproduce partner's cross pair (a,b)=(1,5).
nu_num=sum(1 for t in LQ if t.index(1)<t.index(5))
nu=Fraction(nu_num,len(LQ))
mu_num=0
for t,k in zip(LQ,ks):
    if t.index(1)<t.index(5):
        mu_num += k+1
mu=Fraction(mu_num,lift_count)
assert nu==Fraction(32,35)
assert mu==Fraction(185,203)

# Universal constants from the analytic theorem at r=24.
r=24
K=3*r-1
delta_mu=Fraction(1755,256*r*r)
delta_nu=Fraction(5265,1024*r*r*r)
epsilon=delta_mu+delta_nu
states=K*(K+1)//2

assert K==71
assert delta_mu==Fraction(195,16384)
assert delta_nu==Fraction(195,524288)
assert epsilon==Fraction(6435,524288)
assert epsilon < Fraction(1,81)
assert states==2556

print("q_extensions", len(LQ))
print("restored_extensions", lift_count)
print("kappa_histogram", {k:ks.count(k) for k in sorted(set(ks))})
print("partner_pair_nu", nu, "mu", mu, "difference", mu-nu)
print("r", r, "shallow_kappa_max", K-1, "cut_state_cap", states)
print("delta_mu_bound", delta_mu, float(delta_mu))
print("delta_nu_bound", delta_nu, float(delta_nu))
print("transfer_error_bound", epsilon, float(epsilon), "lt_1_over_81", epsilon < Fraction(1,81))
print("POS3_SHALLOW_RUN_LOCALIZATION_REGRESSION_PASS")
