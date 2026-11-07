"""test_fastrecall_new_link.py - a link added between two cards the fast path already knows reaches the next walk.

    python test_fastrecall_new_link.py

Builds a three-claim store in a temporary folder and runs math_recall.py once, so the fast path prepares its state.
Then it adds one link between two claims that were already in the store; no claim is added. The next --id walk on
the first claim must name the second claim, and its output must match the walk with the fast path off
(MATH_RECALL_FAST=0). A fast path that reads only new cards would miss the link until a full rebuild. HOME and the
prepared-state cache point into the temporary folder, so the prepared states never touch the real cache.
Needs only the math_brain library and its dependency, cryptography. Takes about 20 seconds.
"""
import json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
UP = os.path.dirname(HERE)
BUILD = next((p for p in (os.path.join(UP, "framework", "mathbrain", "src"), os.path.join(UP, "mathbrain", "src"),
                          os.path.join(UP, "src"))
              if os.path.isdir(os.path.join(p, "math_brain"))), None)
if BUILD is None:
    print("SKIP: math_brain library not found beside this folder")
    sys.exit(0)
WORK = tempfile.mkdtemp(prefix="fr_link_")
STORE = os.path.join(WORK, "st.sqlite3")
ENV = dict(os.environ, MATHBRAIN_BUILD_SRC=BUILD, MATHBRAIN_STORE=STORE, PYTHONPATH=BUILD,
           HOME=WORK, USERPROFILE=WORK, MATH_RECALL_SERVER_DISABLE="1")
for k in [k for k in ENV if k.startswith("MATH_RECALL_") and k != "MATH_RECALL_SERVER_DISABLE"]:
    del ENV[k]
ENV["MATH_RECALL_CACHE_DIR"] = os.path.join(WORK, "cache")   # the default cache sits beside math_recall.py
CLAIMS = ["Every finite group of prime order is cyclic.",
          "A compact subset of a Hausdorff space is closed.",
          "Every bounded monotone sequence of real numbers converges."]
TOOL = os.path.join(HERE, "math_recall.py")
res = []


def ok(name, cond, extra=""):
    res.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name + (" " + extra if extra else ""), flush=True)


def run(args, env=ENV):
    return subprocess.run([sys.executable] + args, cwd=WORK, env=env, capture_output=True, text=True, timeout=300)


ids = []
r = run(["-m", "math_brain.cli", "init", STORE])
for c in CLAIMS:
    if r.returncode == 0:
        r = run(["-m", "math_brain.cli", "add-claim", STORE, c, "--kind", "concept", "--domain", "demo"])
        if r.returncode == 0:
            ids.append(json.loads(r.stdout.strip().splitlines()[-1])["claim_id"])
ok("store built", r.returncode == 0 and len(ids) == 3)
a, b = (ids + ["", ""])[:2]

first = run([TOOL, "group of prime order is cyclic"])
walk0 = run([TOOL, "--id", a])
SECOND = "compact subset of a Hausdorff space"
ok("first calls run", first.returncode == 0 and walk0.returncode == 0)
ok("before the link the walk does not name the second claim", b and SECOND not in walk0.stdout)

sys.path.insert(0, BUILD)
from math_brain.models import EdgeKind, GraphEdge
from math_brain.store import ResearchStore

st = ResearchStore(STORE)
try:
    st.add_edge(GraphEdge(source_id=a, target_id=b, kind=EdgeKind.ANALOGOUS_TO,
                          rationale="both are closure statements"), commit=True)
finally:
    st.close()

fast = run([TOOL, "--id", a], dict(ENV, MATH_RECALL_FAST_DEBUG="1"))
slow = run([TOOL, "--id", a], dict(ENV, MATH_RECALL_FAST="0"))
# the check means something only while the fast path is on: with it off both calls read the store
ok("the fast path served the walk", fast.returncode == 0 and "[fastrecall] live:" not in fast.stderr,
   fast.stderr.strip()[-200:])
ok("the walk after the link names the second claim", fast.returncode == 0 and SECOND in fast.stdout,
   fast.stdout.strip()[-200:])
ok("fast output matches the fast path off", fast.stdout == slow.stdout)

shutil.rmtree(WORK, ignore_errors=True)
print("RESULT %d/%d" % (sum(res), len(res)))
sys.exit(0 if all(res) else 1)
