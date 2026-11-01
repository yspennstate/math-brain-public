"""Bounded recall and public manuscript retrieval for the C0047 referee packet."""
import pathlib
import subprocess
import urllib.request

root = pathlib.Path(__file__).resolve().parent
try:
    result = subprocess.run(
        ["python", "~/.claude/dreaming/brain.py", "recall", "C0047 Benjamini Schramm percolation proof mistakes"],
        capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60,
    )
    print("RECALL_EXIT", result.returncode)
    print((result.stdout + result.stderr)[:5000])
except subprocess.TimeoutExpired:
    print("RECALL_TIMEOUT_60S")

url = "https://raw.githubusercontent.com/openai/math/main/preprints/Nonuniqueness-of-percolation-on-nonamenable-quasi-transitive-graphs-September-24-2026/paper.pdf"
target = root / "openai_nonuniqueness_2026.pdf"
with urllib.request.urlopen(url, timeout=45) as response:
    target.write_bytes(response.read())
print("PDF_BYTES", target.stat().st_size)
