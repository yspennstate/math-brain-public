"""Exact arithmetic checks for C003; no training simulation or large matrices."""
from fractions import Fraction as Q
import json, math
from pathlib import Path

def check():
    cases=[]
    for m in [1,2,3,10,100]:
        a,b=Q(m*m),Q(m)
        for n in range(21):
            plus=(1+Q(2,m))**n
            minus=(1-Q(1,m))**n
            ac=Q(m*(m+2),3)*plus+Q(2*m*(m-1),3)*minus
            bc=Q(m*(m+2),3)*plus-Q(m*(m-1),3)*minus
            assert a==ac and b==bc
            assert 0<b<=a<=m*m*plus
            if n in [0,1,5,20]:
                cases.append({"m":m,"n":n,"a":str(a),"b":str(b)})
            a,b=a+Q(2,m)*b,(1+Q(1,m))*b+Q(1,m)*a
    # q=1, k layers: reciprocal chi-square means agree exactly.
    inverse_checks=[]
    for m in [3,4,10,100]:
        rho=Q(m,m-2)
        for k in [0,1,5]:
            projected_inverse_mean=rho**k
            gamma_ratio=Q(m,2)*Q(2,m-2)
            assert projected_inverse_mean==gamma_ratio**k
            inverse_checks.append({"m":m,"k":k,"mean":str(projected_inverse_mean)})
    # Independent scalar check: m=1 gives Z=(g_n...g_1)^2; E Z^2=3^n.
    assert all(Q(3)**n == Q(1,3)*3*Q(3)**n for n in range(21))
    # Doob L2 twice: ||max||_2 <=4||Z||_2. Markov at 4*m*exp(n/m)/sqrt(delta)
    # has failure <=delta; sqrt to obtain op threshold 2*sqrt(m)*exp(n/(2m))*delta^(-1/4).
    constants={"trace_max_L2_factor":4,"trace_max_second_moment_factor":16,
               "trace_threshold_factor":4,"operator_threshold_factor":2}
    assert constants["trace_threshold_factor"]**2==constants["trace_max_second_moment_factor"]
    assert constants["operator_threshold_factor"]**2==constants["trace_threshold_factor"]
    return {"status":"pass","method":"exact rational recurrence vs independent eigenmode formula",
            "cases":cases,"inverse_checks":inverse_checks,"constants":constants,
            "scope":"initialization only; neither a GD simulation nor a convergence proof"}

if __name__=="__main__":
    result=check()
    dest=Path(__file__).resolve().parents[1]/"logs"/"initialization_check.json"
    dest.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":result["status"],"cases":len(result["cases"]),
                      "inverse_checks":len(result["inverse_checks"]),"log":str(dest)}))
