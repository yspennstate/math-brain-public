"""Use the installed mesh recipient fallback; do not launch or wake processes."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, "~/<private-repo>/12_cognitive_architecture/agent_mesh")
import team_comm

peer = sys.argv[1]
body_file = Path(sys.argv[2]).resolve()
assert peer in ("w436", "w437", "w438", "claude-4a88bc43")
assert body_file.is_relative_to(ROOT)
if peer.startswith("w"):
    assert Path("~/brain_workers", peer).is_dir()
m = team_comm.mesh()
try:
    # This is the same registration-only fallback used by team_comm for a named
    # worker recipient; it does not start an agent, call ring(), or create a team.
    team_comm.ensure(m, peer)
    result = m.send("w435", peer, "P0043/review-packet", body_file.read_text(encoding="utf-8"), kind="message")
    (ROOT / ("DELIVERY_"+peer+".json")).write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps(result))
finally:
    m.conn.close()
