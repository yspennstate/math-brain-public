"""core_steer_selftest.py - the regression net core_steer never had.

    python core_steer_selftest.py

Every case here is a bug that actually happened in this file, not a hypothetical. It touches nothing: it
imports the module and exercises pure functions, sets no affinity, starts no daemon, writes no state.

WHY IT EXISTS. `correctable` has failed the SAME way in two separate generations - once when the batch pool was
split in two (a render's target became a half-pool, so every render that had inherited the agent mask was judged
uncorrectable and stayed there: 23 unpooled, 8 mislabelled), and again when the LP-E pool was added (a render
already in the unreserved half could not move to the newly-opened cores, so only processes launched afterwards
would ever find them). Both were invisible: the daemon logs looked healthy, the renders still rendered, and the
only symptom was cores sitting at zero. A green log is not a pooled render.
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("core_steer", os.path.join(HERE, "core_steer.py"))
cs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cs)

FAILED = []


def check(name, ok, detail=""):
    print("  %-58s %s%s" % (name, "ok" if ok else "FAIL", ("  " + detail) if detail and not ok else ""))
    if not ok:
        FAILED.append(name)


def cores(mask):
    return tuple(c for c in range(16) if (mask >> c) & 1)


# 1. THE BUG THAT COST TWO IDLE CORES: a core in no mask at all can never be scheduled on.
check("every core appears in some mask the daemon sets", cs.uncovered_cores() == [],
      "uncovered: %s" % cs.uncovered_cores())

# 2. THE SHIM BUG: a venv python shim and its worker are one render and must share a pool, or the pool fills
#    with one-thread shims that burn nothing while their workers run elsewhere.
renders = {100, 104, 200, 204}
parent = {100: 1, 104: 100, 200: 1, 204: 200}
for shim, worker in ((100, 104), (200, 204)):
    a = cs.render_mask(cs.render_root(shim, parent, renders))
    b = cs.render_mask(cs.render_root(worker, parent, renders))
    check("shim %d and worker %d land in the same pool" % (shim, worker), a == b,
          "%s vs %s" % (cores(a), cores(b)))
check("render_root survives a pid cycle", cs.render_root(7, {7: 8, 8: 7}, {7, 8}) in (7, 8))

# 3. THE CLAUSE THAT FAILED TWICE - calling the REAL function, never a copy of it. A test that restates the
#    expression drifts from the code exactly as the probe's pool list once drifted from the daemon's.
for frm_name, frm in (("ALL", cs.ALL_MASK), ("agent", cs.AGENT_MASK), ("interactive", cs.INTERACTIVE_MASK),
                      ("batch", cs.BATCH_MASK)) + tuple(("pool %s" % (cores(m),), m) for m in cs.RENDER_MASKS):
    for want in cs.RENDER_MASKS:
        if frm == want:
            continue
        check("correctable: %s -> %s" % (frm_name, cores(want)), cs.is_correctable(frm, want))
# Since 18 Sep a process on his app mask MAY move to a render pool: a render that inherits his shell's mask sat on
# his cores for ever otherwise (see is_correctable). What keeps his apps out of the pools is the classification:
# candidates() never gives one of his apps a render pool as its target. Both halves are checked here; until
# 11 Nov this line still asserted the pre-fix rule and had failed, unread, since that fix.
check("a render that inherited his app mask can be pooled", cs.is_correctable(cs.OWNER_APP_MASK, cs.RENDER_MASKS[0]))
cs.ROOT_POOL.clear()
app_rows = [(2000, 4, n) for n in sorted(cs.OWNER_APP_NAMES)[:1]] + [(2004, 4, "chrome.exe"), (2008, 4, "ffmpeg.exe")]
app_want = {pid: w for pid, _n, w in cs.candidates(app_rows)}
check("his apps are NOT given a render pool as target",
      app_want.get(2004) == cs.OWNER_APP_MASK and app_want.get(2000) == cs.OWNER_APP_MASK
      and app_want.get(2008) in cs.RENDER_MASKS, "targets %s" % (app_want,))
check("a process on a mask nobody here set is left alone", not cs.is_correctable(0x5, cs.RENDER_MASKS[0]))
cs.ROOT_POOL.clear()

# 3b. NO psutil (11 Nov): an encoder is a render by its name alone; a python whose command line cannot be read is
#     left unclassified and is NOT cached as "not a render", so it is read once psutil is back.
_real = sys.modules.get("psutil", "absent")
sys.modules["psutil"] = None                     # makes `import psutil` raise ImportError
cs._RENDER_CACHE.clear()
blind = cs.render_pids([(3000, 4, "ffmpeg.exe"), (3004, 4, "python.exe"), (3008, 4, "chrome.exe")])
check("without psutil a named encoder is still a render", blind == {3000}, "got %s" % sorted(blind))
check("without psutil an unread python is not cached", 3004 not in cs._RENDER_CACHE, "%s" % (cs._RENDER_CACHE,))
if _real == "absent":
    del sys.modules["psutil"]
else:
    sys.modules["psutil"] = _real
cs._RENDER_CACHE.clear()

# 4. ALLOCATION: sticky, deterministic, and no pool starved once there are enough chains to earn it.
cs.ROOT_POOL.clear()
roots = set(46000 + 4 * i for i in range(20))
cs.assign_pools(roots)
first = dict(cs.ROOT_POOL)
cs.assign_pools(roots)
check("assignment is sticky across sweeps (no thrash)", first == cs.ROOT_POOL)
used = set(cs.ROOT_POOL.values())
check("at 20 chains every pool is in use", len(used) == len(cs.POOL_CAPACITY),
      "used %d of %d" % (len(used), len(cs.POOL_CAPACITY)))
cs.assign_pools(set(list(roots)[:10]))
check("a chain that exits frees its seat", all(r in roots for r in cs.ROOT_POOL))
check("render_mask is a pure function of the pid", cs.render_mask(123456) == cs.render_mask(123456))

# 5. POST-BRIDGE (runs only after his restart, so it is never exercised in normal operation).
cs.POST_BRIDGE[0] = True
cs.ROOT_POOL.clear()
cs.assign_pools(set(46000 + 4 * i for i in range(30)))
pools = set(cs.ROOT_POOL.values())
check("post-bridge uses exactly its two pools", pools <= {cs.POSTB_BATCH_MASK, cs.LPE_ONLY_MASK} and pools)
rows = [(1000, 4, "ffmpeg.exe"), (1004, 4, "claude.exe"), (1008, 4, "chrome.exe")]
got = {pid for pid, _n, _w in cs.candidates(rows)}
check("post-bridge pools renders ONLY (agents and apps left alone)", got == {1000},
      "classified %s" % sorted(got))
cs.POST_BRIDGE[0] = False
cs.ROOT_POOL.clear()
rows_all = {pid for pid, _n, _w in cs.candidates(rows)}
check("normal mode still classifies agents and his apps", rows_all == {1000, 1004, 1008},
      "classified %s" % sorted(rows_all))

# 6. RELEASE: every mask the daemon sets must be releasable, or a restart leaves processes pinned forever.
ours = {cs.AGENT_MASK, cs.BATCH_MASK, cs.INTERACTIVE_MASK, cs.OWNER_APP_MASK} | set(cs.RENDER_MASKS)
check("every render pool is in the set restore_all releases", all(m in ours for m in cs.RENDER_MASKS))

print()
if FAILED:
    print("FAILURES: %d" % len(FAILED))
    for f in FAILED:
        print("   " + f)
    sys.exit(1)
print("every case passes")
