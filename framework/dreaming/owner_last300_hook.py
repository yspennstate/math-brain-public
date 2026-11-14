# -*- coding: utf-8 -*-
"""His last 300 prompts as a hook (owner order 12 Nov 2026 04:27: "make my ast 300 prots into hook").

Each of his last 300 prompts (from memory/prompts/LAST_3000_OWNER_PROMPTS.md, re-fires folded) becomes a trigger. When a
prompt or a tool call shares enough rare words with one of them, the hook prints his own words with the date, so the
agent sees what he already asked about the thing it is touching. Advisory only, never blocks.

- Spelling: the user's words are mapped to the nearest correctly spelled word from the brain's own text ("moive" -> "movie"),
  cached in owner_last300_spell.json so a rebuild only looks up new words.
- Fires: at most 2 per prompt, 1 per tool call, a tool-call fire at most once per 3 minutes per session, and each of his
  prompts at most once per 3 hours per session.
- The index rebuilds itself when the prompt file is newer (the hourly prompt build refreshes that file).

python -s owner_last300_hook.py [--codex]          hook mode (reads the event on stdin)
python -s owner_last300_hook.py --build            rebuild the index now
python -s owner_last300_hook.py --show "<text>"    print the matches for a text
python -s owner_last300_hook.py --selftest
"""
import difflib
import json
import math
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.expanduser("~/.claude/projects/" + os.environ.get("BRAIN_SLUG", "default") + "/memory/prompts/LAST_3000_OWNER_PROMPTS.md")
VOCAB_SRC = [os.path.expanduser("~/.claude/projects/" + os.environ.get("BRAIN_SLUG", "default") + "/memory/MEMORY.md"),
             os.path.expanduser("~/.claude/CLAUDE.md"), os.path.expanduser("~/AGENTS.md")]
INDEX = os.path.join(HERE, "owner_last300_index.json")
SPELL = os.path.join(HERE, "owner_last300_spell.json")
STATE_DIR = os.path.join(HERE, "owner_last300_state")
N = 300
PROMPT_COOL = 3 * 3600
TOOL_GAP = 180
STOP = set("""the and for that this with you are was were have has had not but all any can will would should could just
also from they them then than there their what when where which who how why its it's into out our your yours about make
sure keep want need like one two get got use using used now new more most some such very really much many each every
other same only over under after before again please work working agents agent thing things stuff way going know does
did done doing being been here him his her she let lets yes okay don't dont i'm well even still way give gave tell told
said say see seen look looking right time times day days today tonight next last first part parts sure kind lot lots
able ask asked""".split())
WORD = re.compile(r"[a-z][a-z0-9]{2,}")


def toks(text):
    return [w for w in WORD.findall(text.lower()) if w not in STOP]


def load_vocab():
    words = {}
    mem = os.path.dirname(VOCAB_SRC[0])
    paths = list(VOCAB_SRC) + [os.path.join(mem, f) for f in os.listdir(mem) if f.endswith(".md")]
    for p in paths:
        try:
            for w in WORD.findall(open(p, encoding="utf-8", errors="ignore").read(200000).lower()):
                words[w] = words.get(w, 0) + 1
        except OSError:
            pass
    return {w for w, c in words.items() if c >= 4}


def canon(tokens, vocab, spell, by_first):
    out = []
    for t in tokens:
        if t in vocab or t.isdigit() or len(t) < 4:
            out.append(t)
            continue
        if t not in spell:
            m = difflib.get_close_matches(t, by_first.get(t[0], []), n=5, cutoff=0.75)
            ana = [w for w in m if sorted(w) == sorted(t)]
            spell[t] = ana[0] if ana else (m[0] if m and difflib.SequenceMatcher(None, t, m[0]).ratio() >= 0.8 else t)
        out.append(spell[t])
    return out


def parse_prompts():
    rows, day = [], ""
    for line in open(SRC, encoding="utf-8", errors="ignore"):
        m = re.match(r"## (\d{4}-\d{2}-\d{2})", line)
        if m:
            day = m.group(1)
            continue
        m = re.match(r"- (\d{2}:\d{2}) \[([0-9a-f]{8})\] (.*)", line)
        if m and len(m.group(3)) >= 25:
            rows.append({"at": day + " " + m.group(1), "sess": m.group(2), "text": m.group(3).strip()})
            if len(rows) >= N:
                break
    return rows


def build(fresh_vocab=False):
    vocab = None
    if not fresh_vocab:
        try:
            vocab = set(json.load(open(INDEX, encoding="utf-8"))["vocab"])
        except Exception:
            vocab = None
    if not vocab:
        vocab = load_vocab()
    by_first = {}
    for w in vocab:
        if len(w) >= 4:
            by_first.setdefault(w[0], []).append(w)
    try:
        spell = json.load(open(SPELL, encoding="utf-8"))
    except Exception:
        spell = {}
    rows = parse_prompts()
    df = {}
    for r in rows:
        r["t"] = sorted(set(canon(toks(r["text"]), vocab, spell, by_first)))
        for t in r["t"]:
            df[t] = df.get(t, 0) + 1
    idf = {t: round(math.log((len(rows) + 1) / c), 3) for t, c in df.items()}
    json.dump(spell, open(SPELL + ".tmp", "w", encoding="utf-8"))
    os.replace(SPELL + ".tmp", SPELL)
    out = {"built": time.time(), "src_mtime": os.path.getmtime(SRC), "rows": rows, "idf": idf,
           "vocab": sorted(w for w in vocab if len(w) >= 4)}
    json.dump(out, open(INDEX + ".tmp", "w", encoding="utf-8"), ensure_ascii=False)
    os.replace(INDEX + ".tmp", INDEX)
    return out


def load_index():
    try:
        ix = json.load(open(INDEX, encoding="utf-8"))
        if os.path.getmtime(SRC) <= ix.get("src_mtime", 0) + 1:
            return ix
    except Exception:
        pass
    return build()


def matches(text, ix, tool=False):
    vocab = set(ix["vocab"])
    by_first = {}
    for w in ix["vocab"]:
        by_first.setdefault(w[0], []).append(w)
    try:
        spell = json.load(open(SPELL, encoding="utf-8"))
    except Exception:
        spell = {}
    q = set(canon(toks(text)[:400], vocab, spell, by_first))
    idf = ix["idf"]
    need_n, need_s = (4, 14.0) if tool else (3, 10.0)
    norm = re.sub(r"\s+", " ", text.strip().lower())[:200]
    found = []
    for i, r in enumerate(ix["rows"]):
        shared = [t for t in r["t"] if t in q]
        s = sum(idf.get(t, 0) for t in shared)
        if len(shared) >= need_n and s >= need_s and not norm.startswith(r["text"].lower()[:60]):
            found.append((s, i, shared))
    found.sort(reverse=True)
    return found


def main():
    if "--build" in sys.argv:
        ix = build(fresh_vocab=True)
        print("built", len(ix["rows"]), "prompts,", len(ix["idf"]), "terms")
        return
    if "--show" in sys.argv:
        text = sys.argv[sys.argv.index("--show") + 1]
        ix = load_index()
        for s, i, shared in matches(text, ix)[:5]:
            r = ix["rows"][i]
            print(round(s, 1), r["at"], r["sess"], ",".join(shared[:8]), "|", r["text"][:160])
        return
    if "--selftest" in sys.argv:
        return selftest()
    codex = "--codex" in sys.argv
    try:
        data = json.loads(sys.stdin.read() or "{}")
    except Exception:
        return
    if not isinstance(data, dict) or data.get("agent_id") or data.get("agent_type"):
        return
    event = str(data.get("hook_event_name") or "")
    sid = str(data.get("session_id") or data.get("thread_id") or "").strip().lower()[:8]
    if event == "UserPromptSubmit":
        text, tool = str(data.get("prompt") or ""), False
    elif event == "PreToolUse":
        ti = data.get("tool_input") or {}
        text = " ".join(str(ti.get(k) or "") for k in ("command", "file_path", "description", "new_string", "content", "url"))[:4000]
        tool = True
    else:
        return
    if not sid or len(text) < 20:
        return
    os.makedirs(STATE_DIR, exist_ok=True)
    stp = os.path.join(STATE_DIR, sid + ".json")
    try:
        st = json.load(open(stp, encoding="utf-8"))
    except Exception:
        st = {}
    now = time.time()
    if tool and now - st.get("last_tool", 0) < TOOL_GAP:
        return
    try:
        ix = load_index()
    except Exception:
        return
    shown = st.get("shown", {})
    lines = []
    for s, i, shared in matches(text, ix, tool):
        r = ix["rows"][i]
        key = r["at"] + r["sess"]
        if now - shown.get(key, 0) < PROMPT_COOL:
            continue
        shown[key] = now
        lines.append(f"  {r['at']} [{r['sess']}]: \"{r['text'][:420]}\"")
        if len(lines) >= (1 if tool else 2):
            break
    if not lines:
        return
    if tool:
        st["last_tool"] = now
    st["shown"] = {k: v for k, v in shown.items() if now - v < 86400}
    try:
        json.dump(st, open(stp, "w", encoding="utf-8"))
    except Exception:
        pass
    text = ("[his-last-300] The user already said this about what you are touching (the user's words, newest wins over older; a hint, "
            "not a verdict):\n" + "\n".join(lines))
    if codex:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": text}}))
    else:
        try:   # in the dispatcher's own process stdout is a StringIO, which has no reconfigure (12 Nov, an agent)
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
        print(text)


def selftest():
    ix = load_index()
    ok = 0
    pos = " ".join(ix["rows"][5]["text"].split()[3:])
    hit = matches("so about this: " + pos, ix)
    print("PASS" if hit else "FAIL", "his own older prompt matches itself (paraphrase)"); ok += bool(hit)
    neg = matches("ls -la /tmp && echo done", ix, tool=True)
    print("PASS" if not neg else "FAIL", "a plain shell command fires nothing"); ok += not neg
    mis = matches("stop the l4 no more H3 use the google api clips only when i ask on the computer", ix)
    print("PASS" if mis else "FAIL", "the 03:51 directive in other words fires"); ok += bool(mis)
    print(f"{ok}/3")


if __name__ == "__main__":
    main()
