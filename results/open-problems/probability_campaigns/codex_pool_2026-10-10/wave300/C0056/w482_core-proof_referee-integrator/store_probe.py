"""Read-only, bounded schema/namespace probe for C0056 draft placement."""
import sqlite3

path = "~/math-brain-build/local/population/brain.sqlite3"
conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
conn.execute("PRAGMA query_only=ON")
tables = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
print("tables", tables[:30])
for name in tables:
    if name not in {"cards", "nodes", "math_nodes", "entries"}:
        continue
    cols = [r[1] for r in conn.execute(f"PRAGMA table_info({name})")]
    print("columns", name, cols)
    if name == "nodes":
        print("probability_node_ids", conn.execute("SELECT id, title FROM nodes WHERE id LIKE 'math:probability.%' LIMIT 15").fetchall())
        print("anderson_node_ids", conn.execute("SELECT id, title, substr(metadata_json,1,180) FROM nodes WHERE title LIKE '%Anderson%' LIMIT 12").fetchall())
        print("random_operator_namespace_examples", conn.execute("SELECT id, title, substr(metadata_json,1,260) FROM nodes WHERE metadata_json LIKE '%probability.random-operators%' LIMIT 5").fetchall())
        print("c0056_open_card", conn.execute("SELECT title, substr(body,1,1100), substr(metadata_json,1,500) FROM nodes WHERE title='Open problem: Extended states for the three-dimensional Anderson model at weak disorder' LIMIT 1").fetchall())
        print("namespace_metadata_count", conn.execute("SELECT count(*) FROM nodes WHERE json_extract(metadata_json,'$.namespace') IS NOT NULL").fetchone())
        print("probability_logical_examples", conn.execute("SELECT title, json_extract(metadata_json,'$.logical_id') FROM nodes WHERE json_extract(metadata_json,'$.logical_id') LIKE '%probability%' LIMIT 12").fetchall())
        ids = [r[0] for r in conn.execute("SELECT json_extract(metadata_json,'$.logical_id') FROM nodes WHERE json_extract(metadata_json,'$.logical_id') LIKE 'math:probability.%:%'")]
        print("existing_probability_namespaces", sorted({x.split(":", 2)[1] for x in ids}))
    if "namespace" in cols:
        rows = conn.execute(
            f"SELECT namespace, COUNT(*) FROM {name} WHERE namespace LIKE 'probability.%' "
            "GROUP BY namespace ORDER BY COUNT(*) DESC LIMIT 20"
        ).fetchall()
        print("probability_namespaces", name, rows)
        if "title" in cols:
            hits = conn.execute(
                f"SELECT namespace, title FROM {name} WHERE title LIKE '%Anderson%' LIMIT 12"
            ).fetchall()
            print("anderson_titles", name, hits)
conn.close()
