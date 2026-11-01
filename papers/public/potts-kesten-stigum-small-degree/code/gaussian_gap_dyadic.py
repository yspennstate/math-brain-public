"""One-core, checkpointed Gaussian gap certificate using integer intervals only."""
from __future__ import annotations
import argparse
import ctypes
import datetime
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time
from dyadic_interval import I,BITS,SCALE,pi_interval,normal_primitive_bounds

START=time.monotonic()
ROOT=Path(__file__).resolve().parent
OUT=ROOT/"gaussian_gap_dyadic_v1"
SOURCE={name:hashlib.sha256(ROOT.joinpath(name).read_bytes()).hexdigest()
        for name in ("dyadic_interval.py","gaussian_gap_dyadic.py")}
WIDTH=F(1,8)
QUADRATIC=F(2,5)
LINEAR=F(3,50)
GRID=[1/(F(10)-F(i,10)) for i in range(86)]


def text(q):
    return f"{q.numerator}/{q.denominator}"


def save(path,item):
    part=path.with_suffix(path.suffix+".part")
    part.write_text(json.dumps(item,indent=2)+"\n",encoding="utf-8",newline="")
    part.replace(path)


def free_memory():
    class M(ctypes.Structure):
        _fields_=[("length",ctypes.c_ulong),("load",ctypes.c_ulong)]+[
            (name,ctypes.c_ulonglong) for name in
            ("totalphys","availphys","totalpage","availpage","totalvirt","availvirt","availext")]
    m=M();m.length=ctypes.sizeof(m)
    assert ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return m.availphys


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--seconds",type=int,default=240)
    parser.add_argument("--count",type=int,default=85)
    args=parser.parse_args()
    assert 1<=args.seconds<=480 and 1<=args.count<=85
    OUT.mkdir(exist_ok=True)
    available=free_memory()
    if available < 2*(1<<30):
        save(OUT/"wait_memory.json",{"status":"WAIT","available_bytes":available})
        print("WAIT: memory threshold; no computation started",flush=True)
        return
    assert GRID[0]==F(1,10) and GRID[-1]==F(2,3)
    assert all(1/GRID[i]-1/GRID[i+1]==F(1,10) for i in range(85))
    config={"source_sha256":SOURCE,"precision_bits":BITS,"radius":"6/1",
            "bin_width":text(WIDTH),"quadratic_constant":text(QUADRATIC),
            "linear_constant":text(LINEAR),"interval_count":85,"cpu_workers":1,
            "working_memory_estimate_bytes":20_000_000,
            "arithmetic":"Python integers and Fractions; every dyadic operation rounds outward",
            "normal_primitive_even_degree":144,"machin_arctan_even_degree":80}
    if OUT.joinpath("config.json").exists():
        assert json.loads(OUT.joinpath("config.json").read_text(encoding="utf-8"))==config
    else:save(OUT/"config.json",config)
    pi=pi_interval();norm=1/(2*pi).sqrt()
    bins=[]
    for j in range(48):
        path=OUT/f"bin_{j:02d}.json"
        if path.exists():
            r=json.loads(path.read_text(encoding="utf-8"))
            assert r["source_sha256"]==SOURCE
            bins.append(tuple(I.restore(r[k]) for k in ("weight","mean","variance")))
            continue
        if time.monotonic()-START>=args.seconds:
            print(json.dumps({"status":"PARTIAL","phase":"bins","completed":len(bins)}),flush=True)
            return
        a,b=j*WIDTH,(j+1)*WIDTH
        fa,fb=normal_primitive_bounds(a),normal_primitive_bounds(b)
        integral=I.fraction_bounds(fb[0]-fa[1],fb[1]-fa[0])
        w=integral*norm
        phia=(-I.rational(a*a/2)).exp()*norm
        phib=(-I.rational(b*b/2)).exp()*norm
        first=phia-phib
        second=w+a*phia-b*phib
        mean=first/w
        variance=second-first*first/w
        assert w.lo>0 and mean.lower()>a and mean.upper()<b and variance.lo>0
        bins.append((w,mean,variance))
        save(path,{"source_sha256":SOURCE,"a":text(a),"b":text(b),
                   "weight":w.export(),"mean":mean.export(),"variance":variance.export()})
    P=2*sum((w for w,_,_ in bins),I.rational(0))
    D=2*sum((v for _,_,v in bins),I.rational(0))
    tail=1-P*P
    assert 0<P.lo<=P.hi<SCALE and D.lo>0 and tail.lo>0
    save(OUT/"bins_summary.json",{"source_sha256":SOURCE,"pi":pi.export(),
         "normalizing_density":norm.export(),"P":P.export(),"D":D.export(),"tail":tail.export()})
    new_count=0
    for index,(a,b) in enumerate(zip(GRID,GRID[1:])):
        path=OUT/f"endpoint_{index:03d}.json"
        if path.exists():
            row=json.loads(path.read_text(encoding="utf-8"))
            assert row["source_sha256"]==SOURCE and row["a"]==text(a) and row["b"]==text(b)
            assert row["passed"] is True
            continue
        if new_count>=args.count or time.monotonic()-START>=args.seconds:break
        s=I.rational(b)
        slope1=3*(3*s).sqrt()/2
        slope2=3*s.sqrt()/2
        coshes=[(slope2*m).cosh() for _,m,_ in bins]
        Q=I.rational(0)
        for wi,mi,_ in bins:
            ap=2*(-9*s/2-slope1*mi).exp()
            am=2*(-9*s/2+slope1*mi).exp()
            inner=I.rational(0)
            for (wj,_,_),bj in zip(bins,coshes):
                inner+=2*wj*(1/(1+ap*bj)+1/(1+am*bj))
            Q+=wi*inner
        error=9*s*P*D/4
        upper=Q+error+tail-F(1,3)
        lower=Q-error-F(1,3)
        mq=a-upper.upper()-QUADRATIC*b*b
        ml=a-upper.upper()-LINEAR*b
        record={"source_sha256":SOURCE,"a":text(a),"b":text(b),"Q":Q.export(),
                "quadrature_error":error.export(),"g_upper":upper.export(),"g_lower":lower.export(),
                "exact_quadratic_margin":text(mq),"exact_linear_margin":text(ml),
                "passed":mq>0 and ml>0}
        save(path,record)
        assert record["passed"], record
        new_count+=1
        print(json.dumps({"endpoint":index,"b":text(b),"passed":True}),flush=True)
    rows=[]
    for j in range(85):
        path=OUT/f"endpoint_{j:03d}.json"
        if path.exists():
            row=json.loads(path.read_text(encoding="utf-8"))
            assert row["source_sha256"]==SOURCE
            rows.append({"index":j,"file":path.name,"sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
                         "quadratic_margin":row["exact_quadratic_margin"],
                         "linear_margin":row["exact_linear_margin"],"passed":row["passed"]})
    passed=len(rows)==85 and all(row["passed"] for row in rows)
    report={**config,"status":"PASS" if passed else "PARTIAL","completed":len(rows),
            "new_this_run":new_count,"endpoints":rows,"elapsed_seconds":time.monotonic()-START,
            "checked_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "claims_if_complete":["s-g3(s)>=(2/5)s^2 on [1/10,2/3]",
                                  "s-g3(s)>=(3/50)s on [1/10,2/3]"],
            "scope":"Certificate conditional on the separately written analytic error and normalization proof"}
    save(OUT/"report.json",report)
    print(json.dumps({"status":report["status"],"completed":len(rows),"new_this_run":new_count}),flush=True)


if __name__=="__main__":main()
