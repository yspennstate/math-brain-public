"""core_steer.py - put the agents' work on the cores Windows leaves idle.

MEASURED 2026-09-15 15:1x-15:4x on one laptop (Core Ultra 9 285H, 16 logical: P-cores 0,1,10-13; E-cores 2-9; LP-E 14,15):
since the 09-13 21:43 boot the scheduler places EVERY free thread on E-cores 4-9 only - renders, hooks, Claude sessions,
the author's apps - while the six P-cores and E-cores 2,3 sit at 0 pct with the CPU-set flags Allocated|RealTime. A thread
pinned to core 0 runs (52 Miter/s vs 33 shared on the E-cores, 6 when they are saturated), so the cores are usable; the
scheduler just never chooses them, and HIGH priority does not change that. The hybrid policy (powercfg 7f2f5cfa) was 0,
restored to the default 4 - no effect without a reboot at least. Root cause still open (see the memory).

What this does, every INTERVAL seconds, windowless, as the author's user:
  - if E-cores 4-9 are busy (avg over the window > BUSY_PCT) and the agent cores are mostly idle, set the affinity of
    every process in AGENT_NAMES that still has the default all-cores mask to AGENT_CORES (6 P + E 2,3; the parked LP-E
    14,15 are left out - they measured 3.5x slower). Children inherit, so one claude.exe pin carries its hooks.
  - the author's shells (powershell under WindowsTerminal), explorer, dwm, Chrome, VS Code, VLC are never touched.
  - STOP file (beside this script: core_steer.STOP) -> restore every pinned process to all cores and exit.
  - log: ~/.claude/compute/core_steer.log ; state: core_steer_state.json (pids pinned, last decision)
Reversible at any time: create the STOP file, or run  python core_steer.py --restore
"""
import ctypes, ctypes.wintypes as wt, json, os, sys, time

STATE_DIR = r"~\.claude\compute"
LOG = os.path.join(STATE_DIR, "core_steer.log")
STATE = os.path.join(STATE_DIR, "core_steer_state.json")
STOP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "core_steer.STOP")
# FIVE SECONDS, NOT TWENTY (2026-09-16). A render is born carrying its launcher's affinity - an agent shell is
# on INTERACTIVE_MASK - so it spends its first seconds on the author's own cores. A shorter sweep shortens that
# window, and one sweep costs 0.12 s wall on 538 processes (snapshot 0.067, classify 0.052 warm; command lines
# are cached per pid, so the cost does not grow with the rate) - about 2 pct of one core at 5 s, and the daemon
# measured 0.000 cores in practice. HONEST NOTE: this interval was changed to fix a measured 0.75-core leak of
# render work onto his cores, and it DID NOT fix it - the leak went 13 pct to 16 pct across the change, because
# the cause was an encoder that could not be reclassified at any sweep rate (see RENDER_NAMES below). The
# shorter interval is kept because it is nearly free and does narrow the inheritance window for renders that
# ARE correctable; it is not the reason the leak closed.
INTERVAL = 5
BUSY_PCT = 70          # E-cores 4-9 average over the window: above this, move agent work off them
AGENT_IDLE_PCT = 60    # agent cores average below this = they have room to take it. Was 40, and at 16:51 on 2026-09-15
                       # the daemon sat still with the E-cores at 100 pct and the agent cores at 42 - a gap worth acting
                       # on that the tighter bar refused. The E-core condition (>70) is what makes this an imbalance
                       # rather than a busy box; the agent bar only has to leave real headroom.
# THERE IS NO AUTOMATIC RELEASE, and the reason is measured, not assumed.
# The first version released when "the E-cores are quiet while the agent cores carry the load". That is not the
# imbalance reversing - it is THIS DAEMON WORKING. Pinning moves the agents off the E-cores, so the E-cores go quiet
# by construction, and the rule then undid its own fix. Watched live 2026-09-15 18:11-18:13: pin 117 processes ->
# P-cores 100 pct and E-cores 15-26 pct, twelve cores working; ninety seconds later the release fired and the box
# went straight back to six E-cores at 100 pct with ten cores idle. A release rule whose trigger is the success
# state is a flap generator.
# And the deeper reason: while the scheduler refuses to place on 0-3 and 10-13, restoring "all 16 cores" does not
# give a process sixteen cores - it gives it the six E-cores. Releasing is strictly worse than holding, every time.
# The only ways out of a pin are deliberate: the STOP file, or core_steer.py --restore. Both restore by scanning.
RELEASE_SAMPLES = None
E_CORES = [4, 5, 6, 7, 8, 9]
# P-CORES ONLY. The first version used [0,1,2,3,10,11,12,13] and measured 2026-09-15 18:0x showed why that is wrong:
# with 152 processes on that mask, logical 2 and 3 - the two E-cores inside it - sat at 100 pct while the six P-cores
# idled at 12-17. Windows places background-classified threads on efficiency cores by preference, so ANY E-core left in
# the mask becomes the whole mask. Excluding 2 and 3 leaves the scheduler nowhere to fall back to.
AGENT_CORES = [10, 11, 12, 13]
# THREE POOLS, which is what his two orders together actually ask for.
#   2026-09-05: the Claude and Codex interfaces always have capacity, so he can always type to them.
#   2026-09-15: that guarantee costs TWO cores, not eight - he shrank the reserved set to 0 and 1.
# So the interfaces themselves are the only things allowed onto the reserved pair, and they also get the released
# performance cores. Ordinary agent work gets the released performance cores only. Cores 2 and 3 stay OUT of both
# agent pools on purpose: they are efficiency cores, and Windows piles background threads onto any efficiency core
# inside a mask - measured 18:0x with 152 processes on 0-3,10-13, logical 2 and 3 at 100 pct, the P-cores at 12-17.
OWNER_RESERVED = [0, 1]          # the pair he chose on 2026-09-15; the bridge retires once the kernel reserves only these
INTERACTIVE_NAMES = {"claude.exe", "codex.exe", "windowsterminal.exe"}
INTERACTIVE_CORES = [0, 1, 10, 11, 12, 13]
# TWO POOLS, because one pool wasted two cores and oversubscribed the other. Measured 18:14-18:18 with agents alone on
# the P-cores: P held at 100 pct while the E-cores ran 21-66 pct and logical 2 and 3 sat at 0-2 - idle in both pools,
# since nothing pins them and the scheduler will not place there on its own. So heavy batch work (encoders, renderers,
# LaTeX) gets its own mask of 2,3 plus the E-cores: eight cores instead of the six it had, and it stops competing with
# the interactive agent traffic for the fast cores. Everything else stays on the P-cores.
BATCH_CORES = [2, 3, 4, 5, 6, 7, 8, 9]
BATCH_NAMES = {"ffmpeg.exe", "ffprobe.exe", "manim.exe", "blender.exe", "pdflatex.exe", "latex.exe", "dvisvgm.exe",
               "xdvipdfmx.exe", "mscorsvw.exe", "ngen.exe"}
# HIS OWN APPLICATIONS, added 2026-09-15 20:5x. Until this, the bridge freed the agents and left his browser, his
# editor and his shell on the six cores the scheduler is willing to use, because only a process with an EXPLICIT
# affinity can touch a reserved core. So the machine he actually touches was still running on six of sixteen. These
# get the whole usable machine - every core except the two parked low-power ones - which is what removing the
# reservation will give them anyway once he restarts. It is the closest thing to the real fix that does not need a reboot.
OWNER_APP_NAMES = {"chrome.exe", "msedge.exe", "msedgewebview2.exe", "explorer.exe", "dwm.exe", "code.exe",
                   "acrobat.exe", "acrocef.exe", "vlc.exe", "chatgpt classic.exe", "searchhost.exe",
                   "startmenuexperiencehost.exe", "microsoft.media.player.exe", "shellexperiencehost.exe",
                   "textinputhost.exe", "applicationframehost.exe", "lockapp.exe", "sihost.exe"}
OWNER_APP_CORES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
ALL_MASK = (1 << 16) - 1
AGENT_MASK = sum(1 << c for c in AGENT_CORES)
BATCH_MASK = sum(1 << c for c in BATCH_CORES)
INTERACTIVE_MASK = sum(1 << c for c in INTERACTIVE_CORES)
OWNER_APP_MASK = sum(1 << c for c in OWNER_APP_CORES)
AGENT_NAMES = {"claude.exe", "codex.exe", "node.exe", "ffmpeg.exe", "ffprobe.exe", "python.exe", "pythonw.exe", "git.exe",
               "git-remote-https.exe", "bash.exe", "sh.exe", "pdflatex.exe", "latex.exe", "dvisvgm.exe", "blender.exe",
               "manim.exe", "powershell.exe", "pwsh.exe", "cmd.exe", "rclone.exe", "ssh.exe", "scp.exe", "wscript.exe",
               # the console hosts of all of the above: 47 of them were sitting on the default mask, and a console
               # host that cannot keep up with its child is felt as a slow terminal even when the work is elsewhere
               "conhost.exe", "openconsole.exe",
               # the Git Bash toolset every agent pipeline runs through. A grep over a large tree was measured at
               # 0.97 cores while confined to the six cores the scheduler would use - the single busiest thing the
               # bridge was still leaving behind.
               "grep.exe", "sed.exe", "awk.exe", "gawk.exe", "find.exe", "sort.exe", "uniq.exe", "head.exe",
               "tail.exe", "wc.exe", "cut.exe", "tr.exe", "xargs.exe", "cat.exe", "ls.exe", "cp.exe", "mv.exe",
               "tar.exe", "gzip.exe", "zstd.exe", "diff.exe", "cmp.exe", "md5sum.exe", "sha256sum.exe"}
OWNER_SHELL_PARENTS = {"windowsterminal.exe", "explorer.exe"}   # a powershell/cmd under these is HIS shell

try:
    import psutil
except Exception:
    psutil = None

k = ctypes.windll.kernel32


def log(s):
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "  " + s + "\n")
    except Exception:
        pass


def snapshot():
    class PE32(ctypes.Structure):
        _fields_ = [("dwSize", wt.DWORD), ("cntUsage", wt.DWORD), ("th32ProcessID", wt.DWORD),
                    ("th32DefaultHeapID", ctypes.POINTER(ctypes.c_ulong)), ("th32ModuleID", wt.DWORD),
                    ("cntThreads", wt.DWORD), ("th32ParentProcessID", wt.DWORD), ("pcPriClassBase", ctypes.c_long),
                    ("dwFlags", wt.DWORD), ("szExeFile", ctypes.c_wchar * 260)]
    snap = k.CreateToolhelp32Snapshot(0x2, 0)
    rows = []
    if snap == wt.HANDLE(-1).value:
        return rows
    pe = PE32(); pe.dwSize = ctypes.sizeof(PE32)
    if k.Process32FirstW(snap, ctypes.byref(pe)):
        while True:
            rows.append((pe.th32ProcessID, pe.th32ParentProcessID, pe.szExeFile.lower()))
            if not k.Process32NextW(snap, ctypes.byref(pe)):
                break
    k.CloseHandle(snap)
    return rows


def live_reserved_cores():
    """Which logical processors the RUNNING kernel is holding out of the default scheduler, read from
    GetSystemCpuSetInformation (flag bit 1 = Allocated). The registry value only takes effect at a restart, so this
    is the only honest answer to 'is the reservation still eight cores or has he rebooted into two?'."""
    n = wt.ULONG(0)
    k.GetSystemCpuSetInformation(None, 0, ctypes.byref(n), None, 0)
    buf = ctypes.create_string_buffer(n.value)
    k.GetSystemCpuSetInformation(buf, n.value, ctypes.byref(n), None, 0)
    off, out = 0, []
    while off < n.value:
        size = ctypes.c_ulong.from_buffer(buf, off).value
        if ctypes.c_int.from_buffer(buf, off + 4).value == 0:
            lp = ctypes.c_ubyte.from_buffer(buf, off + 14).value
            flags = ctypes.c_ubyte.from_buffer(buf, off + 19).value
            if flags & 0x2:
                out.append(lp)
        off += size
    return sorted(out)


def obsolete():
    """This daemon exists only to bridge the gap between his 2026-09-15 decision (reserve two cores) and the restart
    that makes it real. Once the running kernel reserves at most the pair he chose, the default scheduler can reach
    every other core by itself and pinning would CONFINE agents rather than free them. So the bridge retires."""
    try:
        res = live_reserved_cores()
    except Exception:
        return False, None
    return (set(res) <= set(OWNER_RESERVED)), res


def get_mask(pid):
    h = k.OpenProcess(0x0400, False, pid)          # PROCESS_QUERY_INFORMATION
    if not h:
        return None
    pm, sm = ctypes.c_ulonglong(), ctypes.c_ulonglong()
    ok = k.GetProcessAffinityMask(h, ctypes.byref(pm), ctypes.byref(sm)); k.CloseHandle(h)
    return pm.value if ok else None


def set_mask(pid, mask):
    h = k.OpenProcess(0x0200 | 0x0400, False, pid)  # SET_INFORMATION | QUERY_INFORMATION
    if not h:
        return False
    ok = k.SetProcessAffinityMask(h, ctypes.c_ulonglong(mask)); k.CloseHandle(h)
    return bool(ok)


def per_core(window):
    if psutil is None:
        return None
    return psutil.cpu_percent(interval=window, percpu=True)


def load_state():
    try:
        return json.load(open(STATE, encoding="utf-8"))
    except Exception:
        return {"pinned": {}}


def save_state(st):
    try:
        tmp = STATE + ".tmp"
        json.dump(st, open(tmp, "w", encoding="utf-8"), indent=1); os.replace(tmp, STATE)
    except Exception:
        pass


# A RENDER IS BATCH WORK EVEN WHEN IT WEARS PYTHON'S NAME.
#
# BATCH_NAMES lists manim.exe, but manim is launched as "python.exe -m manim", and the Toolhelp snapshot this
# daemon walks carries the executable name and no command line. So every manim render fell through to the
# python.exe entry in AGENT_NAMES, or - far more often - was never classified at all and simply INHERITED the
# mask of the shell that launched it. Measured 2026-09-16 02:2x: 29 live renders, not one of them in this
# daemon's records, all sitting on [0,1,10,11,12,13] - the author's own two cores plus the agent pool. One of
# them read 32 pct CPU there and 123 pct on the batch pool: the same work, four times the processor, and his
# typing was competing with all 29.
#
# So python-named processes get their command line read once and cached. psutil is optional: without it this
# feature is simply off and the daemon behaves as it did before.
_RENDER_CACHE = {}
_RENDER_HINTS = ("manim", "ffmpeg", "blender", "-m manim")


# An encoder needs no command line to identify it - the executable name IS the classification. Until 2026-09-16
# only python-named processes were considered here, so a bare ffmpeg.exe was never a render: it fell through to
# the wide BATCH_MASK, whose reserved half the scheduler ignores, and - worse - an ffmpeg born holding its
# launcher's INTERACTIVE mask could not be corrected off it at all, because `correctable` let a batch-bound
# process leave AGENT_MASK and not INTERACTIVE_MASK. Measured 04:5x: one ffmpeg at 3.15 cores sitting on the
# cores he types on, and shortening the sweep from 20 s to 5 s did not shift it, because the sweep was never
# the reason. Naming them here puts encoders in the same balanced pools as the renders they belong to.
RENDER_NAMES = ("ffmpeg.exe", "ffprobe.exe", "blender.exe", "manim.exe")


def render_pids(rows):
    """pids of processes that are really renders. Reads a command line once per pid, never per sweep."""
    try:
        import psutil
    except Exception:
        psutil = None          # 11 Nov: this used to return set(), and then not even a bare ffmpeg.exe was a render
    live = set()
    for pid, _ppid, name in rows:
        if name in RENDER_NAMES:
            live.add(pid)
            _RENDER_CACHE[pid] = True
            continue
        if not name.startswith("python"):
            continue
        if psutil is None:
            if pid in _RENDER_CACHE:
                live.add(pid)  # keep what an earlier sweep read; an unread python is left unclassified, not cached
            continue
        live.add(pid)
        if pid in _RENDER_CACHE:
            continue
        try:
            cl = " ".join(psutil.Process(pid).cmdline()).lower()
            _RENDER_CACHE[pid] = any(h in cl for h in _RENDER_HINTS)
        except Exception:
            _RENDER_CACHE[pid] = False
    for pid in [k for k in _RENDER_CACHE if k not in live]:
        del _RENDER_CACHE[pid]
    return {pid for pid, is_render in _RENDER_CACHE.items() if is_render}


# WHY THE BATCH POOL IS SPLIT, and it is not tidiness.
#
# Cores 2 and 3 are inside the kernel's reserved set. A thread with an explicit affinity CAN run there - measured
# 2026-09-16, one pinned process per core returned 199 pct across the two, a full core each - but when the mask
# ALSO offers unreserved cores the scheduler takes those every time. So with the whole pool [2..9] in one mask,
# cores 4-9 ran at 100 pct while 2 and 3 sat at zero: eight cores wide, six cores deep, a quarter of the pool
# idle while renders queued.
#
# Giving a deterministic slice of the renders a mask of [2,3] ALONE leaves them nowhere else to go, and the two
# cores fill. The split is by pid so a process keeps the same pool across sweeps and nothing thrashes. All of
# this is scaffolding for the reservation itself: at the next restart cores 2 and 3 stop being reserved, the
# scheduler stops avoiding them, and RESERVED_ONLY should go back to being the whole pool.
RESERVED_ONLY = [2, 3]
UNRESERVED_BATCH = [4, 5, 6, 7, 8, 9]
# THE TWO CORES NOTHING WAS ALLOWED TO USE. Logical 14 and 15 are the low-power E-cores. They are NOT reserved, so
# the scheduler may place there freely - and it never does, because every mask this daemon sets stops at 13 and
# OWNER_APP_CORES ends at 13 too. Measured 2026-09-16 04:3x, one pinned process per core: every core on the box
# carried load except these two, which sat at 0 and 1 pct. They are slow - 0.27x of logical 13 each, the worst
# silicon here - but a render given the pair ALONE gets 0.54 of a core to itself, and a render in the six-core
# pool was measuring 0.145, because nineteen of them were sharing cores that run 0.32-0.54x under that crowd.
# Slow and empty beats fast and queued. One render in eight comes here.
LPE_ONLY = [14, 15]
RESERVED_ONLY_MASK = sum(1 << c for c in RESERVED_ONLY)
UNRESERVED_BATCH_MASK = sum(1 << c for c in UNRESERVED_BATCH)
LPE_ONLY_MASK = sum(1 << c for c in LPE_ONLY)


RENDER_MASKS = (RESERVED_ONLY_MASK, UNRESERVED_BATCH_MASK, LPE_ONLY_MASK)

# After the restart the kernel reserves only his pair, so cores 2 and 3 stop needing their own pool - the
# scheduler can place there freely and they merge back into one batch pool. The low-power pair still needs
# an explicit mask, because being reachable has never been the same as being chosen.
POST_BRIDGE = [False]
POSTB_BATCH = [2, 3, 4, 5, 6, 7, 8, 9]
POSTB_BATCH_MASK = sum(1 << c for c in POSTB_BATCH)
POSTB_CAPACITY = ((POSTB_BATCH_MASK, 5.60), (LPE_ONLY_MASK, 0.54))   # 8 E-cores at the measured 0.70 each
RENDER_MASKS = RENDER_MASKS + (POSTB_BATCH_MASK,)   # so `correctable` can move a render INTO the post-bridge pool


def render_mask(pid):
    """One render in four is sent to the reserved cores alone, so they are used instead of merely permitted.

    The divisor is (pid // 4) and not pid: WINDOWS ALLOCATES EVERY PROCESS ID AS A MULTIPLE OF FOUR, so
    `pid % 4 == 0` is true for every process on the machine and the first version of this line sent all
    thirty renders to the same two cores. The control caught it before the daemon ever ran it.
    """
    bucket = (pid // 4) % 8
    if bucket in (0, 1):
        return RESERVED_ONLY_MASK       # cores 2,3   - reserved, empty, 1.36 cores of measured capacity
    if bucket == 2:
        return LPE_ONLY_MASK            # cores 14,15 - unreserved but in no other mask, 0.54 cores
    return UNRESERVED_BATCH_MASK        # cores 4-9   - the shared pool, 2.76 cores under today's crowd


# WHAT EACH POOL IS WORTH. Measured 2026-09-16 04:2x by pinning one process per core, NORMAL priority, median of
# three runs of the same loop, against logical 13: cores 2,3 = 0.63, 0.73; cores 4-9 = 0.32, 0.48, 0.54, 0.42,
# 0.47, 0.53; cores 14,15 = 0.27, 0.27.
#
# THE FIRST VERSION OF THIS LINE USED THOSE READINGS DIRECTLY AND THAT WAS WRONG. A burn pinned to an EMPTY core
# measures the core; a burn pinned to a core already carrying nineteen renders measures the CONTENTION. Cores 2
# and 3 were empty when sampled, so 0.63 and 0.73 are real capacity. Cores 4-9 were the crowded pool, so their
# 0.32-0.54 readings are not capacity at all - feeding them back in as capacity told the balancer the six-core
# pool was worth 2.76 when the same silicon idle is worth about 4.2, and it therefore sent a third too few
# chains there. Capacity has to be a property of the HARDWARE, or the allocator keeps whatever imbalance it
# started with and calls it a measurement. Taking the least-contended reading in each class as the class's
# capability: P about 1.00 (logical 13), E about 0.70 (logical 3 at 0.73, logical 2 at 0.63, both idle at the
# time), LP-E 0.27 (both idle). The pools below are those per-class figures times their core counts.
# MEASURED FROM LIVE RENDERS, 2026-09-16 09:2x, after two wrong guesses in opposite directions. Sampling the
# cpu actually delivered to real workers in each pool over four windows: reserved [2,3] gave 1.99, 1.99, 1.99
# cores - dead consistent, a full core each - and unreserved [4-9] gave 3.17, 2.56, 2.56, 2.97, median 2.77.
#
# WHY RESERVED BEATS SIX CORES WITH TWO. Cores 2 and 3 are inside the kernel's reserved set, so ONLY a process
# explicitly masked there can run on them: a render gets them to itself. Cores 4-9 are unreserved, so they are
# shared with his apps (OWNER_APP_MASK covers 0-13) and with every unmanaged process on the box - six cores that
# deliver 2.77 to renders, not the 4.2 the silicon could give in isolation.
#
# BOTH EARLIER NUMBERS WERE WRONG, and the second was my correction of the first. I began with 2.76 measured
# under load, then "fixed" it to 4.20 on the argument that contention is not capacity and a pool should be rated
# by its hardware. That reasoning holds for a pool a render OWNS and fails for one it merely shares: here the
# contention is permanent, so the contended figure was the truthful one and my correction moved it away from
# reality. Capacity for scheduling means what the pool will actually deliver, not what the silicon could.
# CORES 14 AND 15 READING 0 PCT IS NORMAL, AND IT IS NOT THE LP-E FIX FAILING. Measured 2026-09-16 by
# replaying assign_pools over a rising chain count: the least-loaded rule (chains+1)/capacity does not pick
# LP-E until the NINTH concurrent render chain, and at sixteen chains LP-E holds one of them. That is the
# rule behaving correctly - LP-E delivers 0.54 cores against 1.99 and 2.77, so a chain parked there runs
# about 3.4x slower and would become the straggler that sets the makespan; its 1-of-16 share tracks its
# 10 pct share of total capacity. With the four to seven render chains this box usually runs, 14 and 15
# SHOULD sit idle, and they take work on their own once the other pools are deep. Do not force work onto
# them, and do not read 0 pct here as the two-cores-in-no-mask problem of 2026-09-15 - that one was
# INVISIBILITY (no mask contained them at all), this is SCHEDULING. Count live render chains first.

POOL_CAPACITY = ((RESERVED_ONLY_MASK, 1.99), (UNRESERVED_BATCH_MASK, 2.77), (LPE_ONLY_MASK, 0.54))
ROOT_POOL = {}          # render chain root -> the pool it was given, for as long as that chain lives


def assign_pools(live_roots):
    """Give each render CHAIN the pool with the least work per core, and keep it there while it lives.

    WHY NOT THE PID BUCKET ABOVE. It splits renders 25/62.5/12.5 no matter how many there are, and those
    fractions were picked to match the pools' capacities - but a FIXED fraction is only right at one chain
    count. Measured live at 04:44: ten chains on the six-core pool, FOUR on the LP-E pair, none at all on
    cores 2 and 3. Four chains sharing 0.54 of a core while 1.36 cores sat idle is the whole failure - the
    batch finishes at max(chains / capacity), which was 7.41 against the 3.26 the same fourteen chains reach
    when they are shared out by capacity. Least-loaded is list scheduling, and it beat the fixed split on
    makespan at every count measured: 47 pct at three chains, 15-22 pct at ten to twenty, 10 pct at thirty.

    A CLAIM THAT DID NOT SURVIVE ITS OWN CONTROL, recorded so nobody re-derives it: the first version of this
    comment said pids are a sequential counter, so a burst gets consecutive buckets and cannot spread. The
    negative arm refuted it - fourteen consecutive pids wrap mod 8 and spread 4/9/1, perfectly evenly. The
    fixed split is wrong because it ignores N, not because pids are sequential.

    "A pool with no chains on it" is NOT the thing to minimise, and an earlier control that measured that had
    it backwards: with three renders on the box, putting one alone on the low-power pair makes that render
    finish last and the batch slower. An empty pool is correct until there are enough chains to earn it.

    Least-loaded by (chains + 1) / capacity is proportional-fair and STICKY: a chain keeps its pool until it
    exits, so nothing migrates sweep to sweep and an affinity set once is not thrashed. Ties fall back to the
    pid bucket, which keeps the choice deterministic for a given arrival order.
    """
    for root in [r for r in ROOT_POOL if r not in live_roots]:
        del ROOT_POOL[root]                       # a chain that exited frees its seat
    table = POSTB_CAPACITY if POST_BRIDGE[0] else POOL_CAPACITY
    counts = {mask: 0 for mask, _ in table}
    for mask in ROOT_POOL.values():
        counts[mask] = counts.get(mask, 0) + 1
    for root in sorted(r for r in live_roots if r not in ROOT_POOL):
        best = min((counts.get(mask, 0) + 1.0) / cap for mask, cap in table)
        tied = [mask for mask, cap in table
                if abs((counts.get(mask, 0) + 1.0) / cap - best) < 1e-9]
        pick = tied[0] if POST_BRIDGE[0] else (render_mask(root) if render_mask(root) in tied else tied[0])
        ROOT_POOL[root] = pick
        counts[pick] = counts.get(pick, 0) + 1
    return ROOT_POOL


def render_root(pid, parent, renders):
    """The oldest ancestor of this render that is itself a render - the pid the whole chain is bucketed on.

    WHY THE CHAIN AND NOT THE PROCESS. A venv `python.exe` is a shim that relaunches the base interpreter with
    the SAME command line, so every manim render on this box is a pair: a one-thread shim that burns nothing and
    a child that does the work. They have different pids, so bucketing each process on its own pid put the two
    halves of one render in DIFFERENT pools - measured 2026-09-16 04:4x, both processes sitting in the new LP-E
    pool were shims at 0.00 cores while their workers ran elsewhere, so the two cores the pool exists to fill
    stayed at 0 and 1 pct. Bucketing on the chain root puts shim and worker in one pool, which is also what the
    inheritance wants: a child takes its parent's affinity at creation, so the pin survives the relaunch.
    """
    seen = set()
    cur = pid
    while True:
        up = parent.get(cur)
        if up is None or up not in renders or up in seen:
            return cur
        seen.add(cur)                                   # a pid loop cannot happen, but a snapshot is not atomic
        cur = up


def is_correctable(m, want):
    """May a process on mask `m` be moved to `want`? Extracted so the selftest exercises THIS, not a copy.

    This clause has failed the same way twice, both times silently. When the batch pool was split, a render's
    target became a half-pool and every render that had inherited the agent mask was judged uncorrectable -
    23 unpooled, 8 mislabelled. When the LP-E pool was added, a render already in the unreserved half could not
    reach the newly-opened cores, so only processes launched afterwards would ever find them. The daemon logged
    healthy numbers through both. It lived inline in the sweep, where no test could see it; a copy of it in a
    test would have drifted from it exactly as the probe's pool list drifted from the daemon's.
    """
    # THE THIRD TIME, 2026-09-18. `m == ALL_MASK` is the 'nobody has touched this' test, and on this box an
    # untouched render is NOT on ALL_MASK: measured today, every one of 13 live manim renders sat on 0x3FFF
    # ([0..13], the most common mask on the machine - 209 processes) while ALL_MASK is 0xFFFF. So each render
    # had its pool computed correctly by render_mask and was then judged uncorrectable, and the daemon logged
    # 'pinned 1 new processes' every sweep while thirteen renders stayed on the author's cores 0 and 1.
    # THE MASK THEY SIT ON IS OWNER_APP_MASK (0x3FFF, the whole usable machine - his browser, editor and
    # shell). The list below allowed a render to be corrected out of AGENT, INTERACTIVE and BATCH but NOT
    # out of OWNER_APP, so a render that inherited his shell mask was stuck on his cores for ever - exactly
    # the symptom he reports: films render and the machine is unusable. Adding OWNER_APP_MASK to that list
    # is the whole fix, and it is narrow: want in RENDER_MASKS means the process was already classified as
    # a render, so his real apps are never candidates here.
    return (m == ALL_MASK
            or (want in RENDER_MASKS and m in RENDER_MASKS)
            or (want in RENDER_MASKS and m in (AGENT_MASK, INTERACTIVE_MASK, BATCH_MASK, OWNER_APP_MASK))
            or (want == BATCH_MASK and m == AGENT_MASK)
            or (want == OWNER_APP_MASK and m in MASKS_WE_SET))


def candidates(rows):
    names = {pid: name for pid, _, name in rows}
    parent = {pid: ppid for pid, ppid, _ in rows}
    renders = render_pids(rows)
    roots = {pid: render_root(pid, parent, renders) for pid in renders}
    assign_pools(set(roots.values()))
    out = []
    for pid, ppid, name in rows:
        if pid <= 4 or pid == os.getpid():
            continue
        if POST_BRIDGE[0] and pid not in renders:
            continue                       # his decision: once the reservation is gone the scheduler owns everything else
        if pid in renders:
            # a render, whatever the executable is called - the whole shim chain shares one pool, and the
            # pool is the emptiest one per core rather than whatever a pid counter happened to land on
            root = roots[pid]
            out.append((pid, name, ROOT_POOL.get(root) or render_mask(root)))
            continue
        if name in OWNER_APP_NAMES:
            out.append((pid, name, OWNER_APP_MASK))            # his browser, editor, shell: the whole usable machine
            continue
        if name in ("powershell.exe", "pwsh.exe", "cmd.exe") and names.get(ppid, "") in OWNER_SHELL_PARENTS:
            out.append((pid, name, OWNER_APP_MASK))            # a shell HE is typing in is his app, not a worker
            continue
        if name in INTERACTIVE_NAMES:
            out.append((pid, name, INTERACTIVE_MASK))
            continue          # checked BEFORE the agent gate: WindowsTerminal is interactive but not an AGENT_NAME,
                              # so the gate below silently skipped it and his own terminal stayed on six cores
        if name not in AGENT_NAMES:
            continue
        out.append((pid, name, INTERACTIVE_MASK if name in INTERACTIVE_NAMES else
                               BATCH_MASK if name in BATCH_NAMES else AGENT_MASK))
    return out


MASKS_WE_SET = set()          # every mask this daemon has ever applied, so an old generation's pins are still ours


def restore_all(st, why):
    """Restore by SCANNING every process for a mask we set, not by the tracked dict. The dict undercounts badly:
    children inherit their parent's affinity at creation and are never recorded, so on 2026-09-15 18:0x the daemon
    reported 0 pinned while 152 processes - including his film's ffmpeg workers - still carried the 8-core mask and
    could never be released. Tracked pids remain the fast path; the scan is what makes the release complete."""
    ours = {AGENT_MASK, BATCH_MASK, INTERACTIVE_MASK, OWNER_APP_MASK} | set(RENDER_MASKS) | MASKS_WE_SET | {sum(1 << c for c in [0, 1, 2, 3, 10, 11, 12, 13])}   # incl. the retired 8-core mask
    n = 0
    for pid, _, _ in snapshot():
        if pid <= 4:
            continue
        m = get_mask(pid)
        if m in ours and m != ALL_MASK and set_mask(pid, ALL_MASK):
            n += 1
    st["pinned"] = {}
    save_state(st)
    log("restored %d processes to all cores (%s)" % (n, why))
    return n


def uncovered_cores():
    """Cores this daemon never permits anything to run on - the bug class that cost two cores on 2026-09-16.

    Every mask here is an explicit list, and an explicit list is exactly the kind of thing a core falls out of
    silently: nothing reports it, because the logs only ever describe the pools that DO exist. The complement is
    the check - every core, minus the union of what we hand out. It is three lines and it would have caught
    logical 14 and 15, which were in no mask at all while the box ran fourteen cores flat and queued renders.
    """
    union = 0
    for mask in (AGENT_MASK, BATCH_MASK, INTERACTIVE_MASK, OWNER_APP_MASK) + tuple(RENDER_MASKS):
        union |= mask
    return [c for c in range(os.cpu_count() or 16) if not (union >> c) & 1]


def masked_now():
    """How many processes actually carry a mask we set - the honest count, including inherited children."""
    ours = {AGENT_MASK, BATCH_MASK, INTERACTIVE_MASK, OWNER_APP_MASK} | set(RENDER_MASKS) | MASKS_WE_SET | {sum(1 << c for c in [0, 1, 2, 3, 10, 11, 12, 13])}
    n = 0
    for pid, _, _ in snapshot():
        if pid > 4 and get_mask(pid) in ours:
            n += 1
    return n


SINGLE_MUTEX = [None]             # the handle, kept so the mutex lives exactly as long as this process


def single_instance():
    """True when this process is the only daemon; False when another one already holds the mutex.

    The daemon was started twice at each of three boots (18 Oct 00:56 and 00:58, 2 Nov 08:56 and 08:57, 10 Nov
    16:36 and 16:38): two launchers at logon, a minute or two apart, and nothing here to notice the first copy.
    Both copies then swept every process every five seconds for weeks (83 and 339 cpu-seconds by the evening of
    10 Nov) and wrote the same pins. A named mutex is released by the kernel when its holder dies, however it
    dies, so there is no stale lock file to clean. `--restore` is not guarded: it is a one-shot a person runs
    while the daemon is up. If the mutex cannot be created at all the daemon runs (a failed check must not
    leave the box with no daemon). CORE_STEER_MUTEX names another mutex for a test.
    Controls: brain_improvement/agent_run/core_steer_single/test_single.py."""
    name = os.environ.get("CORE_STEER_MUTEX") or "Local\\core_steer_daemon_single_instance"
    k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    k32.CreateMutexW.restype = wt.HANDLE
    k32.CreateMutexW.argtypes = [ctypes.c_void_p, wt.BOOL, wt.LPCWSTR]
    k32.CloseHandle.argtypes = [wt.HANDLE]
    h = k32.CreateMutexW(None, False, name)
    if not h:
        return True
    if ctypes.get_last_error() == 183:            # ERROR_ALREADY_EXISTS: someone else made it first
        k32.CloseHandle(h)
        return False
    SINGLE_MUTEX[0] = h
    return True


def main():
    st = load_state()
    if "--restore" in sys.argv:
        restore_all(st, "--restore"); return
    if not single_instance():
        log("exit pid %d: another core_steer.py already runs as the daemon (single-instance mutex held)" % os.getpid())
        return
    MASKS_WE_SET.update({AGENT_MASK, BATCH_MASK, INTERACTIVE_MASK, OWNER_APP_MASK} | set(RENDER_MASKS))
    unreachable = uncovered_cores()
    if unreachable:
        log("WARNING: cores %s appear in NO mask this daemon sets - nothing on this box can be scheduled there. "
            "That is how logical 14 and 15 sat idle until 2026-09-16; add them to a pool or say in a comment why "
            "they are deliberately excluded." % (unreachable,))
    log("start pid %d interval %ds agent cores %s (%d processes already carry one of our masks)"
        % (os.getpid(), INTERVAL, AGENT_CORES, masked_now()))
    while True:
        if os.path.exists(STOP):
            restore_all(st, "STOP file"); log("exit on STOP"); return
        done, res = obsolete()
        if done and not POST_BRIDGE[0]:
            # THE BRIDGE RETIRES. THE LOW-POWER CAPTURE DOES NOT. Restoring every pin is right for agents, his
            # apps and his terminals: once the kernel reserves only his pair, the scheduler reaches every other
            # core by itself and a mask would CONFINE them. But logical 14 and 15 are a different problem that
            # the restart does not touch. They were never reserved, and they still sat at 0-1 pct on 2026-09-16
            # while processes holding ALL SIXTEEN cores ran elsewhere - Windows places background threads on the
            # performance and efficiency cores and treats the low-power pair as a last resort it rarely reaches.
            # So the daemon drops to render-only pooling instead of exiting: two pools, [2..9] and [14,15],
            # shared out by measured capacity. Everything else is left to the scheduler, as his decision intends.
            n = restore_all(st, "the kernel now reserves only %s - the bridge is obsolete, dropping to "
                                "render-only pooling so the low-power pair keeps being used" % res)
            POST_BRIDGE[0] = True
            log("bridge retired: restored %s processes. Still pooling RENDERS ONLY across %s and %s; set the STOP "
                "file to end this too." % (n, POSTB_BATCH, LPE_ONLY))
            st["pinned"] = {}
            save_state(st)
        pc = per_core(3.0)
        if pc is None:
            time.sleep(INTERVAL); continue
        e_busy = sum(pc[c] for c in E_CORES) / len(E_CORES)
        a_busy = sum(pc[c] for c in AGENT_CORES) / len(AGENT_CORES)
        rows = snapshot()
        alive = {pid for pid, _, _ in rows}
        # forget pinned processes that died
        for pid_s in [p for p in st.get("pinned", {}) if int(p) not in alive]:
            st["pinned"].pop(pid_s, None)
        # PIN UNCONDITIONALLY WHILE THE RESERVATION IS LIVE. The old condition - act only when the E-cores are busy
        # AND the agent pool is idle - is another rule defeated by its own success: once the bridge works, the agent
        # pool runs at 100 pct, the condition fails, and NEW processes are never pooled. Measured 2026-09-15 21:2x:
        # 118 processes still on the default mask, including his own WindowsTerminal, confined by the kernel to six
        # cores while ten sat available. There is no load threshold worth waiting for here: the reserved cores are
        # unreachable to a default mask by construction, so a process on the default mask is always worse off.
        if True:
            n = 0
            POOL = {INTERACTIVE_MASK: "interactive", BATCH_MASK: "batch", OWNER_APP_MASK: "owner_app",
                    AGENT_MASK: "agent", RESERVED_ONLY_MASK: "batch_reserved",
                    UNRESERVED_BATCH_MASK: "batch_unreserved", LPE_ONLY_MASK: "batch_lpe"}
            for pid, name, want in candidates(rows):
                m = get_mask(pid)
                # an encoder that INHERITED the agent mask from its build script still belongs in the batch pool, and
                # one of his apps that inherited anything belongs on the whole machine, so a WRONG pool is corrected,
                # not only an unpinned process
                if m == want:
                    continue
                # A RENDER ALREADY ON THE LOW-POWER PAIR IS LEFT THERE (2026-09-26 02:1x, an agent).
                # Measured with cores 0-13 at 100 pct and 14-15 at 3-9 pct: two BelowNormal ffmpeg encoders on
                # POSTB_BATCH ran 0.08 cpu-s per second each; pinned to LPE_ONLY alone they ran 0.72 and 0.67, and
                # this sweep moved them back to the batch pool within five seconds. POSTB_CAPACITY's 5.60 assumes the
                # E-cores are free for renders; when the agents spill onto them they are not, and the parked pair is
                # used only by a process whose mask holds nothing else. So a render that is on LPE_ONLY - put there by
                # this daemon or by its own agent - stays; everything else is corrected as before.
                if m == LPE_ONLY_MASK:
                    continue
                # A RENDER IS CORRECTABLE OUT OF ANY POOL IT LANDED IN BY ACCIDENT.
                # This clause used to read `want == BATCH_MASK and m == AGENT_MASK`, which stopped firing the
                # moment the batch pool was split into a reserved and an unreserved half: a render's target is
                # now one of those two halves and never BATCH_MASK, so every render that had INHERITED the agent
                # or interactive mask from its build shell was judged uncorrectable and stayed there. Measured:
                # 23 renders with no record at all and 8 mislabelled, while the acceptance test asked simply
                # whether a NEWLY LAUNCHED render reaches the batch pool. It did not.
                # ... and the same clause failed the same way again when the LP-E pool was added on 2026-09-16:
                # a render already sitting in the unreserved half has m == UNRESERVED_BATCH_MASK, which is in
                # neither list above, so not one existing render could ever move to the newly-opened cores and
                # only processes launched afterwards would have found them. `m in RENDER_MASKS` is the general
                # form: a render may move between render pools. It cannot thrash - render_mask is a pure
                # function of the pid, so a process's target never changes and it converges in one sweep.
                correctable = is_correctable(m, want)
                if correctable and set_mask(pid, want):
                    st["pinned"][str(pid)] = {"name": name, "at": time.strftime("%H:%M:%S"),
                                              "pool": POOL.get(want, "agent")}
                    n += 1
            if n:
                log("E-cores %.0f pct, agent cores %.0f pct -> pinned %d new processes to P-cores (tracked %d, actual %d)"
                    % (e_busy, a_busy, n, len(st["pinned"]), masked_now()))
        st["last"] = {"at": time.strftime("%Y-%m-%d %H:%M:%S"), "e_busy": round(e_busy), "agent_busy": round(a_busy),
                      "pinned_tracked": len(st.get("pinned", {})), "pinned_actual": masked_now(),
                      "cores": AGENT_CORES}
        save_state(st)
        time.sleep(INTERVAL)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log("fatal: %r" % (e,))
        raise
