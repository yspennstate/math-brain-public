"""FEI100 supervisor: 100 Codex agents (gpt-6.1-sol, medium, standard tier) on account 5, FEI campaign.

Owner order 2026-10-11 22:43 (see ALLOWED_BY_OWNER.md). Runs windowless under pythonw via launch_fei100.vbs;
a keeper task re-launches it every 10 min (a named mutex keeps one copy). Every child is CREATE_NO_WINDOW.
STOP file: no new stages; running stages finish on their own. Dials: MAX_RUNNING.txt (concurrency ceiling).
Pacing: the weekly meter is kept on a straight line from the first reading to 97% at its reset, so the agents
work the whole week instead of burning it in a day; at 98% nothing new starts.
"""
import ctypes, ctypes.wintypes as wt, datetime as dt, json, os, pathlib, re, subprocess, sys, time

ROOT = pathlib.Path(r"~/brain_workers/FEI100_20261011")
MOP = pathlib.Path(r"~/mop_fei100")
CTX = ROOT / "context"
CODEX = r"~/AppData/Roaming/npm/node_modules/@openai/codex/node_modules/@openai/codex-win32-x64/vendor/x86_64-pc-windows-msvc/bin/codex.exe"
CODEX_HOME = r"~/.codex-img-acc5"
SHIM = r"~/brain_workers/OP200_NIGHT_20261011/shim"
PY = r"C:/Python314/python.exe"
MODEL, EFFORT = "gpt-6.1-sol", "medium"
END = dt.datetime(2026, 10, 21, 19, 15, 57, tzinfo=dt.timezone.utc)
NOWIN, BELOW = 0x08000000, 0x00004000
PARK_PCT, LINE_TOP = 98.0, 97.0
BOOT_MAX, BOOT_STOP = 20, 85.0
SILENT_HUNG = 150 * 60
SYNC_EVERY = 120 * 60
COOLDOWN = 90
MIN_PHYS_GB, MIN_COMMIT_GB = 3.0, 6.0

k32 = ctypes.WinDLL("kernel32", use_last_error=True)
k32.CreateMutexW.restype = wt.HANDLE
k32.CreateMutexW.argtypes = [ctypes.c_void_p, wt.BOOL, wt.LPCWSTR]
k32.OpenProcess.restype = wt.HANDLE
k32.OpenProcess.argtypes = [wt.DWORD, wt.BOOL, wt.DWORD]
k32.GetExitCodeProcess.argtypes = [wt.HANDLE, ctypes.POINTER(wt.DWORD)]
k32.CloseHandle.argtypes = [wt.HANDLE]
k32.TerminateProcess.argtypes = [wt.HANDLE, wt.UINT]
k32.QueryFullProcessImageNameW.argtypes = [wt.HANDLE, wt.DWORD, wt.LPWSTR, ctypes.POINTER(wt.DWORD)]
k32.CreateJobObjectW.restype = wt.HANDLE
k32.CreateJobObjectW.argtypes = [ctypes.c_void_p, wt.LPCWSTR]
k32.SetInformationJobObject.argtypes = [wt.HANDLE, ctypes.c_int, ctypes.c_void_p, wt.DWORD]
k32.AssignProcessToJobObject.argtypes = [wt.HANDLE, wt.HANDLE]


def now():
    return dt.datetime.now(dt.timezone.utc)


def stamp(t=None):
    return (t or now()).strftime("%Y%m%dT%H%M%SZ")


def log(msg):
    with open(ROOT / "supervisor.log", "a", encoding="utf-8") as f:
        f.write(f"{now().isoformat(timespec='seconds')} {msg}\n")


def jload(p, d):
    try:
        return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))
    except Exception:
        return d


def jsave(p, obj):
    p = pathlib.Path(p)
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_text(json.dumps(obj, indent=1), encoding="utf-8")
    os.replace(tmp, p)


class MEMSTAT(ctypes.Structure):
    _fields_ = [("dwLength", wt.DWORD), ("dwMemoryLoad", wt.DWORD)] + [
        (n, ctypes.c_ulonglong) for n in ("tp", "ap", "tpf", "apf", "tv", "av", "aev")]


def mem_gb():
    m = MEMSTAT()
    m.dwLength = ctypes.sizeof(m)
    k32.GlobalMemoryStatusEx(ctypes.byref(m))
    return m.ap / 2**30, m.apf / 2**30


class BASIC(ctypes.Structure):
    _fields_ = [("a", ctypes.c_longlong), ("b", ctypes.c_longlong), ("LimitFlags", wt.DWORD),
                ("c", ctypes.c_size_t), ("d", ctypes.c_size_t), ("e", wt.DWORD), ("f", ctypes.c_size_t),
                ("g", wt.DWORD), ("h", wt.DWORD)]


class EXT(ctypes.Structure):
    _fields_ = [("Basic", BASIC), ("Io", ctypes.c_ulonglong * 6), ("ProcessMemoryLimit", ctypes.c_size_t),
                ("JobMemoryLimit", ctypes.c_size_t), ("p1", ctypes.c_size_t), ("p2", ctypes.c_size_t)]


def cap(proc):
    """Per-process 4 GB, whole agent tree 6 GB; no kill-on-close, so agents outlive a supervisor restart."""
    try:
        j = k32.CreateJobObjectW(None, None)
        e = EXT()
        e.Basic.LimitFlags = 0x100 | 0x200
        e.ProcessMemoryLimit = 4 * 2**30
        e.JobMemoryLimit = 6 * 2**30
        ok1 = k32.SetInformationJobObject(j, 9, ctypes.byref(e), ctypes.sizeof(e))
        ok2 = k32.AssignProcessToJobObject(j, wt.HANDLE(int(proc._handle)))
        if not (ok1 and ok2):
            log(f"job cap not applied pid={proc.pid} set={ok1} assign={ok2} err={ctypes.get_last_error()}")
        return j
    except Exception as ex:
        log(f"job cap failed: {ex}")
        return None


def image(pid):
    h = k32.OpenProcess(0x1000, False, pid)
    if not h:
        return None, False
    code = wt.DWORD()
    alive = bool(k32.GetExitCodeProcess(h, ctypes.byref(code))) and code.value == 259
    buf = ctypes.create_unicode_buffer(1024)
    n = wt.DWORD(1024)
    name = buf.value if k32.QueryFullProcessImageNameW(h, 0, buf, ctypes.byref(n)) else ""
    k32.CloseHandle(h)
    return name, alive


def kill_codex(pid):
    name, alive = image(pid)
    if not alive or not name.lower().endswith("codex.exe"):
        return False
    h = k32.OpenProcess(0x0001, False, pid)
    if h:
        k32.TerminateProcess(h, 1)
        k32.CloseHandle(h)
    return True


def packets():
    d = jload(MOP / "reports/fei-2026-10-11/AGENT_ASSIGNMENTS.json", {})
    return {x["agent_id"]: x for x in d.get("assignments", [])}


def order(pk):
    ids = sorted(pk)
    return [ids[s * 5 + k] for k in range(5) for s in range(len(ids) // 5)]


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40] or "packet"


def meter():
    base = pathlib.Path(CODEX_HOME) / "sessions"
    days = sorted(p for p in base.glob("*/*/*") if p.is_dir())[-2:]
    files = sorted((f for d in days for f in d.glob("rollout-*.jsonl")), key=lambda f: f.stat().st_mtime,
                   reverse=True)[:8]
    best = None
    for f in files:
        try:
            lines = f.read_bytes()[-400000:].decode("utf-8", "replace").splitlines()
        except Exception:
            continue
        for line in reversed(lines):
            if '"rate_limits"' not in line:
                continue
            try:
                e = json.loads(line)
            except Exception:
                continue
            rl = (e.get("payload") or {}).get("rate_limits") or e.get("rate_limits") or {}
            pr = rl.get("primary") or {}
            if "used_percent" in pr:
                ts = e.get("timestamp", "")
                if best is None or ts > best["ts"]:
                    best = {"ts": ts, "used": float(pr["used_percent"]), "resets_at": pr.get("resets_at")}
                break
    return best


def pace_line(st, m):
    if not m or not m.get("resets_at"):
        return None
    t = time.time()
    a = st.get("pace")
    if not a or a.get("resets_at") != m["resets_at"]:
        a = st["pace"] = {"t0": t, "u0": m["used"], "resets_at": m["resets_at"]}
        log(f"pace anchor: used {m['used']}% now, line to {LINE_TOP}% at {m['resets_at']}")
    span = max(1.0, min(a["resets_at"], END.timestamp()) - a["t0"])
    return a["u0"] + (LINE_TOP - a["u0"]) * min(1.0, (t - a["t0"]) / span)


def target(st, m):
    try:
        mx = int((ROOT / "MAX_RUNNING.txt").read_text().strip())
    except Exception:
        mx = 20
    if st.get("park_until", 0) > time.time():
        return 0, "parked (usage limit)"
    if m is None:
        return min(mx, 4), "no meter yet"
    used = m["used"]
    # LINE_TOP.txt (14 Oct 15:5x, claude-aeda7a9b): the line's top for an account that ends before its reset. Owner 14 Oct
    # 04:18 "regardless i want this usage used up full": the fixed 97 line and 98 park left the last three points unspent.
    top, park = LINE_TOP, PARK_PCT
    try:
        top = float((ROOT / "LINE_TOP.txt").read_text().strip())
        park = max(park, top + 0.5)
    except Exception:
        pass
    if used >= park:
        return 0, f"weekly {used}% >= {park}"
    # The account is shared with other agents' tests, so a line drawn from our first reading blocks us whenever they
    # burst. Instead: every agent gets its first stage (bootstrap, ~0.13 pts each), then the remaining budget is spread
    # over the time left to the reset or the campaign end, at the measured cost of one agent-hour.
    boot = sum(1 for a in st["agents"].values() if a["stage"] == 0 and a.get("fails", 0) < 5)
    if boot and used < BOOT_STOP:
        return min(mx, BOOT_MAX), f"bootstrap: {boot} agents before their first finished stage ({used:.1f}%)"
    try:
        per = float((ROOT / "PER_AGENT_PTS_H.txt").read_text().strip())
    except Exception:
        per = 0.4
    # FLOOR.txt: agents kept running while the meter is under 90% whatever the line allows. Set to 10 on 12 Oct 03:3x
    # when the owner told another session to use account 5 up: the week's budget is no longer ours to spread.
    try:
        floor = int((ROOT / "FLOOR.txt").read_text().strip())
    except Exception:
        floor = 1
    end = min(float(m.get("resets_at") or 0), END.timestamp())
    # ACCOUNT_END.txt (14 Oct, claude-aeda7a9b): an ISO time with its offset at which the budget must be spent, for an
    # account that ends before its weekly reset. Owner 14 Oct 01:50 "i only have one more day with this account" and
    # 04:18 "use the rest of the usage over the next 5 hours if possible, but regardless i want this usage used up full".
    # Without it the line ran to the 20 Oct reset and paced the last 7 points to no agents at all.
    try:
        end = min(end, dt.datetime.fromisoformat((ROOT / "ACCOUNT_END.txt").read_text().strip()).timestamp())
    except Exception:
        pass
    hours = max(1.0, (end - time.time()) / 3600)
    allowed = (top - used) / hours
    n = max(min(mx, floor) if used < 90 else 0, min(mx, int(allowed / per)))
    return n, (f"paced: {used:.1f}% used, {allowed:.2f} pts/h for {hours:.0f} h at {per} pts per agent-hour; "
               f"floor {floor} under 90%")


def governor_distress():
    s = jload(r"~/.claude/compute/compute_state.json", {})
    return str(s.get("status", "")).lower() == "distress"


def parse_log(path):
    tid, usage, errs = None, None, []
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                try:
                    e = json.loads(line)
                except Exception:
                    continue
                t = e.get("type")
                if t == "thread.started":
                    tid = e.get("thread_id")
                elif t == "turn.completed":
                    usage = e.get("usage")
                elif t in ("error", "turn.failed"):
                    errs.append(json.dumps(e)[:400])
    except FileNotFoundError:
        pass
    return tid, usage, errs


def fill(template, **kw):
    out = template
    for k, v in kw.items():
        out = out.replace("{" + k + "}", str(v))
    return out


def launch(st, pk, aid):
    a = st["agents"][aid]
    p = pk[aid]
    adir = ROOT / "agents" / aid
    rid = f"{stamp()}-account05-{aid}-{slug(p['topic'])}"
    (adir / "runs" / rid).mkdir(parents=True, exist_ok=True)
    (adir / "logs").mkdir(exist_ok=True)
    first = not a.get("thread")
    tpl = (ROOT / ("FIRST_PROMPT.md" if first else "RESUME_PROMPT.md")).read_text(encoding="utf-8")
    prompt = fill(tpl, aid=aid, stream=p["stream"], stream_name=p["stream_name"], topic=p["topic"],
                  assignment=p["assignment"], run_id=rid, adir=str(adir).replace("/", "\\"),
                  root=str(ROOT).replace("/", "\\"), mop=str(MOP).replace("/", "\\"),
                  ctx=str(CTX).replace("/", "\\"), utc=now().strftime("%Y-%m-%d %H:%M"), model=MODEL, effort=EFFORT)
    n = a["stage"]
    logp = adir / "logs" / f"{n:03d}_{rid}.jsonl"
    cmd = [CODEX, "exec", "--skip-git-repo-check", "-m", MODEL, "-c", f'model_reasoning_effort="{EFFORT}"',
           "-c", 'service_tier="standard"', "-c", "model_auto_compact_token_limit=250000", "--json",
           "-o", str(adir / "logs" / f"{n:03d}.last.txt"), "-C", str(adir)]
    cmd += ["-"] if first else ["resume", a["thread"], "-"]
    env = dict(os.environ)
    env.pop("AGENT_MESH_ID", None)
    env.update(CODEX_HOME=CODEX_HOME, PYTHONUTF8="1", FEI100_AGENT=aid, PATH=SHIM + os.pathsep + env.get("PATH", ""))
    out = open(logp, "wb")
    err = open(adir / "logs" / f"{n:03d}.err", "wb")
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=out, stderr=err, cwd=str(adir), env=env,
                            creationflags=NOWIN | BELOW)
    cap(proc)
    proc.stdin.write(prompt.encode("utf-8"))
    proc.stdin.close()
    out.close()
    err.close()
    a.update(status="running", pid=proc.pid, run_id=rid, log=str(logp), started=time.time())
    log(f"launch {aid} stage {n} pid {proc.pid} {'new' if first else 'resume ' + a['thread']} run {rid}")
    return proc


def finalize(st, aid, procs):
    a = st["agents"][aid]
    tid, usage, errs = parse_log(a["log"])
    if tid:
        a["thread"] = tid
    rec = {"t": now().isoformat(timespec="seconds"), "agent": aid, "stage": a["stage"], "run_id": a["run_id"],
           "thread": a.get("thread"), "usage_reported": usage, "minutes": round((time.time() - a["started"]) / 60, 1),
           "errors": errs[:3]}
    if usage:
        prev = a.get("cum") or {}
        same = prev.get("_thread") == a.get("thread")
        delta = {k: v - (prev.get(k, 0) if same else 0) for k, v in usage.items() if isinstance(v, (int, float))}
        rec["usage_stage"] = delta
        a["cum"] = dict(usage, _thread=a.get("thread"))
        for k, v in delta.items():
            st["totals"][k] = st["totals"].get(k, 0) + max(0, v)
    (ROOT / "ledger").mkdir(exist_ok=True)
    with open(ROOT / "ledger" / "tokens.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
    rd = ROOT / "agents" / aid / "runs" / a["run_id"]
    if rd.exists():
        (rd / ".final").write_text(rec["t"] + "\n", encoding="utf-8")
    text = " ".join(errs).lower()
    if any(s in text for s in ("usage limit", "rate limit", "hit your", "429", "quota")):
        m = meter() or {}
        until = max(time.time() + 3600, float(m.get("resets_at") or 0) if m.get("used", 0) >= 99 else 0)
        st["park_until"] = until
        log(f"usage-limit text in {aid} stage {a['stage']}: parked until {dt.datetime.fromtimestamp(until)}")
    if not usage and not tid:
        a["fails"] = a.get("fails", 0) + 1
    else:
        a["fails"] = 0
    a.update(status="idle", last_end=time.time(), pid=None)
    a["stage"] += 1
    procs.pop(aid, None)
    log(f"done {aid} stage {rec['stage']} {rec['minutes']} min usage={usage} errs={len(errs)}")


def board(st, pk):
    lines = [f"# FEI team board - written {now():%Y-%m-%d %H:%M} UTC by the supervisor", "",
             "Each Codex line: agent, stream, packet, stages finished, then the agent's own STATUS.md (STATE / NEXT).",
             "Each Claude line: the stream lead's STREAM_NOTES.md opening. Read the files themselves for detail.", ""]
    for b in sorted({p["stream"] for p in pk.values()}):
        lines.append(f"## {b} {next(p['stream_name'] for p in pk.values() if p['stream'] == b)}")
        note = ROOT / "claude" / b / "STREAM_NOTES.md"
        if note.exists():
            t = " ".join(note.read_text(encoding="utf-8", errors="replace").split())[:900]
            lines.append(f"- Claude lead ({note}): {t}")
        for aid in sorted(x for x in pk if pk[x]["stream"] == b):
            s = ROOT / "agents" / aid / "STATUS.md"
            t = " ".join(s.read_text(encoding="utf-8", errors="replace").split())[:420] if s.exists() else "(no status yet)"
            lines.append(f"- {aid} | {pk[aid]['topic'][:60]} | stages {st['agents'][aid]['stage']} | {t}")
        lines.append("")
    tmp = ROOT / "BOARD.md.tmp"
    tmp.write_text("\n".join(lines), encoding="utf-8")
    os.replace(tmp, ROOT / "BOARD.md")


def tokens_md(st, m, why, running):
    tot = st["totals"]
    lines = [f"# FEI100 tokens - {now():%Y-%m-%d %H:%M} UTC", "",
             f"Account 5 weekly meter: {m['used'] if m else '?'}% (resets {m['resets_at'] if m else '?'}); target now: {why}; running {running}.",
             "", "Totals over every finished stage (per-stage deltas of the thread-cumulative usage Codex reports):", ""]
    for k in sorted(tot):
        lines.append(f"- {k}: {tot[k]:,}")
    lines += ["", "Per agent (thread-cumulative at the last finished stage):", ""]
    for aid in sorted(st["agents"]):
        c = st["agents"][aid].get("cum")
        if c:
            lines.append(f"- {aid}: stages {st['agents'][aid]['stage']}, in {c.get('input_tokens', 0):,}, cached {c.get('cached_input_tokens', 0):,}, out {c.get('output_tokens', 0):,}, reasoning {c.get('reasoning_output_tokens', 0):,}")
    lines += ["", "Raw ledger: ledger/tokens.jsonl. Full transcripts: the Codex rollouts of these threads in account 5's sessions folder (never deleted)."]
    (ROOT / "TOKENS.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    mtx = k32.CreateMutexW(None, False, "Local\\FEI100_supervisor")
    if ctypes.get_last_error() == 183:
        return
    pk = packets()
    if len(pk) != 100:
        log(f"expected 100 packets, found {len(pk)}; exit")
        return
    st = jload(ROOT / "state.json", {})
    st.setdefault("agents", {})
    st.setdefault("totals", {})
    for aid in pk:
        st["agents"].setdefault(aid, {"stage": 0, "status": "idle"})
    seq = order(pk)
    procs = {}
    log(f"supervisor up pid {os.getpid()}")
    m, last_meter, last_board, last_sync = None, 0, 0, st.get("last_sync", 0)
    why, tgt = "", 0
    while True:
        t = time.time()
        # reap
        for aid, a in st["agents"].items():
            if a.get("status") != "running":
                continue
            p = procs.get(aid)
            done = (p.poll() is not None) if p else not image(a.get("pid") or 0)[1]
            if done:
                finalize(st, aid, procs)
                continue
            try:
                quiet = t - os.path.getmtime(a["log"])
            except OSError:
                quiet = t - a.get("started", t)
            if quiet > SILENT_HUNG and t - a.get("started", t) > SILENT_HUNG:
                log(f"{aid} silent {quiet / 60:.0f} min: ending hung stage (pid {a.get('pid')}: {kill_codex(a.get('pid') or 0)})")
        if t - last_meter > 300:
            m = meter() or m
            tgt, why = target(st, m)
            last_meter = t
        stop = (ROOT / "STOP").exists() or now() >= END
        running = sum(1 for a in st["agents"].values() if a.get("status") == "running")
        slow = governor_distress() and t - st.get("last_launch", 0) < 180
        if not stop and running < tgt and not slow:
            phys, com = mem_gb()
            ready = [x for x in seq if st["agents"][x].get("status") == "idle" and st["agents"][x].get("fails", 0) < 5
                     and t - st["agents"][x].get("last_end", 0) > COOLDOWN]
            ready.sort(key=lambda x: (st["agents"][x]["stage"], seq.index(x)))
            try:
                gp, gc = (float(x) for x in (ROOT / "MEM_GATE.txt").read_text().split()[:2])
            except Exception:
                gp, gc = MIN_PHYS_GB, MIN_COMMIT_GB
            if ready and phys >= gp and com >= gc:
                aid = ready[0]
                try:
                    procs[aid] = launch(st, pk, aid)
                    st["last_launch"] = t
                except Exception as ex:
                    log(f"launch {aid} failed: {ex!r}")
                    st["agents"][aid]["fails"] = st["agents"][aid].get("fails", 0) + 1
            elif ready and t - st.get("last_memlog", 0) > 900:
                log(f"launch held: phys {phys:.1f} GB, commit free {com:.1f} GB")
                st["last_memlog"] = t
        if t - last_board > 600:
            try:
                board(st, pk)
                tokens_md(st, m, why, running)
            except Exception as ex:
                log(f"board failed: {ex!r}")
            last_board = t
        if t - last_sync > SYNC_EVERY:
            try:
                subprocess.Popen([PY, "-X", "utf8", str(ROOT / "fei100_sync.py")], cwd=str(ROOT),
                                 stdout=subprocess.DEVNULL, stderr=open(ROOT / "sync" / "sync.err", "ab"),
                                 creationflags=NOWIN | BELOW)
                log("sync started")
            except Exception as ex:
                log(f"sync launch failed: {ex!r}")
            last_sync = st["last_sync"] = t
        jsave(ROOT / "state.json", st)
        if stop and running == 0:
            log("stop or campaign end, nothing running: exit")
            return
        time.sleep(20 if running < tgt else 45)


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        log(f"supervisor crashed: {ex!r}")
        raise
