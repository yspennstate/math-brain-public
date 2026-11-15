"""codex_hook_dispatch.py - run every Codex hook of one event in ONE python process instead of one process per hook.

WHY (measured 11 Nov 2026 on MATH-ROSS20): both Codex homes on the laptop carry 46 hook commands and no dispatcher:
27 python starts on every prompt, 9 before and 4 after every tool call, 6 at every stop, 42 of them with the user
site loaded (0.26-0.33 s a start that morning; 13 one after another 4.75 s). The 8 Nov brief workers managed 2
commands in 50 minutes with the hooks on against 3 in 6 minutes with them off. The Claude side has had one process
per event since 15 Sep (hook_dispatch.py); this file gives Codex the same, by importing that dispatcher as a module
and handing its dispatch() the Codex hook list. hook_dispatch.py itself is not changed.

WIRING (a changed hook command line needs the author's /hooks review in each Codex home; trust hashes are never
forged): one line per event in hooks.json,
    C:\\Python314\\python.exe -s -B ~\\.claude\\dreaming\\codex_hook_dispatch.py --event <Event>
and the list those lines replace is kept in codex_hook_dispatch_list.json, written by make_codex_hook_list.py from
the hooks.json it replaces, in the shape hook_dispatch.hook_entries reads ({"hooks": {event: [blocks]}}).

WHAT DIFFERS FROM THE CLAUDE SIDE, all of it in this file:
  - Codex takes JSON only. A hook's plain-text stdout is discarded by Codex today, so it is dropped here as well
    (logged with the hook's name) and never turned into context: the merged answer holds what the 46 lines gave.
  - A hook runs in this process only when codex_hook_dispatch_allow.json names it AND the file is unchanged since
    (size and mtime recorded there by test_codex_dispatch.py, which proved it under its Codex arguments and a Codex
    payload). Every other hook runs as its own process with its own unchanged command line. The Claude allowlist is
    not used: it was proven for other arguments.
  - The hooks that run as their own process are started together on every event, tool events included.
  - Own log (compute/codex_hook_dispatch.log), own code cache folder, no profile sampling, no envelope handling.
  - FALLBACK: when hook_dispatch cannot be imported or raises, every entry of the list is run as its own process,
    one after another, and their answers are merged here with nothing but the standard library.
  - TWO LINES ON A PROMPT. Codex cuts what one hook command hands it at about 10,000 chars, and on a session's
    first prompt the hooks write more than that (10,493 chars measured 11 Nov without the inbox and the
    checklist). So the four hooks with the largest standing blocks have their own list and their own line,
    `--event UserPromptSubmit --list <the second list>`; each line has the whole 9,800. A guard's deny, a
    block and an exit 2 survive that path. A list that cannot be read is said once, in the session.

EXIT: 0 with one JSON object or nothing on stdout; 2 with the blocking hook's stderr when a hook exited 2.
"""
import json
import os
import sys
import time

HD_DIR = os.environ.get("CODEX_HOOK_DISPATCH_HD_DIR") or r"~\.claude\dreaming"
LIST = os.environ.get("CODEX_HOOK_DISPATCH_LIST") or os.path.join(HD_DIR, "codex_hook_dispatch_list.json")
ALLOW = os.environ.get("CODEX_HOOK_DISPATCH_ALLOW") or os.path.join(HD_DIR, "codex_hook_dispatch_allow.json")
LOG = os.environ.get("CODEX_HOOK_DISPATCH_LOG") or r"~\.claude\compute\codex_hook_dispatch.log"
CODE_DIR = os.environ.get("CODEX_HOOK_DISPATCH_CODE_DIR") or os.path.join(HD_DIR, "__pycache__", "codex")
CREATE_NO_WINDOW = 0x08000000 if os.name == "nt" else 0
CONTEXT_CAP = 9800
FALLBACK_BUDGET_S = 120.0
RANK = {"allow": 0, "ask": 1, "deny": 2}
SELF = "codex_hook_dispatch.py"


def _user_site_on_path():
    """This file starts with `python -s` (no user site: the start is about 0.1 s cheaper). Today's Codex hook lines
    start WITHOUT -s, so a hook may import a package that lives only in the user site (psutil does on this laptop).
    Such a hook, run inside this process, would fail on the import, and a hook that fails open would then stop
    guarding without a word (11 Nov, running_script_edit_guard.py). So the user site directory goes on the END of
    sys.path: its packages import, nothing in it runs at start, and anything the standard places hold wins."""
    try:
        import site
        us = site.getusersitepackages()
        if us and os.path.isdir(us) and us not in sys.path:
            sys.path.append(us)
    except Exception:
        pass


_user_site_on_path()


def log(s):
    try:
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S") + "  " + s + "\n")
    except Exception:
        pass


def _exc_line():
    et, ev = sys.exc_info()[:2]
    try:
        import traceback
        txt = traceback.format_exc().strip().replace("\n", " | ")
    except Exception:
        txt = "%s: %s" % (getattr(et, "__name__", "Exception"), ev)
    return txt if len(txt) <= 700 else txt[:300] + " ... " + txt[-380:]


def _json_object(text):
    """The dict a hook printed, or None: Codex reads a hook's stdout only when it is one JSON object."""
    t = (text or "").strip()
    if not t.startswith("{"):
        return None
    try:
        obj = json.loads(t)
    except Exception:
        return None
    return obj if isinstance(obj, dict) else None


def json_only(results):
    """results as merge() takes them, with every stdout that is not one JSON object emptied. Returns (kept, dropped)
    where dropped is [(label, chars)]. A hook's exit code and stderr are never touched."""
    kept, dropped = [], []
    for label, rc, out, err in results:
        if (out or "").strip() and _json_object(out) is None:
            dropped.append((label, len(out)))
            out = ""
        kept.append((label, rc, out, err))
    return kept, dropped


def allowed_names(allow_path=None, dispatcher_file=None):
    """Lower-case basenames that may run in this process: named in the allow file, proven against the dispatcher
    that is on disk now (the allow file is not older than it) and unchanged since their proof. Never raises."""
    try:
        allow_path = allow_path or ALLOW
        with open(allow_path, encoding="utf-8") as f:
            d = json.load(f)
        if dispatcher_file and os.path.getmtime(allow_path) < os.path.getmtime(dispatcher_file):
            return set(), "stale"
        names, changed = set(), []
        for name, rec in (d.get("in_process_ok") or {}).items():
            try:
                st = os.stat(rec["path"])
                if st.st_size == rec["size"] and st.st_mtime_ns == rec["mtime_ns"]:
                    names.add(str(name).lower())
                else:
                    changed.append(str(name))
            except Exception:
                changed.append(str(name))
        return names, ("changed since their proof, own process until proven again: " + ", ".join(sorted(changed))
                       if changed else "")
    except Exception:
        return set(), "unreadable"


def via_hook_dispatch(event, payload, hook):
    """(code, out, err) from hook_dispatch.dispatch() on the Codex list. Raises when that module cannot do it."""
    if HD_DIR not in sys.path:
        sys.path.insert(0, HD_DIR)
    import hook_dispatch as HD
    HD.LOG = LOG
    HD.PROFILE_FLAG = os.path.join(HD_DIR, "codex_hook_profile.never")      # no sampling into the Claude profile
    HD._CODE_DIR = CODE_DIR
    HD.PARALLEL_SUBPROC_EVENTS = set(HD.PARALLEL_SUBPROC_EVENTS) | {"PreToolUse", "PostToolUse"}
    os.environ["HOOK_DISPATCH_ENVELOPE"] = "0"
    names, why = allowed_names(dispatcher_file=getattr(HD, "__file__", None))
    if why in ("stale", "unreadable"):
        log("%s allow file %s: every hook runs as its own process" % (event, why))
    elif why:
        log("%s %s" % (event, why))
    HD._allowlist = lambda: set(names)
    base_merge = HD.merge

    def merge(results, ev, session=""):
        kept, dropped = json_only(results)
        if dropped:
            log("%s plain text dropped (Codex takes JSON only): %s"
                % (ev, ", ".join("%s %d chars" % x for x in dropped)))
        return base_merge(kept, ev, session)

    HD.merge = merge
    try:
        HD._unthrottle()
    except Exception:
        pass
    with open(LIST, encoding="utf-8") as f:
        json.load(f)                     # an unreadable list is this file's to report, not a silent zero hooks
    code, out, err, _ = HD.dispatch(event, payload, str(hook.get("tool_name") or ""), settings_path=LIST,
                                    session=str(hook.get("session_id") or ""))
    if out and _json_object(out) is None:
        log("%s merged output was not a JSON object, dropped: %d chars" % (event, len(out)))
        out = ""
    return code, out, err


def _matches(matcher, tool):
    if not matcher or matcher == "*":
        return True
    try:
        import re
        if re.fullmatch(r"[A-Za-z0-9_|, -]+", matcher):
            return tool in {n.strip() for n in re.split(r"[|,]", matcher)}
        return re.search(matcher, tool) is not None
    except Exception:
        return True                      # in doubt the hook runs


def fallback(event, payload, hook):
    """Every entry as its own process, one after another; a small merge. Used only when hook_dispatch failed."""
    import subprocess
    with open(LIST, encoding="utf-8") as f:
        blocks = (json.load(f).get("hooks") or {}).get(event, [])
    tool = str(hook.get("tool_name") or "")
    data = payload.encode("utf-8", "surrogateescape")
    results = []
    for block in blocks:
        if event in ("PreToolUse", "PostToolUse") and not _matches(block.get("matcher"), tool):
            continue
        for h in block.get("hooks", []):
            cmd, args = h.get("command", ""), [str(a) for a in (h.get("args") or [])]
            if SELF in (cmd + " " + " ".join(args)).lower():
                continue
            flag = h.get("enabled_if")
            if isinstance(flag, str) and flag.strip() and not os.path.exists(os.path.expanduser(flag.strip())):
                continue
            label = next((os.path.basename(a) for a in [cmd] + args if a.lower().endswith(".py")), cmd[:40])
            try:
                budget = min(float(h.get("timeout") or FALLBACK_BUDGET_S), FALLBACK_BUDGET_S)
                p = subprocess.run([cmd] + args if args else cmd, shell=not args, input=data, capture_output=True,
                                   timeout=budget, creationflags=CREATE_NO_WINDOW)
                results.append((label, p.returncode, (p.stdout or b"").decode("utf-8", "replace"),
                                (p.stderr or b"").decode("utf-8", "replace")))
            except Exception as e:
                results.append((label, 1, "", "codex_hook_dispatch fallback: %r" % (e,)))
    return plain_merge(results, event)


def plain_merge(results, event):
    """(code, out, err) with nothing but json: exit 2 blocks; deny over ask over allow; a top-level block or stop is
    kept; contexts are joined in list order and cut at CONTEXT_CAP. Plain-text stdout is dropped."""
    vetoes = [(err or "").strip() or ("%s blocked" % label) for label, rc, out, err in results if rc == 2]
    if vetoes:
        return 2, "", "\n".join(vetoes)
    contexts, decision, reason, top = [], None, None, {}
    for label, rc, out, err in results:
        obj = _json_object(out)
        if obj is None:
            continue
        h = obj.get("hookSpecificOutput")
        h = h if isinstance(h, dict) else {}
        c = h.get("additionalContext")
        if c:
            contexts.append(c if isinstance(c, str) else json.dumps(c))
        d = h.get("permissionDecision")
        if isinstance(d, str) and d in RANK and (decision is None or RANK[d] > RANK[decision]):
            decision, reason = d, h.get("permissionDecisionReason")
        if obj.get("decision") == "block" and "decision" not in top:
            top["decision"], top["reason"] = "block", str(obj.get("reason") or "%s blocked" % label)
        if obj.get("continue") is False and "continue" not in top:
            top["continue"], top["stopReason"] = False, str(obj.get("stopReason") or "%s stopped" % label)
        if obj.get("systemMessage") and "systemMessage" not in top:
            top["systemMessage"] = obj["systemMessage"]
    out = dict(top)
    hso = {"hookEventName": event}
    if contexts and event not in ("Stop", "SubagentStop"):
        text = "\n\n".join(contexts)
        if len(text) > CONTEXT_CAP:
            text = text[:CONTEXT_CAP - 60] + "\n[cut: the hooks wrote %d chars]" % len(text)
        hso["additionalContext"] = text
    if decision:
        hso["permissionDecision"] = decision
        if reason:
            hso["permissionDecisionReason"] = reason
    if len(hso) > 1:
        out["hookSpecificOutput"] = hso
    return 0, (json.dumps(out) if out else ""), ""


def _write(stream, text):
    buf = getattr(stream, "buffer", None)
    if buf is not None:
        buf.write(text.encode("utf-8", "replace"))
        buf.flush()
    else:
        stream.write(text)
        stream.flush()


def main():
    global LIST, CODE_DIR
    t0 = time.perf_counter()
    if "--list" in sys.argv[1:-1]:
        LIST = sys.argv[sys.argv.index("--list") + 1]
        CODE_DIR = CODE_DIR + "_" + os.path.splitext(os.path.basename(LIST))[0][-24:]
    try:
        buf = getattr(sys.stdin, "buffer", None)
        raw = buf.read().decode("utf-8", "replace") if buf is not None else sys.stdin.read()
    except Exception:
        raw = ""
    i = raw.find("{")
    payload = raw[i:] if i >= 0 else "{}"
    try:
        hook = json.loads(payload)
        if not isinstance(hook, dict):
            hook = {}
    except Exception:
        hook = {}
    event = str(hook.get("hook_event_name") or hook.get("event_name") or "")
    if not event and "--event" in sys.argv[1:-1]:
        event = sys.argv[sys.argv.index("--event") + 1]
    if not event:
        log("no event name in the payload or the arguments: nothing run")
        return 0
    real_out, real_err = sys.stdout, sys.stderr
    try:
        code, out, err = via_hook_dispatch(event, payload, hook)
    except BaseException:
        sys.stdout, sys.stderr = real_out, real_err
        log("%s fatal in hook_dispatch, running every hook as its own process: %s" % (event, _exc_line()))
        try:
            code, out, err = fallback(event, payload, hook)
            log("%s fallback done exit=%d out=%d %.2fs" % (event, code, len(out), time.perf_counter() - t0))
        except BaseException:
            log("%s fallback failed, no hook ran: %s" % (event, _exc_line()))
            code, err = 0, ""
            out = json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext":
                              "[codex-hook-dispatch] the hook list could not be read or run, so NO hook ran for "
                              "this event. The session is unharmed and unhooked; see " + LOG}}) \
                if event not in ("Stop", "SubagentStop") else ""
    if out:
        _write(real_out, out)
    if err:
        _write(real_err, err)
    return code


if __name__ == "__main__":
    try:
        _rc = main()
    except BaseException:
        log("fatal outside main: " + _exc_line())
        _rc = 0                          # a broken dispatcher must never block a tool call
    sys.exit(_rc)
