"""Read the three requested brain leads with the authorized 60-second timeout."""
from pathlib import Path
import json
import os
import subprocess

ROOT = Path(__file__).resolve().parent
env = dict(os.environ)
# No embeddings, index refresh, publication, or recall dumps for this read-only task.
env.update(BRAIN_RECALL_QUERY_EMBED="0", BRAIN_RECALL_REFRESH="0", BRAIN_RECALL_USAGE="0",
           BRAIN_GRAPH_LAMBDA="0", BRAIN_RECALL_LOG="0", PYTHONDONTWRITEBYTECODE="1")
command = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall",
           "C0041 uniformly elliptic iid RWRE regeneration ballisticity mistakes", "-n", "3"]
try:
    run = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=60, env=env)
    result = {"status": "returned", "returncode": run.returncode,
              "stdout": run.stdout[:14000], "stderr": run.stderr[:1200]}
except subprocess.TimeoutExpired:
    result = {"status": "timed-out-after-60s",
              "fallback_slugs": ["perceptron_proof_open_gaps_fleet_2026_07_12",
                                 "proof_steps_need_derived_joint_structure_2026_09_09"],
              "fallback": "Targeted MEMORY.md grep found no matching index line. Read these two specifically named relevant scars directly."}
(ROOT / "RECALL_RECEIPT.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
