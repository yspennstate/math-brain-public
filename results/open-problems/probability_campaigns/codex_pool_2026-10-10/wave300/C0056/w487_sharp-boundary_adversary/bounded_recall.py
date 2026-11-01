"""Run the required named recall once with the prescribed 60-second bound."""
import subprocess
from pathlib import Path

job = "C0056 Anderson weak disorder spectral measure annealed quenched resolvent mistakes"
try:
    result = subprocess.run(
        ["python", "-X", "utf8", r"~\.claude\dreaming\brain.py", "recall", job],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60,
    )
    print("RECALL_RETURN_CODE", result.returncode)
    print(result.stdout[:14000])
    if result.stderr:
        print("RECALL_STDERR", result.stderr[:1200])
except subprocess.TimeoutExpired:
    print("RECALL_TIMEOUT_60_SECONDS; use named index fallback")
    index = Path(r"~\.claude\projects\<project>\memory\MEMORY.md")
    terms = ("anderson", "perceptron_proof_open_gaps_fleet", "conditional", "annealed", "quenched")
    matches = [(n, line) for n, line in enumerate(index.read_text(encoding="utf-8").splitlines(), 1)
               if any(term in line.lower() for term in terms)]
    for n, line in matches[:8]:
        print(f"INDEX:{n}: {line}")
