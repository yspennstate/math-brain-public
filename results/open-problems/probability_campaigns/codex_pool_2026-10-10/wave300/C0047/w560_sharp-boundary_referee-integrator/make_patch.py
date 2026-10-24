"""Produce a reviewable append-only correction diff; never edits the live record."""
import datetime
import difflib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
live_rel = Path("06_math_research/probability_1000_intake_claude_20260907/attempts.jsonl")
live = Path("~/<private-repo>") / live_rel
raw = live.read_bytes().decode("utf-8")
newline = "\r\n" if b"\r\n" in live.read_bytes() else "\n"
lines = raw.splitlines(keepends=True)
matches = [i for i, line in enumerate(lines) if json.loads(line).get("attempt_id") == "C0047-A001"]
assert len(matches) == 1, matches
record = {
    "schema": "probability-attempt.v1",
    "problem_id": "C0047",
    "attempt_id": "C0047-A001-CORR-W560",
    "corrects_attempt_id": "C0047-A001",
    "author": "w560",
    "recorded_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "method": "Primary-source correction and two independent referee boundary checks",
    "key_identity": "D*rho(G,S)*p_c(G,S)<1 with D=|S| and rho the normalized simple-random-walk spectral radius",
    "result": "The older C0047-A001 phrase p_c<1/rho omits D. Since nonamenable Cayley graphs have rho<1 and p_c<=1, that phrase is automatic and cannot prove p_c<p_u. Juschenko-Nagnibeda Section 1 Theorem 2 equation (3) states the sufficient condition rho*p_c*|S|<1. It is not necessary: on the standard 4-regular tree p_c=1/3, p_u=1, rho=sqrt(3)/2, so D*rho*p_c=2sqrt(3)/3>1. The C_2*C_3 triangle-block graph gives a second obstruction with D*rho*p_c>1.26.",
    "obstruction": "Corrected spectral criterion is sufficient only; no parent-problem proof follows. Recent 2026 bond manuscript claims a full solution, independently unverified here; original site formulation is separate.",
    "independent_check": "w558-C0 and w559-source-002 agree on primary formula; w560 checked both cited formula and explicit boundary examples. Served-model/account independence unverified.",
    "source_url": "https://arxiv.org/html/1206.2183v3",
    "substantive": True,
}
new_lines = lines.copy()
new_lines.insert(matches[0] + 1, json.dumps(record, ensure_ascii=False, separators=(",", ":")) + newline)
path = root / "patches" / "01_c0047_spectral_correction.diff"
path.parent.mkdir(parents=True, exist_ok=True)
diff = difflib.unified_diff(lines, new_lines, fromfile="a/" + live_rel.as_posix(), tofile="b/" + live_rel.as_posix(), n=1)
path.write_bytes("".join(diff).encode("utf-8"))
print("PATCH", path, "ADDED_RECORDS", len(new_lines) - len(lines))
