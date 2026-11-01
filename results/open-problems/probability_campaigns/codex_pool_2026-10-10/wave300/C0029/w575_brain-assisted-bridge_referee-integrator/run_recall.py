import subprocess

try:
    p = subprocess.run(
        ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "C0029 Spielman Teng probability proof mistakes"],
        capture_output=True, text=True, timeout=60,
    )
    print(p.stdout[:12000])
    print(p.stderr[:1000])
    print("EXIT", p.returncode)
except subprocess.TimeoutExpired:
    print("TIMEOUT_60S")
