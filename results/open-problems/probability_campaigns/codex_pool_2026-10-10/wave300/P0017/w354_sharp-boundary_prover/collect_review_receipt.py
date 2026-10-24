import json
import sqlite3
from pathlib import Path

base = Path(__file__).resolve().parent
review_path = Path("~/brain_workers/w356/PEER_REVIEWS.jsonl")
records = []
with review_path.open(encoding="utf-8-sig") as stream:
    for line in stream:
        if "w354-P0017-" in line:
            records.append(json.loads(line))
(base / "REFEREE_VERDICTS.json").write_text(json.dumps({"reviewer": "w356", "path": str(review_path), "records": records}, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(records, ensure_ascii=False))
meshpath = Path("~/.agents/coordination/agent_mesh.sqlite3")
connection = sqlite3.connect("file:" + meshpath.as_posix() + "?mode=ro", uri=True, timeout=3)
messages = connection.execute("SELECT sender_agent,topic,body,created_at FROM messages WHERE recipient='w354' AND sender_agent IN ('w355','w356') ORDER BY rowid DESC LIMIT 6").fetchall()
connection.close()
(base / "PEER_MESSAGES.json").write_text(json.dumps(messages, indent=2, ensure_ascii=False), encoding="utf-8")
print("PEER_MESSAGES", json.dumps(messages, ensure_ascii=False))
