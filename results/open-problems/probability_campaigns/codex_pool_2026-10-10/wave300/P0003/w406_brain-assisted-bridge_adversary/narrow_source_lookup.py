"""Read the exact title-matched SAW cards missed by an arbitrary broad candidate cap."""
import json
import pathlib
import sqlite3
import time
root=pathlib.Path(__file__).resolve().parent
path=pathlib.Path("~/math-brain-build/local/population/brain.sqlite3")
con=sqlite3.connect(path.as_uri()+"?mode=ro",uri=True,timeout=5)
con.row_factory=sqlite3.Row
con.execute("PRAGMA query_only=ON")
start=time.perf_counter()
where="(lower(title) LIKE '%honeycomb%' OR lower(title) LIKE '%hexagonal%' OR lower(title) LIKE '%parafermion%') AND lower(metadata_json) NOT LIKE '%test%' AND lower(metadata_json) NOT LIKE '%answer%' AND lower(metadata_json) NOT LIKE '%challenge%' AND lower(metadata_json) NOT LIKE '%benchmark%'"
count=con.execute("SELECT count(*) FROM nodes WHERE "+where).fetchone()[0]
rows=[{**dict(row),"metadata":json.loads(row["metadata_json"])} for row in con.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE "+where+" ORDER BY title,id LIMIT 8")]
for row in rows: row.pop("metadata_json",None)
result={"command":"python -X utf8 narrow_source_lookup.py","scope":"read-only exact title lookup, capped at eight ordinary mathematical cards","matched_count":count,"returned_count":len(rows),"rows":rows,"elapsed_seconds":time.perf_counter()-start}
(root/"narrow_source_lookup.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,ensure_ascii=False))
