"""Read only target schema and the cited public primary manuscript."""
import json
import pathlib
import sqlite3
import sys
import urllib.request

root=pathlib.Path(__file__).resolve().parent
if sys.argv[1] == "schema":
    database=pathlib.Path("~/math-brain-build/local/population/brain.sqlite3")
    with sqlite3.connect(database.as_uri()+"?mode=ro",uri=True,timeout=10) as con:
        rows=con.execute("SELECT name,sql FROM sqlite_master WHERE type='table'").fetchall()
    (root/"store_schema.json").write_text(json.dumps(rows,indent=2),encoding="utf-8")
    for name, sql in rows:
        if name in ("nodes","sources","edges") or "fts" in name:
            print(name,sql)
elif sys.argv[1] == "recent":
    url="https://raw.githubusercontent.com/openai/math/main/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf"
    request=urllib.request.Request(url,headers={"User-Agent":"C0047-primary-source-audit"})
    with urllib.request.urlopen(request,timeout=40) as response:
        body=response.read(12000001)
    if len(body)>12000000 or not body.startswith(b"%PDF"):
        raise ValueError("Invalid or oversized PDF")
    (root/"recent_nonuniqueness.pdf").write_bytes(body)
    import fitz
    doc=fitz.open(stream=body,filetype="pdf")
    lines=[]
    for page_id,page in enumerate(doc):
        lines.append(f"\n=== PAGE {page_id+1} ===\n"+page.get_text())
    (root/"recent_nonuniqueness.txt").write_text("\n".join(lines),encoding="utf-8")
    print(json.dumps({"url":url,"bytes":len(body),"pages":len(doc),"text_path":str(root/"recent_nonuniqueness.txt")}))
