"""Read-only checks of the review package; writes one local audit result."""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","VECLIB_MAXIMUM_THREADS"):
    os.environ[key]="1"
import csv
import hashlib
import json
import math
from collections import Counter
from pathlib import Path
import re
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
report=(ROOT/"REPORT.md").read_text()
assert report.splitlines()[0]=="MINOR"
assert report.count("Exact Rademacher zeros.")==1
assert report.count("$")%2==0
assert report.count(r"\[")==report.count(r"\]")
assert r"\)" not in report
for target in re.findall(r"\]\(([^)]+)\)",report):
    if not target.startswith("https:"): assert (ROOT/target).exists(),target
for path in (ROOT/"sources").iterdir():
    assert path.suffix==".txt",path
    path.read_text()
assert not list(ROOT.rglob("*.pdf"))
manifest=json.loads((ROOT/"data/claim_snapshot.json").read_text())
assert all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h for p,h in manifest.items())

samples=list(csv.DictReader((ROOT/"data/samples.csv").open()))
assert len(samples)==13020
keys={(r["ensemble"],r["n"],r["matrix"],r["index"]) for r in samples}
assert len(keys)==len(samples)
sizes={128:1200,512:600,1024:250,2000:120}
groups=Counter((r["ensemble"],int(r["n"]),r["index"]) for r in samples)
assert len(groups)==24
for (ensemble,n,index),m in groups.items(): assert m==sizes[n]
for r in samples:
    n=int(r["n"])
    assert int(r["j"])==dict(lower=1,bulk=n//2+1,upper=n)[r["index"]]
    assert math.isclose(float(r["scaled_min"]),n**1.5*float(r["min_abs"]),rel_tol=1e-14)
    assert float(r["residual"])<1e-10
    assert float(r["norm_error"])<1e-12
    assert math.isfinite(float(r["scaled_min"]))
    assert float(r["min_abs"])>1e-12

x=sp.Symbol("x")
small=json.loads((ROOT/"data/small_zero_search.json").read_text())
checked_witnesses=0
for record in small["results"]:
    w=record["witness"]
    if w is None: continue
    a=sp.Matrix(w["matrix"])
    p=a.charpoly(x).as_poly()
    q=a.minor_submatrix(w["coordinate"]-1,w["coordinate"]-1).charpoly(x).as_poly()
    assert sp.gcd(p,p.diff()).degree()==0
    common=sp.gcd(p,q)
    assert common.degree()>0
    assert sp.expand(common.as_expr()-sp.sympify(w["common_factor"]))==0
    checked_witnesses+=1
assert checked_witnesses==4

# Check every mathematical inline expression has balanced braces.
for expr in re.findall(r"\$([^$]+)\$",report):
    assert expr.count("{")==expr.count("}"),expr

result=dict(status="pass",supplied_artifacts_unchanged=len(manifest),
            independent_selected_eigenvectors=len(samples),independent_groups=len(groups),
            exact_small_size_witnesses_rechecked=checked_witnesses,
            retained_source_text_files=len(list((ROOT/"sources").glob("*.txt"))),
            pdf_files=0,report_first_line="MINOR")
(ROOT/"data/referee_artifact_audit.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result))
