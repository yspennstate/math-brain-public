import subprocess

try:
    p = subprocess.run(
        ["python", "~/.claude/dreaming/brain.py", "recall",
         "C0044 directional transience proof mistakes"],
        capture_output=True, text=True, timeout=60, encoding="utf-8", errors="replace"
    )
    print((p.stdout + p.stderr)[:6000])
except subprocess.TimeoutExpired:
    print("RECALL_TIMEOUT_60S")
