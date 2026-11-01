from pathlib import Path
import json
import sqlite3
import time

root = Path(__file__).resolve().parent
paths = [Path("~/math-brain-build/local/population/brain.sqlite3")]
base = Path("~/math-research-brain/local")
frontier = [base] if base.is_dir() else []
for depth in range(3):
    next_level = []
    for folder in frontier[:32]:
        for child in folder.iterdir():
            lowered = child.name.lower()
            if any(word in lowered for word in ("test", "blind", "challenge", "benchmark", "eval", "token", "auth", "key")):
                continue
            if child.is_dir():
                next_level.append(child)
            elif child.suffix.lower() in (".sqlite3", ".sqlite", ".db"):
                paths.append(child)
    frontier = next_level
results = []
for path in list(dict.fromkeys(paths))[:4]:
    if not path.is_file():
        continue
    started = time.monotonic()
    record = {"store":str(path),"mode":"ro","matches":[]}
    try:
        con = sqlite3.connect(path.as_uri()+"?mode=ro",uri=True,timeout=5)
        con.execute("PRAGMA query_only=ON")
        con.set_progress_handler(lambda: int(time.monotonic()-started>45),1000)
        tables = [row[0] for row in con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('nodes','cards')")]
        for table in tables:
            columns = [row[1] for row in con.execute('PRAGMA table_info("'+table+'")')]
            if "title" not in columns:
                continue
            body = "body" if "body" in columns else "statement" if "statement" in columns else None
            selection = [col for col in ("id","kind","title") if col in columns]
            fields = ','.join('"'+col+'"' for col in selection)
            if body:
                fields += ',substr("'+body+'",1,2400)'
            predicate = "(lower(title) LIKE '%ising%' AND (lower(title) LIKE '%trivial%' OR lower(title) LIKE '%gaussian%' OR lower(title) LIKE '%scaling%'))"
            if body:
                predicate += ' OR "'+body+'" LIKE ?'
                parameters = ("%C0052%",)
            else:
                parameters = ()
            for row in con.execute('SELECT '+fields+' FROM "'+table+'" WHERE '+predicate+' LIMIT 6',parameters):
                names = selection+(["body_excerpt"] if body else [])
                record["matches"].append(dict(zip(names,row)))
        con.close()
        record["status"] = "bounded targeted lookup completed"
    except (sqlite3.Error,OSError) as exc:
        record["status"] = str(exc)
    record["seconds"] = time.monotonic()-started
    results.append(record)
report = {"query":"C0052 or Ising titles involving triviality/Gaussianity/scaling","stores":results,
          "current_openness":"UNKNOWN","scope":"Bounded lookup only; no exhaustive novelty or retired-work certificate."}
(root/"SOURCE_LOOKUP_REPORT.json").write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding="utf-8")
print(json.dumps({"stores":[{"store":r["store"],"status":r["status"],"matches":[{"id":m.get("id"),"title":m.get("title"),"body_excerpt":m.get("body_excerpt","")[:900]} for m in r["matches"]]} for r in results]},ensure_ascii=False,indent=2))
