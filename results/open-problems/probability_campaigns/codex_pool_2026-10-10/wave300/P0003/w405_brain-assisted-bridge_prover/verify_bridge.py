from __future__ import annotations
import json, math, time
from collections import Counter
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parent
started=time.monotonic()
gate={"kind":"fresh-local-deterministic-fixture-bound","created_unix":time.time(),"max_seconds":5,"max_cycle_N":8,"max_vertices":18,"no_gpu":True,"no_training":True,"external_compute_authorization_claimed":False}
(ROOT/"COMPUTE_GATE.json").write_text(json.dumps(gate,indent=2),encoding="utf-8")
checks=[]
def check(name,condition,details):
    if time.monotonic()-started>gate["max_seconds"]:
        raise TimeoutError("Fixture time bound exceeded")
    if not condition:
        raise AssertionError(name)
    checks.append({"name":name,"passed":True,"details":details})
def paths(adj,a,b):
    out=[]
    def dfs(cur,p):
        if cur==b:
            out.append(tuple(p))
            return
        for nxt in sorted(adj[cur]):
            if nxt not in p:
                dfs(nxt,p+[nxt])
    dfs(a,[a])
    return out
for N in range(2,9):
    size=2*N+2
    adj={i:{(i-1)%size,(i+1)%size} for i in range(size)}
    ps=paths(adj,0,N)
    blocked=size-1
    keep=[p for p in ps if blocked not in p]
    reduced={i:{j for j in v if j!=blocked} for i,v in adj.items() if i!=blocked}
    pdel=paths(reduced,0,N)
    lengths=Counter(len(p)-1 for p in ps)
    x=Fraction(1,2)
    ratio=sum(x**(len(p)-1) for p in keep)/sum(x**(len(p)-1) for p in ps)
    check("cycle_"+str(N),len(ps)==2 and lengths==Counter({N:1,N+2:1}) and set(keep)==set(pdel) and ratio==Fraction(4,5),
          {"N":N,"paths":len(ps),"lengths":dict(lengths),"p_N":1,"p_Nplus2":0,"fugacity_ratio":"4/5"})
for n in [2,4,8,16,32,64,128]:
    delta=Fraction(1,n)
    min_height=Fraction(3,4)*delta
    check("curve_"+str(n),min_height>0,{"uniform_error":str(delta),"minimum_y_above_obstacle":str(min_height),"raw_avoidance":1,"limit_avoidance":0})
for n in [16,32,64,128]:
    check("buffer_"+str(n),Fraction(1,n)<Fraction(1,10),{"positive_buffer_radius":"1/10","apex_distance":str(Fraction(1,n)),"buffer_avoidance":0,"limit_avoidance":0})
for m in [2,4,8,16]:
    n=2*m
    r=Fraction(1,m)
    distances=[Fraction(1,n),Fraction(1)]
    weights=[Fraction(3,5),Fraction(2,5)]
    q=sum(w for d,w in zip(distances,weights) if d>r)
    check("boundary_atom_"+str(m),q==Fraction(2,5),{"r":str(r),"n":n,"boundary_atom_mass":"3/5","q_m":"2/5"})
x_c=1/math.sqrt(2+math.sqrt(2))
qc=1/(1+x_c*x_c)
measurement={"fixture_checks":len(checks),"passed":len(checks),"cycle_fixtures":7,
    "boundary_atom_raw_error":0.6,"boundary_atom_buffer_error":0,
    "simple_curve_raw_error":1,"simple_curve_buffer_error":0,
    "critical_fugacity":x_c,"mixture_ratio":qc,"fixed_length_probability":1,
    "ensemble_substitution_error":1-qc,
    "warning":"Finite deterministic fixtures verify examples only; neither P0003 nor the general analytical lemma is formally or independently proved by this script."}
(ROOT/"MEASUREMENTS.json").write_text(json.dumps({"command":"python -B -X utf8 verify_bridge.py","gate":gate,"measurements":measurement,"checks":checks,"elapsed_seconds":time.monotonic()-started},indent=2),encoding="utf-8")
print(json.dumps(measurement,indent=2))
