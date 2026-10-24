"""Read-only, bounded grep of exact math-brain export for C0056 bridge cards."""
import json
import subprocess
import time
from pathlib import Path

export = Path("~/math-brain-build/export/population/nodes.jsonl")
queries = {
    "target": r"Anderson.*(spectrum|delocal)|C0056",
    "bridge": r"spectral averaging|Simon.Wolff|Poisson kernel",
    "measure_theory": r"Radon.Nikodym theorem",
}
out = {"source": str(export), "read_only": True, "queries": []}
for name, pattern in queries.items():
    start = time.monotonic()
    try:
        run = subprocess.run(
            ["rg", "-i", "-m", "3", "--no-heading", "-e", pattern, str(export)],
            capture_output=True, text=True, encoding="utf-8", timeout=30, check=False,
        )
        cards = []
        for line in run.stdout.splitlines():
            obj = json.loads(line)
            cards.append({
                "id": obj.get("id"), "kind": obj.get("kind"),
                "title": obj.get("title"), "body": obj.get("body", "")[:4500],
                "metadata_json": obj.get("metadata_json", "")[:1500],
            })
        out["queries"].append({"name": name, "pattern": pattern, "seconds": round(time.monotonic()-start, 3), "exit_code": run.returncode, "cards": cards, "error": run.stderr[:500]})
    except subprocess.TimeoutExpired:
        out["queries"].append({"name": name, "pattern": pattern, "seconds": round(time.monotonic()-start, 3), "timeout": True, "cards": []})
Path("retrieval_measure.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
for q in out["queries"]:
    print(q["name"], q["seconds"], q.get("exit_code", "TIMEOUT"), [(c["id"], c["title"]) for c in q["cards"]])
