# -*- coding: utf-8 -*-
"""Core of the citation hooks C01..C26 (an agent, 11 Nov 2026; C17..C26 an agent, 14 Nov).

Written at the author's request..

Each hook is one file C01_*.py .. C16_*.py holding a HOOK dict (and optionally check(ctx)). cite_hooks_run.py loads them
all and runs them on one hook payload. A call is sorted into CHANNELS:
  github        a git push / gh release / gh repo create / a GitHub contents API call that carries a paper (.tex/.pdf,
                a paper or open-problems repo, or a folder holding a \\documentclass .tex)
  zenodo        a Zenodo API call or upload script, or the browser on zenodo.org
  researchgate  the browser on researchgate.net, or a script that uploads there
  draft         a Write/Edit of a .tex or .bib that touches the bibliography or a \\cite
  prompt        a prompt that asks to publish, post or upload a paper
  develop       problem_recall.py (work on an open problem starts), or a .tex edit with a theorem/lemma/proof
  writing       a .tex edit touching the abstract or the introduction (or background / main results / prior work)
  credit        a .tex edit touching the acknowledgments or the AI declaration
A hook names the channels it fires on. Publishing channels print the MASSIVE banner (C01) and every due checklist
line; each line prints at most once per session per its cool-down. Hooks warn, never block. Fires go to fires.jsonl.
"""
import importlib.util
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STATE_DIR = os.path.join(HERE, "state")
FIRES = os.path.join(HERE, "fires.jsonl")
BANNER = "!" * 100
PUBLISH = ("github", "zenodo", "researchgate")

PAPERISH = re.compile(r"\.tex\b|\.pdf\b|\.bib\b|\bpapers?\b|preprint|manuscript|open[-_ ]?problems|_paper\b|paper_|"
                      r"arxiv|zenodo|researchgate", re.I)
GIT_PUB = re.compile(r"\bgit\s+(?:-C\s+\S+\s+)?push\b|\bgh\s+(?:release\s+(?:create|upload)|repo\s+create)\b|"
                     r"\bgh\s+api\b[^;|&]{0,200}/contents/", re.I)
RUNS = r"(?:curl|wget|Invoke-WebRequest|Invoke-RestMethod|iwr|irm|requests\.\w+|(?:py|python)\S*\s+(?:-\S+\s+)*\S*)"
ZEN_ACT = re.compile(RUNS + r"[^;|&\n]{0,300}zenodo|zenodo\.org/api", re.I)
RG_ACT = re.compile(r"(?:py|python)\S*\s+(?:-\S+\s+)*\S*researchgate\w*\.py", re.I)
HEREDOC = re.compile(r"<<-?\s*(['\"]?)(\w+)\1[^\n]*\n.*?\n\s*\2\b", re.S)
CD = re.compile(r"(?:^|[;&|]\s*)cd\s+(\"[^\"]+\"|'[^']+'|[^\s;&|]+)")
# Commands that only WRITE ABOUT papers or citations (a memory, the board, the checklist, the mesh, a mail, this folder).
ABOUT = re.compile(r"brain\.py\s+(?:remember|recall|dream-about|node)|fleet_board\.py|checklist(?:_hook)?\.py|"
                   r"agent_mesh\.py|send_\w*mail\w*\.py|\bmail\.py|math_recall\.py|problem_recall\.py|"
                   r"citation_hooks[/\\]", re.I)
# His 14 Nov 2026 order (23:34): credit the mathematicians in the development, writing and acknowledgment phases.
DEVELOP_CMD = re.compile(r"(?:py|python)\S*\s+(?:-\S+\s+)*\S*problem_recall\.py", re.I)
TEX_DEVELOP = re.compile(r"\\begin\{(?:theorem|lemma|proposition|corollary|proof|conjecture)\*?\}", re.I)
TEX_WRITING = re.compile(r"\\begin\{abstract\}|\\section\*?\{\s*(?:Introduction|Background|Main results|"
                         r"Related work|Prior work)", re.I)
TEX_CREDIT = re.compile(r"acknowledg|AI declaration|declaration of (?:AI|generative)|use of (?:AI|artificial "
                        r"intelligence|generative)|\\section\*?\{\s*Declarations?\b", re.I)
PROMPT_PUB = re.compile(r"(?:publish|post|upload|push|submit|put)\w*\b.{0,80}\b(?:papers?|preprints?|manuscripts?)\b|"
                        r"\b(?:papers?|preprints?)\b.{0,60}\b(?:publish|post|upload|submit)\w*|zenodo|zendo|zendono|"
                        r"researchgate|researchgat", re.I)


def _win(p):
    p = os.path.expanduser(p.strip("\"'"))
    if re.match(r"^/[a-zA-Z]/", p):
        p = p[1].upper() + ":" + p[2:]
    return p


def _dir_has_paper(d):
    """A folder (or its paper/ subfolder) holds a .tex that starts a document. Top level only: cheap on every push."""
    for base in (d, os.path.join(d, "paper"), os.path.join(d, "papers")):
        try:
            names = os.listdir(base)
        except OSError:
            continue
        for n in names[:200]:
            if n.lower().endswith(".tex"):
                try:
                    with open(os.path.join(base, n), encoding="utf-8", errors="replace") as fh:
                        if "\\documentclass" in fh.read(4000):
                            return True
                except OSError:
                    pass
    return False


def _str(x):
    if x is None:
        return ""
    if isinstance(x, str):
        return x
    try:
        return json.dumps(x, ensure_ascii=False)
    except Exception:  # noqa: BLE001
        return str(x)


PROMPT_WHERE = re.compile(r"github|zenodo|zendo|zendono|researchgate|research gate|arxiv|\b[pe]\d{4}\b|\brepo\b", re.I)


def channels(p):
    ev = str(p.get("hook_event_name") or "")
    tool = str(p.get("tool_name") or "")
    ti = p.get("tool_input") or {}
    if not isinstance(ti, dict):
        ti = {"x": _str(ti)}
    ch = set()
    if not tool and ev not in ("PreToolUse",):
        t = str(p.get("prompt") or "")
        if t.lstrip().startswith(("This session is being continued from a previous conversation", "Stop hook feedback:",
                                  "Loop tick", "<task-notification>")):
            return ch, ""
        if t.lstrip().lower().startswith(("/loop", "fire this every", "fire thsi every", "fire this evey")):
            return ch, ""  # his standing loop orders say "publish papers" without posting one (an agent, 07:40)
        # a publishing ask names where it goes or which paper: a bare "publish papers" in a long work list is not one
        if PROMPT_PUB.search(t) and PROMPT_WHERE.search(t):
            ch.add("prompt")
        return ch, t[:200]
    command = str(ti.get("command") or "")
    if tool in ("Bash", "PowerShell"):
        if DEVELOP_CMD.search(HEREDOC.sub(" ", command)):
            ch.add("develop")  # work on an open problem starts: the credit ledger starts here (his 14 Nov order)
            return ch, command[:200]
        if ABOUT.search(command):
            return ch, command[:200]
        if GIT_PUB.search(command):
            cds = CD.findall(command)
            d = _win(cds[-1]) if cds else str(p.get("cwd") or os.getcwd())
            # a heredoc body is text being written (a table row, a script), not what is pushed (an agent,
            # 11 Nov 08:2x: "final papers" in a board-row script fired all 14 on a brain-tasks-board push)
            bare = HEREDOC.sub(" ", command)
            if PAPERISH.search(bare) or PAPERISH.search(d.replace("\\", "/").split("/")[-1]) or _dir_has_paper(d):
                ch.add("github")
        if ZEN_ACT.search(command):
            ch.add("zenodo")
        if RG_ACT.search(command):
            ch.add("researchgate")
        return ch, command[:200]
    if tool.startswith("mcp__claude-in-chrome__") or tool.startswith("mcp__Claude_Browser__"):
        blob = json.dumps(ti, ensure_ascii=False).lower()
        if "zenodo.org" in blob:
            ch.add("zenodo")
        if "researchgate.net" in blob:
            ch.add("researchgate")
        return ch, blob[:200]
    if tool in ("Write", "Edit", "MultiEdit"):
        fp = str(ti.get("file_path") or "").replace("\\", "/")
        if "/citation_hooks/" in fp:
            return ch, fp
        body = str(ti.get("content") or ti.get("new_string") or "") + " " + _str(ti.get("edits"))
        if fp.lower().endswith(".bib") or (fp.lower().endswith(".tex") and re.search(
                r"\\cite\w*\{|\\bibitem|thebibliography|\\bibliography\{|\\addbibresource", body)):
            ch.add("draft")
        if fp.lower().endswith(".tex"):
            if TEX_DEVELOP.search(body):
                ch.add("develop")
            if TEX_WRITING.search(body):
                ch.add("writing")
            if TEX_CREDIT.search(body):
                ch.add("credit")
        return ch, fp
    return ch, ""


def load_hooks(folder=HERE):
    hooks = []
    for name in sorted(os.listdir(folder)):
        if not re.match(r"C\d\d_.*\.py$", name):
            continue
        try:
            spec = importlib.util.spec_from_file_location("cite_hook_" + name[:-3], os.path.join(folder, name))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            h = dict(mod.HOOK)
            h["check"] = getattr(mod, "check", None)
            hooks.append(h)
        except Exception as e:  # noqa: BLE001
            sys.stderr.write("[citation hooks] could not load %s: %s\n" % (name, e))
    return hooks


def decide(p, hooks, now=None, state=None):
    now = time.time() if now is None else now
    state = {} if state is None else state
    ch, text = channels(p)
    if not ch:
        return [], ch, text
    session = str(p.get("session_id") or p.get("sessionId") or "unknown")
    out = []
    for h in sorted(hooks, key=lambda h: h["id"]):
        if not ch.intersection(h["on"]):
            continue
        chk = h.get("check")
        if chk is not None:
            try:
                if not chk(ch, p):
                    continue
            except Exception:  # noqa: BLE001
                continue
        key = h["id"] + "|" + session
        last = state.get(key)
        if isinstance(last, (int, float)) and now - last < h.get("cool", 1800):
            continue
        state[key] = now
        out.append(h)
    # The banner only ever prints with at least one checklist line under it, and never alone.
    if out and all(h.get("massive") for h in out):
        out = []
    return out, ch, text


def render(hooks, ch):
    pub = sorted(ch.intersection(PUBLISH))
    lines = []
    big = [h for h in hooks if h.get("massive")]
    if big:
        h = big[0]
        lines += [BANNER, "!!! [CITATIONS %s] %s - about to publish on %s" % (h["id"], h["title"].upper(),
                                                                          ", ".join(pub) or "the web"),
                  BANNER, h["rule"]]
    for h in hooks:
        if not h.get("massive"):
            lines.append("  [%s | %s] %s" % (h["id"], h["title"], h["rule"]))
    if big:
        lines.append(BANNER)
    return "\n".join(lines)


def _state_path(session):
    return os.path.join(STATE_DIR, re.sub(r"[^\w.-]", "_", session)[:80] + ".json")


def _load_state(session):
    try:
        with open(_state_path(session), encoding="utf-8") as f:
            d = json.load(f)
        return d if isinstance(d, dict) else {}
    except Exception:  # noqa: BLE001
        return {}


def _save_state(session, d):
    try:
        os.makedirs(STATE_DIR, exist_ok=True)
        path = _state_path(session)
        tmp = path + ".%d.tmp" % os.getpid()
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(d, f)
        os.replace(tmp, path)
    except Exception:  # noqa: BLE001
        pass


def run_payload(raw):
    try:
        p = json.loads(raw or "{}")
    except Exception:  # noqa: BLE001
        return ""
    if not isinstance(p, dict):
        return ""
    if not channels(p)[0]:  # nearly every call: return before loading the 16 hook files
        return ""
    session = str(p.get("session_id") or p.get("sessionId") or "unknown")
    hooks = load_hooks()
    st = _load_state(session)  # one state file per session: concurrent sessions never overwrite each other
    fired, ch, text = decide(p, hooks, state=st)
    if not fired:
        return ""
    _save_state(session, st)
    try:
        with open(FIRES, "a", encoding="utf-8") as f:
            f.write(json.dumps({"t": time.strftime("%Y-%m-%dT%H:%M:%S"), "session": session, "channels": sorted(ch),
                                "ids": [h["id"] for h in fired], "text": text[:160]}, ensure_ascii=False) + "\n")
    except Exception:  # noqa: BLE001
        pass
    head = ("[citation hooks] %d of the %d citation hooks fired (his order 11 Nov: every relevant source is cited before "
            "a paper goes to GitHub, ResearchGate or Zenodo; 14 Nov: the introduction and the AI declaration credit the "
            "mathematicians whose work matters most and say what was known, what is new and how they relate). "
            "Do each check now, not after the upload. "
            "List: python ~/.claude/dreaming/citation_hooks/cite_hooks_run.py --list"
            % (len(fired), len(hooks)))
    return head + "\n" + render(fired, ch)
