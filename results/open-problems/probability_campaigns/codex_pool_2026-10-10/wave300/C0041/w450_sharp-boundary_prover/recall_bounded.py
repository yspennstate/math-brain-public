import os
import subprocess
from pathlib import Path

env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
cmd = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "C0041 uniformly elliptic iid random environment directional transience ballisticity proof mistakes"]
try:
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=60, env=env)
    output = result.stdout + "\nSTDERR:\n" + result.stderr
except subprocess.TimeoutExpired as exc:
    output = "RECALL_TIMEOUT_60S\n"
    if exc.stdout:
        output += exc.stdout.decode("utf-8", errors="replace") if isinstance(exc.stdout, bytes) else exc.stdout
Path(__file__).with_name("recall_result.txt").write_text(output, encoding="utf-8")
print(output[:16000])
