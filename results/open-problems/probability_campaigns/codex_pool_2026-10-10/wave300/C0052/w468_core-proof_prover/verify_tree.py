"""Independent exact checks of the current formulas against spin enumeration.

Compute gate: compute_gate.json. No models, GPUs, training, or network.
Run: python -X utf8 verify_tree.py
"""
from fractions import Fraction as F
from pathlib import Path
import json
import time

root = Path(__file__).resolve().parent
gate = json.loads((root / "compute_gate.json").read_text(encoding="utf-8"))
start = time.monotonic()

def deadline():
    if time.monotonic() - start > gate["hard_loop_deadline_seconds"]:
        raise TimeoutError("Exact verification exceeded its fresh compute gate")

def support_numerator(mask, size, on, off):
    count = mask.bit_count()
    return on ** count * off ** (size - count)

def spin_moments(m):
    vertices = m + 3
    assert 2 ** vertices <= gate["maximum_spin_configurations_per_case"]
    totals = {"Z": 0, "ab": 0, "cd": 0, "ac": 0, "bd": 0, "ad": 0, "bc": 0, "abcd": 0}
    a, b, c, d = 0, 1, m + 1, m + 2
    for mask in range(1 << vertices):
        spins = [1 if mask & (1 << i) else -1 for i in range(vertices)]
        aligned = sum(spins[i] == spins[i+1] for i in range(vertices-1))
        # e^t=3. Multiply every Gibbs weight by 3^(number of edges):
        # aligned edge weight is 9 and opposite-spin edge weight is 1.
        weight = 9 ** aligned
        totals["Z"] += weight
        for name, i, j in [("ab",a,b),("cd",c,d),("ac",a,c),("bd",b,d),("ad",a,d),("bc",b,c)]:
            totals[name] += weight * spins[i] * spins[j]
        totals["abcd"] += weight * spins[a] * spins[b] * spins[c] * spins[d]
    return {name: F(value, totals["Z"]) for name,value in totals.items() if name != "Z"}

def trace_checks(m):
    pairs = 4 ** m
    assert pairs <= gate["maximum_trace_pairs_per_case"]
    all_edges = (1 << m) - 1
    original_num = meeting_num = first_num = second_num = 0
    r_weights = [support_numerator(mask,m,2,3) for mask in range(1<<m)]
    p_weights = [support_numerator(mask,m,16,9) for mask in range(1<<m)]
    for left in range(1 << m):
        deadline()
        l_run = 0
        while l_run < m and left & (1 << l_run):
            l_run += 1
        for right in range(1 << m):
            if left | right == all_edges:
                original_num += r_weights[left] * r_weights[right]
            r_run = 0
            while r_run < m and right & (1 << (m-1-r_run)):
                r_run += 1
            contacts = max(0, l_run + r_run - m + 1)
            weight = p_weights[left] * p_weights[right]
            meeting_num += weight * (contacts > 0)
            first_num += weight * contacts
            second_num += weight * contacts * contacts
    return F(original_num,5**(2*m)), F(meeting_num,25**(2*m)), F(first_num,25**(2*m)), F(second_num,25**(2*m))

rows = []
checks = 0
p, r = F(16,25), F(2,5)
for m in range(1,gate["maximum_bridge_edges"]+1):
    q, augmented, first, second = trace_checks(m)
    spin = spin_moments(m)
    u4 = spin["abcd"]-spin["ab"]*spin["cd"]-spin["ac"]*spin["bd"]-spin["ad"]*spin["bc"]
    expected_second = p**m * (m+1 + 2*sum(F(m+1-k)*p**k for k in range(1,m+1)))
    assertions = [
        q == p**m,
        augmented == (1+m*(1-p))*p**m,
        first == (m+1)*p**m,
        second == expected_second,
        u4 == -2*spin["ab"]*spin["cd"]*q,
        spin["bc"]*spin["ac"]/spin["ab"] == p**m,
        F(2**m,5**m) / (spin["bc"]*spin["ac"]/spin["ab"]) == F(5,8)**m,
    ]
    assert all(assertions), (m, assertions)
    checks += len(assertions)
    rows.append({"m":m,"spin_configurations":2**(m+3),"trace_pairs":4**m,"original_q":str(q),
                 "augmented_meeting":str(augmented),"contact_first":str(first),"contact_second":str(second),
                 "U4":str(u4),"checks_passed":len(assertions)})

receipt = {
    "command":"python -X utf8 verify_tree.py", "status":"PASS", "arithmetic":"exact rational and integer",
    "cases":len(rows), "checks_passed":checks, "elapsed_seconds":time.monotonic()-start, "rows":rows,
    "measurement_at_m100": {"coupling":"t=log(3)","original_over_augmented":"1/37",
                            "single_over_augmented_occupation":str(F(5,8)**100)},
    "limitations":"Finite paths only; no formal proof assistant, no audit, no asymptotic Z^3 evidence."
}
(root / "verification.json").write_text(json.dumps(receipt,indent=2),encoding="utf-8")
print(json.dumps({k:v for k,v in receipt.items() if k != "rows"},indent=2))
