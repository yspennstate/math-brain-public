from fractions import Fraction

# Exact rational hard law on 38 nested-end top-seven orders; every top block
# is followed by the same decreasing tail 8,9,... . Integer masses sum to 1.
M = 7
D = 100000
HARD_NUM = {(7, 6, 5, 4, 3, 2, 1): 13250, (6, 5, 4, 3, 2, 1, 7): 4251, (7, 5, 4, 3, 2, 1, 6): 1043, (5, 4, 3, 2, 1, 6, 7): 1730, (7, 4, 3, 2, 1, 5, 6): 1027, (4, 3, 2, 1, 5, 6, 7): 3049, (7, 6, 5, 3, 2, 1, 4): 1398, (5, 3, 2, 1, 4, 6, 7): 105, (7, 6, 3, 2, 1, 4, 5): 1036, (7, 3, 2, 1, 4, 5, 6): 2918, (3, 2, 1, 4, 5, 6, 7): 2324, (7, 6, 5, 4, 2, 1, 3): 1874, (7, 6, 5, 2, 1, 3, 4): 3820, (6, 5, 2, 1, 3, 4, 7): 165, (7, 6, 2, 1, 3, 4, 5): 3244, (6, 2, 1, 3, 4, 5, 7): 982, (7, 2, 1, 3, 4, 5, 6): 4257, (2, 1, 3, 4, 5, 6, 7): 3217, (7, 6, 5, 4, 3, 1, 2): 8929, (6, 5, 4, 3, 1, 2, 7): 2672, (7, 5, 4, 3, 1, 2, 6): 1037, (5, 4, 3, 1, 2, 6, 7): 568, (6, 4, 3, 1, 2, 5, 7): 153, (7, 4, 3, 1, 2, 5, 6): 329, (4, 3, 1, 2, 5, 6, 7): 2174, (6, 3, 1, 2, 4, 5, 7): 422, (3, 1, 2, 4, 5, 6, 7): 720, (7, 6, 5, 4, 1, 2, 3): 6196, (6, 5, 4, 1, 2, 3, 7): 1256, (5, 4, 1, 2, 3, 6, 7): 312, (4, 1, 2, 3, 5, 6, 7): 927, (7, 6, 5, 1, 2, 3, 4): 5714, (7, 5, 1, 2, 3, 4, 6): 1095, (5, 1, 2, 3, 4, 6, 7): 119, (7, 6, 1, 2, 3, 4, 5): 5940, (6, 1, 2, 3, 4, 5, 7): 2164, (7, 1, 2, 3, 4, 5, 6): 4598, (1, 2, 3, 4, 5, 6, 7): 4985}
assert sum(HARD_NUM.values()) == D

def is_nested_end(order):
    for r in range(2, M + 1):
        sub = [x for x in order if x <= r]
        if sub[0] != r and sub[-1] != r:
            return False
    return True

assert all(is_nested_end(o) for o in HARD_NUM)
orders = list(HARD_NUM)
mass_num = [HARD_NUM[o] for o in orders]

hidden = []
for oi, pi in enumerate(orders):
    for bits in range(1 << M):
        seq = tuple(r for r in pi if not ((bits >> (r - 1)) & 1))
        hidden.append((oi, bits, seq, bits.bit_count()))
H = len(hidden)
ALL = tuple(range(H))
assert H == len(orders) * (1 << M)

qresp = [[-1] * H for _ in range(M)]
obs = [[-1] * H for _ in range(M)]
active = [[False] * H for _ in range(M)]
ismax = [[False] * H for _ in range(M)]

for idx, (oi, bits, seq, k) in enumerate(hidden):
    mask = {i + 1 for i in range(M) if (bits >> i) & 1}
    for step in range(M):
        seen_q = mask | set(seq[:min(step, len(seq))])
        # If no distinguished rank has been seen, the actual query answer may
        # contain additional common-tail information. That signal is independent
        # of the hidden top-order variable conditional on this top mask, so
        # collapsing it to the single symbol M is safe for the upper bound.
        qresp[step][idx] = min(seen_q) - 1 if seen_q else M
        if step < len(seq):
            active[step][idx] = True
            r = seq[step]
            seen = mask | set(seq[:step + 1])
            obs[step][idx] = 1 + sum(rr < r for rr in seen)
            ismax[step][idx] = (r == 1)

nodes = {}
def build(state, step, used):
    key = (state, step, used)
    if key in nodes:
        return
    if not state or step >= M:
        nodes[key] = ("terminal",)
        return
    groups = {}
    for idx in state:
        if active[step][idx]:
            groups.setdefault(obs[step][idx], []).append(idx)
    obs_children = []
    for g in groups.values():
        gt = tuple(g)
        sel = tuple(idx for idx in gt if ismax[step][idx])
        child = (gt, step + 1, used)
        build(*child)
        obs_children.append((sel, child))
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
    nodes[key] = ("node", tuple(obs_children),
                  tuple(qchildren) if qchildren is not None else None)

ROOT = (ALL, 0, False)
build(*ROOT)

compiled = {}
for key, data in nodes.items():
    if data[0] == "terminal":
        compiled[key] = data
        continue
    _, obs_children, qchildren = data
    out = []
    for sel, child in obs_children:
        coeff = [0] * (M + 1)
        for idx in sel:
            oi, bits, seq, k = hidden[idx]
            coeff[k] += mass_num[oi]
        out.append((tuple(coeff), child))
    compiled[key] = ("node", tuple(out), qchildren)

def point_num(a, b):
    """Exact numerator/common denominator for complete delayed-query value V(a/b)."""
    assert 0 <= a <= b and b > 0
    mon = [a**k * (b-a)**(M-k) for k in range(M + 1)]
    memo = {}
    def E(key):
        if key in memo:
            return memo[key]
        data = compiled[key]
        if data[0] == "terminal":
            memo[key] = 0
            return 0
        _, obs_children, qchildren = data
        wait = 0
        for coeff, child in obs_children:
            select = sum(coeff[k] * mon[k] for k in range(M + 1))
            reject = E(child)
            wait += max(select, reject)
        if qchildren is None:
            val = wait
        else:
            query = sum(E(ch) for ch in qchildren)
            val = max(wait, query)
        memo[key] = val
        return val
    return E(ROOT), D * b**M

# For seven iid Bernoulli(p) top-sample bits, maximal coupling gives
# TV <= 7|p-q|. Since success is in [0,1], every deterministic policy payoff,
# and hence the optimal Bellman value V, is 7-Lipschitz.
LIPSCHITZ = 7
TARGET = Fraction(1493, 4000)  # 0.37325

# Exact dyadic adaptive cover. On [l/2^d,(l+1)/2^d], midpoint m is at
# distance at most 1/2^(d+1), so V(p) <= V(m) + 7/2^(d+1).
stack = [(0, 0)]
checked = splits = leaves = 0
unresolved = []
min_margin = None
min_margin_leaf = None
max_mid_value = Fraction(0)
max_midpoint = None
MAX_DEPTH = 30

while stack:
    l, d = stack.pop()
    a = 2*l + 1
    b = 2**(d + 1)
    num, den = point_num(a, b)
    v = Fraction(num, den)
    checked += 1
    if v > max_mid_value:
        max_mid_value = v
        max_midpoint = (a, b, l, d)
    upper = v + Fraction(7, 2**(d + 1))
    margin = TARGET - upper
    if margin > 0:
        leaves += 1
        if min_margin is None or margin < min_margin:
            min_margin = margin
            min_margin_leaf = (l, d, v, upper)
    elif d >= MAX_DEPTH:
        unresolved.append((l, d, v, upper))
    else:
        splits += 1
        stack.append((2*l, d + 1))
        stack.append((2*l + 1, d + 1))

assert not unresolved
assert min_margin is not None and min_margin > 0
assert max_mid_value < TARGET

P0 = Fraction(*point_num(0, 1))
P13 = Fraction(*point_num(1, 3))
P7_20 = Fraction(*point_num(7, 20))
P703_2000 = Fraction(*point_num(703, 2000))
assert all(x < TARGET for x in (P0, P13, P7_20, P703_2000))

print("hard_distribution =", [(o, f"{HARD_NUM[o]}/{D}") for o in orders])
print("support_size =", len(orders))
print("positive_hidden_states =", H)
print("bellman_graph_nodes =", len(nodes))
print("point_V(0) =", P0, float(P0))
print("point_V(1/3) =", P13, float(P13))
print("point_V(7/20) =", P7_20, float(P7_20))
print("point_V(703/2000) =", P703_2000, float(P703_2000))
print("target_bound =", TARGET, float(TARGET))
print("lipschitz_constant =", LIPSCHITZ)
print("checked_dyadic_midpoints =", checked)
print("split_intervals =", splits)
print("certified_leaf_intervals =", leaves)
print("unresolved_intervals =", len(unresolved))
print("max_midpoint_value =", max_mid_value, float(max_mid_value))
print("max_midpoint =", max_midpoint)
print("smallest_exact_cover_margin =", min_margin, float(min_margin))
print("smallest_margin_leaf =", min_margin_leaf)
print("ALL_EXACT_CHECKS_PASS")
