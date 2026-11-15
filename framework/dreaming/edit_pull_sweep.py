"""edit_pull_sweep.py [hours=24] [step=8] [--write] - the hourly backstop for memory EDITS made on other computers.
Walks the GitHub heads the pull recorded in ~/.claude/online_pull/run.log over the last <hours>, in windows of every
<step>th head; a compare that is cut off or fails is retried once, a window over GitHub's 300-file cap (or still failing)
is split at its middle head, and a capped one-pull window is read commit by commit with paged files. The union of changed
memories goes to online_memory_pull.pull_edits (ORIGIN_AHEAD only, backup first, race-safe). Dry unless --write.
Task BrainEditPullSweepHourly runs '3 8 --write' via edit_pull_sweep_hourly.vbs (pythonw; output appended to
~/.claude/online_pull/edit_pull_sweep.log). Measured 7 Nov: 3 h = 9 calls, ~20 s; 24 h = 154 calls, 232 s, unresolved 0.
an agent 7 Nov, topic:recall-xc/edit-pull (recall loop T-20261105-016)."""
import os, re, sys, time, datetime as dt
if sys.stdout is None:                      # pythonw: no console, write to the log
    sys.stdout = sys.stderr = open(os.path.join(os.path.expanduser("~"), ".claude", "online_pull", "edit_pull_sweep.log"),
                                   "a", encoding="utf-8", buffering=1)
    print("--- %s %s" % (time.strftime("%Y-%m-%d %H:%M:%S"), " ".join(sys.argv[1:])))
sys.path.insert(0, os.path.join(os.path.expanduser("~"), ".claude", "dreaming"))
import online_memory_pull as opm
a = [x for x in sys.argv[1:] if not x.startswith("--")]
hours = float(a[0]) if a else 24; step = int(a[1]) if len(a) > 1 else 8; write = "--write" in sys.argv
cut = dt.datetime.now() - dt.timedelta(hours=hours)
heads = []
for l in open(os.path.join(os.path.expanduser("~"), ".claude", "online_pull", "run.log"), encoding="utf-8", errors="replace"):
    m = re.match(r"(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d) \S+ ok via api.*?head ([0-9a-f]{10})", l)
    if m and dt.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S") >= cut and (not heads or heads[-1] != m.group(2)):
        heads.append(m.group(2))
heads.append("main")
UNRES = []
fb = opm._fb(); remote = {}; st_ = {"calls": 0, "retried": 0, "split": 0, "unresolved": 0, "by_commit": 0}
def compare(b, h):
    for k in range(2):
        st_["calls"] += 1
        st, r = opm._get_gz(fb, "/repos/%s/compare/%s...%s" % (opm.REPO, b, h), timeout=90)
        if st == 200 and isinstance(r, dict) and "files" in r:
            return r["files"] or []
        if k == 0:
            st_["retried"] += 1; time.sleep(2)
    return None
def by_commits(b, h):
    """A one-pull window over the 300-file cap: read each of its commits with paged files (up to 3000 a commit)."""
    st_["calls"] += 1
    st, r = opm._get_gz(fb, "/repos/%s/compare/%s...%s" % (opm.REPO, b, h), timeout=90)
    cs = (r or {}).get("commits") or []
    if st != 200 or not cs or (r.get("total_commits") or 0) > len(cs):
        return None
    out = {}
    for c in cs:                                   # oldest first, so the newest blob wins
        for page in range(1, 11):
            st_["calls"] += 1
            s2, r2 = opm._get_gz(fb, "/repos/%s/commits/%s?per_page=300&page=%d" % (opm.REPO, c["sha"], page), timeout=90)
            if s2 != 200:
                return None
            fl = (r2 or {}).get("files") or []
            for e in fl:
                out[e.get("filename")] = e
            if len(fl) < 300:
                break
        else:
            return None
    return list(out.values())
def walk(i, j):
    files = compare(heads[i], heads[j])
    if files is None or len(files) >= 300:
        if j - i > 1:
            st_["split"] += 1; m = (i + j) // 2
            walk(i, m); walk(m, j); return
        got = by_commits(heads[i], heads[j]) if files is not None else None
        if got is not None:
            st_["by_commit"] += 1; files = got
        else:
            st_["unresolved"] += 1
            UNRES.append((heads[i], heads[j], "failed" if files is None else "capped %d" % len(files)))
        if files is None:
            return
    for e in files:
        p = e.get("filename") or ""
        if p.startswith(opm.REMOTE_DIR) and e.get("status") != "removed" and e.get("sha"):
            n = p[len(opm.REMOTE_DIR):]
            if n.endswith(".md") and "/" not in n and n != "MEMORY.md":
                remote[n] = e["sha"]
idx = list(range(0, len(heads) - 1, step)) + [len(heads) - 1]
t0 = time.time()
for i, j in zip(idx, idx[1:]):
    walk(i, j)
print("heads %d in %.0f h, windows %d, %s, memories %d, %.0f s" % (len(heads) - 1, hours, len(idx) - 1, st_, len(remote), time.time() - t0))
for u in UNRES:
    print("unresolved %s...%s %s" % u)
opm.LISTING_MODE = "compare"
n, tally = opm.pull_edits(remote, set(os.listdir(opm.MEM)), "sweep%dh" % hours, dry=not write)
print("written", n, tally)
