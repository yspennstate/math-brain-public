"""Standalone rational check of the exported Gaussian quadrature certificate.

Does not import the generator or trust its PASS flags, printed decimals,
stored margins, or interval partition. Analytic error bounds are checked in
the proof; transcendental enclosures remain the responsibility of Arb.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
DATA=ROOT/"gaussian_gap_v1"


def bounds(row):
    def value(pair):
        m,e=pair
        assert isinstance(m,int) and isinstance(e,int)
        return F(m*(1<<e)) if e>=0 else F(m,1<<(-e))
    lo,hi=value(row["lower"]),value(row["upper"])
    assert lo<=hi
    return lo,hi


def text(x):return f"{x.numerator}/{x.denominator}"


def main():
    source=ROOT/"gaussian_gap_arb.py"
    digest=hashlib.sha256(source.read_bytes()).hexdigest()
    config=json.loads(DATA.joinpath("config.json").read_text(encoding="utf-8"))
    assert config["source_sha256"]==digest
    assert config["precision_bits"]==160 and config["radius"]=="6/1"
    assert config["bin_width"]=="1/8" and config["interval_count"]==85
    bins=json.loads(DATA.joinpath("bins.json").read_text(encoding="utf-8"))["positive_half_bins"]
    assert len(bins)==48
    weights=[bounds(row["weight"]) for row in bins]
    variances=[bounds(row["unnormalized_variance"]) for row in bins]
    means=[bounds(row["conditional_mean"]) for row in bins]
    for j,(w,v,m) in enumerate(zip(weights,variances,means)):
        assert w[0]>0 and v[0]>0
        assert F(j,8)<m[0]<=m[1]<F(j+1,8)
    pl,pu=2*sum(w[0] for w in weights),2*sum(w[1] for w in weights)
    du=2*sum(v[1] for v in variances)
    assert 0<pl<=pu<1 and du>0
    tail_upper=1-pl*pl
    intervals=[]
    for path in sorted(DATA.glob("endpoint_*.json")):
        row=json.loads(path.read_text(encoding="utf-8"))
        assert row["source_sha256"]==digest
        a,b=F(row["a"]),F(row["b"])
        assert a<b and 1/a-1/b==F(1,10)
        q_upper=bounds(row["Q"])[1]
        # Reconstruct an upper bound using separate exact rational components.
        # This is deliberately not the generator's stored g_upper or margins.
        upper=q_upper+F(9,4)*b*pu*du+tail_upper-F(1,3)
        mq=a-upper-F(2,5)*b*b
        ml=a-upper-F(3,50)*b
        assert mq>0 and ml>0
        intervals.append({"a":a,"b":b,"upper":upper,"mq":mq,"ml":ml,
                          "file":path.name,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    intervals.sort(key=lambda row:row["a"])
    assert len(intervals)==85 and intervals[0]["a"]==F(1,10) and intervals[-1]["b"]==F(2,3)
    assert all(left["b"]==right["a"] for left,right in zip(intervals,intervals[1:]))
    min_quadratic=min((row["a"]-row["upper"])/(row["b"]**2) for row in intervals)
    min_linear=min((row["a"]-row["upper"])/row["b"] for row in intervals)
    report={"status":"PASS","generator_sha256":digest,
            "verifier_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "coverage":"every point of [1/10,2/3] via 85 contiguous closed intervals",
            "minimum_exact_quadratic_margin":text(min(row["mq"] for row in intervals)),
            "minimum_exact_linear_margin":text(min(row["ml"] for row in intervals)),
            "certified_quadratic_constant_from_data":text(min_quadratic),
            "certified_linear_constant_from_data":text(min_linear),
            "extra_bound_9_over_20_squared":min_quadratic>F(9,20),
            "extra_bound_13_over_200_linear":min_linear>F(13,200),
            "files":[{"file":row["file"],"sha256":row["sha256"]} for row in intervals],
            "scope":"Exact exported-bound and coverage verification; not an external mathematical audit"}
    ROOT.joinpath("gaussian_gap_verification.json").write_text(
        json.dumps(report,indent=2)+"\n",encoding="utf-8",newline="")
    print(json.dumps({k:v for k,v in report.items() if k!="files"},indent=2))


if __name__=="__main__":main()
