"""Bound a narrow read-only brain recall to 60 seconds."""
import subprocess

query = "P0162 Fourier entropy influence proof mistakes"
try:
    p = subprocess.run(
        ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", query],
        text=True, capture_output=True, timeout=60, check=False,
    )
    print("exit", p.returncode)
    print(p.stdout[:7500])
    print(p.stderr[:1000])
except subprocess.TimeoutExpired:
    print("TIMEOUT_60s")
