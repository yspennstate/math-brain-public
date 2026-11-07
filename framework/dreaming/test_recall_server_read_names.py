"""Controls for the recall server's env filter (BRS_ENV_READ_ONLY) and the seeder's slug reuse (BRAIN_SEED_SLUG_REUSE).

 R1 a BRAIN_ variable some brain code reads is kept; one nothing reads is dropped
 R2 a name that appears only in a comment does not count as read
 R3 BRS_ENV_READ_ONLY=0 keeps every BRAIN_ variable, as before
 R4 per-call and client-only variables are still dropped even when code names them
 S1 the seeder reuses its slug list while it is handed the same name list object
 S2 a different list with the same names is rebuilt, and the slugs are right
 S3 BRAIN_SEED_SLUG_REUSE=0 rebuilds every time

    python test_recall_server_read_names.py      (a second or two; ALL PASS at the end)
Scans a temporary folder and runs the statements cut from _seeds_from_prompt; nothing of the user's is read.
"""
import ast
import io
import os
import shutil
import sys
import tempfile
import textwrap

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
TMP = tempfile.mkdtemp(prefix="read_names_")
results = []
N = 7


def check(ok, what):
    results.append(bool(ok))
    print(("PASS  " if ok else "FAIL  ") + what)


try:
    import brain_recall_server as brs
    with io.open(os.path.join(TMP, "reader.py"), "w", encoding="utf-8") as fh:
        fh.write('import os\nX = os.environ.get("BRAIN_DEMO_READ")\nY = "%s"\n' % brs.CLIENT_ONLY_ENV[0]
                 + '# BRAIN_DEMO_COMMENT_ONLY is mentioned here and nowhere else\n')
    brs.D = TMP
    env = {"BRAIN_DEMO_READ": "1", "BRAIN_DEMO_UNREAD": "1", "BRAIN_DEMO_COMMENT_ONLY": "1",
           brs.CLIENT_ONLY_ENV[0]: "1", "PATH": "x"}

    def run(off=False):
        os.environ.pop("BRS_ENV_READ_ONLY", None)
        if off:
            os.environ["BRS_ENV_READ_ONLY"] = "0"
        brs._READ_NAMES = None
        return brs.brain_env(env)

    got = run()
    check("BRAIN_DEMO_READ" in got and "BRAIN_DEMO_UNREAD" not in got, "R1 a read variable is kept, an unread one dropped")
    check("BRAIN_DEMO_COMMENT_ONLY" not in got, "R2 a name only in a comment does not count")
    got0 = run(off=True)
    check({"BRAIN_DEMO_READ", "BRAIN_DEMO_UNREAD", "BRAIN_DEMO_COMMENT_ONLY"} <= set(got0) and "PATH" not in got0,
          "R3 off keeps every BRAIN_ variable")
    check(brs.CLIENT_ONLY_ENV[0] not in got and brs.CLIENT_ONLY_ENV[0] not in got0,
          "R4 a client-only variable is dropped even when code names it")
except Exception as e:
    check(False, "server filter raised %s: %s" % (type(e).__name__, e))
finally:
    os.environ.pop("BRS_ENV_READ_ONLY", None)

SRC = io.open(os.path.join(HERE, "spread_recall.py"), encoding="utf-8").read().replace("\r\n", "\n")
LINES = SRC.split("\n")
CODE = ""
for fn in ast.parse(SRC).body:
    if isinstance(fn, ast.FunctionDef) and fn.name == "_seeds_from_prompt":
        for node in ast.walk(fn):
            body = getattr(node, "body", None)
            if not isinstance(body, list):
                continue
            for i, st in enumerate(body):
                if (isinstance(st, ast.Assign) and "_SLUG_REUSE" in ast.dump(st) and i + 1 < len(body)
                        and isinstance(body[i + 1], ast.If)):
                    CODE = textwrap.dedent("\n".join(LINES[st.lineno - 1:body[i + 1].end_lineno]))


def slugs_for(names, holder, off=False):
    os.environ.pop("BRAIN_SEED_SLUG_REUSE", None)
    if off:
        os.environ["BRAIN_SEED_SLUG_REUSE"] = "0"
    g = {"os": os, "_SLUG_REUSE": holder, "names": names}
    exec(CODE, g)
    return g["slugs"]


try:
    if not CODE:
        raise LookupError("no slug reuse in _seeds_from_prompt")
    held = ["a.md", "b.md", "notes.txt"]
    h = {}
    s1 = slugs_for(held, h)
    s2 = slugs_for(held, h)
    check(s1 is s2, "S1 the same name list object reuses the slug list")
    s3 = slugs_for(list(held), h)
    check(s3 is not s1 and s3 == ["a", "b"], "S2 a different list is rebuilt, slugs right: %r" % (s3,))
    h0 = {}
    a, b = slugs_for(held, h0, off=True), slugs_for(held, h0, off=True)
    check(a is not b and a == b == ["a", "b"], "S3 off rebuilds every time")
except Exception as e:
    check(False, "slug reuse raised %s: %s" % (type(e).__name__, e))
finally:
    os.environ.pop("BRAIN_SEED_SLUG_REUSE", None)
    shutil.rmtree(TMP, ignore_errors=True)
print("ALL PASS" if all(results) and len(results) == N else "FAILED %d of %d" % (N - results.count(True), N))
sys.exit(0 if all(results) and len(results) == N else 1)
