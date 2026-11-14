#!/usr/bin/env python3
"""recognize_on_read.py - read-time recognition: "what you just read looks like a place we have been".

PostToolUse on Read and Bash. Scores the first 4000 chars of the tool's output against the memories with BM25, on a
query cut to the K rarest words of that text, and names the top memory only when all of these hold:
  - it is a lesson or a scar: `lesson: true` in its frontmatter, or type feedback, or a slug that says
    mistake / scar / wrong / trap / never / bug;
  - it stands out: top score s1 >= S1_MIN, s1 / s10 >= CONC_MIN, s1 / s2 >= GAP_MIN;
  - this session has not been told about it yet, and the last fire was at least GAP_CALLS calls ago.

Why (grand hunts, 11 Nov 2026): lessons were filed after every hunt, yet the brain arm made no recall call after the
first hunt and its lesson text reached it in one hunt of four. The agent does not ask; the reading has to trigger it.
Calibrated on 23 hunt transcripts and 17 owner sessions (scratchpad recog_calib.log, HARDER_HUNT.md "Read-time
recognition, calibrated"): the lesson at top-1 passing the rule in 23 of 23 hunts, 2.7 fires per 100 owner-session
outputs. Silent and fail-safe on any error. Never prints the tool output.
"""
import io
import json
import math
import os
import re
import sys
import time

D = os.path.join(os.path.expanduser("~"), ".claude", "dreaming")
sys.path.insert(0, D)
MEM = os.path.join(os.path.expanduser("~"), ".claude", "projects", os.environ.get("BRAIN_SLUG", "default"), "memory")
STATE = os.environ.get("ROR_STATE") or os.path.join(D, "recognize_on_read")
HEAD = 4000
K = int(os.environ.get("ROR_K", "32"))
S1_MIN = float(os.environ.get("ROR_S1", "30"))
CONC_MIN = float(os.environ.get("ROR_CONC", "1.5"))
GAP_MIN = float(os.environ.get("ROR_GAP", "1.3"))
BUDGET = float(os.environ.get("ROR_BUDGET", "20000"))
DF_FRAC = float(os.environ.get("ROR_DF_FRAC", "1.0"))
GAP_CALLS = int(os.environ.get("ROR_GAP_CALLS", "5"))
EXCLUDE = ("grand_hunt_handoff_", "compaction_")
SCARWORD = re.compile(r"mistake|scar|wrong|trap|never|bug")
# Question time (ROR_QTIME=1, default off): an output that poses a question ('?'-ended line) is scored on its question
# lines alone, names blanked, against the lesson pool; the top lesson is named if it stands out, without waiting
# GAP_CALLS. Why (seed 30, Opus brain arm): the station-17 output scored the old-style lesson 16.2 on the whole text,
# rank 14, so nothing fired and the agent fell; the question line alone names it.
QTIME = os.environ.get("ROR_QTIME", "0") == "1"
QMIN = float(os.environ.get("ROR_QMIN", "15"))
# a memory filed as a lesson (`lesson: true`) needs a smaller lead: on the old-style stations of five Opus hunts the
# lesson was top at 19.1 on every first posting but led an unrelated runner-up by only 1.08-1.44x
QLGAP = float(os.environ.get("ROR_QLGAP", "1.1"))
QLINE = re.compile(r"^[^\r\n]{10,400}\?[^\r\n]{0,120}", re.M)  # a line that asks something
# Inside a hunt (ROR_HUNT=1, or a hunt working folder) a memory ABOUT the hunt - its design, arms, results - would
# tell the agent under test how it is scored: seed 30 call 2 named one. Only the archive lessons stay.
HUNT_ENV = os.environ.get("ROR_HUNT", "0") == "1"
HUNT_CWD = re.compile(r"grand_hunt|[\\/]HH_|[\\/]HX_", re.I)
HUNT_TEXT = re.compile(r"grand[ _-]hunt|hunt arm|brain arm|bare arm|scar station|trap station|scar/trap|hunt transcript",
                       re.I)
BRAIN_READOUT = re.compile(r"(brain\.py\s+(recall|node|neighbors)|math_recall\.py|problem_recall\.py)")


def out_text(ev):
    r = ev.get("tool_response")
    if isinstance(r, dict):
        for k in ("stdout", "content", "output", "text"):
            v = r.get(k)
            if isinstance(v, str) and v.strip():
                return v
            if isinstance(v, dict) and isinstance(v.get("content"), str):
                return v["content"]
        f = r.get("file")
        if isinstance(f, dict) and isinstance(f.get("content"), str):
            return f["content"]
    if isinstance(r, list):
        return "\n".join(x.get("text", "") for x in r if isinstance(x, dict))
    return r if isinstance(r, str) else ""


def head(slug):
    try:
        return io.open(os.path.join(MEM, slug + ".md"), encoding="utf-8", errors="replace").read(2000)
    except OSError:
        return ""


def in_pool(slug, h):
    if re.search(r"^\s*lesson:\s*true", h, re.M | re.I):
        return "lesson"
    m = re.search(r"^\s*type:\s*(\w+)", h, re.M)
    if m and m.group(1) == "feedback":
        return "feedback"
    if SCARWORD.search(slug):
        return "scar"
    return ""


def pruned(text, B, tokens):
    df = B.df_view() if hasattr(B, "df_view") else B.df
    n = B.n
    cand = sorted(set(tokens(text[:HEAD])))
    if hasattr(df, "prefetch"):
        df.prefetch(cand)
    cap = DF_FRAC * n
    toks = [t for t in cand if df.get(t) and df[t] <= cap]
    idf = {t: math.log(1.0 + (n - df[t] + 0.5) / (df[t] + 0.5)) for t in toks}
    keep, tot = [], 0
    # rarest words first; stop once their summed document frequency passes BUDGET (keep at least 4). Scoring time
    # follows the postings read, and a short output otherwise fills its K slots with common words (0.35 s a call
    # uncapped; 0.2 s at 20000 with the same verdicts on the calibration set, 11 Nov)
    for t in sorted(toks, key=lambda t: (-idf[t], t))[:K]:
        if len(keep) >= 4 and tot + df[t] > BUDGET:
            break
        keep.append(t)
        tot += df[t]
    return " ".join(keep)


def allowed(slug, hunt):
    if slug.startswith(EXCLUDE):
        return False
    if slug.startswith("grand_hunt_archive_"):
        return True
    if slug.startswith("grand_hunt_"):
        return False
    return not (hunt and HUNT_TEXT.search(head(slug)))


def strip_names(line):
    """Blank every capitalised word except the first word of the line: outpost and person names."""
    toks = re.split(r"(\s+)", line)
    first = True
    for j, tk in enumerate(toks):
        if tk and tk[0].isalpha():
            if not first and tk[0].isupper():
                toks[j] = " "
            first = False
    return "".join(toks)


CODEISH = re.compile(r"://|[=\\{}<>|$]|\(\?|\?\)|\?\?|[\w\]\)]\?[\w\[\(.:]")


def prose_question(line):
    """A sentence that asks: a word right before the '?', at least five words, no URL, regex or code."""
    if CODEISH.search(line) or not re.search(r"[A-Za-z]\?(\s|$|[\"')*_])", line):
        return False
    return len(re.findall(r"[A-Za-z]{2,}", line)) >= 5


def qjudge(text, hunt=False, B=None):
    """Question-time rule: (slug, s1, 0, gap, kind) or None."""
    ql = [x for x in (m.group(0) for m in QLINE.finditer(text[:HEAD])) if prose_question(x)]
    if not ql:
        return None
    from bm25 import BM25, tokens
    B = B or BM25()
    df = B.df_view() if hasattr(B, "df_view") else B.df
    cand = sorted(set(tokens(" ".join(strip_names(x.lstrip("#*-> ")) for x in ql))))
    if hasattr(df, "prefetch"):
        df.prefetch(cand)
    q = " ".join(t for t in cand if df.get(t))
    if not q:
        return None
    pool = []
    for s, sc in B.score(q, topk=40):
        if not allowed(s, hunt):
            continue
        k = in_pool(s, head(s))
        if k:
            pool.append((s, sc, k))
            if len(pool) == 2:
                break
    if not pool:
        return None
    s1 = pool[0][1]
    s2 = pool[1][1] if len(pool) > 1 else 0.0
    gap = s1 / s2 if s2 > 0 else 99.0
    if s1 < QMIN or gap < (min(QLGAP, GAP_MIN) if pool[0][2] == "lesson" else GAP_MIN):
        return None
    return pool[0][0], round(s1, 1), 0, round(gap, 2), pool[0][2], (pool[1][0] if len(pool) > 1 else "")


def judge(text, hunt=False):
    """(slug, s1, conc, gap, kind) when the rule passes, else None. Kept apart from the hook I/O for the tests."""
    if len(text.strip()) < 40:
        return None
    from bm25 import BM25, tokens
    B = BM25()
    q = pruned(text, B, tokens)
    if not q:
        return None
    # a memory about the hunt itself (its results, its checker) would tell the agent under test how it is scored
    top = [x for x in B.score(q, topk=20) if allowed(x[0], hunt)][:12]
    if len(top) < 2:
        return None
    s1, s2, s10 = top[0][1], top[1][1], top[min(9, len(top) - 1)][1]
    conc = s1 / s10 if s10 > 0 else 99.0
    gap = s1 / s2 if s2 > 0 else 99.0
    if s1 < S1_MIN or conc < CONC_MIN or gap < GAP_MIN:
        return None
    kind = in_pool(top[0][0], head(top[0][0]))
    if not kind:
        return None
    return top[0][0], round(s1, 1), round(conc, 2), round(gap, 2), kind


def desc(slug):
    m = re.search(r"^\s*description:\s*(.+)$", head(slug), re.M)
    return (m.group(1).strip().strip('"') if m else "")[:300]


def load_state(sess):
    p = os.path.join(STATE, "s_%s.json" % re.sub(r"[^\w-]", "", sess)[:64])
    try:
        return p, json.load(io.open(p, encoding="utf-8"))
    except (OSError, ValueError):
        return p, {"calls": 0, "last_fire": -10 ** 6, "fired": []}


def save_state(p, st):
    try:
        os.makedirs(STATE, exist_ok=True)
        tmp = p + ".%d.tmp" % os.getpid()
        with io.open(tmp, "w", encoding="utf-8") as f:
            json.dump(st, f)
        os.replace(tmp, p)
    except OSError:
        pass


def main():
    raw = getattr(sys.stdin, "buffer", sys.stdin).read()
    ev = json.loads(raw.decode("utf-8", "surrogateescape") if isinstance(raw, bytes) else raw)
    if ev.get("tool_name") not in ("Read", "Bash", "PowerShell"):
        return
    # A brain readout already shows the memory it names: recognizing it again only repeats the recall.
    cmd = str((ev.get("tool_input") or {}).get("command") or "")
    if BRAIN_READOUT.search(cmd):
        return
    sess = str(ev.get("session_id") or "nosession")
    p, st = load_state(sess)
    st["calls"] += 1
    t0 = time.time()
    j = None
    hunt = HUNT_ENV or bool(HUNT_CWD.search(str(ev.get("cwd") or "")))
    text = out_text(ev)
    if QTIME:
        j = qjudge(text, hunt)
        if j and j[0] in st["fired"]:
            j = None
    if not j and st["calls"] - st["last_fire"] >= GAP_CALLS:
        j = judge(text, hunt)
        if j and j[0] in st["fired"]:
            j = None
    if j:
        st["last_fire"] = st["calls"]
        st["fired"].append(j[0])
        msg = ("[recognized] what you just read resembles a %s the brain holds: %s - %s\n"
               "  (read-time recognition, s1 %s, %sx the tenth match, %sx the second; a hint, not a verdict: weigh "
               "it against what is in front of you. Full card: python ~/.claude/dreaming/brain.py node %s)"
               % (j[4], j[0], desc(j[0]), j[1], j[2], j[3], j[0]))
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": msg}}))
    save_state(p, st)
    try:
        with io.open(os.path.join(STATE, "fires.jsonl"), "a", encoding="utf-8") as f:
            f.write(json.dumps({"t": round(time.time(), 1), "sess": sess[:8], "call": st["calls"],
                                "ms": int((time.time() - t0) * 1000), "fire": j[0] if j else None}) + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
