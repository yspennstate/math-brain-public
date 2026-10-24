import json
from pathlib import Path

wanted = {
    "w381": {"w381-L8", "w381-L9"},
    "w382": {"w382-P0110-exponential-004", "w382-P0110-small-displacement-007"},
}
for worker, ids in wanted.items():
    path = Path("~/brain_workers") / worker / "CLAIMS.jsonl"
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        row = json.loads(line)
        if row.get("claim_id", row.get("id")) in ids:
            print(json.dumps(row, indent=2, ensure_ascii=False))
