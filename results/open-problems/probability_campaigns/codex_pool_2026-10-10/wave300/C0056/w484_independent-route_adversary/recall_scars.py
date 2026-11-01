import subprocess

command = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "C0056 Anderson delocalization proof mistakes"]
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=60)
    print(result.stdout[:14000])
    print(result.stderr[:1200])
except subprocess.TimeoutExpired:
    print("RECALL_TIMEOUT_60S: use targeted memory-index fallback")
