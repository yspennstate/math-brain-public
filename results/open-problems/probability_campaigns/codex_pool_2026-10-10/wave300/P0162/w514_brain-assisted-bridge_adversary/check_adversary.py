"""Fresh bounded independent truth-table checks for peer composition and delta."""
import json
import math
import time
from pathlib import Path
from check_bent_selector import walsh, entropy, core_value

ROOT=Path(__file__).resolve().parent
GATE={"id":"w514-G3-peer-and-hypothesis-audit","reason":"new paired gadget proof and source/card delta mismatch",
      "core_dimensions":[2,4],"gadget_size":3,"max_physical_dimension":15,
      "max_truth_table_entries":32768,"max_wall_seconds":55,"no_gpu":True,
      "no_training":True,"no_function_search":True}

def influences(values,dimension):
    return [sum(values[x]!=values[x^(1<<i)] for x in range(len(values)))/len(values) for i in range(dimension)]

def restriction(values,i,positive):
    return [v for x,v in enumerate(values) if bool(x&(1<<i)) != positive]

def h2(q):
    if q in (0,1):
        return 0.0
    return -q*math.log2(q)-(1-q)*math.log2(1-q)

def and3():
    values=[1]+[-1]*7
    af=walsh(values)
    gaps=[]
    inf=influences(values,3)
    for i in range(3):
        gap=entropy(af)-(entropy(walsh(restriction(values,i,True)))+entropy(walsh(restriction(values,i,False))))/2
        gaps.append(gap/inf[i])
    rho=min(gaps)
    delta=max(inf)
    wrong=(1+h2(.5))/.5
    right=(1+h2(delta))/delta
    assert rho>wrong
    assert rho<=right
    return {"function":"AND3, +1 only at all-positive input","rho0":rho,"coordinate_input_bias":.5,
            "maximal_flip_influence":delta,"wrong_input_bias_ceiling":wrong,"correct_influence_ceiling":right,
            "verdict":"delta must denote maximal influence, not uniform input bias"}

def composed(m):
    dimension=3*(m+1)
    assert dimension<=GATE["max_physical_dimension"]
    assert 1<<dimension<=GATE["max_truth_table_entries"]
    values=[]
    for bits in range(1<<dimension):
        outer=0
        for j in range(m+1):
            block=(bits>>(3*j))&7
            if block.bit_count()>=2:
                outer|=1<<j
        x=outer&((1<<m)-1)
        v=core_value(x,m)
        if x==0 and outer&(1<<m):
            v=-v
        values.append(v)
    af=walsh(values)
    inf=influences(values,dimension)
    selected=3*m
    ap=walsh(restriction(values,selected,True))
    am=walsh(restriction(values,selected,False))
    gap=entropy(af)-(entropy(ap)+entropy(am))/2
    selector_mask=3<<(3*m)
    sector=0.0
    total_B=0.0
    for index,(a,b) in enumerate(zip(ap,am)):
        mass=(a*a+b*b)/2
        if not mass:
            continue
        q=(a-b)**2/(4*mass)
        term=mass*h2(q)
        total_B+=term
        if not index&selector_mask:
            sector+=term
    p=2.0**(-m)
    alpha=.5
    assert inf[selected]==alpha*p
    assert max(inf)<=.5
    assert all(i==alpha*(.5+p) for i in inf[:3*m])
    assert all(i==alpha*p for i in inf[3*m:])
    assert sector>=alpha*alpha*m*p-1e-12
    assert gap/inf[selected]>=alpha*m-1e-11
    assert gap>=total_B-1e-12
    outer_g=[core_value(x,m) for x in range(1<<m)]
    outer_h=list(outer_g)
    outer_h[0]*=-1
    outer_H=entropy(walsh(outer_g+outer_h))
    outer_I=m/2+(m+1)*p
    composed_H=entropy(af)
    composed_I=sum(inf)
    assert abs(composed_H-(outer_H+2*outer_I))<1e-12
    assert abs(composed_I-1.5*outer_I)<1e-12
    assert composed_H<=4*composed_I
    return {"core_m":m,"physical_dimension":dimension,"truth_table_entries":len(values),
            "all_influences_max":max(inf),"selected_influence":inf[selected],
            "selected_increment_ratio":gap/inf[selected],"proved_ratio_lower_bound":alpha*m,
            "empty_selector_sector_B":sector,"sector_lower_bound":alpha*alpha*m*p,
            "H_over_I":composed_H/composed_I,"composition_entropy_error":abs(composed_H-(outer_H+2*outer_I))}

def main():
    started=time.perf_counter()
    delta=and3()
    rows=[]
    for m in GATE["core_dimensions"]:
        row=composed(m)
        rows.append(row)
        (ROOT/"adversary_checks.json").write_text(json.dumps({"gate":GATE,"delta_counterexample":delta,"peer_composition_rows":rows},indent=2)+"\n",encoding="utf-8")
    elapsed=time.perf_counter()-started
    assert elapsed<GATE["max_wall_seconds"]
    receipt={"gate":GATE,"delta_counterexample":delta,"peer_composition_rows":rows,"seconds":elapsed,
             "scope":"bounded truth-table diagnostics; independent mathematical audit in AUDIT_W513.md"}
    (ROOT/"adversary_checks.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(receipt))

if __name__=="__main__":
    main()
