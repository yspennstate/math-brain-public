"""rem_codex_arm.py - run the dream's REM prompt through Codex when every Claude account is at its limit.

    python rem_codex_arm.py [any claude arguments, ignored] < prompt.md > result.json
    python rem_codex_arm.py --selftest

Measured 10 Nov 2026: of 37 REM sessions since 20 Oct, 15 ended on "You've hit your weekly limit" - the main login
and both pool accounts were spent on the same nights, so no Claude arm could run and the night's consolidation was
lost. run_dream.ps1 calls this as its last arm. It reads the REM prompt on stdin, runs one `codex exec` (gpt-6.1-sol,
high effort, normal speed, no window, BelowNormal), and prints ONE json object shaped like `claude -p --output-format
json` gives: is_error, num_turns, total_cost_usd, result, session_id - so the caller's parsing and retry rules apply
unchanged. The Codex log is kept in logs/rem_codex_<stamp>.log; the thread id it prints is in the json.

Dials (environment): REM_CODEX_HOME (default: the first line of rem_codex_home.txt beside this file, else
~/.codex-img-acc4), REM_CODEX_TIMEOUT_S (default 2400), REM_CODEX_MODEL (default gpt-6.1-sol).
Speed is never a dial: service_tier is pinned to default and both fast modes are off (owner, 8 Nov 2026).
"""
import ctypes
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
NOWIN = 0x08000000
BELOW_NORMAL = 0x00004000
CODEX = os.path.expandvars(r"%APPDATA%\npm\codex.cmd")
HEADER = (
    "You are running the brain's nightly REM dream pass. Every Claude account is at its weekly limit tonight, so this "
    "pass runs in Codex. The prompt below was written for a Claude session: where it names a Claude tool, use your "
    "shell and file tools to the same effect. Start no helper agents. Open the journal file first and append to it "
    "as each section finishes, so a cut leaves the work on disk. Your last message is a short report of what you "
    "did.\n\n---\n\n"
)


class MemStat(ctypes.Structure):
    _fields_ = [("l", ctypes.c_ulong), ("ml", ctypes.c_ulong), ("tp", ctypes.c_ulonglong), ("ap", ctypes.c_ulonglong),
                ("tf", ctypes.c_ulonglong), ("af", ctypes.c_ulonglong), ("tv", ctypes.c_ulonglong),
                ("av", ctypes.c_ulonglong), ("x", ctypes.c_ulonglong)]


def memory():
    m = MemStat()
    m.l = ctypes.sizeof(MemStat)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return m.ap // 2 ** 20, 1 - m.af / max(m.tf, 1)


def min_avail_mb(env_value=None):
    """Free physical memory the arm needs before it starts a Codex worker. 6 GB since 10 Nov 2026 (it was 2.5 GB):
    the laptop's Codex fleet sizes each worker at about that, and a REM worker started under it pushes the box into
    its pagefile while the fleet is up. REM_CODEX_MIN_AVAIL_MB overrides; a value that is not a number is ignored."""
    v = os.environ.get("REM_CODEX_MIN_AVAIL_MB", "") if env_value is None else env_value
    return int(v) if str(v).strip().isdigit() else 6000


def memory_ok(avail, commit, floor=None):
    return avail >= (min_avail_mb() if floor is None else floor) and commit <= 0.92


DEFAULT_HOMES = (".codex-img-acc4", ".codex-img-acc3", ".codex-img-acc5", ".codex-img-acc2")
REFUSED = re.compile(r"usage limit|rate limit|not logged in|multi-factor authentication", re.I)


def codex_homes(env_value=None, file_text=None):
    """The Codex homes to try, in order. REM_CODEX_HOME names one; rem_codex_home.txt lists one per line; without
    either, the accounts whose weekly usage goes to the brain (acc4 first: the laptop fleet's owner agreed to it on
    10 Nov). A home is left for the next one only when it refuses at once (spent, or not signed in)."""
    if env_value is None:
        env_value = os.environ.get("REM_CODEX_HOME", "")
    if env_value.strip():
        return [env_value.strip()]
    if file_text is None:
        try:
            file_text = open(os.path.join(HERE, "rem_codex_home.txt"), encoding="utf-8").read()
        except OSError:
            file_text = ""
    listed = [l.strip() for l in file_text.splitlines() if l.strip() and not l.strip().startswith("#")]
    if listed:
        return listed
    return [os.path.join(os.path.expanduser("~"), d) for d in DEFAULT_HOMES]


def codex_home():
    return codex_homes()[0]


def result(is_error, text, turns=0, session_id="", **extra):
    out = {"type": "result", "subtype": "codex_arm", "is_error": bool(is_error), "num_turns": int(turns),
           "total_cost_usd": 0, "result": text, "session_id": session_id, "runner": "codex"}
    out.update(extra)
    return out


def classify(rc, last, log_text, timed_out):
    """(is_error, text). A refusal keeps the word the caller's retry rule matches on (limit / usage)."""
    tail = re.sub(r"\s+", " ", log_text[-1500:])
    m = re.search(r"(usage limit[^.]{0,160}|rate limit[^.]{0,160}|not logged in[^.]{0,80}|"
                  r"multi-factor authentication required[^.]{0,80})", log_text, re.I)
    if timed_out:
        return (not last.strip()), (last.strip() or "codex arm timed out with no final message: " + tail[-300:])
    if rc != 0 or not last.strip():
        return True, ("codex arm failed (rc %s): %s" % (rc, m.group(1) if m else tail[-300:]))
    return False, last.strip()


def run(prompt):
    """Try each home in turn; move on only when one refuses at once (under five minutes, spent or not signed in)."""
    out = result(True, "codex arm unavailable: no Codex home listed")
    for home in codex_homes():
        out = run_home(prompt, home)
        out["codex_home"] = os.path.basename(home)
        quick = out.get("duration_ms", 0) < 300000
        if not (out["is_error"] and quick and (REFUSED.search(out["result"]) or "no Codex home at" in out["result"])):
            break
    return out


def run_home(prompt, home):
    if not os.path.exists(CODEX):
        return result(True, "codex arm unavailable: codex.cmd not found")
    if not os.path.isdir(home):
        return result(True, "codex arm unavailable: no Codex home at " + home)
    avail, commit = memory()
    if not memory_ok(avail, commit):
        return result(True, "codex arm held by its memory gate (avail %d MB, floor %d MB, commit %.3f) - "
                            "temporarily unavailable" % (avail, min_avail_mb(), commit))
    stamp = time.strftime("%Y%m%d_%H%M%S")
    logs = os.path.join(HERE, "logs")
    os.makedirs(logs, exist_ok=True)
    log_path = os.path.join(logs, "rem_codex_%s.log" % stamp)
    last_path = os.path.join(logs, "rem_codex_%s.last.md" % stamp)
    model = os.environ.get("REM_CODEX_MODEL", "gpt-6.1-sol")
    timeout = int(os.environ.get("REM_CODEX_TIMEOUT_S", "2400"))
    cmd = [CODEX, "exec", "--skip-git-repo-check", "-m", model, "-c", 'model_reasoning_effort="high"',
           "-c", 'service_tier="default"', "-c", "features.fast_mode=false", "-c", "features.ultrafast_mode=false",
           "-c", 'sandbox_mode="danger-full-access"', "-c", "features.hooks=false",
           "-C", os.path.expanduser("~"), "-o", last_path, "-"]
    # hooks off: with them on, the checklist hook filed this prompt as an ask of the author's (T-20261110-053, the
    # 05:29 wiring test) and the prompt hooks put ten thousand characters of his asks in front of the dream.
    env = dict(os.environ, CODEX_HOME=home)
    timed_out = False
    t0 = time.time()
    with open(log_path, "w", encoding="utf-8", errors="replace") as log:
        log.write("rem_codex_arm %s home=%s model=%s timeout=%ds avail=%dMB commit=%.3f\n"
                  % (stamp, os.path.basename(home), model, timeout, avail, commit))
        log.flush()
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=log, stderr=subprocess.STDOUT, env=env,
                             creationflags=NOWIN | BELOW_NORMAL)
        try:
            p.communicate((HEADER + prompt).encode("utf-8"), timeout=timeout)
        except subprocess.TimeoutExpired:
            timed_out = True
            subprocess.run(["taskkill", "/PID", str(p.pid), "/T", "/F"], capture_output=True, creationflags=NOWIN)
            try:
                p.communicate(timeout=30)
            except Exception:
                pass
    rc = p.returncode
    try:
        log_text = open(log_path, encoding="utf-8", errors="replace").read()
    except OSError:
        log_text = ""
    try:
        last = open(last_path, encoding="utf-8", errors="replace").read()
    except OSError:
        last = ""
    sid = ""
    m = re.search(r"session id:\s*([0-9a-fA-F-]{36})", log_text)
    if m:
        sid = m.group(1)
    turns = len(re.findall(r"^(?:exec|codex)$", log_text, re.M)) or (1 if last.strip() else 0)
    is_error, text = classify(rc, last, log_text, timed_out)
    # session_id stays empty on purpose: a timed dream passes it to `claude --resume`, and a Codex thread id there
    # would break the next Claude attempt. The thread id travels as codex_thread.
    return result(is_error, text, turns, "", duration_ms=int((time.time() - t0) * 1000), codex_log=log_path,
                  codex_thread=sid, timed_out=timed_out)


def selftest():
    fails = []
    n = [0]

    def check(name, cond, detail=""):
        n[0] += 1
        if not cond:
            fails.append(name + (" :: " + str(detail)[:200] if detail else ""))
        print(("ok   " if cond else "FAIL ") + name)

    retry_rx = re.compile(r"limit|usage|credit|connect|overload|timeout|timed out|unavailable|502|503|500|429|temporarily")
    e, t = classify(0, "Journal written; three sections done.", "exec\nls\ncodex\nfine\n", False)
    check("a finished run is not an error and returns the last message", (e, t) == (False, "Journal written; three sections done."))
    e, t = classify(1, "", "ERROR: You've hit your usage limit. Try again at 6:00 PM.\n", False)
    check("a usage refusal is an error the caller retries on", e and retry_rx.search(t), t)
    e, t = classify(1, "", "stream error: Not logged in\n", False)
    check("not logged in is an error", e and "not logged in" in t.lower(), t)
    check("not logged in is not retried as transient", not retry_rx.search(t), t)
    e, t = classify(None, "partial report", "exec\n", True)
    check("a timeout that left a final message keeps it", (e, t) == (False, "partial report"))
    e, t = classify(None, "", "exec\nworking\n", True)
    check("a timeout with nothing written is an error the caller retries on", e and retry_rx.search(t), t)
    e, t = classify(0, "   ", "nothing\n", False)
    check("exit 0 with an empty last message is an error", e)
    r = result(True, "x", 3, "abc")
    check("the result carries the fields run_dream.ps1 reads",
          all(k in r for k in ("is_error", "num_turns", "total_cost_usd", "result", "session_id")))
    check("the result is one json object starting with a brace", json.dumps(r).startswith("{"))
    old = os.environ.get("REM_CODEX_HOME")
    os.environ["REM_CODEX_HOME"] = r"C:\no\such\codex\home"
    try:
        r = run("hello")
    finally:
        if old is None:
            os.environ.pop("REM_CODEX_HOME", None)
        else:
            os.environ["REM_CODEX_HOME"] = old
    check("a missing Codex home is refused before anything is launched",
          r["is_error"] and ("unavailable" in r["result"]), r["result"])
    check("that refusal is one the caller treats as transient", bool(retry_rx.search(r["result"])), r["result"])
    check("REM_CODEX_HOME names the one home", codex_homes("C:\\x\\one", "a\nb\n") == ["C:\\x\\one"])
    check("rem_codex_home.txt lists homes in order, comments skipped", codex_homes("", "# note\nC:\\a\n\nC:\\b\n") == ["C:\\a", "C:\\b"])
    d = codex_homes("", "")
    check("the default list starts at acc4 and never names acc6", d[0].endswith(".codex-img-acc4") and not any("acc6" in h for h in d), d)
    check("a spent home is one the arm moves past", bool(REFUSED.search("codex arm failed (rc 1): usage limit reached")))
    check("a finished report is not", not REFUSED.search("Journal written; three sections done."))
    check("the memory floor is 6 GB unless the env names a number",
          (min_avail_mb(""), min_avail_mb("8000"), min_avail_mb("lots")) == (6000, 8000, 6000))
    check("5 GB free holds the arm, 7 GB lets it start", not memory_ok(5000, 0.5, 6000) and memory_ok(7000, 0.5, 6000))
    check("a commit charge over 92 pct holds the arm whatever is free", not memory_ok(20000, 0.93, 6000))
    check("the memory hold is one the caller treats as transient and not a spent home",
          bool(retry_rx.search("codex arm held by its memory gate (avail 1 MB, floor 6000 MB, commit 0.5) - temporarily unavailable"))
          and not REFUSED.search("codex arm held by its memory gate (avail 1 MB, floor 6000 MB, commit 0.5) - temporarily unavailable"))
    cmdline = " ".join(["-c", 'service_tier="default"', "features.fast_mode=false", "features.ultrafast_mode=false"])
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    check("the launch pins normal speed", all(s in src for s in cmdline.split(" ")[1:]))
    check("no faster tier can be asked for",
          not re.search("service_tier=." + "(fast|priority|flex)", src))
    print("%s: %d checks, %d failed" % ("PASS" if not fails else "FAIL", n[0], len(fails)))
    for f in fails:
        print("  " + f)
    return 1 if fails else 0


def main():
    if sys.argv[1:] == ["--selftest"]:
        return selftest()
    prompt = sys.stdin.buffer.read().decode("utf-8", "replace")
    if not prompt.strip():
        out = result(True, "codex arm got an empty prompt")
    else:
        try:
            out = run(prompt)
        except Exception as exc:
            out = result(True, "codex arm crashed: " + str(exc)[:300])
    sys.stdout.write(json.dumps(out))
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
