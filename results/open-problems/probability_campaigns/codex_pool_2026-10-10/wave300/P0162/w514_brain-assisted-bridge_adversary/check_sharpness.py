"""Fresh bounded gate: high precision for the explicit witness, not proof search."""
import json
import time
from decimal import Decimal, localcontext
from pathlib import Path

ROOT=Path(__file__).resolve().parent
GATE={"id":"w514-G2-sharp-coordinate-constant","reason":"new analytic upper bound and its sharpness limit",
      "dimensions":[4,6,8,10,20,40],"decimal_precision":65,"max_wall_seconds":55,
      "max_rows":6,"no_gpu":True,"no_training":True,"no_function_search":True}

def main():
    start=time.perf_counter()
    rows=[]
    with localcontext() as ctx:
        ctx.prec=GATE["decimal_precision"]
        ln2=Decimal(2).ln()
        limit=Decimal(3)/ln2
        def phi(z):
            return z*z*(z*z).ln()/ln2
        for n in GATE["dimensions"]:
            r=Decimal(2)**(-n//2)
            p=r*r
            def L(u):
                return (1+r)/2*phi(1-u*r)+(1-r)/2*phi(1+u*r)
            remainder=(L(2)/2-L(1))/p
            h2=-p*p.ln()/ln2-(1-p)*(1-p).ln()/ln2
            cap=h2/p+2/ln2
            ratio=Decimal(n)+remainder
            assert ratio<=cap
            assert ratio>=n
            assert remainder<limit
            rows.append({"core_n":n,"p":str(p),"delta_over_p":str(ratio),
                         "additive_cost":str(remainder),"optimal_additive_limit":str(limit),
                         "exact_entropy_upper_cap":str(cap),"distance_to_limit":str(limit-remainder)})
    elapsed=time.perf_counter()-start
    assert elapsed<GATE["max_wall_seconds"]
    receipt={"gate":GATE,"rows":rows,"seconds":elapsed,"scope":"finite diagnostics; limit proof in SHARP_COORDINATE_BOUND.md"}
    (ROOT/"sharpness_measurements.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"n4_additive":rows[0]["additive_cost"],"n40_additive":rows[-1]["additive_cost"],
                      "limit":rows[-1]["optimal_additive_limit"],"seconds":elapsed}))

if __name__=="__main__":
    main()
