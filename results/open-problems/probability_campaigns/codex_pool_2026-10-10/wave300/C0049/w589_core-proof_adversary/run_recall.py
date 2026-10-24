from pathlib import Path
import subprocess

base = Path(__file__).resolve().parent
command = ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall", "C0049 random cluster SLE parafermionic proof mistakes", "-n", "3"]
print("RUN", " ".join(command), flush=True)
with (base / "RECALL.txt").open("w", encoding="utf-8") as output:
    try:
        result = subprocess.run(command, stdout=output, stderr=subprocess.STDOUT, timeout=60)
        print("RETURN_CODE", result.returncode, flush=True)
    except subprocess.TimeoutExpired:
        output.write("\nRECALL_TIMEOUT_60S: use cited scar files; do not hold the stage open.\n")
        print("RECALL_TIMEOUT_60S", flush=True)
print((base / "RECALL.txt").read_text(encoding="utf-8")[-16000:])
