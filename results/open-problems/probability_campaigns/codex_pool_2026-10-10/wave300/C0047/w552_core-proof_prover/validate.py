"""Bounded, single-process checks of author lemmas; no theorem certification."""
from __future__ import annotations

import ctypes
import json
import math
import os
import time
from datetime import datetime, timezone
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
START = time.monotonic()
DEADLINE = START + 20


def deadline():
    if time.monotonic() > DEADLINE:
        raise RuntimeError("20-second validation budget exceeded")


def gate(receipt_name="COMPUTE_GATE.json"):
    class Memory(ctypes.Structure):
        _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong)] + [
            (name, ctypes.c_ulonglong) for name in (
                "ullTotalPhys", "ullAvailPhys", "ullTotalPageFile", "ullAvailPageFile",
                "ullTotalVirtual", "ullAvailVirtual", "ullAvailExtendedVirtual"
            )
        ]
    m = Memory()
    m.dwLength = ctypes.sizeof(m)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m)):
        raise RuntimeError("fresh Windows commit measurement unavailable")
    policy_path = Path("~/brain_workers/GATE.json")
    policy = json.loads(policy_path.read_text(encoding="utf-8-sig"))
    spare_gb = m.ullAvailPageFile / 1024**3
    result = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "policy_path": str(policy_path), "policy": policy,
        "commit_spare_gb": spare_gb, "available_physical_gb": m.ullAvailPhys / 1024**3,
        "allowed": spare_gb >= float(policy["commit_floor_gb"]),
        "scope": "existing worker foreground validation only, no additional agent or pool slot",
        "limits": {"wall_seconds": 20, "single_process": True, "threads": 1,
                   "max_percolation_edges": 6, "max_nonbacktracking_length": 6,
                   "gpu": False, "training": False},
        "not_a_formal_or_mathematical_proof_receipt": True,
    }
    (HERE / receipt_name).write_text(json.dumps(result, indent=2), encoding="utf-8")
    if not result["allowed"]:
        print(json.dumps({"validation": "SKIPPED", "reason": "commit gate denied", "gate": result}))
        raise SystemExit(3)
    return result


def connected(n, edges, mask):
    roots = list(range(n))
    def find(x):
        while roots[x] != x:
            x = roots[x]
        return x
    for k, (u, v) in enumerate(edges):
        if mask & (1 << k):
            roots[find(u)] = find(v)
    return [find(x) for x in range(n)]


def two_point(n, edges, p):
    m = len(edges)
    assert m <= 6
    t = [[Q(0) for _ in range(n)] for _ in range(n)]
    derivative = [[Q(0) for _ in range(n)] for _ in range(n)]
    for mask in range(1 << m):
        k = mask.bit_count()
        prob = p**k * (1-p)**(m-k)
        score = Q(k)/p - Q(m-k)/(1-p)
        roots = connected(n, edges, mask)
        for x in range(n):
            for y in range(n):
                if roots[x] == roots[y]:
                    t[x][y] += prob
                    derivative[x][y] += prob*score
    return t, derivative


def russo(n, edges, p):
    result = [[Q(0) for _ in range(n)] for _ in range(n)]
    for e in range(len(edges)):
        remaining = edges[:e] + edges[e+1:]
        for mask in range(1 << len(remaining)):
            k = mask.bit_count()
            prob = p**k * (1-p)**(len(remaining)-k)
            closed = connected(n, remaining, mask)
            opened = connected(n, remaining + [edges[e]], mask | (1 << len(remaining)))
            for x in range(n):
                for y in range(n):
                    if opened[x] == opened[y] and closed[x] != closed[y]:
                        result[x][y] += prob
    return result


def mul(a, b):
    n = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def adjacency(n, edges):
    a = [[0]*n for _ in range(n)]
    for u, v in edges:
        a[u][v] = a[v][u] = 1
    return a


def eigenvalues(a):
    """Small symmetric Jacobi diagonalization; numerical evidence only."""
    a = [[float(v) for v in row] for row in a]
    n = len(a)
    for _ in range(100*n*n):
        i, j = max(((i,j) for i in range(n) for j in range(i+1,n)), key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[i][j]) < 1e-13:
            return [a[k][k] for k in range(n)]
        theta = (a[j][j]-a[i][i])/(2*a[i][j])
        z = math.copysign(1.0, theta)/(abs(theta)+math.hypot(theta,1.0))
        c, s = 1/math.sqrt(1+z*z), z/math.sqrt(1+z*z)
        old = a[i][j]
        a[i][i] -= z*old
        a[j][j] += z*old
        a[i][j] = a[j][i] = 0.0
        for k in range(n):
            if k not in (i,j):
                u,v = a[k][i],a[k][j]
                a[k][i] = a[i][k] = c*u-s*v
                a[k][j] = a[j][k] = s*u+c*v
    raise RuntimeError("Jacobi did not converge")


def nonbacktracking(n, edges, length):
    a = adjacency(n, edges)
    result = [[0]*n for _ in range(n)]
    if length == 0:
        return [[int(i==j) for j in range(n)] for i in range(n)]
    for source in range(n):
        states = {(-1,source): 1}
        for _ in range(length):
            nxt = {}
            for (prev,v), count in states.items():
                for w in range(n):
                    if a[v][w] and w != prev:
                        nxt[v,w] = nxt.get((v,w),0)+count
            states = nxt
        for (_,v),count in states.items():
            result[source][v] += count
    return result


def main():
    fresh_gate = gate()
    graphs = [
        ("path4",4,[(0,1),(1,2),(2,3)]),
        ("triangle",3,[(0,1),(1,2),(2,0)]),
        ("cycle4",4,[(0,1),(1,2),(2,3),(3,0)]),
        ("diamond",4,[(0,1),(0,2),(1,2),(1,3),(2,3)]),
        ("complete4",4,[(i,j) for i in range(4) for j in range(i+1,4)]),
        ("star5",5,[(0,i) for i in range(1,5)]),
    ]
    cases, entries, min_slack = [], 0, None
    for name,n,edges in graphs:
        a = adjacency(n, edges)
        alpha = max(abs(x) for x in eigenvalues(a))
        for p in (Q(1,5),Q(1,2),Q(4,5)):
            deadline()
            t,dt = two_point(n,edges,p)
            assert dt == russo(n,edges,p), (name,p,"Russo mismatch")
            bound = mul(mul(t,a),t)
            for x in range(n):
                for y in range(n):
                    slack = bound[x][y]-dt[x][y]
                    assert slack >= 0, (name,p,x,y,slack)
                    min_slack = slack if min_slack is None else min(min_slack,slack)
                    entries += 1
            m = max(eigenvalues(t))
            q = p + min((1-p)/2, Q(1,100))
            assert alpha*m*float(q-p) < 1
            tq,_ = two_point(n,edges,q)
            actual = max(eigenvalues(tq))
            norm_bound = m/(1-alpha*m*float(q-p))
            assert actual <= norm_bound+1e-10
            cases.append({"graph":name,"p":str(p),"q":str(q),"alpha":alpha,
                          "norm_p":m,"norm_q":actual,"bootstrap_bound":norm_bound})
    nb_graphs = [
        ("complete4",4,graphs[4][2]),
        ("k33",6,[(i,j) for i in range(3) for j in range(3,6)]),
        ("cube3",8,[(i,j) for i in range(8) for j in range(i+1,8) if (i^j).bit_count()==1]),
    ]
    nb_count = 0
    for name,n,edges in nb_graphs:
        a = adjacency(n,edges)
        d = sum(a[0])
        assert all(sum(row)==d for row in a)
        b0 = [[int(i==j) for j in range(n)] for i in range(n)]
        b1 = a
        aa = mul(a,a)
        b2 = [[aa[i][j]-d*int(i==j) for j in range(n)] for i in range(n)]
        vals = [b0,b1,b2]
        for k in range(3,7):
            ab = mul(a,vals[-1])
            vals.append([[ab[i][j]-(d-1)*vals[-2][i][j] for j in range(n)] for i in range(n)])
        for length,poly in enumerate(vals):
            deadline()
            assert poly == nonbacktracking(n,edges,length), (name,length)
            nb_count += 1
    trees = []
    for d in range(3,11):
        b = d-1
        pc,alpha,beta = 1/b,2*math.sqrt(b),math.sqrt(b)
        critical_norm = (1-pc*pc)/(1-beta*pc)**2
        eta = min((1-pc)/2,1/(2*alpha*critical_norm))
        trees.append({"d":d,"pc":pc,"alpha":alpha,"beta":beta,
                      "coarse_certifies":b>4,"nonbacktracking_certifies":b>1,
                      "critical_norm":critical_norm,"conditional_margin":eta})
    result = {"utc":datetime.now(timezone.utc).isoformat(),"pid":os.getpid(),
              "command":"python -X utf8 ~/brain_workers/w552/validate.py",
              "gate":fresh_gate,"exact_russo_cases":len(cases),"exact_bk_entry_checks":entries,
              "min_exact_entry_slack":str(min_slack),"numerical_norm_bootstrap_cases":len(cases),
              "nonbacktracking_exact_matrix_checks":nb_count,"finite_cases":cases,"tree_constants":trees,
              "before_coarse_tree_cases":sum(x["coarse_certifies"] for x in trees),
              "after_nonbacktracking_tree_cases":sum(x["nonbacktracking_certifies"] for x in trees),
              "elapsed_seconds":time.monotonic()-START,"status":"PASS",
              "proof_scope":"finite exact checks and numerical constants only; no infinite uniform-bound certificate"}
    (HERE / "VALIDATION.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps({k:result[k] for k in ("status","exact_russo_cases","exact_bk_entry_checks",
          "numerical_norm_bootstrap_cases","nonbacktracking_exact_matrix_checks",
          "before_coarse_tree_cases","after_nonbacktracking_tree_cases","elapsed_seconds")}))


if __name__ == "__main__":
    main()
