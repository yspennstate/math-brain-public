"""Verify endpoint mixture and joint-hit kernels on a four-cycle, exactly."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json
import time

root = Path(__file__).resolve().parent
start = time.monotonic()
gate = json.loads((root / "kernel_compute_gate.json").read_text(encoding="utf-8"))
n = gate["maximum_cycle_vertices"]
assert n == 4 and 2**n <= gate["maximum_spin_configurations_per_case"] and 4**n <= gate["maximum_trace_pairs_per_case"]
r, s, t = F(2,5), F(3,5), F(4,5)
B = (0,1,3)
Bmask = sum(1<<v for v in B)

def rotated(mask,y):
    return sum(1<<((i+y)%n) for i in range(n) if mask & (1<<i))

def component(trace,anchor):
    seen = {anchor}
    todo = [anchor]
    while todo:
        v = todo.pop()
        for edge,u in [(v,(v+1)%n),((v-1)%n,(v-1)%n)]:
            if trace & (1<<edge) and u not in seen:
                seen.add(u)
                todo.append(u)
    return sum(1<<v for v in seen)

@lru_cache(None)
def current(a,b):
    source = (1<<a) ^ (1<<b)
    odd = []
    for mask in range(1<<n):
        parity = 0
        for edge in range(n):
            if mask & (1<<edge):
                parity ^= (1<<edge) ^ (1<<((edge+1)%n))
        if parity == source:
            odd.append(mask)
    Z = sum(t**o.bit_count() for o in odd)
    law = []
    for trace in range(1<<n):
        mass = sum(t**o.bit_count()/Z * r**(trace.bit_count()-o.bit_count()) * s**(n-trace.bit_count())
                   for o in odd if o & trace == o)
        law.append(mass)
    assert sum(law) == 1
    return tuple(law)

# Enumerate Gibbs spins separately. At t_current=log 3 each aligned bond has
# weight 9 and each misaligned bond has weight 1 after a common rescaling.
spin_weights = []
for mask in range(1<<n):
    sigma = [1 if mask & (1<<i) else -1 for i in range(n)]
    aligned = sum(sigma[i] == sigma[(i+1)%n] for i in range(n))
    spin_weights.append((sigma,9**aligned))
Zspin = sum(weight for _,weight in spin_weights)
moments = []
for subset in range(1<<n):
    total = 0
    for sigma,weight in spin_weights:
        product = 1
        for v in range(n):
            if subset & (1<<v):
                product *= sigma[v]
        total += weight*product
    moments.append(F(total,Zspin))
G = [moments[1^(1<<v)] for v in range(n)]
chi = sum(G)
mu = [g/chi for g in G]
law0 = [sum(mu[x]*current(0,x)[trace] for x in range(n)) for trace in range(1<<n)]

def law_at(y):
    shifted = [F(0)]*(1<<n)
    for trace,mass in enumerate(law0):
        shifted[rotated(trace,y)] += mass
    return shifted

k = [sum(mass for trace,mass in enumerate(law0) if component(trace,0)&(1<<v)) for v in range(n)]
k2 = [[sum(mass for trace,mass in enumerate(law0)
           if component(trace,0)&(1<<u) and component(trace,0)&(1<<v)) for v in range(n)] for u in range(n)]
first = second = QB = F(0)
Qy = []
for y in range(n):
    shifted = law_at(y)
    q = F(0)
    for left in range(1<<n):
        for right in range(1<<n):
            mass = law0[left]*shifted[right]
            connected = bool(component(left|right,0)&(1<<y))
            q += mass*connected
            if y in B:
                N = (component(left,0)&component(right,y)&Bmask).bit_count()
                first += mass*N/len(B)
                second += mass*N*N/len(B)
                QB += mass*connected/len(B)
    Qy.append(q)
first_kernel = sum(k[v]*sum(k[(v-y)%n] for y in B) for v in B)/len(B)
second_kernel = sum(k2[u][v]*sum(k2[(u-y)%n][(v-y)%n] for y in B) for u in B for v in B)/len(B)

u4_sum = F(0)
for x in range(n):
    for y in range(n):
        for z in range(n):
            u4_sum += moments[1^(1<<x)^(1<<y)^(1<<z)] - G[x]*G[(z-y)%n] - G[y]*G[(z-x)%n] - G[z]*G[(y-x)%n]
checks = [first==first_kernel, second==second_kernel, QB>=first*first/second,
          -u4_sum==2*chi*chi*sum(Qy)]
augmented_k = []
for v in range(n):
    enlarged = sum(law0[left]*current(0,0)[right]
                   for left in range(1<<n) for right in range(1<<n) if component(left|right,0)&(1<<v))
    augmented_k.append(enlarged)
    checks += [enlarged==G[v], G[v]/chi<=k[v]<=G[v]]
assert all(checks), checks
elapsed = time.monotonic()-start
assert elapsed<=gate["hard_loop_deadline_seconds"]
receipt = {"command":"python -X utf8 verify_kernels.py","status":"PASS","cases":1,"checks_passed":len(checks),
           "arithmetic":"exact rational, including all repeated endpoint tuples","elapsed_seconds":elapsed,
           "graph":"four-cycle with t=log(3)","spin_configurations":16,"maximum_trace_pairs":256,
           "chi":str(chi),"m1":str(first),"m2":str(second),"Q_B":str(QB),"m2_over_m1_squared":str(second/(first*first)),
           "k_original":[str(v) for v in k],"k_augmented":[str(v) for v in augmented_k],
           "limitations":"Finite translation-invariant graph only; does not establish UCM in critical Z^3."}
(root/"kernel_verification.json").write_text(json.dumps(receipt,indent=2),encoding="utf-8")
print(json.dumps(receipt,indent=2))
