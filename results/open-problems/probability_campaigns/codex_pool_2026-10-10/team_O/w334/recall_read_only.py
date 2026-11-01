"""Run the requested recall with a 60-second bound and no live mutations."""
import os
from pathlib import Path
import runpy
import subprocess
import sys

HERE = Path(__file__).resolve().parent
QUERY = "team O open problems counterexamples proof mistakes"

if "--worker" in sys.argv:
    sys.dont_write_bytecode = True
    os.environ.update(BRAIN_GRAPH_LAMBDA="0", BRAIN_RECALL_REFRESH="0", BRAIN_RECALL_QUERY_EMBED="0")
    def guard(event, args):
        if event == "open":
            path, mode, flags = args
            writes = (isinstance(mode, str) and any(c in mode for c in "wax+")) or (isinstance(flags, int) and flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND))
            if writes and (not isinstance(path, (str, bytes, os.PathLike)) or not Path(path).resolve().is_relative_to(HERE)):
                raise PermissionError("w334 forbids live writes during recall")
        if event.startswith("socket.") and event in {"socket.connect", "socket.connect_ex"}:
            raise PermissionError("w334 local-only recall")
        if event == "subprocess.Popen":
            raise PermissionError("w334 recall cannot launch helpers")
        if event == "sqlite3.connect" and args[0] != ":memory:" and "mode=ro" not in str(args[0]):
            raise PermissionError("w334 requires read-only sqlite")
        if event in {"os.remove", "os.rmdir", "os.rename", "os.mkdir"}:
            raise PermissionError("w334 recall cannot mutate directories")
    sys.addaudithook(guard)
    brain = "~/.claude/dreaming/brain.py"
    sys.path.insert(0, str(Path(brain).parent))
    sys.argv = [brain, "recall", QUERY, "-n", "3"]
    runpy.run_path(brain, run_name="__main__")
else:
    try:
        result = subprocess.run([sys.executable, "-B", "-X", "utf8", __file__, "--worker"], capture_output=True, text=True, encoding="utf-8", timeout=60)
        text = result.stdout + result.stderr
    except subprocess.TimeoutExpired as exc:
        text = "Recall reached the required 60-second timeout; use the MEMORY.md grep fallback.\n"
        if exc.stdout:
            text += exc.stdout.decode("utf-8", "replace") if isinstance(exc.stdout, bytes) else exc.stdout
    (HERE / "recall.md").write_text(text, encoding="utf-8")
    print(text[:4500])
