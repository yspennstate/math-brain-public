"""Same supported team read, with a bounded contention wait and local receipt."""
import contextlib
import io
from pathlib import Path
import sys

sys.path.insert(0, "~/<private-repo>/12_cognitive_architecture/agent_mesh")
import team_comm

team_comm.mesh = lambda: team_comm.Mesh(team_comm.DB, busy_timeout_ms=15000)
buffer = io.StringIO()
with contextlib.redirect_stdout(buffer), contextlib.redirect_stderr(buffer):
    try:
        sys.argv = ["team_comm.py", "read", "--as", "w490", "--max", "8"]
        result = team_comm.main()
    except Exception as error:
        result = 1
        print(str(error))
text = buffer.getvalue()
(Path(__file__).resolve().parent / "TEAM_CHECKPOINT.md").write_text(text, encoding="utf-8")
print(text)
print("team read exit:", result)
