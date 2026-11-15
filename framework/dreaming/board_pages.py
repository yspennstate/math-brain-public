#!/usr/bin/env python3
"""board_pages.py - this computer's owner prompts and who is in charge of what, as two pages on brain-tasks-board.

Owner order, 1 Nov 2026 20:15 (laptop, T-20261101-026): "set up the task repo so that agents communicate through it
better, and so that any prompt I write ends up somewhere there and agents say what they are in charge of, that way
agents know what is going on, what I am interested in, what loop prompts I am writing and the overall system
operating ... they should also say which agent is working on which loop or prompt". Same evening, from the Mac
(a fleet message): "agents on one computer are not seeing what agents in other places are doing".

Two pages per computer, rewritten by `fleet_board.py sync-tasks` (task FleetBoardSyncTasks on the laptop):

  coordination/computers/<computer>/OWNER_PROMPTS.md
      LOOPS RUNNING: every loop he started that fired in the last 36 hours - the agent running it, his order's first
      words, cadence and end date as he gave them, last fire and fire count, the checklist entry.
      HIS ASKS: every other prompt of the last 72 hours, newest first - time, the agent that got it, the thread, the
      checklist entry with its status and the agent's own "working on" line, then the user's words (pasted text cut to a
      preview, every page through the secret scan before it leaves).
  coordination/computers/<computer>/AGENTS.md
      one block per agent active in the last 24 hours: what it is in charge of (its open checklist entries, the user's words
      and its working-on line, the newest dated note) and when it last moved.

Sources, read only: memory/prompts/owner_prompts_hourly.json (BrainOwnerPromptsHourly, his prompts with re-fires
folded) and the task checklist's state.json. Standard library only. `python board_pages.py --print` shows the two
pages without posting them.
"""
import calendar
import json
import os
import re
import sys
import time
from datetime import datetime, timedelta
import io
try:
    from shared_read import open_shared as _open_shared_ro
except Exception:
    def _open_shared_ro(path, binary=False):
        return io.open(path, "rb") if binary else io.open(path, encoding="utf-8")

HOME = os.path.expanduser("~")
# The project folder is the home path with separators as dashes: {{BRAIN_SLUG}} on the laptop, -Users-<name> on a Mac.
PROMPTS = os.path.join(HOME, ".claude", "projects", re.sub(r"[:\\/]", "-", HOME), "memory", "prompts",
                       "owner_prompts_hourly.json")
STATE = os.path.join(HOME, "brain-repo", "12_cognitive_architecture", "task_checklist", "state.json")
ASK_H, LOOP_H, AGENT_H = 72, 36, 24
WORDS, PASTE = 600, 160

LOOP_RE = re.compile(r"^\s*(/loop\b|loop tick\b|[\w-]+ loop tick\b|shorts tick\b|storage loop tick\b)", re.I)
EVERY_RE = re.compile(r"every\s+(\d+\s*(?:s|sec|seconds?|m|min|minutes?|h|hours?))", re.I)
UNTIL_RE = re.compile(r"until\s+([0-9]{1,2}\s+[A-Z][a-z]{2}\s+[0-9:x]{4,5}|[A-Z][a-z]{2}\s+[0-9]{1,2}[^;,)]{0,12})")
FOR_RE = re.compile(r"for\s+(?:the\s+)?next\s+(\d+\s*(?:minutes?|hours?|days?|h|d))", re.I)
ORDER_RE = re.compile(r"\(his\s+([^;)]{4,40}?)\s+order", re.I)


def _load(path):
    try:
        with _open_shared_ro(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def _ts(s):
    # Fast path for the three accepted shapes (9 Nov: strptime and its lazy import cost 17-22 s a run at BelowNormal);
    # anything else takes the original strptime loop, so what parses and what does not is unchanged.
    s19 = (s or "")[:19]
    if (len(s19) == 16 and s19[10] in "T " or len(s19) == 19 and s19[10] == "T" and s19[16] == ":") \
            and s19[4] == s19[7] == "-" and s19[13] == ":":
        try:
            return datetime.fromisoformat(s19)
        except ValueError:
            pass
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M"):
        try:
            return datetime.strptime((s or "")[:19], fmt)
        except ValueError:
            pass
    return None


def _clean(text, limit=WORDS):
    """the user's words for the page: pasted blocks cut to a preview, whitespace folded, cut at `limit`."""
    t = text or ""
    t = re.sub(r"<pasted_content[^>]*>(.*?)</pasted_content[^>]*>",
               lambda m: "[pasted %d chars: %s ...]" % (len(m.group(1)), " ".join(m.group(1).split())[:PASTE]),
               t, flags=re.S)
    t = " ".join(t.split())
    return t if len(t) <= limit else t[:limit].rsplit(" ", 1)[0] + " ..."


def _entries():
    st = _load(STATE) or {}
    ents = st.get("entries") or {}
    return ents if isinstance(ents, dict) else {}


def _by_session(ents):
    out = {}
    for eid, e in ents.items():
        s = (e.get("session") or "")[:8]
        if s:
            out.setdefault(s, []).append(e)
    for v in out.values():
        v.sort(key=lambda e: e.get("asked_at") or "")
    return out


def _entry_for(by_sess, session, ts):
    """The checklist entry this prompt landed in: the session's newest entry asked at or before the prompt."""
    best = None
    for e in by_sess.get((session or "")[:8], []):
        a = _ts(e.get("asked_at"))
        if a and ts and a <= ts + timedelta(minutes=2):
            best = e
    return best


def _agent(p, e):
    if e and e.get("agent"):
        return e["agent"]
    rt = p.get("runtime") or "claude"
    return "%s-%s" % (rt, (p.get("session") or "?")[:8])


PLACEHOLDER = re.compile(r"kept registered by the live inbox hook|^session\b", re.I)


def _working(e):
    """The agent's own line; when it is only the mesh's placeholder, its newest dated note instead."""
    w = " ".join((e.get("working_on") or "").split())
    if not w or PLACEHOLDER.search(w):
        ups = e.get("updates") or []
        notes = [u for u in ups if u.get("note") and not str(u.get("note")).startswith("asked again")]
        w = ("(newest note %s) %s" % (notes[-1].get("at"), " ".join(str(notes[-1]["note"]).split()))) if notes else ""
    return w


def _entry_line(e):
    if not e:
        return "not on the checklist"
    w = _working(e)
    s = "%s %s" % (e.get("id"), e.get("status"))
    if w:
        s += " - working on: " + (w[:220] + " ..." if len(w) > 220 else w)
    r = " ".join(str(e.get("result") or "").split())
    if e.get("status") == "done" and r:
        # the ask and what came of it on one row (owner 1 Nov 20:15: "the information and data obtained from all the
        # prompts should be going online and used by agents")
        s += " - RESULT %s: %s" % (e.get("done_at") or "", r[:300] + " ..." if len(r) > 300 else r)
    return s


def _loop_key(text):
    """One loop = one order: the order's own clock time if it names one, else its first 80 characters."""
    m = ORDER_RE.search(text or "")
    return (m.group(1).lower() if m else "") or " ".join((text or "").split())[:80].lower()


def owner_prompts_page(computer, now=None):
    now = now or datetime.now()
    d = _load(PROMPTS) or {}
    prompts = d.get("prompts") or []
    by_sess = _by_session(_entries())
    loops, asks = {}, []
    for p in prompts:
        first, last = _ts(p.get("ts")), _ts(p.get("last_ts") or p.get("ts"))
        if not first:
            continue
        text = p.get("text") or ""
        if LOOP_RE.search(text):
            if last and now - last <= timedelta(hours=LOOP_H):
                k = (p.get("session"), _loop_key(text))
                cur = loops.get(k)
                if not cur or (last or first) > cur["last"]:
                    loops[k] = {"p": p, "first": first, "last": last or first,
                                "fires": (cur["fires"] if cur else 0) + 1 + int(p.get("refires") or 0)}
                else:
                    cur["fires"] += 1 + int(p.get("refires") or 0)
        elif now - first <= timedelta(hours=ASK_H):
            asks.append(p)
    lines = ["# Owner prompts on %s" % computer, "",
             "Written by `board_pages.py` (run by `fleet_board.py sync-tasks`) at %s from this computer's prompt "
             "ledger and task checklist. Generated; do not edit by hand. His later words win over an earlier task. "
             "Who is in charge of what: AGENTS.md beside this file." % time.strftime("%Y-%m-%d %H:%M %z"), "",
             "## Loops running (fired in the last %d hours): %d" % (LOOP_H, len(loops)), ""]
    for (sess, _), L in sorted(loops.items(), key=lambda kv: kv[1]["last"], reverse=True):
        p, text = L["p"], L["p"].get("text") or ""
        e = _entry_for(by_sess, sess, L["last"])
        ev = EVERY_RE.search(text)
        un = UNTIL_RE.search(text) or FOR_RE.search(text)
        lines.append("- **%s** - every %s, %s; last fired %s, %d fires seen" % (
            _agent(p, e), ev.group(1) if ev else "?", ("until " + un.group(1)) if un else "end not stated",
            L["last"].strftime("%d %b %H:%M"), L["fires"]))
        lines.append("  - checklist: " + _entry_line(e))
        lines.append("  - his order: " + _clean(text, 420))
    lines += ["", "## His asks, last %d hours: %d (newest first)" % (ASK_H, len(asks)), ""]
    for p in sorted(asks, key=lambda p: p.get("ts") or "", reverse=True):
        t = _ts(p.get("ts"))
        e = _entry_for(by_sess, p.get("session"), t)
        rf = int(p.get("refires") or 0)
        lines.append("- **%s** %s, thread *%s*%s" % (t.strftime("%d %b %H:%M"), _agent(p, e), p.get("topic") or "?",
                                                    (", re-sent %d times" % rf) if rf else ""))
        lines.append("  - checklist: " + _entry_line(e))
        lines.append("  - the user's words: " + _clean(p.get("text")))
    if not prompts:
        lines.append("(the prompt ledger %s could not be read)" % PROMPTS)
    return "\n".join(lines) + "\n"


_ARTIFACT = re.compile(r"(/|\\)[\w.-]+\.\w{1,5}\b|\b[\w-]+\.(md|py|txt|json|jsonl|mp4|png|csv|tex|pdf|html|sh)\b"
                       r"|\b[0-9a-f]{8,40}\b|https?://")
_NEXTSTEP = re.compile(r"\bnext\b|\bwatch for\b", re.I)
BLOCKED_SHOWN = 20


def agents_page(computer, now=None):
    now = now or datetime.now()
    ents = _entries()
    agents = {}
    for eid, e in ents.items():
        if e.get("status") not in ("open", "working", "blocked"):
            continue
        la = _ts(e.get("last_activity") or e.get("asked_at"))
        if not la or now - la > timedelta(hours=AGENT_H):
            continue
        agents.setdefault(e.get("agent") or "unknown", []).append((la, e))
    lines = ["# Agents on %s and what each is in charge of" % computer, "",
             "Written by `board_pages.py` at %s from this computer's task checklist: every agent with an open entry "
             "that moved in the last %d hours. An agent says what it is doing with `task_checklist_hook.py working "
             "<id> \"...\"` and `note <id> \"...\"`; that is the line shown here. His prompts and loops: "
             "OWNER_PROMPTS.md beside this file." % (time.strftime("%Y-%m-%d %H:%M %z"), AGENT_H), "",
             "%d agents, %d open entries." % (len(agents), sum(len(v) for v in agents.values())), ""]
    for ag, items in sorted(agents.items(), key=lambda kv: max(x[0] for x in kv[1]), reverse=True):
        items.sort(key=lambda x: x[0], reverse=True)
        lines.append("## %s (last moved %s)" % (ag, items[0][0].strftime("%d %b %H:%M")))
        for la, e in items[:8]:
            w = _working(e) or "(has not said)"
            lines.append("- %s %s, asked %s: %s" % (e.get("id"), e.get("status"), e.get("asked_at"),
                                                  _clean(e.get("asked_words"), 200)))
            lines.append("  - in charge of: " + (w[:300] + " ..." if len(w) > 300 else w))
            ups = e.get("updates") or []
            if ups:
                u = ups[-1]
                lines.append("  - newest note (%s): %s" % (u.get("at"), _clean(u.get("note"), 300)))
                # TOP10 rank 2 asks for each agent's last artifact and next checkpoint; the newest note names an
                # artifact for 11 of 39 entries here and a next step for 2, any note for 32 and 25 (6 Nov 21:0x)
                for label, rx in (("last artifact", _ARTIFACT), ("next step", _NEXTSTEP)):
                    if not rx.search(str(u.get("note") or "")):
                        hit = next((x for x in reversed(ups[:-1]) if rx.search(str(x.get("note") or ""))), None)
                        if hit:
                            lines.append("  - %s (%s): %s" % (label, hit.get("at"), _clean(hit.get("note"), 200)))
        if len(items) > 8:
            lines.append("- and %d more open entries" % (len(items) - 8))
        lines.append("")
    # A blocked entry does not move, so the 24-hour window above never shows one, and OPEN_TASKS.md shows its status
    # word but not why. 6 Nov 21:1x: 66 blocked here, every one with a 'blocked: <why>' note, none of the reasons on
    # the board. List them here with the reason, newest first.
    blk = []
    for eid, e in ents.items():
        if e.get("status") != "blocked":
            continue
        why = next((u for u in reversed(e.get("updates") or []) if str(u.get("note") or "").startswith("blocked:")), None)
        blk.append((_ts(e.get("last_activity") or e.get("asked_at")) or datetime.min, e, why))
    if blk:
        blk.sort(key=lambda x: x[0], reverse=True)
        lines += ["## Blocked, with the reason (%d)" % len(blk), ""]
        for la, e, why in blk[:BLOCKED_SHOWN]:
            lines.append("- %s %s, asked %s: %s" % (e.get("id"), e.get("agent") or "unknown", e.get("asked_at"),
                                                   _clean(e.get("asked_words"), 120)))
            lines.append("  - %s" % (("blocked %s: %s" % (why.get("at"), _clean(str(why.get("note"))[8:].strip(), 240)))
                                     if why else "no reason recorded"))
        if len(blk) > BLOCKED_SHOWN:
            lines.append("- and %d older blocked entries (OPEN_TASKS.md lists them)" % (len(blk) - BLOCKED_SHOWN))
        lines.append("")
    return "\n".join(lines) + "\n"


MEMDIR = os.path.dirname(os.path.dirname(PROMPTS))
LEDGER = os.path.join(HOME, "brain-repo", "12_cognitive_architecture", "brain_improvement",
                      "IMPROVEMENT_LEDGER.jsonl")
# the laptop and yitz8 write arrivals here; the Mac's online_memory_pull.py writes the same {"name": ...} lines to the
# second path, and reading only the first listed the Mac's imports as its own results
ARRIVALS = (os.path.join(HOME, ".claude", "online_pull", "arrivals.jsonl"),
            os.path.join(HOME, ".claude", "dreaming", "online_memory_pull.jsonl"))
RESULT_H, INDEX_LINES, MAX_MEM, MAX_LEDGER = 48, 700, 150, 40
INDEX_RE = re.compile(r"^- \[[^\]]*\]\(([^)]+\.md)\)")


def _front(path):
    """description, status and created_at from a memory's frontmatter (the first 3 KB only)."""
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            head = f.read(3072)
    except OSError:
        return None
    if not head.startswith("---"):
        return None
    fm = head.split("\n---", 1)[0]
    out = {}
    for key in ("description", "status", "created_at", "created"):
        m = re.search(r"^\s*%s:\s*(.+)$" % key, fm, re.M)
        if m:
            out[key] = m.group(1).strip().strip('"')
    return out


_ARRIVED_RE = re.compile(r'\{"name": "([^"\\]*)"[,}]')


def _arrived():
    """Names of memories that came in from the other computers (online_memory_pull.py), so they are not shown as ours."""
    names = set()
    for path in ARRIVALS:
        try:
            with open(path, encoding="utf-8") as f:
                for line in f:
                    m = _ARRIVED_RE.match(line)   # the writer puts "name" first; 6k json.loads cost ~10 s starved
                    if m:
                        names.add(m.group(1))
                        continue
                    try:
                        names.add(json.loads(line).get("name"))
                    except ValueError:
                        pass
        except OSError:
            pass
    return names


# results_page cost 51-112 s at the task's BelowNormal priority on 9 Nov (an agent): 53 s handing Python all
# 59k names of the memory folder, 35 s opening 384 memory heads on a contended disk, 17 s in strptime. The listing
# now asks Windows for "*_<day>.md" (the filesystem filters, FindFirstFileEx returns each match's write time), and
# the parsed frontmatter is kept in a cache keyed by name + write time, so a run opens only new or changed memories.
FRONT_CACHE = os.path.join(HOME, ".claude", "fleet_board", "results_front_cache.json")


def _dated_names(days):
    """{name: write_time} for MEMDIR files ending in one of `days`; None when the filtered listing is unavailable."""
    if os.name != "nt":
        return None
    try:
        import ctypes
        from ctypes import wintypes
        k32 = ctypes.WinDLL("kernel32", use_last_error=True)
        k32.FindFirstFileExW.restype = wintypes.HANDLE
        k32.FindFirstFileExW.argtypes = [wintypes.LPCWSTR, ctypes.c_int, ctypes.POINTER(wintypes.WIN32_FIND_DATAW),
                                         ctypes.c_int, ctypes.c_void_p, wintypes.DWORD]
        k32.FindNextFileW.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.WIN32_FIND_DATAW)]
        k32.FindClose.argtypes = [wintypes.HANDLE]
        bad = wintypes.HANDLE(-1).value
        out = {}
        for day in days:
            fd = wintypes.WIN32_FIND_DATAW()
            h = k32.FindFirstFileExW(os.path.join(MEMDIR, "*" + day), 1, ctypes.byref(fd), 0, None, 2)
            if h == bad:
                if ctypes.get_last_error() == 2:   # ERROR_FILE_NOT_FOUND: no memory for that day
                    continue
                return None
            try:
                while True:
                    if fd.cFileName.endswith(day):   # the 8.3 alias can match a pattern the long name does not
                        out[fd.cFileName] = (fd.ftLastWriteTime.dwHighDateTime << 32) | fd.ftLastWriteTime.dwLowDateTime
                    if not k32.FindNextFileW(h, ctypes.byref(fd)):
                        break
            finally:
                k32.FindClose(h)
        return out
    except Exception:
        return None


def _load_front_cache():
    try:
        with open(FRONT_CACHE, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _save_front_cache(cache):
    try:
        tmp = FRONT_CACHE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(cache, f)
        os.replace(tmp, FRONT_CACHE)
    except OSError:
        pass


def results_page(computer, now=None):
    """What this computer found in the last 48 hours: the memories filed here (status, the hook line) and the brain
    improvement ledger rows written here. Owner order 1 Nov 20:15 (T-20261101-026): "brain results, tests results,
    and so on should end up in the online brain and obtained for all agents faster, that way agents know what is
    cutting edge and what we are doing". Reads the newest lines of MEMORY.md and the files they name; it never lists
    the memory folder (43k files)."""
    now = now or datetime.now()
    cut = now - timedelta(hours=RESULT_H)
    came_in = _arrived()
    mems = []
    try:
        with open(os.path.join(MEMDIR, "MEMORY.md"), encoding="utf-8", errors="replace") as f:
            index = [next(f, "") for _ in range(INDEX_LINES)]
    except OSError:
        index = []
    # MEMORY.md keeps only the newest ~90 entries, so the names with a date suffix inside the window come from one
    # flat listing of the folder (names only, no stat), the undated ones from the index
    days = {(now - timedelta(days=k)).strftime("_%Y_%m_%d.md") for k in range(RESULT_H // 24 + 2)}
    cands = [m.group(1) for m in (INDEX_RE.match(l) for l in index) if m]
    stamps = _dated_names(sorted(days))
    if stamps is None:
        stamps = {}
        try:
            with os.scandir(MEMDIR) as it:
                cands += [e.name for e in it if e.name[-14:] in days]
        except OSError:
            pass
    else:
        cands += sorted(stamps)
    cache, fresh = _load_front_cache(), {}
    seen = set()
    for name in cands:
        if name in seen or name in came_in or name == "MEMORY.md":
            continue
        seen.add(name)
        key = stamps.get(name, int(time.time() // 21600))   # undated index names: re-read every 6 hours
        hit = cache.get(name)
        if hit and hit[0] == key:
            ts, fm = hit[1], hit[2]
        else:
            fm = _front(os.path.join(MEMDIR, name))
            if not fm:
                continue
            t = _ts((fm.get("created_at") or "").replace("+", " ").split(" ")[0]) or _ts(fm.get("created"))
            ts = t.timestamp() if t else None
        fresh[name] = [key, ts, fm]
        if not ts:
            continue
        t = datetime.fromtimestamp(ts)
        if t < cut:
            continue
        mems.append((t, name[:-3], (fm.get("status") or "?").lower(), fm.get("description") or ""))
    _save_front_cache(fresh)
    mems.sort(key=lambda x: x[0], reverse=True)
    total = len(mems)
    mems = mems[:MAX_MEM]
    rows = []
    try:
        with open(LEDGER, "rb") as f:
            f.seek(0, 2)
            size = f.tell()
            f.seek(max(0, size - 3000000))
            tail = f.read().decode("utf-8", errors="replace").splitlines()[(1 if size > 3000000 else 0):]
        for line in tail:
            try:
                r = json.loads(line)
            except ValueError:
                continue
            t = _ts(str(r.get("ts") or ""))
            if t and t >= cut:
                rows.append((t, r))
    except OSError:
        pass
    rows.sort(key=lambda x: x[0], reverse=True)
    counts = {}
    for _, _, st, _ in mems:
        counts[st] = counts.get(st, 0) + 1
    lines = ["# Results found on %s, last %d hours" % (computer, RESULT_H), "",
             "Written by `board_pages.py` (run by `fleet_board.py sync-tasks`) at %s. The memories filed on this "
             "computer (newest first, memories that came in from other computers left out) and the rows its agents "
             "wrote to brain_improvement/IMPROVEMENT_LEDGER.jsonl. Full text of a memory: brain-repo "
             "01_ai_consciousness/claude/memory/<name>.md on GitHub; it reaches local recall on the other computers "
             "through their hourly pull. A provisional result is a lead, not a verdict: check it before you build on "
             "it. Generated; do not edit by hand." % time.strftime("%Y-%m-%d %H:%M %z"), "",
             "## Memories filed here: %d%s (%s)" % (total, (", newest %d shown" % MAX_MEM) if total > MAX_MEM else "",
                                                   ", ".join("%d %s" % (n, s) for s, n in
                                                             sorted(counts.items(), key=lambda kv: -kv[1]))), ""]
    for t, name, st, desc in mems:
        d = _clean(re.sub(r"^\[[A-Z]+\]\s*", "", desc), 300)
        lines.append("- %s **%s** `%s` - %s" % (t.strftime("%d %b %H:%M"), st, name, d))
    lines += ["", "## Brain improvement ledger, rows dated in the window (this computer's copy): %d%s" % (
        len(rows), (" (newest %d shown)" % MAX_LEDGER) if len(rows) > MAX_LEDGER else ""), ""]
    for t, r in rows[:MAX_LEDGER]:
        lines.append("- %s %s, %s: `%s` - %s" % (t.strftime("%d %b %H:%M"), r.get("agent") or "?", r.get("area") or "?",
                                                r.get("id") or "?", _clean(str(r.get("change") or ""), 320)))
    return "\n".join(lines) + "\n"


UNANS_H, UNANS_SHOW = 48, 30
FB = None   # fleet_board sets this to itself before it builds the pages (its api, inbox and parser)


def _acks_by_oid(F, computer, want):
    """Acks by this computer for the messages in want, read by GraphQL. 9 Nov 2026 (an agent): the board tree
    is 17,745 entries and 17,437 of them are ack files, so the one recursive tree GET took 11-15 s of every run, and it
    needs the REST budget, which is spent most hours. One query lists the ~890 ack folders with their oids (3 s); only
    a wanted folder whose oid changed since the last run is read again (aliased chunks of 40, ~2.6 s each)."""
    o, n = F.BOARD.split("/")
    d = F.gql('query($o:String!,$n:String!){repository(owner:$o,name:$n){a: object(expression:"HEAD:coordination/acks")'
              '{... on Tree{entries{name oid}}}}}', {"o": o, "n": n}, 60)
    ents = (((d or {}).get("repository") or {}).get("a") or {}).get("entries")
    if not ents:
        raise IOError("ack folder list refused: %s" % ((F.GQL_ERR[0] or "no data")[:120],))
    oid = {e["name"]: e["oid"] for e in ents}
    cp = os.path.join(F.STATE, "acks_folder_cache.json")
    try:
        cache = json.load(open(cp, encoding="utf-8"))
    except Exception:
        cache = {}
    stale = [i for i in want if i in oid and (cache.get(i) or [None])[0] != oid[i]]
    for k in range(0, len(stale), 40):
        part = stale[k:k + 40]
        d = F.gql('query($o:String!,$n:String!){repository(owner:$o,name:$n){%s}}' % " ".join(
            'a%d: object(expression:"HEAD:coordination/acks/%s"){oid ... on Tree{entries{name}}}' % (j, i)
            for j, i in enumerate(part)), {"o": o, "n": n}, 60)
        if not d or not d.get("repository"):
            raise IOError("ack folders query refused: %s" % ((F.GQL_ERR[0] or "no data")[:120],))
        for j, i in enumerate(part):
            x = d["repository"].get("a%d" % j) or {}
            # keep the oid this read actually saw (HEAD may have moved since the list), so a change is never cached away
            cache[i] = [x.get("oid"), [f["name"] for f in (x.get("entries") or [])]]
    keep = {i: cache[i] for i in want if i in cache}
    try:
        tmp = cp + ".tmp"
        with io.open(tmp, "w", encoding="utf-8", newline="") as fh:
            json.dump(keep, fh)
        os.replace(tmp, cp)
    except OSError:
        pass
    print("unanswered: %d ack folders listed, %d wanted, %d read again" % (len(oid), len(want), len(stale)))
    acked = {}
    for i in want:
        for name in (keep.get(i) or [None, []])[1]:
            mm = re.match(r"([^/]+?)__", name)
            if mm and mm.group(1) == computer:
                acked[i] = acked.get(i, 0) + 1
    return acked


def unanswered_page(computer, now=None):
    """UNANSWERED.md: the fleet messages of the last 48 hours from the OTHER computers, each with what this computer
    did about it - a reply posted from here, an ack by an agent here, or nothing yet. TOP10 rank 2, 3 Nov 2026: this
    laptop was the slow answerer (first answer median 9-12 min against yitz8's 2 min, ROUNDTRIP.md) because its agents
    see the inbox only on a prompt; this page lets the sender see which requests are still waiting here, and lets an
    agent here pick one up. It records only what is on the board; it never answers for an agent."""
    F = FB
    if F is None:
        raise RuntimeError("unanswered_page needs fleet_board (built by fleet_board.py sync-tasks)")
    # a copy at most two minutes old will do for a 48-hour page: the sessions' inbox hook refreshes it all the time, and
    # a fresh read costs 5-9 s when the REST budget is spent (9 Nov). Older than that, this read refreshes it.
    msgs = F.parse(F.inbox_cached(max_age=120))
    if not msgs:
        raise RuntimeError("inbox unreadable")
    cut = time.time() - UNANS_H * 3600
    here = " on " + computer

    def ts(m):
        # the id is the sender's own clock; its header carries the offset (yitz8 -0500, the Mac +0400)
        i = re.match(r"FM-(\d{8})-(\d{6})", m["id"])
        o = re.search(r"([+-])(\d{2})(\d{2})\s*$", m.get("when") or "")
        if not (i and o):
            return F._ts(m["id"])
        off = (1 if o.group(1) == "+" else -1) * (int(o.group(2)) * 3600 + int(o.group(3)) * 60)
        return calendar.timegm(time.strptime(i.group(1) + i.group(2), "%Y%m%d%H%M%S")) - off

    def from_here(m):
        return m["sender"].endswith(here) or (here + " (") in m["sender"]
    acked, acks_known = {}, False
    try:
        acked, acks_known = _acks_by_oid(F, computer, [m["id"] for m in msgs if not from_here(m) and ts(m) >= cut]), True
    except Exception as e:
        print("unanswered: ack folders by oid failed (%r), reading the whole tree" % (e,))
    st, tree = (0, None) if acks_known else F.api("GET", "/repos/%s/git/trees/main?recursive=1" % F.BOARD, timeout=60)
    if st == 200 and isinstance(tree, dict) and "tree" in tree and not tree.get("truncated"):
        acks_known = True
        for e in tree["tree"]:
            mm = re.match(r"coordination/acks/(FM-[^/]+)/([^/]+?)__", e.get("path", ""))
            if mm and mm.group(2) == computer:
                acked[mm.group(1)] = acked.get(mm.group(1), 0) + 1
    if not acks_known:
        # 9 Nov (an agent): when REST is refused (the shared core budget drains most hours) the ack folders of
        # the messages this page shows are read by GraphQL in aliased chunks of 40, so the page is not "acks UNKNOWN".
        # Not first: with REST up the one tree call is faster (5 s against ~19 s for six chunks), and one nested
        # GraphQL query over all ~870 folders came back HTTP 502.
        try:
            o, n = F.BOARD.split("/")
            want = [m["id"] for m in msgs if not from_here(m) and ts(m) >= cut]
            got = {}
            for k in range(0, len(want), 40):
                part = want[k:k + 40]
                d = F.gql('query($o:String!,$n:String!){repository(owner:$o,name:$n){%s}}' % " ".join(
                    'a%d: object(expression:"HEAD:coordination/acks/%s"){... on Tree{entries{name}}}' % (j, i)
                    for j, i in enumerate(part)), {"o": o, "n": n}, 60)
                if not d or not d.get("repository"):
                    raise IOError("acks query failed")
                for j, i in enumerate(part):
                    got[i] = [f["name"] for f in ((d["repository"].get("a%d" % j) or {}).get("entries") or [])]
            for i, names in got.items():
                for name in names:
                    mm = re.match(r"([^/]+?)__", name)
                    if mm and mm.group(1) == computer:
                        acked[i] = acked.get(i, 0) + 1
            acks_known = True
        except Exception:
            acked, acks_known = {}, False
    replies = {}
    for m in msgs:
        if from_here(m):
            for s in re.findall(r"FM-\d{8}-\d{6}", m["text"]):
                replies.setdefault(s, m["id"])
    rows = []
    for m in msgs:
        t = ts(m)
        if t < cut or from_here(m):
            continue
        owner = m["sender"].startswith("from the author via")
        rep, a = replies.get(m["id"][:18]), acked.get(m["id"], 0)
        only = re.match(r"\s*FOR\s+([A-Za-z0-9_.-]+)\s+ONLY\b", m["text"], re.I)
        if only and only.group(1).lower() != computer.lower():
            status, rank = "addressed to %s, not this computer" % only.group(1), 3
        elif rep:
            status, rank = "replied here: %s" % rep, 2
        elif a:
            status, rank = "acked by %d agent%s here, no reply posted" % (a, "" if a == 1 else "s"), 1
        else:
            status, rank = ("nothing yet" if acks_known else "no reply here; acks UNKNOWN"), 0
        rows.append((rank, not owner, -t, m, status, owner))
    rows.sort(key=lambda r: r[:3])
    nowt = time.time()
    waiting = sum(1 for r in rows if r[0] == 0)
    lines = ["# Fleet messages from other computers: what %s did about each, last %d hours" % (computer, UNANS_H), "",
             "Written by `board_pages.py` (run by `fleet_board.py sync-tasks`) at %s from FLEET_INBOX.md and "
             "coordination/acks/. A reply is a message posted from this computer that names the message's id; an ack "
             "is `fleet_board.py ack`. Not every note needs a reply: a note that only reports wants an ack. This page "
             "never answers for an agent. Generated; do not edit by hand." % time.strftime("%Y-%m-%d %H:%M %z"), "",
             "%d messages, %d with nothing from this computer yet%s." % (
                 len(rows), waiting, "" if acks_known else " (the ack listing could not be read, so acks are UNKNOWN)"),
             "", "| message | age | from | status | start |", "|---|---|---|---|---|"]
    shown = [r for r in rows if r[0] == 0] + sorted((r for r in rows if r[0] > 0), key=lambda r: r[2])[:UNANS_SHOW]
    if len(shown) < len(rows):
        lines[-4] += " Every message with nothing yet is listed; of the rest, the newest %d." % UNANS_SHOW
    for rank, _, _, m, status, owner in shown:
        who = re.sub(r"^from (the author via )?", "", m["sender"]).split(" (")[0]
        lines.append("| %s | %.1f h | %s%s | %s | %s |" % (
            m["id"], (nowt - ts(m)) / 3600.0, "owner-headed, via " if owner else "", who, status,
            _clean(m["text"], 140).replace("|", "/")))
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    c = sys.argv[2] if len(sys.argv) > 2 else "this-computer"
    if "--print" in sys.argv:
        sys.stdout.reconfigure(encoding="utf-8")
        print(owner_prompts_page(c))
        print(agents_page(c))
        print(results_page(c))
    if "--results" in sys.argv:
        sys.stdout.reconfigure(encoding="utf-8")
        print(results_page(c))
