from functools import lru_cache
from collections import Counter
from hashlib import sha256
from fractions import Fraction

# Exact integer units: one unit = 1/14 of safety/item value.
Q = 14
TARGET = -17                 # safety <= -17/14
START = (Q, 3*Q)             # balanced 2--1 split after three common unit goods: (1,3)
DEPTH = 30
GRID = tuple(range(Q+1))      # values {0,1/14,...,1}
ACTIONS = [(a,b) for a in GRID for b in GRID if a or b]
ACTIONS.sort(key=lambda ab: (-(ab[0]+ab[1]), -abs(ab[0]-ab[1]), -ab[0], -ab[1]))
POLICY = {}

@lru_cache(maxsize=None)
def win(x, y, d):
    assert x <= y
    if x <= TARGET or y <= TARGET:
        return True
    if d == 0:
        return False
    for a,b in ACTIONS:
        # Adversary values for current lower-/higher-safety agents are a/Q,b/Q.
        # Recipient low: (+a,-b); recipient high: (-a,+b), in safety units 1/Q.
        c_low = tuple(sorted((x+a, y-b)))
        c_high = tuple(sorted((x-a, y+b)))
        if win(c_low[0], c_low[1], d-1) and win(c_high[0], c_high[1], d-1):
            POLICY[(x,y,d)] = (a,b,c_low,c_high)
            return True
    return False

# B16/B24 finite Bellman certificate: within the 1/14-grid game, depth 30 is the first
# winning horizon for target safety -17/14.
for d in range(DEPTH):
    assert not win(START[0], START[1], d), f"unexpected win at depth {d}"
assert win(START[0], START[1], DEPTH)

# Independently validate the reachable policy DAG from the winning root.
seen=set(); leaves=[]; action_counts=Counter(); stack=[(*START,DEPTH)]
while stack:
    x,y,d=stack.pop(); key=(x,y,d)
    if key in seen: continue
    seen.add(key)
    assert x <= y
    if x <= TARGET or y <= TARGET:
        leaves.append(key); continue
    assert d>0 and key in POLICY
    a,b,c1,c2=POLICY[key]
    assert 0 <= a <= Q and 0 <= b <= Q and (a or b)
    assert c1 == tuple(sorted((x+a,y-b)))
    assert c2 == tuple(sorted((x-a,y+b)))
    action_counts[(a,b)] += 1
    stack.append((c1[0],c1[1],d-1))
    stack.append((c2[0],c2[1],d-1))

assert leaves
assert all(min(x,y) <= TARGET for x,y,d in leaves)

rows=[]
for key in sorted(seen):
    if key in POLICY:
        x,y,d=key; a,b,c1,c2=POLICY[key]
        rows.append(f"{x},{y},{d}:{a},{b}:{c1[0]},{c1[1]}:{c2[0]},{c2[1]}")
digest=sha256("\n".join(rows).encode()).hexdigest()

# Source-model conversion.
# Phase 1: present three goods of value 1 to both agents. If one agent gets all three,
# the other has safety 2(0+1)-3=-1 and ratio 2/3, already below 445/462.
# In the 2--1 branch, both agents have missed a unit good and the sorted safety state is
# exactly (1,3)=START/Q; thereafter R_i=1 forever because all grid values are <=1.
# The Bellman strategy uses at most 30 more goods, so a terminal failed agent has V_i<=33
# and safety <= -17/14. Hence its PROP1 factor is at most
# 1 - (17/14)/33 = 1 - 17/462 = 445/462.
U = Fraction(445,462)
assert Fraction(2,3) < U
assert Fraction(1,1) - Fraction(17,14*33) == U
assert 3 + DEPTH == 33

print("I0130_GRID14_BELLMAN_CERTIFICATE_PASS")
print("grid_denominator=14")
print("target_safety=-17/14")
print("balanced_start_safety=(1,3)")
print("first_winning_additional_horizon=30")
print("max_total_goods=33")
print("source_valid_upper_bound=445/462")
print(f"cache_states={win.cache_info().currsize}")
print(f"reachable_policy_dag_nodes={len(seen)}")
print(f"reachable_terminal_nodes={len(leaves)}")
print(f"distinct_actions_used={len(action_counts)}")
print("strategy_sha256="+digest)
print("action_counts="+";".join(f"({a}/14,{b}/14):{c}" for (a,b),c in sorted(action_counts.items())))
