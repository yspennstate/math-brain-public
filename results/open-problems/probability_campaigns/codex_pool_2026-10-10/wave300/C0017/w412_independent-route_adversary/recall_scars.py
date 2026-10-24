"""Bound the explicitly requested recall and use its prescribed fallback."""
import os
import pathlib
import subprocess

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
query = "C0017 square lattice critical bond percolation conformal invariance proof conditioning mistakes"
try:
    p = subprocess.run(["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", query], capture_output=True, text=True, encoding="utf-8", timeout=60)
    output = p.stdout[:16000] + p.stderr[:1000]
    print("RECALL", output, flush=True)
except subprocess.TimeoutExpired:
    output = "TIMEOUT after 60 seconds; prescribed memory-index fallback."
    print(output, flush=True)
memory = pathlib.Path("~/.claude/projects/<project>/memory")
p = subprocess.run(["rg", "-n", "-i", "percolation|conformal|proof_steps_need_derived_joint_structure|perceptron_proof_open_gaps_fleet", str(memory / "MEMORY.md")], capture_output=True, text=True, encoding="utf-8", timeout=35)
print("MEMORY_INDEX_TARGETS", p.stdout[:10000], flush=True)
for slug in ("proof_steps_need_derived_joint_structure_2026_09_09", "perceptron_proof_open_gaps_fleet_2026_07_12"):
    path = memory / (slug + ".md")
    if path.exists():
        print("SCAR", slug, path.read_text(encoding="utf-8")[:11000], flush=True)
pathlib.Path("~/brain_workers/w412/recall_evidence.txt").write_text(output + "\nMEMORY_INDEX_TARGETS\n" + p.stdout, encoding="utf-8")
