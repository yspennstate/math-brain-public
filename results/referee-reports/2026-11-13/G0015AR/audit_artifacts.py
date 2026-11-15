"""Read-only verification of submitted data, plus a pinned claim-file inventory."""
import csv
from collections import deque
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import statistics

ROOT=Path(__file__).resolve().parent
CLAIM=ROOT/"claim_files"
out={}
inventory={str(p.relative_to(CLAIM)):hashlib.sha256(p.read_bytes()).hexdigest()
           for p in sorted(CLAIM.rglob("*")) if p.is_file()}
out["claim_inventory_sha256"]=inventory
out["claim_sources_directory_present"]=(CLAIM/"sources").exists()
out["claim_raw_samples"]=[]
out["claim_geometry"]=[]
for prefix in ("ou", "ou_poisson"):
    summary=json.loads((CLAIM/f"data/{prefix}_conditioned_summary.json").read_text())
    with (CLAIM/f"data/{prefix}_conditioned_raw.csv").open() as f:
        rows=list(csv.DictReader(f))
    for entry in summary["summaries"]:
        group=[r for r in rows if int(r["n"])==entry["n"]]
        assert len(group)==entry["replicates"]
        for stat in ("height","width"):
            vals=[float(r[f"{stat}_scaled"]) for r in group]
            mean=math.fsum(vals)/len(vals)
            se=statistics.stdev(vals)/math.sqrt(len(vals))
            assert abs(mean-entry[stat]["mean"])<1e-13
            assert abs(se-entry[stat]["se"])<1e-13
        out["claim_raw_samples"].append({"model":prefix,"n":entry["n"],"count":len(group),"summaries_recomputed":True})
    with (CLAIM/f"data/{prefix}_example_vertices.csv").open() as f:
        vertices=list(csv.DictReader(f))
    n=len(vertices)
    children=[[] for _ in range(n)]
    for i,row in enumerate(vertices):
        assert int(row["vertex"])==i
        parent=int(row["parent"])
        if i==0:
            assert parent==-1
        else:
            assert 0<=parent<i
            children[parent].append(i)
    depths=[-1]*n
    depths[0]=0
    queue=deque([0])
    while queue:
        i=queue.popleft()
        assert len(children[i])==int(vertices[i]["offspring"])
        assert depths[i]==int(vertices[i]["depth"])
        for child in children[i]:
            depths[child]=depths[i]+1
            queue.append(child)
    profile=[0]*(max(depths)+1)
    for d in depths:
        profile[d]+=1
    with (CLAIM/f"data/{prefix}_example_profile.csv").open() as f:
        saved=list(csv.DictReader(f))
    assert profile==[int(r["vertices"]) for r in saved]
    out["claim_geometry"].append({"model":prefix,"n":n,"height":max(depths),"width":max(profile),"BFS_verified":True})

# Recompute the two-type algebraic warning in exact rational arithmetic.
M=((F(1,2),F(1)),(F(1,4),F(1,2)))
a=(F(1,3),F(2,3));b=(F(3,2),F(3,4));spine=tuple(x*y for x,y in zip(a,b))
assert all(sum(a[i]*M[i][j] for i in range(2))==a[j] for j in range(2))
assert all(sum(M[i][j]*b[j] for j in range(2))==b[i] for i in range(2))
means=tuple(sum(row) for row in M)
rawmean=sum(spine[i]*means[i] for i in range(2))
rawvar=sum(spine[i]*(means[i]+means[i]**2) for i in range(2))-rawmean**2
sigma2=sum(a[i]*b[i]**2 for i in range(2))
out["rational_variance_check"]={"spine_mean":str(rawmean),"spine_raw_variance":str(rawvar),"correct_sigma2":str(sigma2)}

# Freshly obtained PDFs/texts are matched to the submission's metadata, without
# treating its absent source archive as evidence that the actual texts were read.
old=json.loads((CLAIM/"data/source_manifest.json").read_text())
fresh=json.loads((ROOT/"source_manifest.json").read_text())
matched=[]
for record in fresh:
    matches=[r for r in old if r.get("pdf_sha256")==record.get("binary_sha256")]
    assert matches,record
    assert all(r["text_sha256"]==record["text_sha256"] for r in matches)
    matched.append(record["name"])
out["independently_retrieved_source_hashes_matching_submission"]=matched

# Source statement extraction preserves the original TeX exactly.
text=(ROOT/"sources/kumar_duddala_original_tex.txt").read_text()
sections=[("Standing conventions", "\\section*{Standing conventions", "\\part{"),
          ("Strength type and kernel", "Outside the saturated regime", "\\section{Quasi-compactness"),
          ("Spectral assumptions and conclusions", "\\begin{theorem}[Hilbert--Schmidt", "\\begin{proof}"),
          ("Kesten--Stigum assumptions and conclusions", "\\begin{theorem}[Continuous-type Kesten", "\\begin{proof}"),
          ("Offspring variance definition", "\\begin{corollary}[", "\\begin{proof}"),
          ("Exact conjecture and programme", "\\begin{conjecture}[Continuous-type CRT", "\\section{Summary")]
pieces=[]
for title,start,stop in sections:
    if start not in text:
        # The full source remains available if a heading differs.
        pieces.append(title+": see full original TeX (heading extraction not found).")
        continue
    first=text.index(start)
    last=text.index(stop,first)
    pieces.append(title+"\n"+text[first:last])
(ROOT/"sources/exact_definitions_and_conjecture.txt").write_text("\n\n".join(pieces))
out["forbidden_saved_files"]=[str(p.relative_to(ROOT)) for p in ROOT.rglob("*")
                              if p.is_file() and p.suffix.lower() in (".pdf",".png",".jpg",".jpeg",".tif",".tiff")]
assert not out["forbidden_saved_files"]
(ROOT/"independent_data/artifact_audit.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({k:v for k,v in out.items() if k!="claim_inventory_sha256"},indent=2))
