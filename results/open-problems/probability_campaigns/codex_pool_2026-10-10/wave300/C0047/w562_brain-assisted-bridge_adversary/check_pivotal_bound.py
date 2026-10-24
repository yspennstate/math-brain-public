"""Independent exact finite controls for w561's Russo/BK step."""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
import time

root=Path(__file__).resolve().parent
start=time.perf_counter()
gate={"created_at":"2026-10-10","task":"w561 L02 independent Russo/BK control","maximum_states_per_graph":32,"maximum_seconds":5,"network":False,"gpu":False,"processes":1}
(root/"pivotal_compute_gate.json").write_text(json.dumps(gate,indent=2),encoding="utf-8")
graphs=[("triangle",3,[(0,1),(1,2),(2,0)]),("cycle4",4,[(0,1),(1,2),(2,3),(3,0)]),("diamond",4,[(0,1),(0,2),(1,2),(1,3),(2,3)])]
checked=0
records=[]
for name,n,edges in graphs:
    assert 2**len(edges)<=gate["maximum_states_per_graph"]
    for p in (F(1,4),F(1,2),F(3,4)):
        T=[[F(0) for _ in range(n)]for _ in range(n)]
        D=[[F(0) for _ in range(n)]for _ in range(n)]
        for bits in product((0,1),repeat=len(edges)):
            parent=list(range(n))
            def find(x):
                while parent[x]!=x:x=parent[x]
                return x
            for bit,(u,v) in zip(bits,edges):
                if bit:parent[find(u)]=find(v)
            k=sum(bits)
            w=p**k*(1-p)**(len(edges)-k)
            dw=w*(F(k)/p-F(len(edges)-k)/(1-p))
            for x in range(n):
                for y in range(n):
                    if find(x)==find(y):T[x][y]+=w;D[x][y]+=dw
        for x in range(n):
            for y in range(n):
                bound=sum(T[x][u]*T[v][y]+T[x][v]*T[u][y]for u,v in edges)
                assert 0<=D[x][y]<=bound
                checked+=1
        records.append({"graph":name,"p":str(p),"states":2**len(edges),"ordered_pairs":n*n})
result={"command":"python -X utf8 ~/brain_workers/w562/check_pivotal_bound.py","elapsed_seconds":time.perf_counter()-start,"cases":records,"ordered_pair_inequalities_checked":checked,"all_checks_passed":True,"exact_arithmetic":True,"scope":"Finite controls for the derivative inequality; not proof of infinite-volume continuation or critical operator boundedness."}
assert result["elapsed_seconds"]<gate["maximum_seconds"]
(root/"pivotal_measurement.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
print(json.dumps(result,indent=2))
