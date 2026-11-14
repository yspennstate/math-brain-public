# -*- coding: utf-8 -*-
"""The owner-prompt subconscious as a hook (owner order 13 Nov 2026 16:08: "create a secondary subconscious part of the
brain that holds every single one of them again and is connected to the frontier model, that way agents have a better
understanding of how things are done and what i am doing").

The store is 12_cognitive_architecture/owner_prompt_subconscious/store/prompts.sqlite (build.py there): every distinct
prompt he has given since April, with its dates, how often, and a CORRECTION flag. owner_last300_hook.py already covers
his last 300 prompts; this hook covers everything OLDER, so the two never print the same prompt. When a prompt or a tool
call shares enough words with one of his older prompts, it prints his own words with the date. Corrections rank first.
Advisory only, never blocks, silent on any error.

Fires: at most 2 per prompt, 1 per tool call; a tool-call fire at most once per 5 minutes per session; each of his
prompts at most once per 6 hours per session.

python -s owner_subconscious_hook.py [--codex]          hook mode (reads the event on stdin)
python -s owner_subconscious_hook.py --show "<text>"    print the matches for a text
python -s owner_subconscious_hook.py --selftest
"""
import json
import os
import re
import sqlite3
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.expanduser(
    r"~/brain-repo/12_cognitive_architecture/owner_prompt_subconscious/store/prompts.sqlite")
STATE_DIR = os.path.join(HERE, "owner_subconscious_state")
RECENT_SKIP = 300            # his newest distinct prompts belong to owner_last300_hook
TOOL_EVERY_S = 300
SAME_PROMPT_S = 6 * 3600
MIN_SHARED = 3               # distinct rare words a match must share
CUT = 300
STOP = set("""a an the and or but if then else of to in on at by for with from into onto over under about as is are was
were be been being do does did done have has had having i you he she it we they me my your our their this that these
those there here what which who whom whose when where why how all any both each few more most other some such no nor not
only own same so than too very can will just should now also please make sure keep work working want need get use using
like ok okay yes thing things stuff one two new last next every first again still really much many way time let go going
fire minutes hours days next read prompts tasks task manager without stopping implementing agents agent brain""".split())


def words(text):
    seen, out = set(), []
    for w in re.findall(r"[a-z][a-z0-9]{2,}", (text or "").lower()):
        if w not in STOP and w not in seen:
            seen.add(w)
            out.append(w)
    return out[:40]


def search(text, exclude_text="", limit=2):
    ws = words(text)
    if len(ws) < MIN_SHARED or not os.path.exists(DB):
        return []
    db = sqlite3.connect("file:%s?mode=ro" % DB.replace("\\", "/"), uri=True, timeout=2)
    try:
        cutoff = db.execute("select last from p order by last desc limit 1 offset ?", (RECENT_SKIP,)).fetchone()
        cutoff = cutoff[0] if cutoff else ""
        q = " OR ".join('"%s"' % w for w in ws)
        rows = db.execute(
            "select p.id, p.first, p.last, p.times, p.correction, p.text, bm25(f) from f join p on p.rowid = f.rowid "
            "where f match ? and p.last < ? order by bm25(f) limit 40", (q, cutoff)).fetchall()
    finally:
        db.close()
    want = set(ws)
    ex = " ".join(exclude_text.split()).lower()
    out = []
    for pid, first, last, times, corr, t, score in rows:
        if ex and " ".join(t.split()).lower() == ex:
            continue
        shared = want & set(words(t))
        if len(shared) < MIN_SHARED:
            continue
        out.append((score - (3.0 if corr else 0.0) - 0.5 * len(shared), pid, first, times, corr, t, sorted(shared)))
    out.sort()
    return out[:limit]


def fmt(hits):
    lines = ["[subconscious] The user said this before, in older prompts (the user's words; a hint, not a verdict - newer words win):"]
    for _, pid, first, times, corr, t, shared in hits:
        flat = " ".join(t.split())
        tag = "CORRECTION " if corr else ""
        lines.append('  %s%s%s: "%s"' % (tag, first[:16].replace("T", " "),
                                         " (asked %dx)" % times if times > 1 else "",
                                         flat[:CUT] + (" ..." if len(flat) > CUT else "")))
    lines.append("  every prompt of his: python -s ~/.claude/dreaming/owner_subconscious_hook.py --show \"<words>\"")
    return "\n".join(lines)


def load_state(sess):
    try:
        return json.load(open(os.path.join(STATE_DIR, sess + ".json"), encoding="utf-8"))
    except Exception:
        return {"tool_at": 0, "shown": {}}


def save_state(sess, st):
    try:
        os.makedirs(STATE_DIR, exist_ok=True)
        now = time.time()
        st["shown"] = {k: v for k, v in st["shown"].items() if now - v < SAME_PROMPT_S}
        with open(os.path.join(STATE_DIR, sess + ".json"), "w", encoding="utf-8") as f:
            json.dump(st, f)
    except Exception:
        pass


def hook(codex):
    data = json.loads(sys.stdin.read() or "{}")
    event = data.get("hook_event_name") or "UserPromptSubmit"
    sess = re.sub(r"[^A-Za-z0-9_-]", "", str(data.get("session_id") or "nosession"))[:40]
    now = time.time()
    st = load_state(sess)
    if event == "PreToolUse":
        if now - st.get("tool_at", 0) < TOOL_EVERY_S:
            return
        ti = data.get("tool_input") or {}
        text = " ".join(str(ti.get(k) or "") for k in ("description", "command", "file_path", "pattern", "prompt"))
        limit, exclude = 1, ""
    else:
        text = data.get("prompt") or ""
        limit, exclude = 2, text
    hits = [h for h in search(text, exclude, limit + 2) if now - st["shown"].get(h[1], 0) >= SAME_PROMPT_S][:limit]
    if not hits:
        return
    for h in hits:
        st["shown"][h[1]] = now
    if event == "PreToolUse":
        st["tool_at"] = now
    save_state(sess, st)
    out = fmt(hits)
    if codex:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": out}}))
    else:
        print(out)


def main():
    a = sys.argv[1:]
    if a[:1] == ["--show"]:
        hits = search(" ".join(a[1:]), limit=10)
        print(fmt(hits) if hits else "no older prompt of his shares enough words")
        return
    if a[:1] == ["--selftest"]:
        ok = 0
        q = os.environ.get("SUBCON_SELFTEST_QUERY", "")   # a sentence close to one of your own older prompts
        h = search(q) if q else ["skipped"]
        print("PASS" if h else "FAIL", "an older prompt is found" if q else "set SUBCON_SELFTEST_QUERY to test recall")
        ok += bool(h)
        n = search("ls -la")
        print("PASS" if not n else "FAIL", "a plain shell command fires nothing"); ok += not n
        print("%d/2" % ok)
        return
    try:
        hook("--codex" in a)
    except Exception:
        pass


if __name__ == "__main__":
    main()
