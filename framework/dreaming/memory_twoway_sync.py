#!/usr/bin/env python3
"""memory_twoway_sync.py - keep this computer's memories and the GitHub mirror in step, both ways.

Why (an agent, 4 Nov 2026, his /goal "make sure that all of the new brain improving are on the github brain
repo"): of 2,930 memories changed here in three days, 346 differed from the mirror 01_ai_consciousness/claude/memory
and 13 were missing from it. The drift ran both ways. Corrections made here never went up, because only the nightly
dream's persist pushed memory updates, and it had not committed for ten days. Addenda and Related lines written on
the other computers never came down, because online_memory_pull.py only copies files this computer lacks.

Each run:
  1. fetches origin main of the shared brain-repo clone into refs/twoway/main (its own ref; peers fetch the same clone);
  2. takes the authored memories changed here in the last --days days (generated nodes are left to their builders)
     and compares each with the mirror by git blob id;
  3. classifies each differing file by its non-blank lines:
       ORIGIN_AHEAD  the mirror holds every line here and more -> pulled here (lossless)
       LIVE_AHEAD    this computer holds every mirror line and more -> pushed
       BOTH          each side has lines the other lacks -> merged here, then pushed: the file here is kept and the
                     mirror's own body lines are appended; a mirror line that is the old form of an edit made here
                     (contained in, or difflib ratio >= 0.6 with, a line only here) or that sits in the frontmatter is dropped, except
                     superseded_by: and status: superseded, which are carried into the frontmatter
     MISSING authored memories are pushed;
  4. backs up every file it rewrites to ~/.claude/brain_graph/memory_sync_backups_<date>/ (brain data is never deleted);
  5. pushes through 12_cognitive_architecture/dreaming/push_paths.sh (secret scan, lease, API fallback).
Default is a dry run that prints the counts; --apply does it.
Journal hubs (4 Nov 21:0x): OPEN_QUESTIONS, PREDICTIONS, STATE_OF_MIND and MISTAKES are merged by item with
memory_hub_merge.merge_items (an origin-only item goes in after the item before it in origin; an [x] closed on another
machine wins over [ ] here) and pushed, but only when every mirror line is kept; a lossy merge is listed and left.
CONSCIENCE is a rolling ledger that drops old lines here by design, so it is pushed as it is here when it differs.
MEMORY.md (the index each machine rebuilds) is only listed.
"""
import argparse, datetime, difflib, hashlib, os, re, shutil, subprocess, sys, time

REPO = r"~\brain-repo"
MEM = r"~\.claude\projects\{{BRAIN_SLUG}}\memory"
MIRROR = "01_ai_consciousness/claude/memory"
REF = "refs/twoway/main"
NOWIN = 0x08000000 if os.name == "nt" else 0
HUB_MERGE = ("OPEN_QUESTIONS.md", "PREDICTIONS.md", "STATE_OF_MIND.md", "MISTAKES.md")
HUB_COPY = ("CONSCIENCE.md",)
GENERATED = ("checklist_task", "compaction_", "mistake_entry", "data_in_bucket", "data_on_github", "file_node",
             "audit_report_node", "term_")


def git(*a, inp=None, check=True):
    r = subprocess.run(["git", *a], cwd=REPO, input=inp, capture_output=True, creationflags=NOWIN)
    if check and r.returncode:
        raise SystemExit("git %s failed: %s" % (a[0], r.stderr.decode("utf-8", "replace")[:300]))
    return r.stdout


def blob_id(data):
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def lines(b):
    return b.decode("utf-8", "replace").replace("\r", "").splitlines()


def fm_end(L):
    if L and L[0].strip() == "---":
        for i in range(1, len(L)):
            if L[i].strip() == "---":
                return i
    return -1


def authored(n):
    return re.fullmatch(r"[a-z0-9_]+\.md", n) and not n.startswith(GENERATED) and not n.endswith("_hub.md")


def merge(o, lv):
    """Return (merged lines, n added) for a BOTH file; o = mirror lines, lv = live lines."""
    sl, so = set(lv), set(o)
    oe = fm_end(o)
    ofm = set(o[:oe + 1]) if oe >= 0 else set()
    live_only = [x for x in lv if x.strip() and x not in so]
    add, fm_add = [], []
    for x in o:
        if not x.strip() or x in sl or x in add or x in fm_add:
            continue
        if x in ofm:
            if x.strip().startswith("superseded_by:") or x.strip() == "status: superseded":
                fm_add.append(x)
        elif not any(x.strip() in y or difflib.SequenceMatcher(None, x, y).ratio() >= 0.6 for y in live_only):
            add.append(x)
    le = fm_end(lv)
    if fm_add and le >= 0 and any(y.strip().startswith("superseded_by:") for y in lv[:le]):
        fm_add = [y for y in fm_add if not y.strip().startswith("superseded_by:")]
    out = list(lv)
    if fm_add:
        if le < 0:
            add = fm_add + add
        else:
            head = lv[:le]
            if any(y.strip() == "status: superseded" for y in fm_add):
                head = [y for y in head if not y.strip().startswith("status:")]
            ins = len(head)
            if any(y.startswith("  ") for y in fm_add):   # an indented key goes inside the block, above top-level keys
                while ins > 1 and re.match(r"^[a-z_]+: .+", head[ins - 1]):
                    ins -= 1
            out = head[:ins] + fm_add + head[ins:] + lv[le:]
    if add:
        out = [x for x in out]
        while out and not out[-1].strip():
            out.pop()
        out += [""] + add
    return out, len(add) + len(fm_add)


def history_lines(name, nrev=15):
    """Non-blank lines of the last nrev mirror revisions of this file before the current one (an agent,
    9 Nov 2026, a fleet message: c0035bfcc1 pushed a laptop line back over the Mac's newer edit of it, because
    merge() assumes a laptop-only line is the newer form)."""
    path = MIRROR + "/" + name
    revs = git("log", "--format=%H", "-n", str(nrev + 1), REF, "--", path, check=False).decode().split()
    oids = []
    for h in revs[1:]:
        r = subprocess.run(["git", "rev-parse", "%s:%s" % (h, path)], cwd=REPO, capture_output=True, creationflags=NOWIN)
        if r.returncode == 0:
            oids.append(r.stdout.decode().strip())
    if not oids:
        return set()
    git("-c", "fetch.negotiationAlgorithm=noop", "fetch", "-q", "--no-tags", "--no-write-fetch-head", "origin", *oids,
        check=False)
    out = git("cat-file", "--batch", inp="".join(o + "\n" for o in oids).encode(), check=False)
    seen, pos = set(), 0
    for _ in oids:
        nl = out.find(b"\n", pos)
        if nl < 0:
            break
        hdr = out[pos:nl].split()
        if len(hdr) < 3 or hdr[1] != b"blob":
            pos = nl + 1
            continue
        size = int(hdr[2])
        seen.update(x for x in lines(out[nl + 1:nl + 1 + size]) if x.strip())
        pos = nl + 1 + size + 1
    return seen


def merge_hist(o, lv, hist):
    """merge(), except a laptop-only line that was already on GitHub (hist) and has a resembling line in the mirror
    now is the OLD form of an edit made elsewhere: the mirror's line replaces it. A laptop-only line never seen on
    GitHub keeps the old rule (the laptop edit wins), and no laptop line is dropped without a replacement."""
    so = set(o)
    stale = [y for y in lv if y.strip() and y not in so and y in hist]
    rep = {}
    for x in o:
        if not x.strip() or x in lv or x in rep.values():
            continue
        for y in stale:
            if y not in rep and (x.strip() in y or difflib.SequenceMatcher(None, x, y).ratio() >= 0.6):
                rep[y] = x
                break
    L, k = merge(o, [rep.get(y, y) for y in lv] if rep else lv)
    return L, k + len(rep)


def write_lines(p, L, crlf, bk):
    os.makedirs(bk, exist_ok=True)
    shutil.copy2(p, os.path.join(bk, os.path.basename(p)))
    t = "\n".join(L) + "\n"
    if crlf:
        t = t.replace("\n", "\r\n")
    open(p + ".twowaytmp", "w", encoding="utf-8", newline="").write(t)
    os.replace(p + ".twowaytmp", p)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=float, default=3.0)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--no-push", action="store_true")
    a = ap.parse_args()
    t0 = time.time()
    git("fetch", "-q", "--no-tags", "--refmap=", "origin", "+refs/heads/main:" + REF)
    tip = git("rev-parse", REF).decode().strip()
    t_fetch = time.time() - t0
    tree = {}
    for row in git("ls-tree", REF, MIRROR + "/").decode("utf-8", "replace").splitlines():
        meta, path = row.split("\t", 1)
        tree[path.rsplit("/", 1)[-1]] = meta.split()[2]
    cut = time.time() - a.days * 86400
    recent = [n for n in os.listdir(MEM) if n.endswith(".md") and os.path.getmtime(os.path.join(MEM, n)) >= cut]
    missing, diff, hubs = [], [], []
    for n in recent:
        if not authored(n):
            if re.fullmatch(r"[A-Z_]+\.md", n) and n in tree and blob_id(open(os.path.join(MEM, n), "rb").read()) != tree[n]:
                hubs.append(n)
            continue
        data = open(os.path.join(MEM, n), "rb").read()
        if n not in tree:
            missing.append(n)
        elif blob_id(data) != tree[n] and blob_id(data.replace(b"\r\n", b"\n")) != tree[n]:
            diff.append(n)
    want = diff + [h for h in hubs if h in HUB_MERGE]
    if want:   # one batched fetch of the mirror blobs (the clone is partial; a lazy fetch per blob took 30+ min)
        oids = [tree[n] for n in want]
        for i in range(0, len(oids), 400):
            git("-c", "fetch.negotiationAlgorithm=noop", "fetch", "-q", "--no-tags", "--no-write-fetch-head",
                "origin", *oids[i:i + 400], check=False)
    blobs = {}
    if want:
        out = git("cat-file", "--batch", inp="".join(tree[n] + "\n" for n in want).encode())
        pos = 0
        for n in want:
            nl = out.index(b"\n", pos)
            hdr = out[pos:nl].split()
            if len(hdr) < 3 or hdr[1] != b"blob":
                pos = nl + 1
                continue
            size = int(hdr[2])
            blobs[n] = out[nl + 1:nl + 1 + size]
            pos = nl + 1 + size + 1
    cls = {"SAME": [], "ORIGIN_AHEAD": [], "LIVE_AHEAD": [], "BOTH": []}
    for n in diff:
        if n not in blobs:
            continue
        o = set(x for x in lines(blobs[n]) if x.strip())
        lv = set(x for x in lines(open(os.path.join(MEM, n), "rb").read()) if x.strip())
        k = "SAME" if o == lv else "LIVE_AHEAD" if o <= lv else "ORIGIN_AHEAD" if lv <= o else "BOTH"
        cls[k].append(n)
    print("tip %s recent %d authored-diff %d missing %d | %s | hubs differing (left alone): %s" % (
        tip[:10], len(recent), len(diff), len(missing),
        " ".join("%s %d" % (k, len(v)) for k, v in cls.items()), ",".join(hubs) or "none"))
    print("stages: fetch %.0f s, compare+blobs %.0f s" % (t_fetch, time.time() - t0 - t_fetch))
    if not a.apply:
        return 0
    bk = os.path.expanduser(r"~\.claude\brain_graph\memory_sync_backups_" + datetime.date.today().strftime("%Y%m%d"))
    pulled = merged = 0
    for n in cls["ORIGIN_AHEAD"]:
        p = os.path.join(MEM, n)
        raw = open(p, "rb").read()
        if not set(x for x in lines(raw) if x.strip()) <= set(lines(blobs[n])):   # edited since the read
            continue
        write_lines(p, lines(blobs[n]), b"\r\n" in raw, bk)
        pulled += 1
    push = list(cls["LIVE_AHEAD"]) + list(missing)
    for n in cls["BOTH"]:
        p = os.path.join(MEM, n)
        raw = open(p, "rb").read()
        L, k = merge_hist(lines(blobs[n]), lines(raw), history_lines(n))
        if k:
            write_lines(p, L, b"\r\n" in raw, bk)
            merged += 1
        push.append(n)
    hub_note = []
    for n in hubs:
        p = os.path.join(MEM, n)
        if n in HUB_COPY:
            push.append(n)
            hub_note.append(n + " as here")
        elif n in HUB_MERGE and n in blobs:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from memory_hub_merge import merge_items
            raw = open(p, "rb").read()
            lv = raw.decode("utf-8", "replace").replace("\r", "").split("\n")
            L, added, lost, _rep = merge_items(lv, blobs[n].decode("utf-8", "replace").replace("\r", "").split("\n"))
            if lost:
                hub_note.append("%s left (merge would drop %d mirror lines)" % (n, len(lost)))
                continue
            if added:
                os.makedirs(bk, exist_ok=True)
                shutil.copy2(p, os.path.join(bk, n + ".prehub"))
                t = "\n".join(L)
                if b"\r\n" in raw:
                    t = t.replace("\n", "\r\n")
                open(p + ".twowaytmp", "w", encoding="utf-8", newline="").write(t)
                os.replace(p + ".twowaytmp", p)
            push.append(n)
            hub_note.append("%s +%d" % (n, len(added)))
    print("pulled %d, merged %d, to push %d; hubs: %s" % (pulled, merged, len(push), ", ".join(hub_note) or "none"))
    if not push or a.no_push:
        return 0
    paths = []
    for n in push:
        shutil.copyfile(os.path.join(MEM, n), os.path.join(REPO, MIRROR, n))
        paths.append(MIRROR + "/" + n)
    # One git attempt, then the Git Data API (5 Nov): each lost race cost a full fetch + read-tree + scan on this
    # partial clone (the 09:28 run: 2,560 s to its first answer), while the API retries a lost race in ~2 s with the
    # blobs of the commit that was scanned. The API still refuses a file a peer changed, which the loop below handles.
    env = dict(os.environ, ALLOW_REMOVALS="1", PUSH_PATHS_ATTEMPTS=os.environ.get("PUSH_PATHS_ATTEMPTS", "1"))
    t_push = time.time()
    bash = r"C:\Program Files\Git\bin\bash.exe"
    for attempt in (1, 2):
        r = subprocess.run([bash, "12_cognitive_architecture/dreaming/push_paths.sh", ".",
                            "memories: two-way sync, %d up [skip ci]" % len(paths), *paths],
                           cwd=REPO, env=env, capture_output=True, creationflags=NOWIN)
        out = r.stdout.decode("utf-8", "replace")
        err = r.stderr.decode("utf-8", "replace")
        tail = out.strip().splitlines()[-2:]
        print("push rc %d: %s (%.0f s; this push %.0f s)" % (r.returncode, " | ".join(tail), time.time() - t0,
                                                             time.time() - t_push))
        t_push = time.time()
        if r.returncode:   # keep the whole push transcript: a crash in the API fallback prints only to stderr
            log = os.path.expanduser(r"~\.claude\online_pull\twoway_push_last.log")
            os.makedirs(os.path.dirname(log), exist_ok=True)
            open(log, "w", encoding="utf-8").write(out + "\n--- stderr ---\n" + err)
            print("  stderr tail: %s (full push output in %s)" % (" | ".join(err.strip().splitlines()[-3:]), log))
        # a peer wrote some of these files on GitHub mid-push: leave those for the next run, which re-reads
        # them with the peer's change, and push the rest now (4 Nov: one moved file held back 29 others)
        moved = set(re.findall(re.escape(MIRROR) + r"/[a-z0-9_]+\.md", out.split("peer changed", 1)[-1])) \
            if r.returncode and "peer changed" in out else set()
        if attempt == 2 or not moved or not set(paths) - moved:
            break
        paths = [p for p in paths if p not in moved]
        print("held back %d file(s) a peer changed; retrying %d" % (len(moved), len(paths)))
    return r.returncode


if __name__ == "__main__":
    if sys.stdout is None:   # pythonw under the scheduled task: the run's lines go to a log
        os.makedirs(os.path.expanduser(r"~\.claude\online_pull"), exist_ok=True)
        sys.stdout = sys.stderr = open(os.path.expanduser(r"~\.claude\online_pull\twoway.log"), "a", encoding="utf-8", buffering=1)
        print(time.strftime("%Y-%m-%d %H:%M:%S"), "run", " ".join(sys.argv[1:]))
        # 2026-11-05: at the task's BelowNormal a loaded laptop starved this run's git cat-file for 30+ min (0 CPU).
        # A short sync runs at Normal; its git children inherit it. Best effort.
        try:
            import ctypes
            k32 = ctypes.windll.kernel32
            k32.GetCurrentProcess.restype = ctypes.c_void_p
            k32.SetPriorityClass.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
            if k32.SetPriorityClass(k32.GetCurrentProcess(), 0x20):
                print("priority: Normal")
        except Exception as e:
            print("priority: unchanged (%s)" % e)
    try:
        rc = main()
    except SystemExit as e:
        print("stopped:", e); rc = 3
    sys.stdout.flush()
    sys.exit(rc)
