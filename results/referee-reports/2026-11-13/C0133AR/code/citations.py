"""Independently discover survey records, then fetch forward citations."""
import requests,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=requests.Session()
r=s.get("https://api.openalex.org/works",params={"search":"Excited random walks results methods open problems","per-page":5},timeout=40);r.raise_for_status()
d=r.json();(ROOT/"sources/openalex_discovery.json").write_text(json.dumps(d,indent=2))
ids=[w["id"].split("/")[-1] for w in d["results"] if "results, methods, open problems" in w["display_name"].lower()]
merged={}
for wid in ids:
 cursor="*";pages=[]
 while cursor:
  p=s.get("https://api.openalex.org/works",params={"filter":f"cites:{wid},from_publication_date:2012-01-01,to_publication_date:2026-11-13","per-page":200,"cursor":cursor},timeout=40);p.raise_for_status()
  a=p.json();pages.append(a)
  for w in a["results"]:merged[w["id"]]=w
  cursor=a["meta"].get("next_cursor") if a["results"] else None
 (ROOT/"sources"/("citations_"+wid+".json")).write_text(json.dumps(pages,indent=2))
 print(wid,pages[0]["meta"]["count"],flush=True)
rows=[]
for w in sorted(merged.values(),key=lambda w:(w["publication_year"],w["display_name"])):
 loc=w.get("best_oa_location") or w.get("primary_location") or {}
 row=[str(w["publication_year"]),w["display_name"],w.get("doi") or "",loc.get("pdf_url") or loc.get("landing_page_url") or "",w["id"]]
 rows.append("\t".join(row));print("\t".join(row),flush=True)
(ROOT/"sources/citations.tsv").write_text("\n".join(rows)+"\n")
