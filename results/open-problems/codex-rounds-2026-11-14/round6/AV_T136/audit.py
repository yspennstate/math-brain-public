"""Exact finite-depth compression checks. Standard library; no simulation."""
from collections import defaultdict
from fractions import Fraction as Q
from functools import lru_cache
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

started = time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
assert os.environ.get("OMP_NUM_THREADS") == "1"
priority = os.getpriority(os.PRIO_PROCESS, 0)
assert priority >= 15
root = Path(__file__).resolve().parent
out = {"effective_niceness": priority}

@lru_cache(None)
def partitions(slots):
    """Each unordered set partition once, blocks ordered by their first slot."""
    if not slots:
        return ((),)
    first, rest = slots[0], slots[1:]
    result = []
    for p in partitions(rest):
        result.append(((first,),) + p)
        for i, block in enumerate(p):
            q = list(p)
            q[i] = (first,) + block
            result.append(tuple(sorted(q, key=lambda b: b[0])))
    return tuple(result)

@lru_cache(None)
def shapes(slots, depth):
    if depth == 0:
        return (slots,)
    return tuple(tuple(children)
                 for p in partitions(slots)
                 for children in itertools.product(
                     *(shapes(block, depth-1) for block in p)))

def falling(x, n):
    return math.prod((x-i for i in range(n)), start=Q(1))

@lru_cache(None)
def count_weight(tree, masses):
    if len(masses) == 1:
        return Q(1)
    return (falling(masses[0]/masses[1], len(tree)) *
            math.prod((count_weight(t, masses[1:]) for t in tree),
                      start=Q(1)))

def restrict(tree, subset, depth):
    if depth == 0:
        ans = tuple(x for x in tree if x in subset)
        return ans or None
    ans = tuple(r for t in tree
                if (r := restrict(t, subset, depth-1)) is not None)
    def first_slot(t, d):
        return t[0] if d == 0 else first_slot(t[0],d-1)
    return tuple(sorted(ans,key=lambda t:first_slot(t,depth-1))) or None

def nonzero(d):
    return {k: v for k, v in d.items() if v}

# Coefficientwise tests: the restricted topologies remain distinct symbols.
# These tests do not rely on any choice of scalar moments.
mass_sets = [
    (Q(1,8), Q(1)),
    (Q(1,8), Q(1,3), Q(1)),
    (Q(1,8), Q(1,3), Q(2,3), Q(1)),
    (Q(1,8), Q(1,8), Q(1)),
    (Q(1), Q(1), Q(1)),
    (Q(1,8), Q(1,2), Q(4)),
    (Q(6), Q(3), Q(1)),
    (Q(1,1000000), Q(1,7), Q(1)),
]
identities = coefficients = global_shapes = 0
for masses in mass_sets:
    depth = len(masses)-1
    for k in range(1,5):
        slots = tuple(range(k))
        ts = shapes(slots,depth)
        global_shapes += len(ts)
        for colors in partitions(slots):
            lhs = defaultdict(Q)
            for tree in ts:
                key = tuple(restrict(tree,frozenset(s),depth) for s in colors)
                lhs[key] += count_weight(tree,masses)
            rhs = {}
            for tup in itertools.product(*(shapes(s,depth) for s in colors)):
                rhs[tup] = math.prod(
                    (count_weight(t,masses) for t in tup),start=Q(1))
            assert nonzero(lhs) == nonzero(rhs), (masses,k,colors)
            identities += 1
            coefficients += len(rhs)
out["marked_refinement_checks"] = {
    "identities":identities, "restricted_shape_coefficients":coefficients,
    "global_shapes_in_mass_order_sweeps":global_shapes,
    "mass_vectors":[[str(m) for m in ms] for ms in mass_sets],
    "slots_per_block":"all 1 through 4; all color set partitions",
}

# Independently count actual assignments in a regular named-child tree.
def shape_from_assignments(slots, paths, level, depth):
    if level == depth:
        return slots
    groups = {}
    for s in slots:
        groups.setdefault(paths[s][level], []).append(s)
    ordered = sorted(groups.values(), key=lambda g:g[0])
    return tuple(shape_from_assignments(tuple(g),paths,level+1,depth)
                 for g in ordered)

assignment_cases = 0
named_ratios = ((2,), (3,), (4,), (2,2), (2,3), (4,4), (2,2,2))
for ratios in named_ratios:
    depth = len(ratios)
    masses = [Q(1)]
    for p in reversed(ratios):
        masses.insert(0,masses[0]*p)
    masses = tuple(masses)
    paths = tuple(itertools.product(*(range(p) for p in ratios)))
    for k in (1,2,3,4):
        slots = tuple(range(k))
        counts = defaultdict(int)
        for assignment in itertools.product(paths,repeat=k):
            counts[shape_from_assignments(slots,assignment,0,depth)] += 1
            assignment_cases += 1
        for t in shapes(slots,depth):
            assert counts[t] == count_weight(t,masses), (ratios,k,t)
assignment_formula = sum(sum(math.prod(p)**k for k in (1,2,3,4))
                         for p in named_ratios)
assert assignment_cases == assignment_formula
out["independent_named_leaf_assignments"] = assignment_cases
out["independent_assignment_count_formula"] = assignment_formula

# Direct source jets from the generalized binomial series, independently of
# trees and cumulants: cosh(a(z+t))/cosh(az) has rational coefficients when
# tanh(az)=mu is rational.
def poly_mul(p,q,degree):
    r = [Q(0)]*(degree+1)
    for i,v in enumerate(p):
        for j,w in enumerate(q):
            if i+j <= degree:
                r[i+j] += v*w
    return r

@lru_cache(None)
def source_jets(c,a,mu,degree):
    u = [Q(0)] + [a**k*(mu if k%2 else 1)/math.factorial(k)
                      for k in range(1,degree+1)]
    power = [Q(1)] + [Q(0)]*degree
    result = [Q(0)]*(degree+1)
    for q in range(degree+1):
        coefficient = falling(c/a,q)/math.factorial(q)
        result = [x+coefficient*y for x,y in zip(result,power)]
        power = poly_mul(power,u,degree)
    return tuple(result[k]*math.factorial(k) for k in range(degree+1))

def terminal_moment(tree,depth,mu):
    if depth == 0:
        return mu if len(tree)%2 else Q(1)
    return math.prod((terminal_moment(t,depth-1,mu) for t in tree),
                     start=Q(1))

source_cases = 0
for masses in mass_sets:
    depth = len(masses)-1
    for mu in (Q(0),Q(1,3),Q(-2,5)):
        jets = source_jets(masses[0],masses[-1],mu,4)
        for k in range(1,5):
            total = sum((masses[-1]**k*count_weight(t,masses)*
                         terminal_moment(t,depth,mu)
                         for t in shapes(tuple(range(k)),depth)),Q(0))
            assert total == jets[k],(masses,mu,k,total,jets[k])
            source_cases += 1
out["source_derivatives_vs_independent_binomial_jets"] = source_cases

# Full direct cumulant sums on explicit graph families, with zero future
# Gaussian increments and nonzero fixed cut fields.  Topology coefficients
# are still signed and all coincidences are retained.
graphs = [
    ((0,1),(0,1)),
    ((0,1),(0,2)),
    ((0,1),(2,3)),
    ((0,1),(0,1),(0,1)),
    ((0,1),(1,2),(2,0)),
    ((0,1),(0,2),(0,3)),
    ((0,1),(1,2),(2,3)),
    ((0,1),(0,1),(0,1),(0,1)),
    ((0,1),(1,2),(2,3),(3,0)),
    ((0,1),(0,2),(0,3),(0,4)),
    ((0,1),(2,3),(4,5),(6,7)),
    ((0,1),(0,1),(1,2),(2,0)),
]
def cumulant_weight(pi):
    return (-1)**(len(pi)-1)*math.factorial(len(pi)-1)

graph_results = []
for masses in ((Q(1,8),Q(1)), (Q(1,8),Q(1,3),Q(1))):
    depth = len(masses)-1
    for graph in graphs:
        j = len(graph)
        blocks = sorted({v for edge in graph for v in edge})
        slots = {b:tuple(2*i+end for i,e in enumerate(graph)
                        for end,v in enumerate(e) if v==b) for b in blocks}
        mu = {b:Q(b+1,2*b+3) for b in blocks}
        pis = partitions(tuple(range(j)))
        topology_sum = Q(0)
        placements = 0
        # A part's terminal spin moment depends on its induced shape.
        part_slots = {
            (pi,P,b): frozenset(2*i+end for i in P for end,v in enumerate(graph[i])
                                if v==b)
            for pi in pis for P in pi for b in blocks
        }
        # Cache per-block restrictions before forming graph placements.
        options = {}
        for b in blocks:
            options[b] = []
            for tree in shapes(slots[b],depth):
                w = masses[-1]**len(slots[b])*count_weight(tree,masses)
                moments = {}
                for pi in pis:
                    for P in pi:
                        sub = part_slots[pi,P,b]
                        moments[pi,P] = (terminal_moment(
                            restrict(tree,sub,depth),depth,mu[b])
                            if sub else Q(1))
                options[b].append((w,moments))
        for choice in itertools.product(*(options[b] for b in blocks)):
            w = math.prod((v[0] for v in choice),start=Q(1))
            cum = Q(0)
            for pi in pis:
                term = math.prod((math.prod((v[1][pi,P] for v in choice),
                                           start=Q(1)) for P in pi),start=Q(1))
                cum += cumulant_weight(pi)*term
            topology_sum += w*cum
            placements += 1
        # Compressed expression uses only independently computed source jets.
        jets = {b:source_jets(masses[0],masses[-1],mu[b],j) for b in blocks}
        compressed = Q(0)
        for pi in pis:
            term = Q(cumulant_weight(pi))
            for P in pi:
                for b in blocks:
                    k = len(part_slots[pi,P,b])
                    if k:
                        term *= jets[b][k]
            compressed += term
        assert topology_sum == compressed,(masses,graph,topology_sum,compressed)
        graph_results.append({
            "masses":[str(m) for m in masses],"edges":graph,
            "full_internal_placements":placements,"value":str(compressed)})
out["direct_cumulant_vs_compressed_source"] = graph_results

# A third, four-placement evaluation of the load-bearing repeated-edge case.
c = Q(1,8)
muA,muB = Q(1,3),Q(2,5)
four_placements = (c*c*(1-muA*muA*muB*muB) +
                   c*c*(c-1)*(muA*muA+muB*muB-2*muA*muA*muB*muB))
source_manual = Q(65,576)*Q(43,400)-Q(1,480)**2
assert four_placements == source_manual == Q(1397,115200)
assert graph_results[0]["value"] == str(four_placements)
out["independent_repeated_edge_value"] = {
    "four_placement_covariances":str(four_placements),
    "manual_source_derivatives":str(source_manual)}

# Deliberately invalid deletion: distinct terminal labels across colors.
c,a = Q(1,8),Q(1)
same,distinct = c*a,c*(c-a)
assert same+distinct == c*c
assert distinct != c*c
out["cross_part_coincidence_countercheck"] = {
    "same_terminal":str(same),"distinct_terminal":str(distinct),
    "correct_sum":str(same+distinct),"incorrect_without_coincidence":str(distinct)}

# Source and quotation provenance. Copied context is distinguished in INDEX.md.
old = Path("~/codex_op_1114r5/briefs/AV_T136")
fresh = ["01-introduction.tex","09-expansion.tex","scale-introduction.tex",
         "zero-temperature-main.tex","EventuallyNatPos.lean","281.md",
         "fluctuations-palomar-README.md"]
out["fresh_sources_match_round5"] = {
    n:(root/"sources"/n).read_text().rstrip("\n") ==
      (old/"sources"/n).read_text().rstrip("\n") for n in fresh}
assert all(out["fresh_sources_match_round5"].values())
fence = chr(96)*3
quotes = re.findall(fence+r"tex\n(.*?)\n"+fence,
                    (root/"VERIFY.md").read_text(),re.S)
assert len(quotes) == 5
for q,n in zip(quotes,["01-introduction.tex"]*3+
               ["scale-introduction.tex","zero-temperature-main.tex"]):
    assert q in (root/"sources"/n).read_text()
out["exact_theorem_quotations"] = len(quotes)
out["source_sha256"] = {
    p.name:hashlib.sha256(p.read_bytes()).hexdigest()
    for p in sorted((root/"sources").iterdir()) if p.is_file()}
for n in ("LOG.md","PROOF.md","VERIFY.md","REPORT.md"):
    assert not any(ord(c)<32 and c not in "\n\t" for c in (root/n).read_text())
out["elapsed_seconds"] = time.monotonic()-started
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
out["peak_rss_bytes"] = rss if sys.platform=="darwin" else rss*1024
assert out["peak_rss_bytes"] < 1024**3
assert out["elapsed_seconds"] < 120
text = json.dumps(out,indent=2,ensure_ascii=False)
(root/"audit.txt").write_text(text+"\n")
print(text)
