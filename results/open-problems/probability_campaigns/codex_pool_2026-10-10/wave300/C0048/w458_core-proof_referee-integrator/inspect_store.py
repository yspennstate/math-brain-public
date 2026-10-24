"""Read-only, bounded probe for existing C0048 card and related namespaces."""
import sqlite3

db = "~/math-brain-build/local/population/brain.sqlite3"
con = sqlite3.connect("file:" + db + "?mode=ro", uri=True)
tables = [x[0] for x in con.execute("select name from sqlite_master where type='table' and name not like 'sqlite_%' order by name")]
print("tables", tables[:40])
for table in ("claims", "nodes"):
    cols = [x[1] for x in con.execute(f"pragma table_info('{table}')")]
    print("candidate_table", table, cols[:25])
    if "title" in cols:
        rows = con.execute(f"select {', '.join(c for c in ('id','logical_id','title','kind','retired','metadata_json') if c in cols)} from '{table}' where title like ? limit 8", ("%Discontinuity of the Potts phase transition%",)).fetchall()
        for row in rows:
            print("target", row)
        if table == "nodes":
            for needle in ("%Edwards-Sokal%", "%wired FK%", "%critical magnetization%"):
                hits = con.execute("select id,title from nodes where (title like ? or body like ?) and (title like '%Potts%' or body like '%Potts%') limit 6", (needle, needle)).fetchall()
                print("related", needle, hits)
            row = con.execute("select title,body,metadata_json from nodes where id=?", ("claim_9e675eaf413af335c1939c533f557a40",)).fetchone()
            print("fk_existing", row[0], row[1][:2000], row[2][:600])
con.close()
