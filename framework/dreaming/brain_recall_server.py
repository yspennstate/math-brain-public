"""brain_recall_server.py - a resident process that answers `brain.py recall` with its built state kept warm.

RECALL-10X lead 1 for brain.py (an agent, 3 Nov 2026). A cold `brain.py recall` spends most of its CPU
reloading state from disk (file caches, the superseded map, listings, tiers, archived index lines, query
expansions, node documents, the fresh-memory scan). This process loads brain.py once, memoizes those reload
functions, and serves recall calls from brain_recall_client.py over localhost.

Correctness rules:
- Every memo is dropped when the state signature changes (memory folder, MEMORY.md, the BM25 index, the
  embedding sidecar, the superseded index, the graph sidecar) and at most STATE_TTL seconds after it was filled.
- The server exits (after answering) when any brain module it imported changed on disk, so a code change is
  never served by old code; the next client call runs cold and starts a fresh server.
- A call whose BRAIN_* environment differs from the server's is declined, and the client runs cold.
- One call at a time; a call that would wait more than LOCK_WAIT seconds is declined (client runs cold).
- Exits after IDLE_EXIT seconds without a call, or when its working set passes RSS_CAP, or when one call has held
  the lock past ORPHAN_S (its client stopped reading at 180 s, so nobody is waiting for the answer).
Launched windowless by the client (python.exe with CREATE_NO_WINDOW, so its own children inherit a hidden
console). Read-only on the brain except what recall itself writes (its usage logs). Never deletes anything.
"""
import contextlib, functools, io, json, os, secrets, socket, socketserver, sys, threading, time

D = os.path.dirname(os.path.abspath(__file__))
STATE_DIR = os.path.join(D, "brain_recall_server")
ENDPOINT = os.path.join(STATE_DIR, "endpoint.json")
LOG = os.path.join(STATE_DIR, "server.log")
CALL_LOG = os.path.join(STATE_DIR, "calls.jsonl")
STATE_TTL = float(os.environ.get("BRS_STATE_TTL", "120"))
IDLE_EXIT = float(os.environ.get("BRS_IDLE_EXIT", "7200"))
LOCK_WAIT = float(os.environ.get("BRS_LOCK_WAIT", "20"))
RSS_CAP = int(float(os.environ.get("BRS_RSS_CAP_GB", "2.5")) * 1024 ** 3)
# 8 Nov 2026 (an agent): a SOFT cap, taken only between calls. The working set climbs ~4 MB a served call (the
# bounded memo stores and the link cache filling on new questions, mostly pymalloc arenas; a fresh process replaying
# 28 calls levels off at +54 MB - brainloop_c462/heap_split_1108.json, rss_steps_1108.json), so the hard cap fired 19
# times in the 72 h to 8 Nov 01:3x, each time right after a call, and the next caller found no server: it spawned one
# and waited for a 6 s (p50) / 17.5 s (p90) load plus the warm-up, or ran cold (cap_cost_1108.json). Past SOFT_CAP and
# SOFT_IDLE_S into a lull the server leaves and starts its successor itself (ported from the Mac copy's respawn, 5 Nov,
# an agent), so the reload lands in the gap. The hard cap stays as the backstop and starts a successor too.
# BRS_SOFT_CAP_GB=0 turns the soft cap off; BRS_RESPAWN=0 turns the successor start off.
SOFT_CAP = int(float(os.environ.get("BRS_SOFT_CAP_GB", "2.1")) * 1024 ** 3)
SOFT_IDLE_S = float(os.environ.get("BRS_SOFT_IDLE_S", "20"))
SPAWN_STAMP = os.path.join(STATE_DIR, "spawn.stamp")
# 8 Nov 2026 (an agent, row 39; an agent's count): 8 of 34 code-change exits since 6 Nov came within 5
# minutes of the previous one - an agent editing a module in several saves cost a restart (first call p50 10.9 s
# against 3.4 s later, brainloop_c462/firstcall_1108.json) per save. A change is acted on once the changed files have
# been quiet CODE_QUIET_S, or after CODE_HOLD_MAX_S whatever happens; until then the loaded code keeps serving.
# BRS_CODE_QUIET_S=0 acts at once (the old behaviour).
CODE_QUIET_S = float(os.environ.get("BRS_CODE_QUIET_S", "300"))
CODE_HOLD_MAX_S = float(os.environ.get("BRS_CODE_HOLD_MAX_S", "1800"))


def soft_cap_due(rss, idle_s, busy, soft_cap=None, idle_need=None):
    """True when the server should hand over to a successor now: past the soft cap, no call in flight, idle long enough."""
    soft_cap = SOFT_CAP if soft_cap is None else soft_cap
    idle_need = SOFT_IDLE_S if idle_need is None else idle_need
    return bool(soft_cap) and not busy and idle_s >= idle_need and rss > soft_cap


def start_successor(script, env=None):
    """Start a fresh server windowless, outside any job, and stamp the spawn so callers wait for its load instead of
    running cold (brain_recall_client._wait_loading reads the stamp). The successor waits on server.lock until this
    process is gone. Returns the Popen or None."""
    import subprocess
    try:
        with open(SPAWN_STAMP, "w") as f:
            f.write(str(time.time()))
    except OSError:
        pass
    env = dict({k: v for k, v in (env if env is not None else os.environ).items() if not k.startswith("BRAIN_")},
               BRS_SUCCESSOR="1")
    exe = sys.executable
    if exe.lower().endswith("pythonw.exe"):
        exe = exe[:-5] + ".exe"
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0) | getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
    breakaway = getattr(subprocess, "CREATE_BREAKAWAY_FROM_JOB", 0)
    for extra in ((breakaway, 0) if breakaway else (0,)):
        try:
            return subprocess.Popen([exe, "-B", script], cwd=D, env=env, stdin=subprocess.DEVNULL,
                                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, close_fds=True,
                                    creationflags=flags | extra, start_new_session=(os.name == "posix"))
        except OSError:
            if not extra:
                raise
    return None
# 6 Nov 2026 (an agent): a call still holding the lock ORPHAN_S after it took it has outlived its client (the
# client reads for 180 s, then runs cold), so nobody will read its answer. In the 48 h to 6 Nov 22:3x, 21 served calls
# ran past 180 s (the longest 1,316 s), 6,201 s of lock time (22 pct of all of it) went to answers no one was waiting
# for, and 58 of the 106 "busy" declines fell inside those stretches. A Python thread cannot be stopped, so the server
# logs the call and exits; the next caller starts a fresh one. BRS_ORPHAN_S=0 turns it off.
ORPHAN_S = float(os.environ.get("BRS_ORPHAN_S", "200"))
WATCH_S = 15.0
IDLE_RELIST_GAP = float(os.environ.get("BRS_IDLE_RELIST_GAP", "8"))   # seconds without a call before the idle re-list
GROUP = {"_tiers": "tiers", "_archived_index_lines": "archive", "expansions": "selfkeyed", "_fc_get": "selfkeyed"}
EXACT_GROUPS = frozenset() if os.environ.get("BRS_EXACT_NO_TTL", "1") == "0" else frozenset({"tiers", "archive"})
MEMO_NAMES = ("_fc_get", "_load_superseded", "_memlist", "_fast_listing", "_archived_index_lines", "_tiers",
              "_fc_fresh_memories", "_fc_overlay", "_sup_rows")


def log(msg):
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S ") + msg + "\n")
    except Exception:
        pass


# BRAIN_ variables brain.py reads on each call (never at import), so the server applies the caller's value for the call
# instead of declining. 3 Nov 2026: 91 of 98 recall calls were declined "brain env differs", all from compact_nodes.py's
# linker, which sets BRAIN_RECALL_REFRESH=0. BRS_PER_CALL_ENV=0 restores the old decline.
# 5 Nov 2026 (an agent, Mac): BRAIN_RECALL_LOG too. graph_lane.log_recall reads it on each call, and every test
# bank sets BRAIN_RECALL_LOG=0, so all of them were declined and ran cold.
# 5 Nov 2026 (an agent): BRAIN_HEADLESS_DIET too. Only hook_dispatch reads it, never recall, and it
# was the laptop's one remaining env decline (55 calls in 24 h).
PER_CALL_ENV = () if os.environ.get("BRS_PER_CALL_ENV", "1") == "0" else (
    "BRAIN_RECALL_REFRESH", "BRAIN_RECALL_LOG", "BRAIN_HEADLESS_DIET")
CLIENT_ONLY_ENV = ("BRAIN_RECALL_SERVER",)   # read by brain_recall_client, never by brain.py


# 6 Nov 2026 (an agent): decline only on BRAIN_ names some .py in the dreaming tree actually names. In the 48 h
# to 6 Nov 00:4x the live residue of env declines (73 of 6,272 calls) was the recall CTAIL variable, which a test harness
# sets and no brain code reads, so those calls ran cold for nothing. No brain code builds a BRAIN_ name at run time
# (checked 6 Nov: no f"BRAIN_{..}" or "BRAIN_" + x), so a literal scan is the whole read set. Read once per server life;
# a code change restarts the server, so a new name is picked up with the code that reads it.
# BRS_ENV_READ_ONLY=0 restores the old rule (every BRAIN_ name counts).
# Comments are stripped before the scan (6 Nov 18:3x): the first landing named the unread variable in this very
# comment, the live scan found it there, and the filter kept it.
_READ_NAMES = None


def _read_names():
    global _READ_NAMES
    if _READ_NAMES is None:
        import re
        names = set()
        pat = re.compile(r"BRAIN_[A-Z0-9_]*[A-Z0-9]")
        comment = re.compile(r"(?m)(^|\s)#.*$")
        for root, dirs, files in os.walk(D):
            dirs[:] = [d for d in dirs if not d.startswith((".", "__"))]
            for fn in files:
                if fn.endswith(".py"):
                    try:
                        with open(os.path.join(root, fn), encoding="utf-8", errors="replace") as fh:
                            names.update(pat.findall(comment.sub("", fh.read())))
                    except OSError:
                        pass
        _READ_NAMES = frozenset(names)
    return _READ_NAMES


def brain_env(env):
    keep = None if os.environ.get("BRS_ENV_READ_ONLY", "1") == "0" else _read_names()
    return {k: v for k, v in env.items()
            if k.startswith("BRAIN_") and k not in PER_CALL_ENV and k not in CLIENT_ONLY_ENV
            and (keep is None or k in keep)}


def rss_bytes():
    try:
        import ctypes
        from ctypes import wintypes

        class PMC(ctypes.Structure):
            _fields_ = [("cb", wintypes.DWORD), ("PageFaultCount", wintypes.DWORD),
                        ("PeakWorkingSetSize", ctypes.c_size_t), ("WorkingSetSize", ctypes.c_size_t),
                        ("QuotaPeakPagedPoolUsage", ctypes.c_size_t), ("QuotaPagedPoolUsage", ctypes.c_size_t),
                        ("QuotaPeakNonPagedPoolUsage", ctypes.c_size_t), ("QuotaNonPagedPoolUsage", ctypes.c_size_t),
                        ("PagefileUsage", ctypes.c_size_t), ("PeakPagefileUsage", ctypes.c_size_t)]
        pmc = PMC(); pmc.cb = ctypes.sizeof(PMC)
        # The pseudo-handle as a pointer: with ctypes' default int restype it reached psapi as an invalid handle on
        # 64-bit, the call failed and this returned 0 every time, so RSS_CAP never fired (4 Nov: 0 against a 342 MB
        # psutil reading). an agent.
        h = ctypes.c_void_p(-1)
        if ctypes.windll.psapi.GetProcessMemoryInfo(h, ctypes.byref(pmc), pmc.cb):
            # 8 Nov 2026 (an agent, from an agent's yitz8 reading): Windows trims the working set when
            # RAM is short, so a cap on WorkingSetSize never fires on a starved box while the private commit stays
            # at 2.6 GB. Take the larger of the working set and the private commit (PagefileUsage).
            return int(max(pmc.WorkingSetSize, pmc.PagefileUsage))
    except Exception:
        pass
    try:  # macOS (4 Nov 2026): peak resident size in bytes; a cap on the peak is the cautious reading
        import resource
        if sys.platform == "darwin":
            return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    except Exception:
        pass
    return 0


class Brain:
    def __init__(self):
        sys.path.insert(0, D)
        os.chdir(D)
        import runpy
        self.g = runpy.run_path(os.path.join(D, "brain.py"), run_name="brain_recall_server_module")["main"].__globals__
        import bm25, brain_node_documents as bnd
        self.stores = []
        self.miss = {}
        stat_fc = os.environ.get("BRS_STAT_FCGET", "1") != "0" and "_fc_file" in self.g and "_fc_get" in self.g
        for name in MEMO_NAMES:
            if name in self.g and not (stat_fc and name == "_fc_get"):
                self._memo(self.g, name)
        if stat_fc:
            self._stat_memo_fc_get()
        # brain.py's two callers of _archived_index_lines .update() the dict with the live index (_recall_body, the
        # owner-line pass), so a memo that hands back its own dict accumulates earlier calls' live lines: a slug that
        # left MEMORY.md would stay in the archive view until the group dropped. Each call gets a copy (47k entries,
        # a few ms). Found by the lever-6 parity control on 3 Nov; present since lever 1, bounded then by the TTL.
        if "_archived_index_lines" in self.g:
            memo = self.g["_archived_index_lines"]
            real = getattr(memo, "__wrapped__", memo)

            def arch_copy(*a, **k):
                return dict(memo(*a, **k))
            arch_copy.__wrapped__ = real
            arch_copy.__name__ = "_archived_index_lines"
            self.g["_archived_index_lines"] = arch_copy
        self._memo(bm25, "expansions")
        if os.environ.get("BRS_STAT_BUNDLES", "1") != "0":
            self._stat_memo_bundles(bnd)
        else:
            self._memo(bnd, "load_documents")
        if "load_documents" in self.g:
            self.g["load_documents"] = bnd.load_documents
        if os.environ.get("BRS_STAT_READDOC", "1") != "0":
            try:
                self._stat_memo_read_doc(bm25, bnd)
            except Exception as e:
                log("read_doc stat memo off: %s: %s" % (type(e).__name__, e))
        mem = self.g.get("MEM") or ""
        folder = [mem, os.path.join(mem, "MEMORY.md")]
        for name in ("bm25_index.json.gz", "memory_embeddings.npz", "superseded_index.json"):
            folder.append(os.path.join(D, name))
        for env_name in ("BRAIN_GRAPH_SIDECAR", "BRAIN_SUPERSEDED_INDEX"):
            if os.environ.get(env_name):
                folder.append(os.environ[env_name])
        self.group_paths = {"folder": folder, "tiers": [os.path.join(D, "consciousness.tsv")],
                            "archive": [os.path.join(mem, "INDEX_ARCHIVE.md")], "selfkeyed": []}
        self.sigs = {}
        self.filled = {}
        # lever 3: the memory folder's listing kept resident by ReadDirectoryChangesW, so a folder drop no longer
        # re-reads ~50k entries (parity 20/20 live, 2000-file burst and forced overflow equal, 10/10 ranked lists
        # equal in resident_ab.jsonl). BRS_RESIDENT_LISTING=0 turns it off; any failure leaves the memo path.
        self.resident = None
        if os.environ.get("BRS_RESIDENT_LISTING", "1") != "0" and "_fast_listing" in self.g:
            try:
                import brain_resident_listing
                self.resident = brain_resident_listing.install(self)
            except Exception as e:
                log("resident listing off: %s: %s" % (type(e).__name__, e))
        # Lever 8 (3 Nov 2026): keep the PARSED embeddings sidecar between calls (embedding_artifact.RESIDENT, keyed
        # by the file's stat plus the authority's sha256 and size); which rows are current is still judged on every
        # call. Loader 1.0-2.4 s -> 0.5-0.65 s on the loaded laptop, 16/16 recall outputs equal. BRS_EMB_RESIDENT=0 off.
        if os.environ.get("BRS_EMB_RESIDENT", "1") != "0":
            try:
                import embedding_artifact
                embedding_artifact.RESIDENT = True
            except Exception as e:
                log("resident embeddings off: %s: %s" % (type(e).__name__, e))
        # Lever 9 (3 Nov 2026): keep the link walk's neighbour lists per sidecar generation (graph_lane.LAZY_RESIDENT);
        # the capture rewrites the sidecar every 15 minutes, which starts a fresh set. BRS_LINK_RESIDENT=0 off.
        if os.environ.get("BRS_LINK_RESIDENT", "1") != "0":
            try:
                import graph_lane
                graph_lane.LAZY_RESIDENT = True
            except Exception as e:
                log("resident link lists off: %s: %s" % (type(e).__name__, e))
        self.code = self._code_sig()
        self._seen = set(sys.modules)
        self._held = None
        self.calls = 0

    def _memo(self, holder, attr):
        f = holder[attr] if isinstance(holder, dict) else getattr(holder, attr)
        store = {}
        self.stores.append((GROUP.get(attr, "folder"), store))
        miss = self.miss

        @functools.wraps(f)
        def w(*a, **k):
            try:
                key = repr((a, sorted(k.items())))
            except Exception:
                return f(*a, **k)
            if key in store:
                return store[key]
            t = time.perf_counter()
            v = f(*a, **k)
            miss[attr] = miss.get(attr, 0.0) + time.perf_counter() - t
            store[key] = v
            return v
        if isinstance(holder, dict):
            holder[attr] = w
        else:
            setattr(holder, attr, w)

    def _stat_memo_read_doc(self, bm25, bnd, cap=1024):
        """lever 15: keep each memory's BM25 token list across folder drops while its files are unchanged.

        A folder drop (any peer memory write) re-ran the fresh-memory overlay, which re-read EVERY memory newer than
        the current postings generation, not the one that changed: 69 fresh at 15:37 on 4 Nov cost the overlay
        244-502 ms a drop, nearly all of it bm25.read_doc. Here a token list is kept while the memory file's
        (mtime_ns, size), its attachment bundle's stat signature (node file, manifest, documents listing - the same
        signature lever 4 uses) and the slug's query-expansion entry are unchanged. A read that adds to
        bm25.ATTACHMENT_FAILURES is not kept. Each caller gets its own copy of the list. The store sits in no group
        and holds at most `cap` slugs, oldest use dropped first. BRS_STAT_READDOC=0 turns it off.
        """
        from collections import OrderedDict
        real = bm25.read_doc
        store = OrderedDict()
        miss = self.miss

        def sig(mem, slug):
            st = os.stat(os.path.join(mem, slug + ".md"))
            out = [(st.st_mtime_ns, st.st_size)]
            root = bnd.bundle_dir(mem, slug)
            for p in (bnd._node_path(bnd.Path(mem), bnd._slug(slug)), root / bnd.MANIFEST_NAME):
                try:
                    s2 = os.lstat(p)
                    out.append((s2.st_mtime_ns, s2.st_size))
                except OSError:
                    out.append(None)
            try:
                with os.scandir(root / "documents") as it:
                    out.append(tuple(sorted((e.name, e.stat(follow_symlinks=False).st_mtime_ns,
                                             e.stat(follow_symlinks=False).st_size) for e in it)))
            except OSError:
                out.append(None)
            out.append((getattr(bm25, "_DATES_ON", None), getattr(bm25, "_EXPANSION_ON", None)))
            if getattr(bm25, "_EXPANSION_ON", False):
                out.append(repr(bm25.expansions().get(slug)))
            return tuple(out)

        @functools.wraps(real)
        def w(mem_dir, slug):
            try:
                key = (str(mem_dir), slug)
                s = sig(str(mem_dir), slug)
            except Exception:
                return real(mem_dir, slug)
            hit = store.get(key)
            if hit is not None and hit[0] == s:
                store.move_to_end(key)
                return None if hit[1] is None else list(hit[1])
            t = time.perf_counter()
            nfail = len(getattr(bm25, "ATTACHMENT_FAILURES", ()))
            v = real(mem_dir, slug)
            miss["read_doc"] = miss.get("read_doc", 0.0) + time.perf_counter() - t
            if len(getattr(bm25, "ATTACHMENT_FAILURES", ())) == nfail:
                store[key] = (s, None if v is None else tuple(v))
                store.move_to_end(key)
                while len(store) > cap:
                    store.popitem(last=False)
            return v
        w.__wrapped__ = real
        bm25.read_doc = w

    def _stat_memo_bundles(self, bnd):
        """lever 4: keep each attachment bundle across folder drops while its own files are unchanged.

        Under the folder memo every memory write anywhere reloaded and re-hashed all 41 bundles (0.22 s, 1 MB);
        the stat signature of one bundle (node file, manifest, documents listing with mtime and size) costs 0.015 s
        for all 41. A writer publishes by replacing the manifest atomically, so any attach changes the signature.
        The store is in no group, so neither a folder drop nor the state TTL clears it; a code change restarts the
        server. BRS_STAT_BUNDLES=0 restores the folder memo.
        """
        f = bnd.load_documents
        store = {}
        miss = self.miss

        def sig(mem, slug):
            out = []
            try:
                st = os.lstat(bnd._node_path(bnd.Path(mem), bnd._slug(slug)))
                out.append((st.st_mtime_ns, st.st_size))
            except Exception:
                out.append(None)
            root = bnd.bundle_dir(mem, slug)
            try:
                st = os.lstat(root / bnd.MANIFEST_NAME)
                out.append((st.st_mtime_ns, st.st_size))
            except Exception:
                out.append(None)
            try:
                with os.scandir(root / "documents") as it:
                    rows = []
                    for e in it:
                        st = e.stat(follow_symlinks=False)
                        rows.append((e.name, st.st_mtime_ns, st.st_size))
                out.append(tuple(sorted(rows)))
            except Exception:
                out.append(None)
            return tuple(out)

        @functools.wraps(f)
        def w(mem, slug, *a, **k):
            try:
                key = repr((str(mem), slug, a, sorted(k.items())))
                s = sig(mem, slug)
            except Exception:
                return f(mem, slug, *a, **k)
            hit = store.get(key)
            if hit is not None and hit[0] == s:
                return hit[1]
            t = time.perf_counter()
            v = f(mem, slug, *a, **k)
            miss["load_documents"] = miss.get("load_documents", 0.0) + time.perf_counter() - t
            store[key] = (s, v)
            return v
        bnd.load_documents = w

    def _stat_memo_fc_get(self, cap=64):
        """lever 5: keep each recall fast-cache file's parsed value while that file is unchanged.

        Under the self-keyed memo every _fc_get value (walk, links, df, sgraph, superseded head and rows, tfkeys)
        was thrown away by the 120 s state TTL and re-unmarshalled, 0.3-0.7 s a call, and a miss (None) was
        memoized until the TTL even after the file was written. Here the key is the cache file's path (one file
        per (name, key) by construction) and the value is kept only while the file's (mtime, size, id) match a
        stat taken before and after the read; a missing file or a None is never kept. One os.stat per lookup.
        The store sits in no group and holds at most `cap` files, newest use last. BRS_STAT_FCGET=0 turns it off.
        """
        from collections import OrderedDict
        real = self.g["_fc_get"]
        path_of = self.g["_fc_file"]
        store = OrderedDict()
        miss = self.miss

        def st3(p):
            st = os.stat(p)
            return (st.st_mtime_ns, st.st_size, st.st_ino)

        @functools.wraps(real)
        def w(name, key):
            try:
                p = path_of(name, key)
                s = st3(p)
            except Exception:
                return real(name, key)
            hit = store.get(p)
            if hit is not None and hit[0] == s:
                store.move_to_end(p)
                return hit[1]
            t = time.perf_counter()
            v = real(name, key)
            miss["_fc_get"] = miss.get("_fc_get", 0.0) + time.perf_counter() - t
            if v is not None:
                try:
                    if st3(p) == s:
                        store[p] = (s, v)
                        store.move_to_end(p)
                        while len(store) > cap:
                            store.popitem(last=False)
                except Exception:
                    pass
            return v
        self.g["_fc_get"] = w

    def _code_sig(self):
        sig = {}
        for m in list(sys.modules.values()):
            p = getattr(m, "__file__", None) or ""
            if p and os.path.abspath(p).lower().startswith(D.lower()) and p.endswith(".py"):
                try:
                    sig[p] = os.stat(p).st_mtime_ns
                except OSError:
                    sig[p] = None
        sig[os.path.join(D, "brain.py")] = os.stat(os.path.join(D, "brain.py")).st_mtime_ns
        return sig

    def watch_new(self):
        """Add dreaming-folder modules imported since the last look to the code watch (8 Nov 2026, row 39). brain.py
        imports brain_syn, query_embed, moved_facts, index_text, diffusion, code_map and others inside functions, after
        _code_sig ran, so an edit to any of them never restarted the server. Run under the server lock, right after a
        call, so the mtime taken is the one the import read (an edit inside that call's own window is the gap left)."""
        new = set(sys.modules) - self._seen
        if not new:
            return []
        self._seen |= new
        added = []
        for n in new:
            p = getattr(sys.modules.get(n), "__file__", None) or ""
            if p.endswith(".py") and os.path.abspath(p).lower().startswith(D.lower()) and p not in self.code:
                try:
                    self.code[p] = os.stat(p).st_mtime_ns
                except OSError:
                    self.code[p] = None
                added.append(os.path.basename(p))
        if added:
            log("code watch now covers %s" % ", ".join(sorted(added)))
        return added

    def code_changed(self):
        self.watch_new()
        hit, newest = None, 0
        for p, m in self.code.items():
            try:
                now = os.stat(p).st_mtime_ns
            except OSError:
                now = None
            if now != m:
                hit = hit or p
                newest = max(newest, now or 0)
        if hit is None:
            self._held = None
            return None
        if CODE_QUIET_S > 0 and newest:
            quiet = time.time() - newest / 1e9
            if self._held is None:
                self._held = (hit, time.time())
            held_s = time.time() - self._held[1]
            if quiet < CODE_QUIET_S and held_s < CODE_HOLD_MAX_S:
                if not self._held[0].startswith("logged:"):
                    log("code changed: %s; serving the loaded code until the changed files are quiet %d s" % (hit, CODE_QUIET_S))
                    self._held = ("logged:" + hit, self._held[1])
                return None
        return hit

    def _state_sig(self, paths):
        out = []
        for p in paths:
            try:
                st = os.stat(p)
                out.append((p, st.st_mtime_ns, st.st_size, st.st_ino))
            except OSError:
                out.append((p, None, None, None))
        return tuple(out)

    def refresh_state(self):
        """lever 6: the tiers and archive groups each read exactly one file (consciousness.tsv, INDEX_ARCHIVE.md) and
        nothing else, so their stat signature (mtime_ns, size, inode) is the whole of their state: they drop only when
        that file changes, never on the TTL (which threw away 0.2-0.5 s of re-reads on every call made more than two
        minutes after the last). The folder group keeps the TTL: its signature does not cover everything its memos
        read. BRS_EXACT_NO_TTL=0 puts the TTL back on every group."""
        dropped = []
        now = time.time()
        for grp, paths in self.group_paths.items():
            sig = self._state_sig(paths)
            ttl_out = grp not in EXACT_GROUPS and now - self.filled.get(grp, 0) > STATE_TTL
            if sig != self.sigs.get(grp) or ttl_out:
                for g, st in self.stores:
                    if g == grp:
                        st.clear()
                self.sigs[grp] = sig
                self.filled[grp] = now
                dropped.append(grp)
        return dropped

    def call(self, argv, env, cwd):
        dropped = self.refresh_state()
        self.miss.clear()
        saved_env = {}
        for k, v in env.items():
            if k.startswith(("CLAUDE", "CODEX", "AGENT")):
                saved_env[k] = os.environ.get(k)
                os.environ[k] = v
        # 6 Nov 2026 (an agent): and unset the ones the caller lacks. The client sends every CLAUDE/CODEX/AGENT
        # name it has, so one it did not send is one a cold run would not see. Before, a caller with no session id (a
        # script, a scheduled task, a Codex call) ran with the spawner's CLAUDE_CODE_SESSION_ID and ENTRYPOINT, and
        # graph_lane.log_recall filed its search under that person's interactive session: 179 of 2,607 served calls
        # in the 48 h to 6 Nov 21:5x. BRS_POP_SESSION_ENV=0 restores the old behaviour.
        if os.environ.get("BRS_POP_SESSION_ENV", "1") != "0":
            for k in [k for k in os.environ if k.startswith(("CLAUDE", "CODEX", "AGENT")) and k not in env]:
                saved_env[k] = os.environ.pop(k)
        for k in PER_CALL_ENV:   # the caller's value, or unset when the caller has none
            saved_env[k] = os.environ.get(k)
            if k in env:
                os.environ[k] = env[k]
            else:
                os.environ.pop(k, None)
        out, err = io.StringIO(), io.StringIO()
        rc = 0
        old_argv = sys.argv
        sys.argv = [os.path.join(D, "brain.py")] + list(argv)
        t0 = time.time()
        # 7 Nov 2026 (an agent): the call's CPU beside the wall time, so the call log can tell a loaded box
        # (wall >> cpu) from slower code (cpu up). The served median moved 0.75-6.5 s by the hour on unchanged code.
        c0 = time.process_time()   # whole process: calls hold one lock, so this is the call plus ONNX worker threads
        sr = sys.modules.get("spread_recall")   # 12 Nov 2026 (an agent): per-arm times for the call row
        try:
            sr.ARM_MS.clear()
        except Exception:
            pass
        try:
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                try:
                    self.g["main"]()
                except SystemExit as e:
                    rc = e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
        except Exception as e:
            rc = 1
            err.write("brain_recall_server: %s: %s\n" % (type(e).__name__, e))
        finally:
            sys.argv = old_argv
            for k, v in saved_env.items():
                if v is None:
                    os.environ.pop(k, None)
                else:
                    os.environ[k] = v
            try:
                os.chdir(D)
            except OSError:
                pass
        self.calls += 1
        arms = None
        try:
            sr = sys.modules.get("spread_recall")
            arms = {k: {"ms": round(v[0], 1), "n": v[1], "path": dict(v[2])} for k, v in sr.ARM_MS.items()} or None
        except Exception:
            pass
        return {"arms": arms, "rc": rc, "out": out.getvalue(), "err": err.getvalue(), "ms": int((time.time() - t0) * 1000),
                "cpu_ms": int((time.process_time() - c0) * 1000), "dropped": dropped, "calls": self.calls,
                "miss_s": {k: round(v, 2) for k, v in self.miss.items() if v >= 0.05}}


def raise_priority():
    # 8 Nov 2026 (an agent, brain loop tick 57): every hook that recalls waits on this server, and under a
    # saturated box (100 pct of 16 cores, ~26 sessions at Normal) a Normal server waited ~2.6 s of each ~5.6 s call
    # for a core. At AboveNormal the wait went to ~0 (2.2 s a call); back at Normal after a restart it returned (6.7 s).
    # A server uses about a tenth of one core, so the cost to everything else is small. BRS_PRIORITY=normal turns it off.
    if os.name != "nt" or os.environ.get("BRS_PRIORITY", "above").lower() == "normal":
        return
    try:
        import ctypes
        k = ctypes.windll.kernel32
        k.GetCurrentProcess.restype = ctypes.c_void_p
        ok = k.SetPriorityClass(ctypes.c_void_p(k.GetCurrentProcess()), 0x00008000)  # ABOVE_NORMAL_PRIORITY_CLASS
        log("priority AboveNormal: %s" % bool(ok))
    except Exception as e:
        log("priority raise failed: %s: %s" % (type(e).__name__, e))


def main():
    os.makedirs(STATE_DIR, exist_ok=True)
    raise_priority()
    t0 = time.time()
    brain = Brain()
    base_env = brain_env(os.environ)
    lock = threading.Lock()
    token = secrets.token_hex(16)
    last = {"t": time.time()}
    cur = {"t0": None}   # when the call now holding the lock took it
    orphaned = {"s": None}
    stop = threading.Event()

    class Handler(socketserver.StreamRequestHandler):
        def handle(self):
            t_in = time.time()   # 8 Nov 2026 (an agent): lock wait goes in the call row as wait_ms
            try:
                req = json.loads(self.rfile.readline().decode("utf-8"))
            except Exception:
                return
            if req.get("token") != token:
                return
            reply = {"decline": None}
            if req.get("op") == "ping":
                reply = {"ok": True, "pid": os.getpid(), "calls": brain.calls}
            elif not lock.acquire(timeout=LOCK_WAIT):
                reply = {"decline": "busy"}
            else:
                cur["t0"] = time.time()
                try:
                    # code first (3 Nov 2026): with the env check ahead of it, a server whose callers were all declined
                    # on env never saw its own code change and kept running the old code.
                    changed = brain.code_changed()
                    if changed:
                        reply = {"decline": "code changed: " + os.path.basename(changed)}
                        log("code changed: %s" % changed)
                        stop.set()
                    elif brain_env(req.get("env") or {}) != base_env:
                        reply = {"decline": "brain env differs"}
                    else:
                        reply = brain.call(req.get("argv") or [], req.get("env") or {}, req.get("cwd") or D)
                        try:
                            brain.watch_new()
                        except Exception:
                            pass
                        # one row per call (3 Nov 2026): which groups dropped and what each miss cost in real use,
                        # so the next lever is picked from live calls, not forced drops. BRS_CALL_LOG=0 turns it off.
                        if os.environ.get("BRS_CALL_LOG", "1") != "0":
                            try:
                                with open(CALL_LOG, "a", encoding="utf-8") as fh:
                                    fh.write(json.dumps({"t": round(time.time(), 1), "gap_s": round(time.time() - last["t"], 1),
                                                         "op": (req.get("argv") or ["?"])[0], "ms": reply.get("ms"),
                                                         "wait_ms": int((cur["t0"] - t_in) * 1000),
                                                         "cpu_ms": reply.get("cpu_ms"),
                                                         "sess": ((req.get("env") or {}).get("CLAUDE_CODE_SESSION_ID")
                                                                  or (req.get("env") or {}).get("CODEX_THREAD_ID") or "")[:8],
                                                         "dropped": reply.get("dropped"), "miss_s": reply.get("miss_s"),
                                                         "arms": reply.get("arms")}) + "\n")
                            except Exception:
                                pass
                        if rss_bytes() > RSS_CAP:
                            log("rss over cap after a call; exiting")
                            last["respawn"] = True
                            stop.set()
                finally:
                    cur["t0"] = None
                    last["t"] = time.time()
                    lock.release()
            try:
                self.wfile.write((json.dumps(reply) + "\n").encode("utf-8"))
            except Exception:
                pass

    class Server(socketserver.ThreadingTCPServer):
        daemon_threads = True
        allow_reuse_address = False

    srv = Server(("127.0.0.1", 0), Handler)
    port = srv.server_address[1]
    tmp = ENDPOINT + ".%d.tmp" % os.getpid()
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump({"port": port, "token": token, "pid": os.getpid(), "started": time.time(),
                   "load_s": round(time.time() - t0, 2)}, f)
    os.replace(tmp, ENDPOINT)
    log("serving pid %d port %d after %.1f s load" % (os.getpid(), port, time.time() - t0))
    th = threading.Thread(target=srv.serve_forever, daemon=True)
    th.start()
    # 8 Nov 2026 (an agent), ported from the Mac/framework copy (an agent, 6 Nov): every fresh server
    # warms itself with two recalls before its first caller. On this laptop over the 72 h to 8 Nov 00:0x the first call
    # a fresh server answered took p50 11.2 s / p90 22.6 s against 3.4 s / 7.8 s for later calls (62 first calls, 8 pct
    # of all served recall time; brainloop_c462/firstcall_1108.json). Warm-up calls go straight to brain.call, so they
    # write no calls.jsonl row; a caller arriving mid warm-up waits on the lock as usual. BRS_WARMUP=0 turns it off.
    if os.environ.get("BRS_WARMUP", "1") != "0":
        # 8 Nov 2026 (an agent): the lock is taken per warm call, not for both. The first live warm-up held it
        # 29.3 s (server.log 00:06:32), past LOCK_WAIT (20 s), so a caller arriving just after the load was declined
        # "busy" and ran cold; now a caller waits at most one warm call, and a caller already queued goes before the
        # second one (a warm call that cannot get the lock in 1 s is skipped - a real call is warming the server).
        def warm():
            tw = time.time(); done = 0
            for q in ("brain recall warm up of the lanes", "second warm call for the seed index"):
                if not lock.acquire(timeout=1):
                    break
                try:
                    brain.call(["recall", q], {"BRAIN_RECALL_LOG": "0", "BRAIN_RECALL_REFRESH": "0"}, D)
                    done += 1
                except Exception as e:
                    log("warm-up failed: %s: %s" % (type(e).__name__, e))
                    break
                finally:
                    lock.release()
            log("warm-up: %d recalls in %d ms" % (done, (time.time() - tw) * 1000))
        threading.Thread(target=warm, daemon=True).start()
    try:
        while not stop.wait(WATCH_S):
            if time.time() - last["t"] > IDLE_EXIT:
                log("idle exit")
                break
            if soft_cap_due(rss_bytes(), time.time() - last["t"], cur["t0"] is not None):
                log("rss %d MB over the soft cap after %.0f s idle; handing over to a successor"
                    % (rss_bytes() // 2 ** 20, time.time() - last["t"]))
                last["respawn"] = True
                break
            if cur["t0"] is None and time.time() - last["t"] >= SOFT_IDLE_S and lock.acquire(blocking=False):
                try:
                    changed = brain.code_changed()
                except Exception:
                    changed = None
                finally:
                    lock.release()
                if changed:
                    log("code changed: %s; handing over to a successor in a lull" % changed)
                    last["respawn"] = True
                    break
            # 13 Nov 2026 (an agent): the resident folder listing's 600 s safety listing (0.7 s on the loaded
            # laptop) is taken here in a lull, when it is due within two minutes, instead of inside the next caller's
            # recall. A caller that arrives meanwhile waits on the lock for the rest of it. BRS_IDLE_RELIST=0 off.
            # The same lull writes the superseded cache entries a recall left pending (brain._sup_flush_deferred: the
            # 65k-row listing's marshal, ~80 ms, moved off the call that follows another agent's write).
            if (cur["t0"] is None and time.time() - last["t"] >= IDLE_RELIST_GAP and lock.acquire(blocking=False)):
                try:
                    try:
                        fl = brain.g.get("_sup_flush_deferred")
                        if fl is not None:
                            fl()
                    except Exception as e:
                        log("superseded flush failed: %s: %s" % (type(e).__name__, e))
                    if os.environ.get("BRS_IDLE_RELIST", "1") != "0":
                        try:
                            fn = brain.g.get("_rl_idle_refresh")
                            t_r = time.time()
                            if fn is not None and fn():
                                log("idle re-list of the memory folder in %d ms" % ((time.time() - t_r) * 1000))
                        except Exception as e:
                            log("idle re-list failed: %s: %s" % (type(e).__name__, e))
                finally:
                    lock.release()
            t0c = cur["t0"]
            if ORPHAN_S > 0 and t0c is not None and time.time() - t0c > ORPHAN_S:
                orphaned["s"] = round(time.time() - t0c, 1)
                log("a call has held the lock %.0f s, past its client's read timeout; exiting" % orphaned["s"])
                try:
                    with open(CALL_LOG, "a", encoding="utf-8") as fh:
                        fh.write(json.dumps({"t": round(time.time(), 1), "op": "orphaned", "ms": int(orphaned["s"] * 1000),
                                             "aborted": True}) + "\n")
                except Exception:
                    pass
                break
    finally:
        try:
            with open(ENDPOINT, encoding="utf-8") as f:
                mine = json.load(f).get("pid") == os.getpid()
            if mine:  # replace only after the read handle is closed (Windows refuses otherwise)
                os.replace(ENDPOINT, ENDPOINT + ".stopped")
        except Exception:
            pass
        time.sleep(1)
        srv.shutdown()
        try:
            fl = brain.g.get("_sup_flush_deferred")
            if fl is not None and fl():
                log("wrote the pending superseded cache before stopping")
        except Exception as e:
            log("superseded flush failed: %s: %s" % (type(e).__name__, e))
        log("stopped pid %d after %d calls" % (os.getpid(), brain.calls))
        if last.get("respawn") and os.environ.get("BRS_RESPAWN", "1") != "0":
            try:
                p = start_successor(os.path.abspath(__file__))
                log("started successor pid %s" % (p.pid if p else None))
            except Exception as e:
                log("successor start failed: %s: %s" % (type(e).__name__, e))
        if orphaned["s"] is not None:
            # the orphaned call's thread is still running; leave without waiting on it, so the server lock
            # is free for the next server at once
            os._exit(0)


if __name__ == "__main__":
    if os.name == "posix":
        try:
            os.nice(10)   # background brain compute runs niced (compute doctrine)
        except OSError:
            pass
    lockf = None
    try:
        os.makedirs(STATE_DIR, exist_ok=True)
        lockf = open(os.path.join(STATE_DIR, "server.lock"), "a+b")
        try:
            import msvcrt

            def _try_lock():
                msvcrt.locking(lockf.fileno(), msvcrt.LK_NBLCK, 1)
        except ImportError:  # macOS / Linux (4 Nov 2026)
            import fcntl

            def _try_lock():
                fcntl.flock(lockf.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        for _ in range(40):  # a server that is stopping holds the lock for up to ~16 s
            try:
                _try_lock()
                break
            except OSError:
                time.sleep(1)
        else:
            sys.exit(0)  # another server is live
    except Exception:
        sys.exit(0)
    main()
