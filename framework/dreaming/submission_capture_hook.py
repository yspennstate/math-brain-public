#!/usr/bin/env python3
"""submission_capture_hook.py - a paper sent to a journal gets its row in the submissions record the same turn.

The record and its refusals live in submissions.py beside this hook (one paper at one journal at a time, never the
same journal twice). This hook does the capture:

  S1  PostToolUse on a Chrome tool: the page shows a submission confirmation ("successfully submitted", "submission
      received", "manuscript number", ...) on a journal submission site -> says, now, to record it with
      submissions.py add (paper, journal, id), and marks this session as owing a row.
  S2  PostToolUse on Bash/PowerShell running submissions.py add/status -> the debt is paid.
  S3  Stop: a session that saw a confirmation and recorded nothing is held once with the exact command.

The site test reads the active page's URL, never the page text, so reading a journal's email in a webmail tab does
not fire it. State per session in .submission_capture/<session>.json beside this file. Never blocks a tool call;
any error is silent.
  python submission_capture_hook.py --selftest
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SD = os.path.join(HERE, ".submission_capture")
TOOL = (sys.executable or "python") + " " + os.path.join(HERE, "submissions.py").replace("\\", "/")
CONFIRM = re.compile(r"(?i)(successfully submitted|submission (?:has been |was )?(?:received|completed|complete|confirmed)|"
                     r"thank you for (?:your )?submi(?:tting|ssion)|manuscript (?:number|id) (?:is|has been assigned)|"
                     r"your manuscript has been (?:submitted|received)|submission confirmation|"
                     r"your submission (?:has been|was) (?:successfully )?(?:received|submitted))")
JOURNAL_SITE = re.compile(r"(?i)(editorialmanager\.com|manuscriptcentral\.com|mc\.manuscriptcentral|scholarone|"
                          r"submission\.springernature|editorialmanager|ejournalpress|jmlr\.org|elsevier\.com/.*submi|"
                          r"tandfonline\.com/.*submi|wiley\.com/.*submi|editflow|e-publications\.org)")
WEBMAIL = re.compile(r"(?i)//(mail\.google\.|outlook\.(?:live|office)\.|mail\.yahoo\.)")
RECORDED = re.compile(r"submissions\.py\s+(add|status)\b")


def state_path(sid):
    return os.path.join(SD, re.sub(r"[^A-Za-z0-9_-]", "_", sid or "nosession") + ".json")


def load(sid):
    try:
        return json.load(open(state_path(sid), encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return {"owed": [], "reminded": False}


def save(sid, st):
    os.makedirs(SD, exist_ok=True)
    json.dump(st, open(state_path(sid), "w", encoding="utf-8"))


def page_url(ev, text):
    """The URL of the page this Chrome result is about: get_page_text's 'URL:' line, a navigate's url, or the
    executing tab in the Tab Context block. '' when the result names none (a screenshot, a click)."""
    m = re.search(r"URL: (https?://[^\s\"\\]+)", text)
    if m:
        return m.group(1)
    u = (ev.get("tool_input") or {}).get("url") if isinstance(ev.get("tool_input"), dict) else None
    if u and str(u).startswith("http"):
        return str(u)
    t = re.search(r"Executed on tabId: (\d+)", text)
    if t:
        m = re.search(r"tabId %s[^\n]*?(https?://[^\s\"\\)]+)" % t.group(1), text.replace("\\n", "\n"))
        if m:
            return m.group(1)
    return ""


def handle(ev):
    name = ev.get("hook_event_name", "")
    sid = ev.get("session_id", "")
    tool = ev.get("tool_name", "") or ""
    if name == "PostToolUse":
        if tool.startswith("mcp__claude-in-chrome__"):
            text = json.dumps(ev.get("tool_response", ""), ensure_ascii=False)[:200000]
            url = page_url(ev, text)
            st = load(sid)
            if url:
                st["url"] = url
                save(sid, st)
            url = url or st.get("url", "")
            m = CONFIRM.search(text)
            if m and JOURNAL_SITE.search(url) and not WEBMAIL.search(url):
                st["owed"].append(m.group(0)[:80])
                save(sid, st)
                msg = ("[submissions S1] This page reads as a journal submission confirmation (\"%s\"). Record it now, "
                       "before anything else: %s add --title \"<exact title>\" --journal \"<journal>\" --id <manuscript id> "
                       "--date <today> --agent <you>  (the record keeps a paper from going to the same place twice)."
                       % (m.group(0)[:60], TOOL))
                return msg, None
        elif tool in ("Bash", "PowerShell"):
            cmd = json.dumps(ev.get("tool_input", ""), ensure_ascii=False)
            if RECORDED.search(cmd):
                st = load(sid)
                if st["owed"]:
                    st["owed"] = []
                    save(sid, st)
        return None, None
    if name == "Stop":
        if ev.get("stop_hook_active"):
            return None, None
        st = load(sid)
        if st["owed"] and not st.get("reminded"):
            st["reminded"] = True
            save(sid, st)
            return None, ("[submissions S3] This session saw a journal confirm a submission (\"%s\") and no row was "
                          "recorded. Before you stop: %s check \"<title>\" then %s add --title ... --journal ... --id ..."
                          % (st["owed"][-1], TOOL, TOOL))
    return None, None


def main():
    try:
        ev = json.loads(sys.stdin.read() or "{}")
    except Exception:  # noqa: BLE001
        return 0
    try:
        ctx, block = handle(ev)
    except Exception:  # noqa: BLE001
        return 0
    if block:
        print(json.dumps({"decision": "block", "reason": block}))
    elif ctx:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": ev.get("hook_event_name"), "additionalContext": ctx}}))
    return 0


def selftest():
    global SD
    import tempfile
    SD = tempfile.mkdtemp()
    ok = 0
    page = {"hook_event_name": "PostToolUse", "session_id": "t1", "tool_name": "mcp__claude-in-chrome__get_page_text",
            "tool_input": {"tabId": 1}, "tool_response": "Title: Submission\nURL: https://www.editorialmanager.com/journal/x\n"
            "Thank you for submitting your manuscript. Your submission has been received."}
    c, b = handle(page)
    ok += bool(c and "S1" in c and not b); print("S1 fires on a confirmation page:", bool(c))
    c, b = handle(dict(page, session_id="t2", tool_response="https://news.example.com Thank you for your submission to our newsletter"))
    ok += c is None; print("S1 silent off a journal site:", c is None)
    c, b = handle({"hook_event_name": "Stop", "session_id": "t1"})
    ok += bool(b and "S3" in b); print("S3 holds a stop with a debt:", bool(b))
    c, b = handle({"hook_event_name": "Stop", "session_id": "t1"})
    ok += b is None; print("S3 holds only once:", b is None)
    handle(page)
    handle({"hook_event_name": "PostToolUse", "session_id": "t1", "tool_name": "Bash",
            "tool_input": {"command": "python .../submissions.py add --title X --journal Y"}})
    st = load("t1")
    ok += st["owed"] == []; print("S2 clears the debt on submissions.py add:", st["owed"] == [])
    c, b = handle({"hook_event_name": "Stop", "session_id": "t3"})
    ok += b is None; print("S3 silent with no debt:", b is None)
    c, b = handle(dict(page, session_id="t4", tool_response="Title: Editor's decision - Inbox\nURL: https://mail.google.com/mail/u/0/#inbox\n"
                       "Submission Confirmation ... ScholarOne ... editorialmanager.com"))
    ok += c is None; print("S1 silent on a journal mail read in webmail:", c is None)
    handle({"hook_event_name": "PostToolUse", "session_id": "t5", "tool_name": "mcp__claude-in-chrome__navigate",
            "tool_input": {"url": "https://mc.manuscriptcentral.com/somejournal"}, "tool_response": "Navigated"})
    c, b = handle({"hook_event_name": "PostToolUse", "session_id": "t5", "tool_name": "mcp__claude-in-chrome__computer",
                   "tool_input": {"action": "screenshot"}, "tool_response": "Your manuscript has been submitted. Thank you for submitting"})
    ok += bool(c); print("S1 uses the last navigated URL when a result names none:", bool(c))
    print("%d/8 pass" % ok)
    return 0 if ok == 8 else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(main())
