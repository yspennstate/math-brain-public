import subprocess

try:
    p = subprocess.run(
        ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "P0162 Fourier entropy influence proof mistakes"],
        capture_output=True,
        text=True,
        timeout=60,
    )
    print(p.stdout[:6000])
    print(p.stderr[:1000])
except subprocess.TimeoutExpired:
    print("RECALL_TIMEOUT_60S")
