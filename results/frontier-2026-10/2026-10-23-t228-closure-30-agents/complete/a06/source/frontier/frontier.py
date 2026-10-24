# -*- coding: utf-8 -*-
"""frontier.py - the frontier layer for the famous-200 probability problems.

His order, 14 Oct 2026 23:25 (T-20261014-145): "build the part of the brain that does that, i don't want agents wasting
time resolving the same stuff, and then make sure that the codex agent and claude agent running on open problems push
forward like this, with the frontier framework". The five points it carries (the why_one_top200 page, same evening):
hunt rows whose frontier paper reduces the theorem to a finite or numerical condition; concentrate several workers on one
row under a lead who first writes where the known method breaks; score a row by whether the obstruction moved, not by
whether a constant improved; give solvers the frontier paper's method and failure point, not our history; check the
literature before anyone is put on a row.

Layout (this folder):
  rows/TNNN/DOSSIER.md      written by the row's lead before solvers start. Sections, each a '## ' heading:
                            STATEMENT, FRONTIER (the papers that hold the best known result, with locators),
                            ARCHITECTURE (how the frontier proof goes, step by step), FAILURE POINT (exactly where the
                            known method stops and why), SHAPE (is the open part a finite or numerical condition?),
                            OBSTRUCTION (one paragraph: what must change for the row to move), SETTLED (facts nobody
                            re-proves, each with its locator), TARGETS (what counts as moving the obstruction, in order)
  rows/TNNN/routes.jsonl    the route ledger: {"at","by","route","status": live|dead|done|settled,"why","evidence"}
  rows/TNNN/moves.jsonl     obstruction events: {"at","by","kind": moved|narrowed|special|bound|literature|none,
                            "claim","text"} - only "moved" and "narrowed" count as progress on the board
  rows/TNNN/lit.json        the literature check: {"at","by","queries":[...],"newest":[...],"verdict","note"}
  STAFF.json                which worker folders work which row, and who leads it
  SHAPE_SCAN.tsv            the perceptron-shape scan of every live row
  BOARD.md                  written by `board`

Workers never write here. A worker keeps ROUTES.jsonl in its own folder (same fields, plus "row"); `sync` harvests
every staffed folder's ROUTES.jsonl, CLAIMS.jsonl and AUDITS_FROM_REVIEWER.tsv into rows/TNNN/harvest.json.

Commands (python -X utf8 frontier.py ...):
  brief TNNN [--short]      the solver's brief: statement, frontier, architecture, failure point, obstruction, what is
                            settled, the dead routes and why they died, live routes and who holds them, how progress
                            is scored. Our own claim history appears only as settled facts and dead routes.
  check TNNN "idea"         before starting a route or a lemma: does it match a settled fact, a dead route, a live
                            route someone holds, or a claim already made? Exit 2 on a strong match to settled/dead,
                            1 on a live or claimed match, 0 when nothing close is known.
  route TNNN live|dead|done|settled "route" --why ... [--by ID] [--evidence PATH]
  move TNNN moved|narrowed|special|bound|literature|none "text" [--claim ID] [--by ID]
  lit TNNN --verdict open|narrowed|solved --newest "..." [--query "..."] [--note ...] [--by ID]
  sync                      harvest the staffed folders
  board                     rewrite BOARD.md
  gate TNNN                 exit 0 when the row may take solvers (dossier has FAILURE POINT and OBSTRUCTION, literature
                            checked within 7 days); exit 3 with the reasons otherwise
Standard library only.
"""
import argparse
import datetime as _dt
import glob
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
ROWS = os.path.join(ROOT, "rows")
STAFF = os.path.join(ROOT, "STAFF.json")
SCAN = os.path.join(ROOT, "SHAPE_SCAN.tsv")
BOARD = os.path.join(ROOT, "BOARD.md")
LIST = os.path.join(os.path.dirname(ROOT), "top200_probability_2026_10_14", "list.jsonl")
SECTIONS = ("STATEMENT", "FRONTIER", "ARCHITECTURE", "FAILURE POINT", "SHAPE", "OBSTRUCTION", "SETTLED", "TARGETS")
PROGRESS = ("moved", "narrowed")
# The deep-learning half of the list (T223-T422, list tag TOP200_DL, added 16 Oct on his 01:18/01:2x order) is audited
# row by row by a Codex auditor before anyone solves it; solvers go only on rows it passes with a DAYS shape.
DL_AUDITS = ["~/brain_workers/w687/AUDIT_w687.jsonl"]


def dl_audit(row):
    """The newest auditor record for a deep-learning row, or {}."""
    best = {}
    for f in DL_AUDITS:
        for r in jsonl(f):
            if str(r.get("id", "")).upper() == row and str(r.get("at", "")) >= str(best.get("at", "")):
                best = r
    return best


def is_dl(row, lr=None):
    lr = lr if lr is not None else list_rows().get(row, {})
    return lr.get("list") == "TOP200_DL"
STOP = set("""a an the of and or to in on for by with at from as is are be was were that this these those it its into
than then there their which who whom whose not no any all every each some such can may might must will would should
over under between we our one two three via using use used show prove proved proof claim lemma theorem case cases
new known open result results bound bounds holds hold if only when where also more most less least""".split())


def now():
    return _dt.datetime.now().astimezone().isoformat(timespec="seconds")


def read(p):
    try:
        with io.open(p, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def jsonl(p):
    out = []
    for line in read(p).splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except ValueError:
            pass
    return out


def append(p, rec):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def write(p, text):
    tmp = p + ".tmp"
    with io.open(tmp, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, p)


def rowdir(row):
    row = row.upper()
    if not re.fullmatch(r"T\d{3}", row):
        sys.exit("row must look like T067")
    return os.path.join(ROWS, row)


def staff():
    try:
        st = json.loads(read(STAFF) or "{}")
    except ValueError:
        return {}
    return {k: v for k, v in st.items() if re.fullmatch(r"T\d{3}", k)}   # "_retired" and other notes are not rows


def list_rows():
    return {r["problem_id"]: r for r in jsonl(LIST)}


def sections(text):
    """'## NAME' sections of a dossier, keyed by upper-case name."""
    out, cur = {}, None
    for line in text.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            cur = m.group(1).strip().upper()
            out[cur] = []
        elif cur:
            out[cur].append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}


def dossier(row):
    return sections(read(os.path.join(rowdir(row), "DOSSIER.md")))


def stem(w):
    """Crude suffix stem so 'networks' meets 'network' and 'pushing' meets 'push' (18 Oct: a NOT move went through on that)."""
    for suf in ("ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 3 and not (suf == "s" and w.endswith(("ss", "us", "is", "as"))):
            w = w[:-len(suf)]
            break
    return w[:-1] if len(w) > 3 and w.endswith("e") else w


def words(text):
    return {stem(w) for w in re.findall(r"[a-z0-9]+", (text or "").lower().replace("-", " "))
            if len(w) > 2 and w not in STOP}


def bullets(text):
    """A section's items (- / * / '1.' bullets) with their wrapped continuation lines joined; a blank line ends an item."""
    out, cont = [], False
    for line in (text or "").splitlines():
        t = line.strip()
        if not t:
            cont = False
            continue
        if t[0] in "-*" or re.match(r"\d+[.)]\s", t) or not cont:
            out.append(re.sub(r"^(?:[-*]|\d+[.)])\s*", "", t).strip())
        else:
            out[-1] += " " + t
        cont = True
    return [b for b in out if b]


def sim(a, b):
    """Overlap of content words, scaled by the shorter text so a short idea can match a long ledger line."""
    wa, wb = words(a), words(b)
    if not wa or not wb:
        return 0.0
    # floor of 6 (18 Oct): against a five-word line two shared words scored 0.40 and flagged 47 of 160 rows' own targets as settled
    return len(wa & wb) / float(max(min(len(wa), len(wb)), 6))


def routes(row):
    """The row's own ledger plus every staffed worker's ROUTES.jsonl, newest status per route text winning."""
    recs = jsonl(os.path.join(rowdir(row), "routes.jsonl"))
    h = read(os.path.join(rowdir(row), "harvest.json"))
    if h:
        try:
            recs += json.loads(h).get("routes", [])
        except ValueError:
            pass
    last = {}
    for r in recs:
        key = (r.get("route") or "").strip().lower()
        if key:
            last[key] = r
    return list(last.values())


def harvested_claims(row):
    h = read(os.path.join(rowdir(row), "harvest.json"))
    try:
        return json.loads(h).get("claims", []) if h else []
    except ValueError:
        return []


# ---------------------------------------------------------------------------------------------------------- brief
def cmd_brief(a):
    print(brief_text(a.row, a.short))


def brief_text(row, short=False):
    """The brief as one string (frontier_hook.py imports this)."""
    row = row.upper()
    d = dossier(row)
    lr = list_rows().get(row, {})
    out = ["FRONTIER BRIEF %s - %s" % (row, lr.get("title", "")), ""]
    if not d:
        out.append("No dossier yet: the row's lead has not written where the known method breaks. Do not start solving;"
                   " read the frontier papers named in the list row and write that first (frontier.py gate %s)." % row)
        out += ["", "LIST ROW (unchecked): " + lr.get("statement", ""), "WHERE IT STANDS: " + lr.get("where_it_stands", "")]
        if is_dl(row, lr):
            out += ["", dl_audit_text(row)]
        return "\n".join(out)
    # STATE (15 Oct): the lead's note of what is already done, read before anything else so nobody redoes it
    order = ("STATE", "STATEMENT", "FRONTIER", "ARCHITECTURE", "FAILURE POINT", "SHAPE", "OBSTRUCTION", "TARGETS", "SETTLED")
    if short:
        order = ("STATE", "FAILURE POINT", "OBSTRUCTION", "TARGETS")
    for k in order:
        if d.get(k):
            out += ["== " + k, d[k], ""]
    rs = routes(row)
    dead = [r for r in rs if r.get("status") in ("dead", "settled")]
    live = [r for r in rs if r.get("status") == "live"]
    if dead:
        out.append("== DO NOT REDO (settled facts and dead routes; each says why)")
        for r in sorted(dead, key=lambda r: r.get("at", ""))[-(12 if short else 60):]:
            out.append("- [%s] %s -- %s (%s%s)" % (r.get("status"), r.get("route"), r.get("why", ""), r.get("by", "?"),
                                                   ", " + r["evidence"] if r.get("evidence") else ""))
        out.append("")
    if live:
        out.append("== LIVE ROUTES (someone holds these; coordinate before overlapping)")
        for r in live:
            out.append("- %s (%s since %s)" % (r.get("route"), r.get("by", "?"), (r.get("at") or "")[:16]))
        out.append("")
    mv = jsonl(os.path.join(rowdir(row), "moves.jsonl"))
    prog = [m for m in mv if m.get("kind") in PROGRESS]
    out.append("== HOW THIS ROW IS SCORED")
    out.append("Progress is a move of the obstruction above. MOVED: a step of the frontier architecture now goes through "
               "where it failed. NARROWED: the statement itself is now proved on a whole new part of its range (a "
               "parameter interval, an infinite family), so the open part is strictly smaller. A sharper constant for "
               "an unknown quantity, one more isolated case, a certified numerical bound, or a counterexample to an "
               "auxiliary route is recorded but scores nothing - unless it is named in TARGETS.")
    out.append("Moves so far: %d (%s)." % (len(prog), "; ".join(m.get("text", "")[:80] for m in prog[-3:]) or "none"))
    out.append("Before you start any route: python -X utf8 %s check %s \"<the route in one sentence>\"" %
               (os.path.join(ROOT, "frontier.py").replace("\\", "/"), row))
    return "\n".join(out)


def dl_audit_text(row):
    au = dl_audit(row)
    if not au:
        return "AUDIT: not audited yet. Deep-learning rows take solvers only after the auditor passes them with a DAYS shape."
    return "\n".join(["AUDIT (%s): status %s; solver shape %s" % (str(au.get("at", ""))[:16] or "?", au.get("status", "?"),
                                                                   au.get("solver_shape", "?")),
                      "statement ok: " + str(au.get("statement_ok", "")),
                      "repair: " + str(au.get("replace_with", ""))])


# ---------------------------------------------------------------------------------------------------------- check
def cmd_check(a):
    row = a.row.upper()
    idea = a.idea
    hits = []
    for r in routes(row):
        s = sim(idea, (r.get("route") or "") + " " + (r.get("why") or ""))
        if s >= 0.34:
            hits.append((s, r.get("status", "?"), r.get("route"), r.get("why", ""), r.get("by", "?")))
    for line in bullets(dossier(row).get("SETTLED", "")):
        s = sim(idea, line)
        if s >= 0.34:
            hits.append((s, "settled", line, "dossier SETTLED", "lead"))
    for c in harvested_claims(row):
        s = sim(idea, c.get("statement", ""))
        if s >= 0.34:
            st = c.get("audit") or c.get("status") or "claimed"
            # a claim that a route cannot work is a dead route once a reviewer passed it
            tag = "dead" if c.get("kind") == "route-failure" and str(st).upper().startswith("PASS") else "claimed"
            hits.append((s, tag, c.get("statement", "")[:220], "%s v%s %s" % (c.get("id"), c.get("version"), st),
                         c.get("folder", "?")))
    hits.sort(key=lambda h: -h[0])
    if not hits:
        print("nothing close is known for %s: go ahead, and record the route (ROUTES.jsonl in your folder)." % row)
        sys.exit(0)
    worst = 0
    for s, st, route, why, by in hits[:8]:
        print("%.2f [%s] %s\n      why: %s  (%s)" % (s, st, route, why, by))
        if st in ("dead", "settled") and s >= 0.4:
            worst = 2
        elif worst < 1 and st in ("live", "claimed", "done") and s >= 0.4:
            worst = 1
    if worst == 2:
        print("STRONG MATCH to a settled fact or a dead route: do not redo it. Read the evidence; go on only with a "
              "concrete reason it differs, written into your ROUTES.jsonl line.")
    elif worst == 1:
        print("Someone holds or already claimed something close: read it and build on it rather than repeat it.")
    sys.exit(worst)


# ---------------------------------------------------------------------------------------------------------- writes
def cmd_route(a):
    rec = {"at": now(), "by": a.by, "route": a.route, "status": a.status, "why": a.why or "", "evidence": a.evidence or ""}
    append(os.path.join(rowdir(a.row), "routes.jsonl"), rec)
    print(json.dumps(rec, ensure_ascii=False))


def cmd_move(a):
    rec = {"at": now(), "by": a.by, "kind": a.kind, "claim": a.claim or "", "text": a.text}
    append(os.path.join(rowdir(a.row), "moves.jsonl"), rec)
    print(json.dumps(rec, ensure_ascii=False))


def cmd_lit(a):
    p = os.path.join(rowdir(a.row), "lit.json")
    rec = {"at": now(), "by": a.by, "verdict": a.verdict, "queries": a.query or [], "newest": a.newest or [],
           "note": a.note or ""}
    hist = []
    try:
        hist = json.loads(read(p) or "{}").get("history", [])
    except ValueError:
        pass
    hist.append(rec)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    write(p, json.dumps(dict(rec, history=hist), ensure_ascii=False, indent=1))
    print(json.dumps(rec, ensure_ascii=False))


# ---------------------------------------------------------------------------------------------------------- sync
KIND_RX = [("literature", re.compile(r"known literature|already (?:proved|settled)|not new|literature finding", re.I)),
           ("route-failure", re.compile(r"counterexample to (?:the|a|this) (?:route|approach)|obstruction|cannot|"
                                        r"no universal|barrier|fails", re.I)),
           ("bound", re.compile(r"(?:<=|>=|≤|≥|<|>)\s*-?\d+\.\d{2,}|upper bound|lower bound|certified (?:bound|value)|"
                                r"improv", re.I)),
           ("special", re.compile(r"for the law|special case|for (?:offspring|q\s*=|d\s*=|k\s*=)|on K_?\d|family", re.I))]


def kind_of(c):
    k = (c.get("kind") or "").strip().lower()
    if k:
        return k
    st = c.get("statement", "")
    for name, rx in KIND_RX:
        if rx.search(st):
            return name
    return "other"


def cmd_sync(a):
    st = staff()
    by_row = {}
    for row, info in st.items():
        for folder in info.get("folders", []):
            bucket = by_row.setdefault(row, {"routes": [], "claims": [], "at": now()})
            name = os.path.basename(folder.rstrip("/\\"))
            if re.fullmatch(r"T\d{3}", name):  # a worker moved to another row writes in wNNN/TNNN
                name = os.path.basename(os.path.dirname(folder.rstrip("/\\"))) + "/" + name
            for r in jsonl(os.path.join(folder, "ROUTES.jsonl")):
                if (r.get("row") or row).upper() == row:
                    r.setdefault("by", name)
                    bucket["routes"].append(r)
            audits = {}
            for line in read(os.path.join(folder, "AUDITS_FROM_REVIEWER.tsv")).splitlines():
                parts = line.split("\t")
                if len(parts) >= 3 and parts[0] != "claim_id":
                    audits[(parts[0].strip(), parts[1].strip().lstrip("v"))] = parts[2].strip()
            for c in jsonl(os.path.join(folder, "CLAIMS.jsonl")):
                cid, ver = str(c.get("id", "")), str(c.get("version", "")).lstrip("v")
                bucket["claims"].append({"id": cid, "version": ver, "folder": name,
                                         "statement": c.get("statement", ""), "status": c.get("status", ""),
                                         "audit": audits.get((cid, ver), ""), "kind": kind_of(c)})
    for row, b in by_row.items():
        os.makedirs(rowdir(row), exist_ok=True)
        # newest version of each claim only
        newest = {}
        for c in b["claims"]:
            key = (c["folder"], c["id"])
            try:
                v = int(c["version"] or 0)
            except ValueError:
                v = 0
            if key not in newest or v >= newest[key][0]:
                newest[key] = (v, c)
        b["claims"] = [c for _, c in newest.values()]
        write(os.path.join(rowdir(row), "harvest.json"), json.dumps(b, ensure_ascii=False, indent=1))
        print("%s: %d routes, %d claims from %d folders" % (row, len(b["routes"]), len(b["claims"]),
                                                             len(st[row].get("folders", []))))


# ---------------------------------------------------------------------------------------------------------- hunt
HUNT_GLOB = "~/math_frontier_hunt_1014/h*/HUNT.jsonl"
SCAN_HEAD = "id\tshape\twhy\tsolved_already\tconfidence\tsource"


def cmd_hunt(a):
    """Fold the read-only hunters' HUNT.jsonl lines into SHAPE_SCAN.tsv and rows/TNNN/hunt.json.
    A hunter line replaces a hand-written scan line for the same row; rows the hunters have not reached keep theirs."""
    scan = {}
    for line in read(SCAN).splitlines()[1:]:
        p = line.split("\t")
        if len(p) >= 3:
            scan[p[0]] = (p + ["", "", ""])[:6]
    n = 0
    flagged = []
    for f in sorted(glob.glob(a.glob)):
        src = os.path.basename(os.path.dirname(f))
        for h in jsonl(f):
            row = str(h.get("id", "")).upper()
            if not re.fullmatch(r"T\d{3}", row):
                continue
            why = (h.get("condition") or h.get("obstruction") or "").replace("\t", " ").replace("\n", " ")[:240]
            scan[row] = [row, h.get("shape", ""), why, str(h.get("solved_already", "")), str(h.get("confidence", "")),
                         src]
            os.makedirs(rowdir(row), exist_ok=True)
            write(os.path.join(rowdir(row), "hunt.json"), json.dumps(h, ensure_ascii=False, indent=1))
            n += 1
            if str(h.get("solved_already", "")).lower() == "yes":
                flagged.append("%s (%s): %s" % (row, src, (h.get("solved_evidence") or "")[:200]))
    body = [SCAN_HEAD] + ["\t".join(scan[k]) for k in sorted(scan)]
    write(SCAN, "\n".join(body) + "\n")
    print("hunt: %d hunter lines folded, %d rows in %s" % (n, len(scan), SCAN))
    for fl in flagged:
        print("SOLVED-CLAIM, check before anyone works it:", fl)


# ---------------------------------------------------------------------------------------------------------- board
def scan_rows():
    out = {}
    for line in read(SCAN).splitlines()[1:]:
        p = line.split("\t")
        if len(p) >= 3:
            out[p[0]] = {"shape": p[1], "why": p[2], "solved": (p + ["", "", ""])[3]}
    return out


POOL = "~/brain_workers/pool.log"
LAYER_START = _dt.datetime(2026, 10, 14, 23, 25)
STAGE_RE = re.compile(r"^(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d) (w\d+)( stage \d+ (started|ended|stopped)|: new task)")


def worker_hours(folders):
    """Approximate worker-hours on a row since it was staffed, from pool.log stage lines. A worker in a row
    subfolder (wNNN/TNNN) counts from its first brief change after the layer started; a worker whose whole folder is
    the row counts from the layer's start. Stages still running count to now; a worker born on the row (a "(brief)" first stage) counts from that stage. Workers outside the pool give None."""
    want = {}
    for f in folders:
        parts = f.rstrip("/\\").replace("\\", "/").split("/")
        for i, x in enumerate(parts):
            if re.fullmatch(r"w\d+", x):
                want[x] = i + 1 < len(parts) and bool(re.fullmatch(r"T\d{3}", parts[i + 1]))
    if not want:
        return None
    start = {w: (None if sub else LAYER_START) for w, sub in want.items()}
    open_at, total = {}, 0.0
    for line in read(POOL).splitlines():
        m = STAGE_RE.match(line)
        if not m or m.group(2) not in want:
            continue
        t, w, ev = _dt.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S"), m.group(2), m.group(3)
        if ev == ": new task":
            if start[w] is None and t >= LAYER_START:
                start[w] = t
            continue
        if ev.endswith("started"):
            if start[w] is None and t >= LAYER_START and "(brief)" in line:   # a worker born on the row
                start[w] = t
            open_at[w] = t
        elif w in open_at:
            a0 = open_at.pop(w)
            if start[w] is not None:
                total += max(0.0, (t - max(a0, start[w])).total_seconds())
    nowt = _dt.datetime.now()
    for w, a0 in open_at.items():
        if start[w] is not None:
            total += max(0.0, (nowt - max(a0, start[w])).total_seconds())
    return total / 3600.0


def dl_summary(lr):
    dl = sorted(r for r, v in lr.items() if v.get("list") == "TOP200_DL")
    aud = {r: dl_audit(r) for r in dl}
    done = [r for r in dl if aud[r]]
    days = [r for r in done if str(aud[r].get("solver_shape", "")).upper().startswith("DAYS")]
    dos = [r for r in dl if os.path.isfile(os.path.join(rowdir(r), "DOSSIER.md"))]
    return ("Deep-learning rows (T223-T422): %d live, %d audited, %d with a DAYS shape (%s), %d with a dossier. Solvers go "
            "only on DAYS rows whose gate is open." % (len(dl), len(done), len(days), ", ".join(days) or "none", len(dos)))


def cmd_board(a):
    lr = list_rows()
    st = staff()
    sc = scan_rows()
    rows = sorted(set(st) | {r for r in os.listdir(ROWS) if re.fullmatch(r"T\d{3}", r)} if os.path.isdir(ROWS) else set(st))
    out = ["# The frontier board (top-400: probability T001-T222, deep learning T223-T422)", "",
           "Written %s by frontier.py. A row moves only when its obstruction moves; constants and special cases outside "
           "the row's targets are counted but score nothing (his order 14 Oct 23:25)." % now()[:16], "",
           dl_summary(lr), "",
           "| row | title | lead | workers | shape | literature | obstruction moves | worker-h since staffed (approx) | other claims (bound / special / literature / route-failure) | dead routes |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for row in rows:
        info = st.get(row, {})
        lit = {}
        try:
            lit = json.loads(read(os.path.join(rowdir(row), "lit.json")) or "{}")
        except ValueError:
            pass
        mv = jsonl(os.path.join(rowdir(row), "moves.jsonl"))
        prog = sum(1 for m in mv if m.get("kind") in PROGRESS)
        cl = harvested_claims(row)
        kinds = {}
        for c in cl:
            kinds[c.get("kind", "other")] = kinds.get(c.get("kind", "other"), 0) + 1
        # a lead's recorded bound/special/literature moves count too, unless the same claim was harvested
        seen = {str(c.get("id", "")).lower() for c in cl}
        for m in mv:
            k = m.get("kind")
            if k in ("bound", "special", "literature") and str(m.get("claim", "")).lower() not in seen:
                kinds[k] = kinds.get(k, 0) + 1
        dead = sum(1 for r in routes(row) if r.get("status") in ("dead", "settled"))
        wh = worker_hours(info.get("folders", []))
        out.append("| %s | %s | %s | %s | %s | %s | %d | %s | %d / %d / %d / %d | %d |" % (
            row, lr.get(row, {}).get("title", "")[:48], info.get("lead", ""), ", ".join(
                "/".join(f.rstrip("/\\").replace("\\", "/").split("/")[-2:]) if re.search(r"/T\d{3}$", f.rstrip("/\\"))
                else os.path.basename(f.rstrip("/\\")) for f in info.get("folders", [])),
            sc.get(row, {}).get("shape", "") or (("audit: " + str(dl_audit(row).get("solver_shape", "not audited"))[:40])
                                                  if is_dl(row, lr.get(row, {})) else ""),
            (("%s %s" % (lit.get("verdict", ""), (lit.get("at") or "")[:10])).strip() or "not checked") + (
                "; hunter: solved?" if sc.get(row, {}).get("solved", "").lower() == "yes" else ""), prog,
            "-" if wh is None else "%.1f" % wh,
            kinds.get("bound", 0), kinds.get("special", 0), kinds.get("literature", 0), kinds.get("route-failure", 0),
            dead))
    write(BOARD, "\n".join(out) + "\n")
    print("wrote", BOARD, len(rows), "rows")


# ---------------------------------------------------------------------------------------------------------- gate
def cmd_gate(a):
    row = a.row.upper()
    d = dossier(row)
    why = []
    for k in ("FAILURE POINT", "OBSTRUCTION", "FRONTIER", "TARGETS"):
        if len(d.get(k, "")) < 40:
            why.append("dossier has no %s section worth the name" % k)
    try:
        lit = json.loads(read(os.path.join(rowdir(row), "lit.json")) or "{}")
    except ValueError:
        lit = {}
    if not lit:
        why.append("no literature check recorded (frontier.py lit)")
    else:
        age = _dt.datetime.now().astimezone() - _dt.datetime.fromisoformat(lit["at"])
        if age.days >= 7:
            why.append("literature check is %d days old" % age.days)
        if lit.get("verdict") == "solved":
            why.append("literature says SOLVED: retire the row, do not staff it")
    if is_dl(row):
        au = dl_audit(row)
        if not au:
            why.append("deep-learning row not audited yet (auditor output: %s)" % ", ".join(DL_AUDITS))
        else:
            if not str(au.get("solver_shape", "")).upper().startswith("DAYS"):
                why.append("auditor gives solver shape %r, not DAYS" % str(au.get("solver_shape", ""))[:60])
            if str(au.get("status", "")).upper() == "SOLVED":
                why.append("auditor says SOLVED: retire the row")
            if str(au.get("statement_ok", "")).upper().startswith("NO") and "repaired" not in d.get("STATEMENT", "").lower():
                why.append("auditor found the list statement faulty; the dossier STATEMENT must be the repaired one and say so"
                           " (the word 'repaired')")
    if why:
        print("GATE CLOSED for %s:\n- " % row + "\n- ".join(why))
        sys.exit(3)
    print("gate open for %s" % row)


def main():
    p = argparse.ArgumentParser(description="the frontier layer for the top-400 list (probability + deep learning)")
    sub = p.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("brief")
    b.add_argument("row")
    b.add_argument("--short", action="store_true")
    c = sub.add_parser("check")
    c.add_argument("row")
    c.add_argument("idea")
    r = sub.add_parser("route")
    r.add_argument("row")
    r.add_argument("status", choices=["live", "dead", "done", "settled"])
    r.add_argument("route")
    r.add_argument("--why", default="")
    r.add_argument("--by", default=os.environ.get("AGENT_MESH_ID", "?"))
    r.add_argument("--evidence", default="")
    m = sub.add_parser("move")
    m.add_argument("row")
    m.add_argument("kind", choices=["moved", "narrowed", "special", "bound", "literature", "none"])
    m.add_argument("text")
    m.add_argument("--claim", default="")
    m.add_argument("--by", default=os.environ.get("AGENT_MESH_ID", "?"))
    li = sub.add_parser("lit")
    li.add_argument("row")
    li.add_argument("--verdict", required=True, choices=["open", "narrowed", "solved"])
    li.add_argument("--newest", action="append")
    li.add_argument("--query", action="append")
    li.add_argument("--note", default="")
    li.add_argument("--by", default=os.environ.get("AGENT_MESH_ID", "?"))
    sub.add_parser("sync")
    hu = sub.add_parser("hunt")
    hu.add_argument("--glob", default=HUNT_GLOB)
    sub.add_parser("board")
    g = sub.add_parser("gate")
    g.add_argument("row")
    a = p.parse_args()
    {"brief": cmd_brief, "check": cmd_check, "route": cmd_route, "move": cmd_move, "lit": cmd_lit, "sync": cmd_sync,
     "board": cmd_board, "gate": cmd_gate, "hunt": cmd_hunt}[a.cmd](a)


if __name__ == "__main__":
    main()

