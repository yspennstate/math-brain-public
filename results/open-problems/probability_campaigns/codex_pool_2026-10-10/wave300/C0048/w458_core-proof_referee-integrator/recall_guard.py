import subprocess

cmd = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "C0048 Potts proof referee mistakes"]
try:
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    print(p.stdout[:6000])
    print(p.stderr[:1000])
    print("EXIT", p.returncode)
except subprocess.TimeoutExpired:
    print("RECALL_TIMEOUT_60S")
