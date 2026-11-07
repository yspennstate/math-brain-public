"""Controls for the past-session segment slot in brain.py recall (and the builder that feeds it).

 G1 session_segments.py selftest passes (the secret-bearing prompt dropped, a repeated body written once)
 G2 a two-session corpus builds an index whose sidecar scores (no sidecar = no slot)
 G3 a question with a session cue gets the matching segment, gate "cue"
 G4 the same question again in the same session is damped: no segment, gate "repeat"
 G5 a different session still gets it
 G6 no cue and a raw score under the floor: no segment, gate "closed"; with the floor at 0 the gate opens, "bm25"
 G7 no index at all: no segment, gate "no_sidecar", and recall goes on
 G8 the printed row names the past session and the file to read; _recall_body calls the slot

The builder runs as a child process (it points bm25 at its own folder), the brain under test is loaded with
BRAIN_SEG_INDEX and BRAIN_SEGMENT_SLOT_LOG in a temp folder, so nothing touches the real indexes or logs.

    python test_segment_slot.py [BRAIN_PY]      (a few seconds; ALL PASS at the end)
"""
import contextlib
import importlib.machinery
import importlib.util
import inspect
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "brain.py")
SEG = os.path.join(HERE, "session_segments.py")
FLAGS = getattr(subprocess, "CREATE_NO_WINDOW", 0)
results = []
N_CHECKS = 10


def check(ok, what):
    results.append(bool(ok))
    print(("PASS  " if ok else "FAIL  ") + what)


def session(path, prompt, answer):
    rows = [{"type": "user", "message": {"content": prompt}},
            {"type": "assistant", "message": {"content": [{"type": "text", "text": answer}]}}]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(json.dumps(r) for r in rows) + "\n")


def last_gate(log):
    with open(log, encoding="utf-8") as fh:
        return json.loads(fh.read().splitlines()[-1]).get("gate")


tmp = tempfile.mkdtemp(prefix="segslot_")
try:
    r = subprocess.run([sys.executable, "-B", SEG, "selftest"], capture_output=True, timeout=300, creationflags=FLAGS)
    check(r.returncode == 0, "G1 builder selftest: " + r.stdout.decode("utf-8", "replace").strip()[:160])

    root, out = os.path.join(tmp, "transcripts"), os.path.join(tmp, "segments")
    os.makedirs(os.path.join(root, "p"))
    session(os.path.join(root, "p", "a.jsonl"), "please rebuild the lexical postings sidecar for the volcano notes",
            "Rebuilt the lexical postings sidecar, 512 volcano notes indexed.")
    session(os.path.join(root, "p", "b.jsonl"), "render the harbour film at full size tonight",
            "The harbour film rendered, nine minutes long.")
    r = subprocess.run([sys.executable, "-B", SEG, "build", "--root", root, "--out", out], capture_output=True,
                       timeout=600, creationflags=FLAGS)
    idx = os.path.join(out, "bm25_index.json.gz")
    st = {}
    try:
        st = json.loads(r.stdout.decode("utf-8", "replace").strip().splitlines()[-1])
    except Exception:
        pass
    check(r.returncode == 0 and os.path.exists(idx) and st.get("written") == 2 and st.get("missing") == 0,
          "G2 two sessions -> two notes, all indexed (%s)" % {k: st.get(k) for k in ("written", "index_docs", "missing")})

    log = os.path.join(tmp, "logs", "segment_slot.jsonl")
    os.environ["BRAIN_SEG_INDEX"], os.environ["BRAIN_SEGMENT_SLOT_LOG"] = idx, log
    os.environ.pop("CODEX_THREAD_ID", None)
    os.environ["CLAUDE_CODE_SESSION_ID"] = "aaaaaaaa-test"
    spec = importlib.util.spec_from_file_location(
        "brain_under_test", PATH, loader=importlib.machinery.SourceFileLoader("brain_under_test", PATH))
    B = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(B)

    q = "what did we decide yesterday about the volcano postings sidecar"
    s1 = B._segment_slot(q, "some_note")
    want = None
    for f in os.listdir(os.path.join(out, "memory")):
        if f.startswith("transcript_segment_"):
            with open(os.path.join(out, "memory", f), encoding="utf-8") as fh:
                if "volcano" in fh.read():
                    want = f[:-3]
    check(s1 is not None and s1[0] == want and s1[2] == "cue" and "volcano" in s1[3],
          "G3 a session cue brings the volcano segment (%s)" % (s1[:3] if s1 else None,))
    s2 = B._segment_slot(q)
    check(s2 is None and last_gate(log) == "repeat", "G4 the same session is not shown it twice (%s)" % last_gate(log))

    os.environ["CLAUDE_CODE_SESSION_ID"] = "bbbbbbbb-test"
    s3 = B._segment_slot(q)
    check(s3 is not None and s3[0] == want, "G5 another session still gets it")

    os.environ["CLAUDE_CODE_SESSION_ID"] = "cccccccc-test"
    floor = B.SEG_SLOT_FLOOR
    B.SEG_SLOT_FLOOR = 1e9
    s4 = B._segment_slot("volcano postings sidecar")
    check(s4 is None and last_gate(log) == "closed", "G6 no cue, under the floor: closed (%s)" % last_gate(log))
    B.SEG_SLOT_FLOOR = 0.0
    s5 = B._segment_slot("volcano postings sidecar")
    check(s5 is not None and s5[2] == "bm25", "G6 the same query over a floor of 0 opens on bm25")
    B.SEG_SLOT_FLOOR = floor

    B.SEG_SLOT_INDEX = os.path.join(tmp, "nowhere", "bm25_index.json.gz")
    s6 = B._segment_slot(q)
    check(s6 is None and last_gate(log) == "no_sidecar", "G7 no index: no segment, gate %s" % last_gate(log))

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        B._print_segment_row(s1)
    txt = buf.getvalue()
    check("[past session; bm25" in txt and "read it: " + s1[4] in txt, "G8 the row names the session and the file")
    body = inspect.getsource(B._recall_body)
    check("_segment_slot(" in body and "_print_segment_row(" in body, "G8 _recall_body calls the slot")
except Exception as e:
    check(False, "raised %s: %s" % (type(e).__name__, e))
finally:
    shutil.rmtree(tmp, ignore_errors=True)

ok = all(results) and len(results) == N_CHECKS
print("ALL PASS" if ok else "FAILED %d of %d" % (N_CHECKS - results.count(True), N_CHECKS))
sys.exit(0 if ok else 1)
