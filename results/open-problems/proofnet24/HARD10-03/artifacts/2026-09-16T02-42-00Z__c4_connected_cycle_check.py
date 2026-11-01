#!/usr/bin/env python3
"""Finite-state certificate for HARD10-03 NEW-L48 and the termwise-kernel counterexample.

This is a sanity/counterexample certificate, not a proof of the infinite-volume theorem.
It exactly exponentiates the interchange generator on C4.
"""

import itertools
import json
import numpy as np
from scipy.linalg import expm

N = 4
EDGES = [(0,1),(1,2),(2,3),(3,0)]
BETA = 1.0

def all_perms(n):
    return list(itertools.permutations(range(n)))

def ring(p, edge):
    """p maps label -> position; an edge ring swaps the labels at those positions."""
    a,b = edge
    q = list(p)
    ia = p.index(a)
    ib = p.index(b)
    q[ia], q[ib] = b, a
    return tuple(q)

def interchange_generator(n, edges):
    ps = all_perms(n)
    idx = {p:i for i,p in enumerate(ps)}
    Q = np.zeros((len(ps),len(ps)))
    for i,p in enumerate(ps):
        for e in edges:
            q = ring(p,e)
            j = idx[q]
            Q[i,j] += 1.0
            Q[i,i] -= 1.0
    return ps, idx, Q

def one_particle_kernel(n, edges, t):
    L = np.zeros((n,n))
    for a,b in edges:
        L[a,a] += 1.0
        L[b,b] += 1.0
        L[a,b] -= 1.0
        L[b,a] -= 1.0
    return expm(-t*L)

def root_cycle(p,u):
    c=[]
    x=u
    while x not in c:
        c.append(x)
        x=p[x]
    return c

ps, idx, Q = interchange_generator(N, EDGES)
identity = tuple(range(N))
mu = expm(BETA*Q)[idx[identity]]
K = one_particle_kernel(N, EDGES, BETA)

pair_checks = []
max_signed_error = 0.0
max_connected_bound_violation = 0.0

for u,v in itertools.combinations(range(N),2):
    fixed = 0.0
    swap = 0.0
    for prob,pmt in zip(mu,ps):
        if pmt[u] == u and pmt[v] == v:
            fixed += float(prob)
        if pmt[u] == v and pmt[v] == u:
            swap += float(prob)
    q_u = float(K[u,u])
    q_v = float(K[v,v])
    p_uv = float(K[u,v])
    signed_rhs = q_u*q_v - p_uv*p_uv
    sr_return_bound = float((q_u+p_uv)*(q_v+p_uv))
    connected_bound = 0.5*(sr_return_bound - signed_rhs)
    signed_error = abs((fixed-swap)-signed_rhs)
    bound_violation = swap-connected_bound
    max_signed_error=max(max_signed_error,signed_error)
    max_connected_bound_violation=max(max_connected_bound_violation,bound_violation)
    pair_checks.append({
        "pair":[u,v],
        "P_fixed_both":fixed,
        "P_two_cycle":swap,
        "signed_lhs_fixed_minus_two_cycle":fixed-swap,
        "signed_rhs_det_K_pair":signed_rhs,
        "signed_error":signed_error,
        "strong_rayleigh_return_upper":sr_return_bound,
        "NEW_L48_upper":connected_bound,
        "upper_minus_two_cycle":connected_bound-swap
    })

# Termwise first-return/killed-kernel counterexample.
S = [0,1,3]
u = 0
m = 2
lhs = 0.0
for prob,pmt in zip(mu,ps):
    cyc = root_cycle(pmt,u)
    if len(cyc)==m and set(cyc).issubset(S):
        lhs += float(prob)

KS = K[np.ix_(S,S)]
u_idx = S.index(u)
rhs = float(np.linalg.matrix_power(KS,m)[u_idx,u_idx])
ratio = lhs/rhs

sum_two = 0.0
sum_upper = 0.0
q = float(K[0,0])
for v in range(1,N):
    tprob = 0.0
    for prob,pmt in zip(mu,ps):
        if pmt[0] == v and pmt[v] == 0:
            tprob += float(prob)
    sum_two += tprob
    sum_upper += 2.0*q*float(K[0,v])

result = {
    "graph":"C4",
    "edge_rates":"all 1",
    "beta":BETA,
    "one_particle_kernel":K.tolist(),
    "pair_checks":pair_checks,
    "max_signed_identity_error":max_signed_error,
    "max_NEW_L48_bound_violation":max_connected_bound_violation,
    "summed_two_cycle_probability_at_root":sum_two,
    "summed_NEW_L48_upper":sum_upper,
    "termwise_counterexample":{
        "S":S,
        "u":u,
        "m":m,
        "lhs_P_cycle_length_m_and_contained":lhs,
        "rhs_KS_power_m_uu":rhs,
        "ratio_lhs_over_rhs":ratio,
        "violates_termwise_domination":bool(lhs>rhs+1e-12)
    },
    "PASS_NEW_L48": bool(max_signed_error < 1e-12 and max_connected_bound_violation <= 1e-12),
    "PASS_COUNTEREXAMPLE": bool(lhs>rhs+1e-12)
}
print(json.dumps(result, indent=2, sort_keys=True))
