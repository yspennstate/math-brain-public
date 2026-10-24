from fractions import Fraction

# Exact tightening of the archived top-seven hard law.  This checker uses only
# integer/Fraction arithmetic.  It certifies the complete delayed-query Bellman
# value below 37321/100000 for every iid distinguished-rank sampling density
# p in [0,1].  The source fixed-size lift is the same uniform seven-bit
# hypergeometric-to-iid coupling proved in the accompanying report.

M = 7
D = 100000
TARGET = Fraction(37321, 100000)
HARD_NUM = {
    (7,6,5,4,3,2,1):13250, (6,5,4,3,2,1,7):4251,
    (7,5,4,3,2,1,6):1043, (5,4,3,2,1,6,7):1730,
    (7,4,3,2,1,5,6):1027, (4,3,2,1,5,6,7):3049,
    (7,6,5,3,2,1,4):1398, (5,3,2,1,4,6,7):105,
    (7,6,3,2,1,4,5):1036, (7,3,2,1,4,5,6):2918,
    (3,2,1,4,5,6,7):2324, (7,6,5,4,2,1,3):1874,
    (7,6,5,2,1,3,4):3820, (6,5,2,1,3,4,7):165,
    (7,6,2,1,3,4,5):3244, (6,2,1,3,4,5,7):982,
    (7,2,1,3,4,5,6):4257, (2,1,3,4,5,6,7):3217,
    (7,6,5,4,3,1,2):8929, (6,5,4,3,1,2,7):2672,
    (7,5,4,3,1,2,6):1037, (5,4,3,1,2,6,7):568,
    (6,4,3,1,2,5,7):153, (7,4,3,1,2,5,6):329,
    (4,3,1,2,5,6,7):2174, (6,3,1,2,4,5,7):422,
    (3,1,2,4,5,6,7):720, (7,6,5,4,1,2,3):6196,
    (6,5,4,1,2,3,7):1256, (5,4,1,2,3,6,7):312,
    (4,1,2,3,5,6,7):927, (7,6,5,1,2,3,4):5714,
    (7,5,1,2,3,4,6):1095, (5,1,2,3,4,6,7):119,
    (7,6,1,2,3,4,5):5940, (6,1,2,3,4,5,7):2164,
    (7,1,2,3,4,5,6):4598, (1,2,3,4,5,6,7):4985,
}
assert sum(HARD_NUM.values()) == D
orders = list(HARD_NUM)
mass_num = [HARD_NUM[o] for o in orders]

hidden = []
for oi, order in enumerate(orders):
    for smask in range(1 << M):
        seq = tuple(r for r in order if not ((smask >> (r-1)) & 1))
        hidden.append((oi, smask, seq, smask.bit_count()))
H = len(hidden)
ALL = tuple(range(H))

qresp = [[-1]*H for _ in range(M)]
obs = [[-1]*H for _ in range(M)]
active = [[False]*H for _ in range(M)]
ismax = [[False]*H for _ in range(M)]
for idx, (oi, smask, seq, k) in enumerate(hidden):
    sampled = {i+1 for i in range(M) if (smask >> i) & 1}
    for step in range(M):
        seen_q = sampled | set(seq[:min(step, len(seq))])
        qresp[step][idx] = min(seen_q)-1 if seen_q else M
        if step < len(seq):
            active[step][idx] = True
            r = seq[step]
            seen = sampled | set(seq[:step+1])
            obs[step][idx] = 1 + sum(rr < r for rr in seen)
            ismax[step][idx] = (r == 1)

nodes = {}
def build(state, step, used):
    key = (state, step, used)
    if key in nodes:
        return
    if not state or step >= M:
        nodes[key] = ('terminal',)
        return
    groups = {}
    for idx in state:
        if active[step][idx]:
            groups.setdefault(obs[step][idx], []).append(idx)
    outs = []
    for g in groups.values():
        gt = tuple(g)
        sel = tuple(idx for idx in gt if ismax[step][idx])
        child = (gt, step+1, used)
        build(*child)
        outs.append((sel, child))
    qchildren = None
    if not used:
        qgroups = {}
        for idx in state:
            qgroups.setdefault(qresp[step][idx], []).append(idx)
        qchildren = []
        for g in qgroups.values():
            child = (tuple(g), step, True)
            build(*child)
            qchildren.append(child)
    nodes[key] = ('node', tuple(outs),
                  tuple(qchildren) if qchildren is not None else None)

ROOT = (ALL, 0, False)
build(*ROOT)
keys = list(nodes)
kid = {k:i for i,k in enumerate(keys)}
rootid = kid[ROOT]
data = [None]*len(keys)
by_step_used = {(s,u):[] for s in range(M) for u in (True,False)}

for key, i in kid.items():
    raw = nodes[key]
    if raw[0] == 'terminal':
        data[i] = ('terminal',)
        continue
    _, outs, qchildren = raw
    compiled_outs = []
    for sel, child in outs:
        coeff = [0]*(M+1)
        for idx in sel:
            oi, smask, seq, k = hidden[idx]
            coeff[k] += mass_num[oi]
        compiled_outs.append((tuple(coeff), kid[child]))
    qc = tuple(kid[ch] for ch in qchildren) if qchildren is not None else None
    data[i] = ('node', tuple(compiled_outs), qc)
    by_step_used[(key[1], key[2])].append(i)

def point_num(a, b, want_coeff=False):
    assert 0 <= a <= b and b > 0
    mon = [a**k * (b-a)**(M-k) for k in range(M+1)]
    vals = [0]*len(keys)
    coeffs = [[0]*(M+1) for _ in range(len(keys))] if want_coeff else None
    for step in range(M-1, -1, -1):
        # used=True first because a same-step query child has used=True.
        for used in (True, False):
            for i in by_step_used[(step, used)]:
                _, outs, qchildren = data[i]
                wait = 0
                wait_coeff = [0]*(M+1) if want_coeff else None
                for scoeff, child in outs:
                    select = sum(scoeff[k]*mon[k] for k in range(M+1))
                    reject = vals[child]
                    if select >= reject:
                        wait += select
                        if want_coeff:
                            for k in range(M+1):
                                wait_coeff[k] += scoeff[k]
                    else:
                        wait += reject
                        if want_coeff:
                            cc = coeffs[child]
                            for k in range(M+1):
                                wait_coeff[k] += cc[k]
                if qchildren is None:
                    vals[i] = wait
                    if want_coeff:
                        coeffs[i] = wait_coeff
                else:
                    query = sum(vals[ch] for ch in qchildren)
                    if query > wait:
                        vals[i] = query
                        if want_coeff:
                            qc = [0]*(M+1)
                            for ch in qchildren:
                                cc = coeffs[ch]
                                for k in range(M+1):
                                    qc[k] += cc[k]
                            coeffs[i] = qc
                    else:
                        vals[i] = wait
                        if want_coeff:
                            coeffs[i] = wait_coeff
    if want_coeff:
        return vals[rootid], D*b**M, tuple(coeffs[rootid])
    return vals[rootid], D*b**M

# Exact 7-Lipschitz adaptive dyadic cover.
stack = [(0,0)]
checked = splits = leaves = 0
unresolved = []
min_margin = None
max_mid_value = Fraction(0)
max_midpoint = None
MAX_DEPTH = 34
while stack:
    l, d = stack.pop()
    a = 2*l + 1
    b = 2**(d+1)
    num, den = point_num(a,b)
    v = Fraction(num,den)
    checked += 1
    if v > max_mid_value:
        max_mid_value = v
        max_midpoint = (a,b,l,d)
    upper = v + Fraction(M, 2**(d+1))
    margin = TARGET - upper
    if margin > 0:
        leaves += 1
        if min_margin is None or margin < min_margin:
            min_margin = margin
    elif d >= MAX_DEPTH:
        unresolved.append((l,d,v,upper))
    else:
        splits += 1
        stack.append((2*l,d+1))
        stack.append((2*l+1,d+1))

assert not unresolved
assert min_margin is not None and min_margin > 0
assert max_mid_value < TARGET

P0 = Fraction(*point_num(0,1))
P13 = Fraction(*point_num(1,3))
P7_20 = Fraction(*point_num(7,20))
P703_2000 = Fraction(*point_num(703,2000))

# Extract the winning-mask Bernstein coefficients of the active deterministic
# policy at the closest dyadic midpoint to the observed peak.  This is not
# needed for the endpoint certificate; it is a compact B25 diagnostic.
peak_a, peak_b, _, _ = max_midpoint
_, _, peak_coeff = point_num(peak_a, peak_b, want_coeff=True)
assert peak_coeff == (17518,250729,881254,1423165,1233815,550310,100000,0)

print('support_size =', len(orders))
print('positive_hidden_states =', H)
print('bellman_graph_nodes =', len(nodes))
print('target_bound =', TARGET, float(TARGET))
print('point_V(0) =', P0, float(P0))
print('point_V(1/3) =', P13, float(P13))
print('point_V(7/20) =', P7_20, float(P7_20))
print('point_V(703/2000) =', P703_2000, float(P703_2000))
print('checked_dyadic_midpoints =', checked)
print('split_intervals =', splits)
print('certified_leaf_intervals =', leaves)
print('unresolved_intervals =', len(unresolved))
print('max_midpoint_value =', max_mid_value, float(max_mid_value))
print('max_midpoint =', max_midpoint)
print('smallest_exact_cover_margin =', min_margin, float(min_margin))
print('peak_policy_bernstein_coeff =', peak_coeff)
print('ALL_EXACT_CHECKS_PASS')
