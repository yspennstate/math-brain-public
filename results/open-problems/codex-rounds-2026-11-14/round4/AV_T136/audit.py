"""Finite algebra and probability checks; no SK simulation or Lean build."""
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import re
import resource
import sys
import time
from fractions import Fraction as Q

start = time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
assert os.environ.get("OMP_NUM_THREADS") == "1"
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15, priority
root = Path(__file__).resolve().parent
round3 = Path("~/codex_op_1114r3/briefs/AV_T136")
out = {"effective_niceness": priority}

coefficient_cases = 0
for a in (Q(1), Q(4)):
    for L in range(6):
        masses = [a*Q(j+1,L+1) for j in range(L)]
        raw = [Q(0)]*(L+1)
        for i,mass in enumerate(masses,1):
            raw[i] += mass
            raw[i-1] -= mass
        raw[L] -= a
        if L:
            telescoped = [-masses[0]]
            telescoped += [masses[i-1]-masses[i] for i in range(1,L)]
            telescoped += [masses[-1]-a]
        else:
            telescoped = [-a]
        assert raw == telescoped
        assert -sum(raw) == a
        for empty in range(L+1):
            substituted = sum(raw[:empty+1])
            first = masses[empty] if empty < L else a
            assert substituted == -first
            rho = first/2
            assert -(substituted+rho) == first/2
            assert (first-rho)/a == first/a-rho/a
            coefficient_cases += 1
out["exact_coefficient_and_empty_level_cases"] = coefficient_cases
x,a = Q(1,8),Q(4)
rho = x/2
assert x/a-rho/a == Q(1,64)
assert x/a-rho == -Q(1,32)
out["length_four_rate_check"] = {
    "x":str(x),"correct_remaining_normalized_coefficient":str(x/a-rho/a),
    "incorrect_unscaled_rate_coefficient":str(x/a-rho)}

A = math.log(3)/4
b = A/2
K_integral = 1+b*((math.exp(2*b)-1)/b +
                  math.exp(2*A)*math.exp(2*(b-A))/(2*(A-b)))
K_closed = 1.5*math.sqrt(math.sqrt(3))
assert math.isclose(K_integral,K_closed,rel_tol=1e-14)
assert Q(1,2)**-2 == 4
C = 24*K_closed/b**4
right_tail_c = min(1/(4*math.sqrt(C)),1/(16*C))
out["tail_constants"] = {
    "integral":K_integral,"independent_closed_form":K_closed,
    "b":b,"fourth_moment_C":C,"right_tail_c":right_tail_c,
    "scaled_exponential_variance":4}
for j in range(1,51):
    t = j/100
    correction = -math.log1p(-t)-t
    partial = sum(t**k/k for k in range(2,120))
    assert math.isclose(correction,partial,rel_tol=1e-11,abs_tol=1e-16)
    assert correction <= t*t*(1+1e-13)
out["exponential_laplace_series_cases"] = 50

def power_mean(values,mass):
    top = max(values)
    return top+math.log(sum(math.exp(mass*(v-top)) for v in values)/len(values))/mass

def finite_hierarchy(n,a,v1,v2,h1,h2,external=0.0):
    """Gauge-invariant atomic drivers test identities, not Gaussian concavity."""
    spins = list(itertools.product((-1,1),repeat=n))
    edges = list(itertools.combinations(range(n),2))
    edge_atoms = list(itertools.product((-1,1),repeat=len(edges)))
    field_atoms = list(itertools.product((-1,1),repeat=n))
    initial = list(itertools.product(edge_atoms,(-1,1)))
    future2 = list(itertools.product(edge_atoms,field_atoms))
    totals = [0.0]*len(spins)
    pinned_G,original_G = [0.0]*3,[0.0]*3
    max_kernel_error = max_telescope_error = max_root_error = 0.0
    leaf_spin_cases = 0
    for e0,constant in initial:
        rows,F1s = [],[]
        for field1 in field_atoms:
            leaves = []
            for e2,field2 in future2:
                energies = []
                for spin in spins:
                    matrix = sum((0.21*ee0+0.13*ee2)*spin[i]*spin[j]
                                 for (i,j),ee0,ee2 in zip(edges,e0,e2))
                    fields = sum((h1*f1+h2*f2+external)*s
                                 for f1,f2,s in zip(field1,field2,spin))
                    energies.append(matrix+fields+0.17*constant)
                F2 = power_mean(energies,a)
                leaves.append((energies,F2))
            F1 = power_mean([f for _,f in leaves],v2)
            F1s.append(F1)
            rows.append(leaves)
        G = power_mean(F1s,v1)
        test = (1.0,G,G*G)
        for k in range(3):
            original_G[k] += test[k]/len(initial)
        root_mass = 0.0
        for F1,leaves in zip(F1s,rows):
            k1 = math.exp(v1*(F1-G))/len(field_atoms)
            k2sum = 0.0
            for energies,F2 in leaves:
                k2 = math.exp(v2*(F2-F1))/len(future2)
                k2sum += k2
                gibbs = [math.exp(a*(H-F2))/len(spins) for H in energies]
                max_kernel_error = max(max_kernel_error,abs(sum(gibbs)-1))
                root_mass += k1*k2*sum(gibbs)
                for i,pr in enumerate(gibbs):
                    totals[i] += k1*k2*pr/len(initial)
                    leaf_spin_cases += 1
                pin_weight = len(spins)*k1*k2*gibbs[-1]/len(initial)
                for k in range(3):
                    pinned_G[k] += pin_weight*test[k]
                log_product = v1*(F1-G)+v2*(F2-F1)+a*(energies[-1]-F2)
                log_telescope = a*energies[-1]-v1*G-(v2-v1)*F1-(a-v2)*F2
                max_telescope_error = max(max_telescope_error,
                                         abs(log_product-log_telescope))
            max_kernel_error = max(max_kernel_error,abs(k2sum-1))
        max_root_error = max(max_root_error,abs(root_mass-1))
    return {
        "n":n,"a":a,"v1":v1,"v2":v2,"h1":h1,"h2":h2,
        "external":external,"leaf_spin_cases":leaf_spin_cases,
        "max_normalized_kernel_error":max_kernel_error,
        "max_untilted_root_marginal_error":max_root_error,
        "max_telescope_error":max_telescope_error,
        "max_pinned_G_test_error":max(abs(p-q) for p,q in zip(pinned_G,original_G)),
        "max_spin_uniformity_error":max(abs(p-1/len(spins)) for p in totals)}

hierarchies = []
for parameters in (
    (2,1.0,0.2,0.75,0.19,0.11),
    (3,4.0,0.125,0.8,0.16,0.09),
    (2,4.0,0.125,4.0,0.19,0.11),
    (2,1.0,0.25,0.25,0.0,0.11)):
    r = finite_hierarchy(*parameters)
    for key in ("max_normalized_kernel_error","max_untilted_root_marginal_error",
                "max_telescope_error","max_pinned_G_test_error",
                "max_spin_uniformity_error"):
        assert r[key] < 2e-12,(key,r)
    hierarchies.append(r)
out["finite_hierarchies"] = hierarchies
out["total_leaf_spin_cases"] = sum(r["leaf_spin_cases"] for r in hierarchies)
bad = finite_hierarchy(2,1.0,0.2,0.75,0.19,0.11,external=0.7)
assert bad["max_spin_uniformity_error"] > 0.01
assert bad["max_pinned_G_test_error"] > 1e-4
out["deterministic_external_field_countercheck"] = bad

verify = (root/"VERIFY.md").read_text()
fence = chr(96)*3
blocks = re.findall(fence+r"tex\n(.*?)\n"+fence,verify,flags=re.S)
assert len(blocks) == 5
files = ["limiting-law-introduction.tex"]*3+[
    "scale-introduction.tex","zero-temperature-main.tex"]
for block,name in zip(blocks,files):
    assert block in (root/"sources"/name).read_text(),name
out["exact_theorem_quotations"] = len(blocks)
same = {}
for name in files[:1]+files[3:]+[
    "limiting-law-foundations.tex","limiting-law-reduction.tex"]:
    same[name] = ((root/"sources"/name).read_text().rstrip("\n") ==
                  (round3/"sources"/name).read_text().rstrip("\n"))
assert all(same.values()),same
out["fresh_sources_equal_round3"] = same
assert (root/"REPORT.md").read_text().startswith("VERDICT: PROVED ")
for name in ("REPORT.md","VERIFY.md","PROOF.md","LOG.md"):
    txt = (root/name).read_text()
    assert not any(ord(c)<32 and c not in "\n\t" for c in txt),name
out["source_sha256"] = {
    p.name:hashlib.sha256(p.read_bytes()).hexdigest()
    for p in sorted((root/"sources").iterdir()) if p.is_file()}
out["elapsed_seconds"] = time.monotonic()-start
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
out["peak_rss_bytes"] = rss if sys.platform=="darwin" else rss*1024
assert out["peak_rss_bytes"] < 1024**3
assert out["elapsed_seconds"] < 60
result = json.dumps(out,indent=2,ensure_ascii=False)
(root/"audit.txt").write_text(result+"\n")
print(result)
