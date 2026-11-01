"""Finite proof controls, run only under a fresh non-distress local compute gate.

No models, network, SQLite, subprocesses, GPU, or writes outside this folder.
The mathematical proof is ATTEMPT.md; these controls are not a formal proof.
"""
from dataclasses import dataclass
from datetime import datetime
from fractions import Fraction as R
from itertools import combinations, product
import json
import math
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parent

def checkpoint(value):
    (ROOT / "MEASUREMENTS.json").write_text(json.dumps(value, indent=2), encoding="utf-8")

def gate():
    path = Path("~/.claude/compute/compute_state.json")
    now = datetime.now().astimezone()
    try:
        state = json.loads(path.read_text(encoding="utf-8-sig"))
        stamp = datetime.fromisoformat(state["ts"]).astimezone()
        age = (now - stamp).total_seconds()
        row = {"observed_at": now.isoformat(), "sample_age_seconds": age,
               "status": state.get("status"), "mode": state.get("mode"),
               "reasons": state.get("reasons"),
               "cpu_pct": state.get("cpu_pct"), "mem_avail_mb": state.get("mem_avail_mb"),
               "commit_used_pct": state.get("commit_used_pct"),
               "commit_avail_mb": state.get("commit_avail_mb"),
               "hung_windows": state.get("hung_windows")}
        allowed = (0 <= age <= 120 and state.get("status") in ("ok", "warn")
                   and state.get("mode") in ("owner_present_polite", "owner_away_open")
                   and 0 <= float(state["cpu_pct"]) < 90
                   and float(state["mem_avail_mb"]) > 8192
                   and float(state["commit_used_pct"]) < 85
                   and float(state["commit_avail_mb"]) > 16384
                   and state["hung_windows"] == 0)
        row["allowed"] = allowed
        return row
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return {"observed_at": now.isoformat(), "allowed": False, "error": str(exc)}

@dataclass(frozen=True)
class Q2:
    """Exact a + b sqrt(2)."""
    a: R = R(0)
    b: R = R(0)
    def __add__(self, other):
        other = other if isinstance(other, Q2) else Q2(R(other))
        return Q2(self.a + other.a, self.b + other.b)
    __radd__ = __add__
    def __neg__(self):
        return Q2(-self.a, -self.b)
    def __sub__(self, other):
        return self + (-other if isinstance(other, Q2) else -R(other))
    def __rsub__(self, other):
        return Q2(R(other)) - self
    def __mul__(self, other):
        other = other if isinstance(other, Q2) else Q2(R(other))
        return Q2(self.a*other.a + 2*self.b*other.b,
                  self.a*other.b + self.b*other.a)
    __rmul__ = __mul__
    def data(self):
        return {"rational": str(self.a), "sqrt2_coefficient": str(self.b),
                "decimal": float(self.a) + float(self.b)*math.sqrt(2)}

def partition(vertices, edges, bits, terminals):
    parent = list(range(vertices))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for (a,b), bit in zip(edges, bits):
        if bit:
            parent[find(a)] = find(b)
    names = {}
    return tuple(names.setdefault(find(t), len(names)) for t in terminals)

def graph_law(vertices, edges, probabilities, terminals):
    choices = [(0,) if p == 0 else (1,) if p == 1 else (0,1) for p in probabilities]
    law = {}
    count = 0
    for bits in product(*choices):
        mass = Q2(R(1)) if isinstance(probabilities[0], Q2) else R(1)
        for p, bit in zip(probabilities, bits):
            mass *= p if bit else 1-p
        part = partition(vertices, edges, bits, terminals)
        law[part] = law.get(part, 0) + mass
        count += 1
    return law, count

def partitions(n):
    def rec(prefix):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for value in range(max(prefix) + 2):
            yield from rec(prefix + [value])
    yield from rec([0])

def connected_with_exterior(states, exterior):
    parent = list(range(5))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    def glue(part, terminals):
        blocks = {}
        for label, vertex in zip(part, terminals):
            if label in blocks:
                parent[find(vertex)] = find(blocks[label])
            else:
                blocks[label] = vertex
    glue(exterior, range(5))
    for state, terminals in zip(states, [(0,1,2), (2,3,4)]):
        glue(state, terminals)
    return int(find(0) == find(4))

def expectation(laws, exterior):
    value = R(0)
    for states in product(*(list(law) for law in laws)):
        mass = R(1)
        for law, state in zip(laws, states):
            mass *= law[state]
        value += mass * connected_with_exterior(states, exterior)
    return value

def run_controls():
    g = gate()
    result = {"command": "python -B -X utf8 ~/brain_workers/w411/verify_finite.py",
              "gate": g, "status": "BLOCKED_BY_COMPUTE_GATE", "checks_executed": 0,
              "mathematical_proof": "ATTEMPT.md; self-authored, independent review pending",
              "formal_check": False}
    checkpoint(result)
    if not g["allowed"]:
        print(json.dumps(result, indent=2))
        return 2
    started = time.perf_counter()
    cases = states_checked = both_extremes = 0
    edges = list(combinations(range(4), 2))
    for probabilities in product([R(0), R(1,2), R(1)], repeat=6):
        for k in (3,4):
            law, count = graph_law(4, edges, probabilities, range(k))
            cases += 1
            states_checked += count
            assert sum(law.values()) == 1
            top, bottom = (0,)*k, tuple(range(k))
            intermediate = sum(v for key,v in law.items() if key not in (top,bottom))
            optional = sum(p == R(1,2) for p in probabilities)
            if law.get(top,0) and law.get(bottom,0):
                both_extremes += 1
                assert intermediate >= R(1,2)**optional
            target = {top:R(1,2), bottom:R(1,2)}
            tv = sum(abs(law.get(key,0)-target.get(key,0)) for key in law.keys() | target.keys())/2
            assert tv >= min(R(1,2), R(1,2)**optional)
    result.update(status="PARTIAL_PASS", finite_graph_laws=cases,
                  configurations=states_checked, both_extremes_cases=both_extremes)
    checkpoint(result)

    s = Q2(R(0), R(1,2))
    star, star_states = graph_law(4, [(0,3),(1,3),(2,3)], [s]*3, range(3))
    selector = {(0,0,0):Q2(R(1,2)), (0,1,2):Q2(R(1,2))}
    pair_passes = 0
    for a,b in combinations(range(3),2):
        star_pair = sum(m for part,m in star.items() if part[a] == part[b])
        site_pair = sum(m for part,m in selector.items() if part[a] == part[b])
        assert star_pair == site_pair == Q2(R(1,2))
        pair_passes += 1
    star_cross = sum(m for part,m in star.items() if part[0] == part[1] or part[2] == part[1])
    site_cross = sum(m for part,m in selector.items() if part[0] == part[1] or part[2] == part[1])
    defect = star_cross - site_cross
    assert defect == Q2(R(1,2), R(-1,4))
    assert star != selector
    result.update(pair_marginal_controls_pass=pair_passes, star_configurations=star_states,
                  wired_crossing_defect=defect.data(),
                  before_pair_only_false_acceptances=1, after_full_partition_false_acceptances=0,
                  scope="One constructed counterexample and exhaustive K4 finite controls; no scaling-limit experiment")
    checkpoint(result)

    local, _ = graph_law(4, [(0,3),(1,3),(2,3)], [R(1,2)]*3, range(3))
    site = {(0,0,0):R(1,2), (0,1,2):R(1,2)}
    mu, nu = [local,site], [site,local]
    hybrid_checks = 0
    for exterior in partitions(5):
        delta = expectation(nu,exterior)-expectation(mu,exterior)
        signed = R(0)
        bound = R(0)
        for i in range(2):
            other = 1-i
            exterior_law = nu[other] if other < i else mu[other]
            local_keys = mu[i].keys() | nu[i].keys()
            tv = sum(abs(nu[i].get(t,0)-mu[i].get(t,0)) for t in local_keys)/2
            oscillation_mean = R(0)
            for state_other, mass in exterior_law.items():
                outcomes = []
                for state_i in local_keys:
                    states = [None,None]
                    states[i],states[other] = state_i,state_other
                    f = connected_with_exterior(states,exterior)
                    outcomes.append(f)
                    signed += mass*(nu[i].get(state_i,0)-mu[i].get(state_i,0))*f
                oscillation_mean += mass*(max(outcomes)-min(outcomes))
            bound += tv*oscillation_mean
        assert signed == delta
        assert abs(delta) <= bound
        hybrid_checks += 1
    assert hybrid_checks == 52
    # Assumption controls: two terminals permit a fair independent bond selector;
    # three correlated arms permit a fair selector. Neither is covered by L2.
    two_terminal, _ = graph_law(2, [(0,1)], [R(1,2)], range(2))
    assert two_terminal == {(0,0):R(1,2), (0,1):R(1,2)}
    correlated = {}
    for bits in [(0,0,0), (1,1,1)]:
        key = partition(4, [(0,3),(1,3),(2,3)], bits, range(3))
        correlated[key] = correlated.get(key,0) + R(1,2)
    assert correlated == site
    result.update(status="PASS", hybrid_exterior_wirings=hybrid_checks,
                  assumption_negative_controls=2, checks_executed=cases+pair_passes+hybrid_checks+2,
                  elapsed_control_seconds=time.perf_counter()-started)
    checkpoint(result)
    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(run_controls())
