import pathlib
import subprocess

root = pathlib.Path(__file__).resolve().parent
command = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "Metropolis geometric time Cayley fork join open problems mistakes"]
try:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", timeout=55)
    output = result.stdout[:18000] + "\n" + result.stderr[:1000]
except subprocess.TimeoutExpired:
    output = "RECALL_TIMEOUT_55S; use the named memory index fallback.\n"
(root / "recall_receipt.txt").write_text(output, encoding="utf-8")
print(output)
