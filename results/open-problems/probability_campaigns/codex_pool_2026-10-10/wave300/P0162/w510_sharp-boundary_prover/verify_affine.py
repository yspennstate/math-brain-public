"""Bounded, exact truth-table checks for the mathematical boundary packet.

This is corroboration, not a formal proof or a test-bank item.
"""
from __future__ import annotations
import csv
import ctypes
from datetime import datetime, timezone
from fractions import Fraction
import json
import math
from pathlib import Path
import random
import time

ROOT=Path(__file__).resolve().parent
MAX_N=9
MAX_CASES=182
MAX_WALL_SECONDS=30

def h2(t):
    if t==0 or t==1:
        return 0.0
    return -t*math.log2(t)-(1-t)*math.log1p(-t)/math.log(2)

def gate():
    # A fresh local resource sample precedes every finite experiment. Fail closed.
    import psutil
    sample={"utc":datetime.now(timezone.utc).isoformat(),"cpu_percent":psutil.cpu_percent(interval=0.25),"available_memory_bytes":psutil.virtual_memory().available,"max_dimension":MAX_N,"max_cases":MAX_CASES,"max_wall_seconds":MAX_WALL_SECONDS,"estimated_working_memory_bytes":2*1024*1024,"gpu":False,"training":False}
    class PerformanceInfo(ctypes.Structure):
        _fields_=[("cb",ctypes.c_ulong)]+[(name,ctypes.c_size_t) for name in ["CommitTotal","CommitLimit","CommitPeak","PhysicalTotal","PhysicalAvailable","SystemCache","KernelTotal","KernelPaged","KernelNonpaged","PageSize"]]+[(name,ctypes.c_ulong) for name in ["HandleCount","ProcessCount","ThreadCount"]]
    info=PerformanceInfo()
    info.cb=ctypes.sizeof(info)
    api=ctypes.WinDLL("psapi").GetPerformanceInfo
    api.argtypes=[ctypes.POINTER(PerformanceInfo),ctypes.c_ulong]
    api.restype=ctypes.c_int
    ok=bool(api(ctypes.byref(info),info.cb)) and info.CommitLimit>0
    sample["commit_telemetry_available"]=ok
    if ok:
        sample["commit_percent"]=100*info.CommitTotal/info.CommitLimit
        sample["commit_headroom_bytes"]=(info.CommitLimit-info.CommitTotal)*info.PageSize
    sample["allow"]=ok and sample["cpu_percent"]<85 and sample["available_memory_bytes"]>8*1024**3 and sample["commit_percent"]<85 and sample["commit_headroom_bytes"]>16*1024**3
    sample["policy"]="Doctrine thresholds preserved: CPU <85%, physical headroom >8 GiB, commit <85%, commit headroom >16 GiB; missing commit fails closed; <=182 cases, <=30 seconds; no GPU/models/background work"
    (ROOT/"COMPUTE_GATE.json").write_text(json.dumps(sample,indent=2)+"\n",encoding="utf-8")
    if not sample["allow"]:
        raise SystemExit("Fresh resource gate denied: "+json.dumps(sample))
    return sample

def fwht(values):
    result=values.copy()
    half=1
    while half<len(result):
        for start in range(0,len(result),2*half):
            for k in range(start,start+half):
                left,right=result[k],result[k+half]
                result[k],result[k+half]=left+right,left-right
        half*=2
    return result

def random_dual(n,r,rng):
    span={0}
    rows=[]
    for _ in range(512):
        if len(rows)==r:
            return rows,span
        row=rng.randrange(1,1<<n)
        if row not in span:
            rows.append(row)
            span.update({u^row for u in list(span)})
    raise AssertionError("bounded full-rank generator failed")

def case(n,rows,dual,offset):
    r=len(rows)
    size=1<<n
    values=[-1 if all(((row&(x^offset)).bit_count()&1)==0 for row in rows) else 1 for x in range(size)]
    numerators=fwht(values)
    p=Fraction(1,1<<r)
    support=0
    for row in rows:
        support|=row
    m=support.bit_count()
    for s,num in enumerate(numerators):
        expected=size-2*(size>>r) if s==0 else (-2*(size>>r)*(-1 if (s&offset).bit_count()&1 else 1) if s in dual else 0)
        assert num==expected,(n,r,offset,s,num,expected)
    masses=[Fraction(num*num,size*size) for num in numerators]
    assert sum(masses)==1
    influence=sum((s.bit_count()*mass for s,mass in enumerate(masses)),Fraction())
    assert influence==2*p*m
    direct_influence=Fraction(sum(values[x]!=values[x^(1<<i)] for i in range(n) for x in range(size)),size)
    assert direct_influence==influence
    for i in range(n):
        marginal=sum((mass for s,mass in enumerate(masses) if (s>>i)&1),Fraction())
        assert marginal==(2*p if (support>>i)&1 else 0)
    entropy=-sum(float(mass)*math.log2(float(mass)) for mass in masses if mass)
    q=(1-2*float(p))**2
    expected_h=(-q*math.log2(q) if q else 0)+8*float(p)*(1-float(p))*(r-1)
    assert math.isclose(entropy,expected_h,abs_tol=2e-12)
    assert entropy<=4*float(influence)+2e-12
    v=1-masses[0]
    conditional=[mass/v for mass in masses[1:] if mass]
    conditional_h=-sum(float(t)*math.log2(float(t)) for t in conditional)
    assert math.isclose(entropy,h2(float(v))+float(v)*conditional_h,abs_tol=2e-12)
    return {"n":n,"r":r,"m":m,"offset":offset,"H":entropy,"I":float(influence)}

def boundary_row(r):
    p=math.ldexp(1.0,-r)
    a=2*p
    q=(1-2*p)**2
    # log1p preserves the small empty-coefficient entropy at large r.
    empty_h=-2*q*math.log1p(-2*p)/math.log(2)
    entropy=empty_h+8*p*(1-p)*(r-1)
    influence=a*r
    conditional_h=r+math.log1p(-p)/math.log(2)
    marginal_bound=r*h2(a)
    return {"r":r,"H":entropy,"I":influence,"H_over_I":entropy/influence,"before_marginal_entropy_bound":marginal_bound,"after_exact_entropy":entropy,"bound_reduction_factor":marginal_bound/entropy,"conditional_H_over_unconditional_I":conditional_h/influence,"first_coordinate_H_over_Ii":h2(a)/a,"nonempty_mass":4*p*(1-p)}

def main():
    sample=gate()
    started=time.perf_counter()
    rng=random.Random(5100162)
    checks=[]
    for constant in [-1,1]:
        spectrum=fwht([constant]*8)
        assert spectrum==[8*constant]+[0]*7
        checks.append({"n":3,"r":0,"constant":constant,"H":0,"I":0})
    for n in range(1,MAX_N+1):
        for r in range(1,n+1):
            for fixture in range(4):
                if fixture==0:
                    rows=[1<<i for i in range(r)]
                    dual=set(range(1<<r))
                else:
                    rows,dual=random_dual(n,r,rng)
                checks.append(case(n,rows,dual,rng.randrange(1<<n)))
                assert len(checks)<=MAX_CASES
                assert time.perf_counter()-started<MAX_WALL_SECONDS
    boundary=[boundary_row(r) for r in [2,3,4,8,16,32,64,128]]
    for r in [3,4,8,9]:
        p=Fraction(1,1<<r)
        assert p!=4*p*p
    assert boundary[-1]["first_coordinate_H_over_Ii"]>=127
    assert boundary[-1]["conditional_H_over_unconditional_I"]>1e30
    assert 3.99<boundary[-1]["H_over_I"]<4
    result={"state":"PASS","exact_truth_table_cases":len(checks),"max_dimension":MAX_N,"spectrum_coefficient_mismatches":0,"influence_mismatches":0,"entropy_formula_mismatches":0,"wall_seconds":time.perf_counter()-started,"gate":sample,"seed":5100162,"verification_kind":"Exact integer spectra, exact rational influences, floating entropy corroboration; not a formal certificate","boundary_rows":boundary}
    (ROOT/"MEASUREMENTS.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    with (ROOT/"BOUNDARY.csv").open("w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(boundary[0]))
        writer.writeheader()
        writer.writerows(boundary)
    print(json.dumps({k:v for k,v in result.items() if k not in ("gate","boundary_rows")}))
    print(json.dumps(boundary[-1]))

if __name__=="__main__":
    main()
