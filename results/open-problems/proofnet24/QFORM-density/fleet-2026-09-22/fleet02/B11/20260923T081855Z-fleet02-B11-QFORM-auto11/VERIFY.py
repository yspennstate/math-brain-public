#!/usr/bin/env python3
"""Finite regression checks for QFORM zero-disjoint-defect support classification.
Not a proof; REPORT.md contains the proof.
"""
import itertools, math

def tetrad_support_ok(n, edges):
    E={tuple(sorted(e)) for e in edges}
    for i,j,k,l in itertools.combinations(range(n),4):
        vals=(
            int((i,j) in E)*int((k,l) in E),
            int((i,k) in E)*int((j,l) in E),
            int((i,l) in E)*int((j,k) in E),
        )
        if not (vals[0]==vals[1]==vals[2]):
            return False
    return True

def star_or_clique(n, edges):
    E={tuple(sorted(e)) for e in edges}
    adj=[set() for _ in range(n)]
    for i,j in E:
        adj[i].add(j); adj[j].add(i)
    seen=set(); comps=[]
    for v in range(n):
        if adj[v] and v not in seen:
            stack=[v]; seen.add(v); comp=[]
            while stack:
                x=stack.pop(); comp.append(x)
                for y in adj[x]:
                    if y not in seen:
                        seen.add(y); stack.append(y)
            comps.append(comp)
    if len(comps)>1:
        return False
    if not comps:
        return True
    C=comps[0]
    if all(tuple(sorted((i,j))) in E for i,j in itertools.combinations(C,2)):
        return True
    for h in C:
        leaves=[v for v in C if v!=h]
        if (all(tuple(sorted((h,v))) in E for v in leaves)
            and all(tuple(sorted((i,j))) not in E
                    for i,j in itertools.combinations(leaves,2))):
            return True
    return False

for n in range(2,7):
    all_edges=list(itertools.combinations(range(n),2))
    count=0
    for mask in range(1<<len(all_edges)):
        E={all_edges[k] for k in range(len(all_edges)) if (mask>>k)&1}
        if tetrad_support_ok(n,E):
            count+=1
            assert star_or_clique(n,E)
    print(f"n={n}: tetrad-support graphs={count}, all star/clique classification PASS")

print(f"24*sqrt(pi)={24*math.sqrt(math.pi):.12f}")
print(f"2*pi*sqrt(2)={2*math.pi*math.sqrt(2):.12f}")
print("QFORM_TETRAD_ENDPOINT_CHECK_PASS")
