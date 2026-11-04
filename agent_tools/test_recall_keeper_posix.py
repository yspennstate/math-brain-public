"""test_recall_keeper_posix.py - the recall keeper on Linux/macOS: it starts the server, holds one instance, stops.

    python agent_tools/test_recall_keeper_posix.py

Builds a five-claim store with math_brain.cli in a temporary folder and copies this folder's .py files beside it,
then checks: recall_keeper.py starts recall_server.py and the server publishes endpoint.json; a recall through it
prints results and the client audit records that the server answered; a second keeper on the same folder exits at
once (one keeper per folder, an flock in the temporary directory); RECALL_KEEPER_STOP stops the keeper, SERVER_STOP
stops the server and removes endpoint.json. Skipped on Windows. Takes one to two minutes (the keeper checks its stop
file once a minute while the server is healthy).
"""
import atexit, json, os, re, shutil, signal, subprocess, sys, tempfile, time

if os.name == "nt":
    print("SKIP: POSIX only")
    sys.exit(0)

SRC = os.path.dirname(os.path.abspath(__file__))
BUILD = next(p for p in (os.path.join(os.path.dirname(SRC), "mathbrain", "src"),
                         os.path.join(os.path.dirname(SRC), "src")) if os.path.isdir(p))
WORK = tempfile.mkdtemp(prefix="keeper_posix_")
HERE = os.path.join(WORK, "dreaming")
os.makedirs(HERE)
for name in os.listdir(SRC):
    if name.endswith(".py") and not name.startswith("test_"):
        shutil.copy(os.path.join(SRC, name), HERE)
STORE = os.path.join(WORK, "st.sqlite3")
ENV = dict(os.environ, MATHBRAIN_BUILD_SRC=BUILD, MATHBRAIN_STORE=STORE, PYTHONPATH=BUILD)
for k in [k for k in ENV if k.startswith("MATH_RECALL_")]:
    del ENV[k]
CLAIMS = [
    "Every finite group of prime order is cyclic.",
    "The fundamental group of the circle is the integers.",
    "A compact subset of a Hausdorff space is closed.",
    "Every bounded monotone sequence of real numbers converges.",
    "The Euler characteristic of a closed orientable surface of genus g is 2 - 2g.",
]
QUERY = ["group of prime order is cyclic", "--or", "finite cyclic group"]
res = []
STARTED = []   # every keeper and server pid this test may leave behind


def cleanup():
    open(os.path.join(HERE, "RECALL_KEEPER_STOP"), "w").close()
    open(os.path.join(HERE, "SERVER_STOP"), "w").close()
    log = os.path.join(HERE, "recall_keeper.log")
    if os.path.exists(log):
        STARTED.extend(int(p) for p in re.findall(r"started server pid (\d+)", open(log, encoding="utf-8").read()))
    for pid in STARTED:
        try:
            os.kill(pid, signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass
    shutil.rmtree(WORK, ignore_errors=True)


atexit.register(cleanup)


def ok(name, cond, extra=""):
    res.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name + (" " + extra if extra else ""), flush=True)


def run(args, env, timeout=120):
    return subprocess.run([sys.executable] + args, cwd=WORK, env=env, capture_output=True, text=True, timeout=timeout)


r = run(["-m", "math_brain.cli", "init", STORE], ENV)
for c in CLAIMS:
    if r.returncode != 0:
        break
    r = run(["-m", "math_brain.cli", "add-claim", STORE, c, "--kind", "concept", "--domain", "demo"], ENV)
ok("store built", r.returncode == 0 and os.path.exists(STORE), r.stderr.strip()[-200:])

tool = os.path.join(HERE, "math_recall.py")
direct = run([tool] + QUERY, dict(ENV, MATH_RECALL_SERVER_DISABLE="1"))
ok("direct call prints a result", direct.returncode == 0 and "cyclic" in direct.stdout)

keeper_cmd = [sys.executable, os.path.join(HERE, "recall_keeper.py")]
keeper = subprocess.Popen(keeper_cmd, cwd=WORK, env=ENV, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
STARTED.append(keeper.pid)
endpoint = os.path.join(HERE, "endpoint.json")
deadline = time.time() + 120
while time.time() < deadline and not os.path.exists(endpoint) and keeper.poll() is None:
    time.sleep(0.5)
log = os.path.join(HERE, "recall_keeper.log")
logtext = open(log, encoding="utf-8").read() if os.path.exists(log) else ""
if "gate closed" in logtext and not os.path.exists(endpoint):
    print("SKIP: the server's resource gate refused this machine")
    keeper.kill()
    shutil.rmtree(WORK, ignore_errors=True)
    sys.exit(0)
ok("keeper started a server that published endpoint.json", os.path.exists(endpoint), logtext.strip()[-200:])
pid = json.load(open(endpoint, encoding="utf-8")).get("pid") if os.path.exists(endpoint) else None

audit = os.path.join(HERE, "client_audit.json")
served = run([tool] + QUERY, dict(ENV, MATH_RECALL_CLIENT_AUDIT_FILE=audit))
ok("served call prints the same text", served.returncode == 0 and served.stdout == direct.stdout)
try:
    rec = json.load(open(audit, encoding="utf-8"))
except Exception:
    rec = {}
ok("client audit says the server answered", rec.get("server") == 1, str(rec)[:120])

second = subprocess.Popen(keeper_cmd, cwd=WORK, env=ENV, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
STARTED.append(second.pid)
try:
    second.wait(timeout=30)
except subprocess.TimeoutExpired:
    second.kill()
    second.wait()
ok("a second keeper on the same folder exits at once", second.returncode == 0 and keeper.poll() is None,
   "rc=%s" % second.returncode)

open(os.path.join(HERE, "RECALL_KEEPER_STOP"), "w").close()
try:
    keeper.wait(timeout=150)
except subprocess.TimeoutExpired:
    keeper.kill()
    keeper.wait()
ok("RECALL_KEEPER_STOP stops the keeper", keeper.returncode == 0, "rc=%s" % keeper.returncode)

open(os.path.join(HERE, "SERVER_STOP"), "w").close()
deadline = time.time() + 30
while time.time() < deadline and os.path.exists(endpoint):
    time.sleep(0.5)
gone = True
if pid:
    try:
        os.kill(int(pid), 0)
        gone = False
    except ProcessLookupError:
        pass
    except PermissionError:
        gone = False
    if not gone:   # still exiting; give it a moment before the verdict
        time.sleep(5)
        try:
            os.kill(int(pid), 0)
        except ProcessLookupError:
            gone = True
ok("SERVER_STOP stops the server and removes endpoint.json", gone and not os.path.exists(endpoint))
print("RESULT %d/%d" % (sum(res), len(res)))
sys.exit(0 if all(res) else 1)
