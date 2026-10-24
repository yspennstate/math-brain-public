import pathlib
import subprocess

root = pathlib.Path(__file__).resolve().parent
try:
    result = subprocess.run(
        ["python", "-X", "utf8", "~/.claude/dreaming/brain.py", "recall",
         "C0120 directed polymer variance proof conditioning mistakes"],
        capture_output=True, text=True, encoding="utf-8", timeout=60,
    )
    text = result.stdout + "\nSTDERR\n" + result.stderr
    (root / "recall.txt").write_text(text, encoding="utf-8")
    print(text[:7500])
    print("returncode", result.returncode)
except subprocess.TimeoutExpired:
    (root / "recall.txt").write_text("TIMEOUT after 60 seconds; use index fallback.\n", encoding="utf-8")
    print("TIMEOUT after 60 seconds; use index fallback.")
