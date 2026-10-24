import subprocess

query = "P0110 iid FPP KPZ proof bridge mistakes"
try:
    result = subprocess.run(
        ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", query],
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    print(result.stdout[:12000])
    print(result.stderr[:1500])
except subprocess.TimeoutExpired:
    print("RECALL_TIMEOUT_60S")
