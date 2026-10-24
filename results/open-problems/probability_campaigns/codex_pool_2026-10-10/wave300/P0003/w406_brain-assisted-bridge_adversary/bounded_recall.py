"""One authorized 60-second recall, with durable evidence in the worker folder."""
import json
import pathlib
import subprocess
import time

ROOT = pathlib.Path(__file__).resolve().parent
query = "P0003 honeycomb self avoiding walk parafermionic scaling limit mistakes"
command = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", query, "-n", "3"]
start = time.perf_counter()
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=60)
    evidence = {"command":command,"elapsed_seconds":time.perf_counter()-start,"timeout_seconds":60,"status":"completed","returncode":result.returncode,"stdout":result.stdout,"stderr":result.stderr}
except subprocess.TimeoutExpired as exc:
    def decode(value):
        return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else (value or "")
    evidence = {"command":command,"elapsed_seconds":time.perf_counter()-start,"timeout_seconds":60,"status":"timeout","stdout":decode(exc.stdout),"stderr":decode(exc.stderr)}
(ROOT/"recall_evidence.json").write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(evidence,ensure_ascii=False))
