"""FEI100 sync: finished run directories and the agents' rolling files to GitHub.

math-open-problems master: reports/fei-2026-10-11/runs/<stream>/<RUN_ID>/ (Codex and Claude runs),
reports/fei-2026-10-11/fleet05/ (rolling files, board, token ledger). math-research-brain main: the same under
research_pushes/2026-10-11-full-fei-campaign/handoffs/{fleet05,claude}/. Brain-repo ingestion belongs to
claude-51330238 (agreed 11 Oct 23:5x), so this script does not push there.
Commits are built in a temporary index (read-tree origin/<branch>, hash-object, update-index, commit-tree) and
pushed by object: no checkout, no shared working tree touched. [skip ci] on every commit (math-open-problems runs
CI on push). The secret scanner must pass on the new range before any push.
"""
import ctypes, ctypes.wintypes as wt, datetime as dt, hashlib, json, os, pathlib, subprocess, sys, time

ROOT = pathlib.Path(r"~/brain_workers/FEI100_20261011")
SCAN = r"~/.claude/dreaming/scan_secrets.py"
NOWIN = 0x08000000
MAXF = 20 * 2**20
REPOS = {
    "mop": (pathlib.Path(r"~/math-open-problems"), "master"),
    "mrb": (pathlib.Path(r"~/math-research-brain"), "main"),
}
k32 = ctypes.WinDLL("kernel32", use_last_error=True)
k32.CreateMutexW.restype = wt.HANDLE
k32.CreateMutexW.argtypes = [ctypes.c_void_p, wt.BOOL, wt.LPCWSTR]


def log(msg):
    (ROOT / "sync").mkdir(exist_ok=True)
    with open(ROOT / "sync" / "sync.log", "a", encoding="utf-8") as f:
        f.write(f"{dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')} {msg}\n")


def git(repo, *a, env=None, inp=None, timeout=1200):
    p = subprocess.run(["git", "-C", str(repo), *a], capture_output=True, env=env, input=inp, timeout=timeout,
                       creationflags=NOWIN)
    return p.returncode, p.stdout.decode("utf-8", "replace").strip(), p.stderr.decode("utf-8", "replace").strip()


_SCANNER = []


def flagged_by_scanner(path):
    """Pattern names the repo secret scanner finds in one file (its own scan(), fake-token filters included).
    12 Oct (claude-6bb7036b-s08): every sync from 05:04Z on was refused whole for one SVG holding a base64 PNG
    (A084 out/SIGN_MAP.svg, 19 'long API key' matches), so a flagged file now stays on this computer, listed in
    sync/SKIPPED_FLAGGED.tsv, and the commit still goes through the full scan before any push."""
    if not _SCANNER:
        import importlib.util
        try:
            spec = importlib.util.spec_from_file_location("scan_secrets_for_fei100_sync", SCAN)
            mod = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = mod
            spec.loader.exec_module(mod)
            _SCANNER.append(mod.scan)
        except Exception as ex:  # without the pre-check the final scan still guards every push
            log(f"scanner pre-check not loaded: {ex!r}")
            _SCANNER.append(None)
    scan = _SCANNER[0]
    if scan is None:
        return []
    try:
        text = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ["unreadable"]
    return sorted({name for name, _ in scan(text)})


PART_BYTES, PART_FILES = 24 * 2**20, 1500


def push(name, files, msg, landed):
    """Push in parts of at most PART_BYTES / PART_FILES, each a [skip ci] commit on the newest tip; landed(part) records
    a part the moment it is on the remote. 12 Oct (s08): the backlog was 6,360 files / 162 MB per repo, and one push
    that size dies on a Wi-Fi drop (the brain ingest logged 'RPC failed; curl 55' on 250-file parts the same night)."""
    if not files:
        return "nothing"
    parts, cur, size = [], [], 0
    for lp, rp in files:
        n = lp.stat().st_size
        if cur and (size + n > PART_BYTES or len(cur) >= PART_FILES):
            parts.append(cur)
            cur, size = [], 0
        cur.append((lp, rp))
        size += n
    if cur:
        parts.append(cur)
    last = "unchanged"
    for k, part in enumerate(parts, 1):
        m = msg.replace(" [skip ci]", f", part {k} of {len(parts)} [skip ci]") if len(parts) > 1 else msg
        r = push_part(name, part, m)
        if r in ("fail", "blocked"):
            return r if k == 1 else f"{r} at part {k} of {len(parts)} (parts before it landed)"
        landed(part)
        last = r
    return last if len(parts) == 1 else f"{len(parts)} parts, last {last}"


def push_part(name, files, msg):
    repo, br = REPOS[name]
    idx = ROOT / "sync" / f"idx_{name}"
    env = dict(os.environ, GIT_INDEX_FILE=str(idx))
    # A private tracking ref, and --refmap= so the clone's configured refspec does not also update
    # refs/remotes/origin/<br> in the same fetch (math-research-brain refused that double update, 12 Oct).
    track = f"refs/fei100/{name}-{br}"
    # one git process for every file: a process per file took ~5 s each on this machine (11-12 Oct: 20% of
    # 3,857 files in 70 minutes). Blobs do not depend on the base, so they are hashed once.
    rc, out, err = git(repo, "hash-object", "-w", "--no-filters", "--stdin-paths",
                       inp=("\n".join(str(lp) for lp, _ in files) + "\n").encode("utf-8"))
    hashes = out.split()
    if rc or len(hashes) != len(files):
        log(f"{name} hash-object rc={rc} got {len(hashes)} of {len(files)}: {err[:300]}")
        return "fail"
    info = [f"100644 {h}\t{rp}" for h, (_, rp) in zip(hashes, files)]
    info_bytes = ("\n".join(info) + "\n").encode("utf-8")
    # The scan runs once. It took minutes, and the old loop scanned before every push, so master (the GPT tasks
    # commit one file at a time) had always moved by then: 12 rejected pushes 00:59-02:17Z 12 Oct. Later attempts
    # put the same scanned blobs on a newer base and push straight away.
    scanned = False
    for attempt in range(40):
        rc, _, err = git(repo, "fetch", "-q", "--refmap=", "origin", f"+refs/heads/{br}:{track}")
        if rc:
            log(f"{name} fetch rc={rc} {err[:300]}")
            time.sleep(15)
            continue
        _, base, _ = git(repo, "rev-parse", track)
        if idx.exists():
            idx.unlink()
        rc, _, err = git(repo, "read-tree", base, env=env)
        if rc:
            log(f"{name} read-tree rc={rc} {err[:300]}")
            return "fail"
        rc, _, err = git(repo, "update-index", "--add", "--index-info", env=env, inp=info_bytes)
        if rc:
            log(f"{name} update-index rc={rc} {err[:300]}")
            return "fail"
        _, tree, _ = git(repo, "write-tree", env=env)
        _, btree, _ = git(repo, "rev-parse", base + "^{tree}")
        if tree == btree:
            return "unchanged"
        rc, commit, err = git(repo, "commit-tree", tree, "-p", base, "-m", msg)
        if rc:
            log(f"{name} commit-tree rc={rc} {err[:300]}")
            return "fail"
        if not scanned:
            sc = subprocess.run([sys.executable, "-X", "utf8", SCAN, "--range", f"{base}..{commit}"], cwd=str(repo),
                                capture_output=True, timeout=1200, creationflags=NOWIN)
            if sc.returncode != 0:
                log(f"{name} SECRET SCAN BLOCKED {commit[:12]} rc={sc.returncode}: "
                    f"{(sc.stdout + sc.stderr).decode('utf-8', 'replace')[-600:]}")
                return "blocked"
            scanned = True
            log(f"{name} scan clean on {commit[:12]} ({len(info)} files); pushing on fresh bases")
            continue
        rc, _, err = git(repo, "push", "origin", f"{commit}:refs/heads/{br}")
        if rc == 0:
            log(f"{name} pushed {commit[:12]} on {base[:12]} ({len(info)} files, attempt {attempt})")
            return commit
        first = next((ln for ln in err.splitlines() if "rejected" in ln or "error" in ln), err[:160])
        log(f"{name} push rc={rc} attempt {attempt}: {first[:200]}")
        time.sleep(2)
    return "fail"


def final(rd):
    if (rd / ".final").exists():
        return True
    try:
        newest = max(f.stat().st_mtime for f in rd.rglob("*") if f.is_file())
    except ValueError:
        return False
    return time.time() - newest > 3 * 3600


def main():
    k32.CreateMutexW(None, False, "Local\\FEI100_sync")
    if ctypes.get_last_error() == 183:
        return
    pk = {x["agent_id"]: x for x in json.loads((pathlib.Path(r"~/mop_fei100/reports/fei-2026-10-11/AGENT_ASSIGNMENTS.json")).read_text(encoding="utf-8"))["assignments"]}
    sp = ROOT / "sync" / "sync_state.json"
    state = json.loads(sp.read_text(encoding="utf-8")) if sp.exists() else {}
    state.setdefault("mop", {})
    state.setdefault("mrb", {})
    want = {"mop": [], "mrb": []}
    sigs = {"mop": {}, "mrb": {}}

    skipped = []
    flagged = []

    def add(local, mop_path, mrb_path):
        orig = local
        st = local.stat()
        if st.st_size > MAXF or local.name.startswith(".") and local.name != ".final":
            return
        if "__pycache__" in local.parts or local.suffix.lower() == ".pyc":
            return
        sig = f"{st.st_size}:{int(st.st_mtime)}"
        with open(local, "rb") as fh:
            head = fh.read(8192)
        if b"\0" in head:
            # The secret scanner cannot read NUL-heavy content. UTF-16 text goes up as a UTF-8 copy beside the
            # original name; binaries stay here and are listed in SKIPPED_BINARY.tsv, which does go up.
            enc = "utf-16" if head[:2] in (b"\xff\xfe", b"\xfe\xff") else (
                "utf-16-le" if len(head) > 3 and head[1] == 0 and head[3] == 0 and head[0] else None)
            try:
                text = local.read_bytes().decode(enc) if enc else None
            except UnicodeDecodeError:
                text = None
            if text is None or "\0" in text:
                skipped.append((local, st.st_size))
                return
            u = ROOT / "sync" / "utf8" / (hashlib.sha1(str(local).encode("utf-8")).hexdigest() + ".txt")
            u.parent.mkdir(parents=True, exist_ok=True)
            u.write_bytes(text.encode("utf-8"))
            local = u
            mop_path = mop_path and mop_path + ".utf8.txt"
            mrb_path = mrb_path and mrb_path + ".utf8.txt"
        need = [(name, rp) for name, rp in (("mop", mop_path), ("mrb", mrb_path)) if rp and state[name].get(rp) != sig]
        if not need:
            return
        names = flagged_by_scanner(local)
        if names:
            flagged.append((orig, st.st_size, names))
            return
        for name, rp in need:
            want[name].append((local, rp))
            sigs[name][rp] = sig

    camp = "reports/fei-2026-10-11"
    mirror = "research_pushes/2026-10-11-full-fei-campaign/handoffs"
    runs = []
    for rd in sorted(ROOT.glob("agents/A*/runs/*")):
        aid = rd.parent.parent.name
        if aid in pk and final(rd):
            runs.append((rd, pk[aid]["stream"], "fleet05"))
    for rd in sorted(ROOT.glob("claude/B*/runs/*")):
        if final(rd):
            runs.append((rd, rd.parent.parent.name, "claude"))
    for rd, stream, who in runs:
        for f in rd.rglob("*"):
            if f.is_file():
                rel = f.relative_to(rd).as_posix()
                add(f, f"{camp}/runs/{stream}/{rd.name}/{rel}", f"{mirror}/{who}/{stream}/{rd.name}/{rel}")
    for aid in sorted(pk):
        for fn in ("STATUS.md", "WORKLOG.md", "LEARNED.md"):
            f = ROOT / "agents" / aid / fn
            if f.exists():
                add(f, f"{camp}/fleet05/agents/{aid}/{fn}", f"{mirror}/fleet05/agents/{aid}/{fn}")
    for b in sorted(p.name for p in ROOT.glob("claude/B*")):
        for fn in ("STREAM_NOTES.md", "LEARNED.md"):
            f = ROOT / "claude" / b / fn
            if f.exists():
                add(f, f"{camp}/claude/{b}/{fn}", f"{mirror}/claude/{b}/{fn}")
    for fn in ("BOARD.md", "TOKENS.md", "ledger/tokens.jsonl", "FIRST_PROMPT.md", "RESUME_PROMPT.md",
               "ALLOWED_BY_OWNER.md", "fei100.py", "fei100_sync.py"):
        f = ROOT / fn
        if f.exists():
            add(f, f"{camp}/fleet05/{fn}", f"{mirror}/fleet05/{fn}")
    if skipped:
        man = ROOT / "sync" / "SKIPPED_BINARY.tsv"
        rows = ["path\tbytes\tsha256"] + [
            f"{f.relative_to(ROOT).as_posix()}\t{n}\t{hashlib.sha256(f.read_bytes()).hexdigest()}" for f, n in skipped]
        man.write_text("\n".join(rows) + "\n", encoding="utf-8")
        add(man, f"{camp}/fleet05/SKIPPED_BINARY.tsv", f"{mirror}/fleet05/SKIPPED_BINARY.tsv")
        log(f"binary files kept local and listed: {len(skipped)}")
    if flagged:
        man = ROOT / "sync" / "SKIPPED_FLAGGED.tsv"
        rows = ["path\tbytes\tsha256\tscanner_patterns"] + [
            f"{f.relative_to(ROOT).as_posix()}\t{n}\t{hashlib.sha256(f.read_bytes()).hexdigest()}\t{','.join(p)}"
            for f, n, p in flagged]
        man.write_text("\n".join(rows) + "\n", encoding="utf-8")
        add(man, f"{camp}/fleet05/SKIPPED_FLAGGED.tsv", f"{mirror}/fleet05/SKIPPED_FLAGGED.tsv")
        log(f"files the secret scanner flags, kept local and listed: {len(flagged)}")
    n_runs = len({r[0].name for r in runs})
    for name in ("mop", "mrb"):
        files = want[name]
        if not files:
            log(f"{name}: nothing new")
            continue
        msg = (f"FEI campaign: fleet05 and Claude stream runs ({len(files)} files, {n_runs} finished runs so far) [skip ci]\n\n"
               "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>")

        def landed(part, name=name):
            for _, rp in part:
                state[name][rp] = sigs[name][rp]
            tmp = sp.with_name("sync_state.json.tmp")
            tmp.write_text(json.dumps(state), encoding="utf-8")
            os.replace(tmp, sp)

        r = push(name, files, msg, landed)
        log(f"{name}: {r}")


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        log(f"sync crashed: {ex!r}")
        raise
